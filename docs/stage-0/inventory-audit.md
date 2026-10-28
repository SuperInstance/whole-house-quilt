# Stage 0 — Inventory audit

*The fleet's usable capacity as the workbench will see it, verified
live box by box on 2026-10-28, 02:00–02:15 UTC, by the whole-house-stage0
lane. Method: every claim below was read off the machine it describes
during the audit window — `df`, `free`, `nvidia-smi`, `ss`, HTTP probes
against the service itself, seat `--version` output. Where the metal
contradicts the standing record (TOOLS.md, MEMORY, the decision's own
estimate cues), the contradiction is flagged in place and collected at
the end. Nothing was installed, restarted or reconfigured.*

## Thor — the back room (engine, mint, registry, warehouse)

- Jetson AGX Thor, hostname `thor`, kernel 6.8.12-1021-tegra, 14 cores,
  122 GiB RAM (80 used / 42 available during the audit — Eden trial,
  cold librarian and residents all live), load ~6.5.
- GPU: NVIDIA Thor (sm_110, unified memory). 0% utilised at the audit
  instant, but ~54.5 GB held by four resident processes: llama-server
  :8001 (20.9 GB), llama-server :8092 (1.0 GB), ComfyUI's Python
  (28.0 GB), the JEV rack's Python (4.7 GB). The GPU is multi-tenant
  even when "idle" — decision §4's second-tenant condition is the
  normal state, not a test setup.
- **Disk: NVMe 936 GiB — 704 used, 184 GiB free (80%).** The cold
  librarian has moved the needle from 28 GiB free at the storage
  crisis. Toshiba USB shelf: 1.9 TiB, 238 GB used, 1.6 TiB free.

### Resident services, probed live (all HTTP 200)

