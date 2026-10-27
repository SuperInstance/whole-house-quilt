# Protocol: room manifest

*Seeds §12, §20. SCAFFOLD. Shape based on vessel-room-navigator's
`rooms-config.json` (startRoom + rooms map with id/name/type/description/
adjacent/warp), extended with the quilt's own fields: tick policy, residents,
dice, and persistence.*

The manifest is the registry's light half (§11): identities, positions,
states, policies — small even for a rich world, while the heavy files stay
where they were made. One manifest describes a whole house of rooms.

## Fields

- `startRoom` — where a visitor enters.
- `rooms` — a map of slug → room:
  - `id`, `name`, `type` (`physical`, `virtual`, `composite` — the
    navigator's own vocabulary), `description`.
  - `adjacent` (walkable) and `warp` (jumpable) edges to other room slugs.
  - `anchor` — the room's placement agreement (§12): `relativeTo` (another
    room or object slug), `origin` ([x, y, z]), `facing` (degrees). The
    relative placement *is* the shared state; absolute coordinates are a
    projection.
  - `tickPolicy` — `readoutTo` (positions that receive full readouts),
    `consoleTo` (positions that receive change + heartbeat), and
    `heartbeatEvery` (ticks between deadband heartbeats).
  - `deadband` — `{reading: [low, high]}`: inside these bounds, the console
    hears nothing but heartbeats.
  - `residents` — stationed bots: `id`, `role`, `model` (what, if anything,
    is inside the NPC — `"script"`, a decision-model name, or a model
    budget line; residents are stationed, never itinerant).
  - `dice` — the tables this room's actions roll against (§22): `table`
    name, `options`, and `escalatesOn` (the option that wakes a bigger
    mind).
  - `persistence` — `eternal`, `persistent`, or `ephemeral`
    (plato-ghostable's classes): what of this room survives a restart, a
    night, a rebuild.
