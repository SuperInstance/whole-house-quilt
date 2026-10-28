# Adjudication — the whole-house quilt system ("the big project")

**Seat:** Claude Code. **Model:** `claude-opus-5-5` (Opus 5.5), as this session's runtime reports it. **Reasoning effort:** max, as configured and requested. **Date:** 2026-10-27; en-GB.
**Read:** everything the commission lists, seeds §§13–28 and the PLATO report included.
**Tags:** **[m]** measured (corpus, or observed this session) · **[d]** derived (arithmetic shown) · **[a]** assumed. Pre-registered thresholds are [a] unless tagged.

## 1. The decision

The placement both seats reached independently is **confirmed** — engine cells, mint, manifest, registry and warehouse on the Thor; rendering at the ProArt; nothing canonical on the Orin — with three corrections, two from measured facts both missed (§2). The sequencing fork is settled by a **third order** (§3): ZCode's gating governs the *agent* economy, while the *fabric* economy (quota-metered routing across the plans and the Thor's residents) and a room layer built on the fleet's existing rooms enter the first slice. The slice becomes a **workbench**: text-canonical rooms on a PLATO-data floor, judged at the ProArt screen, five of six instantiated by the Thor's resident 30B coder from the first — operability test and build plan in one act.

**In §15's terms.**
- **Reaction** (≤50 ms [a]; never routed): at the ProArt, the staging render loop, input, the missing-heartbeat detector and the local tier — scripts plus the 0.6B model at ~230 tok/s, 6.6× the Orin's ~35 [m; d]; at the Orin, the desk room's sensors; on the Thor, each room's dice beside its engine cell.
- **Conversation** (first token ≤2 s p95 [a]): a dispatcher at the chair routes Casey's questions to the freshest best-fitting pool — Z.AI, MiniMax, Kimi, Claude, or the Thor's 30B at 82.4–82.9 tok/s [m].
- **Production** (minutes to overnight): premium generator authoring; Foundry runs, labelling and long renders on the Thor; night training on the ProArt.
- **Quota metering**: each plan is a resource cell with a quota ledger (window, used, remaining, reset); production may not draw a plan below a 40 % reserve [a] — PLATO's headroom rule, applied to quota — before the last quarter of its window, so nothing is spent flat by noon. Capability, queue depth, quota and cost break ties.
- **Degradation**: a throttled plan goes cold and its load shifts; every plan dry, conversation runs on the 30B and generator work waits for the reset; Thor or LAN dead, the ProArt's local tier carries cached rooms, staging and conversation at reduced depth, the missing heartbeat showing as the alarm; uplink dead, island mode. The render loop never awaits the network.

## 2. The engine-placement ruling

**Ruling.** Casey's sketch put the engine on the Orin; both seats inverted it; the inversion stands. *Yield*: the Orin must yield the instant Casey sits down [m]; a world on a box that must stop is a world that stops. *Reaction path*: the agents' exchange with the world would cross two Wi-Fi hops at 21.6–36.3 ms a round [m legs: 14.7 and 21.6] against a 50 ms tick at 20 Hz [a], p99 jitter unmeasured. *Locality*: fifty manifest readers outweigh one on-notice renderer. *Storage*: the composed destination log, 1.43 GB/h [d, MCode], fills the Orin's 7.84 GB in 5.5 h [d]; the manifest table never bites (~96–128 B a row [d, both seats]).

**Engines-as-cells (R1).** An engine is the **far side of a room** — a placeholder behind the intent/delta piping, placed where that room's reaction path lives: the field room's headless Bevy cell beside its residents on the Thor, the desk room's sensors at the Orin. Bevy is Orin-shaped in capacity, Thor-placed by duty; Bullet waits until a world needs solver authority Bevy lacks; swaps are tested by manifest-equivalence across engines, byte-exactness within one (MCode's split). **Registry versus files (R2).** The scene of record is the **text manifest in the mint** — geometry rows at commission, skin rows when a file is hashed — and any engine's ECS is a fold rebuildable from it (amending both v2s, which made Bevy's transform *the* object model); files stay in the warehouse, render caches at the ProArt.

