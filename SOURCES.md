# Sources, licences, and what this skill claims for itself

This pack was built into a genre that has adopted the *form* of citation without the *function*:
the largest incumbent corpus runs an 11,105-line commercial-finance sales pack with 30 unique URLs
and zero permalinks attached to any figure, and executes an unlinked 30-cell stage-conversion table
as Python priors. This file says what was taken, from whom, under what licence, and what the pack
actually adds — rather than implying more. Full research provenance — five channel reports and
their raw files — lives in [`research/`](research/), gated by
[`research/synthesis.md`](research/synthesis.md).

## 1. The wedge

**Open by fragmentation and adoption collapse, contested on specific items — not open by absence.**
Several incumbent packs ship 9–13 of the domain's 14 canonical items, some competently; none has
real adoption, and the packs that do have adoption don't cover the domain. Breadth and installs are
inversely correlated in this genre. No single incumbent combines coverage, depth, and adoption —
that triple is the opening, not novelty on any one plank:

- **Evidence beneath the posture.** This pack cites primaries or grades folklore explicitly, and
  carries a peer-reviewed layer (Nisbett & Wilson 1977; Lawrence et al. 2006; Fildes & Goodwin
  2007; Schweinsberg et al. 2023, *PNAS*; Maaravi & Levy 2017; Huang 2017; Yeomans 2019) the genre
  does not touch anywhere.
- **Honest scope — the existence gate.** No incumbent asks whether an assisted sales motion is
  worth running at all before teaching how to run one; this pack's default reader is a solo founder,
  not an AE team, and the four incompatible practitioner gates for that question are taught as a
  live disagreement, not resolved silently.
- **Integration as the differentiator.** The field's centre of gravity annexes revenue operations,
  cold outbound, and enablement under "marketing" — exactly what this family's `marketing` pack
  refused in writing before this pack existed. Three sibling packs (`marketing`, `growth`, `success`)
  pre-drew reciprocal handoff rows for `sales`; a single incumbent pack cannot copy that.
- **The forecast-accuracy null (flagship spine).** Four independent legs — GitLab keeps its
  forecasting process gated ("Not Public"), Sourcegraph publishes the fullest method found anywhere
  and still measures nothing, eight open-source CRMs' actual probability code carries zero accuracy
  claims, and the largest MIT-licensed forecasting incumbent discloses its assumptions but never
  measures whether the resulting number was right — plus a fifth, practitioner-level check: zero X
  posts found anywhere in this research state a backtested stage-weighted probability. **Forecast
  method is publishable; forecast accuracy is published by no one.**

## 2. Licences

Verified by opening the `LICENSE` file or root licence declaration directly, not by trusting a
GitHub API badge alone.

### LIFTABLE — file-verified permissive (structure/ideas cited, not reproduced as training content)

