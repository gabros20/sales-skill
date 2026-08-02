# Channel C report — the GitHub/OSS corpus

Lead: sales-lead-c (opus). Workers: 4 sonnet (C1–C4) + 3 lead gap-fill passes (C0, C0b, C0c).
Date: 2026-08-03. Pack: `sales` — 14th and final pack of the Digital Product Skills family.

**Raw files (nothing below lives only in this report):**

| File | Scope |
|---|---|
| `raw/_raw-c1-open-crms.md` | 8 open CRMs: stage models, fields, forecast features, upstream licences |
| `raw/_raw-c2-gitlab-handbook.md` | GitLab handbook deep-read: stages, MEDDPPICC, forecasting, handoffs, licence |
| `raw/_raw-c3-playbooks-ai-sales.md` | Playbooks/handbooks/awesome-lists + the AI-SDR wave |
| `raw/_raw-c4-calculators-vendor-claims.md` | Calculators + Gong/vendor-claim tracing + falsification targets |
| `raw/_raw-c0-lead-gitlab-gapfill.md` | Lead: the GitLab paths C2 left unread |
| `raw/_raw-c0b-lead-c3-followups.md` | Lead: Sourcegraph forecast doc in full, EspoCRM docs, PostHog licence verification |
| `raw/_raw-c0c-lead-incumbent-commercial-skills.md` | Lead: **23.6k★ incumbent that occupies our flagship** |

---

## 0. THE HEADLINE — read this before anything else

**A 23,656-star, MIT, health-clean repo already ships the forecast-honesty flagship this channel
was preparing to recommend.** `alirezarezvani/claude-skills` →
`commercial/skills/commercial-forecaster` (v2.8.0) exists to produce a
commit/best-case/pipe-only number *"without the theatre of a single undefended number,"* states
*"The assumption block is non-optional. If you remove it, the forecast becomes theatre,"* and
ships a runnable `bookings_forecaster.py`. Claiming novelty on forecast-honesty framing would
ship a defect. Full detail and the star-skepticism check (7/7 coverage, **zero flags**, F=0.82 —
the stars are real) in `_raw-c0c`.

**But the same repo hands us a better wedge, grep-verified across all 346 of its skills.** It
covers the RevOps/commercial-finance end of sales thoroughly — forecaster, deal-desk,
pricing-strategist, rfp-responder, commercial-policy, channel-economics, partnerships-architect,
contract-and-proposal-writer, revenue-operations, sales-engineer, cro-advisor — and has **zero**
coverage of the buying conversation and the deal system. A grep for
`discovery|qualif|meddic|bant|objection|demo|icp|win-loss|crm|stage|prospect|cold|outbound|
negotiat|close|territor|quota` over all 346 skill names returned three hits, **all belonging to
other disciplines**: `cold-email` under `marketing-skill/`, `demo-video` under `engineering/`,
`product-discovery` under `product-team/`.

So: **qualification, discovery calls, demo narrative, objection handling, sales stages with exit
criteria, CRM structure, ICP/account selection, win/loss, and both handoffs are absent from this
repo's 346 skills.**

**SCOPE DISCIPLINE — read this before treating that as a wedge.** That statement is verified for
**one repo**, not for the ecosystem. Channel A's census (`channel-a-report.md`) already found
other occupants of exactly this ground: a real 9-skill Apache-2.0 Anthropic/KWP sales pack, and
`awesome-copilot` reproducing MEDDICC letter-by-letter with zero attribution. Channel A also
recorded the precise self-correction that applies here — *"no incumbent ships win/loss" nearly
shipped on 7-repo evidence, falsified by census — deep-read of N repos is not a uniqueness
proof.* I am not repeating that mistake. **Channel C's contribution is a grep-verified coverage
map of the single largest repo, not a uniqueness claim.** Whether the buying conversation is
genuinely open across the ecosystem is Channel A's question to answer, and A's current verdict is
that **novelty is NOT available**.

