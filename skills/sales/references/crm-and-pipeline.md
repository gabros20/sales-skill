# CRM and pipeline

Purpose: how to structure a deal pipeline (the set of open deals tracked toward close) — stages,
exit criteria, and hygiene — and what the open-source record says actually holds up.

Read when: designing or auditing pipeline stages, fields, or a loss-reason taxonomy; deciding
whether "CRM hygiene" work is worth the time it costs; choosing between a fixed stage model and a
customizable one.

Skip when: whether a stage-weighted number or coverage ratio means anything (→
`forecasting-honesty.md`); scoring why a specific deal was lost (→ `win-loss-learning.md`); how
data actually moves between systems (→ automation, which owns sync/write-path mechanics — this file
owns structure only, never the pipe).

Inputs: your current (or planned) stage list; whether any stage carries a stated requirement for
advancing past it; how many pipeline shapes you actually need (new business, renewal, expansion may
not be the same shape).

Produces: a stage/field design that names what a "CRM" is for in this pack (a structured system of
record for deal state, not a communications tool), and an honest verdict on hygiene. Audit an
existing pipeline stage-by-stage with [stage_exit_criteria_audit](../assets/stage_exit_criteria_audit.md).

## Contents
1. Structure is ours, sync is automation's · 2. The exit-criteria gap · 3. Stage design patterns
worth stealing · 4. Hygiene: no forward evidence, only backward · 5. Disqualification as a
first-class pipeline state · 6. Loss reasons as structured data

---

## 1. Structure is ours, sync is automation's

This file covers **CRM structure** — the stages, fields, required values, and loss-reason taxonomy
that make a deal pipeline legible. It does not cover the mechanics of getting data into or out of
that structure (webhooks, syncs, write-paths between tools) — that is automation's territory. If
you're wiring two systems together, this file names what the fields should mean; automation's pack
owns how they move.

## 2. The exit-criteria gap

GitLab publishes the single best stage-gate artifact found anywhere in this research: ten named
opportunity stages, each with a description, primary/secondary activities, **and an explicit Exit
Criteria list** — for example, stage 1-Discovery requires "Recap email sent to customer confirming
pain points, key stakeholders, next steps, project timeline" and a scheduled scoping meeting before
a deal may advance.
(https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/commercial/comm-sales-opp-stages/_index.md,
PRIMARY, CC BY-SA 4.0 handbook prose — quote-with-attribution is safe; a close derivative you ship
inherits ShareAlike.)

**No open-source CRM can express this.** Across eight CRMs examined — Twenty, EspoCRM, Odoo,
SuiteCRM, Krayin, atomic-crm, frappe/crm, and Monica (not a sales CRM at all) — exactly one models
per-stage requirements as a first-class field: Odoo's `crm.stage.requirements`, a free-text tooltip.
**And even Odoo ships it empty** — the default seed data sets no value on any of its four stages.
(https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/addons/crm/models/crm_stage.py,
PRIMARY, LGPLv3.) Every other CRM's stage is a `{value, label, position, [probability]}` record — a
label, not a gate. This survives the vendor's own documentation, not just the code: EspoCRM's
published docs state "Each stage is mapped to the Status field value. Each stage is stored as an
entity" — in other words, a stage is a named entity mapped to a status value, with an ordering
constraint, and nothing more. (https://github.com/espocrm/documentation/blob/9ff984348d31b0fc51bfa1c5bdf83aec83a0d051/docs/general/pipelines.md,
UNLICENSED — cite and quote minimally, do not reproduce or build a derivative asset from it.)

**The honest statement: GitLab's exit criteria are a real process artifact that the tool ecosystem
cannot represent.** If your pipeline needs gates, they live in a checklist, a doc, or a human
review — not in the CRM's stage field, because the CRM's stage field is a label everywhere this
research looked.

## 3. Stage design patterns worth stealing

**A pipeline is not one shape.** GitLab itself runs at least two — new business and
renewal/expansion are handled through different operating procedures, not the same stage list.
EspoCRM's own product agrees at the tooling level: as of v10.0 it lets one entity type carry
*multiple* pipelines, each with its own stages, "available for all users or only for specific
teams" — an existence proof that multi-pipeline modeling is a real, shipped answer, not an exotic
one. (Same EspoCRM documentation permalink as §2; UNLICENSED, cite only.)

**Twenty treats every stage as user-editable metadata, not a fixed schema.** Its default five-stage
Opportunity pipeline (New → Screening → Meeting → Proposal → Customer) is a trivially overridable
default, not a baked-in model — worth citing as the "customizable object" pattern, distinct from
every other CRM examined, which hard-codes an enum.
(https://github.com/twentyhq/twenty/blob/b754e15331c6472d772b1bbe448469f811b28afd/packages/twenty-server/src/engine/workspace-manager/twenty-standard-application/utils/field-metadata/compute-opportunity-standard-flat-field-metadata.util.ts,
PRIMARY; AGPLv3 core, with MIT-licensed toolkit packages — check per-package before reusing code.)

**atomic-crm ships a `Delayed` stage** — the only CRM in this corpus that acknowledges a deal can
stall without being formally lost, alongside the usual Won/Lost.
(https://github.com/marmelab/atomic-crm/blob/167a4cdb652b1ab2b4b030831cfa7adcf2099321/src/components/atomic-crm/root/defaultConfiguration.ts,
PRIMARY, MIT.) A stalled state is cheap to add and closes a real gap: most stage lists force a
choice between "still open" and "dead" with nothing in between.

