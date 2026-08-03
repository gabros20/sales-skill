# Spec review — sales pack (opus, post-integrator, commit 9cfec5a)

Single question: **is every factual claim, figure, quote, citation, and seam statement TRUE to the
research corpus and the rulings?** Style and structure are quality review's job and are not judged here.

**244 discrete fact-checks run · 213 PASS · 31 FAIL (6 BLOCKER · 12 S-MAJOR · 13 MINOR).**

Breakdown of checks: 76 permalink/URL verifications · 10 SHA/path verifications · 118
quote/figure/attribution checks against channel reports and raws · 18 tweet-date derivations ·
7 ruling greps · 9 live-sibling seam and line-cite checks · 6 structural checks.

Gate applied: `.orchestrate/inventory.md` §1 (R1–R24) + `research/synthesis.md`. Where a channel
report and synthesis disagree, synthesis governs. Sibling claims were re-grepped against the LIVE
files at `/Users/tamas/Documents/Personal/Projects/<pack>-skill/`, not against channel E's table.

---

## 1. Verdict table

### 1a. Permalinks — component-wise (integrator's priority item #3)

| Check | Result | Evidence |
|---|---|---|
| All 52 `http(s)://` URLs in the pack appear verbatim in `research/` | **PASS** | Scripted grep -rF of each URL against `research/`; 49 exact hits, 3 resolved below |
| `https://en.wikipedia.org/wiki/Brier_score` | **PASS** | Present schemeless as `en.wikipedia.org/wiki/Brier_score`, `raw/_raw-d3-forecasting-pipeline.md:342` |
| `https://gjopen.com/faq` | **PASS** | Present schemeless, `raw/_raw-d3-forecasting-pipeline.md:358` |
| `https://gong.io/forecast/` | **PASS** | Present schemeless, `raw/_raw-d3-forecasting-pipeline.md:160` |
| All 24 schemeless URLs (saastr, christophjanz, kalzumeus, paulgraham, gartner, support.google, internal.gitlab, PostHog, 15 × x.com) | **PASS** | Each found verbatim in corpus, 1–8 hits apiece |
| Pinned SHAs: PostHog `259e5a69…`, krayin `6ad119ee…`, alirezarezvani `aa8d7788…` | **PASS** (strings) / **FAIL** (one assembly) | SHAs real; see **S8** — the alirezarezvani SHA is attached to a file the corpus read at `main` |
| Cited repo paths (`contents/handbook/onboarding/sales-handover.md`, `packages/Webkul/Lead/src/Models/Lead.php`, `commercial/skills/commercial-forecaster/SKILL.md`, `content/handbook/sales/meddppicc.md`, `content/handbook/sales/command-of-the-message/command-plan.md`, `skills/gtm-enterprise-account-planning/SKILL.md`) | **PASS** | All present in corpus |
| **Verdict: zero fabricated permalinks.** The integrator's two composed-URL fixes appear to be the only URL-shaped instances. | **PASS** | — |

### 1b. Ruling greps (re-run; integrator claimed clean)

| Ruling | Check | Result | Evidence |
|---|---|---|---|
| R3 | KBCM/KeyBanc zero-figure | **PASS** | 4 hits (`SKILL.md:114,160`, `surface-enterprise-team.md:109,139`), all never-ship statements, no number attached |
| R6 | Quotes terminating in "…" | **PASS** | Zero hits across pack |
| R20 | Bare "3x" without derivation | **PASS** | 13 hits; every one carries `coverage = 1/win rate`, sits in the never-ship table, or is `3.03` from `1/0.33` |
| R5 | "70%" without subject | **PASS** | 7 hits; each carries its subject inline or is inside a quoted primary whose subject is stated in adjacent prose |
| R7 | Prior-art framing opens the flagship | **PASS** | `forecasting-honesty.md` §1 = "This is prior art, not our novelty", first section |
| R8 | MEDDPICC qualifier + in-part + live + exclusion | **PASS** in `icp-and-qualification.md:104-116` and `surface-enterprise-team.md:61-62` · **MINOR** in `SKILL.md:71` | All four components verified against `channel-d-report.md` §6e:477-505 |
| R21 | GitLab 33% only as planning-only assumption | **PASS** | `forecasting-honesty.md:148`, `SKILL.md:161`, `proposals…md:136-138` all carry the exact qualifier |
| R12 | Disclose-at-first-contact, category rule | **PASS** | Both statutes + three evasion exhibits present; the 10M-threshold correction shipped in inverted-danger form |
| R13 | Both Google numbers, 5,000/day Google-primary | **PASS** | 0.30% + 0.10% both present; Yahoo attributed secondary |
| R16 | ICP inherited | **PASS** | Funnel stages, channel clause and Poyar caveat reproduced verbatim from live `marketing/references/audience-and-segmentation.md:65-78` |
| R19 | Licensing wording | **PASS** | PostHog "the MIT permission grant, applied by PostHog to the `/contents/` folder" exact; Sourcegraph Apache-2.0 + archived-2024 travels on both citations; GitLab CC BY-SA 4.0; Founding Sales / Chaotic Flow cite-only |
| — | R-number leaks into shipped text | **PASS** | Zero |

