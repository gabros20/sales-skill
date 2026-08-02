# _raw-a1 — ecosystem breadth sweep (skills.sh + gh code/repo search)

Worker A1, Channel A. Date 2026-08-03. Method: skills.sh `/api/search?q=` (63 core queries +
9 follow-up queries, 7s spacing, 0 confirmed rate-limit empties) cross-checked against `gh api
search/code` / `gh api repos/.../contents` (GitHub's own search + contents API, not subject to
the skills.sh rate limit). **The GitHub code-search cross-check surfaced several large packs
that a skills.sh-only sweep would have under-ranked or missed entirely** (see §Coverage) — this
independently reproduces the lead's `alirezarezvani/claude-skills` gotcha (raw-a0): skills.sh
semantic search is lossy for large multi-plugin repos. Treat this file's install counts as
skills.sh-reported and directionally honest, not exhaustive.

No WebSearch was used anywhere in this file (WebSearch was reported exhausted session-wide by
the lead partway through — irrelevant to this file since none of these findings depend on it).

---

## 0. Headline finding the lead needs first

**The marketing incumbent already claims several of our 14 items, at 100–1000x the install
scale of every dedicated sales pack found.** `coreyhaines31/marketingskills` (the family's
adjudicated marketing incumbent) ships, under its own marketing plugin:
- `revops` — **81,381 installs**. Description (verbatim, read from SKILL.md): "When the user
  wants help with revenue operations, lead lifecycle management, or **marketing-to-sales
  handoff processes**... lead scoring, lead routing, MQL, SQL, pipeline stages, deal desk, CRM
  automation, marketing-to-sales handoff, ... lead qualification, or when should marketing hand
  off to sales." This is a direct, high-scale claim on items **9 (CRM), 10 (pipeline), 12
  (marketing→sales handoff), and 2 (qualification)**.
- `prospecting` — **32,221 installs**. Description: find/qualify/build a prospect list, "ICP-fit
  accounts," "target account list," "outbound list" — a direct claim on **item 1 (ICP/account
  selection)** and cold outbound, both of which marketing's own `handoff.md:42` cedes to sales
  in doctrine ("cold outbound/prospecting are SALES's — the incumbent genre routinely blends
  these into marketing; this pack does not").
- `cold-email` — 89,060 installs; `sales-enablement` — 84,811 installs (objection docs, demo
  scripts, proposal templates — items 5, 6, 7).

Source: https://github.com/coreyhaines31/marketingskills (skills at
`skills/revops/SKILL.md`, `skills/prospecting/SKILL.md`, `skills/sales-enablement/SKILL.md`,
`skills/cold-email/SKILL.md`). **This is independent, in-the-wild evidence that our
marketing→sales seam ruling is the non-default choice in the ecosystem** — the single
highest-install "GTM" pack in the entire sweep is the one blending marketing and sales exactly
as the charter warned. It doesn't invalidate our seam (our seam is a design choice, not a
description of the field) but the lead should know the field's center of gravity disagrees with
us by orders of magnitude in install count.

---

## 1. Census table (sorted by breadth score, high to low)

Breadth key (14 items): 1=ICP/account-selection 2=qualification 3=stages+exit-criteria
4=discovery 5=demo 6=objection 7=proposal/collateral 8=pricing-presentation 9=CRM-structure
10=pipeline 11=forecasting 12=mktg→sales-handoff 13=sales→success-handoff 14=win/loss

