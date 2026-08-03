# Fixer report — sales pack spec-review fixes (sonnet)

Applied all 31 findings from `.orchestrate/reports/_spec-review.md`. All applied-as-specified;
no deviations, nothing could not be applied.

## BLOCKERS

- **B1** — applied-as-specified. `forecasting-honesty.md:95` "nine-stage" → "ten-stage" (matches
  `crm-and-pipeline.md` and `surface-enterprise-team.md`, both already "ten"). Combined with the
  S12 fix below so the "ten" count reads clean against the two extra terminal stages.
- **B2** — applied-as-specified. `SKILL.md:146` "92% of buyers" → "92% of salespeople" (matches
  `channel-d-report.md:112,534`); also fixed the parallel row in the never-ship table.
- **B3** — applied-as-specified. `win-loss-learning.md:152` — replaced the fabricated "Anthropic-
  family reviewers" attribution with "graded generic and templated after a full SKILL.md read"
  (matches `channel-a-report.md:30`).
- **B4** — applied-as-specified. `icp-and-qualification.md:55` "unhedged" → "unqualified,
  non-provisional cession" (matches channel-e-report.md §B). Length-neutral: the MEDDPPICC-glosses
  paragraph (needed for M4) was rewrapped to hold the file at exactly 207 lines, the stated ceiling.
- **B5** — applied-as-specified. `handoff.md:82` — rewrote to describe automation's "do not yet
  exist as shipped skills" sentence as now-stale (product and marketing are shipped on disk),
  queued on the family's sibling-repair list per synthesis §9, explicitly not "no sibling edit is
  needed."
- **B6** — applied-as-specified. `proposals-pricing-and-negotiation.md` §2 — added Schweinsberg
  (DOI 10.1073/pnas.2218582120) and Maaravi & Levy (DOI 10.1017/s193029750000646x + Cambridge Core
  open-access PDF) permalinks so the file's own "both sides are permalinked" claim is now true.

## S-MAJOR

- **S1** — applied-as-specified. Created `SOURCES.md` at repo root, modeled on
  `success-skill/SOURCES.md`'s structure (wedge, licences by tier, trademarks, academic/legal
  sources, practitioner sources, never-ship figures, what this pack claims/didn't do). Every entry
  traces to a citation already shipped somewhere in `skills/sales/`.
- **S2** — applied-as-specified. `forecasting-honesty.md` §4 — restored the source's actual order
  (caveat sentence first, "Win rate - 33%" as one line item inside the same calculation), no longer
  a merged quote asserting a sequence the source doesn't have.
- **S3** — applied-as-specified. Lowercased "In advance." → "in advance." in both
  `win-loss-learning.md:126` and `assets/loss_prediction_log.md:5` to match
  `forecasting-honesty.md:192`'s correct casing.
- **S4** — applied-as-specified. `surface-founder-led-solo.md` — both arvidkahl dates corrected
  2026 → 2025 (ID-derived).
- **S5** — applied-as-specified. `crm-and-pipeline.md:54` — separated the channel analyst's own
  bolded conclusion ("a stage is a named entity...nothing more") from EspoCRM's actual docs text
  ("Each stage is mapped to the Status field value...").
- **S6** — applied-as-specified. `surface-enterprise-team.md:108` — added the correct Medallia
  permalink (`.../status/2047040250212495660`).
- **S7** — applied-as-specified. `SKILL.md:145` and `when-sales-applies.md:101` both rewritten to
  differentiate the two "57%" cousins: "9 in 10" traces to industry marketing blogs (UNSOURCED,
  not "no traceable source"); the 70–80% Shipley figure has no traceable source at all.
- **S8** — applied-as-specified. `forecasting-honesty.md:45` — SKILL.md now cited as read at
  `main`; the pinned SHA is scoped only to the licence-file verification, matching what the corpus
  actually supports.
- **S9** — applied-as-specified. `outbound-and-prospecting.md` — added EU AI Act (eur-lex OJ text)
  and CA SB 1001 (leginfo.legislature.ca.gov) permalinks to both statute quotes.
- **S10** — applied-as-specified. `proposals-pricing-and-negotiation.md` §7 — reframed the
  dvassallo citation to show he is the one rejecting the "$9.99" folklore claim, quoting his actual
  rejection, not merely propagating it.