### 1c. Seams — against LIVE sibling files

| Check | Result | Evidence |
|---|---|---|
| `marketing/references/surface-b2b-sales-assisted.md:51-53` cession quote | **PASS** verbatim | Re-read on disk; sentence spans :50-53, quote exact |
| `marketing/references/surface-b2b-sales-assisted.md:58` | **PASS** | "it does not run the outbound sequence or own the CRM pipeline stage" |
| `marketing/references/handoff.md:42` — hands back / consumes | **PASS** exact | Sales's mirror uses marketing's own two phrases verbatim |
| `marketing/SKILL.md:107` | **PASS** | Cession row present |
| `marketing/references/lifecycle-and-email.md:15` (integrator fix 17) | **PASS** | Dunning→product at :15 confirmed |
| `marketing/assets/email-compliance-checklist.md` | **PASS** | Exists |
| `growth/references/handoff.md:42` — hedge shape | **PASS** exact | Sales mirrors growth's own sentence word-for-word, unconditional clause intact |
| `growth/references/surface-b2b-sales-assisted.md:110-112` | **MINOR** | Claim's text sits at :112-113 (M8) |
| `success/references/renewals-and-expansion.md:117-124` | **PASS** exact | §6 "The sales seam — contested, not settled" spans exactly :117-124 |
| `success/…renewals-and-expansion.md:138-139` + `surface-b2b-high-touch.md:154` (integrator fix 18) | **PASS** | Both invariant lines confirmed; success's own word is "provisional", which sales correctly mirrors |
| `success/SKILL.md:95` (integrator fix 16) | **PASS** | Dunning→product confirmed |
| `product/SKILL.md:27` | **PASS** | "qualification and CRM to `sales`" exact |
| `automation/references/process-capture.md:15` | **PASS** (quote) / **BLOCKER** (gloss) | Both fragments verbatim; the surrounding claim is inverted — see **B5** |
| "Only three sibling `handoff.md` files reciprocate a `sales` row" | **PASS** | Re-grepped all 13 sibling packs: marketing 1, growth 1, success 1, all others 0 |
| `product` contains zero "dunning"/"billing" | **PASS** | Re-verified independently across `product-skill/skills/` |
| Description arrows vs siblings' shipped descriptions | **PASS** | 596 chars ≤600; all six arrows land on territory the target's own description claims; "discovery calls" not bare "discovery" (product claims both "product discovery" and "opportunity discovery"); "renewals + expansion metrics (→ success, contested)" matches success's "renewals/expansion (NRR)" with the contested mark carried |

### 1d. Assets

