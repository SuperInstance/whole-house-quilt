"""SCAFFOLD - whole-house quilt reference model (floor).

A small, readable model of the room / tick / ledger loop described in
docs/seeds.md (§20-§22) and protocols/. Standard library only. This is a
reference for the *shapes*, not the system: no networking, no GPU, no real
models. The dice are honest stubs; the residents are scripts.

Run the demo:   python3 quilt_floor.py
Run the tests:  python3 -m unittest test_quilt_floor.py -v   (from floor/)
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum


class Persistence(Enum):
    """plato-ghostable's classes: what survives a restart / a night / a rebuild."""

    ETERNAL = "eternal"
    PERSISTENT = "persistent"
    EPHEMERAL = "ephemeral"


@dataclass(frozen=True)
class Entry:
    """One ledger entry: an agreed send or receive. Frozen on purpose."""

    seq: int
    tick: int
    kind: str  # "send" | "receive"
    frm: str
    to: str
    what: str  # tick | order | request | roll | refusal | note
    payload: dict


class Ledger:
    """Append-only record of sends and receives (seeds §12).

    There is deliberately no remove/replace API, and entries are exposed
    only as an immutable tuple of frozen entries, so tests (and readers)
    can rely on history never being rewritten.
    """

    def __init__(self) -> None:
        self._entries: list[Entry] = []

    def append(self, tick: int, kind: str, frm: str, to: str, what: str, payload: dict) -> Entry:
        entry = Entry(seq=len(self._entries), tick=tick, kind=kind, frm=frm, to=to, what=what, payload=dict(payload))
        self._entries.append(entry)
        return entry

    @property
    def entries(self) -> tuple[Entry, ...]:
        return tuple(self._entries)

    def __len__(self) -> int:
        return len(self._entries)


class Dice:
    """Decision models are the dice (§22): a probability for every option.

    The stub rolls against a fixed table - weights authored 'up the stack',
    rolled here, in the room. A production die is a trained decision model;
    its interface is this one.
    """

    def __init__(self, table: str, weights: dict[str, float], rng: random.Random) -> None:
        total = sum(weights.values())
        if total <= 0:
            raise ValueError("dice weights must sum to a positive number")
        self.table = table
        self.weights = {k: w / total for k, w in weights.items()}
        self._rng = rng

    def roll(self) -> dict:
        r = self._rng.random()
        acc = 0.0
        picked = next(iter(self.weights))
        for option, p in self.weights.items():
            acc += p
            if r <= acc:
                picked = option
                break
        return {"table": self.table, "options": dict(self.weights), "picked": picked}


@dataclass
class Resident:
    """A stationed bot (§20): it lives in its room; it does not travel."""

    id: str
    role: str
    model: str = "script"

    def act(self, room: "Room", tick: int) -> None:
        """One tick of the resident's work. The base resident does nothing."""


@dataclass
class EngineWatcher(Resident):
    """Script resident: random-walk the gauges, staying near nominal."""

    rng: random.Random = field(default_factory=lambda: random.Random(7))

    def act(self, room: "Room", tick: int) -> None:
        s = room.state
        s["rpm"] += self.rng.choice([-6, -3, 0, 3, 6])
        s["coolant_c"] += self.rng.choice([-0.4, 0.0, 0.4])
        s["oil_psi"] += self.rng.choice([-0.5, 0.0, 0.5])


@dataclass
class Navigator(Resident):
    """Resident with dice: hold or correct against the cross-track table."""

    dice: Dice | None = None

    def act(self, room: "Room", tick: int) -> None:
        s = room.state
        s["xte_m"] += s.get("drift_m", 2.0)
        if self.dice is not None and abs(s["xte_m"]) > 10:
            result = self.dice.roll()
            room.pending_rolls.append(result)
            if result["picked"] == "correct-port":
                s["xte_m"] -= 8
            elif result["picked"] == "correct-starboard":
                s["xte_m"] += 8


