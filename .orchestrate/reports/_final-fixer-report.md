# Sales pack — final fixer report

Applied against `.orchestrate/reports/_quality-review.md` (Opus quality pass, commit `6b9b919`).
All P0/P1 findings applied; both cheap P2 findings applied; F8 (P3) applied since the fix was
trivial and verifiable on disk.

## Findings

**F1 (P0, auto-block) — `evals/` suite.** Applied exactly per §3 of the review. Built
`evals/README.md` + `evals/activation/cases.json` (27), `evals/traversal/cases.json` (10),
`evals/output/cases.json` (6), `evals/compression-ablation/cases.json` (3) = 46 cases. Schemas
copied verbatim from `success-skill/evals/` (read first, no invented fields). README carries
success's never-ship-quoting caveat verbatim. No deviation.

**F2 (P1) — digit-carrying prohibitions.** Fixed both:
- `outbound-and-prospecting.md` — dropped the "60–70% positive reply rates" parenthetical; kept
  the mechanism ("a vendor case-study reply rate is one customer's best-case story"), line-neutral.
- `agentic.md` — dropped "$5.8B, compounding at over 20% a year"; kept "AI-SDR market-size figures
  are unsourced and never ship," one line shorter.
- Added the review's exact clarifying clause to `SKILL.md`'s invariant: "The one exception is the
  never-ship table below **and the per-file Never-ship sections**." No deviation.

**F3 (P1) — `SOURCES.md` completion.** Added all 7 missing X handles to §5
(@Shpigford, @techsaleshackz, @mistamor, @alexabelonix, @webjuice_ie, @staticmaker1, @iuditg) —
§5 now lists 24 unique handles, verified by script. Added new §4b "Public-web primaries and vendor
pages" covering all 8 sources the review named (Good Judgment Open, Brier score article, Gartner's
buying-journey page, Google's bulk-sender requirements, Gong, Aviso, Clozd, RAIN Group), each with
its grade and citing file. No deviation.

**F4 (P1) — expansion-sale job-coverage gap.** Applied option 1 (recommended): added the 11th Jobs
row to `SKILL.md` ("Close an expansion or upsell deal on an existing account" →
`proposals-pricing-and-negotiation.md`), and added a new §8 "The expansion sale" to that file
(what carries over from the original deal, estimated-until-quoted applied to the expansion amount,
explicit contested-ownership pointer to `handoff.md` — does not adjudicate the seam). Also
qualified the SKILL.md "Not this skill" success row's Ask column so it no longer conflicts with the
new Jobs row: it now reads "renewal **workflow** and **NRR reading**... not closing the expansion
deal itself, which is this pack's own Jobs row above." No deviation.

**F5 (P2) — drifted sibling line-cites.** Re-grepped all three live sibling repos before writing
(not trusted from the review text):
- `success/references/renewals-and-expansion.md` — "the sales clause / marked provisional" spans
  lines 139–140 (confirmed). Fixed in `handoff.md` from `:138-139` → `:139-140`.
- `growth/references/surface-b2b-sales-assisted.md` — the clause is at line 112 alone; line 113 is
  blank (confirmed). Fixed in `handoff.md` from `:112-113` → `:112`.
- `marketing/references/surface-b2b-sales-assisted.md` — the quoted "Three adjacent disciplines…"
  sentence begins mid-line 50 and runs to line 53 (confirmed). This citation is actually in
  `outbound-and-prospecting.md`, not `handoff.md` (the review's file attribution was imprecise;
  the line numbers and fix were correct). Fixed from `:51-53` → `:50-53`.
- Left untouched, verified exact: `success/SKILL.md:95`, `marketing/…/lifecycle-and-email.md:15`,
  `success/…/surface-b2b-high-touch.md:154`, `growth/…/handoff.md:42`, `product/SKILL.md:27`,
  `automation/…/process-capture.md:15`, and marketing's `:58`/`:54-56` in
  `outbound-and-prospecting.md`.

**F6 (P2, budget) — respected as a hard ceiling.** `SKILL.md` grew only by the one Jobs row + the
one invariant clause (218 → 220 lines). `forecasting-honesty.md` (265) and
`icp-and-qualification.md` (207) — untouched, zero growth, confirmed by `wc -l`.
`proposals-pricing-and-negotiation.md` grew by 20 lines (165 → 185) for the new §8 — slightly over
the review's "~15 lines" estimate; trimmed once for concision but the content (three teaching
points: carryover, estimated-until-quoted, contested pointer) didn't compress further without
losing a required point. This file has no hard ceiling under F6 (only SKILL.md/forecasting-honesty/
icp-and-qualification do), so this is a minor deviation from the estimate, not a rule violation.

**F8 (P3) — missing file:line on automation's cite.** Grepped the live `automation-skill` repo:
the fail-closed-for-irreversible-actions gate is `automation/references/approval-and-authority.md:109`
("Fail closed (deny/hold) for irreversible or high-value actions..."). Added that file:line to
`agentic.md`'s cite. No deviation.

**F7 (P3) — noted, no action taken**, per the review's own "leave alone" recommendation (family
convention, not a sales defect).

## Verification

- Both assets `--selftest`: `coverage_calc.py` PASS, `forecast_calibration_check.py` PASS.
- Ruling greps re-run, zero violations: R3 (KBCM — all 4 hits are prohibitions, no digit attached),
  R5 (bare 70% — all hits carry subject inline or are the stated rule itself), R6 (zero
  ellipsis-terminated quotes), R20 (every "3x" sits inside derivation or never-ship framing).
  Additionally grepped for the two removed figures ("5.8B", "60–70%"/"60-70%") in
  `outbound-and-prospecting.md` and `agentic.md` — zero hits, confirming the F2 strip.
- All 4 `cases.json` files parse (`python3 -c "import json; json.load(open(...))"`) — 27 + 10 + 6
  + 3 = 46 cases, confirmed by script. Activation split is 17 positive / 10 negative, confirmed.
- Every `expected_references`/`forbidden_references` path in `traversal/cases.json` resolves to a
  real file under `skills/sales/` — confirmed by script, zero missing.
- `SOURCES.md` §5 now lists 24 unique `@handle`s (was 17), confirmed by script.
- Broken relative-markdown-link scan across `SKILL.md` + all 15 references: zero broken links.

## GREEN
