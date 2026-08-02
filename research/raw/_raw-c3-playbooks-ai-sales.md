# C3 — GitHub/OSS: open sales playbooks/handbooks/lists + AI-sales/outreach wave

Worker: sales-lead-c / C3. Channel: GitHub/OSS corpus.
Surfaces used: `ghrelay` (search/batch/hydrate/enrich/rank/skim/read), `gh` CLI (`gh api`, `gh search repos`).
**WebSearch was NOT used at any point in this run** (avoided per the mid-run quota-exhaustion
notice from sales-lead-c) — every finding below is backed by `ghrelay`/`gh api` live GitHub
data, so the null results are trustworthy repo-search nulls, not silent-quota nulls.

Corpus files (for reproducibility, not part of the deliverable):
`research/raw/corpus-c3.json` (2,060 unique repos from 25 batched GitHub-search shards),
`research/raw/corpus-c3-aisales.json`, `research/raw/corpus-c3-aisales2.json` (hydrated/enriched
finalists).

---

## Part 1 — Playbooks / handbooks / awesome lists

### Table

| Repo | Stars | What it is | Content grade (1-5) | Verdict | License (verified upstream) |
|---|---|---|---|---|---|
| PostHog/posthog.com | 1,108 | Company website+docs+**handbook** monorepo; `contents/handbook/growth/sales/` has ~55 real files (discovery, qualification, outbound, pipeline, expansion, onboarding, forecasting-adjacent) | **4/5** | Genuinely the strongest open sales-process content found in this whole search — a real company's day-to-day playbook, not marketing copy | **Split license**: root MIT-style-permissive for site code; **`/contents/` folder (includes the handbook) is MIT** — see quote below |
| Sourcegraph/handbook | 185 | Archived (2024) company handbook monorepo; `content/departments/sales/` has ~50 files (forecasting, career frameworks, onboarding, sales-ops, sales-enablement) | **3/5** | Real, concrete forecast-category definitions (Commit/Best-Case/Pipeline/Omitted) worth citing; rest is heavily dashboard-link-dependent (dead without internal Looker/Salesforce access) and the repo is **archived, frozen since 2024-07-02, migrated to Notion** — treat as a historical snapshot, not living doctrine | Apache-2.0 (root `LICENSE`, verified) |
| basecamp/handbook | 6,611 | 37signals **employee** handbook (benefits, HR policy, "how we work") | **N/A — out of scope** | Not a sales handbook at all — no sales/GTM content in its 16 files; charter flagged it as a candidate, verified and ruled out | **No LICENSE file anywhere in the repo** — unlicensed content, would be a reproduction trap if anyone cited it |
| vladar107/awesome-sales-engineer | 17 | Awesome-list: sales-engineering/pre-sales bibliography (books, podcasts, cheat sheets, methodology links) across Discovery/Demo/Objection-Handling/POC/Storytelling | **3/5** | Real curated bibliography of known, real, non-fabricated books (*Great Demo!*, *SPIN Selling*, *The Challenger Sale*, *Mastering Technical Sales*) and one real community (PreSales Collective); thin under several headings (Objection Handling and POC sections are one line each) — a decent reading-list pointer, not primary content | **CC0 1.0** (root `LICENSE`, verified) |
| Salesably/awesome-ai-agents-for-sales | 31 | Vendor-maintained (Salesably.ai) curated directory of AI-sales tools/agents by category | **2/5** | Well-organized taxonomy (Autonomous AI SDRs / Prospecting / Outreach / Coaching / Revenue Intelligence / etc.) but it is a company's own marketing directory, not independent curation, and several linked "open source projects" turn out to be the same low-star repos found independently in this search | **No LICENSE file** — unlicensed, do not reproduce the list verbatim |
| LLMbreaker/awesome-ai-sales-tools | 14 | "Curated list of AI tools for sales automation" | **1/5** | Affiliate-link farm — entries carry `?utm_source=github&utm_medium=git-repo&utm_campaign=awesome-ai-sales-tools` tracking params, one-line descriptions, mixes real tools (Gong, Outreach) with unverifiable ones | Not checked further — grade alone disqualifies it from citation |
| mailtoharshit/awesome-salesforce (+ ~15 sibling `awesome-salesforce-*` repos) | 800 (top one) | Salesforce-platform-specific resource lists (admin/dev/architecture) | **N/A — out of scope** | Real curated lists but scoped to one CRM vendor's ecosystem, not general sales process/methodology; noted, not pursued further | Not checked (out of scope) |
| "sales playbook" / "sales handbook" / "founder-led sales" / "sales enablement" / "win-loss analysis" / "objection handling" / "discovery questions" / "cold email templates" named-match repos (see Null Results) | 0-2 (all of them) | Hundreds of repos literally named `sales-playbook`, `Sales-Handbook`, `sdr-playbook`, etc. | **1/5 or unratable (empty)** | Overwhelmingly either (a) empty scaffolds, (b) personal Claude-Code/Codex "agent skill" packages that use "playbook" as a metaphor for a prompt library, or (c) outright SEO/spam farms (see `annatran05022000-cpu/*`, `laravelmail/*` — dozens of near-identical "cold email template" repos from what looks like one content-mill account) | Mostly unlicensed; not evaluated individually — none survive the content-grade bar |