| Source | Licence | Used for |
|---|---|---|
| `odoo/odoo` | LGPLv3 (module manifest + upstream tarball license text, not just the badge) | The sole open-source CRM found to model per-stage exit-criteria as a first-class field (`crm.stage.requirements`) — and ships it empty by default; the Naive Bayes win-probability code with zero "accuracy" occurrences |
| `twentyhq/twenty` | AGPLv3 core, MIT-licensed toolkit packages (check per-package) | The customizable-object stage-metadata pattern, contrasted with every other CRM's hard-coded enum |
| `marmelab/atomic-crm` | MIT | The `Delayed` stage — the only CRM in this corpus that gives a stalled deal a state other than Won/Lost |
| `frappe/crm` | AGPLv3 | First-response SLA fields tracked on the deal record itself, not only pre-conversion |
| `krayin/laravel-crm` | MIT | The structured (not free-text) `lost_reason` field pattern |
| `sourcegraph/handbook` | Apache-2.0, **archived 2024-07-02** — the staleness caveat travels with every citation, and the repo's own README flags that incorrect content was added before archival | The fullest published forecast method found anywhere: Won/Commit/Best Case/Pipeline/Omitted rolling up to Commit/Best Case/Call, with the headline number stated as an openly-judged middle, not a derivation |
| `alirezarezvani/claude-skills` | MIT under the repo's root grant; licence files verified at pinned commit `aa8d778811a557a2c28ccadda4cf3d0bd028a4cc`; the SKILL.md content itself was read at `main`. The tree carries five distinct copyright holders — per-directory check before adapting anything | The `commercial-forecaster` skill, cited as the prior-art object of study for assumption-disclosure forecasting, never as this pack's own novelty |
| `coreyhaines31/marketingskills` | MIT | The largest-adoption incumbent found (84,811 installs on `sales-enablement` alone) — cited for the shape of a well-organized objection library and demo-script category, never for its talk-track content itself |
| `github/awesome-copilot` | MIT | Cited as the **cautionary exhibit**, not a source to lift from: its `gtm-enterprise-account-planning` skill reproduces MEDDICC letter-by-letter with zero attribution to MEDDICC Ltd or PTC |
| `refoundai/lenny-skills` | Cited for contrast, not lifted | Reproduces MEDDIC's six letters but — unlike awesome-copilot — cites an external source, a meaningfully lower-risk version of the same act |
| `vladar107/awesome-sales-engineer` | CC0 | A reading-list pointer (Peter Cohan's *Great Demo!*, alongside SPIN and Challenger) — cited as a bibliography entry, not as evidence any of the listed books were independently verified |

### CITE-ONLY — described and linked, never reproduced

- **GitLab's public handbook** (`gitlab-com/content-sites/handbook`) — the single richest exhibit in
  this pack: the ten named opportunity stages with published exit criteria, the MEDDPPICC
  operational instance, the retain-and-expand "run parallel" sentence, the 33% planning-only
  win-rate assumption, the pipeline-aging automation, the booking-metric estimated-vs-quoted split,
  and the loss-reason taxonomy. Handbook **prose is CC BY-SA 4.0** (ShareAlike attaches to any close
  derivative published from it); **code is MIT** under the repo's separate root licence — two
  different licences, two different scopes, never conflated. GitLab itself redacted a third party's
  methodology from public view ("due to IP constraints, we have migrated content from this page to
  GitLab's internal Handbook") — an incumbent independently reaching this pack's own
  cite-never-reproduce posture for trademarked content.
- **EspoCRM's documentation** (`espocrm/documentation`) — UNLICENSED. Quoted minimally with
  attribution for its own bolded conclusion that "a stage is a named entity mapped to a status
  value, with an ordering constraint," and for its multi-pipeline feature description; nothing
  reproduced at length or built into a derivative asset.
- **`TheCraigHewitt/sales-skills`**, **`gtmagents/gtm-agents`**, **`louisblythe/sales-skills`**
  (no licence file), **`LeadMagic/gtm-skills`** — cited only for the fact of their existence, install
  counts, and content shape (win/loss skills, an AI-SDR-mechanics treatment); nothing lifted from any
  of them. `louisblythe/sales-skills`'s bot-behavior mechanics (voicemail-drop-optimization,
  ghost-recovery, response-latency-management) are named as a map of what "mechanics" covers, not as
  content to adapt.
- **PostHog's live internal handbook** (`PostHog/posthog.com`) — the MIT permission grant, applied
  by PostHog to the `/contents/` folder only; the handbook lives entirely under that path. Cited for
  its $1,000/mo sales-handover threshold, never presented as a universal PLG rule.
- **Founding Sales** (Pete Kazanjy) and **Chaotic Flow** (Joel York) — all-rights-reserved despite
  being free to read. Cite-and-link only; nothing quoted at length or reproduced.

### AMBIGUOUS or UNLICENSED, flagged and nothing built on

- **`EspoCRM`, `SuiteCRM`, `Monica`** — cited for stage-model structure only (no per-stage
  requirement field beyond Odoo's), no licence claim made or relied on beyond the EspoCRM docs entry
  above.

## 3. Trademarked methodologies — named, cited, never reproduced

Practitioner opinion on every named framework and method below is genuinely split, and this pack
claims no consensus in either direction.

| Mark | Owner / status | This pack's posture |
|---|---|---|
| **SPIN SELLING** | Trademark held by Korn Ferry (Reg. 2,413,866, via Miller Heiman, acquired 2019) **and** Huthwaite Research Group Ltd ("Huthwaite Creators of SPIN Selling," Reg. 2,823,457) — two live corporate lineages | Never assert a single current owner. Its 35,000-call study is cited as unpublished — a real null, not folklore |
| **MEDDPICC** | Reg. No. 6,489,058 ordered CANCELLED by federal court, held generic **for business-education services and content** — a partial, live ruling, not a clean win (*MEDDICC Ltd. v. 01 Consulting LLC*, E.D. Pa., ECF 99/100, filed 2026-04-21) | Cite the opinion, never the winning party's press release; always carry the qualifier, the live-case status, and the McMahon-testimony-excluded correction |
| **MEDDICC** | MEDDICC Ltd (Andy Whyte, founded 2020), commercial and live | Cite; never reproduce its training materials or qualifying-question banks |
| **Command of the Message** | Force Management LLC, Reg. 3,929,561 | Cite-only — GitLab's own handbook pulled this content from public view for exactly this reason |
| **Challenger** | Challenger Inc. (Gartner lineage); trademark record not independently pulled | Do not assert trademark specifics as verified — unverified, not absent. The one methodology in this corpus with a real peer-reviewed critique (Rapp, Bachrach, Panagopoulos & Ogilvie, 2014, *JPSSM* 34(4):245–259) |
| **BANT** | No registration located in this research; functions as generic descriptive | Safe to use as a term; its IBM-origin story is FOLKLORE — no primary IBM record located |
| **Sandler Selling System** | Sandler Systems, Inc. (incorporated Maryland, 1983) | Makes no empirical claim to evaluate at all — a different, quieter null than SPIN's; never call it "research-backed" or "debunked" |

## 4. Academic and legal sources

Grade: measured-with-method throughout. Cited by full reference at point of use in
`references/forecasting-honesty.md`, `references/win-loss-learning.md`,
`references/icp-and-qualification.md`, `references/discovery-calls.md`, and
`references/outbound-and-prospecting.md`.

- **Nisbett, R. E., & Wilson, T. D. (1977)**, "Telling More Than We Can Know: Verbal Reports on
  Mental Processes," *Psychological Review* 84(3):231–259. Full text read directly. The validity
  boundary on stated reasons — win/loss's flagship spine.
- **Lawrence, Goodwin, O'Connor & Önkal (2006)**, "Judgmental forecasting: A review of progress over
  the last 25 years," *International Journal of Forecasting* 22(3):493–518, DOI
  10.1016/j.ijforecast.2006.03.007. Sandbagging is peer-reviewed, not folklore.
- **Fildes & Goodwin (2007)**, "Against Your Better Judgment?", *Interfaces* 37(6):570–576, DOI
  10.1287/inte.1070.0309. 120 forecasters surveyed; only 52.8% ever check whether their own
  adjustments improve accuracy.
- **Schweinsberg, Petrowsky, Funk & Loschelder (2023)**, "Understanding the first-offer conundrum,"
  *PNAS*, DOI 10.1073/pnas.2218582120. 26 million eBay negotiations; anchoring's price effect is
  linear, its impasse-risk effect is nonlinear.
- **Maaravi & Levy (2017)**, "When your anchor sinks your boat," *Judgment and Decision Making*, DOI
  10.1017/s193029750000646x. Under information asymmetry, moving first is a disadvantage.
- **Rapp, Bachrach, Panagopoulos & Ogilvie (2014)**, *Journal of Personal Selling & Sales Management*
  34(4):245–259. The one real peer-reviewed critique of a named methodology (Challenger) in this
  corpus.
- **Huang (2017)** and **Yeomans (2019)**, *Journal of Personality and Social Psychology* — real
  evidence that question-asking builds liking, studied in **non-sales dyads**; no branded sales
  discovery methodology may borrow this authority.
- **CEB Marketing Leadership Council with Google (2012)**, *The Digital Evolution in B2B Marketing*
  — the sole primary behind the "57%" decision-already-made figure; n=1,500 contacts, 22
  organizations, 10 industries.
- **EU AI Act, Regulation (EU) 2024/1689, Article 50** — Official Journal text,
  eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689. Government/public record,
  freely quotable.
- **California Business & Professions Code §§ 17940–17943 (SB 1001)** — statute text,
  leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=7.&title=&part=3.&chapter=6.&article=.
  Freely quotable; the pack's clearest correction of a widely repeated scope misreading.

## 4b. Public-web primaries and vendor pages

Not academic or legal, but each is a named, checkable web source rather than a reconstructed
claim. Grade stated inline at point of use in the citing file.

- **Good Judgment Open** (`gjopen.com/faq`) — PRIMARY. The tournament explainer's own statement
  that a single scored forecast is uninformative outside its question's full lifespan — the
  small-numbers gate's second leg (`references/forecasting-honesty.md` §5).
- **Brier score reference article** (`en.wikipedia.org/wiki/Brier_score`) — PRIMARY. The
  sample-size statement behind the small-numbers gate: large N needed for rare, high-skill
  forecasts; modest N suffices for common, low-skill ones (`references/forecasting-honesty.md` §5).
- **Gartner's B2B buying-journey page** (`gartner.com/en/sales/insights/b2b-buying-journey`) — the
  live page 403s every direct fetch; quoted from a 2020-04-21 Wayback Machine snapshot, not a
  reconstructed URL. The buying-group figure, never shipped without its deconfliction clause
  (`references/surface-enterprise-team.md` §4).
- **Google's bulk-sender requirements** (`support.google.com/a/answer/81126`) — PRIMARY, effective
  2024-02-01. The 0.30%/0.10%/5,000-per-day figures, Google-primary and not extended to Yahoo,
  whose own page states no numeric threshold (`references/outbound-and-prospecting.md`). Re-read
  2026-10-17 (the URL now redirects to `support.google.com/mail/answer/81126`) for the one-click
  unsubscribe plus visible-link requirement on bulk marketing mail, cited beside the
  manufactured-reply-signal exhibit, never restated as consent doctrine.
- **Gong** (`gong.io/forecast/`) — VENDOR-SELF-REPORTED, method not disclosed. A customer quote
  claiming 95% forecast accuracy and a separate "20% more precision" claim, cited only with the
  method-absence statement attached (`references/forecasting-honesty.md` §3).
- **Aviso** — VENDOR-SELF-REPORTED marketing headline ("29 Quarters of Highly Accurate
  Forecasts"), no accuracy metric stated anywhere it appeared; no permalink was captured, treated
  as uncited (`references/forecasting-honesty.md` §3).
- **Clozd** (`clozd.com/blog/win-loss-101-what-to-ask-buyers-in-win-loss-interviews`) —
  VENDOR-SELF-REPORTED, one page from one vendor, checked once. The leading win/loss vendor's own
  buyer-interview guidance, scoped narrowly and never generalized to the industry
  (`references/win-loss-learning.md`).
- **RAIN Group** — the one real named study (489 sellers) behind the "8 touches to reach a
  prospect" figure, cited with its scope, never as a bare law (`SKILL.md`'s never-ship table).

## 5. Practitioner (X) sources

Every X permalink in this pack was copied verbatim from a research raw file, or — for the
2026-10 practitioner-craft additions below — re-fetched at the permalink and quoted from the fetched
text, and grade is stated inline at point of use (FOLKLORE / OPINION / FIRST-PERSON / FIGURE, single
company, etc.). None was reconstructed.

- **@patio11** — the predict-then-score loop (in advance, before the outcome is known) — the only
  calibration mechanism found on any surface, serving both forecasting honesty and win/loss.
- **@arvidkahl** — the skeptic-and-seller tension unique to founder-led sales; the complexity-moat
  erosion argument, with its own unrecovered falsification condition.
- **@KyleAsay_** — the three negative exit criteria (no velocity, no concerns, no next-best-option)
  as the inversion of a hand-set stage weight.
- **@thaAdamLittle** — the RepVue quota-attainment series (subject: share of reps at quota, always
  stated), and the positive model of naming a custom metric and labelling a shortcut "rough
  heuristic."
- **@BrianLaManna_** — the CRM-hygiene counter-exhibit, the "Unfortunately Nope" disqualification
  bucket, the forecast-date-as-leverage exhibit, and the pipeline-surplus discounting-discipline
  exhibit.
- **@dvassallo** — cited as a FOLKLORE specimen paired with his own reasoned rejection of the claim
  he repeats, not as a propagator of it.
- **@harsh_biz**, **@jeffreyhuber**, **@NickAbraham12**, **@seanlongden** — the "email is cooked"
  CONTESTED thesis, both poles permalinked.
- **@salesxsaas** — the standing, unanswered AI-SDR challenge, cited as an open bar nobody in this
  research met, never as proof AI-SDR doesn't work.
- **@Chris_Orlob**, **@meddpicc**, **@BowTiedSalesGuy** — the split-practitioner-opinion exhibits on
  MEDDPICC and named methodologies generally.
- **@FidelCacheFlow** — the credentials-as-evidence FOLKLORE specimen.
- **@levikmunneke**, **@gtmba_** — the outbound funnel-math and coverage-multiple folklore exhibits.
- **@Shpigford** — the gate eroding from below: build-it-yourself economics for engineer-buyers
  making the existence gate a moving target, not a fixed threshold (`when-sales-applies.md`).
- **@techsaleshackz** — the framework-discard exhibit; read as one discard anecdote, never
  generalized to "frameworks don't work" (`discovery-calls.md`).
- **@mistamor** — the hygiene-as-noise coaching exhibit: an AE coach classifying CRM hygiene as
  noise, not signal, in his own Performance Improvement Plan framework (`crm-and-pipeline.md`).
- **@alexabelonix** — the 4/50 founder micro-loop: a complete manual-outreach-to-ICP-revision cycle
  at n=1, honest about its own denominator (`surface-founder-led-solo.md`).
- **@webjuice_ie** — one of the three evasion exhibits: account farming behind proxies
  (`outbound-and-prospecting.md`).
- **@staticmaker1** — the funded-industry figure behind engagement-simulation warmup tooling
  (`outbound-and-prospecting.md`).
- **@iuditg** — the truncated Solution Selling specimen: a conversion-lift claim cut off mid-number
  in its own source, unquotable and unproven regardless of the missing digit
  (`objections-and-enablement.md`).

Added 2026-10 (outbound craft, timing signals, demo-first, agentic concealment; every quote
re-fetched 2026-10-17):

- **@NickAbraham12** (also above) — the low-commitment ask ("an ask they would feel silly saying no
  to") and the hiring-trigger opener; one agency's outbound-then-referrals sequence
  (`outbound-and-prospecting.md`, `icp-and-qualification.md`, `surface-founder-led-solo.md`).
- **@thejustinwelsh** — the recipient-side account of why one cold email got a reply.
- **@heyblake** — first line hand-written, no calendar link, an open-ended follow-up cadence cited as
  the counter-example to a written stop.
- **@AlfieJCarter** — the three mechanical pipeline flags (promotional post, VENDOR-SELF-REPORTED)
  (`crm-and-pipeline.md` §4).
- **@HamptonAc_** — a published agent-prompt article: the 1–10 lead-score cutoff, "like a human
  wrote it," the follow-up cap, and a denominator-shrinking conversion claim (`agentic.md`).
- **@everestchris6** — the build-before-contact pipeline, the plain-language sales brief, the
  owner-asking-for-help timing signal (`demo-and-narrative.md` §6).
- **@browomo** — a second-hand orchestrator prompt whose checker screens for "absence of AI markers"
  and whose escalation triggers live in its own prompt (`agentic.md`).
- **@scaling_shields** — two "met a guy" funnels whose arithmetic reconciles and whose provenance
  does not; the stated-need and competitor-review timing signals.
- **@dimitarangg** — the concealed-source opener, cited as what the visibility test rejects.
- **@GeorgeJeffersn** — the deliberate-mistake pretext, cited as the same.
- **@coldemailchris** — the reply-keyword opt-out sold as a way to trick the spam filter (the fourth
  evasion exhibit), per-mailbox-provider reply reading, model-scored reply triage.
- **@axtalks** — the first-person list-before-copy diagnosis.
- **@cyrilXBT** — a funnel stated in the future tense.
- **@omoalhajaabiola**, **@SahilBloom** — the manual prebuilt-proof and mock-up-in-the-email advice.
- **@NickSpisak_**, **@BrettFromDJ** — outcome-not-technology positioning and the false "AI made
  this" claim, both cited to bound what the disclosure rule is not.
- **@lukepierceops** — "Can you give me an example of that?" as a discovery-call mechanic
  (`discovery-calls.md` §4).

## 6. Figures this pack refuses to ship

The full never-ship table, with the mechanism taught in place of each figure, is in
`skills/sales/SKILL.md`'s "Never-ship figures" section and `research/synthesis.md` §3. The standing
rules matter more than the list:

- The never-ship list is not the rule — judge the **figure class**. Sales strips split three ways:
  survives-at-origin-but-mutates (57% and its cousins), pure folklore with no defensible version
  (92% give-up rate, BANT's IBM origin, "always be closing"), and vendor-research genre with a real N
  and an undisclosed method (Gong Labs, RAIN's 8-touches, HubSpot's 21%).
- **A disclaimed figure is still a figure.** KBCM/KeyBanc ships nowhere in this pack — the subject
  was verified once, the value never was.
- **A win rate without its denominator is not a number.** Coverage is 1/win-rate, derived, never a
  portable constant.
- Verify the **subject** of a metric before repeating it — three different subjects circulate behind
  a bare "70%" in this corpus alone.

## 7. What this pack claims for itself

Constructed here, not lifted from any source:

- **The forecast-accuracy null, stated as a four-leg finding with a fifth practitioner check** — no
  single source in the corpus states this; each leg is independently sourced and the synthesis is
  this pack's.
- **The predict-then-score loop as a shared mechanism across forecasting and win/loss** — patio11's
  primitive answers both jobs; treating it as one through-line rather than two separate tips is this
  pack's integration.
- **The three-way strip taxonomy** (survives-at-origin / pure-folklore / vendor-research-genre) —
  the sales corpus splits differently from every sibling pack's strip set, and teaching the split
  itself, rather than debunking figures one at a time, is this pack's construction.
- **The existence gate as four incompatible practitioner positions taught as disagreement** — no
  source in the canon resolves which gate governs; naming the disagreement instead of picking a
  winner is this pack's answer.
- **The seam rulings in `references/handoff.md`** — mirroring three siblings' pre-drawn rows exactly,
  and flagging `product`'s and `automation`'s prose-only silence as deliberate rather than an
  oversight, is this pack's synthesis of sibling files none of which mention `sales` by name in a
  handoff row.

## 8. What this pack did not do

- It did not measure anything itself. Every figure is someone else's, graded.
- It did not resolve the sales↔success expansion-sale seam — both positions ship, contested, per
  synthesis §5 and `references/handoff.md`.
- It did not validate any named qualification framework or selling method against an outcome,
  because no source anywhere in the corpus does either — that null is the finding, stated plainly
  rather than papered over with doctrine.
- It did not audit any AI-SDR vendor's ARR, retention, or performance claims independently — every
  such figure ships VENDOR-SELF-REPORTED, with its contested counter-figure attached where one
  exists.
- Several corpus items remain unread and are listed honestly in `research/synthesis.md` §8.