| Check | Result | Evidence |
|---|---|---|
| `coverage_calc.py --selftest` | **PASS** | Runs clean |
| `forecast_calibration_check.py --selftest` | **PASS** | Runs clean |
| Docstring directional claims (the success build's reversed-trend class) | **PASS** | All checked: `1/0.33 ≈ 3.03` ✓; `1/0.25 = 4` ✓; Brier 0-1 vs 0-2 correctly opposed; GJ Open worked example `(1-0.7)² + (0-0.3)² = 0.18` ✓ against `raw/_raw-d3:358-360`; Wikipedia n>1000 quote verbatim; Lawrence 2006 attribution correct. **No reversed direction found.** |
| `coverage_calc.py:8-9` GitLab 33% handling | **PASS** | Paraphrase + separate quote — correct, unlike `forecasting-honesty.md:144` (S2) |
| `loss_prediction_log.md` patio11 quote | **FAIL** | See **S3** |
| `stage_exit_criteria_audit.md` GitLab aging figures | **PASS** | SMB 7/15, MM 21/45, Large/PubSec 45/90 + New Business + stages 1-2 scoping all match `raw/_raw-c2:268-272` |
| `SOURCES.md` promised at `SKILL.md:218` | **FAIL** | Confirmed absent at both repo root and pack root — **S1** |
| `evals/` promised in the same paragraph | Noted | Directory exists, empty; integrator flagged it as scheduled |

### 1e. Mid-quote elisions (integrator's priority item #3 — "five remaining")

Ten elision instances across eight quotes, not five. Each checked against its raw:

| File:line | Source | Verdict |
|---|---|---|
| `icp-and-qualification.md:84` | `channel-b-report.md:286` | **PASS** — reproduces the corpus's own elision exactly |
| `win-loss-learning.md:54-55` | `raw/_raw-d5:35-42` | **FAIL** — drops "It is proposed that", a hedge (**S11**) |
| `win-loss-learning.md:63-64` | `raw/_raw-d5:61-71` | **FAIL** — drops the n=52/n=378 subjects from the quote and silently closes the raw's trailing "…" with a period (**S11**) |
| `forecasting-honesty.md:39` | `raw/_raw-c0c:48-52` | **PASS** — reproduces the source's own elision |
| `forecasting-honesty.md:144` | `raw/_raw-c2:229-231` | **FAIL** — reverses source order (**S2**) |
| `forecasting-honesty.md:207` | `raw/_raw-b3:201` | **PASS** — reproduces the raw's own re-fetch, which still carries one "…" despite claiming full recovery |
| `forecasting-honesty.md:227` | `raw/_raw-c2` booking-metric fields | **PASS** — leading elision only, meaning intact |
| `crm-and-pipeline.md:99` | `raw/_raw-b3:266-267` | **PASS** — reproduces the raw exactly; elided content is unrecovered in the corpus too |

---

## 2. Findings, ranked

### BLOCKERS

**B1 — The pack ships two different stage counts for the same permalinked GitLab artifact.**
`references/forecasting-honesty.md:95` says GitLab publishes "a detailed, named **nine-stage**
opportunity process with exit criteria per stage". `references/crm-and-pipeline.md:39` and
`references/surface-enterprise-team.md:37` both say "**ten** named opportunity stages". All three
cite the identical permalink
(`…/46180fa3…/content/handbook/sales/commercial/comm-sales-opp-stages/_index.md`). The dedicated
GitLab channel states "GitLab Commercial Sales uses **10 named** opportunity stages (11 counting the
terminal 'Closed Won' label separately from numbered stages)" (`raw/_raw-c2-gitlab-handbook.md:47`).
Channel D's "nine" (`channel-d-report.md:286`, `raw/_raw-d3:31,455`) is contradicted by D's own
enumeration on the same line, which lists ten items. At least one of the pack's two numbers is wrong,
and they cannot both stand.

**B2 — The never-ship recognition table inverts the subject of a figure, in the pack that teaches
subject discipline.** `SKILL.md:146` ships: *"92% of **buyers** give up after 4 follow-up nos"*. The
corpus claim is about salespeople: *"92% of **salespeople** give up after 4 nos; 80% of **prospects**
say no 4 times"* (`channel-d-report.md:112`, and again at `:534`). Synthesis §3.2 renders it
subject-neutral ("92% give up after 4 nos"); "buyers" appears in no source. The table's stated job is
recognition so a reader can correct the figure in the wild — with the subject inverted, a reader will
not recognise the real claim, and the row itself violates the R5 discipline the same table enforces
two rows below.

**B3 — A fabricated review attribution.** `references/win-loss-learning.md:151-152` describes
`gtmagents/gtm-agents` as *"a broad, ~12–13-of-14-item pack graded generic and templated **on the
skill Anthropic-family reviewers actually read**."* No such reviewer exists anywhere in the corpus.
The grading is channel A's own: *"content verified generic/templated (see §Pack notes)"*
(`raw/_raw-a1-ecosystem-breadth.md:55`) and *"generic/templated (A1 read a full SKILL.md)"*
(`channel-a-report.md:30`). Every corpus occurrence of "Anthropic" refers to
`anthropics/knowledge-work-plugins`, a different repo that this claim is not about. The sentence
ships an invented third-party review and implies Anthropic assessed a competitor's pack.

