# A2 — Deep-read of top sales/GTM incumbents

Worker A2, Channel A (skills-ecosystem census). Mission: actually read the content of the
biggest sales/GTM skill packs, not their descriptions. All fetches via
`raw.githubusercontent.com` (confirmed-working recipe) or `gh api`, both same-session,
2026-08-02/03. Every repo's default branch, star count, and last-push date recorded via
`gh api repos/<owner>/<repo>`.

---

## 1. refoundai/lenny-skills

**Repo:** MIT license (`LICENSE` at repo root, standard MIT text, copyright Refound AI 2025).
main branch, **1,212 stars**, last pushed 2026-07-16.

**IMPORTANT — charter mismatch:** the charter expected six sales skills (`founder-sales`,
`sales-qualification`, `enterprise-sales`, `product-led-sales`, `building-sales-team`,
`sales-compensation`). The **current `main` branch tree has only three**:
`skills/founder-sales`, `skills/enterprise-sales-motion`, `skills/plg-sales-integration`.
The repo's own README (fetched from `main`) self-describes as **"2.0"** — "76 product
management and engineering skills... Organized as a product operating model" — i.e. it was
restructured/renamed since whatever snapshot the breadth sweep or skills.sh indexed. Proof
that skills.sh is stale here: `curl skills.sh/api/search?q=sales-do` still returns
`refoundai/lenny-skills/product-led-sales` with 1,697 installs — a skill folder that **does
not exist** on the current `main` tree. **Flag for the lead: any install-count citation for
this repo's sales skills needs the commit/version pinned, or it is citing content that no
longer exists.**

**Structure:** router-lite — each skill is `SKILL.md` (auto-loaded framework) +
`references/artifacts.md` (full template/framework list) + `references/guest-insights.md`
(every sourced quote). Genuine progressive disclosure. Sizes: founder-sales SKILL.md ~84
lines / artifacts ~140 lines / guest-insights ~110 lines; enterprise-sales-motion SKILL.md
~97 lines / artifacts ~410 lines / guest-insights ~575 lines; plg-sales-integration similar
scale.

**Citation practice:** the best-cited incumbent found in this census. Every "Core Principle"
quote in every SKILL.md is attributed by name and backed by a `references/guest-insights.md`
entry with a **direct YouTube link + timestamp** or **Lenny's Newsletter URL**. E.g.
`skills/founder-sales/references/guest-insights.md:242` — Jason Lemkin quote sourced to
`youtube.com/watch?v=I-R1bc1rlFs @ 01:27:28`. This is real sourcing — but every source is a
**secondary source** (podcast interview or newsletter opinion piece), never a primary dataset
or published study. MEDDIC is summarized as a template with an explicit external reference —
`skills/enterprise-sales-motion/references/artifacts.md:183` — "Reference:
lucidchart.com/blog/close-more-deals-with-meddic-sales-process" — i.e. cited to a third-party
blog, not reproduced from paid MEDDIC training material. Lower trademark-reproduction risk
than awesome-copilot's version (see §2).

**Scope vs. charter's 14 includes:** covers founder-led sales assessment, discovery volume,
objection handling (light), some pricing/comp (Sales Comp Plan Aligned to Retention,
`enterprise-sales-motion/references/artifacts.md:228`), MEDDIC as one listed template, PLG↔
sales handoff triggers (PQL signals). **Absent:** no dedicated forecasting skill, no
win/loss-learning skill (closest is "Leave No Deal Behind Campaign Checklist" — a
re-engagement tactic list, not a root-cause/learning process,
`enterprise-sales-motion/references/artifacts.md:333`), no CRM-structure skill, no dedicated
qualification-framework skill (MEDDIC appears only as one bullet inside
enterprise-sales-motion, never as its own skill — unlike the charter's expected
`sales-qualification`, which does not exist in the current tree), no discovery-call-specific
skill, no sales→success handoff content anywhere.

**Quality:** genuinely high. Concrete, named, falsifiable-in-principle tactics — "The
Collison Install" (`founder-sales/SKILL.md:53`), "The $1 Invoice Test," specific ARR figures
per named company at first-sales-hire ("Zip $200k ARR (4th employee), Hex $250k (8th)...",
`founder-sales/references/artifacts.md:127`). Not generic filler — reads as genuinely
distilled from real interviews.

**Agentic posture:** pure advisor. No asset generation, no CRM writes, no templates meant to
be executed by the agent — it's decision-support for a human.

**License:** MIT, `LICENSE` file present at repo root, clean single-license repo.

**VERDICT: MEDIUM threat.** Deepest, best-cited founder-led-sales and enterprise-transition
content in the census — directly overlaps charter item 4 (founder-led sales canon). But it
leaves forecasting, win/loss, CRM structure, and qualification frameworks completely open,
and every citation is secondary-source opinion, never primary evidence — exactly where our
wedge (evidence-graded methodology claims) applies.

---

## 2. github/awesome-copilot — `gtm-*` family

**Repo:** MIT license, main branch, **37,357 stars**, last pushed 2026-08-01 (i.e. the day
before this research, extremely active).

**Tree:** 11 `gtm-*` skills under `skills/` (charter said "12+"; confirmed count is 11):
`gtm-0-to-1-launch`, `gtm-ai-gtm`, `gtm-board-and-investor-communication`,
`gtm-developer-ecosystem`, `gtm-enterprise-account-planning`, `gtm-enterprise-onboarding`,
`gtm-operating-cadence`, `gtm-partnership-architecture`, `gtm-positioning-strategy`,
`gtm-product-led-growth`, `gtm-technical-product-pricing`. Each is a **single monolithic
SKILL.md** (300–570 lines), no `references/` subfolder — one dump per skill, not
progressive disclosure.

