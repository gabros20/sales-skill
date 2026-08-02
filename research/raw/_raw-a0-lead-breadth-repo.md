# _raw-a0 (lead) — the breadth repo nobody was assigned: `alirezarezvani/claude-skills`

Author: Channel A lead. Date: 2026-08-03.
Scope: a repo that did NOT surface in the lead's skills.sh calibration queries for `sales`/`gtm`/`crm`,
found instead via `gh search repos`. It is the largest and most architecturally serious incumbent in
the channel. Workers A1/A2 were not briefed on it (A3 has it on the license list only), so the lead
took it.

**Method note / gotcha for the family:** skills.sh semantic search did not return this repo's
commercial skills for `sales`, `gtm`, `crm`, or `forecasting`. It is indexed on skills.sh (its
`sales-engineer` skill appeared at 743 installs under `q=sales`), but its *strongest* sales-adjacent
content — the whole `commercial/` plugin — never surfaced. **skills.sh search alone is not a census.**
Cross-check with `gh search repos` / `gh api search/code`. This repeats success's channel-A caveat
("the search is semantic and lossy") with a concrete new instance.

**Second gotcha (shell):** in zsh, an unquoted `$VAR` containing two paths does **not** word-split, so
`find $C -name '*.md'` silently searches one non-existent path and returns zero for everything. Two
coverage greps returned all-zeros before this was caught. Zero results from a shell loop deserve the
same suspicion as an empty API response. Also `grep -o` combined with `-l` is a no-op conflict.

---

## 1. Repo identity (verified)

| Field | Value |
|---|---|
| full_name | `alirezarezvani/claude-skills` (no rename/redirect observed) |
| URL | https://github.com/alirezarezvani/claude-skills |
| Stars / forks | **23,656★** / 3,281 (`gh api repos/...`, 2026-08-03) |
| Last push | 2026-07-17T13:02:50Z |
| Self-description | "345 Claude Code skills & agent skills & plugins … engineering, marketing, product, compliance, C-level advisory, research, business operations, **commercial & finance**" |
| GitHub API `license.spdx_id` | `MIT` |
| Root LICENSE (file opened) | `MIT License / Copyright (c) 2025 Alireza Rezvani` — **API AGREES** |
| Manifest | `commercial/.claude-plugin/plugin.json` → `"license": "MIT"`, `"version": "2.9.0"` — consistent |
| Skill frontmatter | all 10 `SKILL.md` files under `commercial/` + `business-growth/` carry `license: MIT` — consistent |

**Clause-2 (every license file) — full sweep done at any depth, `.git` pruned. SIX license files,
FIVE distinct copyright holders, all MIT:**

| Path | Copyright | Governs |
|---|---|---|
| `LICENSE` | MIT © 2025 **Alireza Rezvani** | repo root — **covers `commercial/` and `business-growth/`, our citation targets** |
| `loop-library/LICENSE` | MIT © 2026 **Forward Future** | `loop-library/` |
| `engineering/skillopt-sleep/LICENSE` | MIT © 2026 **Microsoft Corporation** | that skill |
| `engineering/collab-proof/LICENSE` | MIT © 2026 **dong7812** | that skill |
| `engineering-team/self-improving-agent/LICENSE` | MIT © 2026 **Reza Rezvani** | that skill |
| `engineering-team/playwright-pro/LICENSE` | MIT © 2026 **Reza Rezvani** | that skill |

(`engineering/skills/dependency-auditor/references/license_compatibility_matrix.md` and
`.../scripts/license_checker.py` match the filename sweep but are *subject-matter* files about
licensing, not licenses. Excluded — noted so the next reader does not re-flag them.)

