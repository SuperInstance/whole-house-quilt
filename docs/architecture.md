# Architecture — the whole-house quilt, digested

*This is the synthesis document. The primary record is chronological —
[`seeds.md`](seeds.md), §§1–28, in the order the rulings were made — and this
document reorganises it for a new reader, citing the seed section behind each
claim. Where the two disagree, the seeds win: they carry the corrections.*

## 1. What is being built

A system in which a house (and, by the same piping, a boat, a workshop, any
instrumented place) is a **quilt of rooms**: addressable cells of text state,
each perceiving at its own density, each staffed by residents, all agreeing
through a ledger. Agents and resources alike are cells on the grid (§9) — a
loaded model server is a citizen of the grid, not infrastructure beneath it —
and humans meet the whole thing at a front end whose quality is the system's
actual product (§15).

## 2. The fabric: four tiers, routing by latency class

The architecture is the whole estate plus its APIs, spread on purpose (§14).
Nothing is trying to run on an offline Thor; the Thor is an enhancement to
the laptop and the other systems, not a container that must hold everything.

| Tier | What lives there | Law |
|---|---|---|
| **At the screen** (the ProArt: RTX 4050, the desk) | Reaction: input, motion, reactive scripts, tiny local models; the last mile of every render | Nothing here waits on a network. This tier must survive alone, at reduced depth. |
| **The house** (Orin: state, ledger, ears; Thor: resident models, generation, queues) | The remembered, the generated, the judged | Seconds to minutes. Batching is welcome; this tier is a back room. |
| **Subscriptions** (premium Z.AI, MiniMax, Kimi; a fair Claude plan) | Heavyweight thinking on tap | Each plan is a compute pool whose currency is quota, not watts; the balancer meters quota like the purse meters money (§8, §15). |
| **Rentals** (APIs, cloud by the drink) | Overflow and exotica | Used when the fabric's own tiers genuinely cannot do the job. |

Routing is by **latency class first** (§15): reaction never leaves the
screen; conversation goes to whichever seat or subscription is freshest and
best-fitting; production queues to the Thor or to long cloud sessions.
Capability, queue depth, quota remaining, and cost break the remaining ties,
and cheap decision models do the dispatching — the small model as captain of
its own attention, big models as gauges it consults. Degradation is graceful
by design: a rate-limited plan shifts load to the others; a dead LAN leaves
the local tier carrying the experience. The front end never waits on the
wrong tier.

Priorities inside the fabric are **priced** (§9): an agent that jumps a queue
pays purse for the jump, and the ledger remembers whether the situation
warranted it. Unpriced priority inflates to worthlessness; priced priority
stays a signal.

## 3. Rooms that perceive

A room is a cell of state with **hooks, triggers, and a tick policy** (§20).
Perception is positional and *addressed*, never broadcast:

- **In the room** (diagnostic position): full readout density — everything
  ticking past, at the rate diagnosis needs.
- **At the console** (command position): a tick **only on change**, plus a
  slow **deadband heartbeat** — *everything within bounds, no errors* — every
  minute or five. Silence between heartbeats is information; a heartbeat that
  fails to arrive is the alarm.

"Change of state is perception" is the console's tick rule. An agent may
visit a room, **author how it perceives and how it ticks, and leave**: the
room remains self-running, its levers inside the machine. Its NPCs are
**stationed model-bots — residents, not travellers** — small operators (§18)
and terminal watchers (§19), not an agent moving around the ship. A room
authored well never needs its author in it again.

The **bridge console** (§24) is the master projection: every room's addressed
ticks in one place, quiet unless something changes. **Zooming** into a room
changes position, and position is perception: at the bridge, summaries and
heartbeats; in the room, readouts. Each room has two faces, both projections
of the one text state — a chart-like face for the visiting human, and a text
feed for its residents, a "text-based Nobeltec" shaped for the eyes that
live there.

## 4. The world is text

Canonical state — ledger, ticks, manifests — is **structured text** in
formats designed for type-safe parsers to grab quickly (§21). Parsing is
mechanical: malformed sends are rejected by the contract, never
misunderstood by a helpful model, so tiny watchers can keep up with a room
without spending a mind on reading. Meaning stays in the models; shape stays
in the parser. Every renderer is a **replaceable projection** of the text —
the chart is not the coast — so renders can be re-taken at higher fidelity
without re-staging anything. The concrete contracts live in
[`../protocols/`](../protocols/): `tick`, `send/receive`, and `room-manifest`.

Shared state is minted only from **agreed sends and receives** (§12): the
active ledger is the agreement, and the anchor chain — an object's origin,
facing, and position relative to its anchor — is what placement means. Heavy
files stay where they were made; what moves is the manifest, and bulk moves
on **fetch-on-notice** (§11, §12).

## 5. Decision models are the dice

At the moment an action is attempted, the world stops describing and
**decides** (§22). The referee is a small decision model stationed in the
room: a roll that returns **a probability for every option** — honest about
chance in a way a deliberating model's paragraph is not. Combat is the
canonical case precisely because resolution cannot leave the room mid-swing.

Big minds **author the tables** — the stats, the deadbands, what is rolled
against what, and which face of the die means *wake a bigger mind* — but they
never roll. Every roll is recorded in the ledger, so a die that runs hot or
cold is discoverable from its own history and can be re-weighted in sleep
cycles: attested updating for adjudication.

## 6. The sim/real seam