**frappe/crm tracks first-response SLA on deals, not just on leads** — response-time fields
(`first_response_time`, `sla_status`) attached to the deal record itself, unusual among the CRMs
examined, most of which track responsiveness only pre-conversion.
(https://github.com/frappe/crm/blob/66165cb1dae46bd02f5899baeb30f05df7b6098e/crm/fcrm/doctype/crm_deal/crm_deal.json,
PRIMARY, AGPLv3.) Worth adding if responsiveness inside an active deal is a signal you'd otherwise
lose.

## 4. Hygiene: no forward evidence, only backward

CRM-hygiene doctrine — keep the pipeline current, log every interaction, close stale deals promptly
— circulates as an assumed good. **No practitioner exhibit found in this research shows hygiene
improving an outcome.** What was found runs the other direction, from named practitioners:

> "John Bristow is one of the best sellers I've ever met. $200M+ closed in revenue. … (Except his
> terrible Salesforce hygiene)"
> — @BrianLaManna_ (https://x.com/BrianLaManna_/status/2062516506601148869)

An AE coach who works with reps on Performance Improvement Plans classifies "CRM hygiene before
lunch" as noise, not signal, in his own coaching framework
(https://x.com/mistamor/status/2070190497910469003). **State this honestly rather than repeating the
doctrine: hygiene may still be worth doing for reasons other than performance (accurate reporting,
forecast inputs, handoff quality), but no evidence in this corpus ties it to close rates or
attainment.** Don't claim what isn't there.

**One real, numeric hygiene mechanism does exist and is worth adopting as-is**: GitLab's
segment-differentiated pipeline-aging automation, which auto-closes stalled early-stage deals on a
fixed clock —

> "Large/PubSec: Day 45 / Day 90 — Mid-Market: Day 21 / Day 45 — SMB: Day 7 / Day 15" (inactivity
> warning / auto-closure), closing with reason "No Progression-Auto Close."
> (https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md,
> PRIMARY, CC BY-SA 4.0)

This is a mechanism, not an outcome claim — it doesn't assert that auto-closing stale deals improves
win rate, only that it keeps the pipeline's active count honest. Cite it for what it is.

The same honesty runs as three mechanical flags any pipeline can carry at any scale — "flag every
deal with no next step, no recent activity, or a close date that has already passed"
(x.com/AlfieJCarter/status/2065482113768407079, inside a promotion for a sales-skill bundle:
VENDOR-SELF-REPORTED, no outcome claimed). The third is the forecast-honesty one: an open deal whose
close date has passed is a prediction that already failed. Score the miss in the predict-then-score
log (`forecasting-honesty.md` §6) before re-dating it; a silently moved close date erases the only
calibration data a small pipeline produces.

## 5. Disqualification as a first-class pipeline state

A concrete, low-cost pattern: treat "not pursuing this" as its own bucket rather than letting dead
deals rot in an active stage.

> "The best thing I ever did for my pipeline was add an 'Unfortunately Nope' category. Not every
> account deserves your energy. The hardest skill in enterprise sales isn't opening deals. It's
> having the discipline to deprioritize the ones that aren't going anywhere."
> — @BrianLaManna_ (https://x.com/BrianLaManna_/status/2056031787588166039, FIRST-PERSON RESULT —
> practice, not a measured outcome)

Pairs with §3's `Delayed`/stalled pattern: a pipeline with only Won/Lost forces every stuck deal to
either look alive or be prematurely killed. A third bucket for "not now" or "not pursuing" is cheap
and matches what open designs already do.

## 6. Loss reasons as structured data

GitLab requires a named loss reason on every closed-lost opportunity, with follow-up fields for two
categories — **Competitive Loss** (requires naming the competitor) and **Product Maturity**
(requires the product-line stage) — plus a dollar-gated requirement to write qualitative detail on
losses of $25,000+ Net ARR.
(https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md,
PRIMARY.) The full picklist itself lives in a gated internal deck — only the process and these two
category names are public — but the structure is the citable part: a required reason field plus a
dollar threshold for detail is adoptable at any scale.

Krayin's `lost_reason` field is the equivalent at open-source-CRM scale: a structured (not free-text)
lookup tied to the same pattern as its lead-source list (`krayin/laravel-crm`,
`packages/Webkul/Lead/src/Models/Lead.php`, read at pinned commit
`6ad119ee031636c6e250668a73483110a26f7ad3`; PRIMARY, MIT). Structured loss reasons feed win-loss
learning directly — see `win-loss-learning.md`
for what to do with them once collected, since a loss-reason field only captures a stated reason,
and a stated reason is not the same thing as the actual cause.

## Validation

- Every stage or field pattern cited names its source CRM and license; nothing here presents a
  hand-set probability lookup table (EspoCRM, SuiteCRM, Krayin's default, frappe/crm) as validated —
  see `forecasting-honesty.md` for why a hand-set weight can't be validated at solo scale.
- No hygiene claim ships without noting the absence of forward evidence (§4).
- "CRM" in this file never means sync/write-path mechanics — that boundary is stated, not implied.

## Failure modes and handoff

- **Wants a CRM tool recommendation** — out of scope; this file covers structure, not vendor
  selection.
- **Wants to know if a stage-weighted number is trustworthy** — → `forecasting-honesty.md`.
- **Wants to interpret a batch of loss reasons** — → `win-loss-learning.md`.
- **Wants to automate data moving between the CRM and another tool** — → automation, which owns
  sync/write-path mechanics.
