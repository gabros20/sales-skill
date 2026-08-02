# Stage exit-criteria audit sheet

Run this per pipeline stage, not per deal. It exists because almost no CRM tool can express exit
criteria as a first-class field — of eight open CRMs surveyed, only Odoo's `crm.stage.requirements`
models it at all, and even Odoo ships it empty by default (`addons/crm/models/crm_stage.py`,
https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/addons/crm/models/crm_stage.py,
LGPLv3). The tool will not remind you this is missing. This sheet does.
See [crm-and-pipeline](../references/crm-and-pipeline.md) for the full finding this audit operationalizes.

## How to use it

Copy the table below once per stage in your own pipeline. Answer every row honestly — "we don't
have one" is a valid, useful answer; a blank left unanswered is not. Re-run this audit whenever a
stage definition changes, not just at pipeline setup.

## Per-stage audit

| Stage name: _______________ | Answer | Notes |
|---|---|---|
| **Positive exit criteria exist** — is there a written, checkable condition that must be true before a deal advances *out* of this stage? (Not a label, not a percentage — a fact a rep can verify.) | Yes / No | If No: this stage is a label, not a gate. |
| **The criteria are checkable by someone other than the rep** — could a manager or a peer verify the condition without asking the rep to self-report? | Yes / No | GitLab's exit criteria are things like "recap email sent," "demo output shared" — verifiable artifacts, not a rep's confidence level. |
| **Negative exit criteria are applied** — has the deal been checked against reasons to *refuse* forecasting it, not just reasons to advance it? | Yes / No | Use KyleAsay's three: no velocity, no concerns ("no concerns often means no consideration"), no next-best-option. See [forecasting-honesty](../references/forecasting-honesty.md). |
| **Estimated-vs-quoted split is visible** — for the dollar value attached to this deal, is it clear whether the amount is a firm quote or a working estimate? | Estimated / Quoted / Unclear | GitLab's own pipeline mixes "Estimated Net ARR" and quote-sourced amounts without disclosing the ratio in the total — this row exists so your own pipeline doesn't repeat that silently. The proposal is the event that converts an estimate into a quote: see [proposals-pricing-and-negotiation](../references/proposals-pricing-and-negotiation.md) §4. |
| **A stalled-but-not-lost state exists** — can this deal sit in a "delayed" state, or does it have to be marked won, lost, or left artificially "active" while going nowhere? | Named state exists / Forced binary | atomic-crm's `Delayed` stage is the exhibit; most CRMs examined force a binary. |
| **An aging rule exists for this stage** — is there a defined point at which an inactive deal in this stage gets flagged or auto-closed? | Yes / No + threshold | GitLab auto-closes New Business deals in `1-Discovery`/`2-Scoping` on a segment-tiered clock (SMB 7/15 days, Mid-Market 21/45, Large/PubSec 45/90). Pick a threshold that fits your own velocity — see [surface-smb-transactional](../references/surface-smb-transactional.md) for the segment-tiered exhibit. |

## Worked example — one stage, honestly audited

A solo founder or small team running the stage they call "Evaluating" might fill this in as:

| Stage name: Evaluating | Answer | Notes |
|---|---|---|
| Positive exit criteria exist | No | The stage means "they said they'd look at it." No defined next action. |
| Checkable by someone other than the rep | No | Follows from the row above — there's nothing written to check. |
| Negative exit criteria applied | Yes | No next-best-option check catches most of what sits here; several deals have been sitting untouched for weeks with no competing option named. |
| Estimated-vs-quoted split visible | Estimated | Nothing here has a quote attached yet — that's consistent with the stage name, not a hidden problem. |
| Stalled-but-not-lost state exists | Forced binary | The tool only offers Won/Lost; three deals are functionally stalled but marked "active," inflating the pipeline total. |
| Aging rule exists | No | No threshold set anywhere. |

**What this audit changed:** nothing in the pipeline moved, but two facts that were previously
invisible are now written down — "Evaluating" is a label, and the pipeline total includes at least
three deals that should be discounted or flagged. That is the audit doing its job: it does not fix
the pipeline, it makes its actual state legible before a forecast is built on top of it. Pick an
aging threshold (see [surface-smb-transactional](../references/surface-smb-transactional.md) for
GitLab's segment-tiered exhibit as a starting reference, not a rule to copy verbatim) and decide
whether "Evaluating" needs a real exit criterion or should be merged into an adjacent stage that
already has one.

## What a "no" answer means, precisely

A "No" on the first row does not mean the stage is useless — it means the stage is currently a
label, and any probability or forecast weight attached to it is a hand-set number with no
verification behind it, not a measurement. That is not a defect unique to your pipeline; it is the
default state of stage-weighted forecasting everywhere this pack's research looked (see
[forecasting-honesty](../references/forecasting-honesty.md) for the full null). The point of this
sheet is to make that state visible and chosen, not to shame it away — some stages genuinely don't
need a hard gate. The failure mode is not having a soft stage; it is not knowing which stages are
soft.

## Failure modes

- Running this audit once at pipeline setup and never again — a stage definition drifts as fast as
  anything else in a live CRM.
- Answering "Yes" to the first row because a stage *has a name* — a label is not a criterion.
- Treating a "No" answer as something to hide rather than something to disclose when the
  pipeline's forecast is presented.