---

## 1. What the OSS corpus DOES cover

**Real, published, enterprise sales process exists — from exactly two companies.**

- **GitLab** publishes the single best stage-gate artifact found anywhere in this research: 10
  named opportunity stages (`0-Pending Acceptance` → `7-Closing` → `Closed Won`, with `8-Closed
  Lost`, `9-Unqualified`, `10-Duplicate`), each carrying description, primary/secondary
  activities, **and an explicit Exit Criteria list**, verbatim and permalinked (`_raw-c2` §1).
  Qualification is **MEDDPPICC** — nine letters, two D's and two P's, verified against the page's
  own section headers, not against a search summary (`_raw-c2` §2). Also public: a
  segment-differentiated pipeline-aging automation (Large/PubSec day 45/90, Mid-Market 21/45, SMB
  7/15, auto-closing to `No Progression-Auto Close`), the marketing→sales lifecycle with
  operational SAO criteria for inbound and outbound separately, and a sales→success handoff that
  names the stage the CSM enters (3-Technical Evaluation or 4-Proposal), the stage responsibility
  transfers (Closed Won), and a $50K threshold that changes the handoff's formality.
- **Sourcegraph** publishes the forecast method GitLab keeps internal (`_raw-c0b` §2): a
  **two-level** taxonomy — opportunity-level Won/Commit/Best Case/Pipeline/Omitted, where Commit
  carries three named checkable conditions — and a separate roll-up level of Commit/Best
  Case/**Call**, with the source's own framing: *"If you consider the Commit as the floor and
  Best Case as the ceiling, then the Call is the number in between that you are forecasting as
  the most likely outcome."* Commit is summed from records; Call is what the rep *"feel[s] will
  come in."* A published forecast that is deliberately three numbers, and explicit that the
  headline one is a judgement rather than a derivation.

The two are near-perfect complements: GitLab publishes stages and gates the forecast; Sourcegraph
publishes the forecast and (in this file) not the stages. Both independently use **Clari**.

**Working open CRMs, with instructive designs** (`_raw-c1`): Odoo alone computes a real
algorithmic probability (Naive Bayes over the company's own won/lost history, mechanism
transparently documented including its smoothing correction) and alone models per-stage
requirements as a first-class field. EspoCRM computes a live weighted pipeline
(`amount × probability ÷ 100`). frappe/crm buckets every status into Open/Ongoing/Won/Lost and
tracks first-response SLA **on deals**, not just leads. atomic-crm ships a `Delayed` stage —
acknowledging a deal can stall without being lost. Twenty treats the whole schema as
user-editable metadata rather than a fixed sales model.

**One genuinely strong live company handbook**: PostHog's, 54 files under
`contents/handbook/growth/sales/`, actively maintained, covering discovery, ICP, lead scoring,
outbound, expansion, and a usage-threshold ($1,000/mo) PLG→sales handover (`_raw-c3`).

**Primary vendor-claim methodology, fully traced** (`_raw-c4` §3): Gong publishes its own
methodology disclosure in a JSON-LD FAQ block that readability extraction drops — recovered via
`curl` with a Chrome UA. It names the sample frame (*"5,000+ companies"* — its own customers) and
uses the word *"correlates"* — then in the same paragraph slides into causal license.

---

## 2. What the OSS corpus DOES NOT cover — the null-result pattern

This is the channel's most valuable output. Five nulls, each verified by a fetch, a grep, or a
status code, never by an empty search.

**N1 — Nobody publishes forecast accuracy. Nobody.** Three independent legs:
- GitLab: the forecasting handbook is `internal.gitlab.com`, verified 302→403 to sign-in; Sales
  KPIs are explicitly classified *"Not Public"*; survived checks across three separate files.
- Sourcegraph: publishes categories, definitions, cadence, tooling and the fields that feed the
  number — and no measurement of whether it was right.
- Eight open CRMs: no accuracy claim, verified by grepping the probability-computation code
  itself (Odoo's 2,890-line `crm_lead.py` grepped in full for `accuracy` — zero hits), not by
  keyword sweeps of unrelated files.
- The 23.6k★ incumbent forecaster: structures and discloses the forecast; measures nothing.

**Forecast method is publishable. Forecast accuracy is published by no one in this corpus.**
That asymmetry is the spine of the forecasting strip, and it does not depend on any vendor claim.

**N2 — Exit criteria are effectively unrepresentable in CRM tooling.** Of eight CRMs, exactly one
(Odoo) models per-stage requirements as a first-class field, **and it ships empty** — the seed
data sets no value on any of its four default stages. Every other CRM's stage is
`{value, label, position, [probability]}`. Verified by reading the actual stage/entity-definition
model file in each repo. **And it survives the vendor's own documentation**: EspoCRM's
`docs/general/pipelines.md` describes a stage as an entity mapped to a status value with an
ordering constraint, and nothing else (`_raw-c0b` §3). So GitLab's published exit criteria are a
*process* artifact that the *tool* ecosystem cannot express — a genuine gap the pack can name.

**N3 — There is no good open sales playbook on GitHub.** Hundreds of repos named
`sales-playbook`/`sales-handbook`, virtually all 0–2 stars, and they are empty scaffolds, prompt
packs using "playbook" as metaphor, or SEO content-mill output (the `annatran05022000-cpu/*` and
`laravelmail/*` families). Founder-led sales: four repos, all 0–1 star, all personal prompt
projects — that canon lives in essay form elsewhere. `awesome-sales` is dominated by Power BI
"Awesome Chocolates" tutorial projects, a pure name collision. Zapier and Buffer publish no sales
handbook on GitHub (both 404, verified). Reached via ~25 `ghrelay batch` shards over 2,060
deduplicated repos (`_raw-c3`).

**N4 — Sales math is not open-sourced, with one large exception.** C4's ~19 queries found nothing
above 1 star (`_raw-c4` §1). That headline is **now partially false**: the exception is
`bookings_forecaster.py` inside the 23.6k★ incumbent, missed only because grep.app was down
during C4's window. The corrected finding: *standalone* sales-math calculators are essentially
absent from GitHub; the one substantial artifact lives inside an agent-skill aggregator. And no
open-source artifact anywhere in this search **backtests** a stage-weighted or category-based
forecast against realised outcomes.

**N5 — No open CRM ships qualification structure.** No BANT/MEDDIC/MEDDPICC fields in any of the
eight, verified by reading every Lead/Deal/Opportunity field-definition file. Odoo's predictive
lead scoring is a generic classifier over admin-configured fields, not a qualification framework.

---

## 3. LICENSING LEDGER — every repo touched

Binding rule applied throughout: **the licence file at the upstream repo is authoritative, the
API lies, registry mirrors are never a shortcut, manifests count, a dangling pointer is not a
licence, list every licence file, cite current names.**

| Repo (current name) | Upstream URL | Licence file(s) READ | Verdict | Notes |
|---|---|---|---|---|
| twentyhq/twenty | github.com/twentyhq/twenty | root `LICENSE`; `packages/{twenty-ui,twenty-sdk,twenty-shared,twenty-client-sdk,create-twenty-app}/LICENSE` | AGPLv3 core + inline `/* @license Enterprise */` commercial files + MIT toolkit packages + a bespoke "Twenty Application Exception" (AGPLv3 §7) | **Badge = Other/NOASSERTION.** 3-way split invisible to the API |
| espocrm/espocrm | github.com/espocrm/espocrm | `LICENSE.txt` (+ vendored `client/fonts/inter/LICENSE.txt`, excluded as third-party) | AGPLv3 | composer.json `AGPL-3.0-or-later`; badge matches |
| **espocrm/documentation** | github.com/espocrm/documentation | **none — full tree grepped for `licen\|copying`, zero hits; README and mkdocs.yml also carry no licence** | **UNLICENSED — all rights reserved. TRAP.** | Code AGPLv3, docs unlicensed. See §4 |
| odoo/odoo (`addons/crm`) | github.com/odoo/odoo | root `LICENSE`; `addons/crm/__manifest__.py` | **LGPLv3** (Community) | **Badge = Other/NOASSERTION.** Enterprise edition: `odoo/enterprise` → 404, **UNVERIFIED**, no claim made |
| SuiteCRM/SuiteCRM (renamed from salesagility/SuiteCRM) | github.com/SuiteCRM/SuiteCRM | root `LICENSE.txt`; per-file header e.g. `modules/Charts/code/Chart_pipeline_by_sales_stage.php` | AGPLv3 **+ a binding §7(b) attribution clause** ("Powered by SugarCRM" / "Supercharged by SuiteCRM") that exists only in source headers | Badge matches coarsely, **cannot express §7(b)**. Rename verified |
| krayin/laravel-crm | github.com/krayin/laravel-crm | `LICENSE` | MIT | composer.json matches; badge matches |
| monicahq/monica | github.com/monicahq/monica | `LICENSE.md` | AGPLv3 | Not a sales CRM — zero deal/pipeline concept (full-tree grep) |
| marmelab/atomic-crm | github.com/marmelab/atomic-crm | `LICENSE.md` | MIT | Badge matches |
| frappe/crm | github.com/frappe/crm | root `LICENSE` | AGPLv3 | `install.py` header says "MIT License. See license.txt" → file does not exist. **Dangling pointer, NOT a second licence** |
| gitlab-com/content-sites/handbook | gitlab.com/gitlab-com/content-sites/handbook | root `LICENSE`; `content/handbook/about/handbook-usage.md` | **Dual-scope: MIT for "the GitLab Software" (site code), CC BY-SA 4.0 for handbook prose** | ShareAlike attaches to close derivatives — quote-with-attribution is safe, derivative assets inherit obligations |
| PostHog/posthog.com | github.com/PostHog/posthog.com | root `LICENSE` (only licence file in repo — full tree enumerated) | **Split inside one file**: everything outside `/contents/` proprietary ("do not duplicate… for commercial or non-commercial use"); `/contents/` under the **MIT permission grant** | **Badge = Other/NOASSERTION.** MIT **by text, not by name** — the words "MIT License" never appear. Lead-verified; path confirmed (54 files under `contents/handbook/growth/sales/`) |
| sourcegraph/handbook | github.com/sourcegraph/handbook | root `LICENSE` | Apache-2.0 | **Archived 2024-07-02**; README warns content may be incorrect. Historical snapshot only |
| basecamp/handbook | github.com/basecamp/handbook | none found (`LICENSE`, `LICENSE.md` absent from 16 files) | **UNLICENSED — TRAP** | Also out of scope: HR-only, no sales content |
| vladar107/awesome-sales-engineer | github.com/vladar107/awesome-sales-engineer | `LICENSE` | CC0 1.0 | Freely reproducible |
| Salesably/awesome-ai-agents-for-sales | github.com/Salesably/awesome-ai-agents-for-sales | none found | **UNLICENSED — TRAP** | Vendor's own marketing directory; cite taxonomy shape only |
| eracle/OpenOutreach | github.com/eracle/OpenOutreach | **`LICENCE.md`** (British spelling) | GPL-3.0 | **Badge = Other/NOASSERTION** purely because of the filename spelling |
| growchief/growchief | github.com/growchief/growchief | `LICENSE` | AGPL-3.0 | LinkedIn automation — ToS hazard |
| filip-michalsky/SalesGPT | github.com/filip-michalsky/SalesGPT | `LICENSE` | MIT | Stale ~23 months |
| zubair-trabzada/ai-sales-team-claude | github.com/zubair-trabzada/ai-sales-team-claude | `LICENSE` | MIT | Names BANT+MEDDIC in marketing copy — the citation trap |
| linvo-io/linvo-scraper | github.com/linvo-io/linvo-scraper | `LICENSE` | MIT | Scraping + anti-detection; stale |
| relaticle/relaticle | github.com/relaticle/relaticle | `LICENSE` | AGPL-3.0 | Open CRM w/ AI agents; not deep-read |
| iPythoning/b2b-sdr-agent-template | github.com/iPythoning/b2b-sdr-agent-template | `LICENSE` (read by lead) | **MIT — CONFOUNDED grade lifted** | Copyright "PulseAgent"; badge agrees |
| BatManUtd/ltv-cohort-kit | github.com/BatManUtd/ltv-cohort-kit | `LICENSE` | MIT | **Overlap flag: CAC-payback/LTV is growth's and success's** |
| santiagoceron10/revops-pipeline-forecasting | github.com/santiagoceron10/revops-pipeline-forecasting | `LICENSE` | MIT | Its own DESIGN.md calls its 3×/2× bands *"rule of thumb"* |
| cognis-digital/dealflow | github.com/cognis-digital/dealflow | `LICENSE` (COCL 1.0, read through §9) | **Custom non-commercial-only**, commercial use excluded, CLA relicensing clause | Not OSI, not redistribution-safe. **CITE ONLY** |
| AgentSpore/saascalc | github.com/AgentSpore/saascalc | `LICENSE` absent; `pyproject.toml` has no licence field | **No grant — all rights reserved** | Cite only |
| harshith-vaddiparthy/SaaSValuationCalculator | github.com/harshith-vaddiparthy/SaaSValuationCalculator | `LICENSE` absent; `package.json` read | **ISC via manifest** (manifests count) | Low value for this pack |
| luisminvielle/ote-calculator · Azeemaj101/Sales-Commission-Calculator · wsalinasVBAPro/Funnel-Model-Python | (see `_raw-c4` §5) | `LICENSE` absent in all three; no manifests | **No grant — all rights reserved** | Cite only |
| **alirezarezvani/claude-skills** | github.com/alirezarezvani/claude-skills | **RESOLVED — all SIX read** at SHA `aa8d778`: root `LICENSE`; `engineering-team/playwright-pro/`; `engineering-team/self-improving-agent/`; `engineering/collab-proof/`; `engineering/skillopt-sleep/`; `loop-library/` | **All six MIT — but FIVE distinct copyright holders**: Alireza Rezvani (root), Reza Rezvani ×2, dong7812, **Microsoft Corporation**, Forward Future | **Independently replicates A's 8th-clause candidate — treat *identical SPDX ≠ single owner* as CONFIRMED, not proposed.** `commercial/` has no licence of its own so the forecaster falls under the root grant, corroborated by its frontmatter. Terms are clear; **provenance is not** — a root MIT in one person's name above Microsoft-copyrighted subdirectories means blanket reliance is unsafe. Cite freely; per-directory check before adapting |

### Licensing lessons this channel established

1. **Four distinct mechanisms by which the licence API misleads**, all found here: a multi-way
   split reported as NOASSERTION (Twenty), a materially different obligation set hidden behind
   NOASSERTION (Odoo — LGPL, not AGPL/GPL/MIT), a two-halves-in-one-file split reported as
   NOASSERTION (PostHog), and a licence invisible because the file is spelled `LICENCE.md`
   (OpenOutreach). SuiteCRM adds a fifth shape that is not an API failure at all — an obligation
   living only in per-file source headers, which no badge system can represent.
2. **Vendor DOCS are systematically worse-licensed than vendor CODE.** EspoCRM's code is cleanly
   AGPLv3; its documentation repo has no licence file, no README statement, no mkdocs key. The
   natural inference "the project is open source, so its docs are too" ships a violation.
3. **Content repos are the trap category generally** — basecamp/handbook, Salesably, EspoCRM docs
   all unlicensed; GitLab and PostHog are the disciplined exceptions, and both had to be read
   carefully to learn *which part* is licensed how.
4. **GitLab redacted a third party's methodology itself.** Its public page states it adopted Force
   Management's Command of the Message and that *"Due to IP constraints, we have migrated content
   from this page to GitLab's internal Handbook."* An incumbent independently reaching our
   cite-never-reproduce posture — the strongest possible support for that standing rule.

---

## 4. Candidate never-ship figures

Applying **R21**: collect a figure only if the reader must recognise-and-correct it, its
arithmetic *is* the teaching, or both sides are permalinked.

| Figure | Status | What the primary actually says | Why it qualifies / how to ship it |
|---|---|---|---|
| **"57% of the buying decision is made before contacting sales"** | **TRACED, misquoted two ways — and INDEPENDENTLY CONFIRMED by Channel D-W2** | CEB Marketing Leadership Council, *The Digital Evolution in B2B Marketing* (2012, w/ Google), PDF via Wayback: *"57% — that's how far the average B2B buyer is through the purchase decision before engaging a supplier sales rep,"* n=1,500 contacts across 22 large B2B orgs, 10 industries; upper limit *"as high as 70%"* | **Recognise-and-correct, both sides permalinked.** Two distinct misquotes to teach: (a) **misattribution to Gartner** — Gartner acquired CEB in 2017, five years *after* this 2012 study; (b) **progress→completion conflation** — "57% *through the process*" becomes "the decision is already made," which the primary contradicts (43% remains on average). The study is methodologically defensible within its own stated scope; the folklore is downstream. **Two channels reached this independently (C via the Wayback PDF, D-W2 separately) — treat the trace as settled.** Channel A additionally frames 57% as one instance of a three-member folklore GENRE (with webdesign's "9 in 10 rule out before contact" and Shipley's "70–80% determined by capture work"); A's recommendation to teach the SHAPE rather than three separate strips should govern |
| **"3× pipeline coverage"** | **FOLKLORE** | No primary derivation located. Four candidate sources checked, all 404/no derivation. The one OSS repo that computes it labels its bands *"Health (rule of thumb)"* | **Its arithmetic IS the teaching.** `required_coverage = 1/win_rate`, and `1/0.33 ≈ 3`. "3×" is only correct at a ~33% win rate held fixed across the window. No source found states this next to the recommendation. Ship the identity, retire the number |
| **"Always Be Closing"** | **TRACED — lineage is the teaching; CONVERGES with Channel D-W2's independent trace** | Written by David Mamet for the **1992 film**; the character Blake and the ABC monologue **do not appear in the 1984 stage play** — invented for the adaptation to make sales pressure explicit | **Recognise-and-correct.** A satirical line from a deliberately unsympathetic antagonist in a film *critiquing* toxic sales culture, adopted earnestly as doctrine — inverting the source's intent. Every named methodology the pack cites rejects the posture |
| **Gong's "N million calls → X% more likely to close" genre** | **CORRELATIONAL, self-selected — and Gong discloses it** | Gong's own FAQ: research draws on *"5,000+ companies"* (its customer base) and says a technique *"correlates"* with higher win rates — then in the same paragraph implies causal license (*"because we measured it… not because reps told us it works"*) | **Recognise-and-correct, permalinked both sides.** Teach the frame, not one number: the sample is companies that bought a conversation-intelligence tool; no segment breakdown, no confidence intervals, no controls, no raw data. Best single exhibit: *"sellers that frequently use AI generate 77% more revenue"* (N=7.1M opportunities) — reverse causation and deal-size confounding are unaddressed |
| **"94% of buyers use AI before they talk to you"** | **MISATTRIBUTED at the source** | The 94% is **Forrester's** 2026 survey of ~18,000 buyers, cited *inside* a Gong article whose own trend figures (250%/280%/208%) carry no stated N | **Recognise-and-correct.** A reader citing "Gong says 94%" attributes a disclosed survey stat to Gong's telemetry corpus. Ships as a worked example of checking whose number is inside whose article |
| **"6–10 people in a B2B buying group"** | **TRACED, accurately quoted** | Gartner, verbatim via Wayback (live site 403s everything): *"six to 10 decision makers, each armed with four or five pieces of information they've gathered independently and must deconflict with the group"* | **Borderline under R21** — the figure is *not* misquoted, so it fails the recognise-and-correct test. What is routinely dropped is the second clause: the teachable point is information reconciliation inside the group, not headcount. Ship the clause, or don't ship the figure |
| **"It takes 8 touches to reach a prospect"** | **UNTRACED IN CHANNEL C — but Channel D has provenance. Use D's, do not re-chase** | Channel C could not locate it: C4's surfaces degraded (DDG CAPTCHA, Bing RSS serving unrelated geo-junk) and my retry via `lite.duckduckgo.com` with a Chrome UA was bot-blocked (HTTP 202, zero results). **Channel D-W2 found a named RAIN Group study of 489 sellers behind ONE version of the claim** | **Do NOT ship as debunked, and do NOT ship C's null.** C's failure was a tooling failure, not evidence of absence — and D has since found real provenance for one variant. Ship D's traced version with its scope, and note that the "8" circulates detached from whichever study produced it. Cross-channel: cite D, do not re-derive |
| **GitLab "3.5× pipe coverage"** | **UNVERIFIED — do not cite** | Surfaced only via an AI-search summary; could not be located on any page fetched directly. Both handbook pages that would carry it (Pipeline X-Ray, Pipeline Management Tools) **404** | Recorded so nobody re-introduces it |
| **GitLab "33% win rate"** | **Real but must not be upgraded** | Public GTM-resources capacity model: *"Win rate - 33%… This is a calculation only and should be used to set goals and plan"* | Ship only as *"a planning-only assumption, explicitly not a measurement."* Rendering it as "GitLab's forecast is 33% accurate" misrepresents the source |

---

## 5. Recommendations to synthesis

1. **Do not claim novelty on forecast honesty.** It is occupied by a 23.6k★ MIT incumbent with
   near-identical framing. Differentiate on what it doesn't do — solo-scale existence gate, and
   the accuracy nobody measures — or move the flagship.
2. **Channel C offers a coverage map, not a wedge.** Within the largest repo the RevOps/finance
   end is well covered and the buying conversation is grep-verified absent. **Do not promote that
   into "the buying conversation is open"** — Channel A's census found other occupants of that
   exact ground (Anthropic/KWP's 9-skill Apache-2.0 sales pack; `awesome-copilot`'s MEDDICC
   reproduction) and A's verdict is that novelty is not available. Combine C's map with A's
   census before any wedge is stated.
2b. **A cross-channel corroboration worth chasing.** Channel A found that this same repo attributes
   a 30-cell stage table to "KeyBanc/OpenView/Bessemer" with no link and then **executes it as
   Python priors**. Channel C independently found its `bookings_forecaster.py` carrying a stated
   **70/30 last-4Q/last-12Q weighting** and per-stage conversion assumptions. These are very
   likely the same artifact seen from two sides — an unciteable figure compiled into running
   code. If so it is the family's sharpest example yet of *the genre adopting the form of
   citation without the function*, and it deserves to be one exhibit, jointly owned by A and C,
   rather than two half-findings.
3. **The strongest teachable asset pairing is GitLab + Sourcegraph**: published exit criteria per
   stage, plus a forecast expressed as floor/ceiling/judged-middle where the headline number is
   openly a judgement. Both permalinked, both licence-clean for quotation (CC BY-SA 4.0 and
   Apache-2.0), with the Sourcegraph staleness caveats attached.
4. **Ship the "estimated until quoted" exhibit** (GitLab's Net ARR source table) — it teaches a
   real precision limit without relying on any vendor's claim.
5. **The sales↔success seam gains a worked example, not an adjudication.** GitLab's CSM tracks
   renewals and schedules two reviews at 5 and 3 months; the AE runs the expansion engagement and
   presents pricing. Matches our provisional split — but GitLab's own text insists the roles *"run
   parallel"* and that expansion strategy is decided jointly, so the "run parallel" sentence must
   travel with any citation or we would be citing a source that refuses to draw the line we drew.
6. **Tell the marketing-seam owner**: the largest incumbent files `cold-email` under
   `marketing-skill/` — independent empirical support for marketing's shipped claim that the genre
   blends outbound into marketing.

---

## 6. Coverage statement — what was NOT searched

**Search surfaces per claim area.** Repo discovery, licences, CRM internals and the incumbent
census: `ghrelay` and `gh api`/`gh search` against live GitHub — **unaffected by the outage**, so
those nulls are trustworthy. GitLab handbook: GitLab's public REST API plus `curl` of raw
markdown (rendered `handbook.gitlab.com` pages returned nav-only content to WebFetch and were
abandoned). Vendor claims: direct WebFetch, `curl` with a Chrome UA for 403s, and `web.archive.org`
for Gartner and the CEB PDF. **WebSearch was quota-dead (200/200) session-wide**; per the
controller's ruling, no null in any Channel C raw rests on it — C2 used it twice before quota
death and both leads were independently re-confirmed against primary sources or explicitly graded
UNVERIFIED; C1, C3 and all lead passes never used it.

**Not covered:**
- ~~The incumbent's root `LICENSE` text~~ — **CLOSED.** All six licence files read at a pinned
  SHA; see the ledger row. Terms resolved (MIT throughout); provenance explicitly not resolved
  and flagged as the remaining risk before adaptation.
- **The incumbent's actual skill quality** — I read `commercial-forecaster/SKILL.md` and the
  script's dataclass. `deal-desk`, `pricing-strategist`, `rfp-responder`, `commercial-policy`,
  `channel-economics`, `partnerships-architect`, `sales-engineer`, `revenue-operations`,
  `cro-advisor` were identified by name only. A depth assessment is needed before the census
  concludes how good the incumbent actually is.
- **Twenty's `/* @license Enterprise */`-marked files** — mechanism confirmed, files not enumerated.
- **Odoo Enterprise** — no public repo exists to verify; no claim made about its terms.
- **GitLab**: `sales-operating-procedures/deal-closure.md`, `facilitate-the-opportunity.md`, and
  the `engage-and-educate-the-customer/` subtree (tree fully enumerated, so this is a bounded
  gap); the Enterprise playbook subtree; `training/`; `command-of-the-message/metrics.md` and
  `proof-points.md`.
- **PostHog**: `lead-scoring.md`, `product-led-lead-qualification.md`, `who-we-do-business-with.md`
  (ICP), `expansion-and-retention.md`, `outbound-sales.md` identified but not deep-read — the
  richest unmined seam left in this channel.
- **Sourcegraph**: only `forecasting.md` was read in full; ~50 other sales files exist, most
  dependent on dead internal dashboard links.
- **Additional CRMs ranked but not deep-read**: Django-CRM, Huly, NocoBase, relaticle, wacrm,
  CordysCRM.
- **grep.app code lane** was used once successfully (and it overturned a headline). Other tokens
  — `coverage_ratio`, `win_rate`, `weighted_pipeline`, MEDDIC/BANT field names — were never
  probed. **Given what one probe found, this lane is under-exploited and should be re-run.**
- **"8 touches"** — untraced in Channel C after two blocked attempts on different surfaces.
  **No longer a family gap**: Channel D-W2 found a named RAIN Group 489-seller study behind one
  variant. Cite D; C should not re-chase it.
- Non-English playbooks; Salesforce's own documentation on standard forecast categories (needed
  to settle whether Commit/Best Case/Pipeline/Omitted originates with Salesforce or Clari — an
  open question this channel explicitly declined to assert either way).
