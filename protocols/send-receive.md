# Protocol: send / receive

*Seeds §12, §21, §22. SCAFFOLD.*

Shared state is minted only from agreed **sends and receives** — nothing
else exists between cells (the piping discipline). Every crossing of a cell
boundary is one of these messages, and every one of them is a ledger entry:
the ledger is nothing more than the ordered record of sends and receives,
which is what makes any interaction findable, rewindable, and gradable.

A **send** is written by the sender when the message leaves; the matching
**receive** is written by the receiver when it is accepted (schema-valid and
acted on, or schema-valid and refused *by rule* — a refusal is still a
receive, with `accepted: false` and a `reason`). A send with no receive is
an unminted intention: it does not change shared state.

## Fields

- `id` — unique per send (`"<from>:<tick>:<seq>"` is a fine shape).
- `from`, `to` — cell slugs (rooms, residents, resources, the console).
- `tick` — the sender's logical tick.
- `what` — the message kind: `tick` (a perception, see tick.md), `order`
  (an instruction), `request` (a question or a resource claim), `roll`
  (a dice result, §22), `refusal` (a named, total refusal), or `note`
  (anything else, kept rare).
- `payload` — the body; its shape is fixed per `what` by the receiving
  cell's manifest. For `roll`, the payload MUST carry `options` (a map of
  option → probability, summing to 1), `table` (the table rolled against),
  and `picked`.
- `priority` — optional; when present it is a **purse spend** (§9): the
  amount of budget the sender pays for queue position. Unpriced priority is
  not representable in this protocol, on purpose.
