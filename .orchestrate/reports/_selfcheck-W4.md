# Self-check — W4 (ICP/qualification + outbound + agentic)

Files written:
- `skills/sales/references/icp-and-qualification.md` (208 lines; budget 140–180, soft ±15% ceiling
  ~207 — held ~1 line over rather than cutting the MEDDPICC correction or the reproduction exhibit)
- `skills/sales/references/outbound-and-prospecting.md` (160 lines; budget 150–190)
- `skills/sales/references/agentic.md` (116 lines; budget 110–140)

## Ruling-by-ruling

- **R1** (permalink or explicit grade). Every figure/quote carries either a tool-returned x.com
  permalink, a commit-pinned GitLab blob path, a live-fetched primary URL (support.google.com,
  eur-lex.europa.eu text quoted without a bare link since the statute citation form itself is what
  the corpus uses), a docket citation (ECF 99/100, no press-release substitute), or a family
  file:line cite re-verified by my own `grep -n` against the live sibling repos (not copied blind
  from Channel E's table — two of E's own citations had drifted from the charter's originals, and
  I confirmed marketing's `surface-b2b-sales-assisted.md:51,58,111` and `handoff.md:42` and
  `SKILL.md:107`, growth's `handoff.md:42`, and product's `SKILL.md:27` all resolve at the line
  cited, at time of writing). No reconstructed permalink used anywhere.
- **R2** (figure-survival). Figures shipped: the levikmunneke funnel chain (arithmetic IS the
  teaching, clause b — the 15k vs. 20k discrepancy is the point); Gmail's 0.30%/0.10% (both from
  the same primary page, both required together); GitLab's $100K/$50K ARR thresholds (primary,
  both numbers necessary to the teaching); the MEDDPICC ruling (both the holding and its two
  corrections travel together — nothing shipped as a bare "MEDDPICC is generic" without the
  business-education-services qualifier and the live-case caveat); 11x's ARR/retention pairs
  (clause a/c — reader must recognise both sides are contested, both permalinked in the same
  TechCrunch piece). No orphan figure shipped without its correcting half.
- **R3** (KBCM). Confirmed absent by grep after writing:
  `grep -ri kbcm skills/sales/references/{icp-and-qualification,outbound-and-prospecting,agentic}.md`
  returns nothing.
- **R5** (bare 70%). No orphan "70%" ships. The one "70%"-containing string
  (`outbound-and-prospecting.md:96`, "60–70% positive reply rates") carries its subject and
  disqualifier inline in the same clause (one vendor's cherry-picked case study, not a benchmark).
- **R6** (no truncated quotes). Caught and fixed two of my own drafting errors during self-review:
  I had inserted my own mid-quote "…" (not present in the source) into the EU AI Act Art. 50(1)
  text, the seanlongden copy-spinning prompt, the NickAbraham12 warmup-tool quote, and GitLab's
  Champion definition. All four were rewritten to either quote the source in full or trim at a
  natural clause boundary with no ellipsis of my own manufacture. The one remaining "…" in the
  files (`icp-and-qualification.md:84`, the @meddpicc vendor tweet) is verbatim from the source
  raw, mid-quote (bullet separator in the original tweet), and the quote does not *end* in "…" —
  compliant with R6's actual target (truncation-by-our-tooling), not a violation of its letter.
- **R8** (MEDDPICC ruling). Stated exactly per the ruling: "generic for business education services
  and content" qualifier never stripped; SJ granted in part / denied in part stated explicitly;
  "DENIED in all other respects" and the surviving tortious-interference/trade-libel claims stated;
  case-live status (docket through 2026-07-16) stated; McMahon's testimony stated as **excluded**
  (not relied upon — the inversion error from D1's press-release sourcing is named and corrected in
  my own text); cited to ECF 99/100 throughout, the press release never cited as a source.
- **R9** (taxonomy split). Frameworks (MEDDIC/MEDDPICC/BANT) vs. methods (SPIN/Challenger/Sandler)
  stated as a named section with its own header; the corpus's own conflation (including D1's raw)
  named as the failure mode being corrected. Practitioner-opinion-is-split stated with the
  BowTiedSalesGuy same-person-opposite-positions exhibit (14 months apart), and "never call
  Sandler/Gap Selling research-backed or debunked" stated explicitly with the reasoning (no
  empirical claim exists to grade, a different null from SPIN/MEDDIC's unpublished-study null).