- **S11** — applied-as-specified (both sub-items). (a) `win-loss-learning.md:53` — restored "It is
  proposed that" into the abstract quote. (b) `win-loss-learning.md:63` — restored the n=378/n=52
  subjects inside the quote itself; the "denied it" clause is now paraphrased outside the blockquote
  with a note that the raw's own capture stops mid-sentence there, rather than silently closing a
  truncated quote with a period (also keeps the file R6-clean — no quote ends in "…").
- **S12** — applied-as-specified. `surface-enterprise-team.md:43` — `9-Unqualified` and
  `10-Duplicate` now attributed to the companion GTM-resources permalink, separate from the
  comm-sales-opp-stages permalink that documents the ten named stages.

## MINOR

- **M1** — applied-as-specified (3 instances). `objections-and-enablement.md:44,65` and
  `demo-and-narrative.md:39` — `icp-and-qualification.md §1` → named-anchor citation
  ("MEDDIC/MEDDPICC: evidence and legal status"), the section that actually carries the
  methodology-evidence content.
- **M2** — applied-as-specified. `objections-and-enablement.md` Contents entry now reads "No
  framework has published evidence a technique changes outcomes," matching the §2 header exactly.
- **M3** — applied-as-specified. `outbound-and-prospecting.md:110` — Art. 50(5) quote now includes
  "or exposure."
- **M4** — applied-as-specified. `icp-and-qualification.md` — restored both dropped parentheticals
  (Decision Criteria's technical/financial-lens gloss; Paper Process's MSA/order form/PO gloss).
- **M5** — applied-as-specified. `outbound-and-prospecting.md:77` — "SPF/DKIM required for all
  senders" → "SPF or DKIM required for all senders."
- **M6** — applied-as-specified. `outbound-and-prospecting.md:60` — replaced the ambiguous
  "undersells the low end by a third" with the corpus's clearer framing: the upper bound is exactly
  right, and the author's own numbers imply a funnel one-third better than he claims at the low end.
- **M7** — applied-as-specified. `win-loss-learning.md:49` — full text now cited as read from the
  CSULB PDF; the psycnet.apa.org link is labeled as the bibliographic record only.
- **M8** — applied-as-specified. `handoff.md:41` — growth citation `:110-112` → `:112-113`.
- **M9** — applied-as-specified. `SKILL.md:71` — MEDDPICC ruling row now carries all four
  corrections (business-education-services qualifier, SJ granted in part, case live as of 2026-07,
  McMahon testimony excluded), matching R8's requirement.
- **M10** — applied-as-specified. `surface-enterprise-team.md:79` — Sourcegraph's actual warning
  ("incorrect content has been added before the repo was archived") replaces the softened "may be
  out of date" paraphrase.
- **M11** — applied-as-specified. `agentic.md:46` — added the TechCrunch permalink.
- **M12** — applied-as-specified. `outbound-and-prospecting.md:115` — "appears only inside §
  17942(c)'s service-provider carve-out" → "appears in the operative text of this chapter in
  exactly one place," matching the raw's careful wording (the term is also *defined*, not
  operatively used, at § 17940(c)).
- **M13** — applied-as-specified. `crm-and-pipeline.md:52` — added LGPLv3 to the Odoo
  `crm_stage.py` citation, matching `assets/stage_exit_criteria_audit.md:7`'s labeling and the
  pack's own Validation requirement.

## Verification

- `coverage_calc.py --selftest` — PASS.
- `forecast_calibration_check.py --selftest` — PASS.
- Ruling re-greps: **R3** (KBCM/KeyBanc) — 4 hits, all never-ship statements, no number attached,
  zero violations. **R6** (quotes ending "…") — zero hits across the pack. **R20** (bare "3x") — 8
  hits in `forecasting-honesty.md` + 2 in `SKILL.md`, every one inside derivation/never-ship
  framing, zero violations. **R5** (bare "70%") — 6 hits, every one carries its subject inline or
  sits inside quoted primary text whose subject is stated in adjacent prose, zero violations.
- `icp-and-qualification.md` — exactly 207 lines (the stated ceiling), verified after rewrapping
  the MEDDPPICC-glosses paragraph to absorb M4's restored text without net growth.
- `SKILL.md` description — unchanged, still 596 chars (≤600).

No deviations from the work order. No finding could not be applied.
