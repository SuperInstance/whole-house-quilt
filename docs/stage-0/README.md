# Stage 0 — weather and inventory

*Component 0 of the adjudicated build order (decision §12), plus the
inventory the first slice's estimates stand on. Built 2026-10-28 by the
whole-house-stage0 lane: booked on the fleet schedule board (thor,
proart, jetson-orin — `box` seat, 02:00 UTC, 2 h 30 m), measured live,
nothing installed, restarted or reconfigured anywhere.*

- **[lan-weather.md](lan-weather.md)** — measured LAN weather:
  latency percentiles per pair, throughput per direction, the hub
  path into the ProArt, the radios, the traps, and the seeds' stale
  figures replaced. Headline: medians are 4–5 ms everywhere, but any
  path touching the Thor tails to 80–112 ms at p99; loss is 0%
  everywhere; the ProArt → Orin leg runs ~192 Mb/s. One-minute
  samplers accrue the 24 h record on each box
  (`~/whq-stage0/weather-24h.csv`).
- **[inventory-audit.md](inventory-audit.md)** — the fleet's usable
  capacity, verified on the metal: per-box hardware and disks,
  resident services probed live, the seat matrix, the subscription
  pools as quota-metered capacity — and four record-vs-metal
  discrepancies, the largest being the Orin's disk (2 TB, 1.7 TiB
  free, where the decision's §2 argues from 7.84 GB) and the Thor's
  NVMe tail (184 GiB free, where the estimate cues assume 28 GiB).
- **[data/weather-2026-10-28.csv](data/weather-2026-10-28.csv)** —
  the snapshot numbers in machine-readable form, for later estimates
  to cite.

Stage 0 stops here, as chartered: the eleven components are later
stages and await Casey's word.
