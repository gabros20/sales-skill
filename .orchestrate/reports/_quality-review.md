# Sales pack — Opus quality review (24-dimension family rubric)

Reviewer: opus quality pass · 2026-08-03 · commit `6b9b919` (post-spec-fixes)
Scope: `skills/sales/` in full (SKILL.md + 15 references + 4 assets), `SOURCES.md`,
`.orchestrate/inventory.md`, `research/synthesis.md`, `research/channel-e-report.md`.
Calibration: shipped sibling `/Users/tamas/Documents/Personal/Projects/success-skill/skills/success/`
(SKILL.md, `handoff.md`, `health-and-risk-signals.md`, `renewals-and-expansion.md`, `evals/`).

**Score: 20.5 / 24. Verdict: NOT-SHIP — eval-dimension auto-block (`evals/` is empty).**
Everything else is release-grade. With the eval suite built and the three P1 fixes applied, this
ships. On content quality alone (dims 1–23) it scores 20.5/23, ahead of where success sat pre-fix.

---

## 1. Scorecard

| # | Dimension | Score | One-line justification |
|---|---|---|---|
| 1 | Router clarity (10 jobs, <30s) | **1** | Ten one-intent rows; the Contribution column names the *distinctive* content, not the topic, so a cold reader picks by what they'll get, not by keyword collision. |
| 2 | Description honesty + routing | **1** | 596/600 chars; all twelve promised jobs present; six boundary arrows; `(→ success, contested)` carries the contested mark *into the description* — no sibling does this. |
| 3 | Job coverage vs canonical 14 | **0.5** | All 14 Includes are covered, plus cold outbound and AI-outbound policy. **But "expansion-sale close" — named in the charter axis, the mission paragraph, and the description — has no teaching file.** `handoff.md` says sales closes it; nothing says how. "Commercial collateral" (E's flagged "case study inside a deal", new writing) is also absent. |
| 4 | Surface coverage + default correctness | **1** | Three base surfaces + additive agentic. Default (founder-led solo) declared in four places and backed by a do-not-stall instruction. `surface-founder-led-solo.md`'s job-by-job reshape table is the best surface artifact in the pack. |
| 5 | Flagship distinctiveness | **1** | `forecasting-honesty.md` is unambiguously the best file: prior-art disclaimer first (R7), two peer-reviewed papers read from PDFs, a four-leg null plus a fifth practitioner check, the coverage tautology with visible arithmetic, the small-numbers gate, five primitives that run at n=1. The §1 self-limitation ("real gaps, but narrow; don't oversell them") is the move that makes it credible. |
| 6 | Second flagship (win/loss) | **1** | The observer-test inference — *a second buyer interview is not corroboration, because both draw on the same pool of plausible theories* — is the sharpest single argument in the pack, and it is derived, not quoted. Clozd scoped to one page, one vendor, checked once, with the broader claim explicitly refused. |
| 7 | Evidence discipline (grades, permalinks, subjects) | **0.5** | Near-flawless: grades inline everywhere, subjects attached (stockings `n=52, four identical pairs`; RepVue "share of reps at quota"; CEB's three lost qualifiers). **Two violations of the pack's own "a disclaimed figure is still a figure" invariant** — see §2, F2. |
| 8 | Never-ship table quality | **1** | 17 rows across a real three-way class taxonomy, with a "Ship instead" column on every row. The lead sentence ("the split is itself the finding — read the class before correcting") makes it a teaching device rather than a blocklist. Best never-ship table in the family. |
| 9 | Named concepts, no numbered invariants | **1** | The Existence Gate, the coverage tautology, the small-numbers gate, predict-then-score, the evasion-category rule, estimated-until-quoted, the observer test, the exit-criteria gap. Grep for `R<n>` / "invariant N" in the pack: zero hits. |
| 10 | Seam fidelity (3 mirror rows + boundaries) | **1** | Exact four-column format; hedge written twice per hedged row; marketing unhedged; growth's "regardless of which funnel stage an experiment touches" preserved unconditional inside a provisional row; success carries both positions and declines to adjudicate. Verified against all three siblings on disk. |
| 11 | Crosslink coherence | **0.5** | All 15 refs reachable from the router; **0 broken markdown links** (checked programmatically). Skip-when blocks route bidirectionally and name the reason, not just the file. Docked for three drifted sibling line-cites — see §2, F4. |
| 12 | Asset quality + self-testing | **1** | Both `.py` pass `--selftest` (and self-test at import); the refusal behavior is real, not decorative (`format_result` raises on a blank denominator). Both `.md` assets carry worked examples with honest grades — `loss_prediction_log.md`'s "Unverifiable" and "Not scoreable" rows teach the discipline better than the prose does. |
| 13 | Register consistency (family voice) | **1** | Read-when / Skip-when / Inputs / Produces / Contents / Validation / Failure-modes in all 15 refs. The mixed crosslink style (7 files markdown-link, 8 files backtick) **matches the shipped success pack exactly** — family convention, not a sales defect. |
| 14 | Read-when / Skip-when sharpness | **1** | Consistently strong. `win-loss-learning.md`'s skip-when explaining that the predict-then-score *mechanism* is shared with the flagship, and which file applies it to what, is the model the rest of the family should copy. |
| 15 | Validation sections actionable | **1** | Present in all 15, written as checkable assertions rather than aspirations. `crm-and-pipeline.md`'s three items are thin for a 172-line file but each is genuinely checkable. |
| 16 | Failure-modes sections concrete | **1** | Every file; every entry names either an applied section or a destination file. `handoff.md`'s six are effectively the seam's regression tests. |
| 17 | Honesty about thin evidence | **1** | `demo-and-narrative.md` §1 and `objections-and-enablement.md` §2 both state the null and explain why the absence *is* the position. "Unverified, not debunked" on Cohan's *Great Demo!* is exactly the right grade and the right register. |
| 18 | Solo-reader serviceability | **1** | Every job has a solo path: negative exit criteria instead of MEDDPICC, a spreadsheet with exit criteria instead of a CRM, predict-then-score with zero tooling, the friction gate as a price lever. The default reader can act on all 15 files. |
| 19 | Enterprise surface correctness | **1** | GitLab's ten stages with the two-page provenance split stated; MEDDPPICC's nine letters confirmed against section headers; Sourcegraph with a *double* caveat (archived-2024 **and** its own README's incorrect-content warning); buying-group figure only with its deconfliction clause; RepVue always with subject. |
| 20 | Agentic overlay quality | **1** | Additive-only and says so three ways; disclosure escalated from instruction to a required logged field; volume ceiling and kill switch placed *outside* the agent's reasoning loop; the evasion rule written against the capability so it binds tools that don't exist yet; mechanics ceded to `ai` cleanly. |
| 21 | No scope creep | **1** | Pricing design → product; deliverability cited, never restated; sync → automation; agent mechanics/evals → ai; ICP inherited, never redefined; legal review declared out of family entirely. `outbound-and-prospecting.md`'s "`ai` owns how to generate 25 variants; this pack owns whether you should" is the cleanest seam sentence in the pack. |
| 22 | Licensing / attribution compliance | **0.5** | Repos, licences, and trademarks are thorough (per-directory checks, ShareAlike consequences, PostHog's `/contents/`-scoped wording, five-copyright-holder note). **But SOURCES.md is incomplete against pack citations** — 7 X handles and 8 non-repo sources cited in refs appear nowhere in it. See §2, F3. |
| 23 | Length / budget discipline | **0.5** | Within budget, but three files sit *at or one line past* their soft ceiling: SKILL.md 218 (ceiling 218), `forecasting-honesty.md` 265 (ceiling 264), `icp-and-qualification.md` 207 (ceiling 207). No headroom anywhere for a fix that adds lines. |
| 24 | Eval-readiness | **0** | **AUTO-BLOCK.** `evals/` exists and is empty. Behavior is highly specifiable — full spec in §3. |

**Total: 20.5 / 24.**

---

## 2. Findings, prioritized

### P0 — blocking

**F1. `evals/` is empty.** Build the four-directory suite specified in §3 (46 cases). Mirror
`success-skill/evals/` exactly: four subdirectories each containing `cases.json`, plus a top-level
`README.md` stating the counts and the never-ship-quoting caveat.

### P1 — fix before ship

**F2. Two violations of the pack's own "a disclaimed figure is still a figure" invariant.**
SKILL.md states: *"In working prose, never name a never-ship number in order to forbid it — state
the mechanism and point at the primary source instead. The one exception is the never-ship table
below."* Two files name the digits anyway, in working prose:

- `outbound-and-prospecting.md:101` — *"Never cite a vendor case-study reply rate (e.g. one
  vendor's "60–70% positive reply rates") as a market benchmark."*
- `agentic.md:54-55` — *"AI-SDR market-size figures ("$5.8B, compounding at over 20% a year") are
  unsourced and never ship."* (This figure is *already* carried for recognition in the SKILL.md
  never-ship table, so the prose repetition is pure re-shipping.)

This is the family's own recorded lesson from the operate build — *naming a number to forbid it
still ships it*. Fix: drop the digits and state the mechanism (`"a vendor case-study reply rate is
one customer's best-case story"` / `"AI-SDR market-size figures are unsourced and never ship"`).
Both edits are line-neutral or shorter, which matters given F5.

Adjacent, **not** a defect: `proposals-pricing-and-negotiation.md:135` (`$9.99 beats $10`) and
`objections-and-enablement.md` §6 sit inside file-level `## Never-ship` sections, which serve the
same recognition job as the SKILL.md table. Recommend the fixer add one clause to the SKILL.md
invariant making that explicit — *"the never-ship table below and the per-file Never-ship
sections"* — so the rule is unambiguous rather than fixed case-by-case.

**F3. `SOURCES.md` is incomplete against what the pack cites.** Missing entirely:

- **X handles cited in refs but absent from §5:** `@Shpigford` (the gate eroding from below),
  `@techsaleshackz` (the framework-discard exhibit), `@mistamor` (the hygiene-as-noise coaching
  exhibit), `@alexabelonix` (the 4/50 founder micro-loop), `@webjuice_ie` and `@staticmaker1` (two
  of the three evasion exhibits and the funded-industry figure), `@iuditg` (the truncated Solution
  Selling specimen). Seven of twenty-four handles.
- **Non-repo sources cited PRIMARY or VENDOR-SELF-REPORTED in refs but absent from §§2/4/5:**
  Good Judgment Open (`gjopen.com/faq`, PRIMARY, `forecasting-honesty.md` §5), the Brier score
  reference article (PRIMARY, same section), Gartner's B2B buying-journey page (the buying-group
  figure, Wayback-verified, `surface-enterprise-team.md` §4), Google's bulk-sender requirements
  (`support.google.com/a/answer/81126`, the 0.30/0.10/5,000 numbers), Gong (`gong.io/forecast/`),
  Aviso, Clozd, RAIN Group.

The family rule is list-every-licensed-and-cited source, not every *repo*. Add a short §4b for
public-web primaries and vendor pages, and complete §5.

**F4. Job-coverage gap: the expansion-sale close is promised and not taught.** The description, the
mission paragraph, the charter axis, and success's own contested seam all state that sales closes
the expansion sale. `forecasting-honesty.md:13` routes "the expansion-sale motion" to
`handoff.md` — but `handoff.md` is a seam map that establishes *who owns it*, not *how to run it*,
and the SKILL.md "Not this skill" table pushes anything containing the word "expansion" toward
`success`. A reader asking "help me close the upsell on this existing account" has no landing spot
and is actively mis-routed.

Two acceptable fixes; recommend the first:
1. Add an 11th Jobs row — *"Close an expansion or upsell deal on an existing account"* →
   `proposals-pricing-and-negotiation.md` — and add a short section to that file (the expansion
   sale as a live-deal negotiation with an incumbent relationship: what carries over from the
   original deal, the estimated-until-quoted split on an expansion amount, and the explicit
   contested-ownership pointer to `handoff.md`). Costs ~15 lines in a file with headroom (165 of
   a 140–180 budget).
2. Strike "expansion-sale close" from the description and mission. **Not recommended** — the
   charter names it, and success's shipped seam depends on sales having it.

### P2 — fix if cheap

**F5. Three sibling line-cites have drifted by one.** Quotes are correct; numbers are not (the
family's own standing warning). Re-grep and correct in `handoff.md`:
- `success/references/renewals-and-expansion.md:138-139` → the "sales clause marked provisional"
  invariant is at **`:139-140`**.
- `marketing/references/surface-b2b-sales-assisted.md:51-53` → the quoted sentence begins at
  **`:50`** ("Three adjacent disciplines…"); `:58` and `:54-56` are exact.
- `growth/references/surface-b2b-sales-assisted.md:112-113` → the clause sits at **`:112`** alone;
  `:113` is blank.

Verified exact and needing no change: `success/SKILL.md:95`, `marketing/…/lifecycle-and-email.md:15`,
`success/…/surface-b2b-high-touch.md:154`, `growth/…/handoff.md:42`, `product/SKILL.md:27`,
`automation/…/process-capture.md:15`.

**F6. Budget headroom is zero.** SKILL.md (218), `forecasting-honesty.md` (265) and
`icp-and-qualification.md` (207) are all at or one line past their soft ceiling. F2's edits are
subtractive, which helps; F4's addition should land in `proposals-pricing-and-negotiation.md`
(which has room), not in SKILL.md beyond the one router row.

### P3 — noted, no action required

**F7.** `assets/…` is referenced from `references/*.md` without the `../` prefix in six places
(`win-loss-learning.md` and the two `.md` assets use `../assets/` correctly). The shipped success
pack does exactly the same thing, so this is a family convention (paths read as pack-root-relative),
not a sales defect. Leave alone unless the family standardizes.

**F8.** `agentic.md` cites "automation's own irreversible-action approval gate" without a
file:line, unlike every other cross-pack cite in the pack. Cosmetic.

### Verified clean (no action)

- **R3 (KBCM)** — 4 hits, all prohibitions, no number attached anywhere. Clean.
- **R5 (bare 70%)** — 6 hits; each carries its subject inline or sits inside quoted primary text
  whose subject is stated in adjacent prose. Clean.
- **R6 (truncated quotes)** — zero quotes end in an ellipsis; all 8 ellipses are mid-quote
  elisions. Clean.
- **R20 (win rate / coverage)** — `coverage = 1/win-rate` taught with visible arithmetic; every
  "3x" sits inside derivation or never-ship framing; the denominator rule is enforced in code.
  Clean.
- **Both assets** `--selftest` **PASS.**
- **Description** 596 chars, ≤600.
- **All 15 references reachable from the router; 0 broken relative links.**

---

## 3. Eval suite specification (the final fixer builds this)

Mirror `success-skill/evals/` exactly: `evals/README.md` + four subdirectories each holding a
single `cases.json`. **Schemas, verbatim from the sibling — do not invent fields:**

- `activation/cases.json` — `{"id", "prompt", "should_trigger"}`
- `traversal/cases.json` — `{"id", "prompt", "expected_references"[], "forbidden_references"[]}`
- `output/cases.json` — `{"id", "prompt", "assertions"[]}`
- `compression-ablation/cases.json` — `{"id", "prompt", "variants"[], "preserve"[]}`

Routing is asserted in `traversal`, not in `activation` (success's convention). The intended route
for each activation positive is given below so the fixer can pair them; it does **not** go in the
JSON.

**Suite size: 27 activation + 10 traversal + 6 output + 3 compression-ablation = 46 cases.**

### 3.1 `activation/` — 27 cases (17 positive, 10 negative)

**Positives (`should_trigger: true`) — one per job ref, one per surface, plus two indirect:**

| id | prompt | intended route |
|---|---|---|
| `gate-existence` | "We're two people, $40/mo per customer, and someone told us to hire an SDR. Do we even need a sales motion?" | `when-sales-applies` |
| `account-selection` | "Which of these 200 accounts should I actually spend time on — and should I be running MEDDIC on them?" | `icp-and-qualification` |
| `cold-outbound` | "Write a cold outbound sequence for CTOs at Series-B fintechs, and tell me what spam rate I have to stay under." | `outbound-and-prospecting` |
| `discovery-call` | "Structure my first call with a new prospect. Does SPIN actually work?" | `discovery-calls` |
| `demo-build` | "Build the demo flow for a prospect who told us they care about audit logs and SSO." | `demo-and-narrative` |
| `battlecard` | "Build a battlecard against our main competitor and an objection library from what we keep hearing." | `objections-and-enablement` |
| `proposal-anchor` | "Draft the proposal, and tell me whether to name our price first." | `proposals-pricing-and-negotiation` |
| `crm-stages` | "Design our deal pipeline stages and the exit criteria for each one." | `crm-and-pipeline` |
| `forecast-build` | "Build me a Q3 bookings forecast from our open pipeline." | `forecasting-honesty` |
| `winloss-program` | "Set up a win/loss interview program — what do we ask buyers after we lose?" | `win-loss-learning` |
| `handoff-seam` | "We just closed a deal. What exactly do we hand to customer success, and what stays ours?" | `handoff` |
| `surface-solo` | "I'm a solo founder selling my own product. What parts of the sales apparatus should I skip?" | `surface-founder-led-solo` |
| `surface-smb` | "Four reps, $8k deals, three-week cycles. How much process should we carry?" | `surface-smb-transactional` |
| `surface-enterprise` | "Six-month cycle, eight stakeholders, procurement involved. What qualification structure applies?" | `surface-enterprise-team` |
| `agentic-unattended` | "Our AI SDR sends first-touch emails with nobody reading them first. What has to be true?" | `agentic` (+ base surface) |
| `indirect-coverage` | "My board wants 3x pipeline coverage. Where does that number even come from?" | `forecasting-honesty` |
| `indirect-stalled` | "Deals keep sitting in 'Evaluating' for months and I can't tell which are real." | `crm-and-pipeline` |

**Negatives (`should_trigger: false`) — the seven wrong-pick traps from `channel-e-report.md` §D and
`synthesis.md` §6, plus two adversarial sibling-vocabulary traps and one out-of-family:**

| id | prompt | belongs to |
|---|---|---|
| `neg-design-onboarding` | "Design the in-product onboarding wizard — empty states, progressive disclosure, the aha-moment copy." | `design` |
| `neg-growth-experiment` | "Design an A/B test on the demo-request landing page to see if a shorter form lifts conversion." | `growth` |
| `neg-success-renewal` | "Build the renewal workflow our CSM runs 90 days before contract end." | `success` |
| `neg-product-dunning` | "Build the dunning sequence for failed payments, and restructure our pricing tiers." | `product` |
| `neg-marketing-lifecycle` | "Write the six-email lifecycle nurture for trial signups who haven't activated." | `marketing` |
| `neg-automation-crmsync` | "Sync our CRM deal records into Postgres and keep them consistent both ways." | `automation` |
| `neg-ai-evals` | "Set up evals for our sales-assistant agent — retrieval quality and hallucination rate." | `ai` |
| `neg-adversarial-discovery` | "Run product discovery with our users — interviews, opportunity trees, JTBD." | `product` (bare "discovery" trap, E §D) |
| `neg-adversarial-pipeline` | "Our CI pipeline is failing at the deploy stage." | out of family ("pipeline", 340 sibling hits) |
| `neg-outoffamily-legal` | "Review the MSA redlines their counsel sent back and tell me which clauses are enforceable." | out of family — counsel (`proposals…` §6) |

### 3.2 `traversal/` — 10 cases

| id | prompt | expected_references | forbidden_references |
|---|---|---|---|
| `gate-first` | "Build me a CRM and an outbound sequence." | `references/when-sales-applies.md` | `references/surface-enterprise-team.md`, `references/crm-and-pipeline.md` |
| `flagship-forecast-solo` | "Build a forecast from my six open deals." | `references/forecasting-honesty.md`, `references/surface-founder-led-solo.md`, `assets/coverage_calc.py`, `assets/forecast_calibration_check.py` | `references/surface-enterprise-team.md`, `references/win-loss-learning.md` |
| `second-flagship-winloss` | "We lost three deals to price this quarter. Set up win/loss learning." | `references/win-loss-learning.md`, `assets/loss_prediction_log.md` | `references/demo-and-narrative.md`, `references/outbound-and-prospecting.md` |
| `default-surface-unnamed` | "Should we use MEDDIC?" *(no business model named — must assume the default and say so)* | `references/icp-and-qualification.md`, `references/surface-founder-led-solo.md` | `references/surface-enterprise-team.md` |
| `enterprise-qualification` | "Eight stakeholders, $200k ACV. What qualification structure applies?" | `references/icp-and-qualification.md`, `references/surface-enterprise-team.md` | `references/surface-founder-led-solo.md` |
| `agentic-stacks-on-base` | "Our AI SDR runs unattended outbound. It's just me running the company." | `references/agentic.md`, `references/outbound-and-prospecting.md`, `references/surface-founder-led-solo.md` | — *(asserts the overlay does not replace a base surface)* |
| `agentic-not-loaded` | "Cold email campaign, AI-drafted, but I read and send every one myself." | `references/outbound-and-prospecting.md` | `references/agentic.md` *(human-in-loop → base policy only)* |
| `seam-contested` | "Who closes the upsell on an existing account — us or CS?" | `references/handoff.md` | — |
| `stage-audit` | "Audit our pipeline stages." | `references/crm-and-pipeline.md`, `assets/stage_exit_criteria_audit.md` | `references/forecasting-honesty.md` |
| `demo-after-discovery` | "Build the demo for next week's call with the prospect we spoke to Tuesday." | `references/demo-and-narrative.md`, `references/discovery-calls.md` | `references/proposals-pricing-and-negotiation.md` |

Verify every expected/forbidden path exists on disk before committing (success's stated rule).

### 3.3 `output/` — 6 cases

1. **`contract-forecast`** — *"Build me a forecast for next quarter. I have nine open deals."*
   - output carries an explicit assumption block naming every rate and window used
   - refuses to emit "3x" (or any fixed multiple) as a portable constant
   - any coverage figure is derived from the reader's own win rate **and** its stated denominator,
     or the output refuses and says why
   - the small-numbers gate is applied to n=9 explicitly — no calibration verdict is drawn
   - `coverage_calc.py` and/or `forecast_calibration_check.py` is run or named
   - the output states what the forecast **cannot** support
2. **`contract-qualification-taxonomy`** — *"Write me a deal-health checklist."*
   - MEDDIC / MEDDPICC / BANT are named as **frameworks**; SPIN / Challenger / Sandler as
     **methods**; the two categories are never conflated
   - no consensus is claimed in either direction on any of them
   - no qualifying-question bank is reproduced from GitLab or any incumbent
   - if MEDDPICC's legal status appears, all three corrections travel: "generic **for business
     education services and content**", summary judgment granted **in part** with the case live,
     and McMahon's testimony **excluded**
3. **`contract-winrate-denominator`** — *"Our win rate is 21%. Is that good?"*
   - the output refuses to evaluate the figure until the denominator is stated
   - no benchmark win rate is supplied from any source
   - the denominator rule is stated in substance ("21% and 47% can both be correct on the same
     business, on different denominators")
4. **`contract-handoff-contested`** — *"Write the sales→success handoff for our expansion motion."*
   - the `success` row carries **both** positions and states sales does not adjudicate
   - the `marketing` row carries **no** hedge
   - growth's "regardless of which funnel stage an experiment touches" stays unconditional
   - if GitLab's stage-3/4 or retain-and-expand exhibit is cited, the "run parallel" sentence
     travels with it
5. **`contract-ai-outbound`** — *"We're launching an AI SDR next month."*
   - disclosure at first contact, with both statutory anchors (EU AI Act Art. 50(1)+(5); CA SB 1001)
   - the "10 million monthly visitors" exemption is **corrected**, never repeated as an exemption
   - the evasion rule is stated against the **category**, not one tool or prompt
   - any vendor figure ships VENDOR-SELF-REPORTED, and any contested pair ships both halves
6. **`never-ship-strings`** — forbidden-string sweep over any produced artifact: "92% ... give up",
   "80% need 5 follow-ups", "21x more likely", "$5.8B", "85% fail within 6 months", "17% higher
   sales volume", "20–30% higher win rates", "3x" as a standalone coverage rule, "8 touches" as a
   law, any KBCM/KeyBanc quota figure, a bare "70%" with no subject, "GitLab's forecast is 33%
   accurate". *Carry success's caveat verbatim in `README.md`: this cases file is not agent-loaded,
   so quoting the banned figures inside it is not a shipping violation.*

### 3.4 `compression-ablation/` — 3 cases

Each with `"variants": ["no-skill", "current", "compressed-candidate"]` and
`"preserve": ["task success", "safety", "required-reference recall", "artifact completeness",
"human comprehension"]`. Chosen to exercise rules at the **start**, **middle**, and **end** of
SKILL.md's loaded set:

1. **`ablate-existence-gate`** *(start — "Route before acting" step 1)* — *"Set up our outbound
   machine: sequences, a CRM, the works. We charge $29/mo."* Does the gate still run before the
   apparatus when the router is compressed?
2. **`ablate-figure-grade`** *(middle — Universal invariants)* — *"A vendor says their AI SDR books
   3x more meetings and they're a $5.8B market. Put it in the board deck."* Do inline grading, the
   contested-pair rule, and the never-ship refusal survive?
3. **`ablate-contested-seam`** *(end — "Not this skill" + never-ship table)* — *"Write the renewal
   and expansion ownership doc for our account team."* Does the contested mark survive compression,
   or does the pack quietly resolve the seam in its own favour — the one failure that breaks a
   shipped sibling's checked invariant?

---

## 4. Ship recommendation

Build the 46-case suite (§3) and apply F2, F3, F4; F5 and F6 if cheap. Nothing in this pack needs
rewriting — the content is release-grade and, on the flagship and the seam work, ahead of the
shipped siblings. Re-run both `--selftest`s and the four ruling greps after the fixes, then this is
a GREEN final pass away from release.
