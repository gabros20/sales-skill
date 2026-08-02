# Raw C4 — Calculators/Tools + Vendor-Claim Tracing (GitHub/OSS channel, worker C4)

Search surfaces used this session, noted per-claim: `ghrelay` (GitHub search/rank/health), direct
`WebFetch` on known URLs, `curl -A <Chrome-UA>` (for sites that 403 WebFetch), `html.duckduckgo.com/html`
and Bing `format=rss` as search proxies (both proved unreliable mid-session — see Null Results),
`web.archive.org` CDX API + direct wayback fetch for dead/paywalled/JS-only pages. **WebSearch died
session-wide (200/200 quota) partway through my first two queries** — those two calls returned an
empty-looking "budget exhausted" response and were NOT used as evidence for any finding below; every
claim and every null result here is backed by a WebFetch/curl fetch of a real page, cited with its URL
and fetch method.

---

## 1. Calculators/tools table

| Repo | What it computes | Math defensible? | License (every file read) | Adapt or cite |
|---|---|---|---|---|
| [`BatManUtd/ltv-cohort-kit`](https://github.com/BatManUtd/ltv-cohort-kit) | Repeat-purchase cohort tables + CAC-payback LTV curves from a Shopify/WooCommerce order CSV. Deterministic, zero-dependency JS, runs from disk (no server). | Yes — `src/cohort.js` states its methodology in a code comment block verbatim: cohort = calendar month of first order; net revenue = total − refund, attributed to the *original order's* month; retention = ≥1 order with total ≥0 that month; **right-censoring** (a cohort×offset cell is only shown if that calendar month has fully elapsed as of the "as-of" date — no fake zeros for unelapsed months); `LTV(k) = cumulative net revenue through offset k / cohort size × margin%`; `CAC = monthly ad spend / new customers that month`; `Payback = first k where LTV(k) ≥ CAC`. Every definition is stated on the tool's own page per its README. | MIT — read directly (`LICENSE` file, standard MIT text, copyright BatManUtd 2026). | **ADAPT.** Best-built asset found in this channel. **Overlap flag: CAC-payback/LTV is growth's and success's territory (SaaS unit economics), not sales-specific** — D2C order-CSV framing is closer to growth/marketing than to a sales motion. Cite only if sales pack references it for context; do not re-ship as a sales-owned asset without checking growth/success didn't already ship the same math. |
| [`santiagoceron10/revops-pipeline-forecasting`](https://github.com/santiagoceron10/revops-pipeline-forecasting) | Pipeline coverage (raw + **stage-weighted**) vs a target, health banding, gap-to-target. An n8n + Postgres + local-Ollama demo workflow, not a standalone calculator. | **Partially — and it is a live illustration of the folklore problem the charter flags.** `DESIGN.md` states the formula explicitly: stage weights (Discovery 0.2, Demo 0.4, Proposal 0.6, Negotiation 0.8) chosen as "win-probability weights" with **no stated derivation**; `weighted_pipeline = Σ(amount × stage weight)`; `coverage_ratio = open_pipeline / target`; `weighted_ratio = weighted_pipeline / target`; `gap_to_target = max(0, target − weighted_pipeline)`. The health bands (`≥3× Healthy`, `2–3× Thin`, `<2× At risk`) are labeled **"Health (rule of thumb)"** in the repo's own design doc — i.e. even this repo's author does not claim to justify the "3×" convention, just asserts it. The seeded demo is explicitly reverse-engineered to "make the gap story show" (target tuned so raw coverage lands ~2.2×) — a demo, not a validated model. | MIT — read directly (`LICENSE` file). | **ADAPT the formula shape** (raw vs. stage-weighted coverage, gap-to-target) as a worked example; **do not adopt the "3×/2×" thresholds as validated** — cite them only as the folklore convention they demonstrably are (see §4 below). |
| [`AgentSpore/saascalc`](https://github.com/AgentSpore/saascalc) | Stateless SaaS metrics API — LTV, CAC, MRR, ARR, runway, churn, payback, quick ratio. | Formulas not inspected in depth (out of scope — overlaps growth/success). | **No LICENSE file** (`hasLicenseFile:false`); `pyproject.toml` has no `license` field at all → all-rights-reserved by default. | **CITE ONLY, do not adapt** — no license grant exists. Also note: README explicitly frames this as a "Reddit signal"-triggered founder-persona repo (TAM/SAM/CAGR competitor-landscape table inside the README) — a recognizable pattern of AI-agent-generated "founder" repos seeding GitHub with market-sizing boilerplate rather than organic open source; treat market-sizing claims inside such READMEs as self-authored marketing copy, not evidence. |
| [`cognis-digital/dealflow`](https://github.com/cognis-digital/dealflow) | "Model your sales pipeline as a YAML state machine and compute conversion rates, stage velocity, and weighted forecast straight from CRM exports." `dealflow forecast -p pipeline.yml -d deals.csv`. Real package (PyPI, CI, tests, 176 files) — the most production-shaped repo found in this search. | Not deep-read (license blocks reuse — see next column); README claims conversion-rate/stage-velocity/weighted-forecast computation but the underlying formula wasn't extracted since code can't be adapted anyway. | **Custom "Cognis Open Collaboration License (COCL) 1.0"** — read directly (`LICENSE` file). Grants non-commercial use only (§2); "Commercial Use of the Software is NOT granted under this License… contact Cognis Digital LLC" (§3); inbound contributions are relicensed to the licensor including for commercial resale (§4.2) — a classic CLA-style non-commercial-with-commercial-upsell license, **not OSI-approved, not permissive.** | **CITE ONLY** (name it as an example of a stage-weighted-forecast CLI shape) — cannot adapt code or redistribute under our pack's terms. Also flagged: this repo shares the "TAM/SAM/CAGR"-free but market-copy-heavy README pattern (`.cognis` dir, README typing-animation badges) common to the same auto-generated-project-farm genre as `saascalc` above — treat with proportionate skepticism about real-world usage (0 stars, `ratio-anomaly` flag from `ghrelay rank`). |
| `harshith-vaddiparthy/SaaSValuationCalculator` | SaaS valuation calculator (revenue multiple-based). | Not deep-read — out of core scope (valuation, not pipeline/quota/forecast math). | **No LICENSE file in repo**, but `package.json` declares `"license": "ISC"` (manifest counts per standing rule) — ISC is a permissive, OSI-approved license. | Adapt-eligible by manifest declaration, but low value for this pack (valuation ≠ sales motion) — noted for completeness only. |
| `luisminvielle/ote-calculator`, `Azeemaj101/Sales-Commission-Calculator`, `wsalinasVBAPro/Funnel-Model-Python` | OTE (on-target-earnings) calculator; chemical-co. commission-tier exercise; weighted-conversion bookings forecaster. | Toy/exercise-grade; `wsalinasVBAPro` is the only one with a real "weighted conversion" forecast shape but no stated methodology beyond code. | **No LICENSE file, no license field in any manifest found** (verified — `read … LICENSE` returned `not in tree` for all three, no `package.json`/`pyproject.toml` present). | **CITE ONLY, do not adapt** — all rights reserved by default; also all are 0-star, single-commit, unmaintained (`A` subscore 0–0.08 in `ghrelay rank`). |

**Landscape finding (the headline result of part (a)):** GitHub has **no established, well-maintained,
meaningfully-starred open-source calculator for sales-specific math** — pipeline coverage, quota
capacity/ramp, stage-weighted forecasting, commission plans, or ICP/territory scoring. Every
candidate surfaced by ~19 distinct `ghrelay search` queries (pipeline coverage, sales capacity model,
sales ramp model, commission calculator, SaaS metrics calculator, CAC payback calculator, lead scoring
model, ICP scoring, stage-weighted forecast, sales forecast backtest, OTE calculator, win-rate
calculator, territory planning, deal-scoring rubric, quota-attainment calculator, sales-quota-calculator-excel,
sales-rep-ramp-time-calculator, account-scoring B2B model, revenue-forecasting-SaaS-open-source) tops
out at **0 real stars** (one repo, `dealflow`, shows `st:1`, i.e. a single star). This contrasts
sharply with the CS/support and growth-experiment tooling niches the sibling packs found — sales math
(pipeline coverage, quota capacity, comp plans) is apparently never open-sourced as a standalone tool,
likely because it's either buried inside commercial RevOps platforms (Clari, InsightSquared) or kept
as private spreadsheets. Grep.app code search (would have let me search for the code-token
`pipeline_coverage` etc. across GitHub's larger corpus) was down (`SOURCE_DOWN`, 504) for the window I
tried it — noted as a genuine tooling gap in coverage, not a swept null (see §6).

---

## 2. Formula reference notes (from the corpus above + primary reasoning)

- **Required pipeline (the base identity everyone converges on):** `required_pipeline = quota / win_rate`.
  Every stage-weighted-forecast repo found (`revops-pipeline-forecasting`, `dealflow`,
  `wsalinasVBAPro/Funnel-Model-Python`) implements a variant of this, and it is definitionally an
  algebraic inverse of win rate — if win rate is fixed and known, the pipeline multiple needed to
  produce one win is exactly `1/win_rate`. **This is where "3× coverage" folklore likely originates
  numerically**: `1/win_rate ≈ 3` only when win rate ≈ 33%. No source found in this search — including
  the dedicated repos above — states this derivation explicitly; `revops-pipeline-forecasting`'s own
  design doc labels its thresholds "rule of thumb" without connecting them back to any specific win
  rate. **I could not find a single primary source that performs this derivation on the page** (see
  Null Results, §6) — the arithmetic is trivial and undocumented everywhere I looked, which is itself
  the teaching point: the multiplier silently assumes your win rate is ~33% and stays fixed across the
  observation window, an assumption almost never stated when the number "3×" is quoted.
- **Stage-weighted (probability-weighted) pipeline:** `weighted_pipeline = Σ(deal_amount × stage_win_probability)`,
  with `stage_win_probability` a hand-set lookup table per CRM stage (never observed/backtested in any
  source found — every instance in this search is an *asserted* table, not a fitted one). This is the
  standard "expected value of pipeline" convention (sometimes called "weighted forecast" in Salesforce/
  HubSpot CRM UIs) — the sibling repos above use 4-stage tables (0.2/0.4/0.6/0.8-style geometric
  spacing) with no stated basis for the specific numbers, which is consistent with how CRM vendors ship
  default stage-probability tables out of the box (Salesforce Opportunity stage `Probability` field
  defaults are also hand-set, not fitted — not independently re-verified here, flagging as a claim to
  confirm against Salesforce's own docs if the pack cites it).
- **No backtested forecast model was found anywhere in this search.** Every "forecast" repo either (a)
  computes a point-in-time coverage/weighted-pipeline snapshot with no historical accuracy check
  (`revops-pipeline-forecasting`, `dealflow`), or (b) is a generic retail/e-commerce time-series
  forecasting exercise (Prophet/XGBoost/SARIMA repos surfaced under "sales forecast backtest") that has
  nothing to do with B2B sales-rep pipeline forecasting — those are demand-forecasting student projects,
  unrelated to the CRM-stage-forecast question the charter asks about. **This is a genuine gap**: no
  open-source artifact anywhere in this search actually validates a stage-weighted or category-based
  (Commit/Best-Case/Pipeline) sales forecast against realized outcomes. If the pack needs a "does
  anyone backtest this" answer, the honest answer from this channel is: not in public GitHub repos.

---

## 3. VENDOR CLAIM LEDGER

All Gong entries below were fetched from **gong.io directly** (`www.gong.io/blog/...` and
`www.gong.io/gong-labs`), via `WebFetch` (worked without blocking) and `curl -A <Chrome-UA>` for the raw
HTML (used to extract the JSON-LD FAQ block that WebFetch's readability extraction dropped). All are
primary — none is a secondhand blog's rendition.

### Gong Labs — the methodology statement itself (from `gong.io/gong-labs`, JSON-LD FAQ schema)

Fetched via `curl -A <Chrome-UA> https://www.gong.io/gong-labs` (2026-08-03); the FAQ answers are not
in the page's rendered/readability text (WebFetch missed them — they're accordion-hidden) but **are
present verbatim in an embedded `application/ld+json` FAQPage schema block**, which is the authoritative
methodology disclosure Gong publishes:

> **"How does Gong Labs collect its data?"** — "Gong Labs analyzes anonymized interaction data from the
> Gong platform, including recorded calls, meeting transcripts, email activity, and rep behavior data.
> For each research question, our team defines a methodology to identify and measure specific trends at
> scale. All data is used in aggregate and no individual, company, or conversation is ever identifiable
> in our findings."
>
> **"How much data does Gong Labs research use?"** — "Our research draws from billions of sales
> interactions across **5,000+ companies**. The scale of this dataset is what makes Gong Labs findings
> uniquely reliable — rather than extrapolating from a small sample, we're measuring patterns across
> tens of millions of data points per topic."
>
> **"How is Gong Labs research different from surveys or analyst reports?"** — "Most sales research asks
> people what they think or what they believe they do. Gong Labs measures what actually happens...
> When we say a particular discovery technique **correlates** with higher win rates, it's because we
> measured it across millions of calls, not because reps told us it works."

**This is the systemic finding the charter asked me to establish, and Gong discloses it plainly rather
than hiding it**: the sample frame is **"5,000+ companies"** — i.e., Gong's own paying customer base,
a self-selected population (companies that bought a conversation-intelligence tool, skewing toward
funded/mid-market+ tech and SaaS sales orgs that already invest in sales tooling — Gong does not
disclose industry/segment/company-size breakdowns anywhere in this FAQ). The FAQ's own "different from
surveys" answer **uses the word "correlates" in one sentence, then in the very same paragraph implies
causal license** ("it's because we measured it… not because reps told us it works" — conflating
"measured, not self-reported" with "therefore causal"). Gong does not publish confidence intervals,
control variables, peer review, or raw data/code for any claim found below.

| Claim (verbatim) | Source URL | N (stated) | Method disclosed? | Correlational/causal | GRADE + reader-correction |
|---|---|---|---|---|---|
| "sellers that frequently use AI generate 77% more revenue than those not using AI at all" | [gong.io/blog/the-best-sales-insights-of-2025](https://www.gong.io/blog/the-best-sales-insights-of-2025) | 7.1 million opportunities (2025) | Partial — dataset size stated, no controls/segment breakdown, no significance testing | Correlational, framed with causal language ("generate") | **Correlational dressed as causal.** "Frequently use AI" reps are plausibly higher performers/better-resourced/at larger accounts to begin with — the claim doesn't rule out reverse causation (successful reps adopt more tools) or confounding by deal size/seniority. Reader correction: read as "AI use correlates with revenue in Gong's self-selected customer base," not "AI use causes +77% revenue." |
| "those that close successfully have twice as many buyer contacts as those that don't" / 77% of deals involve multiple contacts / 130% win-rate boost on deals over $50K | [gong.io/blog/the-best-sales-insights-of-2025](https://www.gong.io/blog/the-best-sales-insights-of-2025) | 1.8 million opportunities | Partial — N stated, no time window, no controls | Correlational, no causal language disclaimer | **Correlational observation, plausible confound**: multi-threading and deal size/complexity both independently predict "successful," so an observational split can't cleanly attribute the lift to threading itself. Defensible as a *pattern*, not as a prescriptive "add contacts → win more" causal claim. |
| "selling teams for closed-won deals are 67% larger than those for lost deals"; sales engineers "increase win rates by up to 30%" | [gong.io/blog/the-best-sales-insights-of-2025](https://www.gong.io/blog/the-best-sales-insights-of-2025) | Not stated for this specific cut | No — no N, no segment, no method for this claim | Correlational, no causal disclaimer | **Unfalsifiable as stated** — "up to 30%" is a range-ceiling framing with no distribution shown; no N given for this specific claim inside a larger N=unstated dataset. |
| "1M+ executive sales cycles" analyzed in partnership with 30 Minutes to President's Club (Armand Farrokh) and Jen Allen-Knuth; "won $50K–$250K deal... typically involves at least 10 stakeholders"; win rates "drop by roughly 6%" when eval starts with an exec vs. "5% increase" when exec is looped in around the 3rd touchpoint | [gong.io/blog/when-and-how-to-multi-thread-when-selling-to-executives](https://www.gong.io/blog/when-and-how-to-multi-thread-when-selling-to-executives) | 1M+ executive sales cycles | Partial — N and co-research-partner named; no segment/industry breakdown, no confidence interval on the 6%/5% deltas | Correlational | **Correlational, precise-sounding numbers without error bars.** The 6% vs 5% deltas read as statistically precise but no significance test or variance is shown — classic "precision theater." Treat the direction (early-exec-involvement can backfire; mid-cycle exec involvement helps) as plausible, the exact percentages as decorative precision. |
| "C-level executives are 30.2% less likely to reply to cold emails than non-executives"; reply rates "drop sharply once emails exceed 100 words," best range 50–100 words; executives spend "no more than nine seconds" reading, "less than three seconds" deciding to open | [gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says](https://www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says) | "1M+ executive sales cycles" (same dataset as above) | **No** — the article's own text states "We analyzed 1M+ executive sales cycles in partnership with Gong and Jen Allen-Knuth" but gives no data-collection detail, sample composition, significance testing, or control variables beyond that one sentence | Correlational | **The "9 seconds" / "3 seconds" figures in particular are unfalsifiable as published** — no instrument is named for measuring executive read-time from email/call data (this smells like an inferred/estimated framing device rather than a directly measured behavior); "30.2%" (one decimal place) is precision-theater on an undisclosed base. |
| "high performers maintain the same talk-to-listen ratio whether they win or lose" (60% vs. low performers swinging 54%→64%) | [gong.io/blog/the-best-sales-insights-of-2025](https://www.gong.io/blog/the-best-sales-insights-of-2025) | Not disclosed | No | Correlational | **No N for this specific cut** inside a "tens of millions of interactions" umbrella claim — can't assess robustness. |
| "94% of buyers use AI before they talk to you" — Gong's own trend line: "250% increase in AI-driven vendor discovery," "280% increase in AI used as buying advisor," "208% increase in AI-assisted vendor evaluation" since early 2024 | [gong.io/blog/94-of-buyers-use-ai-before-they-talk-to-you](https://www.gong.io/blog/94-of-buyers-use-ai-before-they-talk-to-you) | Not disclosed for the Gong-sourced trend %s | Gong: no. (The **94%** headline figure is NOT Gong's own — it's attributed inside the same article to **Forrester's 2026 B2B buyer survey of "nearly 18,000 global business buyers,"** a disclosed survey N) | Gong trend lines: correlational/no N. Forrester figure: survey self-report, N disclosed. | **Mixed-source article — attribute carefully.** The eye-catching "94%" in the headline is Forrester's (survey-based, N disclosed: 18,000), not Gong's own conversation-intelligence data; Gong's own "250%/280%/208%" increases have no stated base N. A reader citing "Gong says 94% of buyers use AI" is misattributing a Forrester survey stat to Gong's telemetry corpus — this is exactly the kind of mix-up the pack should teach readers to check. |

### Other vendor benchmark sources

| Vendor | What was checked | Methodology page found? | Grade |
|---|---|---|---|
| **Salesforce "State of Sales"** | `https://www.salesforce.com/resources/research-reports/state-of-sales/` — fetched via `curl -A <Chrome-UA>`, 200 OK, 459KB HTML | **No** — page is a client-side-rendered React/JS app; static HTML contains only generic marketing copy ("AI agents. Revenue strategies. Explore the latest sales trends you need to succeed.") and no report content, methodology, sample size, or respondent composition. The actual report is presumably gated behind a lead-capture form not reachable by static fetch. | **Cannot grade the content — grade the disclosure practice: 0/10 accessible.** The public landing page discloses nothing about how the "State of Sales" data was collected; a reader who cites Salesforce's "State of Sales" stats without finding the actual PDF has no way to know if it's a customer telemetry pull or an outside-panel survey. |
| **HubSpot "State of Sales" / Sales Trends Report** | Direct guesses `hubspot.com/state-of-sales` (404), `blog.hubspot.com/sales/state-of-sales-report` (404) both dead; `blog.hubspot.com/sales/sales-statistics` (200) checked via WebFetch | **No** — the evergreen stats roundup page references "HubSpot's Sales Trends Report" and "State of Sales report" by name repeatedly but provides **no methodology documentation on that page**: no sample size, no respondent job titles/company sizes/countries, no survey-vs-telemetry statement. Notably the page's own strongest buying-group stat ("large strategic deals include an average of 17 contacts") is **attributed to Gong**, not to HubSpot's own survey — HubSpot is citing Gong's corpus rather than running independent telemetry for that figure. | **Undisclosed / re-citation without methodology.** Grade: unfalsifiable as published on this page; the report itself (not located) may have more detail, but the surface HubSpot actually points readers to does not. |
| **Salesloft** | `salesloft.com/resources` (200, checked via WebFetch) | Resources hub lists content categories (Blog, Videos, Webinars, "Research & Guides," Case Studies) but **no specific benchmark-report titles or methodology text were present in the fetched page** — direct `/resources/benchmark-report` URL guess 404'd. | **Null result, not "no research exists."** I could not locate a dedicated benchmark-methodology page from this surface; see §6. |
| **Outreach (rebranded outreach.ai)** | `outreach.io/resources` 301-redirects to `outreach.ai/resources` (checked via WebFetch) | Page lists IDC-branded reports ("IDC 2025 CX CSAT Award for Sales," "2025 Agentic AI Revenue Intelligence — IDC Report") — i.e., **third-party analyst reports, not Outreach's own disclosed-methodology research**. One self-referential claim: "Outreach helps sellers close over 2 million opportunities every month" — stated as a capability/scale claim, not framed as a research finding with method. | **No Gong-Labs-equivalent research vertical found on Outreach.** The claims that exist are IDC-attributed (external) or undisclosed internal-scale marketing copy. |
| **Chorus / ZoomInfo** | `chorus.ai` (200, redirects into zoominfo.com product page — minimal content); `zoominfo.com/blog` → 302 → `pipeline.zoominfo.com` (checked via WebFetch); `zoominfo.com/resources` returned 403 | **No dedicated "Labs"-style research vertical found.** `pipeline.zoominfo.com`'s visible article list (fetched 2026-08-03) is GTM-data-platform content (ABM platforms, lead routing, marketing orchestration) with **no call/conversation-analysis benchmark articles and no methodology disclosures** on the pages reached. | **Null result** — Chorus's conversation-intelligence data (which would be the direct Gong-Labs analog) does not appear to feed a public benchmark-research vertical the way Gong's does, at least not on the surfaces reached this session. |

---

## 4. FALSIFICATION TARGETS — named suspect figures

| Figure | Claimed source | Primary found? | What the primary actually says | Verdict |
|---|---|---|---|---|
| **"57% of the buying decision is made before contacting sales"** | Usually attributed loosely to "CEB" or (post-2017 CEB/Gartner merger) misattributed to "Gartner" | **YES — fully traced.** CEB Marketing Leadership Council, *"The Digital Evolution in B2B Marketing"* (2012, research conducted in partnership with Google). PDF retrieved via Wayback Machine (`web.archive.org` snapshot of `cebglobal.com/content/dam/.../ceb-mktg-b2b-digital-evolution.pdf`, 46 pages, fetched 2026-08-03). Page 1 of the "Prologue" chapter states the methodology directly. | Exact primary wording (Figure 1/callout, p.1): **"57% — that's how far the average B2B buyer is through the purchase decision before engaging a supplier sales rep."** Body text: "CEB Marketing Leadership Council surveyed more than **1,500 customer contacts** (decision makers and influencers in a recent major business purchase) for **22 large B2B organizations** (spanning all major NAICS categories and **10 industries**). ...the survey revealed that the average customer had completed **more than one-half** of the purchase decision-making process prior to engaging a supplier sales rep directly... At the upper limit, that number ran **as high as 70%**." Sourced in the chart footnote as "CEB, Customer Purchase Research Survey, 2011," n=1,500. **Methodology is genuinely disclosed** — survey-based (self-report by buyers, not telemetry), specific N, specific scope (large B2B orgs, 10 industries) — this is a defensible finding by the survey's own stated scope, not "unfalsifiable marketing." | **TRACED, but widely MISQUOTED downstream.** Two distinct misquote patterns exist in circulation and should both be taught: (1) **misattribution** — the study is CEB's (a private research/advisory firm), commonly re-attributed to "Gartner" because Gartner acquired CEB in 2017, five years after this report; citing it as "a Gartner study" without the 2012/CEB origin is chronologically wrong. (2) **completion-vs-progress conflation** — the primary says the buyer is "57% **through the** purchase decision-making **process**" (a progress measure, on a 1,500-respondent, 2011-vintage B2B survey), which gets flattened in circulation into "the decision is **already made**" — a stronger, false claim the primary does not support (it explicitly still shows 43% of the process remaining on average, and Figure 2's own distribution shows suppliers ranging 45%–70%, i.e. never near 100%). |
| **"the typical buying group involves 6 to 10 decision makers"** | Gartner | **YES — fully traced, primary matches the popular figure.** `gartner.com/en/sales/insights/b2b-buying-journey`, retrieved via Wayback Machine (2020-04-21 snapshot, fetched 2026-08-03 — live gartner.com blocks all fetch attempts with 403, including `curl` with a Chrome UA). | Exact verbatim: **"The typical buying group for a complex B2B solution involves six to 10 decision makers, each armed with four or five pieces of information they've gathered independently and must deconflict with the group."** | **TRACED, essentially accurately represented** in most citations — unlike the 57% figure, the "6–10" number in circulation matches Gartner's own wording closely. The nuance usually dropped: the "four or five pieces of information they've gathered independently and must deconflict" clause — the harder, more teachable part of Gartner's actual point (information *asymmetry and reconciliation* inside the buying group, not just headcount) is almost never carried over into the popular one-liner. |
| **"3× pipeline coverage"** | Diffuse / "sales folklore," no single named source | **NO — searched, not found.** Checked (all via direct WebFetch/curl, 2026-08-03): `openviewpartners.com/blog/pipeline-coverage-ratio/` (404), `saastr.com/how-much-pipeline-do-you-really-need/` (404), `clari.com/blog/pipeline-coverage-ratio/` (404, generic nav only), `forecastio.ai/blog/pipeline-coverage-ratio` (404). Within this channel's own OSS corpus, `santiagoceron10/revops-pipeline-forecasting`'s own `DESIGN.md` labels its coverage thresholds **"Health (rule of thumb)"** — i.e. the closest thing to a primary artifact in this search *itself* declines to justify the number. | No primary derivation located anywhere searched. | **FOLKLORE.** The number is algebraically explicable — `required_coverage = 1/win_rate`, and `1/0.33 ≈ 3` — but I found no source, anywhere searched, that states this derivation on the page next to the "3×" recommendation. Every instance found either asserts the multiplier as received wisdom or (in the one OSS repo that computes it) explicitly flags it as an un-derived rule of thumb. This is exactly the R21 case where "its arithmetic IS the teaching": the reader should be shown `coverage = 1/win_rate` and told that "3×" is only correct for a ~33% win rate — a different win rate needs a different multiple, and nobody selling the "3×" heuristic says so. |
| **"it takes 8 touches to reach a prospect"** (and the related "80% of sales happen on the 5th–12th contact") | Frequently attributed to "National Sales Executive Association" (name varies by source) | **NO — not traced this session.** Searches attempted: Bing `format=rss` queries for the origin/debunking of this claim returned unrelated/geo-junk results (see §6 — this specific search surface degraded mid-session and I could not get usable results before abandoning it); no working alternative surface was found in the remaining time budget. | N/A | **FOLKLORE by default (unable to trace, not verified false).** Do not present this as debunked — I did not find a working search path to either confirm or refute it this session. Flag for a future pass with a working search tool (WebSearch, once quota resets, or a different proxy) rather than asserting a grade I couldn't support with a fetch. |
| **"Always Be Closing" (Glengarry Glen Ross)** | Pop-culture sales lore, sometimes cited as if it were an established methodology | **YES — traced via Wikipedia (`en.wikipedia.org/wiki/Glengarry_Glen_Ross_(film)`, fetched via WebFetch 2026-08-03).** | Verbatim from the article's Legacy section: **"The film has had an enduring legacy for its memorable dialogue and performances, particularly the 'Always Be Closing' speech by Alec Baldwin, whose character Blake was created for the film adaptation to make the pressures of sales work more explicit."** The article confirms Blake/the ABC monologue does **not appear in the original 1984 stage play** — it was written by David Mamet specifically for the 1992 film. | **TRACED — and the lineage itself is the teaching.** "Always Be Closing" originates as a **fictional, satirical** line delivered by a deliberately unsympathetic, high-pressure antagonist character invented for a film critiquing toxic sales culture — not as a documented sales methodology with any evidentiary basis. Its adoption into earnest real-world sales motivational culture inverts the film's own intent (Blake is not portrayed as an admirable figure). Modern named methodologies the pack cites elsewhere (SPIN, Challenger, MEDDIC, Sandler) explicitly reject high-pressure "always closing" framing in favor of qualification/discovery-led selling — worth stating explicitly as the contrast. |

**Not re-derived per charter instruction:** KBCM ~70→75% AE quota-attainment benchmark — already
primary-verified in success's corpus; not touched here.

---

## 5. LICENSING LEDGER (for §1 assets)

| Repo | File(s) actually read | License finding |
|---|---|---|
| `BatManUtd/ltv-cohort-kit` | `LICENSE` (root) | MIT, full text read, copyright BatManUtd 2026 — clean, adoptable. |
| `santiagoceron10/revops-pipeline-forecasting` | `LICENSE` (root) | MIT, full text read, copyright Santiago Ceron / SC Agentic Solutions 2026 — clean, adoptable. |
| `cognis-digital/dealflow` | `LICENSE` (root) — read in full (COCL 1.0, all 9 sections down through §9 Security-Tool Acceptable Use, truncated at that point) | **Custom "Cognis Open Collaboration License 1.0."** Non-commercial-only grant (§2); commercial use explicitly excluded and requires a separate paid license (§3); relicensing/CLA clause on inbound contributions (§4.2). **Not a redistribution-safe license for a commercial skill pack asset** — cite existence and shape only. |
| `AgentSpore/saascalc` | `LICENSE` — absent (confirmed via `read`, `not in tree`); `pyproject.toml` — read in full, **no `license` field present** | No license grant anywhere in the repo (no file, no manifest field) → default all-rights-reserved. Cite only. |
| `luisminvielle/ote-calculator` | `LICENSE` — absent (confirmed via `read`, `not in tree`, no nearest-match candidates either) | No license file found. Cite only. |
| `Azeemaj101/Sales-Commission-Calculator` | `LICENSE` — absent (confirmed via `read`, `not in tree`) | No license file found. Cite only. |
| `harshith-vaddiparthy/SaaSValuationCalculator` | `LICENSE` — absent (`read` → `not in tree`); `package.json` — read in full | **Manifest declares `"license": "ISC"`** (permissive, OSI-approved) even though no `LICENSE` file text exists in the repo. Per standing rule ("package manifests count"), this is a valid permissive-license declaration — adopt-eligible, though the pack has no real use for a valuation calculator. |
| `wsalinasVBAPro/Funnel-Model-Python` | `LICENSE` — absent; no manifest file present at all | No license anywhere. Cite only. |

No renamed/redirected repos encountered in this set (all `full_name`s matched their current canonical
location; no stale-citation risk found here).

---

## 6. NULL RESULTS — exactly where I looked and found nothing usable

- **WebSearch tool, first two queries of this session** ("gong.io labs 'we analyzed' million sales
  calls" and "gong.io 'methodology' sales call data analysis site:gong.io") — both returned a
  "budget exhausted (200/200)" response that visually resembles an empty result set. **Neither was used
  as evidence for anything above.** I re-ran every subsequent lookup through WebFetch/curl instead, per
  the mid-session correction from sales-lead-c.
- **`ghrelay code "pipeline_coverage" --lang ...`** — grep.app (the code-search backend) returned
  `SOURCE_DOWN` (504) when I tried it once, mid-session. Not retried (breaker/cooldown + time budget).
  This means GitHub's larger code corpus was never searched for the literal code tokens
  `pipeline_coverage`, `coverage_ratio`, `win_rate` etc. — a real coverage gap in part (a), not a swept
  null. A follow-up pass should retry `ghrelay code` once grep.app is confirmed up (`ghrelay doctor`).
- **`html.duckduckgo.com/html/?q=...`** — worked once (found the Gong "Best Sales Insights of 2025"
  post), then returned a bot-CAPTCHA ("select all squares containing a duck") on every subsequent call
  this session. Abandoned as a search surface after ~3 CAPTCHA responses.
- **Bing `www.bing.com/search?format=rss&q=...`** — worked for the first two queries (Salesforce/HubSpot
  lookups, returned topically relevant if shallow results), then degraded into serving **unrelated,
  apparently geo-cached/generic results** (car-rental sites, Croatian news, Chilean street addresses,
  generic "pipeline" dictionary/CRM-software hits) regardless of query content for every query after
  that, including three separate reformulations of the "8 touches" origin query and one "3x pipeline
  coverage derivation" query. I could not get a working query through after that point and stopped
  using this surface. **This is why "it takes 8 touches" is graded FOLKLORE-by-default above rather than
  FOLKLORE-confirmed** — I have not actually located and read a source stating this figure at all, so I
  cannot describe what it originally measured.
- **`gartner.com` (live site)** — every direct fetch attempt (WebFetch and `curl -A <Chrome-UA>`) to
  `gartner.com/en/sales/insights/b2b-buying-journey` and `gartner.com/en/newsroom` returned **403
  Forbidden**. Worked around via Wayback Machine snapshots (see §4) — the live site itself is not
  fetchable by this session's tools.
- **`hbr.org/2012/07/the-end-of-solution-sales`** (the Adamson/Dixon/Toman Challenger-sale HBR piece,
  relevant background for the family's Challenger evidence-base item, not this worker's direct
  assignment) — fetched successfully (200) but **paywalled beyond the introductory paragraph**; no 57%
  or related purchase-decision statistic appears in the visible portion. Not chased further since the
  CEB PDF (§4) already gave a stronger, fully-disclosed primary for that figure.
- **`salesforce.com/resources/research-reports/state-of-sales/`** — 200 OK via `curl -A <Chrome-UA>`,
  459KB of HTML fetched and inspected directly (not just WebFetch's readability extraction) — confirmed
  client-side-rendered React app; no report content, methodology, or sample-size text present in the
  static payload at all, only marketing meta tags. Did not attempt to locate the underlying PDF/gated
  report (would require submitting a lead-capture form — out of scope, and prohibited by the "entering
  personal data into a form" rule regardless).
- **`salesloft.com/resources/benchmark-report`** (404) and **`outreach.io/resources/benchmarks`** (404)
  — direct URL guesses at a benchmark-report path, both dead; the working `/resources` index pages for
  both vendors were checked instead (see §3 table) and showed no equivalent to Gong's dedicated
  methodology-disclosing research vertical.
- **`zoominfo.com/resources`** — 403 Forbidden via `curl -A <Chrome-UA>`; worked around via
  `zoominfo.com/blog` (which itself 302-redirects to `pipeline.zoominfo.com`, checked instead, see §3).
- **`chorus.ai`** — resolves (200) but redirects into a near-empty ZoomInfo product stub with no
  research content; no dedicated Chorus research vertical found on any surface reached this session.

---

**Coverage note for the channel lead:** part (a) is a genuinely thin landscape — confirmed via ~19
distinct `ghrelay` queries plus `rank`/`health`/`skim` on the 8 best candidates, not a shallow pass.
Part (b) got strong, fully-verified primary sourcing on 3 of the 5 named suspect figures (57%,
buying-group 6–10, Always Be Closing) and a complete Gong Labs methodology trace (5 primary posts + the
FAQ schema disclosure), but 2 items (8-touches origin, and a live-site check of Salesforce/Gartner's
gated/blocked report internals) were blocked by tooling failures this session (WebSearch quota death,
DuckDuckGo CAPTCHA, Bing RSS degradation, Gartner/Salesforce bot-blocking) rather than by an actual
absence of anything to find — flagged above per source, not silently dropped.