**B4 — A seam misstatement that contradicts synthesis §5.2 and two other files in this pack.**
`references/icp-and-qualification.md:53-55`: *"Product's own router confirms the split cleanly,
ceding 'qualification and CRM to `sales`' without qualification — **the only unhedged cession to
sales found anywhere in the family's routing tables**."* Synthesis §5.2 (R15) states: *"Marketing
row: **FIRM, zero hedge**."* This pack's own `references/outbound-and-prospecting.md:42-46` and
`references/objections-and-enablement.md:31-36` both say marketing ceded *"with no hedge word, three
times over"* — including at `marketing/references/handoff.md:42` and `marketing/SKILL.md:107`, which
are routing tables, both re-verified on disk this pass. Channel E's source wording was *"the only
**unqualified, non-provisional** cession"* (`channel-e-report.md` §B); rewriting that as "unhedged"
collides with the family's reserved term for the marketing seam and makes the sentence false.

**B5 — An inverted claim about a quoted sibling sentence, against a synthesis-recorded repair
item.** `references/handoff.md:82-83` quotes automation saying its commercial upstreams *"do not yet
exist as shipped skills"* and then asserts: *"Both statements were accurate when written and **become
true the moment this pack ships** — **no sibling edit is needed**."* Sales shipping makes that
sentence more false, not true. Synthesis §9 explicitly queues the opposite: *"automation
process-capture stale count + its **now-stale** 'do not yet exist' sentence (product/marketing
shipped)"* is on the sibling queue to clear **at sales release**. `product-skill` and
`marketing-skill` are shipped on disk today.

**B6 — The contested anchoring pair ships with no permalinks, in a file that twice claims it does.**
`references/proposals-pricing-and-negotiation.md:47-48` opens: *"both sides are **permalinked**"*, and
its Validation at `:144` requires *"both **permalinked** positions"*. Neither Schweinsberg et al.
(2023) nor Maaravi & Levy (2017) carries a DOI, URL, or grade anywhere in the file. R24 requires the
pair ship "with permalinks both sides"; R1 requires permalink or explicit grade. Both are in the
corpus: DOI `10.1073/pnas.2218582120` (open access, `raw/_raw-d5:206`) and DOI
`10.1017/s193029750000646x` plus an open-access Cambridge Core PDF (`raw/_raw-d5:232-234`). Every
other peer-reviewed citation in the pack (Nisbett, Lawrence, Fildes, Huang, Yeomans) carries a DOI or
URL — these two are the only bare ones, and the file asserts the opposite in its own text.

### S-MAJOR

**S1 — `SOURCES.md` does not exist.** `SKILL.md:218` promises "Attribution, licences, and what this
pack claims for itself — `SOURCES.md` at the repository root." Confirmed absent at repo root and pack
root. Fixer should build it from the pack's actual citations plus synthesis §7's licensing rules.

**S2 — The GitLab 33% quote reverses source order.** `references/forecasting-honesty.md:144` ships
`"Win rate - 33% … This is a calculation only and should be used to set goals and plan."` In the
source the caveat **precedes** the number: *"The following calculation is used to measure/plan for
sales capacity. This is a calculation only and should be used to set goals and plan... Days to close
- 180 days / Months to close - 6 months / **Win rate - 33%**"* (`raw/_raw-c2:229-231`). The ellipsis
asserts a sequence the source does not have. `assets/coverage_calc.py:8-9` handles the same material
correctly (paraphrase + separately-quoted caveat) — copy that pattern.

**S3 — The patio11 quote is altered in two files and correct in a third.**
`references/win-loss-learning.md:127` and `assets/loss_prediction_log.md:5` both ship
*"…because of X.' **In advance.**"* — capitalised as a new sentence. The source reads
*"…because of X.' **in advance.**"* (`raw/_raw-b1-founder-led-sales.md:200`, and identically at
`channel-b-report.md:48`). `references/forecasting-honesty.md:192` ships it correctly, so the pack
contradicts itself on the same verbatim quote in three places.