- **R10** (discovery gap). Stated in "What discovery evidence does not validate": non-sales-dyad
  rapport evidence vs. no published branded-methodology win-rate evidence, with the explicit rule
  that a qualification/discovery framework may never borrow the rapport papers' authority. Full
  treatment correctly routed to `discovery-calls.md` (W3's file) rather than re-derived here.
- **R11** (trademarked methodologies — cite, never reproduce). GitLab's MEDDPPICC nine-letter
  expansion and one-line glosses are cited (CC BY-SA 4.0, attributed); the qualifying-question
  banks are explicitly named and declined ("not reproduced here... paraphrase or omit"). The
  awesome-copilot MEDDICC letter-by-letter reproduction is named as the cautionary exhibit,
  contrasted with refoundai/lenny-skills' lower-risk cited version. GitLab's own Force Management
  redaction ("Due to IP constraints...") cited as the precedent for the posture this file follows.
- **R12** (AI policy). Disclosure rule stated with both statutory anchors (EU AI Act Art. 50(1) and
  (5); California SB 1001, with the 10M-visitor-threshold misreading explicitly corrected — the
  threshold gates only the § 17942(c) service-provider carve-out, not the § 17941(a) prohibition).
  Category rule (never manufacture false engagement signals) stated as binding tools that don't
  exist yet, with all three exhibits (copy-spinning, simulated engagement, proxy farming) and the
  funded-industry data point. `ai` vs. sales boundary (mechanics vs. whether-to) stated explicitly
  in both outbound-and-prospecting.md and agentic.md.
- **R13** (deliverability — cite, never restate). Marketing's cession and CRM-disclaimer quotes are
  cited with file:line, never restated as sales's own doctrine. Google numbers always both stated
  together (0.30%/0.10%); 5,000/day stated as Google-primary, Yahoo-secondary, never fused.
- **R14** ("email is cooked" CONTESTED). Both poles permalinked (jeffreyhuber's collapse assertion
  vs. NickAbraham12/seanlongden's configuration-diagnosis); the structural warmup-industry evidence
  and the harsh_biz first-person exhibit both carried; the asymmetry (diagnosis vs. assertion)
  stated explicitly rather than resolved.
- **R16** (ICP inherited from marketing). Opens icp-and-qualification.md's first substantive
  section. Marketing's five-stage funnel is described and attributed (named-practitioner framework,
  Kyle Poyar, dated, evidence-grade caveat preserved) rather than restated as if it were sales's own
  finding; sales's role is stated narrowly as account-selection application, not fit-criteria
  authorship. Explicit "never draft a new ICP definition inside a sales deliverable" rule stated,
  and E.4's own framing (the most likely accidental-contradiction seam) is echoed.
- **R17** (term discipline). "Sales-qualified lead" spelled out on first use; "qualification"
  explicitly ruled out as customer-facing journey vocabulary, citing design's prior ruling.
  "Discovery" never appears bare as a process-step name — checked by grep; every instance is either
  "discovery call(s)," "discovery conversation," or refers to the academic evidence, not the sales
  step. "CRM pipeline stage" only appears inside a direct quote from marketing.
- **R19** (licensing wording). GitLab handbook prose cited as CC BY-SA 4.0 ("GitLab handbook prose,
  CC BY-SA 4.0 — quotable with attribution"). `github/awesome-copilot` cited as MIT (no adaptation,
  citation only). `louisblythe/sales-skills` stated explicitly as **no license file — cite only,
  never lift**, per the corpus's own verdict, in agentic.md. No adaptation of any incumbent's
  content attempted anywhere in these three files — citation and paraphrase-with-attribution only.
- **R23** (11x figures; AI-SDR market sizes never-ship). Both contested pairs (ARR, retention) from
  the same TechCrunch piece carry both sides every time they're mentioned — checked by re-reading
  agentic.md's AI-SDR section twice for a lone-sided citation; none found. "$5.8B... over 20% a
  year" AI-SDR market-size figure is named explicitly as never-ship and not otherwise used as a
  citable fact anywhere.
- **Touched but governed by other writers' files, not re-derived here**: R7 (forecasting prior art —
  W2's flagship), R15 (handoff mirror rows — W6's file; I did not write a handoff row), R18
  (dunning/billing routing — not in scope for these three files), R20/R21/R22 (win-rate/coverage/
  GitLab-33%/vendor-forecast-accuracy — W2's forecasting-honesty.md), R24 (anchor-first — W5's
  proposals-pricing-and-negotiation.md).
- **Not applicable**: R4 (57% CEB figure — W1's front-door file; confirmed absent by grep above).

## Cross-file consistency checks performed

- Re-verified all family file:line citations against the live sibling repos with `grep -n` rather
  than trusting Channel E's table verbatim (E's own report flags that two of fourteen cites had
  already drifted by the time it was written) — all four citations used here (marketing ×3 lines,
  product ×1 line) resolved exactly at the line cited.
- Re-read all three files end-to-end after the R6 ellipsis fixes to confirm no other
  self-manufactured truncation remained.
- Confirmed `agentic.md` never restates `outbound-and-prospecting.md`'s policy content — it only
  states what changes structurally under autonomy, per the family's overlay convention
  (cross-checked against success's `overlay-agentic.md` as the format model).

## Gaps flagged (not invented)

- No gap required a GAP flag. Every fact the inventory row called for (R16 opening, R9 taxonomy,
  R8 MEDDPICC ruling exact, GitLab MEDDPPICC + ARR thresholds, qualification-first vs. friction-gate
  tension; marketing's cession opening, R12/R13/R14 governance, harsh_biz exhibit, evasion category;
  R23, disclosure operationalized, salesxsaas challenge, ai boundary, louisblythe cite-only) was
  present in the assigned research corpus with a citable permalink or an explicit grade already
  attached by the channel reports.
- PostHog's ICP/lead-scoring handbook files (`lead-scoring.md`, `product-led-lead-qualification.md`,
  `who-we-do-business-with.md`) are named in the synthesis as the richest unmined seam for this
  exact file, but no raw file in my assigned reading contains their actual content — only that they
  exist and were not deep-read. Not cited; flagged here rather than guessed at.
