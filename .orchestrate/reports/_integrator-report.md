# Integrator report — sales pack

Opus integrator pass over the six-writer BASE (commit 9a93f92). 34 fixes. Both assets pass
`--selftest` after every edit. All 52 pack permalinks verify against `research/`; zero crosslinks
broken; zero R-number leaks; zero ellipsis-terminated quotes.

## Fixes, one line each

### Class A — ruling violations

| # | File | Defect | Ruling |
|---|---|---|---|
| 1 | `references/discovery-calls.md:22` | `(R16)` — build-inventory ruling number shipped to a reader | register / no numbered invariants |
| 2 | `references/demo-and-narrative.md:98` | `(R11's standing rule)` leaked | register |
| 3 | `references/demo-and-narrative.md:104` | `(R10)` leaked | register |
| 4 | `references/demo-and-narrative.md:119` | `(R10)` leaked | register |
| 5 | `references/demo-and-narrative.md:138` | `(R10 governs both)` leaked | register |
| 6 | `references/objections-and-enablement.md:55` | `(R11)` leaked | register |
| 7 | `references/objections-and-enablement.md:116` | `(R6)` leaked | register |
| 8 | `references/objections-and-enablement.md:121` | `(R11)` leaked | register |
| 9 | `references/objections-and-enablement.md:130` | `(R11)` leaked | register |
| 10 | `SKILL.md` never-ship table | `R3:` leaked into the shipped table's "why" cell | register |
| 11 | `references/surface-enterprise-team.md:60` | MEDDPICC qualifier truncated to "business-education services" — **"and content" dropped** | R8 |
| 12 | `SKILL.md` jobs row | MEDDPICC qualifier compressed to "services/content"; restored to the ruling's exact wording | R8 |
| 13 | `references/forecasting-honesty.md:45` | alirezarezvani blob URL was **composed** from a verified repo + verified SHA + verified path, but that assembled URL exists nowhere in the corpus | R1 (reconstructed permalink = fabricated) |
| 14 | `references/crm-and-pipeline.md:150` | krayin `Lead.php` blob URL likewise composed | R1 |
| 15 | `references/outbound-and-prospecting.md` §Deliverability | Section said "cite the anchor and moves on" but **cited no anchor** — now cites marketing's `lifecycle-and-email.md` §1 and `assets/email-compliance-checklist.md` | R13 |

### Class B — citations that don't resolve or don't carry what's promised

| # | File | Defect |
|---|---|---|
| 16 | `references/handoff.md` dunning | `success/SKILL.md:99` → line 99 is about data/PII. Correct line is **`:95`** (verified) |
| 17 | `references/handoff.md` dunning | `marketing/references/lifecycle-and-email.md:17` → line 17 is analytics instrumentation. Correct line is **`:15`** (verified) |
| 18 | `references/handoff.md` success row | "a checked invariant at `renewals-and-expansion.md:154`" — **wrong file.** Line 154 there is about customer stories. The invariant text lives at `renewals-and-expansion.md:138-139` and `surface-b2b-high-touch.md:154`. Channel E made this error (§C.2) and W6 copied it as given |
| 19 | `references/handoff.md` marketing row | `surface-b2b-sales-assisted.md:58` cited for "deliverability and consent doctrine" — line 58 says nothing about deliverability. Split: `:58` now cited for what it actually says, deliverability re-pointed at marketing's real doctrine files |
| 20 | `references/icp-and-qualification.md:18` | Crosslink `../../../../marketing-skill/skills/marketing/references/…` — a **machine-local path escaping the pack**. Resolves only on this disk; no shipped sibling does this. Converted to the family's `pack/references/file.md` convention |
| 21 | `references/surface-founder-led-solo.md:110` | "see win-loss-learning's denominator rule" — that file explicitly **disclaims** the denominator and routes it away. Re-pointed at `forecasting-honesty.md` §4 / `coverage_calc.py` |
| 22 | `references/objections-and-enablement.md:34` | "repeated **verbatim** at `handoff.md:42` and `SKILL.md:107`" — neither is verbatim; both restate. Softened to "drawn again in" |
| 23 | `references/outbound-and-prospecting.md:45` | Same claim, same fix |
| 24 | `references/objections-and-enablement.md:31` | Marketing cession quote carried a self-manufactured `...` elision; the elided clause restored so the quote is exact |
| 25 | `references/crm-and-pipeline.md` Contents | Listed "5. Disqualification as a stage"; the header reads "as a first-class pipeline state" |
| 26 | `assets/stage_exit_criteria_audit.md` | Estimated-vs-quoted row named the split but not the event that resolves it; now points at `proposals-pricing-and-negotiation.md` §4, and that file points back (judgment call b) |

