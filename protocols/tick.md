# Protocol: tick

*Seeds §20. SCAFFOLD.*

A **tick** is one unit of perception: what a room has to say, addressed to a
position. Ticks are not broadcast. The same room speaks at different
densities to different positions, and the tick carries its addressee so the
piping can route it without interpretation.

## Fields

- `kind` — `"readout"`, `"change"`, or `"heartbeat"`.
  - `readout`: full state density, for a position inside the room
    (diagnosis).
  - `change`: only what changed since the last tick to this addressee, and
    only when something crossed a bound (the console's normal tick).
  - `heartbeat`: the deadband tick — *everything within bounds, no errors* —
    emitted on the room's heartbeat interval even when nothing changed. A
    heartbeat that fails to arrive is itself the alarm.
- `room` — the emitting room's slug.
- `to` — the addressee: a position (`"console"`, `"in-room"`) or a cell slug.
- `tick` — the emitting room's logical tick count.
- `values` — for `readout` and `change`: a flat object of reading names to
  numbers or short strings. For `heartbeat`: empty or omitted.
- `bounds` — optional, on `heartbeat`: the deadband the room is certifying,
  as `{reading: [low, high]}`.

## Rules

- A room MUST emit a heartbeat every `heartbeat_every` ticks to each
  console-class addressee in its manifest, whether or not anything changed.
- A room MUST NOT emit `change` ticks for movement inside the deadband.
- `readout` ticks are emitted only to in-room positions, or on explicit
  request (a send/receive `request` with `what: "readout"`).