**S4 — Two wrong publication dates on the default surface's opening exhibit.**
`references/surface-founder-led-solo.md:36` dates `x.com/arvidkahl/status/1896219399369249126` to
2026-03-02; the ID derives to **2025-03-02**. `:49` dates `…/1897011837893550461` to 2026-03-04; it
derives to **2025-03-04**. I derived dates from all 18 X status IDs in the pack: the other 16 match
the pack exactly. The corpus carries the same error (`channel-b-report.md:69`), so this is inherited
rather than introduced — but it is provably wrong and trivially fixable.

**S5 — A researcher's summary sentence is presented as a source quote.**
`references/crm-and-pipeline.md:55-56`: *"EspoCRM's published docs describe a stage as **'a named
entity mapped to a status value'** with an ordering constraint and nothing else."* That phrase is the
channel analyst's own bolded conclusion (`raw/_raw-c0b:211`: "**A stage is a named entity mapped to a
status value, with an ordering constraint. Nothing more.**"), not EspoCRM's wording. EspoCRM's actual
text is *"Each stage is mapped to the Status field value. Each stage is stored as an entity."*
(`raw/_raw-c0b:204-205`).

**S6 — The Medallia 19.5% figure ships with no permalink, adjacent to a permalink for a different
figure.** `references/surface-enterprise-team.md:106-108` reads: *"…team quota attainment holding at
57% (https://x.com/thaAdamLittle/status/2037542426160648422), **Medallia 19.5%**."* The Medallia
figure's real source is `x.com/thaAdamLittle/status/2047040250212495660`
(`raw/_raw-b3-pipeline-forecast-crm.md:373`), which appears nowhere in the pack. R1 fails: no
permalink and no grade, with a misleading nearest-URL.

**S7 — "No traceable source at all" overstates the corpus for one of the two 57% cousins.**
`references/when-sales-applies.md:103-104` ("The other two have **no traceable source at all**") and
`SKILL.md:145` ("the cousins have no traceable source at all"). The "9 in 10 buyers rule a firm out"
claim has three named sources — *"Hinge Marketing / Archmark / ArchDaily blog links in SOURCES.md
(industry blogs, not primary research)"* — graded **"UNSOURCED (secondary/marketing-blog sourcing)"**
(`raw/_raw-e1-webdesign-lift.md:241`, `channel-e-report.md:280`). The defensible claim is "no
**primary** source; the sourcing is industry marketing blogs."

**S8 — A composed citation of the same class as integrator fixes 13/14.**
`references/forecasting-honesty.md:44-47` cites
*"`commercial/skills/commercial-forecaster/SKILL.md`, **read at pinned commit `aa8d7788…`**"*. The
corpus read that file at `main`
(`raw/_raw-a0:86` → `github.com/alirezarezvani/claude-skills/blob/main/…`; `raw/_raw-c0c:44` →
`raw.githubusercontent.com/…/main/…`). `aa8d778` is the SHA at which the **six licence files** were
read (`channel-a-report.md:455-458`, `raw/_raw-c0c:140`). Every component is real; the assembly —
"this SKILL.md was read at this SHA" — is not in the corpus. The integrator warned this failure mode
would recur invisibly to a URL-shaped check; this is one line below its own fix 13.

**S9 — Two statutes quoted verbatim with neither permalink nor grade.**
`references/outbound-and-prospecting.md:108-116` quotes EU AI Act Art. 50(1) and 50(5) and California
SB 1001 §§ 17940–17943 directly, with no link and no evidence grade. Both permalinks are in the
corpus: `eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689` (`raw/_raw-d4:226`) and
`leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=7.&title=&part=3.&chapter=6.&article=`
(`raw/_raw-d5:307`). Synthesis §7 calls court opinions and statutes/OJ text *"freely quotable, our
best primaries"* — the pack's strongest citations are its only unlinked ones.

**S10 — A named individual is cited as a folklore propagator while his rejection of it is
suppressed.** `references/proposals-pricing-and-negotiation.md:129-131`: *"an unattributed 'the
science says $9.99 beats $10' claim circulates in this corpus's founder-led material with no study
named ([@dvassallo](…), FOLKLORE)."* The actual tweet is a rejection: *"The science says that a $10
product sells significantly more when priced $9.99. **Yet, I prefer pricing my products in multiples
of $5.** A $9.99 price makes me feel as if the seller is taking advantage of a bug in my brain."*
The raw flags this explicitly: *"Note the author declines to follow it — so the tweet is both a
folklore specimen **and a reasoned** [rejection]"* (`raw/_raw-b1:148-154`).

**S11 — Two Nisbett & Wilson elisions change what the quote says.**
(a) `references/win-loss-learning.md:54-55` elides across *"**It is proposed that** when people
attempt to report on their cognitive processes…"* (`raw/_raw-d5:35-42`), turning the authors' own
hedged proposal into a flat assertion — the exact hedge-dropping class the brief asks about.
(b) `:63-71` elides *"—four different nightgowns in one study (378 subjects) and"* and *"in the other
(52 subjects)"*, removing the study's subject and N from inside the quote (the prose above restores
them, which mitigates but does not fix the quote), and closes with *"virtually all subjects denied
it**.**"* where the raw records *"virtually all subjects denied it**…**"* (`raw/_raw-d5:71`) — a
truncated quote silently rendered complete.