### Class C — structure and register

| # | File | Fix |
|---|---|---|
| 27 | `references/handoff.md` | Added missing `## Validation` (+ Contents entry) |
| 28 | `references/agentic.md` | Added missing `## Validation` (+ Contents entry) |
| 29 | `references/surface-founder-led-solo.md` | Added missing `## Validation` |
| 30 | `references/surface-smb-transactional.md` | Added missing `## Validation` (+ Contents entry) |
| 31 | `references/surface-enterprise-team.md` | Added missing `## Validation` (+ Contents entry) |
| 32 | `references/surface-enterprise-team.md` ×3 | Mid-paragraph line-break artifacts from editing, rewrapped |
| 33 | `references/forecasting-honesty.md` §3 leg 2 | Sourcegraph's Commit/Call taxonomy was stated twice, with the same permalink, in §3 and §6. §3 now points forward (judgment call c) |
| 34 | `SKILL.md` | Description rewritten (below); `design` row folded into `product` (judgment call a); never-ship table rebuilt (below); route-step-4 and Mission/Core-workflow duplication trimmed to hold the line budget |

### Content gap closed

**R4's entire subject was absent from the shipped pack.** Grep for `57%`, `9 in 10`, `Shipley`,
`CEB`, `Always Be Closing`, `21x`, `BANT…IBM` returned nothing but an unrelated RepVue 57%. R4 is a
dedicated ruling with a dedicated primary and no writer covered it. Added
`when-sales-applies.md` § "The decision-already-made genre": the CEB/Google 2012 primary quoted
from the corpus PDF with its permalink, the three mutations that change what it means
(progress ≠ completion; "supplier sales rep" is the actual cutoff; 70% is a supplier-level maximum,
not a buyer figure), the Gartner misattribution and the 17% time-allocation confusion, and the
instruction to teach the genre's *shape* rather than debunk three strips — plus matching Validation
and Failure-mode rows. Filed here because the genre's rhetorical job is "the buying conversation
starts later than you think," which is the existence gate's own territory and sits directly beside
the erosion-from-below section.

## Description — collision-check verdict: PASS after two fixes

Final (597 chars, ≤600). Every §2b item present and checked one by one: sales-motion existence ·
ICP account selection + qualification · cold outbound/prospecting · AI-outbound policy · discovery
calls · demos · objections + battlecards (sales enablement) · proposals · pricing presentation +
negotiation · CRM structure + deal pipeline · forecasting honesty · win/loss · expansion-sale close.
All six required arrows present and correct.

Two collisions found against the ten shipped siblings' descriptions:

1. **Bare "discovery."** The old Use-for clause read "Use for discovery, pipeline forecasts,
   win/loss audits." `product`'s shipped description claims "product discovery" and "Use for
   opportunity discovery." This is the exact term E §D flags as colliding hard, and it was a
   straight R17 violation sitting in the highest-traffic string in the pack. Now "discovery calls".
2. **"expansion" un-disambiguated.** Sales claimed "expansion close" while `success`'s shipped
   description claims "renewals/expansion (NRR)" — and sales's arrow said only
   "renewals (→ success, contested)", so the cession did not reach the colliding term. Now
   "renewals + expansion metrics (→ success, contested)". This is the success build's own lesson
   applied: a cession must reach the description.

