# floor/ — reference model (SCAFFOLD)

A small, readable Python model of the room/tick/ledger loop — seeds §19's
"floor" at desk scale. **Standard library only; it runs.**

It exists so the protocol shapes in [`../protocols/`](../protocols/) can be
handled, tested, and argued with. It is not the cudaclaw-pattern CUDA floor
and does not pretend to be; the research corrections for that floor
(bounded epochs, warp-per-client or state-bucketing, 40% reserve) are in
[`../docs/architecture.md`](../docs/architecture.md) §8.

What's modelled:

- **Rooms** with tick policies: full `readout` in-room; `change`-only plus
  a scheduled deadband `heartbeat` at the console (§20).
- **Residents**: stationed stubs — an engine watcher (script) and a
  navigator holding dice.
- **Dice**: a probability per option, rolled in the room against an
  authored table (§22).
- **Persistence classes**: eternal / persistent / ephemeral
  (plato-ghostable).
- **The ledger**: append-only sends and receives; entries are frozen and
  exposed only as an immutable tuple.

Run it:

```sh
cd floor
python3 quilt_floor.py            # demo: two rooms, 12 ticks, both views
python3 -m unittest test_quilt_floor.py -v
```

Run output from the build is recorded in [`../BUILD-LOG.md`](../BUILD-LOG.md).