The same piping runs simulated or real rooms indifferently (§23): actuators
go straight out to real robotics; sensors return their data as text. A room
neither knows nor cares which is on its far side, which makes a simulated
sensor the placeholder for a physical one (§13 applied to reality itself)
and testing a matter of swapping the far end. The worked example is a **nav
room**: autopilot and GPS piped in, a resident navigator perceiving position
and heading ticks and sending helm orders down the text pipe — while its
console projection is only a heading and a GPS position.

The layering floor is standing law and is not amended by any of this: hand
steering at the bottom with no electricity, the autopilot above it, the
perceiving room above that. Nothing crucial ever depends on the MUD layer
(§23; the EILEEN stack in [`prior-art.md`](prior-art.md)).

## 7. Who does the thinking: generators, systems, operators

**Big thinkers author generators; small models refine instances** (§16).
Authoring the generator — the algorithm, the archetype code, the template —
is capital, paid once, and it is the only work that earns the premium tiers.
Running the generator and polishing its instances is instance-shaped work and
stays with local and smaller models. A big thinker re-enters only when the
archetype itself changes.

One level up (§17): a **workbench system** of the Claude-Motion kind — state
held as code, not pixels — is hard for small models to *create* but, once
built, is operable by a 30B-class local coder, because code is its native,
verifiable medium. And such a system **accretes**: every tile, button, and
lever it grows converts a class of future generation into manipulation, so
it becomes more real-time by needing its generator less. The panel is the
system's accumulated capital. Hence the rubric (§18), Casey's words:

> "We're not trying to make every agent morph into an excavator. We're
> trying to make better and better excavators that smaller and smaller
> agents can operate smartly."

A plan succeeds insofar as its machinery gets better while the operators it
requires get smaller. A plan that needs a genius at every seat fails the
rubric, however impressive its machinery.

## 8. The descent, and the floor as corrected by research

Recurring work has a lifecycle (§19): deliberation defines it, scripts
operate it, and its terminal state is **persistent machinery on the floor
gated by a handful of small perception checks**. A job is finished being
designed when what remains of it is watching; the size of its terminal
perception set is a design-quality metric.

The floor's pattern is cudaclaw's — a persistent CUDA worker kernel with
lock-free queues in unified memory ([`prior-art.md`](prior-art.md)) — but
the PLATO→CUDA research ([`plato-to-cuda.md`](plato-to-cuda.md)) corrects
the naive version of it, and the correction is binding:

- **The data architecture ports.** Fixed, capped per-client state arrays
  indexed by slot (PLATO: exactly 150 words per user); a room's shared
  "common" in fast memory (PLATO's cap, 1,500 words ≈ 12 KB, sits
  comfortably in a thread block's shared memory); state tiered
  fast-memory/slow-memory the way ECS tiered against central memory;
  checkpointing at boundaries, because GPU memory is ECS, not disk.
- **The execution architecture does not port naively.** PLATO serialised
  each user's burst, so shared state never faced contention; SIMT removes
  that assumption. Irregular per-client control flow inside a warp
  serialises by divergence. The fixes are **warp-per-client** for irregular
  work, **state-bucketing** of homogeneous clients (FLAME GPU 2's
  approach), and thread-per-client only for uniform tick code.
- **Event-first, not tick-everything.** PLATO's economy came from *not*
  ticking idle clients; tick only dirty rooms, and keep a **~40% capacity
  reserve** — PLATO's own headroom rule — so response stays immediate.
- **Bounded epochs over immortal kernels.** Published evidence on persistent
  workers is mixed (one measurement found persistent scheduling *slower*
  than eager launches), and display GPUs kill long-running kernels; prefer
  bounded-epoch kernels unless the GPU is dedicated.
- **At dozens of clients, the feel is decided at the host↔device boundary**,
  not by compute: binary batched ring buffers across it, text protocols on
  the host side only.

## 9. The staging ladder

Rendering is a ladder climbed after the world already works (§26), rooted
in the Mud-to-SCUMM line and generalised by the Eden ladder:

1. **Staging** — the interactive environment itself: quick, game-engine
   style, on the metal; real-time because it is state and simple rendering,
   not dreaming.
2. **Samples** — little rendered pieces, quick enough to judge by eye.
3. **The long render** — high-end enhancement passes over the staged state
   (EdenLive-class diffusion skinning, upscalers, DLSS-class techniques as
   they arrive) at whatever cost in hours they honestly take. Overnight is
   a legitimate render time, because nobody is waiting: the world was
   already playable. The same night hours carry the sleep cycles — the
   house improves its mind and its pictures in the same darkness.

Assets that worked are **kept, not regenerated** (§12): seed plus parameters
are the asset; geometry is a cache.

## 10. Placeholders, and what would falsify this

Every major component sits behind a protocol seam with a named placeholder
(§13): an NVIDIA Isaac/Cosmos piece, an EdenGolem-generated graybox, a
Bevy/Bullet cell. Borrowed parts are a parts bin, never the stack; each is
swapped for the glove-fit piece without redesign when it is ready.

This is a design-phase document, and its load-bearing unknowns are named in
the seeds: the formal adjudication is still in flight
([`decision/`](decision/)); the smallest first slice and its kill criteria
are proposed at seeds §4 and await that ruling; cudaclaw on the Thor's
sm_110 stack is unverified; and the PLATO→CUDA mapping, per the research, is
original — unvalidated and unrefuted. The references implementation of the
loops described here is the Python scaffold in [`../floor/`](../floor/),
offered so the shapes can be handled and tested, not as the system.
