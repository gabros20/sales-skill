# Handoff

Purpose: Map every seam between `sales` and the rest of the family from sales's side — the three
mirror rows siblings pre-drew before sales shipped, and the two siblings that cede in prose only.

Read when:
- Downstream or upstream work is expected: a sibling pack will act on something sales produced, or
  sales needs an artifact a sibling owns.
- A request looks like it belongs partly to sales and partly to another pack, and the boundary
  needs naming rather than assuming.
- A stalled or contested seam needs its exact wording, not a paraphrase — the contested `success`
  row especially.

Skip when:
- The request is fully inside one job with no downstream consumer in view — do the work in the
  relevant job reference and stop.

Inputs: whichever job produced the artifact in question, and which sibling pack is the named next
consumer or prior producer.

Produces: a named handoff — artifact, owner, and the line sales does not cross — not a
restatement of the artifact itself.

## Contents

- The seam map (three mirror rows)
- The sales↔success worked example: GitLab's parallel roles
- `product` and `automation`: deliberate silence, not absence
- Dunning and billing: routed, never claimed as sales's own position
- Validation
- Failure modes

## The seam map

Marketing, growth, and success all pre-drew a row for `sales` before this pack existed — sales
mirrors each one back, matching its hedge exactly rather than flattening or re-hedging it.

