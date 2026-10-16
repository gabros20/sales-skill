# Changelog

All notable changes to **sales** are documented here.

The release procedure synchronizes `.codex-plugin/plugin.json`, this changelog, git tag
`v<version>`, and the matching GitHub Release. Runtime `SKILL.md` contains no version metadata.

## [Unreleased]

### Added
- Practitioner outbound craft folded into the existing references, every quote re-fetched at its
  permalink and graded inline: the first touch in `outbound-and-prospecting` (an ask smaller than a
  meeting, one checkable observation, the source named, a written stop condition), check-the-
  chain-against-its-own-headline in the funnel math (one cited chain fails its headline), a deliverability → list → offer → copy diagnostic
  order, a fourth evasion exhibit (a reply-keyword opt-out sold as a way to trick the spam filter),
  and two bounds on what the disclosure rule is not.
- `icp-and-qualification`: timing signals (stated need, incumbent dissatisfaction, spend in motion)
  for ordering accounts that already fit, four scoring checks (decay is not demand, check firing
  rate, hand-set weights are assumptions, segment comparisons hit the small-numbers gate), and the
  partner-footprint rule.
- `demo-and-narrative` §6: demo-before-the-discovery-call, consistent with demo-as-answer only where
  the need is observable from outside; attach-versus-offer taught as contested.
- `agentic`: concealment gates ("absence of AI markers," "like a human wrote it") named as the
  inverse of the structural disclosure field; escalation tripwires; model-scored qualification
  (cutoffs as assumptions, the denominator-shrinking conversion claim).
- `discovery-calls` §4 third mechanic (ask for an instance); `crm-and-pipeline` §4 mechanical flags
  with the past-close-date flag routed to predict-then-score; `proposals` §4 contingent budget
  phases; `surface-founder-led-solo` append-only ledger and referral sequencing.
- Evals: 2 output cases (first touch, agentic concealment) and 2 traversal cases (demo-first
  outreach, timing signals).

## [0.1.0] — 2026-08-03

### Added
- Initial release: faceted-router `sales` skill — 11 primary jobs × 3 surfaces
  (agentic as additive overlay) + handoff, 15 references, 4 assets.
- Flagship reference: forecasting-honesty (the forecast-accuracy null checked across four
  independent sources plus a practitioner check; the coverage tautology, 1 ÷ win-rate, taught
  with visible arithmetic instead of shipped as a fixed multiple; the small-numbers gate; the
  predict-then-score loop as the constructive primitive).
- Second flagship-grade reference: win-loss-learning (the observer-test argument — a second
  opinion on a lost deal is not independent evidence, because both draw on the same pool of
  plausible stories).
- The Existence Gate (`when-sales-applies`): four incompatible practitioner answers for whether
  an assisted sales motion is worth running at all, taught as a live disagreement rather than a
  single resolved rule.
- Expansion-sale close taught as its own job inside
  `proposals-pricing-and-negotiation.md`, with the contested boundary against `success`'s
  renewal position carried forward rather than resolved silently.
- Runnable, self-testing assets: `coverage_calc.py`, `forecast_calibration_check.py`,
  `loss_prediction_log.md`, `stage_exit_criteria_audit.md`.
- Never-ship strip against the sales-folklore corpus (the "57% of the buying decision" genre,
  "92% give up after 4 follow-ups," the 21x speed-to-lead figure, unsourced AI-SDR market sizes,
  fixed stage-probability defaults), split three ways by how each figure actually fails, enforced
  by `scripts/lint-skill`.
- Behavioral eval suite: 46 cases across activation, traversal, output, and
  compression-ablation.
- Research corpora + synthesis in `research/` (5 channels, date-stamped 2026-08-03).

[0.1.0]: https://github.com/gabros20/sales-skill/releases/tag/v0.1.0