Verdict: **MIT, citable with attribution.** The API's bare "MIT" is *correct but concealing*: it hides
that this repo is partly a **vendored aggregation of third-party work** — at least five copyright
holders, one of them Microsoft. That is a fact about the ecosystem worth carrying (a "345 skills" repo
is not 345 skills one author wrote), and it is a new clause-2 instance for the family's licensing rule:
*same SPDX across every file can still mean multiple owners.* For our purposes the citation path is
clean — nothing under `commercial/` or `business-growth/` is third-party-vendored, and the root MIT ©
Alireza Rezvani plus 10 consistent frontmatter declarations govern everything we would cite.

Nothing here is left for A3 on this repo; A3 should treat it as **verified to all 7 clauses by the
lead** and spend its budget elsewhere. Rename check: `gh api repos/alirezarezvani/claude-skills --jq
.full_name` returns the requested name — no redirect.

## 2. Why it matters: it is architecturally the closest thing to our own family design

`commercial/` is a plugin (`plugin.json` v2.9.0) of 7 skills + 1 orchestrator, 103 paths. Each skill is
a router `SKILL.md` + `references/*_canon.md` + `references/*_anti_patterns.md` + `assets/*_template.md`
+ `scripts/*.py` (stdlib-only, `--help`/`--sample` on all). Self-described as "21 stdlib-only Python
tools, 28+ reference docs."

Commercial skills: `pricing-strategist`, `deal-desk`, `partnerships-architect`, `channel-economics`,
`commercial-policy`, `rfp-responder`, `commercial-forecaster`, `commercial-skills` (orchestrator).
Adjacent `business-growth/skills/`: `revenue-operations`, `sales-engineer`,
`contract-and-proposal-writer`, `customer-success-manager`.

It also ships slash commands (`commercial/commands/cs-commercial-forecast.md`, `cs-deal-review.md`,
`cs-pricing-strategy.md`, `cs-rfp-respond.md`, …) and an orchestrator agent
(`commercial/agents/cs-commercial-orchestrator.md`). This is a router + references + runnable-assets
+ agentic-surface pack — i.e. **the same shape we ship.** Do not describe this ecosystem as
architecturally naive. It is not.

## 3. It already occupies our FLAGSHIP framing — forecasting honesty

`commercial/skills/commercial-forecaster/SKILL.md` (v2.8.0). Source:
https://github.com/alirezarezvani/claude-skills/blob/main/commercial/skills/commercial-forecaster/SKILL.md

Quotes (verbatim):
- description: "…without **the theatre of a single undefended number**. … Every output explicitly names
  the conversion rate used, the data window, and the weighting choice."
- "The skill recommends **three forecast numbers + an explicit assumption block**. The CRO presents the
  number, the board sees the assumptions, **the theatre dies**."
- "**The assumption block is non-optional.** If you remove it, the forecast becomes theatre."
- "If the slide has a single number and no assumption block, the slide is theatre."
- Hard rule 1: "**Forecast without disclosed assumptions is theatre.** … Manual suppression of the
  assumption block makes the human responsible for the theatre."

Mechanism: 3-tier commit / best-case / pipe-only; per-cohort NRR/GRR with leaky-cohort callout; and a
per-stage **coefficient-of-variation confidence band** (`CoV = StDev / Mean`; HIGH <10%, MEDIUM 10–25%,
LOW 25–50%, VERY LOW >50%) recommending `extend-data-window` / `treat-as-soft-floor` / `commit-quality`
per stage. Scripts: `bookings_forecaster.py`, `cohort_arr_projector.py`, `funnel_confidence_scorer.py`.

**This is a real, specific, non-trivial treatment of "what can a pipeline number honestly predict."**
Our flagship framing MUST account for it and cannot claim virgin territory — the same constraint
`t0ddc3by/claude-for-customer-success` placed on success's health-score flagship (success
`skills-ecosystem-report.md` §3.3). Grade: **A / threat HIGH on framing.**

## 4. …but its evidence layer is empty — and this is the sharpest instance of the family wedge yet

The wedge is NOT "it cites nothing." It is worse and more precise:

**It has adopted the FORM of citation without the FUNCTION.** It has a `references/` directory, files
named `*_canon.md`, explicit "Sources:" lines, and named authorities — and not one resolvable claim.

Grep-verified over the `commercial/` + `business-growth/` markdown corpus (74 files, **11,105 lines**):
- Total `http(s)://` occurrences: **48**; unique URLs: **30**.
- URLs that are a bare homepage or a topic-index page: **~22 of 30** (`https://tomtunguz.com/`,
  `https://www.saastr.com/`, `https://www.bvp.com/atlas`, `https://openviewpartners.com/`,
  `https://www.forrester.com/research/`, `https://winningbydesign.com/`, `https://www.paddle.com/resources`,
  `https://www.ycombinator.com/library`, …).
- **Permalinks to a specific figure, report page, table, or paper: ZERO.**
- One "source" is a **faculty directory page**: `https://mitsloan.mit.edu/faculty/directory/robert-gibbons`.
- One counted URL is a **placeholder example**: `https://trust.example.com/soc2-2026.pdf`.
- `commercial-forecaster/references/saas_forecasting_canon.md` (152 lines) — **0 links.**
- `commercial-forecaster/references/forecast_anti_patterns.md` (187 lines) — **0 links.**
- `rfp-responder/references/shipley_method_canon.md` (64 lines) — **0 links.**

Yet those three files name: Skok, Tunguz, OpenView, BVP, **Pacific Crest/KeyBanc**, ProfitWell, Patrick
Campbell, McKinsey, MIT Sloan, Bain, Forrester, Andrew Chen (a16z), Brian Balfour, Ramanujam, Lenny
Rachitsky, Reforge (per the SKILL.md "References" block, verbatim).

**The worst instance — an executed uncited table.** `saas_forecasting_canon.md` ships a 30-cell
stage-conversion benchmark table (discovery/demo_completed/proposal/negotiation/verbal/commit ×
saas/api/enterprise-software/marketplace/services) whose entire provenance is one bare line:

> `Sources: KeyBanc SaaS Survey, OpenView benchmarks, Bessemer Atlas. Profile picker is a starting prior, not a prescription.`

No link, no year, no edition, no page. **These numbers are then consumed as default priors by
`bookings_forecaster.py`** — i.e. unverifiable figures drive a computation the reader is told to put in
front of a board. This is the strongest single artifact in the channel for our measurement-honesty
line: the pack that says *"forecast without disclosed assumptions is theatre"* ships the assumptions
themselves as undisclosed.

**Cross-check available:** the charter records KBCM/KeyBanc AE quota attainment (~70→75%) as already
primary-verified in success's corpus. Channel B/C should determine whether the KeyBanc SaaS Survey
publishes per-stage conversion rates **at all** — if it does not, this table's attribution is not merely
unlinked but false. Flagged, NOT concluded.

**The irony worth using.** `shipley_method_canon.md` quotes the APMP Body of Knowledge in quotation
marks — *"every assertion in a proposal must be backed by evidence the evaluator can independently
verify"* — uncited, in a file where zero assertions are independently verifiable.

## 5. Candidate never-ship figures harvested here

All from `alirezarezvani/claude-skills`, all **UNSOURCED** (0 links in their containing files). Graded
against the charter's R21 rule (collect only if the reader must recognise-and-correct it, or its
arithmetic is the teaching).

