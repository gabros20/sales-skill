# W5 self-check — demo, objections/enablement, proposals/pricing/negotiation

## Files written
- `skills/sales/references/demo-and-narrative.md` (138 lines, budget 110–140)
- `skills/sales/references/objections-and-enablement.md` (141 lines, budget 110–140, +1 line over
  soft ceiling — within ±15%)
- `skills/sales/references/proposals-pricing-and-negotiation.md` (157 lines, budget 140–180)

## Assignment discrepancy flagged, not acted on
The team-lead's brief to me assigned `assets/stage_exit_criteria_audit.md` as a fourth deliverable,
but `.orchestrate/inventory.md` §2 binding table explicitly assigns that file to **W6**, and the
file already existed on disk, fully written, well-cited (GitLab exit criteria, KyleAsay negative
criteria, Odoo's empty-requirements-field exhibit, atomic-crm's `Delayed` stage, GitLab's
segment-tiered aging automation), and consistent with the rest of the corpus. I did not touch or
duplicate it — the inventory table governs over a message-level assignment, and overwriting
finished, correct work would have been a regression. Flagging for the integrator in case the
brief's assignment needs correcting for the record.

## Ruling-by-ruling
- **R1 (permalink or grade).** Every factual/figure claim carries either an x.com permalink, a
  GitHub blob permalink (GitLab handbook at pinned SHA `46180fa3686c8baa55f91bf32c6e1d676eefd475`;
  vladar107/awesome-sales-engineer at pinned SHA `fdb7823eae1084f60e10bd8d83795677e29afec1`), a
  repo-root URL for a named-but-not-blob-cited incumbent (coreyhaines31/marketingskills), an
  academic citation (Schweinsberg et al. 2023 *PNAS*, Maaravi & Levy 2017 *JDM* — cited
  author/year/journal only, no DOI was given in channel-d for these two and none was fabricated),
  or an explicit grade (FOLKLORE, PRIMARY). No permalink was reconstructed; every URL was grep-
  verified present in `research/raw/` or a channel report before use.
- **R2/figure-survival.** No demo-specific benchmark figure ships anywhere in `demo-and-narrative.md`
  — none was found in the corpus, and the file says so explicitly in §1 rather than filling the gap
  with an adjacent number. No figure in any of the three files ships without meeting (a) recognise-
  and-correct, (b) arithmetic-is-the-teaching, or (c) both-sides-permalinked.
- **R6 (no truncated quotes).** Caught and fixed two near-misses during self-review: (1) an early
  draft of the FidelCacheFlow citation strung together fragments as one quoted sentence when the
  source tweet itself is truncated with "…" — rewritten to quote only the individual complete
  fragments the raw itself safely quotes ("7 years", "2x President's Club", etc.), never the
  assembled truncated sentence. (2) an early draft of the iuditg "proven to increase conversion by
  48…" never-ship item reproduced the literal truncated string inside quote marks while warning
  against quoting it — rewritten to describe the claim without reproducing the truncated fragment.
  Grepped both final files for "…" afterward; the only remaining instance is prose *about* the
  ellipsis rule itself, not a shipped truncated quote.
- **R9/taxonomy.** `objections-and-enablement.md` §5 states plainly that objection handling is not
  a qualification framework and that MEDDIC/MEDDPICC/BANT vs. SPIN/Challenger/Sandler taxonomy and
  the split-opinion finding live in `icp-and-qualification.md` — not restated in full here, per the
  family's crosslink-don't-duplicate convention.
- **R10.** `demo-and-narrative.md` §5 explicitly states the JPSP question-asking papers (liking,
  non-sales dyads) may not be borrowed by a demo methodology any more than by a branded discovery-
  call methodology, and repeats this in Never-ship (§6) and Failure modes.
- **R11 (cite-never-reproduce).** Both `demo-and-narrative.md` and `objections-and-enablement.md`
  name coreyhaines31/marketingskills' `demo-scripts.md` and `objection-library.md` (MIT-licensed,
  84,811 installs) and cite their *structure* (talk-track field shape; "demo scripts by call type")
  without reproducing any script or talk-track content, explicitly invoking the awesome-copilot
  MEDDICC reproduction as the cautionary exhibit each time.
