# D3 — Sales Forecasting & Pipeline Evidence (channel D, worker 3)

Scope: FLAGSHIP CANDIDATE. Central question — "what can a pipeline number honestly predict?"
Grading scheme used throughout: PRIMARY / SECONDARY / VENDOR-SELF-REPORTED / FOLKLORE / CONTESTED /
PRACTITIONER-OPINION (uncited).

Tooling note for reproducibility: WebSearch was dead for the whole session (200/200 quota exhausted by
other channels before I started). DuckDuckGo Lite/HTML, Bing, and Marginalia were all effectively
unusable (captcha/JS/empty). What worked: WebFetch directly against known documentation sites; the
GitLab handbook's public GitLab.com repo + API (`gitlab.com/api/v4/projects/.../repository/tree` and
`.../files/.../raw`) to walk the actual handbook source tree; Semantic Scholar's public search API
(heavily rate-limited, needed long backoff, eventually replaced with OpenAlex which did not rate-limit);
Crossref for DOI metadata; and `curl -sL -o p.pdf URL && pdftotext p.pdf p.txt` for two open-access PDFs,
which is how the verbatim academic quotes below were obtained with real page context. RepVue, Pavilion/
Benchmarkit, and Salesforce's State-of-Sales page are all bot-protected or JS-rendered and could **not**
be verified via fetch in this pass — flagged explicitly below rather than guessed.

---

## 1. Published forecast methods (real category definitions, permalinks)

### GitLab handbook — NULL RESULT on forecast-category percentages (stage definitions only)

GitLab's public handbook does publish a detailed, named sales **opportunity-stage** process, but I could
**not** find a public forecast-category (Commit/Best Case/Pipeline/Omitted, or equivalent) definition
with probability percentages anywhere in the public handbook source tree.

- Verified page: `https://handbook.gitlab.com/handbook/sales/commercial/comm-sales-opp-stages/`
  (source: `content/handbook/sales/commercial/comm-sales-opp-stages/_index.md` in
  `gitlab.com/gitlab-com/content-sites/handbook`, fetched via the public GitLab repository-files API).
  It defines nine stages — **0-Pending Acceptance, 1-Discovery, 2-Scoping, 3-Technical Evaluation,
  4-Proposal, 5-Negotiating, 6-Awaiting Signature, 7-Closing, Closed Won, 8-Closed Lost** — each with
  primary/secondary activities and exit criteria (MEDDPPICC qualification, multi-threading,
  documentation). Opening line of the page: *"Pipeline management is key to predictable, scalable
  revenue attainment."*
- I fetched the raw markdown of that page directly (not just the summarized rendering) and grepped it
  for "percent", "%", "probability", "forecast category", "commit", "best case", "omitted", "pipeline
  weight" — **zero occurrences of any of these terms.** The stage table has no probability column.
