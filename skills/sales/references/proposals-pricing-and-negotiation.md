# Proposals, pricing presentation, and negotiation

Purpose: presenting and negotiating a specific price inside a live deal — a different territory
from how a price is designed and shown to a self-serve visitor. Covers the anchor-first debate
(contested, not a rule), the estimated-vs-quoted precision limit on a deal's stated value, and
discounting discipline tied to sales-pipeline health rather than deal-by-deal pressure.

Read when: building a proposal or quote; deciding whether to name a price first in a negotiation;
setting discounting policy; explaining why a sales pipeline's dollar total is not one trustworthy
number.

Skip when: how price tiers and page psychology are designed and shown to a self-serve visitor (→
product's `business-model.md`); objection handling and battlecards generally (→
`objections-and-enablement.md`); a deal's stage/exit-criteria structure and pipeline hygiene (→
`crm-and-pipeline.md`); contract or legal review of negotiated terms (out of this family entirely —
§6).

Inputs: the deal's stated value (know whether it's estimated or quoted), the counterpart's apparent
information position, any discount already on the table, the seller's own close-date pressure.

Produces: a stated position on anchoring (contested, with boundary conditions, never a rule), a
discipline for keeping estimated and quoted amounts distinct, and a discounting rule tied to
pipeline volume rather than single-deal pressure.

## Contents
1. Pricing presentation vs. pricing design — the seam · 2. Anchor-first: contested, not a rule ·
3. The forecast-date lever · 4. Estimated until quoted · 5. Discounting discipline · 6. Out of
family · 7. Never-ship

---

## 1. Pricing presentation vs. pricing design — the seam

Two different things share the word "pricing," and the family already drew the line once, by what
it chose not to lift. The retiring `webdesign` skill's anchoring, decoy-effect, charm-pricing, and
three-tier-psychology content was deliberately not carried into this family's sales territory: it
is **self-serve pricing-*page* content — a visitor reading tiers on a website, not a rep presenting
a quote in a live deal** (channel-E seam audit, `persuasion-and-conversion.md:106–124`). That
content is already homed in product's `business-model.md`, which teaches the identical psychological
mechanics for a self-serve reader. This file is the other side of that seam: a human presenting or
negotiating a specific number, to a specific counterpart, inside a specific deal. The same
vocabulary — anchoring, framing — appears on both sides of the line; say which side you're on
before using it.

## 2. Anchor-first: contested, not a rule

Whether to name a price first is genuinely disputed in the peer-reviewed evidence, and both sides
are permalinked — this ships as contested doctrine with boundary conditions, never as advice to
always or never anchor.

- **Schweinsberg et al. (2023), *PNAS*** — 26 million eBay negotiations: anchoring produces a
  *linear* effect on the price achieved but a **nonlinear** effect on the risk the negotiation
  collapses entirely, a shape the authors describe as "incompatible with current theorizing."
  Aggressive anchoring buys a better price at a disproportionately rising risk of no deal at all.
  (Consumer marketplace, buyer-side offers — the *shape* of the finding transfers to a sales
  negotiation; the specific numbers do not.)
- **Maaravi & Levy (2017), *Judgment and Decision Making*** — under **information asymmetry**, it
  is actually preferable for *both* counterparts not to give the first offer.

The boundary condition to carry, not smooth over: Schweinsberg's finding supports anchoring when
the relationship can absorb some impasse risk and the anchoring party has good price information;
Maaravi's argues against it when either side doesn't know enough to set a defensible number. A rep
who always anchors first, or who never does, is applying one paper's finding outside the condition
that produced it.

## 3. The forecast-date lever

A concrete first-person exhibit of what happens when the seller's own timeline becomes the
counterpart's leverage:

> "Got a massive deal out there with a 9/30 close date. After we got asked for our best & final
> twice, they are now trying to negotiate a 3rd time, with a new person. Hardest thing to do in
> sales but you have to know your drop dead number & what thresholds cannot be crossed."
> — [@BrianLaManna_](https://x.com/BrianLaManna_/status/1972968791828000962), 2025-09-30

Two teachings sit in one exhibit: a **pre-committed walk-away number**, decided before the pressure
arrives rather than during it; and the mechanism itself — a quarter-end or forecast-committed close
date is not neutral information once the other side knows it exists, it is a lever they can and
will use. This connects directly to `forecasting-honesty.md`'s sandbagging evidence (Lawrence et
al. 2006: forecasts get "made to happen" under internal pressure) — the same pressure that produces
sandbagging on the seller's side of a forecast is exactly what a counterpart can apply from the
buyer's side of a negotiation.