@dataclass
class Room:
    id: str
    name: str
    state: dict = field(default_factory=dict)
    deadband: dict[str, tuple[float, float]] = field(default_factory=dict)
    heartbeat_every: int = 5
    persistence: Persistence = Persistence.PERSISTENT
    residents: list[Resident] = field(default_factory=list)
    pending_rolls: list[dict] = field(default_factory=list)
    _last_console_values: dict = field(default_factory=dict)

    def _outside_deadband(self) -> dict:
        out = {}
        for key, (lo, hi) in self.deadband.items():
            if key in self.state and not (lo <= self.state[key] <= hi):
                out[key] = self.state[key]
        return out

    def console_tick(self, tick: int) -> dict | None:
        """What the console hears (§20): change outside the deadband, or a
        heartbeat on schedule. Otherwise silence - and silence is data."""
        changed = {
            k: v
            for k, v in self._outside_deadband().items()
            if self._last_console_values.get(k) != v
        }
        if changed:
            self._last_console_values.update(changed)
            return {"kind": "change", "room": self.id, "to": "console", "tick": tick, "values": changed}
        if self.heartbeat_every and tick % self.heartbeat_every == 0:
            return {"kind": "heartbeat", "room": self.id, "to": "console", "tick": tick}
        return None

    def readout_tick(self, tick: int) -> dict:
        """What someone standing in the room hears: everything, every tick."""
        return {"kind": "readout", "room": self.id, "to": "in-room", "tick": tick, "values": dict(self.state)}


class World:
    """Rooms + ledger + clock. `step` is one tick of the whole house."""

    def __init__(self, rooms: list[Room]) -> None:
        self.rooms = {r.id: r for r in rooms}
        self.ledger = Ledger()
        self.tick = 0

    def step(self) -> dict[str, dict | None]:
        self.tick += 1
        views: dict[str, dict | None] = {}
        for room in self.rooms.values():
            for resident in room.residents:
                resident.act(room, self.tick)
            for roll in room.pending_rolls:
                self.ledger.append(self.tick, "send", room.id, "dice", "roll", roll)
                self.ledger.append(self.tick, "receive", "dice", room.id, "roll", roll)
            room.pending_rolls.clear()
            views[room.id] = room.console_tick(self.tick)
            if views[room.id] is not None:
                self.ledger.append(self.tick, "send", room.id, "console", "tick", views[room.id])
        return views


def build_demo_world() -> World:
    rng = random.Random(42)
    engine = Room(
        id="engine-room",
        name="Engine Room",
        state={"rpm": 810, "coolant_c": 82.0, "oil_psi": 42.0},
        deadband={"rpm": (780, 840), "coolant_c": (78, 86), "oil_psi": (38, 46)},
        heartbeat_every=5,
        residents=[EngineWatcher(id="engine-watcher", role="watch gauges", model="jev-semantic")],
    )
    nav = Room(
        id="nav-room",
        name="Navigation Room",
        state={"heading_deg": 181.0, "xte_m": 0.0, "drift_m": 2.0},
        deadband={"heading_deg": (178, 184), "xte_m": (-15, 15)},
        heartbeat_every=5,
        residents=[
            Navigator(
                id="navigator",
                role="perceive position and heading; send helm orders",
                model="decision-table",
                dice=Dice(
                    "cross-track-correction",
                    {"hold": 0.62, "correct-port": 0.23, "correct-starboard": 0.11, "escalate": 0.04},
                    rng,
                ),
            )
        ],
    )
    return World([engine, nav])


def main() -> None:
    world = build_demo_world()
    print("Whole-house quilt - reference model demo (SCAFFOLD)")
    print("Console view = change-only + deadband heartbeat (§20).")
    print("Room view    = full readout, as if standing in the engine room.")
    print()
    for _ in range(12):
        views = world.step()
        t = world.tick
        readout = world.rooms["engine-room"].readout_tick(t)
        print(f"tick {t:2d} | ROOM (engine): rpm={readout['values']['rpm']:>4} "
              f"coolant={readout['values']['coolant_c']:.1f}C oil={readout['values']['oil_psi']:.1f}psi")
        for room_id, view in views.items():
            if view is None:
                print(f"tick {t:2d} | CONSOLE <- {room_id}: (silence - within deadband)")
            elif view["kind"] == "heartbeat":
                print(f"tick {t:2d} | CONSOLE <- {room_id}: HEARTBEAT - all within deadband, no errors")
            else:
                print(f"tick {t:2d} | CONSOLE <- {room_id}: CHANGE {view['values']}")
    print()
    print(f"Ledger: {len(world.ledger)} entries (append-only).")
    rolls = [e for e in world.ledger.entries if e.what == "roll" and e.kind == "send"]
    for e in rolls:
        print(f"  roll @tick {e.tick} from {e.frm}: table={e.payload['table']} picked={e.payload['picked']}")


if __name__ == "__main__":
    main()