- I also walked the GitLab handbook's sales directory tree via the public API (`sales/revenue-analytics`,
  `sales/commercial`, `sales/field-operations/sales-strategy`, `sales/field-operations/sales-operations`,
  `sales/process`, `sales/sales-operating-procedures`) looking for a dedicated "forecasting" page. None
  exists as a distinct handbook page; forecasting is referenced only in passing (e.g. Revenue Analytics'
  "Pipeline Analytics — monitoring leading revenue indicators", Renewal Operations "providing forecast
  clarity"), never with a category/percentage table.
- **Conclusion: GitLab publishes its opportunity STAGE process publicly (citable, PRIMARY, permalink
  above) but does not publish its forecast-category percentage weights publicly** — those most likely
  live in internal Clari/SFDC configuration, not the open handbook. Cite the stage process; do not
  attribute a Commit/Best-Case percentage table to GitLab — none was found. This null result stands
  unless someone finds a page this pass missed.

### HubSpot — real, hand-verified category definitions (PRIMARY, official docs)

Fetched and independently re-verified against raw HTML (not just the summarized extraction) at
`https://knowledge.hubspot.com/forecast/set-up-the-forecast-tool`. Exact verbatim text from the page:

> "Not forecasted: deals that are in the pipeline for the current time period, but are not included in
> the forecast. Pipeline: deals that have a low likelihood of closing. Best case: deals that will close
> in the best case scenario, which have a moderate likelihood of closing. Commit: deals that have a high
> likelihood of closing and have been committed to the forecast. Closed won: deals that have closed
> within the forecasted time period."

Five categories total: **Not forecasted / Pipeline / Best case / Commit / Closed won** — note this is
HubSpot's own label set, not "Omitted" (that word appears in third-party SEO content describing
Salesforce's categories, see below, and should not be attributed to HubSpot).

Deal-amount calculation, also verbatim from the same page:

> "Weighted amount: the Amount multiplied by the Deal probability." / "Total amount: the full deal
> amount."

This confirms HubSpot's forecast tool is architecturally a **stage-weighted pipeline calculator** —
amount × probability — with the four open categories layered on top as a qualitative sort, not a
separate calibrated model. Grade: PRIMARY (official product documentation), but note it documents the
*mechanism*, not any accuracy/calibration claim — HubSpot makes no accuracy claim on this page.

### Salesforce forecast categories — NOT INDEPENDENTLY VERIFIED, flag only

The commonly cited "Pipeline / Best Case / Commit / Closed / Omitted" five-category framing that
appears across many SEO content-marketing sites (resources.rework.com, forecastio.ai, orm-tech.com,
crmnewstoday.com) is attributed to Salesforce's native forecast-category field, but I did **not**
independently fetch a Salesforce primary-documentation page confirming this wording in this pass — the
Salesforce help/docs pages I tried were either 403'd or JS-rendered with no static content. **Do not
cite "Salesforce's forecast categories are X" without a direct fetch of help.salesforce.com or
developer docs; treat as SECONDARY/unverified pending that fetch.**

---

## 2. The weighted-pipeline critique + backtest hunt

### Core finding, stated plainly: nobody publishes a backtest calibrating stage-weight percentages against actual close outcomes.

**Search paths tried:** GitLab handbook source tree (no percentages published at all, see §1); Semantic
Scholar / OpenAlex academic search (returned judgmental-forecasting-bias literature, see §4, but no paper
calibrating CRM stage-probability fields against realized win rates); direct fetch of Clari, Aviso,
BoostUp/Terret, Mediafly marketing pages (see §3 — all assert accuracy, none publish a stage-weight
calibration table or backtest); direct fetch of practitioner blog posts specifically arguing the weighted-
pipeline critique (below) — none of them cite a backtest either, they argue from first principles or
anecdote. I could not find, through any available route, a published study that took a company's (or an
industry's) actual stage-entry-to-close conversion data and validated hand-set stage percentages against
it. **This absence is the headline finding for this section** — the literature that exists argues stage
weights are *assumed*, and simultaneously nobody supplies the calibration study that would settle it.

### The critique itself, from a named practitioner (PRACTITIONER-OPINION, uncited)

Don Otvos ("almost 20 years in Sales and Sales Operations," described as a Sales Ops leader associated
with Datahug), LinkedIn Pulse, "The Weighted Pipeline is Killing Your Forecast Accuracy"
(`https://www.linkedin.com/pulse/weighted-pipeline-killing-your-forecast-accuracy-don-otvos`):

> "assuming that all deals have the same probability to close at the same stage neglects to account for
> huge amounts of data."

And directly on the small-numbers problem this pack needs (verbatim, quoted via fetch):

> "the number of deals that would need to be included in a calculation of this type for the result to be
> statistically sound is far greater than that which is in almost any company's pipeline."

This is exactly the small-deal-count critique the brief asked for, from a named industry practitioner —
but it is an uncited blog opinion, not a study. Grade: PRACTITIONER-OPINION, no citation to underlying
data.

A second practitioner source, ORM (`https://orm-tech.com/blog/weighted-pipeline`), makes the "understates
risk twice" argument:

> "Stage-weighted pipeline understates risk twice. The value is too high, and the probability is too
> confident about deals that have stopped moving."

with supporting anecdotes ("Pipeline routinely carries an average deal size well above what actually
closes. I see pipelines with an $80,000 average deal size while closed-won deals average $40,000")
presented in first person, **no citation, no study** — explicitly vendor/practitioner content marketing.
This source does **not** address the small-deal-count problem at all (checked directly).

A third source (`https://prospeo.io/s/pipeline-value`) states the calibration fix that would be needed but
that nobody appears to have published: "The right way to set stage probabilities is to go into your CRM
history and calculate the actual close rate for every deal that ever reached each stage" — i.e., the
correct method is descriptively simple (empirical Bayes on your own historical stage-entry-to-close data)
but the same sources uniformly report that **most teams never do this** — "Most teams never calibrate
stage probabilities from actual close data, picking round numbers that feel right — 20%, 50%, 80% — and
never revisiting them." All of this is vendor content-marketing (forecastio.ai, prospeo.io), grade
VENDOR-SELF-REPORTED/uncited, but consistent across independent vendor sources, which is at least weak
convergent signal that the "made-up, never recalibrated" critique is a genuine practitioner consensus even
without a formal study behind it.

### CSO Insights "74%/50%/75%" figure — appears repeatedly, uncited, could not trace to primary

Multiple secondary sources (forecastio.ai synthesis; Don Otvos's LinkedIn post, which cites "CSO Insights
research showing forecasts achieve more than 75% accuracy rarely and in the ballpark of 50% frequently")
attribute a forecast-accuracy statistic to "CSO Insights." I attempted to trace this to a primary CSO
Insights report and could not — CSO Insights was absorbed into Miller Heiman Group and later Korn Ferry
during the relevant period, and no primary report page was reachable via the tools available this pass
(search engines dead, no working direct URL found). **Grade: FOLKLORE / could not verify.** Do not cite a
specific CSO Insights percentage without a primary report in hand.

---

## 3. Forecast-accuracy claims table (vendor + analyst)

| Source | Claim | Method disclosed? | Grade |
|---|---|---|---|
| Clari | `clari.com/blog/forecast-accuracy/` and `clari.com/platform/forecasting/` both 404'd/returned no accuracy percentage on this pass — could not locate a live accuracy-claim page. | N/A — page not found | COULD NOT VERIFY |
| Gong Forecast | "Our forecast accuracy has grown to the point that we're at 95%" — customer quote (Drew Korab, Director of RevOps, Upwork), on `gong.io/forecast/`. Also: "Gong leverages 300+ unique signals to predict deal outcomes with 20% more precision than algorithms based on CRM data." | **No.** For the 95% figure: no measurement period, no baseline, no validation method stated. For the "20% more precision" figure: "precision" is undefined, no comparison baseline named beyond "algorithms based on CRM data," no sample size, no horizon. | VENDOR-SELF-REPORTED, method NOT disclosed |
| Aviso | "RingCentral gets 29 Quarters of Highly Accurate Forecasts" (resource-center headline) | **No.** No accuracy metric, no baseline, no methodology in the fetched page; only a case-study teaser link. | VENDOR-SELF-REPORTED, method NOT disclosed |
| BoostUp.ai | **Notable finding: `boostup.ai` now 301-redirects to `terret.ai`** — the company appears to have rebranded/pivoted (login endpoint still shows `app.boostup.ai/login`). Terret's homepage makes no forecast-accuracy percentage claim; markets "Terret Forecast" as a "machine forecast" product with no disclosed accuracy figure. | N/A — no percentage claim found on current site | VENDOR-SELF-REPORTED (no live accuracy claim to grade) |
| Mediafly (formerly InsightSquared) | `mediafly.com` homepage shows unrelated case-study metrics ("90% adoption... Sealed Air," "8% to 55% win rate increase... Databricks," etc.) — none of these are forecast-accuracy figures. No forecasting-specific accuracy claim was found on the pages fetched this pass. | N/A | COULD NOT VERIFY (may exist on a page not fetched) |
| CSO Insights (via secondary citation) | "74% of sales organizations rely on weighted pipeline forecasting, but fewer than 50% of those teams achieve forecast accuracy higher than 75%" (as repeated by forecastio.ai and Don Otvos's blog, not independently located at a CSO Insights primary) | No — not traced to primary in this pass | FOLKLORE / could not verify |
| "Less than half of forecasted deals close" / "forecast accuracy is under 50%" (widely repeated framing) | Commonly repeated across sales-tech blog content | Not traced to any primary in this pass; search tooling (WebSearch dead, DDG/Bing/Marginalia all blocked or empty) could not locate an original source | FOLKLORE |

**Pattern across every vendor checked (Clari, Gong, Aviso, BoostUp/Terret, Mediafly): none disclose what
"accuracy" is measured against (closed-won dollars? deal count? which forecast category?), over what
horizon (weekly snapshot vs. quarter-close), or on whose data (their own customer base, and how many
customers/deals). This absence of method disclosure is itself the finding — it is uniform across the
category, not an artifact of which vendor pages happened to be reachable.**

---

## 4. Academic judgmental-forecasting evidence (the strongest evidence base available to this pack)

All items below have real DOIs, obtained via OpenAlex/Semantic Scholar/Crossref and (for the two starred
items) verified by downloading the actual open-access PDF and reading it directly with `pdftotext`.

### ★ Lawrence, Goodwin, O'Connor & Önkal (2006), "Judgmental forecasting: A review of progress over the
   last 25 years," *International Journal of Forecasting* 22(3), 493–518.
   DOI: `10.1016/j.ijforecast.2006.03.007`. Open-access PDF (Bilkent University repository, downloaded and
   read directly): `https://repository.bilkent.edu.tr/bitstreams/0dd7098f-7171-4819-a8bb-6325ef8a8929/download`.
   537 citations (OpenAlex). This is **the** canonical review the brief named (Lawrence/Goodwin/O'Connor/
   Önkal — not Fildes as first author, but Fildes appears throughout the reference list and in related
   co-authored work below).

   - Has a dedicated §3.3 "Sales forecasting" section, directly on-topic. Key finding, verbatim: when
     domain-knowledge-laden forecasts were studied across 13 organizations (Lawrence et al. 2000), "these
     forecasts were the outcome of organisational budgeting and incentive issues, which tended to bias
     the forecasts; e.g. **if the forecast was used as a target to be achieved, the forecasts tended to
     be below the actual**. When this organisational bias was (statistically) removed from the forecast,
     they tended to be significantly and substantially more accurate than the naïve benchmark."
   - The single best quote in the whole file for teaching "a forecast that hits its target isn't
     necessarily an honest forecast" (sandbagging/gaming), verbatim: *"In the course of one such meeting
     ... substantial marketing expenses were committed to arrest declining sales with the comment that
     sales needed to reach a certain level. In another case, sales levels were manipulated by promotional
     spending to ensure that sales targets were met. **One major multi-national commented that they
     always ensure that sales are within 0.5% of the forecast — they made sure it happened that way!**"*
     Immediately followed by an explicit **null-result admission from the review's own authors**: *"To
     our knowledge, this aspect of the sales forecasting process has been largely ignored by
     researchers."* — i.e., the peer-reviewed literature itself flags that gaming/self-fulfilling-forecast
     behavior is under-studied.
   - Real, citable **definition of calibration** for the pack to use as the honest alternative to a point
     forecast, verbatim: *"calibration (a measure of the correspondence of forecast probabilities with the
     realized proportion of correct predictions or with the relative frequencies of occurrence of the
     predicted event, depending on the task structure used) and over/underconfidence (an index of the
     provider's probability assessments exceeding or falling short of the attained proportion correct for
     the corresponding events)."*
   - Overconfidence is reported as domain-dependent, not universal: well-calibrated groups include
     "weather forecasters' probability of precipitation forecasts," "experienced bridge players'
     probability forecasts of making the contracts that they had bid"; poorly-calibrated/overconfident
     groups include "professional economic forecasters' future recession predictions," "sports experts'
     forecasts," "Russian managers' economic forecasts," "election results," "starting salaries and job
     offers." Sales forecasting specifically is not in either named list in this section — the
     overconfidence evidence base for sales-specific probability judgments is thinner than for point
     sales forecasts (§3.3), which is itself worth noting as a gap.
   - Also documents that forecast errors from judgmental adjustment of statistical forecasts can be
     hugely value-additive or destructive depending on practice quality: citing Fildes et al. 2006 (see
     next entry's context), "forecast errors increased from 10% to 33 percentage points through
     adjustment in some situations, while in others there were improvements of a similar magnitude" —
     i.e., judgment is not uniformly good or bad, execution quality is what varies.

### ★ Fildes & Goodwin (2007), "Against Your Better Judgment? How Organizations Can Improve Their Use of
   Management Judgment in Forecasting," *Interfaces* (now *INFORMS Journal on Applied Analytics*) 37(6),
   570–576. DOI: `10.1287/inte.1070.0309`. This is the Fildes/Goodwin paper the brief specifically
   flagged. Open-access working-paper version (Lancaster University eprints, downloaded and read
   directly): `https://eprints.lancs.ac.uk/id/eprint/48879/1/Document.pdf` (note: this is the 2007 LUMS
   working-paper preprint, not necessarily byte-identical to the published Interfaces version — content
   and survey numbers below are from the preprint I actually read).

   - Method, verbatim: *"We conducted a survey of 120 forecasters to investigate whether their forecasting
     procedures were consistent with the [11] principles. In addition, we conducted four in-depth case
     studies."* Respondents: "115 forecasters attending four international forecasting practitioner
     conferences in the United States" plus 5 more from case-study companies. Median forecast scope: 350
     different items per forecaster. This is a genuinely disclosed, citable method — sample size, sample
     composition, and recruitment are all stated.
   - Directly relevant, damning finding on whether practitioners even track their own accuracy, verbatim:
     asked *"Do you ever review the extent to which judgmental adjustments [to statistical forecasts]
     improve the accuracy of your forecasts?"* — **"Only 52.8% of respondents said they did."** And on
     error measurement generally: **"Only 27.5% of respondents reported using multiple error measures...
     and 25% did not indicate that they used any error measure at all."** One case-organization's own
     software "produced forecasts less accurate than the random walk, yet the result was unknown to the
     company forecasters." This is strong, citable evidence that even professional, resourced forecasting
     operations frequently do not close the loop on their own accuracy — directly useful for a pack
     arguing that solo-founder pipeline math is not uniquely unrigorous.
   - The 11 "Principles of Forecasting" tested trace to Armstrong (2001) / Armstrong & Pagell (2003), *The
     Principles of Forecasting Handbook* — cited but not independently re-verified in this pass; flag as
     a further-reading pointer, not independently confirmed content.
   - Also cites, in-text (not independently verified by me — one level removed): Fildes et al. 2006 found
     that judgmental adjustment of statistical sales forecasts "increased [errors] from 10% to 33
     percentage points... in some situations, while in others there were improvements of similar
     magnitude" across four companies studied in detail — i.e. adjustment quality is highly variable, not
     reliably good or bad.

### Bonney, Plouffe & Hochstein (2020), "Examining salesperson versus sales manager evaluation of customer
   opportunities: A psychological momentum perspective on optimism, confidence, and overconfidence,"
   *Industrial Marketing Management* 91, 279–293. DOI: `10.1016/j.indmarman.2020.05.012`. 19 citations
   (OpenAlex). Abstract obtained directly from Semantic Scholar (not independently PDF-verified — no
   open-access PDF located this pass), verbatim opening: *"Making correct decisions regarding the merit of
   sales opportunities, as well as deciding which opportunities to pursue and which to abandon, is one of
   the most critical tasks sales managers and salespeople grapple with... Assessments of future sales,
   however, are often inaccurate and little is known about how salespeople and sales managers make
   decisions about sales opportunities, or if they differ in their ability to (correctly) assess the
   merits of such opportunities."* Directly on-topic (rep vs. manager opportunity assessment,
   overconfidence) but I only have the abstract, not the findings/results section — grade as PRIMARY
   (peer-reviewed), abstract-only verified.

### McCarthy Byrne, Moon & Mentzer (2010/2011), "Motivating the industrial sales force in the sales
   forecasting process," *Industrial Marketing Management* 40(1), 128–133. DOI:
   `10.1016/j.indmarman.2010.06.003`. 29 citations. Title-only verified (Crossref/OpenAlex returned no
   abstract text) — directly on-topic by title (sales-force incentive/motivation as a driver of forecast
   distortion) but content not independently confirmed beyond the title in this pass.

### Mantrala & Raman (1990), "Analysis of a sales force incentive plan for accurate sales forecasting and
   performance," *International Journal of Research in Marketing* 7(2–3), 189–202. DOI:
   `10.1016/0167-8116(90)90021-E`. 48 citations. The earliest citable academic treatment found of the
   incentive-design ↔ forecast-accuracy link (i.e., a formal analysis of why sales-force forecasts are
   structurally biased by the incentive plan attached to them — the root of "sandbagging"). Title-only
   verified; no abstract text available via Crossref/OpenAlex in this pass.

### Hoyle, Dingus & Wilson (2020), "An exploration of sales forecasting: sales manager and salesperson
   perspectives," *Journal of Marketing Analytics* 8, 155–167. DOI: `10.1057/s41270-020-00082-8`. 15
   citations. Directly on-topic by title (practitioner-perspective study of sales forecasting from both
   manager and rep viewpoints); title-only verified, no abstract text available in this pass.

### Eitle & Buxmann (2019), "Business Analytics for Sales Pipeline Management in the Software Industry: A
   Machine Learning Perspective," *Proceedings of the 52nd Hawaii International Conference on System
   Sciences (HICSS)*. DOI: `10.24251/hicss.2019.125`. 22 citations. Reconstructed abstract (OpenAlex,
   abstract_inverted_index): uses actual CRM data from a software company to build ML models (CatBoost,
   Random Forest outperformed SVM/XGBoost/Decision Trees) across the sales pipeline stages; explicit
   finding, paraphrased from the reconstructed abstract: *"the probability of either winning or losing a
   deal in [the] early stage is more difficult to predict than analyzing lead phases separately."* This is
   a genuine empirical (ML, not judgmental) forecasting study using real software-industry pipeline data —
   useful as a contrast case (a data-driven alternative to hand-set stage weights), though it is a
   conference paper, not journal-refereed to the same standard.

### Fildes & Goodwin (2011), "Optimism bias and differential information use in supply chain forecasting,"
   found via search but not pursued further — no DOI resolved in the Semantic Scholar record (listed as
   DOI: None), 1 citation, and it is supply-chain- rather than sales-specific. Noted for completeness, not
   used as a citable source.

**Assessment of this literature for the pack's purposes:** the judgmental-forecasting literature
(Lawrence/Goodwin/O'Connor/Önkal 2006; Fildes/Goodwin 2007) is genuinely strong, peer-reviewed, and
directly on-topic — it is the best evidence base found in this entire research pass, exactly as the brief
predicted. Its two load-bearing, hand-verified findings for the pack are: (1) forecasts used as *targets*
get gamed toward the target (sandbagging/overshoot-to-target is a documented, quoted phenomenon, not
folklore), and (2) even professional, resourced forecasting operations frequently fail to track or
validate their own forecast accuracy (52.8% do review it, meaning **47.2% of surveyed professional
forecasters do not**; 25% use no error measure of any kind). Both are stronger, more honest teaching hooks
than any vendor accuracy percentage in §3.

---

## 5. Benchmark-source grading table

| Source | What it publishes | Sample / method | Grade |
|---|---|---|---|
| KBCM (KeyBanc Capital Markets / Sapphire Ventures private-SaaS survey) | Quota-attainment trend | See §8 below — reused from sibling corpus, subject is **sales AE quota attainment**, not CS/CSM. Primary permalink **not captured** by the sibling corpus either; treat as SECONDARY at best pending someone locating the actual survey page/PDF. | SECONDARY (unresolved permalink) |
| Bridge Group | Named, recurring survey report — confirmed live: "2026 AE Research Report" (described on-page as its 10th edition), plus a separate SDR report. Fetched `bridgegroupinc.com` homepage directly (curl, 200 OK) and confirmed the report exists and is a long-running (10th-edition) survey series — "19 Years of Published Research," built from work with "500+ B2B organizations" per the homepage's own framing. | Could **not** locate the methodology section (sample size, recruitment, self-report vs. verified) on the pages fetched this pass — the report itself is gated. | COULD NOT VERIFY METHOD (existence and longevity confirmed; sample method not confirmed) |
| Pavilion / Benchmarkit | SaaS compensation/performance benchmark reports | `pavilion.com/benchmarkit` and `benchmarkit.ai/2024-saas-benchmarks-report` both failed to return usable static content (JS redirect / 404) in this pass. | COULD NOT VERIFY (blocked) |
| RepVue | Self-reported rep-submitted comp/quota-attainment data tied (per RepVue's own public positioning, not independently confirmed here) to LinkedIn-verified employment | `repvue.com/about` and the RepVue homepage both returned Cloudflare bot-challenge pages (HTTP 429/"We're verifying your browser") to every fetch attempt (WebFetch and curl, multiple UAs) — **could not independently confirm RepVue's stated verification method in this pass.** Do not cite specific RepVue numbers or verification claims without a successful fetch. | COULD NOT VERIFY (Cloudflare-blocked) — self-reported-data bias risk should be assumed generically for any self-submission platform regardless |
| Salesforce "State of Sales" | Survey of sales leaders/reps | `salesforce.com/resources/research-reports/state-of-sales/` returned a 200 but the page is JS-rendered — no methodology text (sample size, surveyed titles, vendor) was present in the fetched HTML. | COULD NOT VERIFY (JS-rendered, static fetch insufficient) |

**Pattern:** of five benchmark ecosystems named in the brief, only one (Bridge Group) could be confirmed
as a real, long-running, named report at all in this pass, and even that one's sample method is unverified.
The other four (Pavilion/Benchmarkit, RepVue, Salesforce State of Sales, and KBCM's own primary page) were
all either bot-blocked, JS-rendered, or — in KBCM's case — already flagged as permalink-less by the
sibling corpus. **This is itself a finding: the SaaS benchmark-report ecosystem is, in practice, hard to
audit even when you try** — reports are frequently gated behind lead-forms, rendered client-side, or
sit behind bot protection, which is a structurally different situation from the peer-reviewed academic
literature in §4, where DOIs and open-access mirrors made verification straightforward. The pack can
honestly teach this asymmetry: "the number you can verify is not always the one that's easiest to find."

---

## 6. Small-numbers honesty + calibration alternatives

This is the strongest available teaching material for what the brief calls "likely where the pack's
distinctive teaching lives."

- **Brier score — real, hand-verified definition and formula**, Wikipedia (`en.wikipedia.org/wiki/Brier_score`,
  fetched directly): formula BS = (1/N)·Σ(f_t − o_t)², where f_t is the forecast probability and o_t is
  the realized outcome (0 or 1). *"The lower the Brier score is for a set of predictions, the better the
  predictions are calibrated."* Range 0 (perfect) to 1 (worst) in this formulation (Good Judgment Open's
  own explainer, see below, uses a 0–2 range for a slightly different multi-option formulation — note the
  scale differs by convention, don't conflate the two without checking which formulation a source uses).
- **The single most load-bearing quote for the small-numbers argument, verbatim from Wikipedia's Brier
  score article**: *"Quite large sample sizes, i.e. n > 1000, are required for higher-skill forecasts of
  relatively rare events, whereas only quite modest sample sizes are needed for low-skill forecasts of
  common events."* This is a general statistical-forecasting-verification fact (not sales-specific) but it
  is exactly the honest technical grounding for "you cannot validate a calibration claim on 5 open deals" —
  a solo founder's pipeline is nowhere near n>1000, and even "modest" sample sizes for low-skill/common
  events are unlikely to be met by 5–20 open opportunities. This directly underwrites a pack rule: **a
  single deal's "60% probability" is not falsifiable and cannot be validated on n=1 or n=5; only a large
  number of same-type deals scored the same way, tracked over time, produces a checkable calibration
  curve.**
- **Good Judgment Open's own Brier-score explainer** (`gjopen.com/faq`, fetched directly), the practical
  worked-example version of the same idea, verbatim: *"The Brier score is the squared error of a
  probabilistic forecast... For each answer option, we take the difference between your forecast and the
  correct answer, square the differences, and add them all together."* With the worked example: a 70%
  forecast on a yes/no question that resolves YES scores (1–0.7)² + (0–0.3)² = 0.18. Individual scores are
  **averaged across the question's lifespan and across many questions** to produce a meaningful reported
  score — reinforcing that a single scored event tells you almost nothing; calibration is a property of a
  *track record*, not of any one forecast. This is a clean, citable, non-sales-specific source the pack can
  use to teach the honest alternative: publish your own historical stage-to-close conversion rate as a
  track record over many deals, rather than asserting a single deal's probability as if it were
  independently falsifiable.
- **Calibration, defined by the peer-reviewed literature** (Lawrence et al. 2006, quoted in full in §4):
  "a measure of the correspondence of forecast probabilities with the realized proportion of correct
  predictions or with the relative frequencies of occurrence of the predicted event" — this is the
  academically precise version of the same Brier-score idea and can be cross-referenced with the Wikipedia/
  Good Judgment Open sources above for a three-way convergent definition (academic review, Wikipedia,
  live forecasting-tournament platform) — strong grounds for the pack to state this as settled technical
  vocabulary, not a contested claim.
- I did not find (and did not have search-engine access to hunt further for) a sales-specific
  calibration-curve publication, i.e. nobody publishing "here is our stage-3 probability plotted against
  our actual stage-3 close rate over N deals." This null result is consistent with, and reinforces, the
  §2 finding that no stage-weight backtest could be located anywhere.

---

## 7. Pipeline coverage ratio ("3x pipeline coverage") — verdict: tautology restated as a rule

Fetched `https://prospeo.io/s/pipeline-value` directly. It states the underlying math explicitly:

> "coverage needed = 1 / win rate"

with a worked table (win rate → minimum coverage): Enterprise 20–25% win rate → 4x–5x coverage;
Mid-market 25–35% → 3x–4x; SMB 30–40% → 2.5x–3x. And, verbatim: *"A team with a 25% win rate needs 4x
coverage. A team closing 35% needs roughly 3x."*

**Verdict: the "3x pipeline coverage" rule is not an independently-discovered empirical benchmark — it is
the reciprocal of an assumed win rate, presented as a rule of thumb.** If your win rate is exactly 33%,
you need exactly 3x coverage by definition (1/0.33 ≈ 3), not because some study found "3x" to be a magic
number. The "3x" figure that circulates as received wisdom is simply what falls out of assuming a ~30–35%
win rate, which happens to be a common (but not universal, per the same source's own table — enterprise
motions need 4–5x, SMB motions need 2.5–3x) mid-market SaaS win rate. **This is a tautology, not a
finding**, and the pack should teach it as such: derive your own coverage ratio from your own win rate
(coverage = 1/win rate), never adopt "3x" as a portable constant. I could not find an independent academic
or analyst-firm study establishing "3x" as an empirically-discovered threshold distinct from this
arithmetic identity — every source I found (vendor content-marketing) presents it via the same 1/win-rate
derivation, which is itself the answer: there is no separate "3x" finding to trace, because the ratio is
definitionally downstream of win rate.

---

## 8. KBCM reuse note (per instructions — read from sibling corpus, not re-researched)

Per instructions, this figure was already primary-verified (or rather, primary-*checked-and-rejected* — see
below) in the `success-skill` sibling corpus. I did **not** re-research it; I read and report exactly what
that corpus recorded, from two files:
`/Users/tamas/Documents/Personal/Projects/success-skill/research/web-research-report.md` (line ~533) and
`/Users/tamas/Documents/Personal/Projects/success-skill/research/_raw/_raw-web-lead-btyd-followups.md`
(§3.5).

- **Subject**: the sibling channel (channel A) originally flagged a figure as "**KBCM CSM quota attainment
  55–65%**" (a Customer-Success-Manager quota figure). On investigation, **that CSM-specific figure could
  not be confirmed anywhere in KBCM materials.**
- **What the KeyBanc/Sapphire survey actually reports** (per the sibling corpus's direct quote): *"quota
  attainment expectations also having expanded from ~70% to ~75%"* — this is explicitly **sales (AE)
  quota attainment**, not a CSM figure.
- **Sample / survey**: described as the "KeyBanc/Sapphire private-SaaS survey" (KeyBanc Capital Markets ×
  Sapphire Ventures). **Year**: the sibling corpus references "the 2024 survey landing page" as one of the
  materials searched, implying a 2024 vintage, but does not state definitively that ~70%→75% is the 2024
  figure specifically — treat the year as *likely 2024, not confirmed*.
- **Link**: **the sibling corpus does not record a specific permalink** to the KBCM/Sapphire primary page
  or PDF containing this figure — it lists the *materials searched* (Sapphire Ventures press page,
  PRNewswire, KeyBanc investor-relations releases, "the 2024 survey landing page," SaaSletter's benchmark
  writeup) but no single URL is captured as the source of the exact quote. I did not attempt to
  independently re-locate this permalink myself (out of scope per instructions — "do not re-derive this").
  **This pack should treat the ~70%→75% AE quota-attainment figure as SECONDARY at best until someone
  obtains the actual KBCM/Sapphire report PDF and records its permalink.**
- **Disposition inherited verbatim from the sibling corpus**: *"do not cite 'KBCM CSM quota attainment
  55–65%.' Either it is a different source, a different year, or — most likely — a conflation of a
  sales-quota figure with a CS context."*
- **Lesson applied**: this is the sibling build's own stated lesson ("verify the SUBJECT of every metric
  from its local context") — for this pack's purposes, the usable, subject-correct fact is: **AE (sales
  rep) quota attainment, per one industry survey, is reported to have moved from roughly 70% to roughly
  75%** — cite it as a directionally-suggestive SECONDARY figure with an unresolved permalink, never as a
  CSM/CS figure, and flag the missing permalink to whoever finalizes citations for this pack.

---

## 9. NULL RESULTS (explicit, for the record)

1. **No published backtest or calibration study of stage-weighted pipeline probabilities was found
   anywhere** — not in the GitLab handbook, not from any of the five forecasting vendors checked, not in
   the academic literature search (which surfaces judgmental-forecasting bias broadly but not a sales-
   CRM-stage-percentage calibration study specifically). Routes tried: GitLab handbook source tree walk;
   Semantic Scholar + OpenAlex academic search (multiple query variants); direct fetch of Clari, Aviso,
   BoostUp/Terret, Mediafly, Gong marketing/resource pages; direct fetch of three independent practitioner
   critique articles. This is stated as the headline result of §2, not a side note.
2. **GitLab's public handbook does not publish forecast-category percentage weights**, despite publishing
   a detailed nine-stage opportunity process. Verified by grepping the raw markdown source directly for
   probability-related terms — zero hits. (§1)
3. **The "CSO Insights forecast accuracy ~50-75%" statistic could not be traced to a primary CSO Insights
   report** — search tooling failure (WebSearch dead, DDG/Bing/Marginalia all non-functional this
   session) prevented a full trace, but no primary was located via any working route either. (§2, §3)
4. **No sales-specific published calibration curve** (predicted stage probability vs. realized close rate,
   plotted) was found from any vendor, analyst, or academic source. (§6)
5. **Salesforce's own "forecast categories" definitions were not independently fetched** — every attempt
   hit a 403 or JS-rendered page with no static methodology/definition text. The widely-repeated
   "Pipeline/Best Case/Commit/Closed/Omitted" framing attributed to Salesforce online should be treated as
   unverified pending a successful direct fetch. (§1)
6. **RepVue's, Pavilion/Benchmarkit's, and Salesforce State-of-Sales's stated survey methodologies could
   not be independently confirmed** — all bot-blocked or JS-rendered against every fetch method tried
   (WebFetch, curl with multiple user agents). (§5)
7. **The KBCM/Sapphire primary permalink is missing even in the sibling corpus that already investigated
   it** — inherited gap, not something this pass could close per its own scope instructions. (§8)

---

## 10. Candidate never-ship figures (for the pack's cross-pack never-ship list)

- **"CSM quota attainment 55–65%" attributed to KBCM** — confirmed misattribution by the sibling corpus;
  the real KBCM figure is AE (sales) quota attainment ~70%→75%, and even that lacks a recorded permalink.
  Never ship the CSM-quota-attainment version of this figure under any circumstances.
- **"3x pipeline coverage" as a portable, source-agnostic constant** — it is the reciprocal of an assumed
  ~30–35% win rate, not an independently discovered threshold. Never ship "3x coverage" as a standalone
  rule; if shipped at all, it must be shown as coverage = 1/your own win rate, with the derivation visible.
- **Any vendor forecast-accuracy percentage (Clari, Gong's 95%/"20% more precision," Aviso's "29 quarters
  of highly accurate forecasts," or similar)** — none of the vendors checked disclose what "accuracy" is
  measured against, over what horizon, or on what sample. Never ship a bare vendor accuracy percentage
  without the vendor's own method statement attached, and even then it must be labeled vendor-self-reported.
- **"CSO Insights: forecast accuracy is ~50%" / "under half of forecasted deals close"** — could not be
  traced to a primary in this pass despite trying; treat as folklore and never ship as an attributed,
  sourced statistic. If the pack wants to make this point, use the Fildes & Goodwin (2007) finding instead
  (52.8% of surveyed professional forecasters review their own adjustment accuracy; 25% use no error
  measure at all) — it is peer-reviewed, method-disclosed, and makes a comparable point honestly.
- **Any Salesforce-attributed "Omitted" forecast category wording** — not independently verified; the
  verified HubSpot equivalent is "Not forecasted," and the two products should not be assumed to use
  identical category taxonomies without direct verification of each.
- **RepVue-sourced specific numbers of any kind** — could not fetch the site at all in this pass (bot-
  blocked); do not cite RepVue figures pulled from memory/training data, only from a verified live fetch.
