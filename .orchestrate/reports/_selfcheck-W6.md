# Self-check — Writer W6

Files written:
- `skills/sales/references/handoff.md` (108 lines; budget 100–130)
- `skills/sales/references/surface-smb-transactional.md` (107 lines; budget 100–130)
- `skills/sales/references/surface-enterprise-team.md` (136 lines; budget 110–140)
- `skills/sales/assets/stage_exit_criteria_audit.md` (66 lines; budget ~70)

## Rulings touched and how honored

- **R1 (permalink discipline).** Every external claim carries either a full permalink (GitLab
  pinned-SHA blob URLs for all six GitLab exhibits; frappe/crm, atomic-crm, Odoo pinned-SHA GitHub
  blob URLs; two x.com status URLs for RepVue) or an explicit grade. The one figure without a
  reconstructable permalink — Gartner's buying-group quote — is cited to its live URL with an
  explicit note that the verifying source is a 2020-04-21 Wayback snapshot, and I deliberately did
  **not** fabricate a specific archive.org URL, since none was recorded in the research corpus
  (`research/raw/_raw-c4-calculators-vendor-claims.md:145` only records "retrieved via Wayback
  Machine, 2020-04-21 snapshot," no pinned archive.org link). No permalink in my files was
  reconstructed from memory; all were copied from `_raw-c2`, `_raw-c0` (GitLab), `_raw-c1`
  (frappe/crm, atomic-crm, Odoo), `_raw-c0b`/`channel-c-report.md` (Sourcegraph), and
  `channel-b-report.md` (RepVue).
- **R2 / family "R21" figure-survival.** Buying-group figure ships only with its reconciliation
  clause attached (surface-enterprise-team.md §4) — I do not ship the bare "6–10" headcount.
  RepVue figures ship only with "share of reps at quota" attached (§5). I caught and removed one
  internal-numbering leak of my own: an early draft used "R2's recognise-and-correct test" in
  prose — a build-inventory ruling number with no meaning to a shipped-file reader — and replaced
  it with plain description before finalizing.
- **R3 (KBCM ships nowhere).** Stated explicitly and by name in surface-enterprise-team.md §5: "No
  quota-attainment figure attributed to KBCM/KeyBanc ships anywhere in this pack." No KBCM figure
  appears in any of my four files.
- **R5 (bare "70%" needs a subject).** Flagged explicitly at the close of surface-enterprise-team
  §5 ("Any bare '70%' attached to quota in this corpus has at least three distinct subjects...").
  I do not ship a bare 70% anywhere myself.
- **R6 (no quote ending "…").** Checked every quoted string in all four files against its source
  raw. Found and fixed one mid-quote ellipsis in handoff.md (automation's process-capture.md:15
  citation) — restructured into two separately-quoted clauses rather than eliding across them, so
  no quote in the shipped files uses "…" anywhere, start, middle, or end.
- **R8 / R9 (MEDDPICC ruling; frameworks-vs-methods taxonomy).** I do not restate the legal ruling
  or the taxonomy myself — surface-enterprise-team.md §2 explicitly defers both to
  [icp-and-qualification](../skills/sales/references/icp-and-qualification.md) ("this file cites
  GitLab's operational instance of the framework, not the ruling") to avoid a second, possibly
  drifting copy of a ruling another writer owns.
- **R11 (trademarked methodologies: cite, never reproduce).** surface-enterprise-team.md §2
  explicitly instructs "not safe to reproduce: the qualifying-question banks GitLab publishes
  under each letter... paraphrase or omit," matching `_raw-c2`'s own ruling on the same material,
  and I did not reproduce GitLab's question banks anywhere.
- **R15 (seam invariants — mine above all).** The three mirror rows in handoff.md follow E's §C
  spec exactly: marketing FIRM with no hedge anywhere near it; growth's row keeps "regardless of
  which funnel stage an experiment touches" unconditional while the row itself is tagged
  provisional (the two-different-hedges distinction from E §C.2 is stated explicitly, not just
  implied); success's row carries both positions (sales closes the expansion sale AND Murphy's
  complexity-gated CS-native position) and states sales does not adjudicate. Product/automation
  silence is noted once, in prose, framed as deliberate sequencing, not oversight — no "rows this
  file originates" device used (per C.0's explicit ruling that sales doesn't need it, unlike
  success). GitLab's retain-and-expand exhibit carries the "run parallel" sentence every time it is
  cited (handoff.md and surface-enterprise-team.md both), including in the Failure modes list as a
  standing warning against dropping it.