| Figure (verbatim) | File | R21 |
|---|---|---|
| "By the time the RFP issues, **70-80% of the eventual outcome is determined by the capture work** done in the preceding 6-18 months" | `rfp-responder/references/shipley_method_canon.md` | **(a) YES** — same folklore shape as the charter's "57% of the buying decision happens before sales contact"; a reader will meet it |
| 30-cell stage-conversion prior table, attributed to "KeyBanc SaaS Survey, OpenView benchmarks, Bessemer Atlas" | `commercial-forecaster/references/saas_forecasting_canon.md` L125–131 | **(a)+(b) YES** — it is executed by `bookings_forecaster.py`; the arithmetic IS the teaching |
| "Top-quartile SaaS companies hit commit within 5%; bottom-quartile miss by 25%+" | same, L75 | (a) YES |
| "Hockey-stick forecasts (best-case > 80% of pipe-only) have **2x lower realization rate**" | same, L76 | (a) YES |
| "Pipeline coverage **3.0x is the floor**" / "SaaS-industry floor: 3.0x" / "top-quartile 3.0-4.5x, median ~3.0x, bottom-quartile <2.5x" | same, L49–50, L60, L77, L90, L146 | (a) YES — repeated 5× as settled fact; the single most load-bearing uncited number in the pack |
| "Forecast accuracy degrades sharply for stages with CoV > 25%" | same, L69 | (a) YES |
| "Cohort decomposition is **mandatory above $50M ARR**" | same, L85, L152 | (a) YES |
| "100% NRR = 'good', 110% = 'better', 120%+ = 'best'" | same, L83 | (a) — note charter's NRR-vs-growth collision flag from success |

Stalled-opp rule (`opp age > 2x median stage age AND last_activity > 45 days → × 0.5`, L29) is also
unsourced but is a heuristic, not a benchmark — record, do not treat as a figure.

## 6. What it does NOT cover — the wedge, grep-verified

Coverage of the charter's 14 includes across `commercial/` + `business-growth/` markdown
(`find … -exec grep -il`, file counts):

| Term | Files | Read |
|---|---:|---|
| pipeline | 31 | **owned** |
| proposal | 28 | **owned** |
| forecast | 24 | **owned** |
| CRM | 15 | substantial |
| outbound | 6 | thin |
| objection | 4 | see below |
| win/loss | 4 | thin |
| ideal customer profile | 2 | name-drop |
| exit criteria | 2 | name-drop |
| handoff | 2 | name-drop |
| MEDDIC | 1 | name-drop |
| BANT | 1 | name-drop |
| **account selection** | **0** | absent |
| **SPIN selling** | **0** | absent |
| **Challenger sale** | **0** | absent |
| **cold email** | **0** | absent |
| **prospecting** | **0** | absent |
| discovery call | 1 | name-drop |

The division is clean and it is our opening:

> **It owns the deal-ECONOMICS layer (forecast, pricing, discount policy, RFP, partnerships, channel,
> deal desk). It does not own the buying CONVERSATION or the qualification layer.** Top-of-funnel
> (account selection, prospecting, cold email) is at literal zero.

Two specific proofs that the qualification layer is a shell, not content:

1. **BANT/MEDDPICC is a checkbox, never taught.** The only BANT occurrence is a bullet in an
   exit-criteria list: `business-growth/skills/revenue-operations/references/pipeline-management-framework.md:33`
   — "- MEDDPICC or BANT qualification framework completed". The framework is named as a gate item and
   its content never appears. (Useful for us: it does NOT reproduce trademarked methodology content —
   so on the charter's cite-never-reproduce rule this pack is *compliant by omission*, not by
   discipline. The reproduction risk to watch is `shipley_method_canon.md`, which distils Shipley
   Associates' commercial methodology at 64 lines with zero attribution links.)

2. **A router row that does not reach its content.** `pricing-strategist/SKILL.md:104` sends the reader
   to deal-desk for MEDDIC — "**deal-desk** — per-deal discount approval, MEDDIC, deal scoring."
   `grep -ril meddic commercial/skills/deal-desk/` returns **0 files**. The cross-reference promises
   content that does not exist. (Our own family shipped this exact defect class in the marketing build
   — "router rows must reach the content they promise." Independent confirmation it is a genre-wide
   failure mode, not just ours.)

Also relevant to our seam contracts: **objection handling is filed under MARKETING here.** `gh api
search/code` for "objection handling" in this repo returns `marketing-skill/skills/copywriting/SKILL.md`,
`marketing-skill/skills/marketing-strategy-pmm/SKILL.md`, `marketing-skill/skills/page-cro/SKILL.md`,
and `business-growth/skills/sales-engineer/SKILL.md`. This is precisely the blend our marketing pack
explicitly refused (charter: "the incumbent genre routinely blends these into marketing; this pack does
not," marketing `handoff.md:42`). **Independent external evidence that our marketing→sales seam
ruling is the non-default choice** — worth citing in the pack as a live contrast, not just an assertion.

## 7. Verdict

**Threat: HIGH on the forecasting flagship's framing, LOW on the pack as a whole.**

- It is a 23.6k★ MIT pack with our architecture, already saying "undefended forecast numbers are
  theatre," with runnable scripts. We cannot present that thesis as unclaimed.
- But it defends that thesis with an evidence layer of 30 homepage URLs and zero permalinks across
  11,105 lines, and it ships an executed benchmark table whose attribution is one unlinked sentence.
- And it is a **commercial/RevOps** pack, not a **selling** pack: qualification, discovery, objections,
  ICP/account selection, prospecting and win/loss are name-drops or zeros.

Sharpened wedge statement for the channel report: *the ecosystem's best forecasting content already
knows that a number without its assumptions is theatre — and then does the same thing one level down,
because its own priors arrive unsourced. Doing this properly is not a new thesis; it is the first
honest execution of an existing one.* That is a narrower and more defensible claim than "nobody
thought of this," and it matches the quality-skill precedent (first NARROW wedge, justified on a
grep-verified empty layer).

## 8. Coverage statement — what the lead did NOT do here

**Search-surface provenance (per the controller's WebSearch-quota ruling).** Nothing in this file
touched WebSearch. Every claim here is backed by one of: `gh api repos/…`, `gh api search/code`,
`gh search repos`, `curl` to `raw.githubusercontent.com`, or a local `git clone --depth 1` grep. All
four surfaces were live throughout. **No null/emptiness finding in this file rests on a WebSearch
result**, so none of it falls under the re-verification ruling. The zeros in §6 are `grep -il` counts
over a cloned working tree — reproducible offline, not search-derived.

- Read in full: `commercial-forecaster/SKILL.md`, `saas_forecasting_canon.md` (numeric lines + calibration
  section + hard rules), `shipley_method_canon.md` (first 30 of 64 lines), `commercial/plugin.json`,
  root + `loop-library/` LICENSE.
- **Not read:** `deal-desk`, `commercial-policy`, `channel-economics`, `partnerships-architect`,
  `pricing-strategist` (beyond the MEDDIC line), `revenue-operations` references
  (`revops-metrics-guide.md`, `gtm-efficiency-benchmarks.md`, `pipeline-management-framework.md` beyond
  the BANT line), `sales-engineer` + its `demo_script_template.md`, `contract-and-proposal-writer`,
  `customer-success-manager`, the `commands/` and `agents/` surfaces, and **all 21 Python scripts** —
  none were executed or read. Claims about script behaviour above are taken from SKILL.md prose and are
  marked as such; they are **UNVERIFIED at the code level.**
- **Not checked:** per-skill LICENSE files below `maxdepth 2`; whether `business-growth/` or the other
  13 top-level categories contain further sales content; the `docs/skills/**` mirror (appears to be a
  generated duplicate of each SKILL.md — assumed, **not verified**).
- **Not done:** any comparison of this pack's figures against primary sources. Every "UNSOURCED" grade
  above means "no link in the containing file," **not** "the claim is false." Whether KeyBanc/OpenView/
  Bessemer actually publish these numbers is Channel B/C work and is flagged, not concluded.
- The clone used is at `…/scratchpad/arz2` (shallow, HEAD = 2026-07-17 push) for anyone re-checking.