| Pack / skill | Upstream | Installs | Scope (1-line) | Breadth (items) | Grade |
|---|---|---:|---|---|---|
| **gtmagents/gtm-agents** (8 sales-category plugins + orchestration + competitive-intel) | github.com/gtmagents/gtm-agents | 495 top (`cold-outreach`); most plugin skills 55–280 | 263-skill marketplace; dedicated `sales` category = sales-prospecting, sales-pipeline (crm-hygiene/forecast-discipline/deal-review), sales-enablement, sales-operations (territory/comp/quota), sales-coaching, account-management (QBRs/expansions), sales-calls (MEDDIC checklist), enterprise-sales (procurement/value-story); plus `sales-handoff-orchestration` and `competitive-intelligence` (battlecards + **win-loss-dataset**) in adjacent categories | **~12-13/14** — 1(partial),2✓,3✓,4✓,5(partial),6✓,7(partial),8(partial via comp-mechanics≠pricing),9✓,10✓,11✓,12✓,13✓,14✓ | **A** — broadest structural coverage found; content verified generic/templated (see §Pack notes), so breadth ≠ depth |
| **TheCraigHewitt/sales-skills** (mirrored as `TheCraigHewitt/skills` sales dir) | github.com/TheCraigHewitt/sales-skills | 9-43 per skill (low; mirrored twice, counts split) | 21-skill dedicated sales pack: buyer-persona, discovery-call, demo-script, objection-handling, proposal-pricing, pipeline-review, **forecast**, **win-loss-analysis**, sales-comp, negotiation, competitive-intel, call-debrief, cold-call/cold-email/outbound-sequence/linkedin-outreach/direct-mail, referral-intro, event-networking, lead-research, sales-context | **~9-10/14** — 4✓5✓6✓7✓8✓10✓11✓14✓ explicit-by-name; 1,2,3 partial; **9,12,13 absent** | **A** — single most name-exact overlap with our flagship items (forecast + win-loss both present, well-written); MIT-licensed; installs tiny |
| **ncklrs/startup-os-skills** (sales-relevant subset of a 55-skill multi-domain pack) | github.com/ncklrs/startup-os-skills | 137-552 per skill (proposal-writer highest at 552) | account-executive, demo-specialist, discovery-caller (SPIN, budget/timeline qualification named), proposal-writer (ROI, SOW, RFP, pricing presentation), sales-negotiator (BATNA), sales-ops-analyst ("building forecasting models," CRM workflows), sales-leader, sales-strategist, renewal-manager, qbr-facilitator, sales-enablement, gtm-leader/gtm-copywriter, competitive-strategist | **~10/14** — 2✓3✓4✓5✓6(partial)7✓8✓9✓10✓11✓13✓; **1,12,14 absent/weak** — no win-loss skill found | **A** — real per-skill depth (not templated boilerplate, verified via SKILL.md descriptions), best installs among dedicated multi-skill breadth packs |
| **guia-matthieu/clawfu-skills** (sales+revops+sdr-automation dirs of a large multi-domain pack) | github.com/guia-matthieu/clawfu-skills | 150-550 (yc-pitch-deck 543, rfp-response 276, spin-selling 228) | sales/: challenger-sale, meddic-scorecard, never-split-difference (Voss), sales-narrative, sandler-system, spin-selling. revops/: account-health, commission-intelligence, crm-hygiene, deal-risk-scoring, **forecast-scenarios**, lead-scoring, **pipeline-forecasting**, revenue-attribution. sdr-automation/: icp-matching, lead-qualification-bant, lead-qualification-meddic, outbound-sequencer, prospecting-research, signal-monitoring | **~10/14** — 1✓2✓(BANT+MEDDIC named)3(partial)4(partial via customer-discovery)6✓7✓9✓10✓11✓13(partial); **5,12,14 weak/absent** | **A** — best NAMED-METHODOLOGY coverage of any pack found (SPIN, Challenger, Sandler, MEDDIC, BANT, Voss negotiation all as distinct skills); already on A3's license list per lead note |
| **anthropics/knowledge-work-plugins/sales** (OFFICIAL Anthropic) | github.com/anthropics/knowledge-work-plugins | `forecast` 2275 (highest of ANY forecast-named skill in the sweep); `pipeline-review` 2119; `competitive-intelligence` 3661 | 9 skills: account-research, call-prep, call-summary, competitive-intelligence, create-an-asset, daily-briefing, draft-outreach, **forecast**, pipeline-review. Plus `partner-built/apollo` and `partner-built/common-room` add prospect/compose-outreach/call-prep variants | **~7-8/14** — 1✓4✓5(partial)6(partial via call-summary)7✓10✓11✓; **9,12,13,14 absent** | **A** — official origin = highest credibility; `forecast` skill is a real stage-weighted method (best/likely/worst, commit-vs-upside, gap analysis) but **default stage probabilities are generic/hand-set (20/40/60/80%), only backtested if the CRM is connected for historical win rates** — directly relevant to our forecasting-honesty flagship, see §5 |
| **LeadMagic/gtm-skills** (24-category, ~130-skill repo) | github.com/LeadMagic/gtm-skills | 3-6 per skill (very low; huge breadth, near-zero adoption) | All 24 category dirs enumerated: foundation (icp-scoring, icp-targeting-tiers, competitive-intel, pricing-strategy, buyer-psychology), sales-revops (demo-scripts, objection-handling, pipeline-management, deal-desk, sales-enablement, buyer-indecision), founder-led (41 skills incl. founder-sales, solo-founder-gtm, sales-team-building), outbound (10), prospecting (8), sales-plays (5 signal-based), automation (hubspot-setup, salesforce-setup, crm-integration), customer-success (separate dir: qbr-planning, cs-playbooks), management-leadership (sales-coaching, gtm-leadership) | **~7/14** — 1✓5✓6✓8(partial)9✓10✓13(partial); **CONFIRMED ABSENT: 11 (forecast) and 14 (win-loss)** — checked all 24 category dirs directly, no skill named forecast/forecasting/win-loss/win-loss-analysis anywhere in the repo | **A** — largest single repo found by skill count; **flagship-relevant negative finding**: the biggest GTM breadth repo in the ecosystem has a genuine hole at both our candidate flagship items |
| **alirezarezvani/claude-skills** `commercial/` + `business-growth/` | github.com/alirezarezvani/claude-skills | sales-engineer 743; commercial-forecaster/revenue-operations/cro-advisor 560-925; competitive-intel 652 | **Already deep-read by the lead — see `research/raw/_raw-a0-lead-breadth-repo.md`, do not re-derive.** pricing-strategist, deal-desk, partnerships-architect, channel-economics, commercial-policy, rfp-responder, commercial-forecaster; revenue-operations, sales-engineer, contract-and-proposal-writer, customer-success-manager | **~5-6/14** per lead's own read — 7✓8✓9(partial)10✓11✓; **1,2,4,5,14 at or near zero** | **A / threat HIGH on forecasting framing, LOW on breadth** — 23.6k★, MIT, but owns deal-ECONOMICS not the buying CONVERSATION (lead's framing, verbatim) |
| **hubspot/agent-cli-skills** (vendor, official HubSpot) | github.com/hubspot/agent-cli-skills | crm-lookup 896, crm-data-quality 862, deal-management 824, sales-reporting 819, sales-execution 818 | Full deal-lifecycle CLI: audience-targeting, bulk-operations, communication-history, crm-data-quality, crm-lookup, custom-object-management, customer-retention, data-enrichment, **deal-management** (create/qualify/advance/close deals), quote-to-cash, sales-execution, sales-reporting, team-ownership, ticket-resolution, workflow-automation | **~5/14** — 7(partial via quote-to-cash)8(partial)9✓✓10✓12(partial via audience-targeting/MQL) | **B** — vendor-locked to HubSpot's API/data model, real workflow coverage, zero methodology teaching, highest installs among CRM-tool wrappers |
| **louisblythe/sales-skills** | github.com/louisblythe/sales-skills | 44-260 per skill (lead-qualification-logic 204, deal-review-win-loss 198, win-loss-reason-extraction 192) | **122+ micro-skills** for building an AI sales bot/voice-agent (repo description: "Sales skills for Claude Code **and AI agents**"). Covers the full cycle in granular AI-agent-operational form: ideal-customer-profile-matching(1), lead-qualification/-logic/budget-extraction-qualification(2), territory-account-launch(3, partial), discovery(4), sales-presentations(5), objection-handling/-recognition/-pattern-learning(6), pricing-discussion-logic/pricing-negotiation(8), pipeline-management(10), time-to-close-prediction(11, forecast-flavored), handoff-detection(12), customer-onboarding(13), **deal-review-win-loss + win-loss-reason-extraction(14)** — plus dozens of bot-operational skills (voicemail-drop-optimization, ghost-recovery-sequences, spam-bot-detection-avoidance, conversation-pause-intelligence) that are AI-SDR mechanics, not selling doctrine | **~10-11/14 in granular/bot form** | **A for breadth, B for our purposes** — **no LICENSE file found** (`license: null` on the GitHub API) — flag for licensing worker: unlicensed, all-rights-reserved by default; also our single best AI-SDR-wave finding (see Q5) |
| **coreyhaines31/marketingskills/sales-enablement** (+ `revops`, `prospecting`, `cold-email` — filed under MARKETING, not a dedicated sales pack) | github.com/coreyhaines31/marketingskills | sales-enablement 84,811; revops 81,381; cold-email 89,060; prospecting 32,221 | See §0 above — pitch decks, one-pagers, objection docs, demo scripts, proposal templates (sales-enablement); MQL/SQL, lead scoring/routing, pipeline stages, deal desk, CRM automation, marketing-to-sales handoff (revops); ICP-fit account lists, outbound lists (prospecting) | **~7/14 spread across 4 marketing-filed skills** — 1,2,5,6,7,9,10,12 all touched | **A — the single biggest-install threat to our marketing-seam boundary**, not to our sales-methodology depth (see §0) |
| **claude-office-skills/skills** (several standalone, high-install) | (source string only; **not verified as a resolvable GitHub org — see §Coverage**) | crm-automation 4421; lead-qualification 3641; customer-success 3740; pipedrive-automation 3570 | Standalone high-install CRM/qualification/CS skills, not obviously bundled as one coherent sales system | **~3/14 spread thin** (9, 2, 13) | **B/C** — high installs but appears to be discrete single-purpose tool skills rather than a system; **flag for A3**: could not confirm upstream repo resolves cleanly (see coverage note) |
| **chadboyda/agent-gtm-skills** | github.com/chadboyda/agent-gtm-skills | ai-cold-outreach 138, lead-enrichment 137, solo-founder-gtm 132, ai-sdr 96 | ai-cold-outreach, ai-pricing, **ai-sdr**, content-to-pipeline, expansion-retention, gtm-engineering, gtm-metrics, lead-enrichment, positioning-icp, **sales-motion-design** (PLG vs sales-led decision — existence-gate relevant), **solo-founder-gtm** ("complete solo founder GTM playbook"), social-selling, video-outreach | **~4-5/14** (1 via positioning-icp, 8 partial, 10 partial, 11 absent) | **B** — most directly useful for Q3 (founder-led) and Q5 (AI-SDR), not for full-cycle breadth |
| **sachacoldiq/coldiq-s-gtm-skills** | github.com/sachacoldiq/coldiq-s-gtm-skills | cold-email 146, cold-email-4-sequence 130, gtm-philosophy 87 | 34 skills, near-exclusively outbound/SDR mechanics: cold-call-scripts, cold-email templates ×3, sdr-master-prompts, sdr-outbound-rules, personalization playbooks ×3, buying-signals, inbound/outbound-triggers, list-building, linkedin-campaign, email-metrics-benchmarks, gtm-philosophy, gtm-plays-11 | **~1-2/14** (1 partial via buying-signals; everything else is outbound mechanics, not in our 14) | **B** — deep on ONE topic (outbound), essentially zero on qualification/discovery/demo/proposal/CRM/pipeline/forecast/win-loss |
| **doris-labs/sales-skills** | github.com/doris-labs/sales-skills | 1-2 per skill (near-zero adoption) | Near-complete NAME coverage: cold-email, expansion-upsell, negotiation, objection-handling, proposal, renewal-churn-save, sales-context, competitive-battlecard, closing-plan, discovery-call, discovery-planning, **meddpicc-qualification**, prospecting, social-selling, deal-review-prep | **~8/14 by name** (1,2,3,4,6,7,13,14) | **B** — best evidence for "breadth exists in the long tail but adoption is ~zero"; template-shaped, unverified depth |
| **jmbluhm/b2b-sales-skills** | github.com/jmbluhm/b2b-sales-skills | 2 per skill (near-zero) | Pure named-methodology pack: challenger-sale, **meddpicc**, mutual-action-plan, multi-threading, **chris-voss-framework**, sandler-pain-funnel, feel-felt-found, **spin-selling**, value-selling-roi | **~5/14 by name** (2,3,6,8) — methodology-only, no CRM/pipeline/forecast/win-loss | **B** — narrow but methodologically literate; near-zero installs |
| **beingsmit/technical-product-gtm** (source of `github/awesome-copilot`'s gtm-* mirror) | github.com/beingsmit/technical-product-gtm | mirrored copy on awesome-copilot: `gtm-enterprise-account-planning` 1536 | 11 skills, only 1-2 genuinely sales-cycle: **gtm-enterprise-account-planning** (MEDDICC qualification, deal health, mutual action plans, "stale MAP = dead deal"), gtm-technical-product-pricing (partial). Rest (gtm-0-to-1-launch, gtm-ai-gtm, gtm-board-and-investor-communication, gtm-developer-ecosystem, gtm-enterprise-onboarding, gtm-operating-cadence, gtm-partnership-architecture, gtm-positioning-strategy, gtm-product-led-growth) is broader GTM/product strategy, not selling | **~2-3/14** (2,3 via account-planning; 8 partial) | **B** — single strong skill (account-planning) inside a mostly-adjacent pack; this is the repo `github/awesome-copilot` mirrors as its 11-skill gtm-* family |
| **refoundai/lenny-skills** | github.com/refoundai/lenny-skills | founder-sales 2230, sales-qualification 1960, enterprise-sales 1750, product-led-sales 1697, building-sales-team 1616, sales-compensation 1549 | Confirmed: repo's actual directory names differ from skills.sh skillIds (dir has `enterprise-sales-motion`, `first-b2b-customers`, `plg-sales-integration`, `founder-sales`, `defining-icp` — no literal `sales-qualification`/`product-led-sales`/`building-sales-team` folder; skills.sh may index a renamed/restructured branch). 6 sales-tagged skills within a 74-skill PM-focused pack | **~5/14** (1 via defining-icp, 2, 3, 12 via plg-sales-integration) | **B** — high installs, single-skill-each breadth, PM-context framing not sales-system framing |
| **sales-skills/sales** (`sales-do`) | source string `sales-skills/sales`; **org confirmed to exist (`gh api orgs/sales-skills`), but `gh api repos/sales-skills/sales` returns 404 — anomalous, unverified** | sales-do 323 (highest); sales-cadence 140; sales-forecast 87; sales-coaching 87; sales-proposal-template 78 | ~150+ `sales-<vendor-tool>` skills (sales-salesforce, sales-gong, sales-clay, sales-6sense, sales-zoominfo, sales-apollo, sales-salesloft, sales-lemlist, sales-woodpecker, sales-hunter, dozens more) — one skill per sales-tool integration — plus a smaller real-methodology subset (sales-forecast, sales-coaching, sales-deal-inspect, sales-account-map, sales-lead-score, sales-proposal-template, sales-crm-selection, sales-lead-routing, sales-funnel, sales-call-review, sales-compete) | **~7/14 spread thin across dozens of tiny skills** (1,2,7,9,10,11,12,14 all touched somewhere in the tail) | **C** — vendor-integration-per-tool bulk with a real-content minority; **license/identity unverified — flag for A3**, see §Coverage |
| **membranedev/application-skills** | 1000-skill repo, one skill per SaaS app | zoho-crm 560, dynamics-crm 537, sugarcrm 200, capsule-crm 166, agile-crm 165 (+ 1crm, amocrm, centralstationcrm, civicrm, close, copper, copperx, espocrm, and more alphabetically) | One skill per CRM vendor's API — pure vendor wrapper family, no methodology content | **0/14 as methodology; item 9 (CRM) only, and only as API plumbing** | **C** — one row for the whole family per charter guidance |
| **claude-office-skills/skills/crm-automation**, **customware-ai/skills/crm-builder**, **casper-studios/casper-marketplace/attio-crm** | see individual repos | crm-automation 4421; crm-builder 1289; attio-crm 313 | Standalone CRM-vendor-wrapper skills, not bundled sales systems | item 9 only | **C** — vendor wrappers, one row |
| **sickn33/agentic-awesome-skills** (44.3k★ catalog aggregator, 1987+ skills, heavily self-duplicated across `skills/` and 2× `plugins/.../skills/` mirrors) | github.com/sickn33/agentic-awesome-skills | not separately indexed on skills.sh under a clean id | sales-automator (thin: cold email + templates), sales-enablement (**explicitly sourced from coreyhaines31/marketingskills** per its own `source:` field — a mirror, not original), odoo-sales-crm-expert (vendor), salesforce-automation (vendor), offers, revops, pricing, pitch-psychologist (thin, template stub), competitor-tracking, billing-automation | **~4/14 shallow, mostly re-hosted content** | **C** — aggregator/catalog, not an original pack; inflates apparent skill-count metrics ecosystem-wide without adding original content |
| **github/awesome-copilot** gtm-* family (11 skills, mirrors `beingsmit/technical-product-gtm`) | github.com/github/awesome-copilot | ~1500-1740 each | gtm-0-to-1-launch, gtm-ai-gtm, gtm-board-and-investor-communication, gtm-developer-ecosystem, **gtm-enterprise-account-planning**, gtm-enterprise-onboarding, gtm-operating-cadence, gtm-partnership-architecture, gtm-positioning-strategy, gtm-product-led-growth, gtm-technical-product-pricing | **~2-3/14** (same as beingsmit above — this IS beingsmit, mirrored) | **B** (duplicate entry of beingsmit above — do not double-count in synthesis) |
| **anthropics/financial-services/deal-tracker, deal-screening, deal-sourcing** | github.com/anthropics/knowledge-work-plugins | 358-360 each | **NAMING COLLISION, not sales content** — these are M&A/PE investment "deals," not B2B sales pipeline deals. Confirmed by directory (`financial-services/`, not `sales/`) | 0/14 | **D — noise**, same genre as the "close-management" false-positive below |
| **anthropics/knowledge-work-plugins/close-management** | github.com/anthropics/knowledge-work-plugins | (appeared under `MEDDICC` code search) | **NAMING COLLISION** — this is `finance/skills/close-management`, i.e. accounting month-end close, not deal-closing | 0/14 | **D — noise** |
| **github/awesome-copilot** salesforce-apex-quality, salesforce-component-standards, salesforce-flow-design | github.com/github/awesome-copilot | 8724 (bigquery-pipeline-audit, unrelated) | Salesforce **developer** skills (Apex code quality, component standards, Flow design) — software engineering on the Salesforce platform, not selling | 0/14 | **D — noise floor confirmed**, exactly the false-positive class the brief warned about |
| **wondelai/skills/cro-methodology** | — | 4024 | CRO = conversion-rate-optimization (growth/marketing), not sales methodology — a naming collision on "sales-methodology" query | 0/14 | **D — noise** |

---

## 2. Pack notes (A/B grade, prose)

**gtmagents/gtm-agents.** The broadest *structure* found in the sweep: a 263-skill
commands+agents+skills marketplace with a dedicated `sales` category (8 plugins) plus
cross-category `sales-handoff-orchestration` and `competitive-intelligence` (which explicitly
ships a `run-win-loss-program` command and `win-loss-dataset` skill —
`plugins/competitive-intelligence/.claude-plugin` verified via `gh api`). I read
`plugins/sales-pipeline/skills/forecast-discipline/SKILL.md` in full: it is a real framework
(forecast tiers, grading rubric, cadence, accountability, continuous improvement) but generic
and templated — no backtested numbers, no primary sources, references its own internal
"GTM Agents Inspection Worksheet." Verdict: **wide but shallow**. Installs are moderate (cold-
outreach highest at 495; most sales-plugin skills sit 55-280).

**TheCraigHewitt/sales-skills.** MIT-licensed (verified: `Copyright (c) 2026 Craig Hewitt`),
21 skills, single-purpose sales pack (not bundled with marketing/growth/PM content like every
other broad pack found). Its `forecast/SKILL.md` opens: *"You are a revenue operations leader
who has built and defended forecasts... forecasting is the most lied-about activity in sales.
Reps are optimistic. Managers sandbag. Executives want a number they can take to the board."*
This is a genuinely well-framed honesty angle — **our forecasting flagship cannot claim this is
unclaimed territory as a THESIS**, only that we can execute it with better evidence discipline
(same pattern as the lead's alirezarezvani finding, independently). `win-loss-analysis/SKILL.md`
similarly opens with a credible practitioner voice. Cross-references between its own skills
(e.g. forecast → "see pipeline-review... see sales-comp") suggest a genuinely designed system,
not a random skill dump. Installs are tiny (9-43 per skill, split across two indexed mirrors) —
this is a QUALITY/breadth threat, not an adoption threat.

**ncklrs/startup-os-skills.** A 55-skill multi-domain pack (also covers PM, marketing, video/
Remotion tooling) whose ~15 sales-tagged skills have real per-skill depth verified from their
descriptions: `discovery-caller` names SPIN selling, active listening, budget/timeline
qualification, stakeholder mapping explicitly; `sales-negotiator` names BATNA, anchoring,
multi-party negotiation; `account-executive` names multi-threading, champion development, buying
committee navigation. No win-loss skill found anywhere in its 55-skill directory listing
(checked directly). Best installs of any dedicated multi-skill sales breadth pack (`proposal-
writer` 552, several others 130-300).

**guia-matthieu/clawfu-skills.** Distinctive because it treats named sales methodologies as
first-class, separately-named skills — SPIN, Challenger, Sandler, MEDDIC (as both
`meddic-scorecard` and `lead-qualification-meddic`), BANT, and Chris Voss's negotiation
framework (`never-split-difference`) — inside a `sales/` + `revops/` + `sdr-automation/` triad.
This is the ecosystem's best coverage of the charter's methodology-evidence question (channel B
territory, but flagged here since I found it during breadth work). Also has real forecasting
content (`forecast-scenarios`, `pipeline-forecasting`) but **no win-loss skill**. Already on A3's
license-check list per the lead's calibration note — do not re-verify license here.

**anthropics/knowledge-work-plugins/sales.** Official Anthropic pack, 9 skills, highest-install
forecast skill in the entire sweep (2275) by a wide margin. Read `forecast/SKILL.md` in full:
weighted forecast with best/likely/worst, stage-probability table (Negotiation 80% / Proposal
60% / Evaluation 40% / Discovery 20% — **these are illustrative placeholder percentages in the
template, not backtested defaults**), commit-vs-upside split, gap analysis. The "supercharged"
tier explicitly notes historical win-rate calibration only happens **if the CRM is connected**;
standalone use runs on generic stage priors. This is the cleanest single data point for our
forecasting-honesty flagship: **the most-installed, most credible forecast skill in the
ecosystem is honest about its own generic-prior limitation in its own copy, but still ships
generic priors as the default path.** `pipeline-review` (2119 installs) flags stale/stuck
deals, single-threaded risk, close-date hygiene — real pipeline-management content. Also has a
`partner-built/` layer (apollo, common-room connectors) with additional prospect/outreach
skills not counted in the core 9.

**LeadMagic/gtm-skills.** Not on the lead's seed list — new discovery via `gh api search/code`.
The single largest repo by skill count found in this sweep (24 category directories, roughly
130 skills). I enumerated every category directory directly via `gh api repos/.../contents/skills/<dir>`
(not a search — a full listing) and confirmed **zero skills named forecast, forecasting,
revenue-forecast, or win-loss anywhere in the repo**. This is a strong, directly-verified
negative finding for Q2/Q4 below — not an absence-of-evidence problem, an absence-of-content
fact. Installs are very low (3-6 per skill) despite the size, suggesting the repo is new/
undiscovered rather than rejected.

**louisblythe/sales-skills.** 122+ micro-skills, explicitly framed for building an AI sales
bot/voice-agent (repo description: "Sales skills for Claude Code **and AI agents**"). This is
architecturally different from every other pack in this table — it decomposes selling into
atomic behaviors an autonomous agent would need (response-latency-management, voicemail-drop-
optimization, ghost-recovery-sequences, spam-bot-detection-avoidance, conversation-pause-
intelligence) alongside conventional sales concepts (ICP matching, lead qualification, pipeline
management, win-loss). **No LICENSE file found via the GitHub API** (`license: null`) — flag to
A3/licensing: default-copyright, cite with extreme caution or not at all. This is the strongest
single AI-SDR-wave finding in the sweep (see Q5).

**coreyhaines31/marketingskills.** Covered in §0 — the marketing incumbent's `revops`,
`prospecting`, `cold-email`, and `sales-enablement` skills collectively claim roughly 8 of our
14 items at install counts (32k-89k) that dwarf every dedicated sales pack in this table by two
to three orders of magnitude. This is the census's single most important number for the lead's
wedge calibration.

---

## 3. Answers to the lead's 5 questions

**1. Is there an end-to-end sales system, or is the field fragmented?**
Both, layered. **Structurally**, `gtmagents/gtm-agents` and `louisblythe/sales-skills` cover
essentially all 14 items — but the former is generic/templated per-skill (verified by reading
one full SKILL.md) and the latter is AI-bot-behavior-shaped, not a human playbook.
**Content-wise**, `TheCraigHewitt/sales-skills`, `ncklrs/startup-os-skills`, and `guia-matthieu/
clawfu-skills` each independently cover 9-10/14 items with real, differentiated per-skill prose
— none of them is a copy of another, and none has serious install traction (single-to-triple-
digit installs each). No pack combines (a) genuine end-to-end coverage, (b) non-templated depth,
and (c) meaningful install adoption, simultaneously. Verdict: **OPEN-BY-FRAGMENTATION, tilting
toward CONTESTED on specific items** — see item-by-item breakdown: CRM/pipeline/proposal/
pricing are contested by `alirezarezvani/claude-skills` (deal-economics) and `coreyhaines31/
marketingskills` (handoff+CRM+prospecting, at huge scale); qualification/methodology is
contested by `guia-matthieu/clawfu-skills` and `jmbluhm/b2b-sales-skills`; discovery/demo/
objection/win-loss/forecast-as-a-system is where the genuinely broad, high-quality, dedicated
packs (TheCraigHewitt, ncklrs) sit — and none of them has adoption. **The wedge is not "nobody
has built this," it's "several people have built pieces of this well, and nobody has adoption
while doing it."**

**2. Does anything cover FORECASTING with real method?**
Not an empty shelf, but no one owns it authoritatively. Ranked by credibility/install:
(a) `anthropics/knowledge-work-plugins/sales/forecast` — 2275 installs, official Anthropic,
real weighted method, **honestly flags its own generic-prior limitation in its own copy** (see
Pack notes above) — best single data point for our flagship framing.
(b) `alirezarezvani/claude-skills/commercial-forecaster` — lead's find, sophisticated mechanism
(CoV confidence bands, 3-tier commit/best/pipe), but its own priors are unsourced (30-cell
benchmark table attributed to "KeyBanc SaaS Survey, OpenView, Bessemer Atlas" with zero links) —
**directly usable as a "theatre" example** per the lead's framing.
(c) `TheCraigHewitt/sales-skills/forecast` — well-framed honesty angle ("forecasting is the most
lied-about activity"), near-zero installs.
(d) `guia-matthieu/clawfu-skills` — `forecast-scenarios` + `pipeline-forecasting`, real content,
low-moderate installs (165-181).
(e) `LeadMagic/gtm-skills` — **confirmed absent**, directly verified against all 24 category
directories, despite being the largest repo in the sweep.
Queries that back this: `forecast`, `forecasting`, `pipeline-forecast`(via revenue-forecast/
sales-forecast queries), `revenue-forecast`, `sales-forecast` — all live skills.sh queries,
0 empty, cross-checked with `gh api search/code?q=sales+forecast+filename:SKILL.md` (6904 total
hits, top unique repos listed in raw notes). **Verdict: forecasting is a contested-but-thin
shelf — real method exists in 4-5 places, none dominant, and the honesty gap (unsourced priors)
is present in the two highest-credibility examples (Anthropic's generic defaults, alirezarezvani's
unsourced benchmark table).**

**3. Does anything serve the SOLO/FOUNDER-LED reader?**
Yes, clearly, in multiple places: `chadboyda/agent-gtm-skills/solo-founder-gtm` ("complete solo
founder GTM playbook from stack selection through..."), `refoundai/lenny-skills/founder-sales`
(2230 installs, highest install count of any founder-focused sales skill found),
`LeadMagic/gtm-skills/founder-led/` (41 skills, largest single founder-focused category in the
sweep, includes `solo-founder-gtm`, `founder-sales`, `sales-team-building`),
`chadboyda/agent-gtm-skills/sales-motion-design` (explicitly frames the PLG-vs-sales-led
existence-gate decision — "choose between PLG and sales-led," "time-to-first-value" — this is
the closest thing found to the charter's "when does a sales motion even exist" question).
Not one of these is a comprehensive END-TO-END founder-led sales system; they are founder-
flavored entries into otherwise-generic breadth packs.

**4. Does anything cover WIN/LOSS learning?**
Yes, but thinly and without a dominant owner. Direct hits: `gtmagents/gtm-agents/
win-loss-dataset` (59 installs, part of a `run-win-loss-program` command + `win-loss-analyst`
agent), `TheCraigHewitt/sales-skills/win-loss-analysis` (well-written, 10-41 installs across its
two mirrors), `louisblythe/sales-skills/deal-review-win-loss` + `win-loss-reason-extraction`
(192-198 installs, AI-bot-flavored). `gh api search/code?q=win-loss+filename:SKILL.md` returned
601 total hits, the large majority of which are **single-skill personal repos, forks, or
registry/catalog mirrors** (kortix-ai/suna, mohitagw15856, majiayu000/claude-skill-registry ×2,
criptogus, growthack88, pmalliance, deanpeters, matteotitta ×2, lionelsimai, whyashthakker,
FerroxLabs, octavehq, ashutoshsrivastava17, nthnclrk, naveedharri) — evidence the topic is a
known, easy genre move (an LLM can generate a plausible win-loss-analysis skill on request) but
**confirms nobody has built an authoritative, high-install win-loss pack**. Notably absent from
win-loss: `LeadMagic/gtm-skills` (confirmed, see Q2) and `ncklrs/startup-os-skills` (confirmed
absent from its 55-skill directory listing).

**5. AI-SDR / AI-outbound wave — who is there?**
Fragmented, low-traction, no dominant player. `gh api search/code?q=ai-sdr+filename:SKILL.md`
returned 405 total hits; distinct real entries: `chadboyda/agent-gtm-skills/ai-sdr` (96
installs, highest of any dedicated ai-sdr skill), `sales-skills/sales/sales-aisdr` (23),
several 1-2-install personal/toy repos (robomotionio, darsh20009, sshjddhhd-svg, smithery.ai,
jkrbx5v4sq-png). The more interesting finding is **`louisblythe/sales-skills`**: not badged
"ai-sdr" but its entire 122-skill design is for building an AI sales bot (voicemail-drop-
optimization, ghost-recovery-sequences, spam-bot-detection-avoidance, response-latency-
management, conversation-pause-intelligence) — this is a much deeper AI-SDR-mechanics treatment
than anything carrying the literal "ai-sdr" tag, unlicensed, 44-260 installs per skill.
**Verdict: the wave is real in skill-count terms but nobody has consolidated it — confirms the
charter's framing of this as fresh/under-canonized, matching the AI-support precedent from the
success pack.**

---

## 4. Coverage statement

**Queries run (skills.sh, all live, 0 confirmed rate-limit empties out of 72 total):**
sales, selling, sell, crm, pipeline, forecasting, forecast, outbound, cold-email, cold-outreach,
prospecting, sdr, bdr, gtm, go-to-market, revenue, revops, revenue-operations, deals, deal-desk,
closing, negotiation, discovery, discovery-call, demo, objection, objection-handling, proposal,
rfp, quota, account-executive, account-planning, founder-led, founder-sales, b2b, b2b-sales,
enterprise-sales, meddic, meddpicc, spin-selling, challenger-sale, sandler, bant, qualification,
lead-qualification, win-loss, sales-enablement, battlecard, pricing-negotiation, contract,
upsell, expansion-revenue, renewal, territory, commission, sales-compensation, ae, pitch,
sales-pitch, lead-gen, lead-generation, ai-sdr, sales-agent (63 core) + sales-qualification,
product-led-sales, win-loss-analysis, sales-forecast, revenue-forecast, sales-methodology,
deal-management, marketing, customer-success (9 follow-up) = **72 total, all returned ≥1
result, none required the 60s-backoff-retry protocol.**

**Queries in the brief NOT run:** growth (adjacent probe — skipped; the lead's own corpus and
the `coreyhaines31` findings already establish the marketing/growth boundary question, and I
judged the remaining budget better spent on GitHub code-search cross-checks, which surfaced more
new packs per unit effort than a 73rd skills.sh call would have). No query returned an empty
result requiring the retry protocol, so there are no "unconfirmed emptiness" claims to log from
skills.sh itself.

**Emptiness claims and what surface backed them (per the lead's WebSearch-exhaustion ruling —
I used ZERO WebSearch calls in this file, so this ruling does not invalidate anything here):**
- "LeadMagic/gtm-skills has no forecast/win-loss skill" — backed by a **positive, direct `gh api
  repos/.../contents/skills/<dir>` listing** of all 24 category directories (not a search, a
  full enumeration) — this is the strongest possible evidence type, stronger than a search
  returning zero.
- "ncklrs/startup-os-skills has no win-loss skill" — same method, direct full directory listing
  of its 55 skills.
- "gtmagents/gtm-agents DOES have win-loss (win-loss-dataset)" — positive finding, confirmed via
  `marketplace.json` plugin manifest read directly.
- Forecasting/win-loss "not dominant/fragmented" claims (Q2, Q4) are based on skills.sh install
  counts actually returned (not on absence) — safe.

**GitHub-side gaps (time-boxed, not exhaustive):**
- Did not read full SKILL.md content for: `gtmagents/gtm-agents` beyond `forecast-discipline`
  (7 other sales-plugin skills read only via plugin.json descriptions, not full SKILL.md prose);
  `ncklrs/startup-os-skills` beyond the 6 skills quoted in §Pack notes; `guia-matthieu/
  clawfu-skills` beyond directory listings + names (no full SKILL.md reads — already flagged to
  A3 per lead note, so treated as lower priority here); `louisblythe/sales-skills` beyond 1 skill
  (`ideal-customer-profile-matching`) and its repo description.
- Did not verify license files for any pack in this table except TheCraigHewitt (MIT, read
  directly) and `louisblythe/sales-skills` (confirmed **no license** via GitHub API `license`
  field). Every other A/B-grade pack's license is **unverified by me** — flag to A3/licensing
  for the standard 7-clause pass, especially `gtmagents/gtm-agents` (large marketplace, likely
  multi-license), `LeadMagic/gtm-skills`, `ncklrs/startup-os-skills`, `guia-matthieu/
  clawfu-skills` (partially on A3's list already per lead), `doris-labs/sales-skills`,
  `jmbluhm/b2b-sales-skills`.
- **`sales-skills/sales` (skillId `sales-do`) anomaly, unresolved**: the GitHub org
  `sales-skills` exists (`gh api orgs/sales-skills`, created 2026-03-19, 1 public repo) and its
  org repo-listing endpoint reports `sales-skills/sales` with `license: null`, but a direct
  `gh api repos/sales-skills/sales` call returns **404 Not Found** on two separate attempts.
  This is inconsistent and I could not resolve it in budget — could be a visibility/permissions
  quirk, a just-deleted/renamed repo, or a skills.sh source string that doesn't map cleanly to a
  fetchable GitHub API endpoint (same failure class as the lead's non-GitHub-source warning,
  though the org itself is real). **Flag to A3: verify via browser or fresh `gh` call before
  citing anything from this source; do not treat the org's existence as proof the repo/license
  is fetchable.**
- `claude-office-skills/skills` (crm-automation 4421, lead-qualification 3641, customer-success
  3740, pipedrive-automation 3570 — all high-install, all touched here) — I did not attempt to
  resolve its upstream GitHub org/repo at all; flag to A3 as an unverified-identity high-install
  source.
- Adjacent probes for `customer-success` and `marketing` were run only as single skills.sh
  queries (see census table) — not a full census of those two packs' sales-claiming content;
  per the brief's instruction, this was intentionally shallow ("do not census them exhaustively").
- I did not check `travisvn/awesome-claude-skills`, `ComposioHQ/awesome-claude-skills`, or
  `Jeffallan/claude-skills` beyond confirming they are curated list/unrelated-domain repos (not
  content repos) per the lead's request — `sickn33/agentic-awesome-skills` (the fourth repo the
  lead named, actually `sickn33/agentic-awesome-skills` not `antigravity-awesome-skills` as
  typed) WAS checked and is in the census table above (grade C, aggregator).

**Method limitation to log for the controller (independent confirmation of raw-a0's gotcha):**
skills.sh's `q=lenny` style search did not surface `LeadMagic/gtm-skills` under any of the 72
queries run despite `lead-generation`/`prospecting`/`gtm` all being in the query set — it was
found only via `gh api search/code?q=MEDDICC+filename:SKILL.md`. Large multi-category repos with
generic per-skill names (no "sales" or "gtm" token in many individual skill names) appear to be
systematically under-indexed by skills.sh's apparent per-skill-description matching. **Any
synthesis step that ranks "how contested is this niche" purely off skills.sh install/hit counts
will underweight large, low-adoption, high-breadth repos like LeadMagic and louisblythe — which
are exactly the ones most relevant to a BREADTH ranking.**