**Provenance:** every gtm-* skill's frontmatter names a single external author — `metadata:
author: Smit Patel, source: https://github.com/beingsmit/technical-product-gtm` — a
**40-star personal repo** (MIT, confirmed via `gh api repos/beingsmit/technical-product-gtm`)
ported wholesale into the 37k-star awesome-copilot collection.

**Read in full:** `gtm-enterprise-account-planning` (429 lines), `gtm-technical-product-pricing`
(353 lines), `gtm-product-led-growth` (339 lines). Skimmed `gtm-operating-cadence` (420
lines) and `gtm-ai-gtm` (569 lines) for scope/figures.

**Citation practice: zero external citations across all five files read.** Every claim is
first-person practitioner narrative presented as universal rule: *"I've never seen a deal
close with a stale MAP. Not once in 11 years"* —
`skills/gtm-enterprise-account-planning/SKILL.md:65-66`. This pattern repeats in every file
("What I Learned Running Both Motions in Parallel," "The Pricing Conversation I Wish I'd Had
Earlier") — confident, specific, completely unverifiable single-author anecdote.

**MEDDICC reproduced in full, zero source:** `gtm-enterprise-account-planning/SKILL.md:234-241`
defines all seven MEDDICC letters (Metrics, Economic Buyer, Decision Criteria, Decision
Process, Identified Pain, Champion, Competition) as "Component 3: Opportunity Plan
(MEDDICC)" with **no external reference at all** — more concerning than Lenny's version
(§1), which at least cites a blog. Not verbatim reproduction of trademarked training
materials (the definitions are the same short public-domain-style glosses found on
Wikipedia/most sales blogs), but a first-class, unattributed framework reproduction.

**Scope:** enterprise account planning (MAP, EB validation, stage gates), pricing strategy
(seat/usage/outcome models, freemium thresholds, enterprise pricing conversation, when to
raise prices), PLG vs. sales-led selection, operating cadence (meeting architecture,
weekly/quarterly planning — cross-functional, not sales-specific), and "AI GTM" —
**but `gtm-ai-gtm` is about positioning/selling AI *products*, not about using AI *to* sell**
(charter item 6 is the AI-SDR/outbound wave — a real scope mismatch/gap here). No
forecasting skill for sales pipeline (growth forecasting appears only inside
`gtm-product-led-growth` §6 as marketing-channel forecasting, not deal forecasting). No
win/loss skill (mentioned only as a quarterly-planning input, one bullet,
`gtm-operating-cadence/SKILL.md:1292`). No marketing→sales or sales→success handoff content.

**Quality:** well-organized, decision trees, "Common Mistake" callouts, quick-reference
sections — genuinely readable. But every specific number (Value Ratio thresholds, 40% win
rate, "$5K→$50K inflection") comes from one person's unverifiable experience, stated with the
same confidence as a benchmark study.

**Agentic posture:** advisor/framework only — decision trees for the human to apply, no
asset generation or write actions.

**License:** MIT at repo root; each individual skill's frontmatter also declares
`license: MIT`.

**VERDICT: HIGH threat.** Largest single-repo GTM content library in the census (37k stars,
pushed same week), directly overlaps enterprise account planning, pricing presentation, and
PLG-motion scope — but is entirely single-author anecdote with zero sourcing for aggressive
numeric claims. Exactly the shape of incumbent our wedge (evidence-graded, source-linked
methodology) should out-position.

---

## 3. sales-skills/sales — **NOT RETRIEVABLE**

`gh api repos/sales-skills/sales` → `404 Not Found`. `gh api repos/sales-skills` (org) →
`404 Not Found`. `curl -I https://github.com/sales-skills/sales` → `HTTP/2 404`. `gh search
repos` for "sales" and "sales-do" does not surface an org named `sales-skills` anywhere in
the top 30 results.

The repo unambiguously **did exist and was indexed**: `curl skills.sh/api/search?q=sales-do`
returns `{"id":"sales-skills/sales/sales-do","skillId":"sales-do","installs":323,"source":
"sales-skills/sales"}`, and `gh search code "sales-do" --filename SKILL.md` surfaces multiple
**third-party repos** whose own SKILL.md files instruct users to install it —
e.g. `aibot88/sec_skill_store:skills/claudskills/sales-unboxd/SKILL.md`: `` `npx skills add
sales-skills/sales --skill sales-do -a claude-code` ``, repeated across a dozen files in that
repo.

**Conclusion: the repo has been deleted, made private, or transferred/renamed since being
indexed.** Cannot assess structure, citation practice, scope, quality, agentic posture, or
license — do not infer content from the name or from third-party references to it. Flag for
the breadth-sweep worker: this may be evidence of churn in the niche (packs appearing and
disappearing), worth a note in the census methodology.

**VERDICT: N/A (not retrievable) — no threat assessment possible.**

---

## 4. anthropics/knowledge-work-plugins — OFFICIAL Anthropic

**Repo:** Apache-2.0 (`LICENSE` at repo root; each plugin subfolder — including `sales/` and
`small-business/` — also carries its own `LICENSE`, all Apache-2.0, confirmed by fetching
`sales/LICENSE` directly), main branch, **23,252 stars**, last pushed 2026-08-02 (i.e. the
day this research ran — actively maintained by Anthropic).

**Correction to charter's scope:** the charter only knew of `small-business/skills/sales-brief`,
`crm-cleanup`, `crm-maintenance`. There is also a **full, separate `sales` plugin** with 8
skills: `account-research`, `call-prep`, `call-summary`, `competitive-intelligence`,
`create-an-asset`, `daily-briefing`, `draft-outreach`, `forecast`, `pipeline-review`. This is
materially bigger than what the charter described and directly hits our flagship candidate
(forecasting).

**Structure:** each skill/command is single-file (168–440 lines), template-heavy, following a
consistent "STANDALONE (always works) / SUPERCHARGED (MCP-connected)" pattern. No
`references/` folders in the `sales` plugin. `small-business/skills/crm-maintenance` is the
exception — it has a genuine `reference/` folder (`hubspot-fields.md`, `cleanup-checklist.md`,
`gotchas.md`, worked examples) — the most rigorously engineered single skill found in this
whole census.

**Read in full:** `sales/skills/forecast/SKILL.md` (214 lines), `sales/skills/pipeline-review/
SKILL.md` (245 lines), `small-business/skills/crm-cleanup/SKILL.md` (58 lines),
`small-business/skills/crm-maintenance/SKILL.md` (68 lines), `small-business/skills/
sales-brief/SKILL.md` (partial, ~150 lines).

**Citation practice:** zero citations anywhere — but this is templated productized tooling,
not argumentation, so the absence reads differently than in §1/§2. The forecast skill's
**default stage-probability table is asserted with zero backtest or source**:
`sales/skills/forecast/SKILL.md:186` header "Default Probability" → Prospecting 10%,
Discovery 20%, Evaluation 40%, Proposal 60%, Negotiation 80%, Closed Won 100%. Immediately
followed by "Tell me if your stages or probabilities are different" — a partial honesty
mitigation (invites override), but the defaults themselves are unexplained folklore numbers.
Also unsourced: **"3x pipeline coverage is healthy. Below 2x is risky"** —
`sales/skills/forecast/SKILL.md:213`. And in `pipeline-review/SKILL.md`, a bare
un-sourced prioritization weighting: Close Date 30% / Deal Size 25% / Stage 20% / Activity
15% / Risk 10% (no line-numbered header but appears under "## Prioritization Framework").

**Scope:** `forecast` is the only dedicated **sales pipeline forecasting** skill found in the
entire census (direct hit on charter item 5, the flagship candidate) — best/likely/worst
scenarios, commit-vs-upside, gap analysis, all templated. `pipeline-review` covers deal
health scoring, stale/stuck-deal detection, hygiene audit, single-threading risk.
`small-business/sales-brief` is **not** a B2B sales-motion skill despite its name — it is a
retail/e-commerce revenue-and-content-marketing tool ("PUSH THESE (winners) / CLEAR THESE
(slow movers)" content calendar, pulling PayPal/QuickBooks/HubSpot data,
`small-business/skills/sales-brief/SKILL.md:1-15`) — a naming trap worth flagging.
`crm-cleanup`/`crm-maintenance` are pure CRM-hygiene execution with genuinely strong approval
gates ("Never delete records," "Never change deal stage... without explicit approval,"
"Side-by-side diffs... wait for approval per item" — `crm-maintenance/SKILL.md`, Approval
gates section). **Absent from the whole `sales` plugin:** no qualification framework, no
win/loss learning, no discovery-call skill, no objection-handling skill, no pricing
presentation skill — it is pipeline/ops-focused, not deal-conversation-focused.

**Quality:** genuinely well-engineered as a product (this is a live Anthropic/Cowork feature,
not a hobby repo) — but the forecasting methodology itself is exactly the kind of
un-vetted, hand-set heuristic our flagship should interrogate rather than copy uncritically.

**Agentic posture:** strongly agentic-as-doer, but tightly gated. `draft-outreach` drafts
actual emails/LinkedIn messages; `crm-maintenance` writes CRM records but only after explicit
per-item approval; `create-an-asset` generates decks/pages. This is the **highest-discipline
approval-gate pattern found in the census** — worth citing as a positive bar to match, not
just critique.

**License:** Apache-2.0, `LICENSE` at repo root and mirrored per-plugin (`sales/LICENSE`,
`small-business/LICENSE` — did not fetch small-business's copy directly but repo-root
Apache-2.0 applies uniformly per standard practice; flag for the licensing worker to
independently verify the small-business plugin's own LICENSE file, not just the repo root).

**VERDICT: HIGH threat on execution/CRM-ops surface** (official, live, best-gated agentic
pattern found) **but a real coverage gap on sales methodology** — no qualification, no
win/loss, no discovery, no objection handling, and the one forecasting skill ships
unexplained default probabilities. This is the official floor the charter asked us to find,
and it sets that floor much higher on execution discipline than on sales-methodology depth.

---

## 5. hubspot/agent-cli-skills

**Repo:** Apache-2.0, main branch, **18 stars**, last pushed 2026-07-23 — small, low-traction
vendor pack.

**Tree:** 4 skills, all short: `crm-data-quality` (100 lines), `crm-lookup` (99 lines),
`sales-execution` (121 lines + a `resources/activity-properties-reference.md`),
`sales-reporting` (140 lines). Read all four in full.

**Content: 100% CLI/API reference documentation.** Every line is `hubspot` CLI syntax, `jq`
pipelines, HubSpot property names (`hs_call_title`, `hs_timestamp` format gotchas between
write/read paths), pagination rules, dry-run/digest/confirm safety patterns. **Zero selling
methodology, zero sales strategy, zero citations** — there is nothing to cite; it is
technical reference material, not argumentation.

**Confirms the charter's hypothesis exactly:** the "win/loss analysis" section in
`sales-reporting/SKILL.md` (§3, "Win/loss analysis") is literally a `jq` script that counts
`hs_is_closed_won=true` vs. `hs_is_closed=true AND hs_is_closed_won!=true` records and
computes a win rate percentage by rep — **no loss-reason capture, no root-cause analysis, no
learning process.** It calls itself "win/loss analysis" but is pure closed-deal counting.
Same for `sales-execution`'s "log activities" — it is CRM data entry, not sales technique.
**This is the clean confirmatory example: it drives the HubSpot API, it does not teach
selling.**

**Scope:** CRM lookup, data hygiene (dedupe, missing fields), activity logging (calls,
notes, meetings, tasks with mandatory create-then-associate step), and reporting (daily
briefing, pipeline snapshot, win/loss counts). No qualification, no discovery, no objection
handling, no pricing, no forecasting methodology (only raw deal aggregation).

**Quality:** as technical CLI documentation, genuinely solid — correctly documents real
HubSpot API gotchas (timestamp format mismatches between write and read paths, `~` being
token-match not substring-match, pagination truncation at exactly 100 rows). Not filler, but
also not a sales-methodology competitor at all.

**Agentic posture:** doer, not advisor — every skill exists to make HubSpot API calls. No
approval-gate discipline comparable to Anthropic's pack (§4) — e.g. `sales-execution` creates
calls/notes/meetings/tasks and associates them without a described human-approval step.

**License:** Apache-2.0, `LICENSE` at repo root.

**VERDICT: LOW threat.** Does not compete on sales methodology or strategy at all — it is
pure CRM-API tooling. Useful as a contrast case: shows what "drives the CRM" looks like when
completely separated from "teaches selling," and its "win/loss analysis" naming mismatch
(count of outcomes ≠ learning from outcomes) is a good illustrative example for our
win/loss-learning wedge.

---

## 6. coreyhaines31/marketingskills — `sales-enablement` (+ `revops`)

**Repo:** MIT, main branch, **42,757 stars** — the single largest star count in this entire
census, matching the charter's note that this is "the biggest single number in the field."
Last pushed 2026-07-29.

**Already adjudicated as the marketing incumbent by the marketing pack** (per charter). My
task here is narrower: does `sales-enablement` claim genuine SALES scope, and how deep is it?
I also found and read a second, directly-relevant skill, `revops`, not named in the charter.

### sales-enablement

**Structure:** genuine router — `SKILL.md` (359 lines) + 4 reference files:
`deck-frameworks.md` (263 lines), `demo-scripts.md` (355 lines), `objection-library.md` (270
lines), `one-pager-templates.md` (208 lines). Also has an `evals/evals.json` — the only
incumbent found with an explicit eval harness. Read `SKILL.md` and `objection-library.md` in
full.

**Content:** genuinely broad, genuine sales-conversation-support scope — sales decks (10-12
slide framework, buyer-type customization table), one-pagers, **full objection-handling
library** with a quick-reference table plus detailed talk tracks per objection ("Why they say
it" / "Response approach" / "Talk track" / "Proof point" / "Follow-up question" — e.g. "It's
too expensive," `references/objection-library.md`), ROI calculator design, demo scripts by
call type, sales case-study briefs, proposal templates, sales playbooks (mentions
"BANT, MEDDIC, or your framework" only in passing — `SKILL.md`, "Sales Playbooks" section —
**not reproduced**, lower risk than awesome-copilot's full MEDDICC breakdown), and buyer
persona cards.

**Citation practice:** zero primary citations — but this is prescriptive template/framework
content (how to structure a deck, how to phrase an objection response), not factual/numeric
claims, so the absence of sourcing is a different category of gap than §1/§2/§7's anecdote
problem.

**Quality:** genuinely useful, practitioner-grade, well-organized. Not filler.

**Agentic posture:** advisor/generator — helps create collateral, no CRM execution.

### revops (not named in charter, directly relevant to our scope)

**Structure:** router — `SKILL.md` + 4 reference files (`automation-playbooks.md`,
`lifecycle-definitions.md`, `routing-rules.md`, `scoring-models.md`). Read `SKILL.md` in
full.

**This directly overlaps charter items — CRM structure, pipeline management, marketing→sales
handoff.** Covers: lead lifecycle stages (Subscriber→Lead→MQL→SQL→Opportunity→Customer→
Evangelist, with owner column), MQL definition (fit + engagement, never either alone), MQL→SQL
handoff SLA (4-hour contact, 48-hour qualify/reject), lead scoring model construction,
lead routing methods (round-robin/territory/account-based/skill-based), **full pipeline stage
table** (Qualified→Discovery→Demo/Evaluation→Proposal→Negotiation→Closed Won/Closed Lost,
with required fields and exit criteria per stage — nearly identical shape to what our charter
calls "CRM structure" + "pipeline management"), stage-hygiene rules, deal-desk
approval-tier table by discount size, CRM automation workflow list, data hygiene/dedup
strategy, and a **RevOps metrics benchmark table** — all unsourced: Lead-to-MQL 5-15%,
MQL-to-SQL 30-50%, SQL-to-Opportunity 50-70%, Win rate 20-30%, LTV:CAC 3:1-5:1, Coverage
ratio "target 3-4x," `skills/revops/SKILL.md` (RevOps Metrics Dashboard table). Also contains
the classic speed-to-lead folklore figure: **"Contact within 5 minutes = 21x more likely to
qualify (Lead Connect)"** — `skills/revops/SKILL.md:143` — a well-known, often-misattributed
statistic (commonly traced, with varying fidelity, to a 2007 MIT/InsideSales.com study; here
attributed only to "Lead Connect," no link).

**Cross-check against the marketing pack's own shipped claim:** I independently verified —
by reading `revops/SKILL.md` and `sales-enablement/SKILL.md` directly, not just their
descriptions — that the marketing pack's cession is accurate. `marketing-skill/skills/
marketing/references/handoff.md:42` states "Revenue operations, sales enablement (battlecards,
objection handling)... are `sales`'s, not marketing's... because the incumbent genre
routinely blends these into marketing and the family's seam is only real if stated." This is
**confirmed true, not contradicted**: both skills are real, substantial, and were correctly
identified and ceded rather than absorbed. No conflict to flag — this is a positive
cross-channel consistency check.

**License:** MIT, `LICENSE` at repo root, single clean license.

**VERDICT: MEDIUM-HIGH threat.** `sales-enablement` is a full, well-structured,
genuinely-in-scope sales-conversation-support skill in the single biggest-star repo found in
the whole census. `revops` directly overlaps CRM-structure/pipeline-management scope with a
rich unsourced-benchmarks table — the richest source of candidate never-ship figures for the
CRM/pipeline slice specifically (not overlapping with the sales/GTM AI-SDR figures found
elsewhere).

---

## 7. gtmagents/gtm-agents, chadboyda/agent-gtm-skills, Cold-IQ/ColdIQ-s-GTM-Skills

### gtmagents/gtm-agents

**Repo:** Apache-2.0, main branch, **361 stars**, last pushed 2026-04-03 (staler than the
others — ~4 months old relative to today). Enormous multi-plugin repo spanning far beyond
GTM/sales: `abm-orchestration`, `account-management`, `analytics-pipeline-orchestration`,
`b2b-saas`, `brand-strategy`, `sales-prospecting`, `video-marketing`, and many more plugins.

Read in full: `plugins/sales-prospecting/skills/cold-outreach/SKILL.md` (short, ~35 lines)
and `plugins/video-marketing/skills/scriptwriting/SKILL.md` (~30 lines). Both are short,
templated, formulaic ("Framework / Templates / Tips" repeated verbatim across unrelated
topics), zero citations, unsourced target benchmarks (cold-outreach: "watch ≥30% opens, ≥10%
replies," no source). Pattern strongly suggests templated/LLM-generated-at-scale content
rather than practitioner-authored depth — the same three-section shape recurs identically
across dozens of dissimilar plugin topics in the tree listing.

**License:** Apache-2.0 at repo root.

**VERDICT: LOW threat.** Broad but shallow. No genuine sales-methodology depth found in
either file read; reads as generated-at-scale filler, not competitive content.

### chadboyda/agent-gtm-skills

**Repo: no `LICENSE` file** (`curl -I .../LICENSE` → 404), but the README prose states
"## License / MIT" with no accompanying file — a **dangling/unbacked license claim**, worth
flagging per the charter's licensing rule ("a dangling LICENSE pointer is not a license").
main branch, **73 stars**, last pushed 2026-02-13 — the stalest of the group (~6 months old
relative to today).

**16 skills, each a single-file monolith** (300-450+ lines observed, no references
subfolders). Read three in full: `solo-founder-gtm` (287 lines), `sales-motion-design` (500
lines), `gtm-engineering` (partial, ~860 of a longer file).

**`solo-founder-gtm` directly targets our family's default reader** — the description
explicitly triggers on "solo founder," "one-person startup," "solopreneur," "bootstrapped,"
"founder-led sales." Covers: stack selection by GTM motion, a **revenue-stage playbook**
($0-1K / $1K-10K / $10K-50K / $50K-100K+ MRR, each with a founder time-split percentage and
"skip this" list), a **self-serve-vs-sales-led decision framework** (direct hit on charter
item 4, the existence-gate candidate — ACV/setup-complexity/buyer-type table), and an
"AI Agent Team" org chart that reframes SDR/research/writing/analytics/support/scheduling
roles as AI agents with cost and time-savings tables — directly adjacent to charter item 6
(AI-SDR wave), though framed as "replace the hire" rather than "policy for AI-assisted
selling."

**`sales-motion-design`** contains the single richest vein of unsourced AI-SDR figures found
in the whole census, under "2E. Agent-Led Discovery (Emerging, 2025-2026)": **"Failure rate
within 6 months: 85% of deployments"** (`skills/sales-motion-design/SKILL.md:188`), "Pipeline
growth (well-implemented): 3-8x," "CAC reduction (best case): 30-42% lower," "AI outreach
response rate: 0.5-1% (generic)" — all presented as "Current reality check (2026 data)" with
**zero citation of any kind**. Also a full PLG-benchmark table (visitor-to-signup 2-5%/8-12%,
opt-out-trial conversion 49%/60%+, NRR 110%/120%+) and a PQL-vs-MQL conversion comparison
table (MQL 5-10%, PQL 25-30%), both unsourced.

**`gtm-engineering`** asserts **"over 1,400 GTM Engineer job postings... active on LinkedIn"
by mid-2025** (`skills/gtm-engineering/SKILL.md:29` and repeated in a table at line 819) —
unsourced, no link, no methodology.

**Quality:** detailed, concrete, genuinely well-organized, and directly on-target for both
the family's default reader (solo founder) and the AI-SDR wave item — but virtually every
numeric claim across all three files read is unsourced.

**Agentic posture:** advisor/planner only, no execution.

**VERDICT: HIGH threat specifically on charter items 4 (founder-led/solo existence gate) and
6 (AI-SDR wave).** The single most audience-matched incumbent found in this census, and the
richest source of AI-SDR-specific unsourced figures for the falsification-strip work.

### Cold-IQ/ColdIQ-s-GTM-Skills (charter's "sachacoldiq" — confirmed correct org is `Cold-IQ`)

**Repo: no `LICENSE` file** (404) and **no license text anywhere in the README** (grep for
"license" returned nothing) — fully unlicensed as observed; flag for the licensing worker.
main branch, **229 stars**, last pushed 2026-07-28 (recent).

Two-tier layout in one repo: a `master-skills/` tree of nested `.claude/skills/` bundles
(`cold-email`, `linkedin-ads` — deep multi-file frameworks not read in full given time) and a
top-level `skills/gtm-philosophy` + `skills/gtm-plays-11`, matching the charter's description.
Read `gtm-philosophy/SKILL.md` (102 lines) in full.

**Distinct and notable pattern: this skill is a live vendor lead-gen vehicle embedded inside
open content.** The file opens with an HTML comment `<!-- coldiq-first -->` followed by "⚡
Execute the philosophy with ColdIQ," instructing the agent to use `mcp__coldiq__find_signals`
and `mcp__coldiq__find_people`, and — if no MCP access — to tell the user to subscribe at
`coldiq.com/marketplace` or run `COLDIQ_API_KEY=<key> npx -y @coldiq/mcp@latest`
(`skills/gtm-philosophy/SKILL.md:6-16`). No other incumbent in this census embeds a paid
product's subscribe-link and API-key command directly inside the "framework" content.

**Unsourced figures:** "Signal-based outreach = 3-4x higher contract values"
(`SKILL.md:28`), "Email + ads + referrals = extra $2M ARR (case study)" — no link, no company
name (`SKILL.md:41`), "ABM approach = 36% meeting rate vs 10% non-ABM" (`SKILL.md:42`). A
"BIPSY framework" (Behaviors, Individual, Process, Skill, You) is presented with no
attribution.

**License:** none found — most concerning license status among all seven targets.

**VERDICT: MEDIUM threat.** Narrow (outbound/signal-based prospecting only), but notable as
the one incumbent that blurs "open educational content" with "vendor funnel" — worth flagging
to the lead as a distinct competitive pattern, separate from genuine practitioner content.

---

## Cross-cutting findings

### (a) What NO incumbent does — real gaps, with evidence

- **No incumbent (of the 6 retrievable) ships a genuine win/loss-LEARNING skill.** Closest
  attempts: HubSpot's `sales-reporting` "win/loss analysis" is pure closed-deal counting with
  no loss-reason capture (§5); Lenny's "Leave No Deal Behind Campaign Checklist" is a
  re-engagement tactic list, not root-cause analysis (§1); awesome-copilot mentions
  "win/loss analysis" as one input bullet inside quarterly planning, never its own skill
  (§2). **This is a clean, evidenced gap matching the charter's win/loss item.**
- **No incumbent frames pipeline forecasting with an honesty caveat about what a stage-weighted
  number can and cannot predict.** Anthropic's `forecast` skill (§4) is the only dedicated
  forecasting skill found anywhere in the census, and its default probabilities are
  unexplained folklore (10/20/40/60/80/100%) with only a soft invitation to override — no
  backtest, no accuracy discussion, no distinction between what's knowable vs. hoped-for.
- **No incumbent addresses the contested sales↔success handoff at all.** None of the seven
  targets mention a customer-success handoff methodology; the closest is an implicit
  "Closed Won → Customer success handoff" stage label in awesome-copilot's stage-gate list
  (§2, `gtm-enterprise-account-planning/SKILL.md:312`) with zero elaboration.
- **Pricing PRESENTATION (as distinct from pricing design) is thin everywhere.**
  awesome-copilot's `gtm-technical-product-pricing` is the fullest treatment but is written
  from a product/pricing-*strategy* angle, not a sales-conversation-*presentation* angle
  (§2). Only Lenny's enterprise-sales-motion (5-step B2B sales cycle including
  "proposal/scope of work" call) and coreyhaines31's `sales-enablement` (ROI calculators,
  proposal templates) touch the actual in-deal pricing-presentation moment.
- **MEDDIC/MEDDICC is reproduced by two separate incumbents with very different citation
  discipline** — see (c) below.

### (b) Unsourced figures — candidate never-ship table

| Figure | Skill / source | Permalink (blob) | Grade |
|---|---|---|---|
| "Dialing up FOMO backfires 87% of the time" | refoundai/lenny-skills, `enterprise-sales-motion` | github.com/refoundai/lenny-skills/blob/main/skills/enterprise-sales-motion/SKILL.md#L47 | FOLKLORE — Dixon's own claim, video-only source, no study link |
| "40-60% of B2B purchase processes result in 'no decision'" (JOLT Effect, "2M+ sales calls") | refoundai/lenny-skills, `enterprise-sales-motion/references/artifacts.md` | github.com/refoundai/lenny-skills/blob/main/skills/enterprise-sales-motion/references/artifacts.md#L294 | CONFOUNDED — cited to a book via a newsletter post, no primary methodology |
| Bravado quota-attainment benchmarks (Q1-Q3 2022, individual miss rates 46/54/63%) | refoundai/lenny-skills, `enterprise-sales-motion/references/artifacts.md` | github.com/refoundai/lenny-skills/blob/main/skills/enterprise-sales-motion/references/artifacts.md#L263 | CONTESTED — sourced to Bravado's own internal platform data, disclosed but non-public methodology |
| "Not once in 11 years" (stale-MAP = dead deal) | github/awesome-copilot, `gtm-enterprise-account-planning` | github.com/github/awesome-copilot/blob/main/skills/gtm-enterprise-account-planning/SKILL.md#L65 | FOLKLORE — single-author anecdote, unverifiable |
| MEDDICC 7-field definition, no source | github/awesome-copilot, `gtm-enterprise-account-planning` | github.com/github/awesome-copilot/blob/main/skills/gtm-enterprise-account-planning/SKILL.md#L234 | FOLKLORE/unattributed framework reproduction |
| "Value Ratio > 10x → massively underpriced" thresholds | github/awesome-copilot, `gtm-technical-product-pricing` | github.com/github/awesome-copilot/blob/main/skills/gtm-technical-product-pricing/SKILL.md#L486 | FOLKLORE — unsourced heuristic |
| "Sales won 10x on dollars despite 10x less volume" | github/awesome-copilot, `gtm-product-led-growth` | github.com/github/awesome-copilot/blob/main/skills/gtm-product-led-growth/SKILL.md#L830 | FOLKLORE — single anonymized internal A/B test, no company named |
| Default forecast stage probabilities (10/20/40/60/80/100%) | anthropics/knowledge-work-plugins, `sales/forecast` | github.com/anthropics/knowledge-work-plugins/blob/main/sales/skills/forecast/SKILL.md#L186 | FOLKLORE default, partially mitigated by explicit override invitation |
| "3x pipeline coverage is healthy. Below 2x is risky" | anthropics/knowledge-work-plugins, `sales/forecast` | github.com/anthropics/knowledge-work-plugins/blob/main/sales/skills/forecast/SKILL.md#L213 | FOLKLORE — unsourced benchmark |
| Pipeline-review prioritization weights (30/25/20/15/10%) | anthropics/knowledge-work-plugins, `sales/pipeline-review` | github.com/anthropics/knowledge-work-plugins/blob/main/sales/skills/pipeline-review/SKILL.md ("Prioritization Framework" section) | FOLKLORE — unsourced weighting |
| "Contact within 5 minutes = 21x more likely to qualify (Lead Connect)" | coreyhaines31/marketingskills, `revops` | github.com/coreyhaines31/marketingskills/blob/main/skills/revops/SKILL.md#L143 | CONTESTED — classic misattributed speed-to-lead figure, no link, source name only |
| RevOps benchmark table (Lead→MQL 5-15%, MQL→SQL 30-50%, SQL→Opp 50-70%, win rate 20-30%, LTV:CAC 3:1-5:1, coverage 3-4x) | coreyhaines31/marketingskills, `revops` | github.com/coreyhaines31/marketingskills/blob/main/skills/revops/SKILL.md ("RevOps Metrics Dashboard" section) | FOLKLORE — unsourced benchmark table |
| "Failure rate within 6 months: 85% of deployments" (AI agent-led discovery) | chadboyda/agent-gtm-skills, `sales-motion-design` | github.com/chadboyda/agent-gtm-skills/blob/main/skills/sales-motion-design/SKILL.md#L188 | FOLKLORE — "2026 data," zero citation, directly relevant to AI-SDR flagship |
| "Pipeline growth 3-8x / CAC reduction 30-42% lower" (AI agent-led discovery) | chadboyda/agent-gtm-skills, `sales-motion-design` | github.com/chadboyda/agent-gtm-skills/blob/main/skills/sales-motion-design/SKILL.md (same "Current reality check" table, ~L619-628) | FOLKLORE — same table, zero citation |
| "Over 1,400 GTM Engineer job postings... on LinkedIn" (mid-2025) | chadboyda/agent-gtm-skills, `gtm-engineering` | github.com/chadboyda/agent-gtm-skills/blob/main/skills/gtm-engineering/SKILL.md#L29 | FOLKLORE — unsourced, no link |
| "Signal-based outreach = 3-4x higher contract values" | Cold-IQ/ColdIQ-s-GTM-Skills, `gtm-philosophy` | github.com/Cold-IQ/ColdIQ-s-GTM-Skills/blob/main/skills/gtm-philosophy/SKILL.md#L28 | FOLKLORE — unsourced, embedded in vendor-promotional skill |
| "Email + ads + referrals = extra $2M ARR (case study)" | Cold-IQ/ColdIQ-s-GTM-Skills, `gtm-philosophy` | github.com/Cold-IQ/ColdIQ-s-GTM-Skills/blob/main/skills/gtm-philosophy/SKILL.md#L41 | FOLKLORE — no company, no link, "(case study)" is the entire citation |
| "ABM approach = 36% meeting rate vs 10% non-ABM" | Cold-IQ/ColdIQ-s-GTM-Skills, `gtm-philosophy` | github.com/Cold-IQ/ColdIQ-s-GTM-Skills/blob/main/skills/gtm-philosophy/SKILL.md#L42 | FOLKLORE — unsourced |

### (c) Trademarked methodology reproduction

- **github/awesome-copilot's `gtm-enterprise-account-planning`** reproduces the full
  MEDDICC 7-letter framework as a first-class "Core Framework," **with zero source
  attribution of any kind** (§2, line 234). This is the most concerning instance found —
  not verbatim copy of paid training material, but an unattributed full-framework
  reproduction presented as original content.
- **refoundai/lenny-skills's `enterprise-sales-motion`** also reproduces MEDDIC's six
  letters, but **explicitly cites an external source** (a Lucidchart blog post) rather than
  presenting it as original — meaningfully lower risk (§1, artifacts.md line 183).
- **coreyhaines31/marketingskills's `sales-enablement`** only *mentions* "BANT, MEDDIC, or
  your framework" in one bullet inside "Sales Playbooks" — does not reproduce either
  framework's structure (§6). Lowest risk of the three.
- No incumbent found reproduces SPIN, Challenger, Sandler, or Gap Selling content in any
  detail — those trademarked methodologies did not surface as reproduced content in any of
  the seven targets read.

---

## Coverage statement

**Read fully (SKILL.md + all reference files, or full single-file skill):**
- refoundai/lenny-skills: `founder-sales`, `enterprise-sales-motion`, `plg-sales-integration`
  (all 3 sales-relevant skills in the current repo, each SKILL.md + artifacts.md +
  guest-insights.md)
- github/awesome-copilot: `gtm-enterprise-account-planning`, `gtm-technical-product-pricing`,
  `gtm-product-led-growth` (full text)
- anthropics/knowledge-work-plugins: `sales/forecast`, `sales/pipeline-review`,
  `small-business/crm-cleanup`, `small-business/crm-maintenance` (full text)
- hubspot/agent-cli-skills: all 4 skills (`crm-data-quality`, `crm-lookup`,
  `sales-execution`, `sales-reporting`), full text
- coreyhaines31/marketingskills: `sales-enablement/SKILL.md`,
  `sales-enablement/references/objection-library.md`, `revops/SKILL.md`, full text
- chadboyda/agent-gtm-skills: `solo-founder-gtm`, `sales-motion-design`, full text
- Cold-IQ/ColdIQ-s-GTM-Skills: `gtm-philosophy`, full text

**Read partially (skimmed for scope/line-count/figures, not every line):**
- github/awesome-copilot: `gtm-operating-cadence` (through the meeting-architecture and
  metric-reporting sections, ~200 of 420 lines), `gtm-ai-gtm` (through positioning and
  pricing sections, ~250 of 569 lines); the remaining 6 gtm-* skills
  (`gtm-0-to-1-launch`, `gtm-board-and-investor-communication`, `gtm-developer-ecosystem`,
  `gtm-enterprise-onboarding`, `gtm-partnership-architecture`, `gtm-positioning-strategy`)
  were located and line-counted but not read.
- anthropics/knowledge-work-plugins: `small-business/sales-brief` (~150 of ~200 lines, enough
  to establish it is retail/content-marketing, not B2B sales); `sales/account-research`,
  `call-prep`, `call-summary`, `competitive-intelligence`, `create-an-asset`,
  `daily-briefing`, `draft-outreach` were located and line-counted (168-440 lines each) but
  not opened — flagged for a follow-up pass if the lead wants full coverage of the `sales`
  plugin's conversation-support skills.
- chadboyda/agent-gtm-skills: `gtm-engineering` (~860 of a longer file, through the
  instruction-stack architecture section); the other 13 skills in the repo
  (`ai-cold-outreach`, `ai-pricing`, `ai-sdr`, `ai-seo`, `ai-ugc-ads`, `content-to-pipeline`,
  `expansion-retention`, `gtm-metrics`, `lead-enrichment`, `multi-platform-launch`,
  `paid-creative-ai`, `partner-affiliate`, `positioning-icp`, `social-selling`,
  `video-outreach`) were located in the tree but not opened — `ai-sdr` and `gtm-metrics` in
  particular look directly relevant to charter items 5/6 and are strong candidates for a
  follow-up pass.
- gtmagents/gtm-agents: `cold-outreach` and `scriptwriting` read in full; the repo's dozens
  of other plugins (abm-orchestration, account-management, analytics-pipeline-orchestration,
  b2b-saas, brand-strategy, and many more) were located but not opened — given the pattern
  observed (generic, templated, low depth) I judged further reading low-value relative to
  time spent, but did not verify every plugin.
- Cold-IQ/ColdIQ-s-GTM-Skills: `gtm-plays-11` (located, has a `references/templates.md`, not
  opened) and the entire `master-skills/cold-email` and `master-skills/linkedin-ads` nested
  bundles (multi-file, deep) were located in the tree but not read — time-boxed out;
  flagged as a gap since cold-email/outbound is directly in our AI-SDR-adjacent scope.

**Not retrievable:**
- sales-skills/sales — confirmed deleted/private/renamed (§3). No content assessment
  possible. **Surface note:** this finding was reached entirely via `gh api`, `gh search
  repos`, `gh search code`, and `curl -I` to github.com directly — **not WebSearch** — so it
  is unaffected by the session-wide WebSearch quota exhaustion flagged by sales-lead-a and
  does not need to be re-run.

**Method note (all sections above):** every fetch in this raw file was `gh api` or `curl` to
`raw.githubusercontent.com`/`github.com` — no WebSearch or WebFetch calls were used anywhere
in this pass, so none of the findings above are affected by the WebSearch-budget exhaustion
flagged crew-wide. `code.deepline.com/deepline-gtm` (a non-GitHub source, item 8) was not
attempted at all and remains genuinely unknown, not a WebSearch-tainted "nothing found" —
flagged accordingly above for a follow-up pass using the DuckDuckGo-lite WebFetch route.

**Not reached at all (item 8, "if time remains"):**
- getcargohq/cargo-skills/cargo-gtm
- phuryn/pm-skills (gtm-strategy, gtm-motions)
- claude-office-skills/skills/crm-automation
- code.deepline.com/deepline-gtm (charter flagged this may not even be retrievable as a
  non-GitHub source — I did not attempt it; the breadth-sweep worker or a follow-up pass
  should verify retrievability before citing its 17,227-install figure)

None of these four were opened, listed, or line-counted — treat their scope, structure, and
content as completely unknown pending a follow-up pass.