- **R17 (term discipline).** Fixed on self-review: several early-draft instances of bare
  "discovery" in `demo-and-narrative.md` (referring to the sales meeting) were rewritten to
  "discovery call" / "discovery-call methodology" throughout — grepped clean afterward. "Sales
  pipeline" is qualified at first use in `proposals-pricing-and-negotiation.md`'s Purpose line
  (fixed one instance where an unqualified "pipeline health" preceded the qualified use — reordered
  the wording so the qualified form comes first). "CRM" is used consistent with the automation-
  owns-sync/sales-owns-structure split (no sync-mechanics claims made). No use of "expansion,"
  "SQL," or bare "qualification" as user-facing vocabulary in any of the three files.
- **R21 clause (b), arithmetic-is-the-teaching.** BrianLaManna's best-and-final/drop-dead-number
  exhibit and the GitLab estimated-Net-ARR mechanism are both shipped as structural/precision-limit
  teachings, not as portable benchmark numbers — no percentage is extracted from either as a
  standalone figure.
- **R24 (anchor-first CONTESTED).** `proposals-pricing-and-negotiation.md` §2 carries both
  permalinked sides (Schweinsberg et al. 2023 PNAS nonlinear-impasse-risk finding; Maaravi & Levy
  2017 information-asymmetry finding) with their boundary conditions stated explicitly, and Never-
  ship (§7) separately bans shipping anchor-first as a rule in either direction.

## Cross-links verified against sibling filenames in the inventory
All crosslinks point to files actually named in `.orchestrate/inventory.md` §2:
`discovery-calls.md`, `icp-and-qualification.md`, `crm-and-pipeline.md`, `forecasting-honesty.md`,
`win-loss-learning.md`, `outbound-and-prospecting.md`, plus the two forward-references between my
own three files. No crosslink invents a filename not in the inventory.

## Boundary/seam citations
- Marketing's cession (`surface-b2b-sales-assisted.md:51–53`, `handoff.md:42`, `SKILL.md:107`) is
  quoted verbatim in `objections-and-enablement.md` §1, matching the line numbers channel-E's audit
  verified as exact (not the two files where E found drift — success and growth — which I did not
  cite).
- The pricing-presentation/pricing-design seam in `proposals-pricing-and-negotiation.md` §1 cites
  channel-E's exact boundary framing ("self-serve pricing-*page* content — a visitor reading tiers
  on a website, not a rep presenting a quote in a live deal") and correctly identifies the retiring
  `webdesign` skill's `persuasion-and-conversion.md:106–124` as the source E deliberately did not
  lift, now homed in product's `business-model.md`.
- §6 states legal/contract review is out-of-family without inventing a cession from any named
  sibling — phrased as "no sibling pack claims it," which is what the research supports (no channel
  report attributes legal-review ownership to any pack).

## GAPs flagged (needed-but-missing facts, not invented)
- No DOI was located in the research corpus for Schweinsberg et al. (2023) or Maaravi & Levy
  (2017) — cited by author/year/journal only, consistent with how this family cites other academic
  papers without a located DOI (e.g. success's Ascarza/de Haan citations). If a DOI surfaces later
  it should be added, not fabricated now.
- No demo-specific conversion/win-rate figure exists anywhere in the corpus — stated as an honest
  absence in `demo-and-narrative.md` §1/§6, not treated as a research gap needing a follow-up
  search (five channels already covered this territory; a sixth pass is unlikely to find what four
  independent surfaces didn't).
- `Great Demo!` (Peter Cohan) is cited only as a bibliography entry, never independently evaluated
  for its own evidence base — flagged in §1 as unverified, not debunked, and not cited for any
  claim beyond its own existence as a reference point.

## Status
All three reference files written to budget, self-reviewed against R1/R2/R6/R9/R10/R11/R17/R21/R24,
two citation defects (near-miss R6 violations) found and fixed before this report was written.
