# Live eval — `sales` @ 612719a (post-GREEN)

Simulated cold agent with all 14 packs installed. Method as briefed: activation scored from the 14
frontmatter **descriptions only** (no sales references loaded); traversal scored with sales's router
added; output scored after reading the relevant references and producing the artifact; ablation
scored by checking whether the named rule's text is physically present in `SKILL.md`.

**Result: 46/46 (+3 adversarial: 2 clean, 1 known seam). No blocker. No description fix required
before ship.**

| Suite | Score |
|---|---|
| activation | 27/27 |
| traversal | 10/10 |
| output | 6/6 cases (33/33 individual assertions) |
| compression-ablation | 3/3 |
| adversarial (mine) | 2 clean, 1 documented-seam mis-route (accepted, see below) |

---

## 1. Activation — 27/27

Scored by picking one pack from the 14 descriptions, then comparing to `should_trigger`.

| # | id | my cold pick | expected | verdict |
|---|---|---|---|---|
| 1 | gate-existence | sales | true | PASS |
| 2 | account-selection | sales | true | PASS |
| 3 | cold-outbound | sales | true | PASS |
| 4 | discovery-call | sales | true | PASS |
| 5 | demo-build | sales | true | PASS |
| 6 | battlecard | sales | true | PASS |
| 7 | proposal-anchor | sales | true | PASS |
| 8 | crm-stages | sales | true | PASS |
| 9 | forecast-build | sales | true | PASS |
| 10 | winloss-program | sales | true | PASS |
| 11 | handoff-seam | sales | true | PASS (lowest confidence — see note A) |
| 12 | surface-solo | sales | true | PASS |
| 13 | surface-smb | sales | true | PASS |
| 14 | surface-enterprise | sales | true | PASS |
| 15 | agentic-unattended | sales | true | PASS (contested with `automation` — note B) |
| 16 | indirect-coverage | sales | true | PASS |
| 17 | indirect-stalled | sales | true | PASS |
| 18 | neg-design-onboarding | design | false | PASS |
| 19 | neg-growth-experiment | growth | false | PASS |
| 20 | neg-success-renewal | success | false | PASS |
| 21 | neg-product-dunning | product | false | PASS |
| 22 | neg-marketing-lifecycle | marketing (growth defensible) | false | PASS |
| 23 | neg-automation-crmsync | automation (data defensible) | false | PASS |
| 24 | neg-ai-evals | ai | false | PASS |
| 25 | neg-adversarial-discovery | product | false | PASS |
| 26 | neg-adversarial-pipeline | operate | false | PASS |
| 27 | neg-outoffamily-legal | none / out of family | false | PASS (note C) |

**What carried the positives.** Sales's description names the load-bearing nouns verbatim —
"cold outbound/prospecting", "objections + battlecards", "proposals + pricing presentation +
negotiation", "CRM structure + deal pipeline", "win/loss audits", "AI-outbound policy". In every
contested case the verbatim name beat the sibling's generic category (battlecard beat marketing's
"competitive positioning"; discovery **call** beat product's "opportunity discovery"). The six-arrow
`Not` tail did the negative work on its own: cases 19–24 are each disclaimed by name in the
description, so no sibling reference was needed to reject them.

**Note A — `handoff-seam` (case 11).** Neither sales's nor success's description names the
post-close handoff artifact, which is a genuinely shared object. I picked sales because the asker is
the seller ("what stays *ours*") and success's description scopes to "keep customers **after** they
buy," i.e. post-handoff activity. A cold model that anchors on the words "hand to customer success"
could pick success. Not a fix now — the failure is graceful (success would route the boundary
question back), and the description has no spare characters. If it ever regresses, the minimal fix
is adding "post-close handoff" to sales's `Use for` list.

**Note B — `agentic-unattended` (case 15).** Genuine three-way pull: sales ("AI-outbound policy"),
`ai` ("agents, guardrails"), `automation` ("human-in-the-loop processes … behind which approval").
Sales wins because the artifact requested is a *policy* for *outbound*, and sales's description names
that compound verbatim while disclaiming "agent mechanics (→ ai)". Correct as shipped.

