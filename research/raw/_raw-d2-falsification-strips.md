# D2 — Falsification Strips: Tracing B2B Sales' Most-Cited Statistics

Channel D worker D2. Mission: trace famous sales statistics to primary sources or grade them folklore, documenting drift from original wording. Every claim below has a permalink (or an explicit note that none exists), a verbatim quote, and local context proving the quote means what's claimed.

**Tooling note:** WebSearch was exhausted session-wide before this file's research began. All search was done via WebFetch against Brave Search (`search.brave.com`) and, for JS-heavy/blocked pages, via `crawl4ai`'s Python API run through Bash (browser-rendered fetch with a Chrome UA). The Wayback Machine (`web.archive.org`) was reached the same way, since direct WebFetch to `web.archive.org` errors out in this environment. No URL below was guessed or reconstructed — every link was either returned by a search result or found via the Wayback CDX/`available` API.

---

## Strip 1 — "57% of the B2B buying decision is complete before a customer contacts a supplier" (THE flagship misquote)

### Claim as commonly stated
"57% (or 60%, or 70%) of the buying journey is over before a customer talks to sales." Frequently also stated as a Gartner stat: "buyers only spend 17% of their time with sales reps."

### Origin hunt
Searched for the CEB "Digital Evolution in B2B Marketing" 2012 report. Found a legitimate hosted copy of the **full original PDF** on Google's own domain (Google co-published the study), not just a logo/cover fragment as an earlier fetch attempt suggested:

**PRIMARY, retrieved in full:** `https://www.thinkwithgoogle.com/_qs/documents/677/the-digital-evolution-in-b2b-marketing_research-studies.pdf` — "The Digital Evolution in B2B Marketing," CEB Marketing Leadership Council, "Research Conducted by Marketing Leadership Council, In Partnership with Google," © 2012 The Corporate Executive Board Company.

### Original wording + what it actually measured
Page 2 of the report ("Prologue: The Current State of Practice"), under "The Rising Importance of Digital":

> "To understand the scope of this issue in the B2B context, CEB's Marketing Leadership Council (MLC) surveyed more than 1,500 customer contacts (decision makers and influencers in a recent major business purchase) for 22 large B2B organizations (spanning all major NAICS categories and 10 industries). In a striking finding, the survey revealed that the average customer had completed **more than one-half of the purchase decision-making process prior to engaging a supplier sales rep directly** (Figure 1). At the upper limit, that number ran as high as **70%** (Figure 2)."

Figure 1's chart shows the exact figure: **"57% Complete"**, plotted along an axis from "Customer Due Diligence Begins" → "Customer's First Serious Engagement with Sales" → "Purchase," captioned "Customers are choosing to delay commercial conversations with suppliers." n = 1,500. **Source line under the chart: "CEB, MLC Customer Purchase Research Survey, 2011."**

Figure 2 gives the distribution *across the 22 supplier organizations* (not across individual customers): a histogram with buckets 45–50% (4 suppliers), 51–55% (8), 56–60% (5), 61–65% (3), 66–70% (2), >70% (0). The 57% is a customer-level average; the 70% is the observed maximum of a *supplier-level* average — a materially different quantity than "the average buyer."