**S12 — Two terminal stages attributed to the wrong GitLab page.**
`references/surface-enterprise-team.md:43-45` attributes `9-Unqualified` and `10-Duplicate` to the
comm-sales-opp-stages permalink. The corpus sources them to a different page: *"parallel terminal
states: `8-Closed Lost`, and — **per the companion GTM-resources page** — `9-Unqualified`,
`10-Duplicate`"* (`raw/_raw-c2:51-53`). This also makes the file's own "ten named opportunity stages"
read as twelve enumerated items (see B1).

### MINOR

- **M1** — `objections-and-enablement.md:44-45` and `:65`, and `demo-and-narrative.md:39`, cite
  "`icp-and-qualification.md` **§1**" for methodology-evidence content. That file's §1 is "ICP is
  inherited, not redefined"; the methodology evidence lives under "MEDDIC/MEDDPICC: evidence and
  legal status". The file uses named anchors, not numbered sections — three cross-references point at
  the wrong content.
- **M2** — `objections-and-enablement.md` Contents says "2. No framework has published evidence";
  the header reads "2. No framework has published evidence **a technique changes outcomes**". Same
  class as integrator fix 25.
- **M3** — `outbound-and-prospecting.md:110` quotes Art. 50(5) as *"at the latest at the time of the
  first interaction."*; the source reads *"…first interaction **or exposure**."* (`raw/_raw-d4:234`).
- **M4** — `icp-and-qualification.md:130-133` silently drops the source's trailing parentheticals
  from two MEDDPPICC glosses: Decision Criteria loses *"(includes the technical and financial lens
  with which the customer views GitLab)"*, Paper Process loses *"(including the MSA, order form, PO,
  etc.)"* (`raw/_raw-c2:158-166`).
- **M5** — `outbound-and-prospecting.md:77` states *"SPF/DKIM required for all senders"*; Google's
  own summary line is *"All senders: SPF **or** DKIM. Bulk senders: SPF, DKIM, and DMARC."*
  (`raw/_raw-d4:147`). The slash reads as a conjunction on a compliance requirement.
- **M6** — `outbound-and-prospecting.md:62` says the stated range *"undersells the low end by a
  third"*. The stated low bound (20k) is **higher** than the arithmetic (15k). The corpus's clearer
  phrasing: *"his own numbers imply a funnel one-third better than he claims"* (`raw/_raw-b2:99`).
  The magnitude is right; the direction word is ambiguous.
