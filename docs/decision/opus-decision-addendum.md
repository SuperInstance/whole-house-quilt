# Addendum — SuperInstance/quilt (quilt-core)

**Seat:** Claude Code (`claude-opus-5-5`); 2026-10-27; en-GB. **Occasion:** refinement 20 (23:45 UTC, fourteen minutes into the run). **Not read:** quilt-core itself, so its internals appear below only as audit questions.

**The fact** [reported, refinement 20]: SuperInstance/quilt, the quilt-core monorepo, is a mature, general Quilt runtime: 15 MB, 529 files, a VitePress site, Apache-2.0, actively maintained. §7 built the mint on quilt-engine v0.1, six days old [d], without naming it: incomplete. The corpus held two traces I did not chase: lane-sheets' kinds "reduced from the quilt sheet runtime's nine", and its "quilt fabric opcodes (BIND/LINK/EFFECT/VIEW/TICK, ACK/NAK argued as the +1)". Whether either is quilt-core is the audit's first question.

## 1. The relationship

**Overall: build on it at the substrate, sit beside it in two components, supersede none of it.**
- *Build on*: seeds §25 requires building on the fleet's prior art, and seeds §13 seats the fleet's own piece, once ready, "without redesign". If quilt-core keeps a ledger, a mint on a v0.1 beside it duplicates it by omission — the greenfielding §7 marked both v2s down for.
- *Supersede nothing*: that presumes knowing what quilt-core does badly; I have seen none of it. Parts replaced from this lane fork a moving upstream; if quilt-core is the patchwork-quilt programme's, the seeds' lane note places it "in another lane" and disclaims any "raid on it". Supersession is an upstream proposal to Casey from audit evidence; §7 reserves rebuilds to his ratification. Apache-2.0 settles licensing; the choice is engineering.

**Per component:**
- **Mint, ledger: build on, conditionally.** If component 1 finds the send/receive agreement in quilt-core, quilt-core takes the seat and quilt-engine's place is the audit's finding; if not, quilt-engine keeps it. Either way the occupant must pass the SEND/RECV fixtures and a byte-exact restore; the house's manifest fold, persistence classes and class tags sit on top, never patched in.
- **Cell piping: build on, under §5.** Cells pipe through quilt-core wherever it carries §5's records intact; where it already names a record §5 coins, §5 adopts its name and fields, adding only what the house needs. The text record stays canonical: §11 rejects canonical state in an engine's format, and a runtime's earns no exemption. The hazard is duplicate vocabulary (two TICKs, two ACK/NAK pairs, two state hashes), concrete if those fabric opcodes are quilt-core's; component 2 freezes no name before component 1 reconciles it.
- **Room server: sit beside.** Seeds §25 names the room layer's artefacts (mud-mcp, vessel-room-navigator, PLATO's engine-blocks); refinement 20 names a general runtime. A room is a cell and may run on quilt-core, but its contract (an author enters by MCP, writes, leaves) stays with mud-mcp on tiles unless the audit finds quilt-core serving it; then it competes under the same test. The lead is quilt-cell-bridges, porting "vessel, chart-room" to Quilt cells.
- **Floor contracts: sit beside, beneath.** PRIOR-ART's mapping puts Quilt as the grid, cudaclaw-pattern dispatch beneath. The ring's codecs are generated from §5, so what §5 adopts reaches the ring with the floor untouched. If quilt-core schedules cells itself, M8's "idle rooms tick zero times" binds its loop; failure moves the hot path onto the floor.

**Unknowable before the audit:** its language; whether it runs on the Thor within "no installs on the Thor's pinned torch" (a docs site proves neither); whether it has a ledger, scheduler, wire format or persistence; how quilt-engine, quilt-cell and quilt-jetson relate to it; whose lane maintains it.

## 2. The amended §7 row

Replace

```
|Mint, ledger|builds on quilt-engine v0.1, quilt-cell, plato-ghostable classes; Oracle replica|quilt-engine|SEND/RECV, class tags|
```

with

```
|Mint, ledger|builds on **SuperInstance/quilt (quilt-core, Apache-2.0)** if component 1 finds the send/receive agreement there, else on quilt-engine v0.1 beside it; quilt-cell, plato-ghostable classes; Oracle replica; supersedes nothing in quilt-core|quilt-engine v0.1, until component 1 rules|SEND/RECV, class tags|
```

The seam column stands: the agreement pair binds whoever holds the seat, renamed at most if §5 adopts quilt-core's names. Component 1 audits "§7's artefacts", so this row admits quilt-core as a first-class, per-repo entry, audited first, since the mint, §5 and the room server wait on it. No other row changes before that verdict.

## 3. Rulings

None changes.
- **Placement** rests on yield, reaction path, locality and storage: properties of boxes and the LAN, not of a runtime. A runtime that cannot run on the Thor loses the seat; it does not move the mint.
- **Sequencing** followed contention evidence, and a mature runtime adds none. Whatever quilt-core ships beyond the seams stays dark in the slice: owning machinery is no evidence for running it, or MCode's front-load returns by the back door.
- **Floor**: PLATO's evidence and a measured multi-tenant GPU decided it; quilt-core sits above the ring.
- **Slice**: scope unchanged. Component 1 takes quilt-core within the same 3-day box, asking "runs where, speaks what, reuse or extend" at three seams, not reading 529 files; as with terrain, nothing is built on it before the audit runs it. Component 2's wait on that verdict is the one new edge, inside the existing order.

The `est:` line stands unrepriced: a passing quilt-core favours 9–28wd's bottom, a colliding vocabulary its top; pricing either now would be invention. §14's worst risk stands; the risk that bites first, the inventory's maturity, gains a candidate reported mature, unverified.