**Note C — `neg-outoffamily-legal` (case 27).** The pack has no explicit legal/contract-review
disclaimer anywhere (not in the description, not in the `Not this skill` table). The case as written
is safe because "which clauses are enforceable" is a legal-judgment ask, not a commercial one. But
note the near neighbour: "negotiate these MSA redlines" *should* trigger sales
(`proposals-pricing-and-negotiation`), and nothing in the pack tells a reader where legal advice
stops. Optional, non-blocking: one `Not this skill` row sending statutory/enforceability questions
out of the family. I would not spend the SKILL.md budget on it.

---

## 2. Traversal — 10/10

Scored with sales's router loaded. "Extra" = read but neither expected nor forbidden (not a fail).

| # | id | my read set | verdict |
|---|---|---|---|
| 1 | gate-first | `when-sales-applies` (+ `surface-founder-led-solo`, extra) | PASS |
| 2 | flagship-forecast-solo | `forecasting-honesty`, `surface-founder-led-solo`, both forecast assets | PASS |
| 3 | second-flagship-winloss | `win-loss-learning`, `loss_prediction_log.md` | PASS |
| 4 | default-surface-unnamed | `icp-and-qualification`, `surface-founder-led-solo` | PASS |
| 5 | enterprise-qualification | `icp-and-qualification`, `surface-enterprise-team` | PASS |
| 6 | agentic-stacks-on-base | `agentic`, `outbound-and-prospecting`, `surface-founder-led-solo` | PASS |
| 7 | agentic-not-loaded | `outbound-and-prospecting` only | PASS |
| 8 | seam-contested | `handoff` (+ `proposals-pricing-and-negotiation`, extra) | PASS |
| 9 | stage-audit | `crm-and-pipeline`, `stage_exit_criteria_audit.md` | PASS |
| 10 | demo-after-discovery | `demo-and-narrative`, `discovery-calls` | PASS |

All 15 references and 4 assets verified present on disk; every expected path resolves.

**The three cases that could plausibly have failed, and why they didn't:**

