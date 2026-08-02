# Channel A · skills-ecosystem census — report

Date: 2026-08-03 · Lead: channel-A sub-orchestrator (opus) · Workers: 3 × sonnet
Charter: `research/charter.md` · Every claim below traces to a raw file listed here.

**Source files:**
- [`raw/_raw-a0-lead-breadth-repo.md`](raw/_raw-a0-lead-breadth-repo.md) — **lead**: `alirezarezvani/claude-skills` (23.6k★) deep-read + full 7-clause licensing; the repo skills.sh hides
- [`raw/_raw-a1-ecosystem-breadth.md`](raw/_raw-a1-ecosystem-breadth.md) — A1: 72 live skills.sh queries + `gh` cross-checks; 25-row census sorted by breadth
- [`raw/_raw-a2-incumbent-deepread.md`](raw/_raw-a2-incumbent-deepread.md) — A2: 7 incumbents read in full, 618 lines, unsourced-figure harvest, trademark audit
- [`raw/_raw-a3-licensing.md`](raw/_raw-a3-licensing.md) — A3: 24-row licensing ledger, Tier-3 resolution, official-pack sweep

---

## 1. Verdict

**OPEN BY FRAGMENTATION *AND* ADOPTION COLLAPSE — tilting to CONTESTED on specific items.**

This is close to success's verdict but with a distinct and sharper mechanism. Success faced three
disjoint camps that each covered part of the ground. Sales faces something more uncomfortable:

