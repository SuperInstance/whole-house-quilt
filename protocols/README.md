# Protocols

SCAFFOLD — first concrete shapes, written 2026-10-27 from seeds §20–§22.
These are the text protocols of the whole-house quilt: the piping every cell
speaks. They are deliberately small, JSON-shaped, and type-checked: parsing
must stay mechanical (§21), so a tiny watcher can grab a room's traffic at
speed without a model interpreting it. Malformed messages are rejected by
the schema, never "understood" charitably.

| Protocol | Spec | Schema | Example |
|---|---|---|---|
| Tick — what a room perceives, addressed to a position | [tick.md](tick.md) | [tick.schema.json](tick.schema.json) | [tick.example.json](tick.example.json) |
| Send/Receive — the ledger's unit of agreement | [send-receive.md](send-receive.md) | [send-receive.schema.json](send-receive.schema.json) | [send-receive.example.json](send-receive.example.json) |
| Room manifest — what a room is | [room-manifest.md](room-manifest.md) | [room-manifest.schema.json](room-manifest.schema.json) | [room-manifest.example.json](room-manifest.example.json) |

Common rules for all three:

- `v` is the protocol version (integer, currently `1`).
- Times are logical ticks (`tick`, a non-negative integer from the room's
  or the world's clock) — the quilt's shared clock is the tick count, not
  wall time; wall-clock timestamps, when needed, ride inside payloads.
- Identifiers are lowercase slugs (`engine-room`, `helm-orders`).
- A message that fails its schema is not delivered and not logged as
  delivered; the rejection itself is a ledger event under send/receive.