| Sibling | What `sales` hands it | What `sales` consumes from it | The line `sales` does not cross |
|---|---|---|---|
| `marketing` | Pipeline and close-rate signal that feeds positioning and message iteration | Qualified demand — a defined fit-plus-intent signal on a named account or contact — plus the assets sales pulls from (case studies, competitive positioning) | Sales does not create or capture demand, and does not own the ICP *definition* — it inherits marketing's ICP-as-a-funnel model and applies it to account selection (see [icp-and-qualification](icp-and-qualification.md)). Marketing's own line: it "does not run the outbound sequence or own the CRM pipeline stage" (`marketing/references/surface-b2b-sales-assisted.md:58`). Sales cites marketing's shipped deliverability and consent doctrine, never restates it (`marketing/references/lifecycle-and-email.md` §1, `marketing/assets/email-compliance-checklist.md`) |
| `growth` (provisional) | Pipeline and qualification signal shaping which stage of a sales-assisted funnel is worth testing | An experiment readout on a funnel stage that touches a sales-assisted deal | This seam is drawn provisionally, the way marketing drew its own — cold outbound, CRM stages, and deal mechanics stay `sales`'s **regardless of which funnel stage an experiment touches** (`growth/references/handoff.md:42`). Sales does not read a funnel-stage result's confidence into a deal-stage outcome growth didn't test (`growth/references/surface-b2b-sales-assisted.md:112-113`) |
| `success` (contested) | The expansion sale itself, closed by sales in a sales-assisted motion | The renewal workflow, up to a complex deal that needs negotiation | Contested, not settled, exactly as success's own file states it: sales closes the expansion sale in a sales-assisted motion, **and** Lincoln Murphy's complexity-gated CS-native position is live and citable — a CSM renews by default, only genuinely complex renewals route to a dedicated CS-native resource, explicitly *not* "Account Management carryover." Sales does not adjudicate the industry fight either (`success/references/renewals-and-expansion.md:117-124`; the provisional mark is a checked invariant in success's own Validation sections, `renewals-and-expansion.md:138-139` and `surface-b2b-high-touch.md:154`) |

The hedge is written twice for each hedged row, never once: as the parenthetical after the pack
name, and restated in prose opening the fourth column. Marketing's row carries no hedge because
marketing's own cession carries none — mirroring it with a hedge would weaken a seam marketing
deliberately drew hard (`marketing/references/surface-b2b-sales-assisted.md:51-56`), and would be
a defect in this file, not a caution.

## The sales↔success worked example: GitLab's parallel roles

GitLab's public handbook is a real instance of this split, not an adjudication of it. The CSM is
introduced by the Solutions Architect at **3-Technical Evaluation or 4-Proposal**, and full
responsibility transfers to the CSM at **Closed Won**
(`content/handbook/customer-success/pre-sales-post-sales-transition.md`,
https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/customer-success/pre-sales-post-sales-transition.md,
CC BY-SA 4.0). Formality scales with deal size: at **$50K+** the SA/AE formally introduce the CSM;
under $50K, the SA and AE simply prepare the account for digital onboarding emails
(`content/handbook/sales/commercial/comm-sales-opp-stages/_index.md`, stage 6, same handbook). On
the renewal side, the CSM tracks renewal dates and schedules two Renewal Review meetings — one at
five months out, one at three months out — while the SAE/AE runs the expansion engagement and
presents pricing (`content/handbook/sales/sales-operating-procedures/retain-and-expand.md` §4,
https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/sales-operating-procedures/retain-and-expand.md,
same handbook).

**This exhibit does not travel without its own qualifying sentence.** GitLab's text states the
roles are deliberately parallel, not sequential: *"the roles and responsibilities of the
CSM/PSE/AE/SAE run parallel and it is very important that all roles work together."* Citing the
stage split without that sentence would cite a source as drawing a hard line it explicitly refuses
to draw. GitLab is also one enterprise, sales-assisted, high-ACV company — its worked example
corroborates the provisional split above; it says nothing about the CS-native or lower-touch
motions Murphy's contested position concerns, and does not reach far enough to adjudicate them.

## `product` and `automation`: deliberate silence, not absence

Only three sibling `handoff.md` files reciprocate a `sales` row — marketing, growth, success.
`product` cedes "qualification and CRM to `sales`" in prose (`product/SKILL.md:27`) rather than a
handoff row, and `automation` names the gap explicitly in its own file: the business rule behind a
customer-facing action is "owned by `product`, `marketing`, `sales`, or `success`," and "at this
pack's launch those three commercial upstreams do not yet exist as shipped skills"
(`automation/references/process-capture.md:15`). Both statements were accurate when written.
`product`'s cession stays accurate, but automation's "do not yet exist as shipped skills" sentence is
now stale: `product` and `marketing` are both shipped on disk, and this pack shipping makes
automation's claim more false, not less. That is a sibling-repair item queued on the family's memory
for automation to clear at this pack's release (synthesis §9) — it is not an edit this pack makes
itself, and their silence in this file should not be read as an oversight.

## Dunning and billing: routed, never claimed as sales's own position

If a deal stalls on a failed payment, route it to `product` — but **per success's and marketing's
documented position, not as sales's own finding.** `success/SKILL.md:95` and
`marketing/references/lifecycle-and-email.md:15` both assign dunning/billing-failure recovery to
`product`; `product`'s own pack contains zero occurrences of either word. This is not sales's
territory to claim either way — cite the two siblings that made the assignment, never state that
product says so itself.

## Validation

- Each hedged row writes its hedge twice — as the parenthetical after the pack name, and again in
  prose opening the fourth column — and the unhedged `marketing` row writes none.
- The `success` row carries both positions and states that sales does not adjudicate between them.
- Any citation of GitLab's stage split or retain-and-expand section carries the "run parallel"
  sentence.
- Every sibling file:line cite was re-grepped against the live sibling pack before shipping —
  quotes survive drift, line numbers don't.
- Dunning routing is attributed to success and marketing, never to `product` itself.

## Failure modes

- Flattening the `success` row into a firm claim in either direction — sales does not get to
  resolve the industry fight quietly in its own favor; that breaks a checked invariant in a
  shipped sibling.
- Adding a hedge to the `marketing` row. Marketing's cession has none; matching its confidence is
  the correct mirror, not a caution to soften.
- Collapsing growth's two distinct hedges into one — growth hedges *whether the seam sits in the
  right place*, never *whether deal mechanics are sales's*. The unconditional clause stays
  unconditional even inside a provisional row.
- Citing GitLab's stage-3/4 handoff or retain-and-expand split without the "run parallel" sentence,
  or presenting it as evidence for the contested seam rather than as one worked example inside it.
- Stating that `product` claims dunning/billing ownership — it never has; the assignment is
  one-directional from success and marketing.
- Reading `product`'s or `automation`'s missing row as evidence sales has no seam there — both
  cede in prose, on record, before this pack shipped.