> **Several people have already built 9–13 of our 14 items, some of it well. Not one of them has
> adoption. Meanwhile the packs with adoption do not cover the domain.** (A1 §3.1, verbatim: *"The
> wedge is not 'nobody has built this,' it's 'several people have built pieces of this well, and
> nobody has adoption while doing it.'"*)

The distribution makes this concrete. **Breadth and installs are inversely correlated:**

| Pack | Breadth | Installs/skill | Content quality |
|---|---|---|---|
| `gtmagents/gtm-agents` | **~12–13/14** | 55–495 | generic/templated (A1 read a full SKILL.md) |
| `louisblythe/sales-skills` (122 skills) | ~10–11/14 | 44–260 | AI-bot behaviour, not a human playbook; **UNLICENSED** |
| `TheCraigHewitt/sales-skills` (21 skills) | ~9–10/14 | **9–43** | real, differentiated, well-written; MIT |
| `ncklrs/startup-os-skills` | ~10/14 | 137–552 | real per-skill depth; **UNLICENSED** |
| `guia-matthieu/clawfu-skills` | ~10/14 | 150–550 | best named-methodology coverage found |
| `LeadMagic/gtm-skills` (~130 skills) | ~7/14 | **3–6** | largest repo by skill count; forecast + win-loss **confirmed absent** |
| — | — | — | — |
| `coreyhaines31/marketingskills` (**marketing-filed**) | ~7/14 across 4 skills | **32k–89k** | the field's actual centre of gravity |
| `anthropics/knowledge-work-plugins/sales` | ~7–8/14 | 2,119–3,661 | official; only dedicated forecast skill with real adoption |

**No pack combines end-to-end coverage, non-templated depth, and meaningful adoption
simultaneously.** That triple is the opening — not novelty.

**Contested on specific items** (A1 §3.1): CRM / pipeline / proposal / pricing are contested by
`alirezarezvani` (deal economics) and `coreyhaines31` (at 100–1000× the install scale of any dedicated
sales pack); qualification/methodology is contested by `guia-matthieu/clawfu-skills` and
`jmbluhm/b2b-sales-skills`; discovery / demo / objection / win-loss / forecast-as-a-system is where the
genuinely broad, high-quality dedicated packs sit — **and none of them has adoption.**

**Two things the charter got wrong, corrected here:**

1. **The official ecosystem HAS staked a claim.** `anthropics/knowledge-work-plugins/sales` is a real,
   Apache-2.0, actively-pushed 9-skill occupant, self-described as *"Prospect, craft outreach, and build
   deal strategy faster. Prep for calls, manage your pipeline…"* (A3 §6). We cannot write "the official
   ecosystem hasn't touched sales."
2. **The marketing seam is contested at enormous scale.** `coreyhaines31/marketingskills` ships, **under
   its marketing plugin**, `revops` (81,381 installs — explicitly "marketing-to-sales handoff…lead
   qualification…pipeline stages…deal desk…CRM"), `prospecting` (32,221 — "ICP-fit accounts", "outbound
   list"), `cold-email` (89,060), `sales-enablement` (84,811). Our marketing pack's `handoff.md:42`
   cedes exactly these to sales, calling out that "the incumbent genre routinely blends these into
   marketing; this pack does not." **A1 §0 is in-the-wild proof that our seam ruling is the
   non-default choice, and that the field's centre of gravity disagrees with us by orders of magnitude
   in reach.**

   **Reframe (from Channel E, and it is the better framing): the family seam IS the differentiator
   against the biggest incumbent.** The largest player in this space annexes sales items from the
   *marketing* side of the boundary; our marketing pack already refused that annexation in writing,
   naming revops/enablement/outbound as sales's precisely *because* the genre blends them. So this is
   not a liability to defend — it is the one structural advantage a 14-pack family has that a single
   pack cannot copy. **Argue the seam explicitly and cite marketing's own cession row as evidence the
   line was drawn before the deal was in view.** (E's build invariant 1: mirror marketing's row FIRM,
   no hedge.)

**The flagship opening is unchanged and is the strongest-evidenced in any build of this family** — see §3.

---

## 2. Top 5 incumbents by BREADTH (charter rule: not installs)

Ranking revised after A1's census; A2's seven deep-read targets were **not** the broadest packs.

**1. `gtmagents/gtm-agents` — ~12–13/14. Broadest structural coverage found. Threat: MEDIUM.**
263-skill marketplace with a dedicated `sales` category (prospecting, pipeline incl. forecast-discipline
and deal-review, enablement, operations, coaching, account management, sales-calls with a MEDDIC
checklist, enterprise-sales), **plus `sales-handoff-orchestration` and a `win-loss-dataset`** — i.e. it
nominally covers both our contested handoff seam and our win/loss gap. Threat is capped by content:
A1 read a full SKILL.md and graded it generic/templated. **Breadth ≠ depth, and this is the clearest
instance.**

**2. `louisblythe/sales-skills` — ~10–11/14, 122+ micro-skills. Threat: MEDIUM (and the AI-SDR find).**
Designed for building an AI sales bot: `deal-review-win-loss`, `win-loss-reason-extraction`,
`time-to-close-prediction`, alongside bot mechanics (voicemail-drop-optimization, ghost-recovery,
response-latency-management). **This is a deeper AI-SDR-mechanics treatment than anything carrying the
literal `ai-sdr` tag.** **NO LICENSE FILE — all-rights-reserved by default. Cite only, never lift.**

**3. `anthropics/knowledge-work-plugins/sales` — ~7–8/14. THE occupant by credibility. Threat: HIGH.**
9 skills, Apache-2.0 (file-verified), 23,252★, pushed 2026-08-02. Its `forecast` (2,275 installs) is the
**highest-adoption dedicated forecasting skill in the entire sweep** — and the source of our sharpest
flagship exhibit (§3.1). Also ships `marketing`, `customer-support`, `finance` plugins: **seam-check our
handoffs against these before release.**

**4. `TheCraigHewitt/sales-skills` — ~9–10/14. Closest name-exact overlap with our scope. Threat: LOW-MEDIUM.**
21-skill dedicated sales pack, MIT, genuinely well-written: buyer-persona, discovery-call, demo-script,
objection-handling, proposal-pricing, pipeline-review, **forecast**, **win-loss-analysis**, negotiation,
call-debrief, outbound. **It is the only pack that ships both of our candidate flagship items by name and
does them well.** Installs: **9–43.** The clearest single illustration of the adoption-collapse thesis.
Its forecast skill even carries our honesty framing — *"forecasting is the most lied-about activity"*
(A1 §3.2c). **Read it in full before we write ours; do not assume we are first.**

**5. `guia-matthieu/clawfu-skills` — ~10/14. Best methodology literacy. Threat: MEDIUM on qualification.**
SPIN, Challenger, Sandler, MEDDIC, BANT and Voss negotiation each as **distinct named skills**, plus
`forecast-scenarios`, `pipeline-forecasting`, `deal-risk-scoring`, `lead-scoring`, ICP-matching. If any
pack contests our qualification chapter, it is this one. **UNLICENSED (A3 §5).**

Also material: **`github/awesome-copilot` gtm-*** (37,357★, MIT) — largest star count, but A1 establishes
it is a **mirror of `beingsmit/technical-product-gtm` (40★)** and only ~2–3/14 on our scope; its value to
us is the IP exhibit (§4.4), not competition. **`alirezarezvani/claude-skills`** (23.6k★) — ~5–6/14, owns
deal economics, contests our flagship framing (§3.2). **`LeadMagic/gtm-skills`** — ~130 skills across 24
categories and **forecast and win-loss are confirmed absent from all of them** (A1 verified directory by
directory): the largest GTM repo in the ecosystem has a hole at exactly our two flagship candidates.
**`hubspot/agent-cli-skills`** — vendor API driver, real workflow coverage, zero methodology teaching.
**`refoundai/lenny-skills`** — the only incumbent that reproduces a qualification framework *while
citing a source*.

---

## 3. The flagship: forecasting honesty is evidenced, not asserted

Forecasting is **not** an empty shelf (A1 §3.2 — real method exists in 4–5 places). It is a
**contested-but-thin shelf with no authoritative owner, where the honesty gap is present in the two
highest-credibility examples.** That is a better wedge than emptiness, because it cannot be dismissed as
a topic nobody wanted.

### 3.1 The official pack ships unsourced forecast defaults — lead-verified, and a worker gloss corrected

The lead fetched `anthropics/knowledge-work-plugins/sales/skills/forecast/SKILL.md` (214 lines) and read
it directly rather than trusting a line number (charter: a reconstructed permalink is a fabricated
citation). Present verbatim:

> `## Stage Probabilities (Default)` — "If you don't provide custom probabilities, I'll use:"
> Closed Won 100% · Negotiation/Contract 80% · Proposal/Quote 60% · Evaluation/Demo 40% ·
> Discovery/Qualification 20% · Prospecting/Lead 10%
>
> "3. **Coverage matters** — 3x pipeline coverage is healthy. Below 2x is risky."

**Correction to A1 (§3.2a), recorded per the charter's verify-the-claim-in-local-context rule.** A1
wrote that this skill *"honestly flags its own generic-prior limitation in its own copy."* **It does
not.** The lead grepped all 214 lines for limitation, caveat, accuracy, and validity language. What
actually exists is two things, neither of which is a disclosure:
- *"Tell me if your stages or probabilities are different"* — an **override invitation**, not a
  statement that the defaults are unvalidated.
- Under a conditional `## If CRM Connected` heading: *"Use your actual historical win rates"* — a
  **conditional improvement**, not a caveat on the defaults it ships to everyone else.

There is no accuracy discussion, no backtest, no source, and no statement of what the number can and
cannot predict. **The stronger framing survives verification: Anthropic's own official sales pack ships
hand-set forecast probabilities and an unsourced coverage benchmark as defaults.** This is exactly the
KBCM lesson from the success build — a worker's summary was more generous than the local context
supported, and checking the file changed the finding.

### 3.2 The best incumbent states our thesis, then violates it one level down

`alirezarezvani`'s `commercial-forecaster` (v2.8.0) is not naive. Verbatim: *"the theatre of a single
undefended number"*; *"The assumption block is non-optional. If you remove it, the forecast becomes
theatre."* It ships 3-tier commit/best-case/pipe-only and per-stage coefficient-of-variation confidence
bands with runnable scripts.

Then its `references/saas_forecasting_canon.md` ships a **30-cell stage-conversion benchmark table**
whose entire provenance is one unlinked line — *"Sources: KeyBanc SaaS Survey, OpenView benchmarks,
Bessemer Atlas"* — and **those numbers are executed as default priors by `bookings_forecaster.py`.**

Grep-verified across its `commercial/` + `business-growth/` corpus (**74 files, 11,105 lines**): 48
`http(s)` occurrences, **30 unique URLs, ZERO permalinks to a specific figure, report, table or paper.**
~22 of 30 are bare homepages or topic indexes; one "source" is a **faculty directory page**; one counted
URL is a **placeholder** (`trust.example.com`).

**So the wedge is not "the incumbents cite nothing." It is that the genre has adopted the FORM of
citation — a `references/` directory, files named `*_canon.md`, explicit "Sources:" lines, named
authorities — without the FUNCTION: not one resolvable claim.** That statement survives the obvious
objection ("but they do have references"), which "cites nothing" does not.

### 3.3 Convergence: one uncited number in three independent packs

The strongest single exhibit. **"3x pipeline coverage"** appears, uncited, in three packs with no
citation relationship to each other — found independently by the lead and by A2:

| Pack | Wording | Provenance offered |
|---|---|---|
| `anthropics/knowledge-work-plugins` `sales/forecast` | "3x pipeline coverage is healthy. Below 2x is risky" | none |
| `alirezarezvani` `saas_forecasting_canon.md` | "SaaS-industry floor: 3.0x" (**5×**); "top-quartile 3.0–4.5x, median ~3.0x" | "KeyBanc SaaS Survey, OpenView, Bessemer Atlas" — no link |
| `coreyhaines31/marketingskills` `revops` | "coverage 3-4x" in a benchmark table | none |

Three packs, one number, zero traceable sources — **folklore propagation caught in the act.** It also
gives the pack a concrete teaching artifact under R21(a): the reader *will* meet this number.

**Cross-channel corroboration (do not re-derive).** C2 found GitLab's handbook — the most open sales
handbook in existence — has **forecasting as a NULL**: the real method is internal-only (403) and the
public heuristic is a "33% assumed win rate" that GitLab itself explicitly marks as non-measured. The
one organisation that publishes everything does not publish a validated forecast method. **There may be
no defensible public stage-weighted forecast method at all, and saying so plainly is the contribution.**

**Open item for Channel B/C — flagged, NOT concluded.** Does the KeyBanc/KBCM SaaS Survey publish
per-stage conversion rates *at all*? The charter records KBCM AE quota attainment (~70→75%) as already
primary-verified in success's corpus, so a live primary route exists. If KeyBanc publishes no such
table, `alirezarezvani`'s attribution is not merely unlinked but **false** — materially stronger. Do not
assert without checking.

---

## 4. Licensing (7 clauses) — and a surprise

### 4.1 The GitHub API told the truth this run — 23 of 23

**A3 found ZERO disagreements** between `license.spdx_id` and the actual file across every reachable
GitHub repo verified. This contradicts the family's standing prior ("lied ≥13 times in one prior run").
Reported as an honest negative.

**Do not weaken the rule** — it earned its place and the failure mode is silent. But this run must not be
cited as further evidence of a high lie rate, and family memory should record that **the lie rate is
variable, not constant.** The one apparent divergence (`twentyhq/twenty`, API = `NOASSERTION`) is A3's
judgment that the **API was more accurate than the repo's own `package.json`**, which claims a flat
`"AGPL-3.0"` and conceals the real complexity. Not counted as a lie.

### 4.2 Proposed 8th clause: identical SPDX ≠ single owner

Lead finding on `alirezarezvani/claude-skills`: **six license files, all MIT, five distinct copyright
holders** — Alireza Rezvani (root), Forward Future, **Microsoft Corporation**, dong7812, Reza Rezvani.
The API's bare "MIT" was *correct but concealing*: a "345 skills" repo is not 345 skills one author wrote.

Confirmed genre-wide, not a one-off: `github/awesome-copilot`'s entire gtm-* family is **vendored from
`beingsmit/technical-product-gtm` (40★)** via a frontmatter `metadata.source` — 40★ of content
distributed at 37k★ of reach. `sickn33/agentic-awesome-skills` (44.3k★) re-hosts `coreyhaines31` content
per its own `source:` field. **Aggregators inflate ecosystem skill-counts without adding original work.**

**Proposed clause:** *record the set of distinct copyright holders, not just the SPDX string.* Exclude
two filename false-positives: `references/license_compatibility_matrix.md` and `scripts/license_checker.py`
are subject-matter files *about* licensing.

### 4.3 Ledger rows

| Repo | License (file opened) | Citable? |
|---|---|---|
| `anthropics/knowledge-work-plugins` | Apache-2.0 (root + `sales/LICENSE`) | **YES** |
| `github/awesome-copilot` | MIT | YES-WITH-ATTRIBUTION (note vendored provenance) |
| `beingsmit/technical-product-gtm` | MIT, 40★ | YES-WITH-ATTRIBUTION — **the true author of the gtm-* content** |
| `alirezarezvani/claude-skills` | MIT © Alireza Rezvani (root governs `commercial/`, `business-growth/`); 5 holders / 6 files | YES-WITH-ATTRIBUTION — verified to all 7 clauses by the lead |
| `TheCraigHewitt/sales-skills` | MIT (per A1) — **A3 did not verify; confirm before citing** | **VERIFY FIRST** |
| `coreyhaines31/marketingskills` | MIT © Corey Haines | YES-WITH-ATTRIBUTION |
| `twentyhq/twenty` | **Composite**: AGPLv3 majority + `/* @license Enterprise */` proprietary carve-out + MIT sub-packages (`twenty-sdk`, `twenty-ui`, `twenty-client-sdk`, `twenty-shared`, `create-twenty-app`) + an AGPLv3 §7 **"Twenty Application Exception"** for apps using only published Application Interfaces; trademark rights NOT granted | YES-WITH-ATTRIBUTION — **never represent Enterprise-marked files as open source** |
| `louisblythe/sales-skills` | **NO LICENSE FILE** (`license: null`) | **NO — cite only** |
| `chadboyda/agent-gtm-skills` | **EFFECTIVELY UNLICENSED** (dangling README claim) | **NO — cite only** |
| `Cold-IQ/ColdIQ-s-GTM-Skills` (renamed from `sachacoldiq/…`) | **EFFECTIVELY UNLICENSED** | **NO — cite only** |
| `getcargohq/cargo-skills`, `ncklrs/startup-os-skills`, `membranedev/application-skills` | **EFFECTIVELY UNLICENSED** | **NO — cite only** |
| `ComposioHQ/awesome-claude-skills` | own content EFFECTIVELY UNLICENSED despite blanket README claim | **NO** for its own content |
| `sales-skills/sales` | org resolves, **repo 404s** — anomalous; A3: NOT CITABLE | **NO** |
| `code.deepline.com/deepline-gtm`, `oxygen-agent.com/oxygen-gtm` | **NO DISCOVERABLE LICENSE** (live pages read; two independent fetch methods for oxygen) | **NO** |
| `code.deepline.com/gtm-meta-skill` | **UNVERIFIED** — real page never located; A3 correctly refused to declare it license-less | **NO (unverified)** |
| `gtmagents/gtm-agents`, `guia-matthieu/clawfu-skills`, `LeadMagic/gtm-skills`, `doris-labs/sales-skills`, `jmbluhm/b2b-sales-skills` | **NOT VERIFIED** — surfaced by A1 after A3's list was fixed | **VERIFY BEFORE CITING** |

**Renames found (cite current names — redirects let stale citations pass review):**
- `sachacoldiq/coldiq-s-gtm-skills` → **`Cold-IQ/ColdIQ-s-GTM-Skills`** (verified genuine)
- `sickn33/antigravity-awesome-skills` → **`sickn33/agentic-awesome-skills`** (44,308★, MIT). The old
  name does not resolve; `gh api` redirects silently. Note this one appeared in the charter's own seed
  list under the stale name.

### 4.4 Trademarked-methodology reproduction — one serious exhibit

**`github/awesome-copilot/skills/gtm-enterprise-account-planning/SKILL.md` reproduces MEDDICC
letter-by-letter** — Metrics, Economic Buyer, Decision Criteria, Decision Process, Identified Pain,
Champion, Competition — as a first-class "Core Framework", **with zero attribution**, in an MIT file, in
a repo under the `github` org at 37,357★. Lead-verified verbatim: 429-line file, **2 outbound links
total**, one of which is the author's LinkedIn.

**This ties to Channel D's primary-sourced 2026 trademark ruling on the MEDDICC marks.** It is our
clearest licensing/ethics exhibit, the justification for cite-never-reproduce, and a differentiation
point we can state without smugness.

Contrast to carry: `refoundai/lenny-skills` reproduces MEDDIC's six letters **but cites an external
source** — meaningfully lower risk. `coreyhaines31` only *mentions* "BANT, MEDDIC, or your framework" —
lowest. **`guia-matthieu/clawfu-skills` ships `spin-selling`, `challenger-sale`, `sandler-system`,
`meddic-scorecard` and `never-split-difference` as named skills and is UNLICENSED — A2 did not read it,
so its reproduction discipline is UNASSESSED. This is the highest-priority remaining IP check.**
A2 confirmed no incumbent *it read* reproduces SPIN, Challenger, Sandler or Gap Selling content.

---

## 5. Candidate never-ship figures

**The full 18-row table with blob permalinks is A2 §(b)** — work from it, not this summary.

**Tier 1 — the reader will meet these and must be able to correct them (R21(a)):**

| Figure | Where | Grade |
|---|---|---|
| **"3x pipeline coverage is healthy / 3.0x is the floor"** | 3 independent packs incl. **official Anthropic** | **FOLKLORE — flagship exhibit (§3.3)** |
| Forecast stage probabilities 10/20/40/60/80/100% | `anthropics/.../sales/forecast` | FOLKLORE default; override invited, **never validated** (§3.1) |
| 30-cell stage-conversion table, "Sources: KeyBanc/OpenView/Bessemer" | `alirezarezvani` `saas_forecasting_canon.md` | **FOLKLORE + R21(b)** — its arithmetic IS the teaching; a script executes it |
| "Contact within 5 minutes = 21x more likely to qualify" | `coreyhaines31` `revops` | CONTESTED — classic misattributed speed-to-lead figure, source name only, no link |
| "85% of AI-SDR deployments fail within 6 months" ("2026 data") | `chadboyda` `sales-motion-design` | FOLKLORE — zero citation; **directly relevant to the AI-SDR strip** |
| "40–60% of B2B purchases end in no-decision" (JOLT, "2M+ calls") | `refoundai/lenny-skills` | CONFOUNDED — book via newsletter, no primary methodology |
| "Dialing up FOMO backfires 87% of the time" | `refoundai/lenny-skills` | FOLKLORE — Dixon's own claim, video-only source |

**Cross-channel: the "57%" genre now has three instances.** The charter flags *"57% of the buying
decision happens before sales contact"* (CEB origin, widely misquoted). Channel E independently found
webdesign's *"9 in 10 buyers rule out before contact"*, and this channel found Shipley's *"70-80% of
the eventual outcome is determined by capture work"* (`alirezarezvani` `shipley_method_canon.md`, zero
links in file). **Three variants of one folklore shape — a decision-already-made-before-you-arrive
figure — each with a different number and no traceable source.** Teaching the *shape* is more durable
than debunking any single figure; recommend the pack treat it as a genre, not three separate strips.

**Tier 2 — collect, do not lead with:** top-quartile commit within 5% / bottom-quartile miss 25%+;
hockey-stick forecasts "2x lower realization"; "cohort decomposition mandatory above $50M ARR";
"100/110/120% NRR = good/better/best" (**collides with success's flagged NRR-vs-growth issue — needs the
family ruling, not a fresh assertion**); the RevOps benchmark table (Lead→MQL 5–15% etc.);
pipeline-review weights 30/25/20/15/10%; "Value Ratio >10x = underpriced"; "1,400 GTM Engineer job
postings"; ColdIQ's "3-4x contract values", "36% vs 10% ABM meeting rate", "extra $2M ARR (case study)";
"Not once in 11 years" (stale-MAP).

---

## 6. Gaps — corrected

**A correction I nearly shipped, recorded because it is the family's recurring failure mode.** On A2's
seven targets alone, the evidence supported "no incumbent ships a genuine win/loss-learning skill." A1's
wider sweep **falsifies that as written**: `TheCraigHewitt/sales-skills/win-loss-analysis` (well-written),
`gtmagents/gtm-agents/win-loss-dataset` (with a `run-win-loss-program` command and `win-loss-analyst`
agent), and `louisblythe`'s `deal-review-win-loss` + `win-loss-reason-extraction` all exist. **This is the
quality-build lesson exactly — grep-verify uniqueness before asserting it — and a seven-repo deep-read is
not a uniqueness proof.**

The **defensible** version, which A1's evidence does support:

1. **Win/loss: no authoritative or adopted owner.** `gh api search/code q=win-loss filename:SKILL.md`
   returns 601 hits, the large majority single-skill personal repos, forks, and registry mirrors — an
   easy genre move an LLM can generate on request. Confirmed **absent** from `LeadMagic/gtm-skills`
   (~130 skills) and `ncklrs/startup-os-skills` (55 skills). Existing implementations top out in the low
   hundreds of installs. Our claim must be **quality and integration, never "first."**
2. **Forecast honesty: a real gap inside a contested shelf** — §3. Method exists in 4–5 places; the
   honesty caveat exists in none of the high-credibility ones. `TheCraigHewitt`'s forecast skill does
   carry the framing (*"the most lied-about activity"*) at 9–43 installs — **read it before writing ours.**
3. **The sales↔success handoff.** A2: none of its seven targets mention a CS-handoff methodology
   (closest: a bare "Closed Won → Customer success handoff" stage label, zero elaboration). **Caveat: A1
   found `gtmagents/gtm-agents/sales-handoff-orchestration` exists — UNREAD. Verify before claiming this
   gap.** Our contested seam with success is likely safe to reciprocate, but not on current evidence.
4. **Pricing PRESENTATION (vs design) is thin everywhere** — matches the product seam exactly.
5. **Nobody joins top-of-funnel to the deal system.** The deal-economics camp is at literal zero on
   account selection / prospecting / cold email; the outbound vendor packs cover only that. The join is
   ours to make.

---

## 7. Coverage statement

**Search-surface provenance (per the WebSearch-quota ruling).** WebSearch was exhausted session-wide
mid-run. **No claim in this report rests on a WebSearch result.**
- Lead: `gh api`, `gh api search/code`, `gh search repos`, `curl` to raw.githubusercontent, and greps
  over a local `git clone --depth 1`. All live throughout.
- A1: **72 skills.sh queries, all live, 0 confirmed rate-limit empties**, cross-checked with `gh api
  search/code`. Every emptiness claim names its backing query, per instruction.
- A2: `gh api` + raw.githubusercontent.
- A3: `curl` + `WebFetch`; re-verified its Tier-3 nulls by two independent fetch methods after the ruling
  and **downgraded one verdict to UNVERIFIED** rather than claim a null it could not stand behind.
- The `3x coverage` and MEDDICC exhibits were each verified **twice, independently** (worker + lead).

**Not covered / known gaps:**
- **7 of the 9 official Anthropic `sales/` skills are unread** (only `forecast` and `pipeline-review` in
  content). **Highest-priority remaining read** — it is the credible occupant. Its sibling `marketing`,
  `customer-support`, `finance` plugins were not seam-checked.
- **`guia-matthieu/clawfu-skills` is unread** — ships SPIN/Challenger/Sandler/MEDDIC/Voss as named skills
  and is unlicensed. **Highest-priority remaining IP check** (§4.4).
- **`TheCraigHewitt/sales-skills` is unread in content** — the pack most name-identical to ours,
  including both flagship items. Its MIT license is A1-reported, **not A3-verified**.
- **`gtmagents/gtm-agents/sales-handoff-orchestration` unread** — bears on gap #3.
- A3's ledger was fixed before A1's census landed, so **`gtmagents`, `clawfu-skills`, `LeadMagic`,
  `doris-labs`, `jmbluhm`, `TheCraigHewitt`, `louisblythe` are licensing-UNVERIFIED** (louisblythe's
  null-license is A1's API read, not a file-level check).
- **Item-8 deep-reads not reached:** `getcargohq/cargo-skills`, `phuryn/pm-skills`,
  `claude-office-skills/crm-automation` (4,421 installs; **A1 could not confirm its upstream org
  resolves**), `code.deepline.com/deepline-gtm` (17,227 installs — largest unexamined, but A3 established
  it is NOT CITABLE, capping its value). **Lead ruling: no top-up worker** — the wedge is over-evidenced,
  these are mid-tier, and the two likeliest to matter are uncitable or vendor-thin. Recorded as a known
  gap, not closed.
- The 21 Python scripts in `alirezarezvani/commercial/` were **never executed or read**; behaviour claims
  come from SKILL.md prose and are marked UNVERIFIED in the lead raw.
- **No incumbent figure was compared against a primary source here.** Every "UNSOURCED" grade means *"no
  link in the containing file"*, **not** *"the claim is false."* That is Channel B/C/D work.

**Method findings for family memory:**
1. **skills.sh search is not a census — TWO independent instances this run.** (a) It never returned
   `alirezarezvani/claude-skills`' entire `commercial/` plugin for `sales`, `gtm`, `crm`, or
   `forecasting` — a 23.6k★ repo, invisible; found only via `gh search repos`. (b) A1's **72 queries,
   including `gtm`, `prospecting` and `lead-generation`, never surfaced `LeadMagic/gtm-skills`** — the
   largest GTM repo found in the entire sweep (~130 skills, 24 categories); it appeared only under
   `gh api search/code q="MEDDICC filename:SKILL.md"`. Two misses, both of them large repos, both found
   only by GitHub-side search. **Any census built on skills.sh alone systematically understates big
   repos.** Always cross-check with `gh search repos` / `gh api search/code`.
2. **The registry serves rot.** `sales-skills/sales` (323 installs) is indexed and rendered with a live
   install count while the repo 404s (A1 confirms the *org* resolves but the repo does not — anomalous).
   Clone and check HEAD before citing.
3. **Aggregators inflate the ecosystem.** `sickn33` (44.3k★) and `awesome-copilot` (37k★) re-host other
   people's skills; star counts and skill counts measure distribution, not authorship.
4. **Three distinct failure modes in this run all present as "empty":** skills.sh rate limits, WebSearch
   quota death, and — the lead's own — zsh not word-splitting an unquoted `$VAR` (plus `grep -o` with
   `-l` being a silent no-op). **A zero from a shell loop deserves the same suspicion as an empty API
   response.**
5. **A deep-read of N repos is not a uniqueness proof** (§6). Breadth sweeps and depth reads answer
   different questions; asserting absence needs the former.

---

# ADDENDUM — 2026-08-03, after Channel C's independent rediscovery

Added after the report above was written, in response to the controller's urgent census amendment.
**Nothing above is rewritten**; this addendum records what changed and what did not.

## A1. Provenance: this repo was already in scope, and C's find converges with mine

`alirezarezvani/claude-skills` was **not** missed by Channel A. The lead found it *before* the report was
written (via `gh search repos`, after skills.sh failed to return it), deep-read it, and wrote it up in
[`raw/_raw-a0-lead-breadth-repo.md`](raw/_raw-a0-lead-breadth-repo.md). It is already load-bearing in the
report above: §2 (breadth ranking), **§3.2 (the flagship exhibit)**, §4.2 (the proposed 8th licensing
clause), §4.3 (ledger row), §5 (three never-ship figures), §6 gap 5.

Channel C's lead reached it independently by a different route. **Two channels, two methods, same
conclusion** — including the same read that its sales-adjacent coverage is RevOps/commercial-finance with
the buying conversation absent. That convergence is worth more than either finding alone, and it is the
second independent confirmation that **skills.sh search hid a 23.6k★ repo** (§7 method finding 1).

## A2. Wedge line — adopting C's sharper formulation

C's framing is better than mine and I am taking it. The report's §1 verdict is unchanged; this is the
one-line statement of it:

> **The largest incumbent occupies commercial-finance sales. The buying conversation and the deal system
> are empty at every scale. And the accuracy-measurement null survives even the best incumbent.**

The third clause is the important one and it is what §3.2 proves: `commercial-forecaster` is the best
forecasting artifact in the ecosystem, it explicitly holds the assumption-disclosure posture we thought
was ours (*"If you remove it, the forecast becomes theatre"*), it ships a runnable
`bookings_forecaster.py` with commit/best-case/pipe-only and coverage ratio — **and its own priors are
unsourced.** The null we are naming is not "nobody built forecasting"; it is "nobody can show that any of
it predicts anything," and that null survives the strongest counterexample the field has.

**Depth check the controller asked for (how deep did A1 actually get?):** A1 scored it from my raw and
explicitly did not re-derive (its census row cites `_raw-a0` and says "do not re-derive"). The depth is
the **lead's**, not A1's: SKILL.md read in full, `saas_forecasting_canon.md` and `shipley_method_canon.md`
read, whole-corpus citation grep (74 files / 11,105 lines), 14-item coverage grep, and the licensing pass.
**Still unread, and still declared:** all 21 Python scripts (never executed — behaviour claims come from
SKILL.md prose), `deal-desk`, `commercial-policy`, `channel-economics`, `partnerships-architect`, and most
of `revenue-operations`.

## A3. LICENSE re-verified at a PINNED SHA — upgrade from the report's HEAD-only check

The report's §4.2 verified at HEAD without pinning. Redone properly.

**Pinned commit: `aa8d778811a557a2c28ccadda4cf3d0bd028a4cc`** (2026-07-17T13:02:50Z, "Merge pull request
#922 from alirezarezvani/dev"). Every claim below is at that SHA.

**Root LICENSE, read in full at the pinned SHA** (`raw.githubusercontent.com/alirezarezvani/claude-skills/aa8d778.../LICENSE`):
verbatim MIT, unmodified body, `Copyright (c) 2025 Alireza Rezvani`. No added clauses, no carve-outs, no
field-of-use restriction — checked against the standard MIT text line by line. **Not a composite license**
(contrast `twentyhq/twenty`, §4.3).

**Every license file at the pinned SHA, enumerated by the git tree API** — a *second, independent* method
from the report's local-clone `find`, and the two agree exactly (6 blobs):

| Path | Copyright | Governs |
|---|---|---|
| `LICENSE` | MIT © 2025 Alireza Rezvani | root — **covers `commercial/` and `business-growth/`** |
| `loop-library/LICENSE` | MIT © 2026 Forward Future | `loop-library/` |
| `engineering/skillopt-sleep/LICENSE` | MIT © 2026 Microsoft Corporation | that skill |
| `engineering/collab-proof/LICENSE` | MIT © 2026 dong7812 | that skill |
| `engineering-team/self-improving-agent/LICENSE` | MIT © 2026 Reza Rezvani | that skill |
| `engineering-team/playwright-pro/LICENSE` | MIT © 2026 Reza Rezvani | that skill |

Three filename false-positives excluded (subject-matter files *about* licensing, not licenses):
`engineering/skills/dependency-auditor/references/license_compatibility_matrix.md`,
`.../scripts/license_checker.py`, and — new at this SHA —
`.../expected_outputs/sample_license_report.txt`.

**The controller's real question — "root-MIT doesn't prove the aggregator could relicense republished
work."** Correct in general, and the report's §4.2 raised exactly this. Tested directly:

- **No third-party source markers exist in our citation path.** All 8 `commercial/skills/*/SKILL.md`
  carry `author: claude-code-skills` (the project's own identity); `business-growth`'s carry
  `author: Alireza Rezvani`. **Zero `source:`, `origin:`, `credit:`, or `attribution:` keys anywhere in
  `commercial/` or `business-growth/`.** The single `metadata:` block in those trees
  (`business-growth/skills/customer-success-manager`) reads `author: Alireza Rezvani`.
- Contrast the known-republished case: `github/awesome-copilot`'s gtm-* family *does* carry
  `metadata.source: https://github.com/beingsmit/technical-product-gtm` (§4.4). **The marker exists in
  this ecosystem and is used when content is republished — and it is absent here.**
- Every directory in this repo with a *different* copyright holder carries **its own LICENSE file**, and
  all four such directories are under `engineering*/` or `loop-library/` — **none in our citation path**.

**Verdict: MIT, CITABLE WITH ATTRIBUTION for `commercial/` and `business-growth/`, verified to all 7
clauses at a pinned SHA by two independent enumeration methods.** C's PROVISIONAL grade can be lifted for
those two trees.

**Stated limit, because it cannot be closed by inspection:** absence of a source marker is *strong
evidence*, not proof, that no content in `commercial/` is republished from a third party. Nothing short of
provenance research on each of ~28 reference docs could establish that, and it is not worth the budget —
**we are citing this repo as an object of study (an incumbent whose evidence layer is empty), not lifting
its text.** That use is safe under any of the readings above. If a later phase wants to *adapt* any of its
scripts or reference content, this question must be reopened first.

## A4. What did NOT change

- The §1 verdict (open by fragmentation + adoption collapse, contested on specific items) stands. C's
  repo does not alter it: at ~5–6/14 it was never the breadth leader — `gtmagents/gtm-agents` (~12–13/14),
  `louisblythe` (~10–11/14), `TheCraigHewitt` (~9–10/14) and `guia-matthieu/clawfu-skills` (~10/14) all
  cover more of our scope. Its significance is **framing threat on the flagship**, not breadth.
- The never-ship figures table (§5), the MEDDICC IP exhibit (§4.4), and the coverage statement (§7) are
  unaffected.
- **Unchanged open item for B/C:** does KeyBanc/KBCM publish per-stage conversion rates at all? If not,
  `saas_forecasting_canon.md`'s attribution is not merely unlinked but **false** (§3.3).

**One flag outside my channel:** this repo's `business-growth/skills/customer-success-manager` ships
weighted health scoring, churn-risk tiering and expansion scoring with three Python tools — i.e. a direct
competitor to the **already-shipped success pack's** flagship. Informational only; success is released.
Recording it so it is not lost.
