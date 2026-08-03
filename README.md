# sales — Sales

**Win the deal — and be honest about whether you can actually predict winning it.**

`sales` is the **Distribute** stage of the [Digital Product Skills](https://github.com/gabros20)
family, pairing with `marketing`: marketing creates and captures demand, `sales` converts it
through a buying process. It covers the jobs a product needs once a qualified prospect is in a
buying conversation — deciding whether an assisted sales motion should exist at all, account
selection and qualification, cold outbound and AI-outbound policy, discovery calls, demos,
objection handling and enablement, proposal/pricing presentation and negotiation, CRM structure and
deal-pipeline hygiene, forecasting, win/loss learning, and the expansion-sale close.

## What makes this pack different

Sales-skill packs already exist, and some cover most of the ground competently. What none of them
combine is coverage, depth, and real use — the packs that cover the domain broadly have little
adoption, and the ones people actually install cover only a slice of it. The largest one in this
space runs an 11,105-line commercial pack with no working links to any figure it cites, and its
stage-by-stage win-probability table — the thing a forecast actually runs on — traces back to a
single unlinked sentence.

This pack asks the question that gets skipped everywhere else: **can anyone actually show a sales
forecast was accurate, or only that it was well-reasoned?** The centerpiece reference,
[forecasting-honesty](skills/sales/references/forecasting-honesty.md) ⭐, checked the four best
places forecast accuracy would show up if it existed anywhere — one company keeps its actual method
private, a second publishes the fullest method found anywhere and still measures nothing, open CRM
tools carry stage-probability code with zero accuracy claims attached, and the most-cited forecasting
tool discloses its assumptions but never checks them against outcomes. Forecast *method* is
published everywhere. Forecast *accuracy* is published by no one. The pack teaches what to do
instead at the scale a small pipeline actually has: write down the prediction before you know the
outcome, then check it — the same discipline a second reference,
[win-loss-learning](skills/sales/references/win-loss-learning.md), applies to why deals were
actually lost, since a lost buyer's stated reason and an outside observer's guess turn out to be the
same plausible story, not independent evidence.

The rest of the pack starts from the front door most sales content skips: whether a dedicated sales
motion is worth running at all. [when-sales-applies](skills/sales/references/when-sales-applies.md)
teaches the four competing answers practitioners actually give — by deal stage count, by price
tier, by how much friction the customer will tolerate before buying, by how much of the founder's
own time it's already eating — as a real disagreement, not a single rule presented as settled.
Every other figure in the pack carries its evidence grade inline, and a long list of familiar sales
folklore ("57% of the buying decision happens before you talk to sales" turned into "the decision is
already made," "92% of salespeople give up after 4 follow-ups," the 21x-faster-lead-response claim,
"always be closing" as inherited wisdom) is checked against its original source and marked
never-ship where it fails, with the honest version taught in its place.

## Install

```bash
npx skills add gabros20/sales-skill -g -y
```

Or use it in Codex with `$sales`. Manual copy also works — copy `skills/sales/` into your client's
skills directory.

## Examples

```text
$sales we're two people, $40/mo per customer, and someone told us to hire an SDR — do we even need a sales motion?

$sales which of these 200 accounts should I actually spend time on, and should I be running MEDDIC on them?

$sales write a cold outbound sequence for CTOs at Series-B fintechs, and tell me what spam rate I have to stay under

$sales build me a Q3 bookings forecast from our open pipeline — and tell me how much I should trust it

$sales design our deal pipeline stages and the exit criteria for each one

$sales set up a win/loss interview program — what do we ask buyers after we lose?
```

## What it does

A **faceted router**: pick one primary job × one base surface, then add the agentic overlay only
when a model runs outbound, qualification, or a deal step without a human reviewing that instance.

**Primary jobs** — when-sales-applies · icp-and-qualification · outbound-and-prospecting ·
discovery-calls · demo-and-narrative · objections-and-enablement ·
proposals-pricing-and-negotiation · crm-and-pipeline · **forecasting-honesty ⭐** ·
win-loss-learning · expansion-sale close.

**Surfaces** — founder-led solo (default) · SMB transactional · enterprise/team ·
**agentic (additive)**.

## Route by job

| User intent | Reads | Contribution |
|---|---|---|
| Decide whether an assisted sales motion applies yet, and which gate governs | [when-sales-applies](skills/sales/references/when-sales-applies.md) | **The Existence Gate** — four incompatible practitioner answers taught as a real disagreement, plus where the gate is eroding as self-serve tools improve |
| Select or prioritize accounts, or set up a qualification framework | [icp-and-qualification](skills/sales/references/icp-and-qualification.md) | The ideal-customer profile inherited from `marketing`, never rebuilt from scratch; named frameworks (MEDDIC, MEDDPICC, BANT) versus methods (SPIN, Challenger, Sandler) kept distinct |
| Design or run cold outbound, or set an AI-outbound policy | [outbound-and-prospecting](skills/sales/references/outbound-and-prospecting.md) | The disclose-at-first-contact rule for AI-run outreach; the rule against manufacturing false engagement signals to beat spam filters |
| Run or structure a discovery call | [discovery-calls](skills/sales/references/discovery-calls.md) | What the evidence actually supports (asking real questions builds rapport) versus what no study has ever shown (that any one branded method wins more deals) |
| Build or run a product demo | [demo-and-narrative](skills/sales/references/demo-and-narrative.md) | The demo built as the answer to what discovery surfaced, not a fixed script, stated honestly against thin published evidence |
| Build a battlecard or objection library | [objections-and-enablement](skills/sales/references/objections-and-enablement.md) | Battlecard discipline fed by win/loss learning; no framework here is oversold as proven to change outcomes |
| Present pricing, write a proposal, or negotiate | [proposals-pricing-and-negotiation](skills/sales/references/proposals-pricing-and-negotiation.md) | Presenting and negotiating a price inside a live deal, not designing the price itself; the anchor-first question taught both ways with its evidence on each side |
| Design CRM stages or audit deal-pipeline hygiene | [crm-and-pipeline](skills/sales/references/crm-and-pipeline.md) | Real per-stage exit criteria as the missing piece most CRM tools can't hold; pipeline structure, kept separate from the sync mechanics that keep it up to date |
| Build or audit a pipeline forecast ⭐ | [forecasting-honesty](skills/sales/references/forecasting-honesty.md) | **The centerpiece.** Why a forecast that names its assumptions is still not the same thing as a forecast that's been checked against outcomes; the pipeline-coverage multiple derived from your own win rate instead of borrowed as a fixed constant; what a small pipeline can and can't validate |
| Run or design a win/loss program | [win-loss-learning](skills/sales/references/win-loss-learning.md) | Why a second opinion on a lost deal isn't independent evidence; the predict-then-score habit as the fix |
| Close an expansion or upsell deal on an existing account | [proposals-pricing-and-negotiation](skills/sales/references/proposals-pricing-and-negotiation.md) | The expansion sale run as a live negotiation against an existing relationship — what carries over from the original deal, and the boundary with `success`'s renewal position, carried forward rather than resolved silently |

Plus [handoff](skills/sales/references/handoff.md) — the map to the rest of the family, including
where sales and `success` disagree about who owns a renewal.

## Surfaces

| Surface | Reads | When |
|---|---|---|
| Founder-led solo — no reps, no dedicated CRM admin | [surface-founder-led-solo](skills/sales/references/surface-founder-led-solo.md) | **Default** |
| SMB transactional — repeatable, short-cycle deals across multiple reps | [surface-smb-transactional](skills/sales/references/surface-smb-transactional.md) | Deal size and cycle are short and coached, not enterprise procurement |
| Enterprise/team — named CRM admin, buying committees | [surface-enterprise-team](skills/sales/references/surface-enterprise-team.md) | Multi-stakeholder deals with a formal buying process, where the canon's full apparatus actually applies |
| **Agentic (additive overlay)** | [agentic](skills/sales/references/agentic.md) | **Stacks on a base surface.** A model runs outbound, qualification, or a deal step with no per-instance human review |

## Outputs

A sales artifact carries: the gate verdict, or a statement that a sales motion already applies ·
every figure with its source and evidence grade · the boundary — which sibling pack owns the
adjacent half, cited by pack and filename · and what the artifact **cannot** support: a forecast
with no track record behind it, a win rate with no denominator attached, a methodology with no
study showing it changes outcomes.

Gates, playbooks, policies, pipeline structures, forecasts, and handoffs are delivered as
documents — never as production code.

## Digital Product lifecycle

`sales` sits at the **Distribute** stage of the Digital Product Skills family, alongside
`marketing`: marketing creates and captures demand, `sales` converts qualified demand through a
buying process. It does not own demand creation, positioning, content, or deliverability
(`marketing`), funnel experiments on any stage including a sales-assisted one (`growth`),
pricing-tier design or dunning (`product`), the sales assistant's mechanics and evals (`ai`), or
CRM sync and write-path mechanics (`automation`). It consumes upstream artifacts — `marketing`'s
qualified-demand definition and ICP, `product`'s pricing tiers — when they're supplied, works
standalone when they aren't, and hands off a compact artifact, typically to `marketing` for a
qualified-demand loop, `growth` to test a funnel-stage change, `success` for the (contested)
expansion-to-renewal handoff, `product` for a pricing fix, or `automation` for CRM sync and
workflow wiring.

## The family

| Skill | Stage | Repository |
|---|---|---|
| `product` | Shape | [product-skill.vercel.app](https://product-skill.vercel.app) |
| `design` | Shape | [designskill.vercel.app](https://designskill.vercel.app) |
| `architecture` | Shape | [architecture-skill.vercel.app](https://architecture-skill.vercel.app) |
| `frontend` | Build | [frontendengskill.vercel.app](https://frontendengskill.vercel.app) |
| `backend` | Build | [backendengskill.vercel.app](https://backendengskill.vercel.app) |
| `data` | Build | [data-skill.vercel.app](https://data-skill.vercel.app) |
| `ai` | Build | [aiengskill.vercel.app](https://aiengskill.vercel.app) |
| `automation` | Build | [automation-skill.vercel.app](https://automation-skill.vercel.app) |
| `quality` | Assure | [quality-skill.vercel.app](https://quality-skill.vercel.app) |
| `operate` | Run | [operate-skill.vercel.app](https://operate-skill.vercel.app) |
| `marketing` | Distribute | [marketing-skill.vercel.app](https://marketing-skill.vercel.app) |
| `sales` | Distribute | [salesskill.vercel.app](https://salesskill.vercel.app) |
| `growth` | Improve | [growthskill.vercel.app](https://growthskill.vercel.app) |
| `success` | Improve | [success-skill.vercel.app](https://success-skill.vercel.app) |

All 14 packs are shipped.

## Reference and asset library

15 references under `skills/sales/references/` (11 primary jobs, 3 base surfaces, 1 agentic
overlay, 1 handoff contract) and 4 assets under `skills/sales/assets/`, all runnable and
self-testing except the two checklists:

- **Assets:** `coverage_calc.py` — pipeline coverage as 1 ÷ your own win rate, and it refuses to run
  without that win rate and its denominator · `forecast_calibration_check.py` — scores a log of
  predictions you made in advance against what actually happened, and refuses a verdict below an
  honest sample size · `loss_prediction_log.md` — a predict-then-score template for deals, with
  worked example rows · `stage_exit_criteria_audit.md` — an audit sheet for per-stage exit criteria
  and the reasons to disqualify a deal rather than carry it forward
- **Eval suites:** `evals/activation/` · `evals/traversal/` · `evals/output/` ·
  `evals/compression-ablation/`

## Repository layout

```text
skills/sales/   runtime skill (SKILL.md + 15 references + 4 assets + evals)
research/       multi-channel research corpora + build-gate synthesis
docs/           installation, usage, and recipes
```

## Documentation & releases

- [docs/installation.md](docs/installation.md) · [docs/usage.md](docs/usage.md) ·
  [docs/recipes.md](docs/recipes.md)
- [CHANGELOG.md](CHANGELOG.md) — release history (current: v0.1.0)
- [SOURCES.md](SOURCES.md) — source attribution and license posture, including the evidence-grading
  rule this skill follows and the figures it refuses to ship
- [CONTRIBUTING.md](CONTRIBUTING.md) — local validation (`scripts/lint-skill`, `scripts/check-sync`)

## License

MIT — see [LICENSE](LICENSE).
