# The Whole-House Quilt

A house-scale system of **rooms made of text state**, each room perceiving at
its own density, staffed by **stationed resident agents**, adjudicated by
**decision models that act as dice**, and agreed through an **append-only
ledger of sends and receives**. Worlds are staged in a quick, game-engine-style
environment and rendered afterwards, at leisure, up a ladder of fidelities.
The whole thing is spread on purpose across the house's machines and the
operator's cloud subscriptions — one fabric, load-balanced, judged by what
arrives at the screen the user is sitting at.

> "We're not trying to make every agent morph into an excavator. We're
> trying to make better and better excavators that smaller and smaller
> agents can operate smartly."
> — Casey, 2026-10-27

## Status

**DESIGN PHASE.** This repository collects the design corpus and the first
honest scaffolding, gathered 2026-10-27:

- the complete seed corpus (28 sections of design rulings, in the order they
  were made) is in [`docs/seeds.md`](docs/seeds.md);
- a sourced deep-research report testing whether PLATO's 1970s architecture
  ports to CUDA/PTX is in [`docs/plato-to-cuda.md`](docs/plato-to-cuda.md)
  (verdict: the *data* architecture ports almost one-for-one; the *execution*
  architecture does not, and the research corrects the floor design
  accordingly);
- the formal two-plan adjudication for the first build is **still in flight**
  and will land in [`docs/decision/`](docs/decision/) when it completes;
- [`protocols/`](protocols/) holds the first concrete message shapes
  (tick, send/receive, room manifest) as specs, JSON Schemas, and examples;
- [`floor/`](floor/) holds a small Python **reference model** (scaffold,
  standard library only) that runs the room/tick/ledger loop so the shapes
  can be handled, tested, and argued with.

Nothing here is a finished system. Scaffolding is labelled SCAFFOLD where it
appears, and stubs are honest stubs.

## The shape, in one screen

- **Rooms, not apps.** Every function lives in a room: a cell of text state
  with its own tick policy, hooks, triggers, and residents. Rooms quilt into a
  whole that can be viewed coarse (the bridge console) or zoomed into
  (the room's own face). *(Seeds §20, §24; prior art: vessel-room-navigator.)*
- **Perception is addressed, not broadcast.** In the engine room you get full
  readouts; at the console you get a tick only on *change*, plus a slow
  deadband heartbeat. A heartbeat that fails to arrive is itself the alarm.
  *(§20)*
- **The world is text.** Canonical state is structured text in formats built
  for type-safe parsers to grab quickly. Every render is a replaceable
  projection of that text — the chart is not the coast. *(§21)*
- **Decision models are the dice.** At the moment of action, a small local
  decision model rolls: a probability for every option. Big minds author the
  tables; they never roll. Every roll is ledger-recorded, so biased dice are
  discoverable. *(§22)*
- **Sim and real share one seam.** The same text piping runs a simulated room
  or a real one — actuators out to robotics, sensors back as text. A room
  neither knows nor cares which is on its far side. *(§23)*
- **Generators up, instances down.** Big thinkers author generators
  (algorithms, archetype code, templates) once, as capital; small local
  models run them and refine instances at marginal cost. *(§16, §17)*
- **Jobs descend.** A well-defined job sinks from deliberation to script to
  persistent machinery gated by a few little perception checks. A job is
  finished being designed when what remains of it is watching. *(§19)*
- **The staging ladder.** Play on the metal (real-time because it is state,
  not dreaming), judge small sample renders, then let the long render take
  the night. *(§26)*
- **Placeholders behind seams.** Borrowed components (NVIDIA blocks,
  Eden-class renderers) prove the shape now, behind protocol contracts, and
  are swapped for glove-fit pieces without redesign. *(§13)*
- **The spread is the system.** No single box must hold the whole thing; the
  Thor is an enhancement to the estate, and cloud subscriptions are
  first-class compute pools metered by quota. *(§14, §15)*

## Document map

| Document | What it is |
|---|---|
| [`docs/seeds.md`](docs/seeds.md) | The complete seed corpus, §§1–28, unabridged — the design's primary record, including corrections. |
| [`docs/architecture.md`](docs/architecture.md) | A digested synthesis for a new reader: the system as a coherent whole, citing seed sections. |
| [`docs/plato-to-cuda.md`](docs/plato-to-cuda.md) | Deep research: PLATO/TUTOR internals, the mechanism-by-mechanism CUDA mapping, current GPU-simulation practice, ten design nuggets. |
| [`docs/plato-to-cuda-sources.md`](docs/plato-to-cuda-sources.md) | The research report's source log. |
| [`docs/prior-art.md`](docs/prior-art.md) | The inventory of existing fleet artifacts this builds on — read before designing anything "new". |
| [`docs/eden-fit.md`](docs/eden-fit.md) | Identification and fleet-fit research for EdenLive / EdenGolem (VAST-AI-Research), the candidate top-rung renderer. |
| [`docs/decision/`](docs/decision/) | Where the formal adjudication lands when the two-plan process completes. |
| [`protocols/`](protocols/) | Tick, send/receive, and room-manifest protocols: spec + JSON Schema + worked example each. |
| [`floor/`](floor/) | Python reference model of the room/tick/ledger loop (SCAFFOLD), with tests. |
| [`BUILD-LOG.md`](BUILD-LOG.md) | How this repository was built, in the body of the work — decisions, substitutions, and run evidence. |

## Licence

MIT — see [`LICENSE`](LICENSE), matching the sibling repositories
(`terrain`, `plato-ghostable`).
