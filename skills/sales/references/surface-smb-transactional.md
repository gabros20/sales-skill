# Surface: SMB Transactional

Purpose: State how the sales motion changes once a real sales team exists but per-deal value stays
small — a repeatable, velocity-driven motion where the solo founder's friction gate has mostly
resolved, and enterprise's stage-gate discipline would be disproportionate overhead.

Read when:
- A team of reps runs a high-volume, lower-ACV motion — many deals moving fast, none individually
  large enough to justify a formal qualification framework.
- The question is how much process to carry at speed: which hygiene disciplines stay, which
  enterprise machinery to skip, and why.

Skip when:
- One person is closing their own deals — go to [surface-founder-led-solo](surface-founder-led-solo.md),
  the DEFAULT surface.
- The deal is large, multi-stakeholder, or needs a named qualification framework — go to
  [surface-enterprise-team](surface-enterprise-team.md).

Inputs: a qualified lead or account (inherited ICP fit signal, per [icp-and-qualification](icp-and-qualification.md)).

Produces: velocity-motion guidance — what hygiene discipline survives at speed, what enterprise
overhead to deliberately not carry, and where to draw the aging/hygiene line.

## Contents

- What relaxes from founder-led-solo, and why
- Velocity as the operating discipline
- Qualification, compressed but not skipped
- Forecast caution: more deals is not more calibration
- Failure modes

## 1. What relaxes from founder-led-solo, and why

A team now exists, so the pure existence-gate question (should there be a sales motion at all?)
is settled — but per-deal value stays low enough that the enterprise motion's overhead is not
worth carrying either. GitLab's own published qualification discipline is the direct license for
this: MEDDPPICC and Close Plan detail are only *required* fields above a stated ARR threshold
("$100K+ for Enterprise, $50K+ for Mid-Market" — `content/handbook/sales/command-of-the-message/command-plan.md`,
https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/command-of-the-message/command-plan.md,
GitLab handbook, CC BY-SA 4.0). Below that line, GitLab does not run the full framework either.
Importing a nine-letter qualification framework onto a sub-threshold SMB deal is not rigor, it is
overhead the framework's own publisher doesn't apply at that size — see
[icp-and-qualification](icp-and-qualification.md) for the frameworks-vs-methods taxonomy and the
MEDDPICC ruling this exhibit sits alongside.

## 2. Velocity as the operating discipline

What replaces heavy qualification at this surface is speed discipline, and two open CRMs model it
concretely (both read in full at the field-definition level):

- **frappe/crm tracks SLA and first-response time on deals, not just leads** — `sla`,
  `sla_creation`, `sla_status`, `communication_status`, `response_by`, `first_response_time`,
  `rolling_responses` are first-class fields on the deal object itself
  (`crm/fcrm/doctype/crm_deal/crm_deal.json`,
  https://github.com/frappe/crm/blob/66165cb1dae46bd02f5899baeb30f05df7b6098e/crm/fcrm/doctype/crm_deal/crm_deal.json,
  AGPLv3). Most CRMs examined track responsiveness on leads and tickets, not on in-flight deals —
  treating a stalled reply as a pipeline-health signal, not just an inbox metric, is the pattern
  worth adopting regardless of which CRM tool is in use.
- **atomic-crm ships a `Delayed` stage** alongside Won/Lost
  (`src/components/atomic-crm/root/defaultConfiguration.ts`,
  https://github.com/marmelab/atomic-crm/blob/167a4cdb652b1ab2b4b030831cfa7adcf2099321/src/components/atomic-crm/root/defaultConfiguration.ts,
  MIT) — the only one of eight open CRMs surveyed that names a stall without forcing a premature
  won/lost call. At velocity, a named "stalled, not lost" bucket keeps aging reports honest
  instead of either abandoning a live deal too early or leaving a dead one inflating the pipeline
  total.
- **GitLab's own aging/auto-close automation is segment-differentiated, and SMB gets the fastest
  clock of the three**: Large/PubSec warns at day 45, auto-closes at day 90; Mid-Market at 21/45;
  **SMB at day 7 warning, day 15 auto-close** to `8-Closed Lost` with reason "No Progression-Auto
  Close" (`content/handbook/sales/field-operations/gtm-resources/_index.md`,
  https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md,
  GitLab handbook, CC BY-SA 4.0). This is the concrete, published version of "velocity means
  faster hygiene enforcement" — not a house opinion, a real company's segment-tiered rule.

Cite [crm-and-pipeline](crm-and-pipeline.md) for the general stage/exit-criteria gap across CRM
tooling; this surface only carries the velocity-specific instances of it.

## 3. Qualification, compressed but not skipped

Compressing qualification is not the same as dropping it. The negative exit criteria this pack's
forecasting flagship teaches — no velocity, no concerns, no next-best-option
(see [forecasting-honesty](forecasting-honesty.md)) — cost nothing to apply at speed and catch the
same false-positive pipeline a heavier framework would, without the framework's overhead. Route a
lead through the inherited ICP fit signal (per [icp-and-qualification](icp-and-qualification.md))
before it enters this surface's fast clock; skipping fit-checking to hit velocity just moves the
same qualification failure downstream into a stalled or auto-closed deal.

## 4. Forecast caution: more deals is not more calibration

A high-volume motion tempts the assumption that more deals means a statistically sound forecast.
It does not, on its own: [forecasting-honesty](forecasting-honesty.md)'s small-numbers gate is a
property of a *tracked record*, not of deal count in a single quarter, and coverage math
(`assets/coverage_calc.py`) still requires the reader's own win rate, not an assumed one. Velocity
changes how fast bad pipeline gets flushed (§2's aging rules); it does not by itself make a
hand-set stage weight any more validated.

## Failure modes

- Applying MEDDPPICC or a similarly heavy framework to sub-threshold deals — GitLab's own
  ARR-gated Command Plan is the argument against it, not a house preference.
- Treating a `Delayed`/stalled deal as permanently open with no aging rule, or as automatically
  lost the moment it stalls — both lose real information the "stalled, not lost" pattern preserves.
- Reading SLA/first-response tracking as a forecast signal — it is a responsiveness/hygiene signal,
  not a probability computation; no CRM examined here computes forecast accuracy from it.
- Assuming a large deal count substitutes for calibration — see §4; cite
  [forecasting-honesty](forecasting-honesty.md) rather than asserting velocity solves this.
- Skipping the inherited-ICP fit check to move faster, then discovering the failure at the
  aging-rule stage instead of at intake.
