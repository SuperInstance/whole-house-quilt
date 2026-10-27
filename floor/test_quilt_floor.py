"""SCAFFOLD tests for the reference model. Run from floor/:
    python3 -m unittest test_quilt_floor.py -v
"""

import unittest

from quilt_floor import Dice, Ledger, Room, World, build_demo_world
import random


class TestConsoleTicks(unittest.TestCase):
    def quiet_room(self) -> Room:
        return Room(
            id="engine-room",
            name="Engine Room",
            state={"rpm": 810},
            deadband={"rpm": (780, 840)},
            heartbeat_every=5,
        )

    def test_silence_within_deadband_between_heartbeats(self):
        room = self.quiet_room()
        heard = [room.console_tick(t) for t in range(1, 5)]
        self.assertEqual(heard, [None, None, None, None])

    def test_heartbeat_arrives_on_schedule(self):
        room = self.quiet_room()
        beat = room.console_tick(5)
        self.assertIsNotNone(beat)
        self.assertEqual(beat["kind"], "heartbeat")
        beat2 = room.console_tick(10)
        self.assertEqual(beat2["kind"], "heartbeat")

    def test_change_tick_only_outside_deadband(self):
        room = self.quiet_room()
        room.state["rpm"] = 900  # above the 840 bound
        view = room.console_tick(1)
        self.assertEqual(view["kind"], "change")
        self.assertEqual(view["values"], {"rpm": 900})
        # same out-of-band value again: no repeat change tick
        self.assertIsNone(room.console_tick(2))

    def test_readout_is_full_density(self):
        room = self.quiet_room()
        view = room.readout_tick(3)
        self.assertEqual(view["kind"], "readout")
        self.assertEqual(view["values"], {"rpm": 810})


class TestLedger(unittest.TestCase):
    def test_append_only(self):
        ledger = Ledger()
        ledger.append(1, "send", "a", "b", "note", {"x": 1})
        ledger.append(1, "receive", "b", "a", "note", {"x": 1})
        entries = ledger.entries
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0].seq, 0)
        self.assertEqual(entries[1].seq, 1)
        # entries are exposed as an immutable tuple of frozen entries
        with self.assertRaises(AttributeError):
            entries.append(entries[0])  # type: ignore[attr-defined]
        with self.assertRaises(Exception):
            entries[0].what = "roll"  # frozen dataclass
        # and the ledger offers no removal API at all
        self.assertFalse(hasattr(ledger, "remove"))
        self.assertFalse(hasattr(ledger, "pop"))
        self.assertFalse(hasattr(ledger, "clear"))


class TestDice(unittest.TestCase):
    def test_roll_returns_probability_per_option(self):
        dice = Dice("t", {"a": 2.0, "b": 1.0, "c": 1.0}, random.Random(1))
        result = dice.roll()
        self.assertAlmostEqual(sum(result["options"].values()), 1.0)
        self.assertIn(result["picked"], result["options"])
        self.assertEqual(result["table"], "t")


class TestDemoWorld(unittest.TestCase):
    def test_demo_world_runs_and_logs(self):
        world = build_demo_world()
        for _ in range(12):
            world.step()
        self.assertEqual(world.tick, 12)
        self.assertGreater(len(world.ledger), 0)
        kinds = {e.kind for e in world.ledger.entries}
        self.assertIn("send", kinds)


if __name__ == "__main__":
    unittest.main()