| Port | Service | State on the metal |
|---|---|---|
| 8001 | llama-server | Qwen3-Coder-30B-A3B-Instruct — the resident coder |
| 8092 | llama-server | **lfm2-1.2b-liquid** — a fast small local tier (see discrepancies) |
| 8077 | JEV rack | healthy; `loaded: {ijepa: true, vjepa2: true, judge: true}` |
| 8188 | ComfyUI | active (systemd) |
| 8190 | Image portal | active |
| 8200 | Foundry portal | active |
| 11434 | Ollama | two models on the shelf: `nemotron-3.5-lightning`, `qwen3.5:9b` |
| 18789 | NemoClaw gateway | Docker container `openshell-default--my-assistant…` up 28 h, healthy |
| 2206 | ProArt hub forward | listening (the ProArt's front door) |
| 8788 | otherhere LAN forward | listening |

- Download governor: `download-governor` active; its attempt ledger
  shows the Eden subset downloads in flight tonight.
- Seats: ZCode 3.16.2-38, MiniMax Code 0.6.13, Kimi Code 2.3.2 —
  driven via the `muse`/`muse2` tmux stage or detached; ZCode headless
  print mode cannot write files (fleet lesson), builds go through
  interactive seats.
- tmux at audit: `muse`/`muse2` (4 windows), `bench-loop`.

## Orin — the front room (desk, sensors, console mirror)

- Jetson Orin Nano Super, hostname **`orin`**, kernel
  6.8.12-1021-tegra, 6 cores, 7 GiB RAM (4 used / 3 available),
  load ~0.25 — idle, yielding by default.
- **Disk: NVMe (XG7000) 1.9 TiB — 88 GiB used, 1.7 TiB free (5%).**
  The emptiest disk in the fleet. See discrepancies: the record, and
  the decision's own §2 storage argument, describe a different box.
- GPU: nvgpu, unified memory with the 7 GiB above — a bench, not a
  warehouse.
- No Ollama (nothing on :11434) — as designed; its language capacity
  is the small resident shelf + gauges on the Thor.
- Seats: ZCode 3.16.2-38, MiniMax Code 0.6.12 (nvm Node v24.22.0).
- Standing tenant: Casey's desktop (Xorg) with the Earth-survey
  Firefox — 1,633 survey PNGs in `~/sitka-reference/`, COVERAGE.md at
  2,036 lines, staging to the Thor verified identical by the survey
  lane. This is the workload the yield rule protects.
- Remote-desktop rig: `orin-novnc` active, but **`orin-x11vnc` has
  been failed since 2026-10-25 17:41 UTC** — the noVNC page's backend
  is down, so the remote door into the front room is currently broken
  even though the service list looks half-green. The local desktop
  (and the survey) are unaffected.

## ProArt — the bridge (rendering, the chair)

- WSL2 on eileen, kernel 6.18.54.1-microsoft-standard, 24 cores,
  15 GiB RAM (8 used / 6 available), load ~0.10, up 9 h 19 m.
- **Disk: 1,007 GiB — 86 used, 871 GiB free.** Plenty of room for
  render caches, which is what the design puts here.
- GPU: NVIDIA GeForce RTX 4050 Laptop, 6,141 MiB (675 MiB used, 0% at
  audit). Reachable only via `/usr/lib/wsl/lib/nvidia-smi` — bare
  `nvidia-smi` is not on the WSL PATH.
- Seats: Claude Code 2.1.302 (`~/.local/bin/claude`, headless can
  write), ZCode 3.16.3-40, MiniMax Code present. TUI seats and the
  shared stage are exclusive, booked per lane.
- Casey's stop order intact: `proart-gpu-resident`, `browser-capture`
  and `proart-portal` all **inactive**, as required since 2026-10-25.
- otherhere answers 200 on :8788 (served by a `workerd`; the
  `otherhere.service` unit reads inactive — the port is the service,
  as the record already notes).
- **iperf3 is not installed in the WSL** — a small tooling gap; Stage 0
  measured around it (see the weather document).
- tmux at audit: `fleet-m1`, `holodeck`, `s3paper`, `stitch`
  (attached — left alone).

## Oracle — the cloud arm (relay, stage-and-forward)

- OCI Ampere A1, hostname `ok`, 4 vCPU, 23 GiB RAM (3 used /
  20 available), disk 45 GiB with **13 GiB free (74%)** — tight, as
  recorded; up 24 days, load ~0.2.
- **No GPU** (verified in an earlier audit and unchanged: no NVIDIA
  device exists on this box).
- Seats: ZCode 3.16.3-40 (headless probe answered correctly on
  2026-10-27), MiniMax Code 0.7.0 (boots to Ready). `gh` authenticated
  as SuperInstance.
- Its weather role: datacentre-speed fetch-and-verify, then forward —
  the last mile home is the house pipe, not the Oracle.

## Subscription pools — quota-metered capacity

The fabric's fourth tier is not a box. Access points verified tonight:

| Pool | Tier (per Casey's ruling) | Verified access points |
|---|---|---|
| Z.AI (GLM) | premium | ZCode seats: Thor, Orin, ProArt, Oracle |
| MiniMax | premium | MCode seats: Thor, Orin, ProArt, Oracle |
| Kimi | premium | Kimi Code seat on the Thor (2.3.2) |
| Claude | fair | Claude Code 2.1.302 on the ProArt |

**Honest gap:** no CLI on any box reports remaining quota, and Stage 0
did not burn calls to probe balances. What the record does show,
twice in one day (the formal-paper revision pass and two adjudication
launches), is the Claude seat's session limit binding in practice —
pool exhaustion is a real, observed event, not a theory. Metering
these pools by observation is component 6's job (the fabric purse);
until then every estimate that spends premium tokens should say so.

## Discrepancies — record vs metal

1. **The Orin's disk.** Decision §2 argues storage placement from "the
   Orin's 7.84 GB"; the standing record likewise treats the Orin as
   storage-poor. The metal: a 2 TB NVMe, 1.7 TiB free. The placement
   ruling does not fall — its yield, reaction-path and locality legs
   stand on their own — but the storage leg was argued against a disk
   that does not exist, and no later estimate should cite the 7.84 GB
   figure. (The Orin's hostname is also `orin` now; the record says
   the rename was blocked awaiting a desk visit.)
2. **The Thor's NVMe tail.** The decision's estimate cues and §2's
   composed-log math use a 28 GiB tail ("fills in ~21 h"). Tonight the
   tail is 184 GiB, after the cold librarian's moves. The cure the
   adjudication prescribed (persistence classes + the Toshiba shelf as
   the log's home) remains right; the *urgency arithmetic* should be
   re-run from 184 GiB before component 3 sizes anything.
3. **The Orin's remote-desktop door is down** (x11vnc failed since
   2026-10-25) behind an active noVNC service — a half-green service
   list masking a broken door, exactly the failure shape the door
   standard exists to catch.
4. Smaller, in the fleet's favour: **the JEV rack's weights are
   loaded** (ijepa, vjepa2, judge all `true`) where the record still
   says "downloading"; **a fast local tier already exists** on the
   Thor (:8092, LFM2-1.2B) that the standing service list omits; the
   NemoClaw gateway is healthy in Docker though its **`agent` tmux
   door session is absent** (the web/Telegram doors are the live ones);
   Kimi Code on the Thor is 2.3.2, a patch above the recorded 2.3.1.