**What the Orin does instead**, holding nothing canonical: (a) **the desk room** — reaction at its own sensors (input activity; YuNet presence from the wired camera [m]), emitting only occupied/vacant change ticks: the one loop §14 rightly keeps local, and the trigger every console yield obeys; (b) **a bridge-console mirror** on the big monitor — text folded from addressed ticks, tens of kilobytes an hour [d: 6 rooms × 60 heartbeats × ~150 B ≈ 54 KB, plus changes] on the ~71 Mb/s pipe [m], so no log tail is needed, watermarked, dark within 1 s of "occupied"; (c) **an on-demand perception instrument** (depth, pose; later whisper) at production latency. No mint, no engine cell, no 3D.

**Three corrections.** *First, a measured fact both seats missed; it refines rather than reopens.* The Thor's 122 GiB [m] is RAM, shared with the 30B, the rack and the Foundry; the durable log needs storage, and the NVMe has 28 GiB free [m] — **~21 h** at 1.43 GB/h [d: 30.1 GB ÷ 1.43]. The seats' Orin argument reaches the Thor's disk in a day. The cure is the sim/real seam: a simulated room on fixed seeds is regenerable from seeds, intents and engine hash, so its raw observations and deltas are plato-ghostable *Ephemeral*, while agreements, intents, rolls and real sensor text are *Persistent* — "capture first" exactly where data is non-renewable. At ~100 B per intent-and-roll record [a], fifty agents at 20 Hz log ~0.36 GB/h [d]: 3.5 days on the NVMe tail, ~230 on the 2 TB shelf, the log's home [d]. *Second, the latency reading.* An asymmetric pair is the signature of pings from each end, and one-way latency needs synchronised clocks; read as round trips (14.7 ms from the Orin, 21.6 ms from the Thor), an agent's round is 21.6 ms — 43 % of a 20 Hz tick, not 73 % [d]. The ruling never rested on it. *Third, §14 amends "thinking on the Thor"*: only reaction thinking — each room's dice — must sit with its engine; conversation and generator thinking live in the fabric.

## 3. The sequencing fork

ZCode gates the slice on a minimal spine; MCode front-loads (v1: seven stages first; v2: a priced lease, a tombstone and a log measurement in the slice). **Ruling: ZCode's gating governs the agent economy; MCode's instinct governs the fabric.** At slice scale nothing bids: five characters and an uncontended cell yield no evidence about priority inflation, and a lease tested without contention passes vacuously — ZCode's metric-theatre charge stands, with DESIGN.md's "never build the dashboard before the debt exists". But §§14–15 moved the economy that matters, and the slice *does* hold real contention — Casey's conversation against backstage production at the 30B — and real quota. So it carries that cell with **class priority** (conversation pre-empts production) and the fabric purse; leases, the commons and pruning at scale wait for a population. MCode's tombstone survives as the floor's restore test.

**The losing orders' risks.** MCode's front-load builds governance without producers: vacuous passes read as validation. ZCode's gating, taken whole, proves a closed box — no cloud, no quota, no rooms — so the first end-to-end run says nothing about the chair, and exhaustion and degradation are found in use. **This order's risk is breadth**, bought down by reuse (§7) and by the template building the rooms.

**§14, ruled.** The coordinator's finding is **confirmed**: neither v2 scores Thor-only self-sufficiency. One correction: both slices are scoped "no LFM, no cloud" system-wide, and ZCode's estimate claims "no cloud dependency by design" as a merit — a scoping error, not a score. Inside the A/B fork, no cloud is legitimate hygiene; outside it, it violates §14, so subscription plans enter the slice as visiting authors and conversation pools (components 6, 8, 9).

## 4. The floor, on the PLATO evidence (§28)

**Grading.** Both floors score alike on the ten nuggets: partial on fixed-size records (2), append-only messaging (5), batched judging (7), checkpoint compaction (8, MCode exercising it) and a tick budget at 25 % for fifty agents (9) [d: 12.5 ÷ 50 ms]; absent on rooms as blocks (1), homogeneity (3), event-first ticking (4 — both tick everything at 20 Hz), I/O warps (6) and bounded epochs (10). Neither states PLATO's serialised execution, but both Stage-1 gates adopt the silicon floor on a cudaclaw build pass ("PASS → silicon floor adopted"): an immortal kernel running divergent per-agent scripts thread-per-agent, on a GPU measured multi-tenant (30B, rack, ComfyUI, Foundry, NemoClaw [m]). That is the assumption in practice; **the gate fails**; their CPU pattern runtime survives.

