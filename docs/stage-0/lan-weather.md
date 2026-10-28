# Stage 0 — LAN weather

*Component 0 of the adjudicated build order (decision §12): "Weather: 24 h
RTT p50/p95/p99 per pair, reading stated; Thor→ProArt throughput per
stream and aggregate; Bevy RSS and tick; Orin yield." Measured
2026-10-28, 01:58–02:10 UTC (17:58–18:10 AKDT), by the whole-house-stage0
lane. Every figure below is from the metal on the night; the seeds'
standing figures are quoted only to be replaced.*

## Method

- **Latency:** ICMP ping, 150 packets at 200 ms spacing per pair and
  direction, percentiles computed from the per-packet series; jitter is
  the RFC 3550 estimator over the same series. Two additional 100-packet
  summary rounds per pair agree with the main run. **Packet loss was 0%
  on every pair, in every round.**
- **Throughput:** iperf3 (10 s tests, JSON out) where both ends have it;
  a Python TCP sink/source pair where they do not (the ProArt WSL has no
  iperf3 — see the inventory audit); bulk transfers *into* the ProArt go
  over the SSH hub, because that is the only inbound path that exists.
- **Hub path:** TCP-connect timing to the hub listener
  (192.168.0.78:2206), plus cold SSH echo round trips through it.
- **24-hour record:** one-minute samplers (3-ping averages to gateway,
  peers and 1.1.1.1) were started on all three boxes at 02:04 UTC,
  writing `~/whq-stage0/weather-24h.csv` on each box for 24 h. Tonight's
  battery is the snapshot; the samplers accrue the record the decision
  asks for, and later estimates should cite the CSVs, not this page.
  *Process note:* the samplers' first minutes overlap this lane's own
  bulk-throughput tests and read high accordingly — self-interference,
  recorded rather than cleaned. The 24 h run washes it out.
- Conditions on the night: house occupied, evening; Eden trial and the
  cold librarian active on the Thor (load ~6.5); Orin and ProArt idle.

## Latency (ms, ICMP)

| Path | avg | p50 | p95 | p99 | max | jitter |
|---|---|---|---|---|---|---|
| Thor → Orin | 9.39 | 4.45 | 41.10 | 80.00 | 85.2 | 12.83 |
| Orin → Thor | 11.07 | 4.27 | 51.80 | 92.00 | 106.0 | 9.58 |
| ProArt → Thor | 10.45 | 5.39 | 42.90 | 84.20 | 101.0 | 13.60 |
| ProArt → Orin | 5.67 | 4.98 | 6.69 | 18.30 | 92.9 | 1.07 |
| Thor → gateway | 8.8–9.9 | — | — | — | ~93 | — |
| Orin → gateway | 1.99–2.01 | — | — | — | 3.4 | — |
| ProArt → gateway | 3.21 | 3.10 | 4.64 | 5.05 | 16.7 | 0.59 |
| Thor → WAN (1.1.1.1) | 37.97 | 33.20 | 65.90 | 112.00 | 115.0 | 14.82 |
| Orin → WAN | 31.47 | 30.80 | 36.60 | 38.20 | 39.3 | 2.62 |
| ProArt → WAN | 33.04 | 32.30 | 37.70 | 42.00 | 52.0 | 2.58 |

**The reading.** Medians are small — 4–5 ms between any two boxes. The
tail is the weather: any path touching the Thor spikes to 80–112 ms at
p99, while paths that avoid the Thor (ProArt ↔ Orin, both boxes to the
WAN) stay tight. The Thor's radio is the storm source (see below). A
Thor ↔ Orin round trip is ~8.7 ms at p50 and ~172 ms at p99. Against
the decision's 50 ms tick at 20 Hz: median rounds fit with room to
spare; p99 rounds blow through three ticks. The event-first floor
(decision §4) is not caution, it is the correct response to this tail —
and no budget in later components should be set from a mean or a median
on any path that touches the Thor. The bridge budget M3 (a Thor-side
change reaches the bridge ≤250 ms p95) is feasible on these numbers,
but only over a persistent channel: a *cold* SSH echo through the hub
costs p50 54 ms (from the Thor) / 75 ms (from the Orin), handshake
included.

## Throughput (Mb/s)

| Path | Method | Result |
|---|---|---|
| Thor → Orin | iperf3, 1 stream | 61.5 |
| Thor → Orin | iperf3, 4 streams | 83.7 |
| Orin → Thor | iperf3, reverse | 94.4 |
| ProArt → Thor | raw TCP (Python sink) | ~92 |
| ProArt → Orin | raw TCP (Python sink) | ~192 |
| Thor → ProArt | via SSH hub (the only inbound path) | 55.3 |
| Orin → ProArt | via SSH hub | 33.5 |

The ProArt is the fastest talker on the LAN (~192 Mb/s to the Orin) —
its radio position is the best in the house. Everything that touches
the Thor is capped by the Thor's own link. Bulk into the ProArt pays
the hub tax: SSH crypto plus, from the Orin, two wireless hops.

## The radios, and the traps

- **Thor:** signal −62 dBm; negotiated rx 172 / tx 206 Mb/s (HE-MCS
  7/8). The weakest radio in the fleet, and it is the box the design
  makes the warehouse — placement stands (decision §2), but every
  Thor-crossing budget inherits this link.
- **Orin:** signal −49 dBm; negotiated rx 585 / tx 351 Mb/s (VHT,
  80 MHz). A healthier radio than the standing record implies.
- **ProArt:** not measurable from inside WSL (the Windows host owns the
  radio); its measured throughput is the evidence that matters.
- The LAN serves IPv6 DNS with no IPv6 transit: tools that prefer AAAA
  records hang. Pin IPv4 (as the fleet already does for
  api.cloudflare.com on the Jetsons) wherever a new tool stalls.
- The ProArt is WSL2 behind NAT: nothing on the LAN can open a
  connection *to* it except through the Thor hub forwards (:2206 SSH,
  :8788 otherhere). Every ProArt figure above respects that asymmetry:
  out of the ProArt is raw LAN; into it is the hub.

## Against the seeds' figures

The seeds carried single numbers — Thor→Orin 21.6 ms, Orin→Thor
14.7 ms, ProArt→Thor 5.2 ms, Thor→Orin iperf ~71 Mb/s — quoted in the
decision (§2) as "21.6–36.3 ms a round". Tonight: those legs are
4–5 ms at the median, 9–11 ms on average, and 80–92 ms at p99. The
seeds were not wrong; they were one summary statistic pretending to be
the weather. Throughput likewise: 61–94 Mb/s Thor ↔ Orin depending on
direction and streams (the ~71 figure sits inside that range), and
~192 Mb/s on the ProArt → Orin leg nobody had measured.

## Two component-0 items that could not be measured

- **Bevy RSS and tick:** there is no Bevy binary, project or process on
  any fleet box tonight (searched the Thor; nothing). Bevy enters with
  component 5, the field room; its RSS and tick are measurable only
  then. Recorded as *absent*, not estimated.
- **Orin yield:** the Orin carried load ~0.25 all evening with only the
  Earth-survey desktop resident — it is yielding by default because
  nothing canonical is placed on it. The yield *mechanism* (desk-room
  occupied/vacant ticks, decision §2) is component 8's to build; what
  Stage 0 certifies is the precondition: an idle, responsive box whose
  only standing tenant is Casey's own desktop work.

## Data

Per-packet series and round summaries are preserved on each box under
`~/whq-stage0/pings/`; the 24 h samplers write
`~/whq-stage0/weather-24h.csv` per box. The snapshot table above is
also filed as `data/weather-2026-10-28.csv` beside this document.
