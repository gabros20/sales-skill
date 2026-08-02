# Self-check — W2 (flagship + CRM/pipeline + calculators)

Files written:
- `skills/sales/references/forecasting-honesty.md` (264 lines; budget 190–230, soft ±15% ceiling
  ~264 — at the ceiling, held there deliberately rather than cutting a citation or a primitive)
- `skills/sales/references/crm-and-pipeline.md` (170 lines; budget 150–190)
- `skills/sales/assets/coverage_calc.py` (~135 lines incl. docstring; budget ~120)
- `skills/sales/assets/forecast_calibration_check.py` (~175 lines incl. docstring; budget ~140,
  the extra length is the two-scale guard and three-tier sample-size logic, both required by the
  inventory row)

## Ruling-by-ruling

- **R1** (permalink or explicit grade). Every figure/quote in both reference files carries either
  a commit-pinned/blob-pinned URL or an explicit grade (VENDOR-SELF-REPORTED for Aviso, where no
  permalink was captured in the corpus — stated as uncited rather than inventing one). No
  reconstructed permalinks used; all pulled verbatim from research/raw/ or the channel reports.
- **R2** (figure-survival). Every number that ships either requires recognise-and-correct (GitLab's
  33% misread as measured accuracy; "3x" folklore vs. the derivation), has arithmetic that IS the
  teaching (coverage = 1/win_rate; the Brier worked examples), or is permalinked on both sides
  (Gong/Aviso claims + their method-absence statement). No orphan figures.
- **R3** (KBCM ships nowhere). Not mentioned anywhere in either file or asset — confirmed by grep
  after writing (`grep -ri kbcm skills/sales/references/forecasting-honesty.md
  skills/sales/references/crm-and-pipeline.md` returns nothing). AE quota attainment is never
  cited, not even hedged.
- **R6** (no truncated quotes). Every quote used (Lawrence et al. 2006, Fildes & Goodwin 2007,
  GitLab handbook passages, Sourcegraph forecasting.md, patio11, KyleAsay_'s full three-criteria
  re-fetch, thaAdamLittle) is the full re-fetched text from the raws, none ending in "…". Where a
  source's own quote does trail off in the raw (thaAdamLittle's "Rough heuristic:" sentence), I
  quoted only the short, non-truncated fragment ("Rough heuristic") rather than the truncated
  sentence around it.
- **R7** (no novelty on assumption-disclosure forecasting). `forecasting-honesty.md` §1 opens with
  the prior-art framing before anything else — alirezarezvani's commercial-forecaster cited as the
  incumbent occupying the posture, novelty explicitly disclaimed, before the pack's own
  contribution (evidence line, null, small-numbers gate, primitives) is introduced.
- **R17** (term discipline). "deal pipeline" is defined in-line on first use in both files
  ("the set of open deals tracked toward close"). CRM structure vs. automation's sync/write-path
  mechanics is stated explicitly as the file boundary in `crm-and-pipeline.md` §1 and in its
  Failure-modes row.
- **R19** (licensing wording). GitLab handbook prose cited as CC BY-SA 4.0 with the
  quote-with-attribution/ShareAlike-on-derivatives distinction noted where I discuss reuse
  (`crm-and-pipeline.md` §2). Sourcegraph cited Apache-2.0 with the archived-2024/2022-content
  staleness caveat traveling with every citation of `forecasting.md`. EspoCRM's documentation repo
  is flagged UNLICENSED, cite-only, do-not-reproduce — not assumed to inherit the AGPLv3 of
  EspoCRM's code repo. Twenty cited as AGPLv3-cored with a per-package MIT caveat rather than a
  blanket license claim. alirezarezvani's commercial-forecaster cited as PRIMARY/MIT per its own
  frontmatter, no adaptation attempted (citation and description only).
- **R20** (win rate denominator; coverage = 1/win_rate, never "3x" as a portable constant). This is
  the central discipline of both the flagship reference and `coverage_calc.py`: the asset's
  `format_result()` raises `ValueError` if no denominator string is supplied, and the reference
  file states the rule explicitly in §4 and again in the Validation section.
- **R21** (GitLab's 33% ships only as a planning-only assumption). Stated verbatim as the rule in
  `forecasting-honesty.md` §4 ("Ship this only as 'a planning-only assumption, explicitly not a
  measurement.' Never write 'GitLab's forecast is 33% accurate,' and never attribute a
  Commit/Best-Case percentage table to GitLab"). No forecast-category percentage table is ever
  attributed to GitLab anywhere in either file — the Commit/Best Case/Call taxonomy is sourced to
  Sourcegraph throughout, kept distinct from GitLab's stage-and-33%-win-rate material.
- **R22** (vendor forecast-accuracy claims need the method-absence statement, always
  VENDOR-SELF-REPORTED). Gong's 95%/"20% more precision" and Aviso's "29 Quarters" both carry the
  method-absence statement inline and are graded VENDOR-SELF-REPORTED in `forecasting-honesty.md`
  §3, with an explicit "never ship a bare vendor accuracy percentage without the method-absence
  statement" rule stated.
- **Not touched / N/A for these two writers**: R4 (57%), R5 (bare 70%), R8/R9 (MEDDPICC/taxonomy),
  R10 (discovery/JPSP), R11 (trademarked-methodology reproduction — Command of the Message not
  cited by name in my files), R12–R14 (AI-outbound/deliverability), R15 (handoff mirror rows —
  W6's file), R16 (ICP inheritance), R18 (dunning), R23 (11x), R24 (anchor-first). None of these
  figures or claims appear in my four files; confirmed by re-reading both reference files in full
  after drafting.

## Self-test output (both required to pass before reporting — confirmed)

```
$ python3 skills/sales/assets/coverage_calc.py --selftest
coverage_calc.py: self-test passed.

$ python3 skills/sales/assets/forecast_calibration_check.py --selftest
forecast_calibration_check.py: self-test passed.
```

Also smoke-tested both CLIs with real arguments (not just --selftest):
`coverage_calc.py --win-rate 0.33 --denominator "..."` → `3.03x`, derivation shown, warning shown.
`forecast_calibration_check.py --predictions 0.7,1 0.3,0 0.9,1` → `n=3`, `verdict: (none)`,
"keep logging" message shown — correctly refuses a verdict at n=3.

## Gaps flagged (not invented)

- No gaps requiring a GAP flag arose — every fact the inventory row asked for (prior-art framing,
  4-leg null, Lawrence/Fildes quotes, tautology, small-numbers gate, 5 primitives; exit-criteria
  gap, CRM structure/automation boundary, hygiene honesty, Twenty/atomic-crm exhibits) was present
  in the research corpus with a citable permalink or explicit grade.