**What it measured, precisely:** self-reported, retrospective survey responses from customer contacts about a recent purchase, asking how far along the purchase decision-making process (research, requirements-setting, vendor comparison, etc.) they felt they were when they first had a serious engagement with a **supplier sales rep**. It is a self-assessed "percent complete" figure, not a time-allocation or behavioral-log measure, and its unit of "before" is specifically "a supplier's sales rep," not "any contact with the supplier company" (e.g., visiting the supplier's website is not the cutoff).

**A drift artifact already exists inside the primary document itself:** the sidebar pull-quote on the same page reads "On average, customers progress **nearly 60%** of the way through the purchase decision-making process before engaging a sales rep" — a rounding-up of 57% to "nearly 60%" that CEB's own marketing copy performed before anyone else did.

### Drift chain, step 2 — the HBR "End of Solution Sales" article
Search surfaced Brent Adamson, Matthew Dixon, and Nicholas Toman, **"The End of Solution Sales,"** *Harvard Business Review*, July–August 2012 (official: `https://hbr.org/2012/07/the-end-of-solution-sales`, paywalled; full text read via a mirrored reprint PDF at `https://www.mitchellmackey.com.au/wp-content/uploads/2012/08/The-End-of-Solution-Sales-CEB-HBR-August-2012.pdf`).

Exact text:

> "In fact, a recent Corporate Executive Board study of more than **1,400** B2B customers found that those customers completed, on average, **nearly 60%** of a typical purchasing decision—researching solutions, ranking options, setting requirements, benchmarking pricing, and so on—**before even having a conversation with a supplier**."

This is a second, closely related but *not identical* CEB figure: **n = 1,400** here vs. **n = 1,500** in the Google-partnered MLC report, and the cutoff is broadened from "engaging a supplier sales **rep**" to simply "having a conversation with a supplier" (any conversation, not necessarily with sales). Whether this is the same underlying survey re-described loosely, or a second CEB Sales Executive Council study, is not resolved by the HBR text itself — it does not cite a report name or date. Either way, this HBR piece (co-authored by CEB's own researchers) is the most plausible vector by which "57%" became "60%" in mainstream business writing: it is far more widely read and quoted than the original MLC/Google PDF.

### Drift chain, step 3 — the Gartner "17%" / "5-6%" figure, and why it is NOT the same claim
Searched for Gartner's figure on time buyers spend with suppliers. The **current live page** at `https://www.gartner.com/en/sales/insights/b2b-buying-journey` no longer contains this stat (see below) — it was recovered via the Wayback Machine:

**PRIMARY, via Wayback:** `http://web.archive.org/web/20210106120644/https://www.gartner.com/en/sales/insights/b2b-buying-journey` (Gartner's own "B2B Buying Journey" insights page, captured 2021-01-06).

Exact text:

> "In fact, Gartner research finds that when B2B buyers are considering a purchase, they spend only **17%** of that time meeting with potential suppliers. When buyers are comparing multiple suppliers, the amount of time spent with any one sales rep may be only **5% or 6%**."

Attributed on-page to **Brent Adamson, Distinguished VP, Advisory, Gartner** — the *same Brent Adamson* who co-authored the original CEB Challenger Sale research and the 2012 HBR "End of Solution Sales" piece. This is not a coincidence: CEB was acquired by Gartner in 2017, and its lead researchers, including Adamson, moved with it. The 57%/60% (CEB, 2011–12) and the 17%/5–6% (Gartner, current as of at least 2021) figures are institutionally continuous — same research lineage, arguably the same person — **but they measure different things**:

- CEB 57%/60%: self-reported **percent of the purchase DECISION completed** before the first serious engagement with a sales rep (a completion/progress measure).
- Gartner 17% / 5–6%: percent of a buyer's **total buying TIME** spent in meetings with potential suppliers overall (17%), or with any single supplier when several are being compared (5–6%) — a time-allocation measure across a total that also includes independent research, internal buying-group coordination, etc.

These are frequently cited back-to-back in vendor content as if they're two versions of the same fact ("buyers do most of their journey without you — CEB says 57%, Gartner says only 17%!"). They are not directly comparable: one is "how far along are you" and the other is "what fraction of your time goes where."

**Additional drift note — citation rot:** the live Gartner page at the same URL, fetched fresh during this research, has been rewritten and **no longer states the 17%/5–6% figures at all**; it now emphasizes a "six buying jobs" framework and a different stat ("B2B buyers are 1.8 times more likely to complete a high-quality deal when they engage with supplier-provided digital tools in partnership with a sales rep"). Any current article that cites "gartner.com/en/sales/insights/b2b-buying-journey" as the source for "17%" is citing a live URL whose content has since changed out from under it; the wording is only recoverable via Wayback. This is itself a structural hazard for citation practices in this genre.

### Drift chain (summary)
CEB/Google MLC report (2011 survey, n=1,500, Figure 1 = "57%", body text = "more than one-half," sidebar = "nearly 60%," upper limit = "70%" for a *different, supplier-level* distribution)
→ HBR "End of Solution Sales" (2012, n=1,400 quoted, "nearly 60%," cutoff broadened to "a conversation with a supplier")
→ generic marketing/sales content (2013–present): rounds indiscriminately to "57%," "60%," or "70%," drops the sample and self-report caveats, drops "before engaging a sales rep" in favor of vaguer "before contacting a supplier" or "before talking to sales," and is frequently spliced together with the unrelated Gartner 17%/5–6% time-allocation stat as if corroborating evidence for the same underlying claim.

### Verdict + grade
**PRIMARY** source located and read for both halves (CEB/Google 2012 report; Gartner b2b-buying-journey page via Wayback). The 57% figure itself is real and traceable, self-reported, with a disclosed sample (n=1,500, 22 orgs, 2011 survey) — it is not fabricated. **What's folklore is the popularized restatement**: "57%/60%/70% of the buying journey" as an undifferentiated blob, and the conflation of the CEB completion-of-decision metric with the Gartner time-allocation metric as though they were the same finding.

---

## Strip 2 — "It takes 8 touches to get a meeting" (5–12 touches genre)

### Origin hunt
Searched broadly ("8 touches" "get a meeting" sales). The most credible attribution across dozens of vendor round-ups is **RAIN Group**.

**PRIMARY-ADJACENT (vendor, but named + sampled study):** `https://rainsalestraining.com/blog/how-many-touchpoints-does-it-take-to-make-a-sale`, citing RAIN Group's own **"Top Performance in Sales Prospecting"** research (`https://rainsalestraining.com/sales-research/sales-prospecting-research`):

> "According to our Top Performance in Sales Prospecting research, it takes an average of 8 touchpoints to get an initial meeting (or other conversion) with a new prospect."

The research page discloses a real sample: **489 sellers who conduct outbound prospecting**, plus **488 buyers representing $4.2 billion in purchases across 25 industries**, analyzed by cohort (Top Performers vs. others, industry, company size, etc.). The specific "8 touchpoints" figure itself was not visible in the crawlable excerpt (it's gated in the downloadable report), and neither the blog post nor the landing page discloses how "touchpoint" is operationally defined, the survey's date/timeframe, or response-rate/selection details.

### What else the genre says (no consensus)
A single Brave Search pass surfaced wildly different numbers, each stated as fact by a different vendor, several with **no source at all**:
- Nimble: "5 to seven touchpoints before a prospect makes a buying decision" — no citation.
- HubSpot ("The Ultimate Guide to Prospecting"): "statistically, across a broad spectrum of data, that number is around eight" — no named dataset.
- TrueList: "eight touchpoints to close a sale" — no citation.
- The Center for Sales Strategy: "12 to 15 touches before a prospect is ready to meet with sales" — no citation found in the snippet.
- impactmarketing.net, secondhand: "According to Salesforce, it takes 6-8 marketing touches to generate a viable sales lead" (this is Strip 5's overlapping claim — not independently verified against a Salesforce primary in this session; flagged as unverified attribution, not confirmed folklore).

### Verdict + grade
**VENDOR-SELF-REPORTED** for the "8 touches" figure specifically (RAIN Group: real named study, real sample size, but underlying methodology/definition not disclosed in the free blog content). **FOLKLORE** for the broader "X touches" genre as commonly repeated: the number quoted ranges from 5 to 15 depending on the source, most sources cite no study at all, and RAIN Group's specific, disclosed 489-seller figure is routinely stripped of its attribution and treated as a universal, vendor-agnostic law of B2B sales.

---

## Strip 3/4 — "92% of salespeople give up after 4 nos, but 80% of prospects say no 4 times before saying yes" / "80% of sales require 5 follow-up calls"

### Origin hunt
Ran a Brave Search for the exact "92%... 4 times" phrasing plus "MarketingDonut," since prior general knowledge of this space points there. Confirmed: **dozens** of current "sales statistics" round-up posts (Zety, Mailshake, Winmo, EmoryDay, ReminderMedia, Connect365, LeadResponse, and more) cite **"Marketing Donut"** by name as the source for this exact stat, e.g. Zety: `"92% of sales pros give up after the 4th call, but 80% of prospects say no four times before they say yes. (MarketingDonut)"`.

The live site (`www.marketingdonut.co.uk`) **no longer resolves** — confirmed via direct WebFetch (`getaddrinfo ENOTFOUND`) and independently via `crawl4ai` (`net::ERR_NAME_NOT_RESOLVED`). The page was recovered via the Wayback Machine:

**Recovered via Wayback (the page itself, not a further-upstream primary):** `http://web.archive.org/web/20231209060719/https://www.marketingdonut.co.uk/sales/sales-techniques-and-negotiations/why-you-must-follow-up-leads/` — "Why you must follow up leads," Marketing Donut (UK small-business advice site).

### Original wording + what it actually cites (or doesn't)
Exact text, in full:

> "Research shows, amazingly, that only 20% of sales leads are ever followed up. In other words, 80% of potential opportunities are lost without trace simply due to lack of follow-up... **Different studies carried out at different times, in different places, by different market research companies over a number of years all reveal that 80% of non-routine sales occur only after at least five follow-ups.** ... There are some fascinating statistics on this: 44% of sales people give up after one 'no'. 22% give up after two 'nos'. 14% give up after three 'nos'. 12% give up after four 'nos'. **That tells you that 92% of sales people give up after four 'no's', and only 8% cent of sales people ask for the order a fifth time.** When you consider that 80% of prospects say 'no' four times before they say 'yes', the inference is that 8% of sales people are getting 80% of the sales."

**No author byline or publication date was recoverable from the fetched excerpt of this page.** Critically: **no study, researcher, organization, or market-research company is named anywhere in the piece** — "different studies... different market research companies" is the entire citation. The 44/22/14/12% breakdown that sums to "92% give up by the 4th no" is presented as settled fact with zero traceability.

### Drift chain
Unnamed "different studies... by different market research companies" (date unknown, no primary ever surfaces) → Marketing Donut UK blog post (undated in the crawlable excerpt; the site's domain has since gone dead) → cited by name as "(MarketingDonut)" across dozens of 2018–2026 vendor "sales statistics" listicles (Zety confirmed citing it as of 2018-06-30) → increasingly cited without even naming Marketing Donut, just presented as free-floating fact.

### The separate "80% of sales require 5 follow-up calls after the meeting" claim
This is often bundled with the above but has an **independent** attribution chain: **The Brevet Group** (a US sales training/consulting firm, now rebranded/absorbed into SBI Growth — the original `blog.thebrevetgroup.com` URL 301-redirects to `sbigrowth.com`).

**Recovered at the successor URL:** `https://sbigrowth.com/insights/10-practical-sales-productivity-tips`, by **Brian Williams, PhD**, dated **May 16, 2016**:

> "80% of sales require 5 follow-up calls after the meeting. 44% of sales reps give up after 1 follow-up."

**No citation, source, or study is given on this page either.** Note this is a *different* breakdown from Marketing Donut's (a flat "44% give up after 1 follow-up," vs. Marketing Donut's cascading 44/22/14/12% across four nos) — two independent vendor content pieces asserting similar-sounding "it takes about 5 follow-ups" claims, with different supporting numbers, neither citing the other or any shared named primary. This looks like convergent folklore (the "5" and "80%" numbers feel authoritative and get reused) rather than one traceable lineage.

### Verdict + grade
**FOLKLORE, confirmed null result.** The single most-cited attribution point for the "92%/80%, four nos" statistic is itself an unsourced blog post that vaguely gestures at "different studies... different market research companies" without naming a single one, and the domain hosting it is now dead (recoverable only via Wayback). The related "80% of sales require 5 follow-up calls" claim traces to a second, equally uncited 2016 vendor blog post with a different, non-matching internal breakdown. Search paths tried: direct fetch/crawl of the Marketing Donut page (succeeded via Wayback, confirmed no citation), Brave Search for "MarketingDonut" + the exact phrase (returned only re-citations, never an upstream source), a follow-up Brave Search attempting to trace a "National Sales Executive Association" attribution some general sales literature associates with this genre (rate-limited by Brave before returning results — **not confirmed either way in this session**).

---

## Strip 5 (brief, per instructions — not chased beyond ~4 extra items)

- **"6-8 touches to generate a viable lead"**: one secondary source (impactmarketing.net) attributes this to "Salesforce," but this was not independently verified against a Salesforce primary in this session (Brave rate-limited before a targeted search could run). Flag as **unverified attribution**, not confirmed as either sourced or folklore.
- **"48% of salespeople never follow up"**: commonly repeated alongside the above; a targeted search to trace it (to the National Sales Executive Association, which some general sales literature associates with this genre) was **rate-limited before returning results**. Treated as an open null result, not a confirmed finding either way — do not repeat without further verification.

---

## Strip 6 — The Gong Labs claim genre (method-disclosure audit, not a single-claim debunk)

### What was checked
`https://www.gong.io/gong-labs` (landing page) and two dated Gong Labs blog posts found via the site's own blog listing (`https://www.gong.io/blog/`):
- `https://www.gong.io/blog/does-cold-email-even-work-any-more-heres-what-the-data-says`
- `https://www.gong.io/blog/data-shows-top-reps-dont-just-sell-they-orchestrate-with-ai`

### Findings, by the audit questions in the brief

**Landing page framing:** "Gong Labs is our original research engine. We turn billions of sales conversations, deals, and workflows into insights that help you spot buyer trends, benchmark performance, and stay ahead of where revenue is going." / "Our research is grounded in real-world data. Not opinions, anecdotes, or theory." The page has FAQ headers ("How does Gong Labs collect its data?", "How much data does Gong Labs research use?") but the answer content was not extractable from the crawlable page (likely a JS accordion) — i.e., even Gong's own explicit methodology FAQ could not be confirmed as substantively answered from what's crawlable without deeper JS interaction than this session pursued.

**Sample size disclosure:** Yes, always, and prominently — "we analyzed 28M+ cold emails with Gong" (cold-email post); "we analyzed 1.8 million new business deals closed in 2024" (AI-orchestration post). A large N is stated as a credibility signal in both.

**Sample construction disclosure:** No. Neither post explains the time period covered with precision, which customers/companies contributed data, industry or geography mix, or how the sample was selected/filtered. By construction, the corpus is **Gong's own paying customers' recorded calls and CRM-linked deals** — a self-selected population of companies that already bought a conversation-intelligence platform, skewing toward larger, better-resourced, process-mature sales orgs. This selection bias is never named or addressed in either post read.

**Base rates vs. relative lift:** Mostly relative lift is reported ("8.1x more meetings," "4.2x more replies," "130% increase in win rates," "42% increase in average win rate"), which is more attention-grabbing than informative without the base rate. One base rate is given in the cold-email post ("the average rep has to send 344 cold emails to land one meeting"); the deals post mixes in one absolute figure ("77% of [closed-won] deals are multi-threaded").

**Correlation vs. causation / confounds:** Not addressed in either post. The deals post states "closed-won deals include an average of 6.7 members of the sales team" without engaging the obvious alternative explanation — that larger, more-likely-to-close deals *attract* more team involvement, rather than more team involvement *causing* the win (reverse causation / confound of deal size and complexity). Neither post discusses controlling for deal size, industry, or rep tenure anywhere in the readable excerpt.

**Underlying data availability:** Not available. Both posts direct readers to "download the report" (a lead-gen gate), not to any independently auditable dataset.

### Verdict on the genre
Not a single-claim debunk but a consistent pattern: **large, real, disclosed N; undisclosed sample construction and selection bias; correlational findings reported as if actionable causal advice; no independent data access.** This is the genre's structural signature, confirmed across the two posts read plus the landing page's own framing. Chorus/Clari/Salesloft equivalents were not checked in this session (time/budget prioritized toward Strip 1).

---

## Strip 7 — Win-rate / close-rate benchmark genre

### What was checked
HubSpot's **"Sales Trends Report"** (2024 edition) PDF, read directly (`https://www.hubspot.com/hubfs/HubSpots%202024%20Sales%20Trends%20Report.pdf`), Chapter 5, "Sales Performance Benchmarks," p.26–27; plus a secondary source that itself analyzes the benchmark-comparability problem, `https://zenitdata.com/blog/b2b-saas-win-rate-benchmarks-by-deal-size-stage-and-segment-2026/`; plus a Brave Search survey of the genre.

### Findings
HubSpot's report presents, as a bare stat tile with **no denominator definition and no sample size on the page itself**:

> "21% — The average sales win rate" / "29% — The average sales close rate" — "based on 2023 performance," drawn from "surveyed sales pros" (mentioned generally elsewhere in the report; not re-verified for exact N in the pages read).

The zenitdata.com piece makes the genre's core problem explicit, comparing HubSpot's 21% against a different, unnamed "credible study" reporting 47%:

> "Both are correct. The difference is not the data but the denominator." / "Win rate calculated against all opportunities entered into a CRM will always be lower than win rate calculated against opportunities that reached the proposal or late stage."

A wider Brave Search scan turned up a spread of "the average win rate" figures — 21% (HubSpot, most re-cited), 29% (close rate, often conflated with win rate by re-citers), 33% (implied by a "3:1 pipeline-to-quota ratio" heuristic on martal.ca), 15–25% (landbase.com) — with at least one aggregator (prospeo.io) explicitly noting "HubSpot's benchmark of 21% 'hides massive variation.'" None of the pages checked disclosed, alongside the headline number, (a) the exact denominator (all CRM opps? SQLs? late-stage only?), (b) whether the figure is self-reported by survey respondents vs. pulled from CRM record data, or (c) the respondent/sample size on the same page as the figure.

### Verdict on the genre
A "benchmark win rate" is **not a single knowable, comparable number across companies** without first fixing the pipeline-stage denominator, the deal-size/segment cohort, and the self-report-vs.-system-of-record provenance — and the widely cited public benchmarks checked here do not make those choices explicit next to the headline figure. Comparing your own win rate to "the industry benchmark of 21%" without replicating HubSpot's exact denominator is close to a category error. This mirrors the report's own genre-aware secondary source (zenitdata.com), which is itself a useful citation for teaching the correction.

---

## Strip 8 — "Always Be Closing"

### Origin hunt
Checked Wikipedia's article on *Glengarry Glen Ross* (a reliable tertiary/encyclopedic source, not the primary script text itself — flagged as such) for the provenance of the "Always Be Closing" / "Coffee's for closers" speech.

### Findings
> The "Blake" character (the motivational-speaker role played by Alec Baldwin who delivers the ABC speech) **"does not appear in the play"** — David Mamet's original stage work (1983 London premiere / 1984 Broadway, Pulitzer Prize) does not contain this character or speech at all. It was written specifically for the **1992 film adaptation**. In the film itself, the character never states his name aloud — he "gives his name as 'Fuck You'" — the credits alone label him "Blake." Some amateur stage revivals have since retrofitted the film's scene back into productions, but it postdates and was never part of the original play.

### Verdict + grade
**SECONDARY / encyclopedic-confirmed**, not independently checked against Mamet's published script text in this session. The phrase's single most famous instance is a scene written for the film — delivered by a fictional, deliberately loathsome, unnamed-on-screen motivational-speaker character in a work that is a satire and critique of predatory, dehumanizing sales culture, not a sales-training endorsement. No verified pre-1992 sales-training usage of the literal phrase "Always Be Closing" was found or searched for with remaining budget; several current sales-training sites use "ABC" as if it were established wisdom, typically (when they source it at all) citing the film itself.

---

## Master table

| Claim | Commonly stated as | Earliest citable source | What it actually measured | Verdict |
|---|---|---|---|---|
| "57% of the buying decision" | "57%/60%/70% of the buying journey happens before contacting a supplier" | CEB/Google, *The Digital Evolution in B2B Marketing*, 2012 (survey fielded 2011, n=1,500) | Self-reported % of the purchase decision-making process completed before the customer's first serious engagement with a **supplier sales rep** (not "any contact with a supplier") | PRIMARY located; commonly-stated form is drifted/rounded |
| "60% of a typical purchasing decision" | Often merged with the above as if the same figure | Adamson/Dixon/Toman, "The End of Solution Sales," *HBR*, July–Aug 2012 (n=1,400 cited) | Restatement of a CEB finding, cutoff broadened to "before even having a conversation with a supplier" | SECONDARY (CEB-authored); a likely drift vector for 57%→60% |
| "Buyers spend only 17% of their time with suppliers" (5–6% per supplier) | Often cited alongside "57%" as reinforcing evidence for the same claim | Gartner, "B2B Buying Journey" insights page, captured via Wayback 2021-01-06 (attributed to Brent Adamson, Distinguished VP, Gartner) | % of total **buying time** spent meeting with potential suppliers overall / with any one supplier when comparing several — a time-allocation metric, not a decision-completion metric | PRIMARY located (via Wayback; live page has since been rewritten and no longer states it) |
| "It takes 8 touches to get a meeting" | Universal law of B2B prospecting | RAIN Group, "Top Performance in Sales Prospecting" (489 sellers + 488 buyers surveyed) | Vendor's own named, sampled — but not fully methodologically disclosed — study | VENDOR-SELF-REPORTED; genre broadly ranges 5–15 with most citing nothing |
| "92% of salespeople give up after 4 nos; 80% of prospects say no 4 times before yes" | Universal statistic proving persistence pays | Marketing Donut UK, "Why you must follow up leads" (site now dead, recovered via Wayback) | The article itself names no study — "different studies... different market research companies," unattributed | FOLKLORE (confirmed null: no primary found) |
| "80% of sales require 5 follow-up calls after the meeting" | Same genre, often bundled with the above | The Brevet Group / SBI Growth blog, Brian Williams PhD, May 2016 | No study cited; different internal breakdown (44% give up after 1) than Marketing Donut's | FOLKLORE (confirmed null: no primary found) |
| "6-8 touches to generate a viable lead" / "48% never follow up" | Same genre | Not resolved this session (Brave rate-limited) | Unknown | UNVERIFIED / open |
| Gong Labs "we analyzed N million calls, X correlates with Y% higher close rate" | Rigorous, data-driven proof of a sales tactic | Gong Labs blog posts (gong.io) | Large real N; undisclosed sample construction (Gong's own customer base, self-selected); relative lift over base rates; correlation presented without confound control; underlying data not public | VENDOR-SELF-REPORTED (genre-level, not a single-claim verdict) |
| "Average win rate is 21%" (HubSpot) / benchmark win-rate tables generally | A single comparable industry number | HubSpot Sales Trends Report 2024; contradicted/contextualized by other benchmarks (e.g., 47% at late-stage) | Denominator (all CRM opps vs. late-stage opps) not fixed across sources; sample/self-report basis not disclosed alongside the figure | VENDOR-SELF-REPORTED / CONTESTED (genre: not a single knowable number without matching denominators) |
| "Always Be Closing" | Timeless, earnest sales-training principle | *Glengarry Glen Ross* (1992 film only; not in Mamet's 1983/84 play) | A speech written for a **fictional, satirical** predatory-sales antagonist in the film adaptation | SECONDARY/encyclopedic-confirmed; genre often cites it as endorsement rather than critique |

---

## Candidate never-ship figures

For each: whether the reader needs to **recognize-and-correct** it (worth teaching the correction, because it's in wide enough circulation that omitting context would look like an error of omission) or should simply **never see it** (no correction is valuable enough to earn the real estate).

1. **"57% of the buying decision is complete before contacting sales" as a bare, uncaveated number.** — **RECOGNIZE-AND-CORRECT.** Too load-bearing and too famous to omit; the pack should state the real figure (57%, n=1,500, self-reported, "before engaging a supplier sales rep directly," CEB/Google 2011–12) and explicitly flag that the popular "60%/70%" and "buying journey" restatements are drift, not the finding.
2. **The Gartner 17% / 5-6% figure presented as confirming or extending the CEB 57% figure.** — **RECOGNIZE-AND-CORRECT.** The two numbers are both real and both traceable, but they measure different things (decision-completion vs. time-allocation) and share an institutional lineage (Adamson, CEB→Gartner) that makes the conflation tempting. Worth a sentence teaching readers these are not interchangeable.
3. **"92% of salespeople give up after 4 nos, but 80% of prospects say no 4 times before saying yes."** — **NEVER SEE IT**, full stop, or cite it only as a case study in unsourced folklore. No primary source exists; the single most-cited attribution point is itself an anonymous, now-dead blog post that names no study. There is no defensible version of this number to teach a correction around — the entire quantitative content is unverifiable.
4. **"80% of sales require 5 follow-up calls after the meeting."** — **NEVER SEE IT** as a standalone assertion, for the same reason as #3 (uncited vendor blog, no traceable primary, internally inconsistent with the similar-sounding Marketing Donut breakdown). If the pack wants to make the general point "most sales need more than one follow-up," make that qualitative claim without borrowing this specific, unsourced number.
5. **"It takes 8 touches to get a meeting" as a universal constant.** — **RECOGNIZE-AND-CORRECT.** Unlike #3/#4, there is a real, named, sampled study behind one version of this number (RAIN Group, 489 sellers). Worth teaching that a real study exists but that the genre's numbers range 5–15 with most vendors citing nothing, and that RAIN Group's own figure has an undisclosed operational definition of "touchpoint."
6. **Any Gong-Labs-style "N million calls show X correlates with Y% higher win rate" claim, cited as causal proof a tactic works.** — **RECOGNIZE-AND-CORRECT.** These posts are common enough in sales content that the pack should teach readers how to read them (real N, undisclosed customer-base selection bias, correlation without confound control, no public data) rather than either banning citation of Gong Labs outright or repeating its headline lift numbers uncritically.
7. **A bare "industry average win rate is 21%" (or any single benchmark win-rate figure) used as a target or comparison without restating the denominator.** — **RECOGNIZE-AND-CORRECT.** The number itself (HubSpot's 21%) is a real, attributable, if thinly documented, figure — the error is using it as if "win rate" were a single comparable metric across companies. Teach the denominator problem, not a ban on citing HubSpot.
8. **"Always Be Closing" invoked as an aspirational sales principle with no context.** — **RECOGNIZE-AND-CORRECT.** Cheap and valuable to fix: one sentence noting the line's most famous utterance is a fictional character in a 1992 film satirizing exactly the mentality the phrase is often used to celebrate, not a real sales methodology with an earnest training pedigree.