Also added: "proposals" and "battlecards" (both required by §2b, both missing); "deal pipeline"
rather than bare "pipeline" (R17, and "pipeline" has 340 hits across seven packs per E §D).

Not added, deliberately: **"revenue operations."** Marketing cedes it unhedged alongside the other
two, and it is named in SKILL.md's "Not this skill" row, but §2b does not list it and the 600-char
budget is fully consumed. Flagged for spec review as a judgment call, not an oversight.

## Never-ship table — consolidated

Rebuilt in `SKILL.md` from A §5 (18-row table + the three-member genre finding) + B §5/§G + C §4 +
D's 20-item list + E §F, filtered through R2. Eight rows became eighteen, grouped by a **Class**
column that keeps the three-way taxonomy visible: *survives at origin* · *pure folklore* ·
*vendor-research genre*, plus a fourth working group for *subject/denominator failures* and one for
the single never-ship claim whose danger is **inverted** (a reader concluding the California
bot-disclosure law exempts them).

Dedupes made: the A/C forecaster exhibit is **one row** (unsourced stage defaults + the 30-cell
conversion table that gets executed as code — same defect, one aggravator). "3-to-1/5-to-1" folded
into the "3x coverage" row. "9 in 10" and Shipley's "70–80%" folded into the 57%-genre row rather
than shipped as separate strips, per A's genre recommendation adopted in synthesis §3.

R2 exclusions, stated so the reasoning is auditable: E §F's remaining webdesign figures (200%
social-proof lift, three-tiers-1.4×, 75%-judge-credibility, Attention-Ratio 31%, CTA 10–90%) are
**not** shipped. They fail clause (a) for this reader — they are pricing-page and landing-page
figures from a retiring skill, they sit on the far side of the boundary this pack just drew to
`product`, and a sales reader will not meet them in sales material. Ditto A's Tier-2 "collect, do
not lead with" list, which is explicitly sub-threshold, and whose NRR row collides with the open
success↔growth family ruling and should not be pre-empted here.

Subjects are attached on every row that carries a number.

## Handoff rows vs E §C — verified, one drift

Checked verbatim against `channel-e-report.md` §§C.1–C.2.

- **marketing — FIRM.** No hedge word anywhere in the row. Hands back "pipeline and close-rate
  signal that feeds positioning and message iteration" (E: match marketing's own term — matched).
  Consumes qualified demand + the assets. Column 4 is an explicit negative. **PASS.**
