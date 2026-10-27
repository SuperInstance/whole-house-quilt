# Build log

*The process, in the body of the work — per the fleet's doctrine that a
result without its process is a claim, not a record.*

## 2026-10-27 — the repository is built (design-phase corpus + scaffold)

**Order.** Casey, 15:39 AKDT: "build the repos and get as much of the
documentation up as possible… GitHub's a good presentation for human eyes,"
and "you can even build the essential programs or essential files in it that
seem pretty obvious what they need to be."

**First decision: the home.** `SuperInstance/quilt` already exists — a
mature, 15 MB, 529-file repository (the general Quilt runtime: "@superinstance/quilt-core",
a VitePress docs site, a demo) under Apache-2.0, actively maintained and
**not** the whole-house system. Building this corpus into it would have
collided with its `README.md` and `docs/architecture.md` and mixed two
subjects in one body. Per the monorepo-first rule read together with the
no-overwrite rule, this work was built as
**`SuperInstance/whole-house-quilt`** instead, and the substitution is
recorded here rather than made silently. The general quilt runtime remains
prior art (see `docs/prior-art.md`).

**Licence.** MIT, matching the sibling repositories in this line
(`terrain`, `plato-ghostable` — both verified MIT via the GitHub API on the
day). The existing `quilt` repo's Apache-2.0 was not matched because this is
a different repository in the terrain/ghostable line.

**What was copied, verbatim, and from where.**

- `docs/seeds.md` — the complete seed corpus (§§1–28) from the fleet's
  research notes of 2026-10-27, unabridged, including the §25 correction
  and the refinement record.
- `docs/plato-to-cuda.md` + `docs/plato-to-cuda-sources.md` — the complete
  deep-research report of 2026-10-27 and its source log. (The research
  directory's own `AGENTS.md` marks its contents as web-derived data; the
  report carries its VERIFIED / INFERENCE / SPECULATION labels throughout,
  and they are preserved.)
- `docs/eden-fit.md` — the EdenLive/EdenGolem identification and fleet-fit
  research note of 2026-10-27.

**What was written for this repository.** `README.md` (the one-screen
statement and doc map), `docs/architecture.md` (the digested synthesis,
citing seed sections), `docs/prior-art.md` (the inventory, from the
2026-10-10 vessel catalogue and the 2026-10-23 prior-art note),
`docs/decision/README.md` (placeholder for the in-flight adjudication),
`protocols/` (specs, schemas, examples), and `floor/` (the reference
model).

**Protocols.** The room-manifest shape is based on
vessel-room-navigator's `rooms-config.json` (fetched live on the day:
`startRoom` + rooms map with id/name/type/description/adjacent/warp),
extended with tick policy, residents, dice, and persistence. All three
worked examples were validated against their JSON Schemas before commit
(local `jsonschema` run):

```
tick example VALID against schema
send-receive example VALID against schema
room-manifest example VALID against schema
```

**Reference model.** `floor/quilt_floor.py` — stdlib-only Python. Demo run
(engine room + nav room, 12 ticks), actual output:

```
Whole-house quilt - reference model demo (SCAFFOLD)
Console view = change-only + deadband heartbeat (§20).
Room view    = full readout, as if standing in the engine room.

tick  1 | ROOM (engine): rpm= 810 coolant=81.6C oil=42.0psi
tick  1 | CONSOLE <- engine-room: (silence - within deadband)
tick  1 | CONSOLE <- nav-room: (silence - within deadband)
tick  2 | ROOM (engine): rpm= 804 coolant=81.2C oil=42.5psi
tick  2 | CONSOLE <- engine-room: (silence - within deadband)
tick  2 | CONSOLE <- nav-room: (silence - within deadband)
tick  3 | ROOM (engine): rpm= 798 coolant=81.2C oil=43.0psi
tick  3 | CONSOLE <- engine-room: (silence - within deadband)
tick  3 | CONSOLE <- nav-room: (silence - within deadband)
tick  4 | ROOM (engine): rpm= 792 coolant=81.6C oil=42.5psi
tick  4 | CONSOLE <- engine-room: (silence - within deadband)
tick  4 | CONSOLE <- nav-room: (silence - within deadband)
tick  5 | ROOM (engine): rpm= 786 coolant=81.2C oil=42.5psi
tick  5 | CONSOLE <- engine-room: HEARTBEAT - all within deadband, no errors
tick  5 | CONSOLE <- nav-room: HEARTBEAT - all within deadband, no errors
tick  6 | ROOM (engine): rpm= 789 coolant=80.8C oil=42.0psi
tick  6 | CONSOLE <- engine-room: (silence - within deadband)
tick  6 | CONSOLE <- nav-room: (silence - within deadband)
tick  7 | ROOM (engine): rpm= 783 coolant=81.2C oil=42.0psi
tick  7 | CONSOLE <- engine-room: (silence - within deadband)
tick  7 | CONSOLE <- nav-room: (silence - within deadband)
tick  8 | ROOM (engine): rpm= 777 coolant=81.6C oil=41.5psi
tick  8 | CONSOLE <- engine-room: CHANGE {'rpm': 777}
tick  8 | CONSOLE <- nav-room: (silence - within deadband)
tick  9 | ROOM (engine): rpm= 774 coolant=82.0C oil=42.0psi
tick  9 | CONSOLE <- engine-room: CHANGE {'rpm': 774}
tick  9 | CONSOLE <- nav-room: (silence - within deadband)
tick 10 | ROOM (engine): rpm= 780 coolant=81.6C oil=42.5psi
tick 10 | CONSOLE <- engine-room: HEARTBEAT - all within deadband, no errors
tick 10 | CONSOLE <- nav-room: HEARTBEAT - all within deadband, no errors
tick 11 | ROOM (engine): rpm= 786 coolant=81.6C oil=42.0psi
tick 11 | CONSOLE <- engine-room: (silence - within deadband)
tick 11 | CONSOLE <- nav-room: (silence - within deadband)
tick 12 | ROOM (engine): rpm= 783 coolant=81.2C oil=42.5psi
tick 12 | CONSOLE <- engine-room: (silence - within deadband)
tick 12 | CONSOLE <- nav-room: CHANGE {'xte_m': 16.0}

Ledger: 15 entries (append-only).
  roll @tick 6 from nav-room: table=cross-track-correction picked=correct-port
  roll @tick 10 from nav-room: table=cross-track-correction picked=hold
  roll @tick 11 from nav-room: table=cross-track-correction picked=hold
  roll @tick 12 from nav-room: table=cross-track-correction picked=hold
```

Tests (`python3 -m unittest test_quilt_floor.py -v`): 7 ran, all OK —
heartbeat/change-only behaviour, full-density readout, dice probabilities
summing to 1, and the ledger's append-only property (immutable exposure,
frozen entries, no removal API).

**Publishing.** Three staged commits (documentation; protocols; reference
model), pushed from the Thor, whose `gh`/git identity is SuperInstance.
A secret scan (tokens, private keys, credential-shaped strings) was run
over the tree before the first push and is re-run before each subsequent
push. Nothing was force-pushed; no other repository was touched.