- **Case 1 (gate-first)** depends entirely on the word "first" in router step 1, against a prompt
  that names a CRM and a sequence outright. It holds because step 1 doesn't just say "first" — it
  enumerates the exact three triggers ("before building outbound infrastructure, a CRM, or a
  forecast"), and the same rule is restated as invariant #1 and Core-workflow step 1. Three
  independent statements of one rule is what makes it survive an impatient reader.
- **Case 10 (demo-after-discovery)** required reading *two* job references, against router step 2's
  "Identify the one primary job … Read one of each." The router alone would under-read. It passes
  because `demo-and-narrative.md` names `discovery-calls.md` five separate times in-file (lines 12,
  101, 105, 138–139), so step 6 ("read every selected reference completely") delivers the second
  file. Recovery is via in-file crosslink, not the router — worth knowing if the demo file is ever
  trimmed.
- **Case 9 (stage-audit)** needed `assets/stage_exit_criteria_audit.md`, and
  **`crm-and-pipeline.md` never mentions that asset — zero occurrences.** It passes only because
  `SKILL.md`'s Resources paragraph describes it in words that match the prompt almost exactly ("an
  audit sheet for per-stage exit criteria"). This is the one asymmetry in the pack:
  `forecasting-honesty.md` names both its assets (3×), `win-loss-learning.md` names its log (3×),
  `crm-and-pipeline.md` names none. **Minimal fix (MINOR, optional):** one sentence in
  `crm-and-pipeline.md`'s Produces line pointing at `../assets/stage_exit_criteria_audit.md`. Not a
  ship blocker — SKILL.md is always loaded, so the asset is never unreachable.

---

## 3. Output — 6/6 cases, 33/33 assertions

I produced a condensed artifact for each prompt from the loaded references, then checked it against
every assertion, then swept all six artifacts for the forbidden strings.

| # | id | assertions | verdict |
|---|---|---|---|
| 1 | contract-forecast | 6/6 | PASS |
| 2 | contract-qualification-taxonomy | 4/4 | PASS (near-miss, see below) |
| 3 | contract-winrate-denominator | 3/3 | PASS |
| 4 | contract-handoff-contested | 4/4 | PASS |
| 5 | contract-ai-outbound | 4/4 | PASS |
| 6 | never-ship-strings | 12/12 | PASS |

**Case 1 (forecast, n=9).** Artifact carried: an assumption block with win rate, denominator, data
window, weighting choice (none applied) and quoted-vs-estimated basis all named; a refusal to
compute coverage until the reader supplies their own win rate and denominator, with
`coverage_calc.py` named; the small-numbers gate applied to n=9 by name, no calibration verdict, with
`forecast_calibration_check.py`'s tiering cited; the floor/ceiling/judgment shape as the reportable
alternative; and an explicit "cannot support" (no backtest possible, and forecast accuracy is
published by nobody). No fixed coverage multiple appears anywhere in the artifact.

**Case 2 (deal-health checklist) — the near-miss worth recording.** My first draft produced a
seven-item checklist whose items were, in substance, MEDDPICC's published letters with no
attribution — *precisely* the act `icp-and-qualification.md` condemns in `github/awesome-copilot`.
The eval's four assertions would not have caught it: they forbid reproducing a **qualifying-question
bank**, not reproducing the **letter expansion**. What caught it was `SKILL.md`'s own invariant
("Trademarked methodologies are named, cited, and taught by their evidence — never reproduced"), so
a compliant agent is protected. **This is an eval-coverage gap, not a pack defect** — the pack's rule
is stronger than the test of it. Optional hardening: add a fifth assertion to this case — "no
framework's letter expansion is reproduced as the artifact's own structure without attribution."

**Case 4 (contested handoff).** All four hedge-discipline assertions held: the success row shipped
both positions plus the non-adjudication sentence; the marketing row shipped with no hedge word at
all; growth's "regardless of which funnel stage an experiment touches" stayed unconditional inside a
row already marked provisional; and the GitLab stage-3/4 exhibit travelled with its "the roles …
run parallel" sentence. This is the hardest case in the suite to pass by accident.

**Case 5 (AI SDR).** Both statutory anchors shipped with the right structure — Art. 50(1)'s
information duty plus Art. 50(5)'s "at the latest at the time of the first interaction" timing, and
SB 1001 as a safe-harbour statute. The visitor-count threshold appeared only as a **correction**
(it gates § 17942(c)'s service-provider carve-out, not the § 17941(a) prohibition), never as an
exemption. Evasion stated against the category. The contested vendor pair shipped both halves with
both source types.

**Case 6 (never-ship sweep).** Correct behaviour is refusal-with-substitute, and that is what the
artifact did: no headline statistic supplied, the three failure classes explained, the reader
redirected to their own numbers with denominators, and one primary citation offered with its actual
subject rather than its folklore paraphrase. Swept all six artifacts: none of the eleven forbidden
strings appears. README caveat confirmed present verbatim.

---

## 4. Compression-ablation — 3/3

Question answered per case: is the named rule physically present in `SKILL.md`'s own text, such that
it survives with zero references loaded?

| # | id | rule under test | in SKILL.md? | verdict |
|---|---|---|---|---|
| 1 | ablate-existence-gate | gate fires before building the apparatus | Yes ×3 — router step 1, invariant 1, workflow step 1 | SURVIVES |
| 2 | ablate-figure-grade | vendor claim stays vendor-claim; market-size figure never ships | Yes — invariant 5 + two never-ship rows | SURVIVES |
| 3 | ablate-contested-seam | success seam ships contested, both positions, sales does not adjudicate | Yes — `Not this skill` success row, verbatim | SURVIVES |

Honest statement of what degrades. In case 1, the *trigger* survives and the Jobs row still names
all four incompatible gates, but the gate **content** (which one binds at a given price point) lives
only in `when-sales-applies.md` — correct, since SKILL.md names the file. In case 3, the contested
label and both positions survive intact, but the GitLab "run parallel" exhibit and the "explicitly
not Account Management carryover" phrasing live only in `handoff.md`; a SKILL.md-only artifact would
be thin but not wrong. Both are acceptable degradation with no correctness error — which is the bar.
Case 2's relative-lift claim ("3× more meetings") is caught by the Gong-Labs never-ship row, which
names exactly that genre (relative lift over an unstated base rate), not just the coverage sense.

**One documentation finding (MINOR, optional).** `evals/README.md`'s caveat about quoting banned
figures is scoped to "the `never-ship-strings` output case's assertions." But two other eval files
also quote never-ship figures in their **prompts** — the AI-SDR market-size figure in
`compression-ablation/cases.json`, and the coverage multiple in `activation/cases.json`. Neither is
a shipping violation by the same reasoning (not agent-loaded, and the prompt is the user's voice —
quoting the folklore is the entire test). But the caveat as written doesn't cover them, which
invites exactly the "a disclaimed figure is still a figure" objection at review time. **Minimal fix:**
broaden the caveat's scope from that one case to the `evals/` directory. One line.

---

## 5. Adversarial cases (mine) — 3

Designed to sit on the three sharpest boundaries named in the brief.

**ADV-1 — marketing/sales, outbound-adjacent content.**
*"Write the sequence of emails we send to everyone who downloaded our whitepaper last month, and the
follow-up cadence when they don't reply."*
→ Routes to **marketing**, correctly. The discriminator is coldness, and both descriptions state it:
sales claims "cold outbound/prospecting"; whitepaper downloaders are marketing-captured demand, so
marketing's "marketing email and lifecycle campaigns" holds, and its `SKILL.md:107` cession is
explicitly of *cold* outbound only. The sequence-and-cadence vocabulary is the trap and it does not
bite. **Matches the documented seam.**

**ADV-2 — success/sales, expansion.**
*"Our biggest customer wants to add 40 more seats. Who runs that conversation and what do we send
them?"*
→ Routes to **sales**, correctly, and this is the family's sharpest live collision. Both
descriptions claim expansion: sales says "expansion-sale close", success says "renewals/expansion
(NRR)". The tiebreaker exists and it is in success's own description — its `Not` tail ends
"the sale (→ sales)". A live deal with a proposal attached is the sale. Sales then routes the
*ownership* question to `handoff.md` rather than adjudicating. **Matches the documented seam; the
descriptions resolve it without either body file.**

**ADV-3 — growth/sales, funnel-stage work. The one that mis-routes.**
*"Our demo-to-proposal conversion dropped from 40% to 22% this quarter. Figure out why and fix it."*
→ From descriptions alone I route this to **growth**, and I believe most cold models would. Growth's
description names "funnel diagnosis" and "diagnose a funnel drop" verbatim; sales's description names
neither "conversion" nor "diagnosis", and its `Not` tail cedes "funnel experiments (→ growth)" —
which reads as covering this. The family's actual intended split lives one layer down, in sales's
`Not this skill` growth row: growth hedges *where* the funnel/deal line sits, never *whether* deal
mechanics are sales's. Diagnosing why demos stop converting is deal mechanics (qualification drift,
demo answering the wrong discovery, pricing presented too early); designing a controlled test of a
fix is growth's.

**Assessment: accepted seam, not a ship blocker, and I recommend no description change.** Three
reasons. The failure is graceful — growth genuinely owns funnel diagnosis, and its own pack routes
deal mechanics back. The prompt is ambiguous on its face ("figure out why" is diagnosis; "and fix
it" is a change), so both packs have a real claim. And the obvious fix — adding "deal-stage
conversion diagnosis" to sales's description — would collide head-on with growth's shipped "diagnose
a funnel drop" and manufacture the inverse false positive, trading a graceful mis-route for a
contested one. This belongs on the family memory as a known seam, alongside the NRR-vs-growth
collision already logged from the success build.

---

## Verdict

**Ship.** 46/46 with no correctness failure in any suite, and the two hardest behavioural
properties — the existence gate firing ahead of an explicit build request, and the contested success
seam surviving as contested — both hold. Three optional, non-blocking items, none touching the
description: point `crm-and-pipeline.md` at its own asset; broaden the `evals/README.md` never-ship
caveat from one case to the directory; add a letter-expansion assertion to the qualification-taxonomy
output case. The one real seam risk (ADV-3, deal-stage conversion diagnosis vs growth's funnel
diagnosis) is better recorded than fixed.