## 4. Estimated until quoted

A sales pipeline's dollar total is not one kind of number. GitLab's own booking-metric field logic
states the distinction directly:

> "The goal of this code is populate the Bookings Metrics field on the Opportunity based on data
> from the Zuora Quote family of objects. **If Zuora data is not present then use an estimated Net
> ARR amount until the deal is quoted.**"
> — [GitLab handbook, SFDC booking-metric fields](https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/sales-systems/gtm-technical-documentation/sfdc-booking-metric-fields.md)
> (PRIMARY, permalinked)

A deal's stated dollar value is an **estimate until a quote or proposal exists**, at which point it
becomes a firm figure with a paper trail behind it. Every pipeline total therefore mixes estimated
and quoted amounts, and the total alone never discloses that ratio. **The proposal is the event
that converts an estimate into a quote** — which is why building the proposal itself lives in this
file rather than in `crm-and-pipeline.md`; the pipeline-hygiene consequences of the
estimated/quoted split (what a CRM record should track, how a total should be reported) belong
there — cite this exhibit if writing that section, rather than re-deriving it.
`assets/stage_exit_criteria_audit.md` audits the split stage by stage and points back here.

## 5. Discounting discipline

Discount pressure is a pipeline-health problem before it is a negotiation-tactics problem:

> "When I have a surplus of pipeline: -Disqualifying properly -Keeping stronger price integrity
> -Holding the line on our buyer process."
> — [@BrianLaManna_](https://x.com/BrianLaManna_/status/2038250214230814796), 2026-03-29

The causal direction stated runs pipeline volume → price discipline, not the reverse: a rep
desperate for *any* deal, because the pipeline behind it is thin, is the rep who discounts. §3's
pre-committed walk-away number is the individual-deal mechanism; this is the structural one — the
fix for chronic discounting is more and better-qualified pipeline, not a sharper negotiation
script. If pipeline volume looks adequate on paper but discounting pressure persists, check whether
stalled deals are being counted as live rather than disqualified — the disqualification-as-a-
first-class-state pattern belongs to `crm-and-pipeline.md`.

## 6. Out of family

**Legal review of contract terms, MSAs, and negotiated legal language is out of this family's
scope entirely.** No sibling pack claims it, and this pack does not either — route it to counsel.
Do not let a proposal's business terms (§4's estimated/quoted split, §5's discount thresholds)
blur into an implied claim that this pack can validate legal enforceability.

## 7. Never-ship

- Any bare pricing-psychology "science" figure presented as settled — e.g., an unattributed "the
  science says $9.99 beats $10" claim circulates in this corpus's founder-led material with no
  study named ([@dvassallo](https://x.com/dvassallo/status/1531338262333165569), FOLKLORE). Grading
  charm-pricing and page-psychology claims in full is the design-side literature's job
  (product/design territory), not this file's — this file only draws the seam (§1).
- Anchor-first stated as a rule in either direction — it is contested with boundary conditions
  (§2), never a should-always/should-never instruction.
- GitLab's "33% win rate" used as evidence for what to concede in a negotiation — it is a
  planning-only assumption (`forecasting-honesty.md`), never a forecast-accuracy claim, and has
  nothing to say about any individual deal.
- A bare pipeline dollar total presented as a single trustworthy number without the estimated/quoted
  disclosure (§4).

## Validation

- Anchor-first guidance always carries both permalinked positions and their boundary conditions —
  never ships as a bare rule.
- Any deal-value figure states whether it is estimated or quoted before it is used in an argument
  or reported as a total.
- Pricing-page psychology and live-deal pricing presentation are never merged into one claim (§1).

## Failure modes and handoff

- **"Should I anchor first?"** — no single answer; walk through §2's boundary conditions against
  the reader's actual information position and tolerance for impasse risk.
- **Self-serve pricing page, tiers, or page psychology** — → product's `business-model.md`; not
  this file.
- **Whether pipeline hygiene or automation is the fix for a messy total** — →
  `crm-and-pipeline.md`.
- **Contract or legal terms** — out of family; route to counsel (§6).
