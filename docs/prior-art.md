# Prior art — the inventory

*Casey's correction (seeds §25) is standing law for this project: the room
layer, the ledger, and much of the machinery described in this repository
are **existing fleet technology**, not reinventions. Any design that
greenfields what exists below is wrong by construction. Read this inventory
before designing anything "new". Sources: the vessel catalogue
(2026-10-10 digestion of ~35 vessel repos), the rack-synergy prior-art note
(2026-10-23), and the repo records themselves.*

## Rooms, vessels, and the boat

- **[terrain](https://github.com/SuperInstance/terrain)** — "MUD-to-Visual
  bridge — rooms as explorable scenes. Crabs stir the mud into walkable
  terrain." The general-purpose parent of the Mud-to-SCUMM line and of the
  staging ladder (seeds §26, §27). **Handling, per Casey: a NUGGET MINE.**
  Less mature than the projects below; read it for ideas, framings, and
  mechanisms worth lifting, verify anything before building on it, and do
  not treat its immaturity as a defect to fix in passing.
- **[vessel-room-navigator](https://github.com/SuperInstance/vessel-room-navigator)**
  — F/V EILEEN as nine navigable 3D rooms ("ScummVM meets Google Street
  View"); rooms as cells; the Unified Room Theory loop
  PROBE → DISCOVER → TEST → PICK → REMEMBER → WALK; alarms click-warp
  attention to the affected room — the addressed tick (seeds §20), built.
  Its `rooms-config.json` is the shape our room-manifest protocol
  ([`../protocols/`](../protocols/)) is based on.
- **[boat-agent](https://github.com/SuperInstance/boat-agent)** — the
  wheelhouse voice-mate. Design law: "the wheel is still yours, always" —
  a hand on the wheel outranks everything the agent thinks, every time.
  The go/no-go gate that no model needs to compute.
- **[vessel-agent-system](https://github.com/SuperInstance/vessel-agent-system)**
  (AELMA) — hardware-in-the-loop digital twin of F/V EILEEN: NMEA telemetry,
  deterministic safety watchers, plain-language narration, zero internet.
  Source of the BMAD stack (raw bits → physical tensors → features →
  operational intelligence → strategic knowledge) and the Non-Renewable
  Resource Principle: capture first, distil later; field data is
  irreplaceable, models are replaceable.
- **[vessel-template](https://github.com/SuperInstance/vessel-template)** —
  the vessel generator: CHARTER (constitution), MANIFEST (hardware, APIs,
  costs), TASKBOARD, FENCE-BOARD (inter-cell messaging) — the cell spec in
  an older vocabulary.
- **[purplepincher-shell-library](https://github.com/SuperInstance/purplepincher-shell-library)**
  — the canonical agent/vessel separation: the agent thinks and is
  swappable; the vessel acts, persists, and accumulates; later agents use
  committed tools without carrying the context.
- **[vessel-quest](https://github.com/SuperInstance/vessel-quest)** — "the
  boat is the game engine; the logbook is the quest log." XP is attention
  logged — the ledger as a record of where the system *looked*.
- **The EILEEN boat stack** (design record, 2026-10-09) — the superimposed,
  fail-soft layering that seeds §23 restates: manual hydraulics and the
  diesel as the metal floor → the proven autopilot → an ESP32 deadband
  layer → a Jetson learning quilt observing and optionally driving *through*
  the autopilot → independent radar/nav/voice modules → cloud LLM as the
  final layer. Failure of any higher layer leaves every lower layer
  operational.

## MUD and PLATO rooms

- **[mud-mcp](https://github.com/SuperInstance/mud-mcp)** — a TypeScript
  MUD server over the Model Context Protocol: the room/tick/text world as a
  tool surface for models.
- **[plato-ghostable](https://github.com/SuperInstance/plato-ghostable)** —
  persistence classes — **Eternal, Persistent, Ephemeral** — as lifecycle
  management for tiles and agents. The settlement gradient our ledger's
  persistence classes descend from.
- **[plato-portal](https://github.com/SuperInstance/plato-portal)** — PLATO
  as shared tile-server memory: a room is a named collection on the server,
  a tile is one JSON record in it; agents carry markdown memory; a fleet
  layer broadcasts and dispatches.
- **[plato-room-code-review](https://github.com/SuperInstance/plato-room-code-review)**
  and
  **[plato-room-deployment-approval](https://github.com/SuperInstance/plato-room-deployment-approval)**
  — PLATO rooms as engine blocks: a function given walls, a tick, and
  residents.

## The quilt shelf and the floor

- **[cudaclaw](https://github.com/SuperInstance/cudaclaw)** — Rust + CUDA:
  a GPU-resident persistent worker kernel for agent command dispatch;
  lock-free queues in CUDA Unified Memory, sub-µs dispatch, warp-level
  parallelism (32 agents serviced per warp scheduler), thousands of ternary
  agents {−1, 0, +1}. The floor pattern of seeds §19 — with the research
  corrections of [`plato-to-cuda.md`](plato-to-cuda.md) applied. (Framing
  note: the "SmartCRDT / warp-level consensus" language is Casey's framing
  from the 2026-10-23 prior-art note; the deep-research pass records that
  the repo README's own wording differs in places. Treat mechanism claims
  as repo claims until verified on the Thor's sm_110 stack.)
- **quilt-engine** — sovereign active log + active ledger: shared state
  minted only from agreed sends/receives. The ledger doctrine of seeds §12
  in working form.
- **quilt-cell** — the cell as a library: 16-dial Q1.15 vectors, FNV-1a
  64-bit state hash, byte-exact across Python/C/Rust/Verilog/VHDL.
- **jev-quilt** — the decision layer as cells, not endpoints: typed cells,
  hook-and-drop deltas, bookkeeper WAL — the dice (seeds §22) as fabric.
- **qthe** — ternary gating at the embedding level (Ground / Attract /
  Repel / Abstain); kin to cudaclaw's ternary agents.
- **quilt-jetson** — the Quilt runtime for NVIDIA Jetson (Rust): the rack's
  and the rooms' natural runtime home at the edge.
- **quilt-claw** — "the agents are cells; the bus is a cell; the store is a
  cell." **quilt-ai** — AI cells behind one uniform interface (the snap-on
  harness pattern). **beam-quilt** — patchwork architecture for distributed,
  self-coordinating intelligence.
- **lane-sheets** — agent workflows as one JSON sheet: lanes of cells
  connected by piping only; nothing reads another cell's interior; byte-exact
  trace conformance as the agreement object ("implementations agree by
  producing identical traces, never by trusting each other"); a downward leg
  compiling sheets toward quilt fabric opcodes. The piping discipline of
  seeds §10, §21 in working form.

## Generation and rendering

- **[foundry](https://github.com/SuperInstance/foundry)** — the parametric
  3D asset factory on the Thor: a brain authors archetype code once;
  seed + parameters *are* the asset and geometry is a cache; minting a
  family takes seconds and refinement is a local verb. The standing proof
  in miniature of seeds §16, and the builder pattern of §17 (brain-written
  code in a glass box, editable and re-runnable, accepted builds registered
  as archetypes).
- **EdenLive / EdenGolem** (VAST-AI-Research, external) — a real-time
  generative renderer plus a graybox-game-building agent skill; state
  first, rendering follows — independent confirmation of the quilt's split,
  and the current candidate placeholder for the staging ladder's top rung.
  Full identification, spec audit, and fleet-fit verdict in
  [`eden-fit.md`](eden-fit.md): adopt the architecture, trial EdenGolem
  now, trial EdenLive's 5B subset offline on the Thor only; the full
  224.8 GB weights tree and the 14B line are out of scope.