**The settled floor — PLATO's data, FLAME's execution.**
- **Rooms share; nothing else does**: hot room state ≤12 KB — TUTOR's 1,500-word common [m, report] — one block's shared memory as within-epoch cache; larger worlds federate by message.
- **Fixed SoA client slots**, hot (~320 B per agent [a]) apart from cold.
- **Event-first**: drain queues, tick dirty rooms only; idle rooms cost nothing; a fixed physics step is declared in a tick policy and runs only while active.
- **Double-buffered append-only messages**: *t* visible at *t+1*; one logical writer per room.
- **Homogeneity**: thread-per-agent for uniform code (CfC passes, integration); state-tag bucketing for script state machines; warp-per-client only for interpreter-like logic; text and judging on the host.
- **Bounded epochs** (≤100 ms [a]), relaunched by host loop or CUDA graph — no GPU here is dedicated: the Thor's is multi-tenant [m]; the ProArt's is display-attached under WSL2 [m: this session's runtime], within reach of the ~2 s watchdog [m, report].
- **Headroom is a hard budget**: ≤60 % of each tick interval (the report's 40 % reserve); per-room budgets; overflow deferred in slot order; a room over budget twice is parked.
- **The boundary**: fixed-size, sequence-numbered binary records in pinned rings (coherent unified memory on the Thor), one crossing per batch; movement coalesces, orders never drop; text stays host-side, codecs generated from §5's schemas. **The ring is the seam**: the CPU executor is today's placeholder; a bounded-epoch GPU executor — cudaclaw's queues without its immortality — takes the seat when a benchmark with a second tenant present improves a chair-side number.
- **Persistence classes on every record**; the restart path before the fast path.

## 5. The world is text (§21), and the sim/real seam (§23)

Tiles are JSON records (plato-portal's definition): one versioned JSON Schema per type, codecs generated for Rust, Python and TypeScript; receivers validate mechanically and NAK malformed sends from a closed reason set (lane-sheets' named refusals). No model reads routine traffic. Protocols: **`TICK`** {room, pos, seq, t, kind: readout|change|heartbeat, dials, hash}; **`SEND`/`RECV`** (quilt-engine's agreement pair) with `ACK`/`NAK`; **`SENSE`/`ORDER`**, the far-side seam; **`ROLL`** {table, options, p[], chose, seed, inputs_hash}; the **manifest** — geometry {id, anchor, offset, facing, state, epoch}, skin {id, hash, lod, pending|ready}, registry {asset, archetype, seed, params_hash, provenance, tier}; **`REQ`** {class, shape: generator|instance, deadline} with quota lines; and authored artefacts — room spec (vessel-room-navigator's rooms-config plus terrain's Room/Exits/Objects/Occupants), tick policy, dice table, `est:`. Spells are typed verbs (MCP tools); equipment, runtime bindings; auras, persistent policies. Both v2s pass the fail-test (typed intents, no model in the pipe) without declaring text canonical; §2 settles it.

**Worked example: the nav room.** Today's far side replays a recorded EILEEN track as text into a heading-hold model; tomorrow's is signalk-bridge (via Oracle's relay) and the real autopilot. The room cannot tell:

```
SENSE {room:nav, src:gps, lat, lon, sog, cog, fix_age_ms}      far side → room
SENSE {room:nav, src:compass, hdg, rot}
ROLL  {table:xte.v1, options:[hold,port2,stbd2], p:[.81,.04,.15], chose:hold}
ORDER {room:nav, to:autopilot, set_hdg, max_delta_deg:2}       room → far side
TICK  {room:nav, pos:bridge, kind:change, hdg, lat, lon}        bridge face
```

The stationed navigator reads full density — track, cross-track error, bearing, set and drift, fix age: Nobeltec as text; the bridge gets two numbers. The layering floor stands: hand steering; the autopilot, holding its last heading if the room falls silent; the ESP32 deadbands; the room steering *through* the autopilot by bounded orders; the cloud planning passages between engagements. Swap acceptance: the far-side binding changes and a diff over the room's artefacts is empty.

## 6. Rooms, positions, dice and faces (§§20, 22, 24)

Each room is a cell with **stationed residents**; **visiting authors** — premium plans through mud-mcp, the 30B for instance work — write its spec, tick policy and dice table, commit and leave, never on its reaction path (purplepincher-shell-library's split: the vessel persists, the agent passes through). Two positions everywhere: the **room** (resident face, full density) and the **bridge** (change-only past deadband, a 60 s heartbeat [a], a missing heartbeat raised by the receiver — a dead sender cannot report itself).

|Room (box)|Stationed residents|Dice → escalation face|Human face / resident face|Far side|
|---|---|---|---|---|
|Field (Thor)|five characters: script + gate arm (fixed, probe, CfC)|harvest, flee, query against gate tables → out-of-distribution flag for the dry dock, never a mid-tick call|top-down staging, score / per-agent dials, last rolls|Bevy ⇄ grid-stepper|
|Engine room (Thor)|budget and quota watchers|park or defer against room budgets → missed twice: park, alarm|gauges (terrain's gauge bridge) / readouts at 1–10 Hz|the system itself|
|Desk (Orin)|YuNet, input script|occupied/vacant, presence deadband with hysteresis → none; local|a lamp / presence stream, never leaving the box|camera, keyboard ⇄ recorded trace|
|Nav (Thor)|navigator: script + small decision model|hold, port, starboard against cross-track and heading deadbands → stale fix: autopilot hold, alarm; out of envelope: Casey|heading, position / text Nobeltec|replay ⇄ signalk-bridge, autopilot|
|Workshop (ProArt, Thor)|archetype-fit judge (rack-class, 140–220 ms [m], authoring pace), registry clerk|which archetype, at what probability → no fit: generator request UP|a door onto staging / per-object pipeline states|Foundry, ComfyUI|
|Dry dock (Thor; plato-room-deployment-approval)|pre-registered rule, lane-sheets scorer|adopt or reject → shared-model change or protected pruning: Casey|verdict card / episode traces|forked worlds|

The **bridge console** is the master projection over every room's bridge ticks — at the ProArt, 5.2 ms from the mint [m], mirrored on the Orin, portable to the laptop. Zooming is a change of position; a missing heartbeat warps attention to its room (vessel-room-navigator's alarm-warp, already built). No room resolves an action up-tier mid-action; both v2s pass that law but name no dice.

## 7. Placeholders, seams and the inventory (§§13, 25, 27)

|Component|Builds on · extends · replaces|Placeholder today|Seam|
|---|---|---|---|
|Mint, ledger|builds on quilt-engine v0.1, quilt-cell, plato-ghostable classes; Oracle replica|quilt-engine|SEND/RECV, class tags|
|Room server|builds on mud-mcp, plato-portal tiles, the 2026-10-02 "everything is a room" note; **replaces** the v2s' push/listener extension of lane-sheets|mud-mcp, external tile server (plato-portal ships clients only)|room contract over MCP|
|Room graph, bridge|builds on vessel-room-navigator; **replaces** the v2s' greenfield scoreboard|as is|TICK by position|
|Engine cells|extends the seats' contract|headless Bevy (borrowed), grid-stepper|intent/delta|
|Floor|extends cudaclaw's queues; **replaces** its immortal kernel|CPU executor|binary ring|
|Dice, judges|builds on the JEV rack, qthe, ncps|fixed tables, probe; CfC candidate|ROLL|
|Fabric purse|builds on DESIGN.md's rate card, liquid-world-model's purse pattern (published prior art)|rules dispatcher; four plans, the 30B|REQ, quota lines|
|Generators|builds on the Foundry glass box and archetype registry; plato-room-code-review admits archetypes|Foundry, ComfyUI, NVIDIA or EdenGolem greyboxes (borrowed)|registry, skin rows|
|Warehouse, fetch|extends the v2s' NVMe-LRU, USB-shelf policy|content-addressed files; ProArt cache|ready skin row|
|Staging, long render|lifts terrain's compiler|Three.js or Bevy; EdenLive-class skinning, upscalers (borrowed)|geometry rows in, skin LOD rows out, never fed back|
|Far sides|builds on vessel-agent-system's twin, signalk-bridge, the EILEEN stack|recorded track, heading-hold model; Isaac-class sims later|SENSE/ORDER|
|Sleep cycle|builds on liquid-world-model's day cycle (shape only), lane-sheets conformance, federated-tinyml-vessel|ncps, PyTorch on the ProArt|episodes in, verdict out|

**Terrain is a nugget mine** — read, verify, lift, never fix in passing: its "true state vs shadows" law is §21 already written; its room text compiling to ~1.2 KB scenes [reported] feeds the staging rung; portals-become-exits suits the workshop's doors. Nothing is built on it before the audit runs it. **Both v2s greenfield the room layer by omission** (they predate §25) and are marked down equally; this design inherits it, and rebuilding any inherited part needs Casey's ratification.

## 8. Generators up, instances down; the descent (§§16, 19)

**The routing rule: generator-shaped work goes up** — premium plans, priced by the purse, production class; **instance-shaped work stays down** — the 30B, then small models, then scripts. Premium pools refuse instance-tagged requests by type; a big thinker re-enters only through an archetype-change request.

|Work|Generator authored by|Instances run and refined by|Terminal perception set (n)|
|---|---|---|---|
|Room kinds|premium visiting author|the 30B instantiates; scripts vary|archetype fit (1)|
|3D objects|premium, in the Foundry glass box|Thor runs seed+params; local refine verbs|fit, sample verdict (2)|
|Materials|premium, once per family|scripts vary seeds|none (0)|
|Dice tables|premium or the 30B|nightly re-weighting from ledgered rolls|bias drift, episode count (2)|
|Tick policies|visiting author|residents; deadbands tuned nightly by script|deadband breach, heartbeat timer (2)|
|Gates, scripts|premium|CfC or probe re-distilled nightly|drift probe, adoption verdict (2)|
|Long renders|premium, the pipeline once|Thor GPU overnight|night window, headroom, keep verdict (3)|
|Routing|premium designs the classes|rules, then a distilled decision model|class, quota, plan health (3)|
|Fetch, cache-ahead|designed once|ProArt resident fetcher|ready-but-uncached, player within *N* doors (2)|
|Sleep cycle|designed once|scripted nightly, then resident|episodes ≥ *n*, chair empty, rule verdict (3)|
|Pruning|the pre-registered rule|automatic class by rule|headroom, dominance (2)|

Twenty-two small checks across eleven jobs [d: column sum], none bigger than a small classifier; the metric is that total falling. Generator authoring and protected-class pruning keep deliberation on purpose. Neither v2 spends premium cognition on instance polish — no economics failure — but neither splits generator from instance, and both send every room description to the 30B for a fresh layout: deliberation every run, generation where manipulation would do.

## 9. The staging ladder (§26)

|World|Staging (rung 1)|Sample (rung 2)|Long render (rung 3)|Gate to climb|
|---|---|---|---|---|
|Workshop rooms|schematic room from geometry rows, seeded materials, local|Foundry preview instance, seconds to tens of seconds [a]|diffusion skinning and upscale, overnight on the Thor; cloud credits for slow one-offs only|kept after a visit → sample; keep, night, headroom → long render|
|Vessel rooms|vessel-room-navigator's rooms and text faces (exist)|per-room render, minutes [a]|EdenLive-class skinning overnight|Casey's keep|
|Field world|top-down projection|a tick-window clip, seconds [a]|the day's film of an adopted candidate, optional|dry-dock adoption|

Playability never waits: R3's failure case is rung one; every new room opens on staging. A cold 120 MB skin set is ~13.5 s at 8.875 MB/s [d] — a fill-in, not a door. Neither v2 makes play wait on render, nor specifies the climb. The night works twice: ProArt training while the chair is empty, Thor renders beside the bounded-epoch floor.

## 10. The two plans graded

|Doctrine|ZCode v2|MCode v2|
|---|---|---|
|§15|box-first; only m6, m7 face the chair; best degradation note (a sleeping Thor freezes, never blanks)|box-first; m7 (Orin fill time) optimises a box for a settled question — struck|
|§17|demonstration-shaped; no panel, no operability test|same, plus mechanisms with no operator|
|**§18 grade**|**B−**|**C+**|

Elsewhere (§§3–9) they score alike, bar MCode's sharper typed seam and nugget 8, and ZCode's struck no-cloud merit.

**The excavator grades.** ZCode, B−: its order improves machinery only where evidence exists, keeps the probe as "a fine System 1" so the smaller operator wins ties, and never asks for cleverness where a rule will do; it loses marks because frontier seats staff every stage and no operator ever shrinks. MCode, C+: its best idea is pure excavator — a lease whose escalating renewal price limits inflation "without a policing agent" — but it front-loads machinery with no operator yet: excavators for a site that does not exist. Neither names who operates what; M6 makes the grade measurable. The grades weigh in §3: ZCode's order is the base, MCode's contracts its best parts.

## 11. Rejected alternatives

- **Casey's sketch**: loses on yield, reaction path and log; MCode's numeric reopening conditions stand, though under §15 even a pass would optimise a box nobody judges.
- **Mint on the Thor, engine cell on the Orin**: the cell's clients are on the Thor, and the Orin must yield.
- **Engine at the ProArt**: a burst-shaped family machine whose GPU belongs to staging and night training — the Orin's problem relocated.
- **Engine or mint in the cloud**: the reaction path would cross the uplink.
- **The seats' sketched merge**: it predates §§13–28 and ships a closed box with an uncontended lease.
- **An immortal GPU floor** (§4); **a greenfield room layer** (§7); **canonical state in an engine's format** (§2).

## 12. Build order and the first slice

Component 0 measures; 1–11 are the slice. After it, each gated by slice evidence: the agent economy (fifty characters, commons, priced leases, pruning), real far sides (the boat; the Orin as ear), GPU-floor adoption, the LoRA leg, routine long renders.

|#|Component|Box|Seat|Done when|
|---|---|---|---|---|
|0|Weather: 24 h RTT p50/p95/p99 per pair, reading stated; Thor→ProArt throughput per stream and aggregate; Bevy RSS and tick; Orin yield|all|ZCode|weather records in the ledger, cited by later estimates|
|1|Inventory audit of §7's artefacts; terrain read only|Thor, ProArt|MCode|per repo: runs where, speaks what, reuse or extend — within 3 days|
|2|§5 contracts, generated codecs, NAK vocabulary|Thor|MCode|fixtures round-trip in three languages; malformed ones refused|
|3|Mint and room server: quilt-engine, mud-mcp on tiles, persistence classes, addressed ticks; restart path first|Thor|ZCode|an author enters by MCP, writes a tick policy, leaves; the room ticks 24 h unattended; restore byte-exact|
|4|Floor v0 (§4) on the Thor's CPU; GPU epoch benchmark off the critical path (2-day box, second tenant present)|Thor|Claude Code|M8; benchmark filed|
|5|Field room, the exemplar: Bevy cell, grid-stepper, gate arms trained with drift|Thor; ProArt trains|ZCode cells; Claude Code gates|manifest-equivalent swap; rolls in the ledger|
|6|Fabric purse: dispatcher at the chair, quota ledger, reserve, failover; the 30B as a class-priority cell|ProArt; ledger on Thor|MCode|M2, M9 drills pass|
|7|Projections: bridge console, holodeck staging window, Orin mirror|ProArt, Orin|Claude Code|M1, M3|
|8|Rooms by template: engine room, desk, nav, workshop, dry dock|Thor, Orin|the 30B coder; ZCode reviews via validators and plato-room-code-review only|contract tests pass; interventions counted (M6)|
|9|Workshop loop, ladder rungs 1–3; one generator request goes UP|ProArt, Thor, cloud|MCode; Kimi as visiting author|M4; one archetype admitted; one overnight render lands as skin rows|
|10|Dry dock: one manual sleep cycle, from episodes to ratification|Thor, ProArt|ZCode|M12|
|11|Acceptance against the pre-registration|all|Muse verifies receipts; Claude Code runs the battery|metrics filed|

**Pre-registered success metrics.** *At the chair*: **M1** no render frame blocked on a remote call; staging p99 frame ≤33 ms on the 4050. **M2** first token ≤2 s p95 on healthy plans, ≤3 s with one throttled, ≤1 s from the local tier with the LAN pulled. **M3** a Thor-side change reaches the bridge ≤250 ms p95 (PLATO IV's average-response requirement [m, report], here at p95); a missing heartbeat raised within period + 30 s. **M4** a commissioned door opens on staging ≤2 s p50, and never locks. **M5** the Orin mirror dark ≤1 s after "occupied", tick counter monotonic. *In the system*: **M6** the 30B coder completes ≥8 of a pre-registered ten-task battery unaided — no premium call, no human edit: instantiate a room; change a deadband; add a lever; re-weight a die; swap an engine; commission from an archetype; run the sleep procedure; park and restore a room; diagnose an injected stall from the engine room; roll back a change. **M7** all routine traffic parsed mechanically. **M8** floor ≤60 % of tick interval at p99; idle rooms tick zero times; restores byte-exact. **M9** every request tagged with class and shape; none instance-tagged served by a premium pool; no plan drawn below reserve by production. **M10** engine swap manifest-equivalent; desk room sim ⇄ real with an empty artefact diff. **M11** accretion baseline (registered rooms, policies, dice tables, archetypes, dials, verbs; manipulation share of workshop requests), then weekly, rising. *The seed's bar*: **M12** gated characters beat fixed gates on resource per life by ≥5 % relative, interval excluding zero, n ≥200 paired episodes, two drift regimes; the CfC beats the probe under drift by ≥5 % or the probe is adopted; fork start-states hash-identical; a sleep cycle ≤2 min of LAN [d: 10 MB ÷ 8.875 MB/s ≈ 1.1 s].

**Kill criteria, by what they kill.** **K1** a model needed in the pipe → contracts wrong; redesign. **K2** inventory fails its box → keep the contracts; rebuild only with Casey's ratification. **K3** coder below 5/10 → product-shaped; freeze features, invest in the template. **K4** a frame blocked remotely, or conversation p95 over 5 s on healthy plans → redesign routing first. **K5** floor cannot hold 60 % → data layout wrong; a GPU is no rescue. **K6** fork traces not identically scorable → halt everything downstream. **K7** gates do not beat fixed gates → kills the decision claim only; scripts or probe stand. **K8** a sleep cycle over 2 min of LAN, or any agent↔engine round on the LAN → re-place.

## 13. Estimate for the first slice

`est: by=opus-adjudicator type=build time=15wd tok=75M cost=£0 cash (prepaid; ~£150 shadow on MCode's assumed $2/$8 card) range=9–28wd hor=5wd cues="inventory unverified; LAN weather unmeasured; Thor NVMe 97% full; Thor GPU multi-tenant; ProArt burst-shaped; seat estimates 10× apart" cont="inventory fails → ratified rebuild; coder <5/10 → three rooms, template next; GPU benchmark inconclusive → CPU floor; quotas bind → production waits" xcl="no installs on the Thor's pinned torch; ProArt trains only with the chair empty; A/B fork exclusive of standing Thor load; premium pools never serve instance work"`

**Reading.** The p50 sits a quarter to a half above the seats' 10–12 days: the slice now carries what §§13–28 added, offset by reuse and the template building five rooms. The range is wide because two components are bets — the inventory's maturity, the coder's operability — whose failure redirects rather than shortens. Tokens side with ZCode's order of magnitude: MCode's 4.2M is ~0.1M per seat-day [d: 4.2M ÷ (3 × 12)], implausibly low for agentic seats that re-read context [a]; the tenfold gap is the record's first calibration datum. Shadow: $195 ≈ £150 [d: 67.5M in × $2 + 7.5M out × $8 per million; 9:1 split assumed]. From component 6 the quota ledger meters this estimate's own burn — the first job the purse grades.

## 14. The honest worst risk

**The template may not be operable by a small model after one slice.** Every doctrine this design leans on — generators up (§16), operate-not-create (§17), smaller operators (§18), the descent (§19), leavable rooms (§20) — assumes that once contracts, an exemplar room and typed verbs exist, the Thor's 30B coder can work inside them. The evidence is one working miniature, the Foundry, and a year of Casey's practice; nothing measured. If it fails, recurring work stalls at the premium tier, quota burns on instance work dressed as generator work, the chair waits on the wrong tier, and the house owns fine machinery only frontier seats can drive — §18's failure mode. The guard is M6 with K3. **What would change my mind**: below 5/10 after one template iteration — not yet a template; narrow to three rooms and a deeper verb set. Ten out of ten first time — the battery is too easy; harden it before believing it. The risk that bites first is nearer: the inventory's maturity (plato-portal ships no server; mud-mcp and the tile server are unverified here) — K2's three-day box.