- **growth — PROVISIONAL, hedge shape preserved.** Parenthetical in column 1 *and* restated in prose
  opening column 4 (E's two-places rule). "Regardless of which funnel stage an experiment touches"
  is unconditional and bolded inside the provisional row. The two-distinct-hedges distinction is
  stated explicitly in Failure modes. `:110-112` cited and verified. **PASS.**
- **success — CONTESTED, not flattened.** Both positions carried, "not Account Management
  carryover" intact, sales explicitly does not adjudicate. **One drift, fixed** — the checked-
  invariant cite (fix 18). E itself pointed at the wrong file; W6 flagged in its self-check that it
  used E's numbers without re-grepping, which is exactly how this reached the pack. **PASS after
  fix.**

The "run parallel" sentence travels with every GitLab retain-and-expand citation, in `handoff.md`
and `surface-enterprise-team.md`, including as a standing Failure-mode warning. Product/automation
prose-only silence is noted once, framed as deliberate. No "rows this file originates" device, per
C.0.

## Judgment calls

**(a) W1's 7th boundary row for `design` — FOLDED into the `product` row.** W1 asked whether to keep
it. It had to go, and not on style grounds: it was **factually wrong and self-contradicting**. The
same SKILL.md table already assigned "pricing-*page* psychology" to `product` one row above, so the
table routed one topic to two packs. E §E.2 is explicit that "product owns pricing-tier design and
page psychology"; the pack's own `proposals-pricing-and-negotiation.md` §1 says the retiring
webdesign content "is already homed in product's `business-model.md`"; and `design`'s shipped
description does not claim pricing psychology at all. A reader following the design arrow would have
landed in a pack that does not carry the content. The product row now states the split in one
sentence ("Product designs and models the price, including how a visitor reads tiers on a page;
sales presents and negotiates a number inside a live deal") and the description arrow was updated to
match. Boundary arrow count is back to the six §2b requires.

**(b) `stage_exit_criteria_audit.md` crosslinks vs W5's expectations — one real gap, fixed.** W5's
`proposals-pricing-and-negotiation.md` §4 owns "the proposal is the event that converts an estimate
into a quote," and W6's audit sheet has a row auditing exactly the estimated-vs-quoted split — but
neither referenced the other. The audit row now points at proposals §4, and proposals §4 names the
audit sheet. The rest of the sheet's crosslinks (`crm-and-pipeline`, `forecasting-honesty`,
`surface-smb-transactional`) all resolve and all carry what they promise. W5's flagged assignment
discrepancy is resolved in W5's favour for the record: the inventory table assigns the sheet to W6,
W6 wrote it, and W5 was correct not to overwrite finished work.

**(c) Flagship at 264 vs 230 soft ceiling — trimmed 2 lines, no evidence cut.** 264 was inside the
±15% ceiling (264.5), so this was optional. One genuine intra-file redundancy existed: Sourcegraph's
Commit/Best Case/Call taxonomy was written out twice, with the same permalink, in §3 leg 2 and again
in §6. §3 now states the finding that matters there — the most complete published method in this
research carries no accuracy figure — and points forward to §6 for the quoted taxonomy. Every
citation, primitive, and number survives. Now 264 lines again after fix 13 added the licensing
caveat the corpus requires; net structural redundancy removed, net evidence added.

## Remaining risks for spec review

1. **`SOURCES.md` does not exist.** `SKILL.md`'s Resources section promises "Attribution, licences,
   and what this pack claims for itself — `SOURCES.md` at the repository root." Both shipped
   siblings have one (success at repo root, marketing at pack root). It is a release-phase artifact
   and building it needs the full licensing ledger, so I did not fabricate one — but the pointer is
   currently a broken promise in a shipped file. Same for `evals/`, which is empty and promised in
   the same paragraph; that one is scheduled.
2. **Sibling line-cites are live-repo dependent.** Nine `pack/file.md:NN` cites now resolve, all
   re-grepped this pass. Three had already drifted since Channel E wrote its table three days ago.
   Expect more drift; the Validation section I added to `handoff.md` now makes the re-grep a stated
   obligation, but it does not stop the rot.
3. **The two composed permalinks (fixes 13/14) were the only R1 exposure I found, and both were
   invisible to a URL-shaped check** — every component was genuinely verified, only the assembly was
   not. Spec review should assume this failure mode exists elsewhere in a form I did not catch and
   re-verify blob URLs component-wise, not string-wise.
4. **`icp-and-qualification.md` at 206 lines** (budget 140–180, ceiling 207). Trimmed twice to get
   under. It is the densest file in the pack and carries the MEDDPICC ruling in full; if spec review
   needs to add anything there, something else has to come out.
5. **Mid-quote elisions remain in five quotes** (`icp-and-qualification.md:84`,
   `forecasting-honesty.md` ×3, `crm-and-pipeline.md:99`, `win-loss-learning.md` ×2). None
   *terminates* in "…", which is R6's stated target, and W4/W5/W6 each checked theirs against source.
   I did not re-cut them: several are the source's own bullet separators and re-cutting risks
   changing meaning. Worth a source-by-source check against the raws in the spec pass.
6. **"Revenue operations" is ceded to sales but does not appear in the description** — see above.
7. **NRR remains an open family collision** (success↔growth, per synthesis §9). Sales's description
   now says "renewals + expansion metrics (→ success, contested)", which routes rather than
   adjudicates. Correct for now; the family ruling still has to land.