- **R16 (ICP inherited from marketing).** Stated in handoff.md's marketing row and repeated in
  surface-smb-transactional.md §3 ("Route a lead through the inherited ICP fit signal") — never
  defined from scratch in any of my files.
- **R17 (term discipline).** "Discovery call" not used bare anywhere (I don't use the bare term at
  all in my four files). "Deal pipeline"/"sales pipeline" avoided in favor of more specific terms
  (stage, pipeline total, deal) where possible; where "pipeline" appears it's in an unambiguous
  sales context. CRM structure vs. automation's sync mechanics: not directly restated in my files
  (that boundary line belongs to crm-and-pipeline.md), but I never use "CRM" to mean a sync/write
  mechanism — only the open-source tools' stage/field structure, consistent with the split.
  "Expansion" used only in the sales-closes-the-expansion-sale sense inherited from success's
  cession, never conflated with product's or growth's senses. "Sales-qualified lead" not used
  (out of scope for my three files). "Qualification" used only internally, never as user-facing
  journey vocabulary.
- **R18 (dunning/billing routing).** handoff.md has a dedicated section: routes to `product` "per
  success's and marketing's documented position, not as sales's own finding," explicitly stating
  product's own pack contains zero occurrences of either word and that sales must never claim
  product says so itself.
- **R19 (licensing wording).** GitLab always cited as "CC BY-SA 4.0" (never "MIT," which is the
  separate site-code license). Sourcegraph always cited as "Apache-2.0" with the archived-2024
  caveat attached at every citation, including a rewritten caveat sentence in
  surface-enterprise-team.md that no longer asserts an unverified "own README" claim (the raw
  distinguishes a page-level warning from a root-README warning; I softened to "its own content
  carries Sourcegraph's own warning... may be out of date" to stay inside what `_raw-c0b` actually
  supports). frappe/crm cited AGPLv3, atomic-crm cited MIT, Odoo cited LGPLv3 — all matching the
  licensing ledger in `_raw-c1-open-crms.md` exactly (Odoo is LGPLv3, not AGPL — a distinction the
  ledger flags as commonly missed). No incumbent content is adapted into a reusable artifact in my
  files — the audit sheet's own template is my own writing, not a close derivative of GitLab's
  stage table, so no ShareAlike obligation attaches to it.
- **R20 (win rate needs its denominator; coverage = 1/win-rate; never ship "3x" as constant).**
  surface-smb-transactional.md §4 explicitly declines to let deal volume substitute for
  calibration and defers to forecasting-honesty.md and coverage_calc.py rather than restating or
  shipping any coverage constant myself. No win-rate percentage ships anywhere in my four files.
- **R21 (GitLab's 33% win rate).** Not cited anywhere in my files — I deliberately avoided pulling
  this figure in, since it is not load-bearing for handoff/surface content and carries its own
  narrow citation rule owned by the forecasting-honesty flagship.

## Gaps flagged, not invented

- Gartner's buying-group quote has no pinned Wayback URL recorded anywhere in the research corpus
  I was given — only "2020-04-21 snapshot, fetched 2026-08-03" in `_raw-c4`. I cited the live URL
  plus the verification method rather than construct an archive.org link myself. If a specific
  Wayback permalink exists, the integrator/spec-review pass should backfill it; I did not fabricate
  one per R1's explicit ban on reconstructed permalinks.
- I did not independently re-verify any of the fixed line-cites from `_raw-e2-seam-audit.md` by
  re-running `grep -n` against the live sibling repos myself (marketing/growth/success/product/
  automation) — I used E's already-corrected, drift-checked numbers as given (e.g. success
  renewals-and-expansion.md `:117-124`/`:154`, not the stale "around line 50"). E's own coverage
  statement flags these as as-read on 2026-08-03 and subject to further drift; worth a final
  re-grep at integration time since sibling packs are live repos.