### Deep notes — the two worth citing

**PostHog/posthog.com** — resolved commit for permalinks: `259e5a6921ce301f4b8efa957d33050ea34e6d36`.

License split, quoted verbatim from the repo's `LICENSE` file (root):
> "# For all content except the /contents/ folder ... Please do not duplicate, copy, or use our website for commercial or non-commercial use. ... # For content in the /contents/ folder ... Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software..."
Permalink: https://github.com/PostHog/posthog.com/blob/259e5a6921ce301f4b8efa957d33050ea34e6d36/LICENSE

The handbook lives entirely under `contents/handbook/...`, so it is covered by the MIT half. This
is a real, in-force, actively-maintained (pushed same-day) company sales handbook — the strongest
single find of this search. Notable files (all under
`contents/handbook/growth/sales/` unless noted):

- `overview.md` — team structure and stated sales philosophy (inbound-first, no-BS, "we don't do
  margin negative deals ... to win"). Quote:
  > "Our primary focus is on making our paying customers successful, not forcing sales through. This mostly means an inbound sales model, but we are also running some outbound sales experiments." / "We don't do margin negative deals in order to win - this doesn't set us up for a successful long term relationship with a paying customer if we're ultimately losing money to land them."
  Permalink: https://github.com/PostHog/posthog.com/blob/259e5a6921ce301f4b8efa957d33050ea34e6d36/contents/handbook/growth/sales/overview.md
- `how-to-do-discovery.md` — a discovery-call framework built around curiosity-over-pitching,
  finding pain, and identifying champions, explicitly framed as guidance not a script. Quote:
  > "Discovery isn't walking through every PostHog feature. It's having real conversations with customers to figure out if PostHog will be a good fit for them. ... This is meant to be a guide, not a rule-set."
  Permalink: https://github.com/PostHog/posthog.com/blob/259e5a6921ce301f4b8efa957d33050ea34e6d36/contents/handbook/growth/sales/how-to-do-discovery.md
- `contents/handbook/onboarding/sales-handover.md` — a genuine, criteria-based **internal
  handoff document** (product-led-onboarding → sales), with a concrete usage/spend threshold
  ($1,000/mo) and explicit "don't wait for the customer to respond" guidance, automated via a
  Vitally→Salesforce lead-creation pipeline. This is the closest primary-source analogue found in
  this channel to the "marketing→sales handoff, what counts as qualified" question the charter
  flags as contested — note this is a **PLG-signal handoff** (usage-based), not a
  marketing-MQL handoff, so it corroborates the shape of a handoff criterion without settling the
  contested marketing-pack vocabulary.
  Permalink: https://github.com/PostHog/posthog.com/blob/259e5a6921ce301f4b8efa957d33050ea34e6d36/contents/handbook/onboarding/sales-handover.md
- Other real, substantive files present but not fully quoted here (worth a second pass by the
  channel lead if forecasting/qualification/expansion citations are needed):
  `lead-scoring.md`, `evaluating-growth-potential.md`, `expansion-and-retention.md`,
  `new-business-how-we-work.md`, `outbound-sales.md`, `product-led-lead-qualification.md`,
  `who-we-do-business-with.md` (ICP), `why-buy-posthog.md`. Also
  `contents/handbook/engineering/revenue-and-forecasting.md` — a **usage-based** revenue-forecast
  methodology (not a sales-pipeline forecast; it forecasts *billing*, not *deal probability*) —
  relevant contrast, not a substitute, for pipeline-forecast citations. Permalink:
  https://github.com/PostHog/posthog.com/blob/259e5a6921ce301f4b8efa957d33050ea34e6d36/contents/handbook/engineering/revenue-and-forecasting.md

**Sourcegraph/handbook** — resolved commit: `5752928b213a3ddbc7cee4459524f404a5b96fb4`. Repo is
`archived: true`, `pushed_at: 2024-07-02` (per `gh api repos/sourcegraph/handbook`) — i.e. frozen
just over two years before this research date. The README carries a live migration warning:
> "The handbook is hosted on Notion, and https://handbook.sourcegraph.com will redirect to the corresponding Notion.site. ... You need to scrub content from the handbook (incorrect content has been added before the repo was archived)."
This means the GitHub snapshot may itself contain content Sourcegraph considered wrong/outdated at
archival time — cite with that caveat attached, not as current company practice.

License: Apache-2.0, root `LICENSE` file verified directly (standard Apache 2.0 boilerplate text
confirmed, not just the badge).
Permalink: https://github.com/sourcegraph/handbook/blob/5752928b213a3ddbc7cee4459524f404a5b96fb4/LICENSE

The one genuinely citable, self-contained file — `content/departments/sales/process/forecasting.md`
— gives a concrete stage-weighted-forecast-category taxonomy (Commit / Best Case / Pipeline /
Omitted) with operational definitions, useful as a **named, real-world example of a forecast
methodology** (not validated/backtested anywhere in the doc — it's a process description, not an
accuracy claim):
> "**Commit** - Opportunities where you have 1) the technical win, 2) received confirmation from the EB that they intend to purchase at or around the Amount/iARR and by the Close date you are forecasting, and 3) you have full understanding of the Paper Process and are aligned with the customer on a clear path to closure" / "**Best Case** - Opportunities that have a 50% and above probability to close in a period."
Permalink: https://github.com/sourcegraph/handbook/blob/5752928b213a3ddbc7cee4459524f404a5b96fb4/content/departments/sales/process/forecasting.md

Caution: most of the *other* sales files in this repo (`sales-ops/prospecting.md`,
`demand-gen/*`) are near-empty wrappers around dead internal Looker-dashboard links behind
`sourcegraph.looker.com` auth — not independently useful, do not cite as content.

**vladar107/awesome-sales-engineer** — resolved commit: `fdb7823eae1084f60e10bd8d83795677e29afec1`.
CC0 1.0 Universal, verified from the actual `LICENSE` file text (not just the shields.io badge,
which is dynamic and would have lied if the repo had none). Full section list and representative
entries (real, checkable references — *Great Demo!* by Peter Cohan, *SPIN Selling* by Neil
Rackham, *The Challenger Sale* by Matthew Dixon, PreSales Collective Slack community) — quoted in
full above under Deep Notes source dump; permalink:
https://github.com/vladar107/awesome-sales-engineer/blob/fdb7823eae1084f60e10bd8d83795677e29afec1/README.md

---

## Part 2 — AI-sales / AI-SDR / outreach-automation wave (2024-26)

### Table

| Repo | Stars | What it does | Maturity signal | Honesty-line read | License (verified) |
|---|---|---|---|---|---|
| eracle/OpenOutreach | 2,590 | **Autonomous prospecting + email-first outreach**: LLM turns a product/ICP description into a firmographic filter, a Gaussian-Process scoring model rations paid contact-lookups to the best-fit leads, an agent sends + follows up from the founder's own mailbox | Actively maintained — pushed **same day** as this research (2026-08-02), `A` (maintenance) subscore 0.96/1, high velocity (198) | **Explicitly consent/ToS-conscious by design**: sources leads from a "licensed discovery source" (BetterContact), zero LinkedIn scraping, "browserless... nothing to get banned." Also unusually honest about its own novelty: *"The learning loop is an active experiment — it is not yet shown to beat picking at random, and no claim is made that it does."* This is the most self-aware repo found in this whole search | **GPL-3.0** — file is `LICENCE.md` (British spelling), NOT `LICENSE`; GitHub's license API reports `"Other"/NOASSERTION` for this repo — **API-lies trap confirmed live**, verified by reading the actual file text |
| growchief/growchief | 3,401 | Social-media outreach automation (LinkedIn/X connection requests, follow-ups, engagement) via API, explicitly pitched as an open-source alternative to PhantomBuster/Expandi/Zopto/LinkedIn Helper/Meet Alfred | `A` subscore very low (0.05) despite high star count — a star-count/activity mismatch worth flagging even though `rank` didn't trip its star-burst flag here | The **opposite honesty posture** from OpenOutreach: it explicitly automates the exact LinkedIn-ToS-violating actions (connection spam, engagement automation) that OpenOutreach's README calls out as "getting banned." Good contrast pair for the wave synthesis | AGPL-3.0 (root `LICENSE`, verified) |
| filip-michalsky/SalesGPT | 2,713 | Early (2023) "context-aware AI Sales Agent" — conversational sales-outreach agent across voice/email/SMS, LangChain-era, published to PyPI | **Stale**: last push 2024-09-17, ~23 months before this research date despite the star count and name recognition — a clean example of the "well-known name, dead repo" pattern | Positions itself as a general-purpose conversational sales agent; no explicit deliverability/consent discussion found in the README head read | MIT (root `LICENSE`, verified) |
| iPythoning/b2b-sdr-agent-template | 150 | Template for an AI SDR working over **WhatsApp/Email/Telegram** for B2B export businesses ("PulseAgent"), built on "OpenClaw" agent runtime, claims a "MemOS + sales_playbook + conversation_history" three-layer architecture | Actively maintained (pushed 2026-07-13, velocity 382) but **self-promotional**: Product-Hunt-launched, "Buy Me a Coffee" button, changelog entries read like marketing copy for a paid companion product | Marketing-forward register ("Turn any B2B export business into an AI-powered sales machine in 5 minutes") — no deliverability/consent discussion visible in the README head; worth noting as the shape of the wave's promotional register, not as evidence of maturity | MIT badge shown; `hasLicenseFile: true` per skim — not independently re-verified beyond the badge given lower priority (star count 150, marketing-heavy) — **grade this citation CONFOUNDED, not verified**, if reused |
| zubair-trabzada/ai-sales-team-claude | 890 | Claude-Code skill pack: "Research prospects, qualify leads (BANT + MEDDIC), map buying committee, generate personalized outreach... produce PDF pipeline reports" — a prompt-orchestration wrapper, not a standalone service | Low `A` (0.09); represents the "AI-agent-skill" sub-genre rather than a running SaaS-style tool | Cites two trademarked commercial methodologies (BANT, MEDDIC) by name inside a tool's marketing copy — exactly the citation trap the charter warns about (cite-the-evidence-about, never reproduce-the-method) | MIT (root `LICENSE`, verified) |
| linvo-io/linvo-scraper | 628 | LinkedIn automation library (Puppeteer): login, scrape Sales-Nav/normal profiles, send connection requests, follow messages, endorse, visit, like posts, "random engagement" — includes anti-detection (`ghost-cursor`) tooling | **Stale**: description itself says "Valid for 2022"; last push 2024-12-11 | The clearest example in this corpus of the pre-2024 LinkedIn-automation genre this wave is partly a reaction against — pure scraping + evasion, no consent framing at all | MIT (root `LICENSE`, verified) |
| Salesably/awesome-ai-agents-for-sales | 31 | (see Part 1 table — vendor-maintained AI-sales-tool directory, doubles as a map of the wave's category taxonomy) | — | Its own category list (Autonomous AI SDRs / Prospecting & Lead Gen / Outreach & Engagement / Email Personalization & Copywriting / Conversation Intelligence / Revenue Intelligence & Forecasting / CRM & Data Enrichment) is itself a useful, non-reproducible map of how the industry currently segments "AI sales" — cite the shape, not the list | No LICENSE — do not reproduce the list |

### What the wave assumes — short synthesis

Across the maintained (non-stale) repos in this sample, three assumptions recur:

1. **Personalization-at-scale is treated as a solved input, not a claim to defend.** Every tool
   in this list (OpenOutreach, iPythoning's template, the Claude-Code skill wrappers) assumes an
   LLM can turn a company URL + ICP description into a "personalized" opener without asking what
   makes a message actually personalized to the recipient vs. templated-with-variables. None of
   the READMEs read here make (or disclaim) a rate/quality claim for their own personalization —
   OpenOutreach's disclaimer about its scoring model *not yet beating random* is the one exception
   in the whole sample, and it applies to lead selection, not message quality.
2. **Deliverability and platform-ToS risk sit on a spectrum the repos silently choose a side of,
   rather than argue for.** growchief and linvo-scraper build directly on top of LinkedIn
   automation/scraping (the "getting banned" risk is real and unaddressed in-repo); OpenOutreach
   is the one repo in this sample built explicitly to avoid that risk by using licensed data +
   owned-mailbox email instead of scraping. Nobody here engages with email deliverability/warm-up
   mechanics or consent-regime (CAN-SPAM/GDPR/CASL) questions in what was read — that stays
   marketing's shipped doctrine per the charter, and this pack should cite it rather than
   re-derive it.
3. **"Autonomous SDR" is used loosely** — it covers everything from a single-agent lead-scoring
   pipeline (OpenOutreach) to a multi-agent Claude-Code prompt pack that still requires a human to
   run commands (zubair-trabzada) to a WhatsApp/Telegram bot template aimed at a narrow vertical
   (iPythoning). The label does not reliably signal what governance/oversight the tool assumes —
   this is exactly where sales's AI-outbound POLICY wedge (per the charter: ai owns mechanics,
   sales owns policy) has room, because none of these repos state what human-in-the-loop check, if
   any, sits before a message actually sends.

Star-skepticism note: none of the seven Part-2 repos above tripped `ghrelay rank`'s `star-burst`
or `possible-fake-stars` flags in this sample, but `A` (maintenance) subscores diverge sharply
from star counts in several cases (growchief: 3,401★ but A=0.05; brightdata/ai-sdr-bdr-agent:
11★, A=0.01, `lic: none` despite being a real company org — checked, no LICENSE file found in
that repo either) — **stars did not track usage or maintenance health in this sample**, consistent
with the family's standing star-skepticism rule.

---

## Licensing ledger

Every repo cited or graded above where a license claim is made, with every license file actually
read (not just the GitHub API field):

| Repo | Upstream URL | License file(s) read | Verdict |
|---|---|---|---|
| PostHog/posthog.com | https://github.com/PostHog/posthog.com | `LICENSE` (root, split-clause: proprietary for site, **MIT for `/contents/`**) | Handbook content (under `/contents/handbook/`) is MIT — reproducible with attribution |
| sourcegraph/handbook | https://github.com/sourcegraph/handbook | `LICENSE` (root, Apache-2.0, full text confirmed) | Apache-2.0 — reproducible with attribution/notice; repo is archived/stale, cite as historical snapshot |
| basecamp/handbook | https://github.com/basecamp/handbook | none found (`LICENSE`, `LICENSE.md` both absent from a 16-file repo) | **Unlicensed — trap.** Also out of scope (no sales content). Do not cite or quote. |
| vladar107/awesome-sales-engineer | https://github.com/vladar107/awesome-sales-engineer | `LICENSE` (root, CC0 1.0 Universal, full text confirmed) | Public domain — freely reproducible |
| Salesably/awesome-ai-agents-for-sales | https://github.com/Salesably/awesome-ai-agents-for-sales | none found (`LICENSE`, `LICENSE.md` both absent) | **Unlicensed — trap.** Describe the taxonomy shape only; do not reproduce the list |
| eracle/OpenOutreach | https://github.com/eracle/OpenOutreach | `LICENCE.md` (note British spelling — NOT `LICENSE`; GPL-3.0, full text confirmed) | GitHub API reports this repo's license as `"Other"/NOASSERTION` — **confirmed API-lies case**; actual license is GPL-3.0 |
| growchief/growchief | https://github.com/growchief/growchief | `LICENSE` (root, AGPL-3.0, full text confirmed) | AGPL-3.0 confirmed |
| filip-michalsky/SalesGPT | https://github.com/filip-michalsky/SalesGPT | `LICENSE` (root, MIT, full text confirmed) | MIT confirmed |
| zubair-trabzada/ai-sales-team-claude | https://github.com/zubair-trabzada/ai-sales-team-claude | `LICENSE` (root, MIT, full text confirmed) | MIT confirmed |
| linvo-io/linvo-scraper | https://github.com/linvo-io/linvo-scraper | `LICENSE` (root, MIT, full text confirmed) | MIT confirmed |
| relaticle/relaticle | https://github.com/relaticle/relaticle | `LICENSE` (root, AGPL-3.0, full text confirmed) | AGPL-3.0 confirmed. (Out of primary scope — this is an open CRM with AI-agent features, not an outreach/SDR tool; noted for the OSS-CRM item in case another worker hasn't covered it.) |
| iPythoning/b2b-sdr-agent-template | https://github.com/iPythoning/b2b-sdr-agent-template | **not independently re-verified** — `skim` reported `hasLicenseFile: true` and the README shows an MIT badge, but I did not read the LICENSE file's actual text | **CONFOUNDED** — do not cite as MIT without a follow-up read of the actual `LICENSE` file text |
| brightdata/ai-sdr-bdr-agent | https://github.com/brightdata/ai-sdr-bdr-agent | not read (repo graded low-priority/low-maturity, not cited) | `rank` reports `lic: none`; not independently verified — do not cite |
| personizeai/revenue-os, codyschneiderx/waterfall-gtm | (not cited in prose above) | not read | Hydrated/ranked only, both low-signal (A ≤0.16), not pursued further |

---

## Null results (precise)

All of the below ran as `ghrelay batch` GitHub-search shards (25 total, see
`research/raw/corpus-c3.json`, `queries` field) against live GitHub Search, `in:readme` /
`in:name` qualified, no WebSearch involved:

- `"sales playbook" in:readme` → 100 results (capped). After sorting the full merged corpus by
  stars and filtering for name/description matches on `playbook`/`handbook`, **every single
  repo matching `sales-playbook`/`Sales-Playbook`/`sales-handbook` in its name has 0-2 stars** and
  is either an empty scaffold, a personal Claude-Code/Codex "agent skill" package, or (in the case
  of the ~10 `annatran05022000-cpu/*` and ~8 `laravelmail/*` repos) what looks like an SEO
  content-mill account publishing near-identical "cold email template" repos for search-engine
  placement rather than for use. **No general-purpose, non-vendor, non-AI-agent-marketing sales
  playbook of any real content depth exists in GitHub search results as of this research date**,
  beyond the two company handbooks documented in Part 1.
- `"founder-led sales" in:readme` and `"founder sales" in:readme` → 100 results each (capped).
  Filtering the merged corpus for `founder-led`/`founder sales` in name or description surfaced
  exactly **4 repos**, all 0-1 stars, all personal tool/prompt-pack projects (e.g.
  `Spexx-commits/revenue-motion-development`, `Autter-dev/agentic-sales-skills`) — **no
  founder-led-sales canon content exists on GitHub**; that literature lives in blog/essay form
  (SaaStr, YC, practitioner threads), consistent with the charter's framing of this as an
  existence-gate question rather than a GitHub-native one. (This null was reached via `ghrelay`
  GitHub-search only — flagging per the mid-run correction, since it's a headline-adjacent
  finding.)
- `"sales enablement" in:readme` → 100 results (capped). Top-40 by stars is dominated by
  Claude-Code/Codex "agent skill" packages (`pmm-skillset`, `genesys-skills`,
  `sales-enablement-plugin`, `enablement-skills`, `taizen-claude-plugins`, `gtm-claude-skills`)
  and vendor-internal IBM training-stub repos (`IBM/SalesEnablement-*`, themselves marked "for
  fun, ain't it grand!" in one description) — **no independent sales-enablement content repo of
  substance found**.
- `"win-loss analysis" in:readme` → 100 results (capped). Every match found was either (a) a
  literal win/loss **sports or poker analytics** project (baseball, cricket — the phrase
  "win-loss" collides hard with sports-analytics naming) or (b) a 0-star personal deal-intelligence
  tool stub. **No open win/loss-analysis methodology content found.**
  KBCM AE-quota-attainment figure (success pack's corpus) is the closer primary source for this
  strip; nothing here adds to it.
- `"discovery questions" sales in:readme`, `"objection handling" sales in:readme`,
  `"sales onboarding" in:readme` → 100 results each (capped); all top matches were 0-1★
  Claude-Code skill packages or single-purpose scaffolds — same pattern as above, not
  independently listed to avoid repetition.
- `awesome-sales in:name` → 100 results (capped). The overwhelming majority (~70 of the top 100
  by any relevance ordering) are **Power BI "Awesome Chocolates" sales-dashboard tutorial
  projects** — a training-dataset name collision with zero relevance to this pack. Filtered that
  noise out; the handful of real candidates are in the Part 1 table (`awesome-salesforce` family,
  `awesome-sales-engineer`, `awesome-ai-agents-for-sales`).
- Company handbooks checked and ruled out: `zapier/handbook` — **repo does not exist** (`gh api`
  404; `gh search repos "zapier handbook"` returned 0 results). `bufferapp/buffer-culture` —
  **repo does not exist** (404); searched `org:bufferapp` directly (`gh search repos
  org:bufferapp`, 30 results) and found no culture/handbook/sales repo, only Buffer's open-source
  Android/iOS SDKs and internal tooling. Neither company publishes a sales/GTM handbook on GitHub.

---

## Coverage statement

Searched: 25 batched GitHub-search shards covering playbook/handbook/founder-led-sales/awesome-list
naming (Part 1) and AI-SDR/outreach-automation naming (Part 2), all via `ghrelay batch` against
live GitHub code+repo search (`in:readme`/`in:name` qualified), yielding 2,060 deduplicated
candidate repos, plus 4 direct `gh api`/`gh search repos` lookups for named company handbooks
(PostHog, Basecamp, Zapier, Buffer, Sourcegraph). 13 repos were individually hydrated, enriched,
ranked, skimmed, and license-verified.

**Not searched / not covered:**
- GitLab's handbook — explicitly out of scope per the assignment (another worker owns it).
- Open CRMs (Twenty, EspoCRM, etc.) as a category — out of scope per this worker's assignment
  (item 7 in the charter, likely a sibling C-worker's territory); `relaticle/relaticle` surfaced
  incidentally in the AI-sales search and is noted/licensed above in case it's useful there.
- Non-English-language playbooks/handbooks were not specifically searched for.
- grep.app / `ghrelay code` (code-token evidence lane) was not used — this assignment is about
  prose content (playbooks/handbooks) and product shape (AI-sales repos), not code patterns, so a
  code-token probe wasn't a fit for the intent.
- Blog-form founder-led-sales canon (SaaStr, Lemkin, YC essays, patio11) — explicitly out of
  scope for this GitHub-only channel; the null result above is *for GitHub specifically* and does
  not speak to whether that literature exists elsewhere (it does, and is presumably another
  channel's territory per the charter's item 4).
- Deeper reads of `iPythoning/b2b-sdr-agent-template`'s actual LICENSE file text, and of
  `personizeai/revenue-os` / `codyschneiderx/waterfall-gtm` / `brightdata/ai-sdr-bdr-agent`
  beyond `rank` metadata — deprioritized as lower-signal than the seven repos fully written up
  above; flagged in the licensing ledger as unverified rather than silently dropped.