- **M7** — `win-loss-learning.md:49` says *"PRIMARY, full text read directly
  (https://psycnet.apa.org/record/1978-00295-001)"*. The full text was read from the CSULB PDF; the
  psycnet link is the bibliographic record only (`raw/_raw-d5:28-31`).
- **M8** — `handoff.md:41` cites `growth/references/surface-b2b-sales-assisted.md:110-112` for "does
  not extend that result's confidence to a deal-stage outcome it didn't test"; the clause sits at
  :112-113 on disk. Channel E's spec pointed at `:144` for the provisional-seam statement.
- **M9** — `SKILL.md:71` describes the MEDDPICC ruling with the "business education services and
  content" qualifier but without the in-part / live-case / McMahon-exclusion corrections R8 requires
  "when the ruling is described". The two reference files carry all four; the router row does not.
- **M10** — `surface-enterprise-team.md:79-80` softens Sourcegraph's README warning to *"may be out
  of date"*; its actual text is *"incorrect content has been added before the repo was archived"*
  (`raw/_raw-c3:74`).
- **M11** — `agentic.md:45-49` quotes the TechCrunch investigation four times (ZoomInfo ×2, Airtable,
  "nearly two dozen sources") with a date but no permalink. The URL is in the corpus at
  `raw/_raw-d4:194`.
- **M12** — `outbound-and-prospecting.md:114-116`: *"the threshold-bearing term 'online platform'
  **appears only** inside § 17942(c)'s service-provider carve-out."* It is also defined at
  § 17940(c). The corpus's careful wording is *"appears in the **operative text** of this chapter in
  exactly one place"* (`raw/_raw-d5:346-349`).
- **M13** — `assets/stage_exit_criteria_audit.md:7` labels Odoo's `crm_stage.py` LGPLv3 (correct per
  `raw/_raw-c1:267`); `crm-and-pipeline.md:52` cites the same file with no licence attached, against
  the pack's own Validation line requiring "every stage or field pattern cited names its source CRM
  and license."

---

## 3. What passed that was worth checking

- **Every permalink in the pack resolves component-wise to the corpus.** 76 URLs, 10 SHAs/paths.
  The integrator's composed-permalink failure mode recurs exactly once more (S8) and it is a SHA
  attribution, not a URL.
- **The three handoff rows are faithful to the live siblings, not to E's table.** Marketing's
  hands-back and consumes phrases are reproduced word-for-word from `marketing/handoff.md:42`;
  growth's unconditional clause is mirrored verbatim from `growth/handoff.md:42`; success's Murphy
  position, complexity gate and "not Account Management carryover" all match
  `success/renewals-and-expansion.md:117-124`. The integrator's three line-cite corrections
  (16/17/18) are all correct on disk.
- **The MEDDPICC ruling survives a line-by-line comparison with `channel-d-report.md` §6e** — court,
  docket number, judge, both ECF numbers, filing date, the "would be compelled to find" holding, the
  registration number, "DENIED in all other respects", "granted in part and denied in part", the
  surviving claims, the 2026-07-16 docket date, the nine-topic McMahon exclusion, and the PTC-1990s /
  2005-MEDDPICC history.
- **Every peer-reviewed quote is verbatim**: Nisbett & Wilson (three of four), Lawrence et al. 2006
  (sandbagging + calibration definition), Fildes & Goodwin 2007 (52.8% and 25%), the Brier n>1000
  sentence, Good Judgment Open's averaging clause, Schweinsberg's significance statement, Maaravi's
  abstract, Huang 2017 and Yeomans 2019 author lists and DOIs.
- **Every primary-source figure checks**: Odoo 2,890 lines with zero "accuracy" hits (re-grepped
  independently), Twenty's five default stages, atomic-crm's `Delayed`, frappe's SLA field list,
  GitLab's exit criteria / ARR gates / aging clocks / $25k loss-detail threshold / $50k CSM formality
  / 3-4 CSM introduction, CEB's n=1,500 / 22 orgs / 10 industries / 57% / 70% supplier maximum,
  Gartner's six-to-10 with its deconfliction clause, RAIN's 489 sellers, RepVue's 45/26.7/59.7 with
  "share of reps at quota", the 11x contested pairs on both sides, coreyhaines31's 42,757★ and 84,811
  installs and 270/355-line files, awesome-copilot's 37,357★, alirezarezvani's 23,656★ and 70/30
  weighting and five copyright holders.
- **Both assets self-test clean, and no directional claim in either docstring is reversed** — the
  specific failure the success build's spec review caught does not recur here.
- **The description is 596 chars, collides with no shipped sibling**, and every cession consumed
  reaches it — including the two the integrator fixed ("discovery calls", "expansion metrics").

---

## 4. Note for the fixer

B1, B2, B3, B4 and B5 are all one-sentence corrections. B6 and S9 need permalinks lifted from
`raw/_raw-d5` and `raw/_raw-d4`. S1 is a new file. S2, S3, S5, S10 and S11 are quote-integrity
repairs — in each case the correct text is quoted in this report with its raw line number.

`icp-and-qualification.md` is at 206 lines against a 140–180 budget (ceiling 207), so B4's fix must
be length-neutral: it is a wording change ("the only unqualified, non-provisional cession"), not an
addition.
