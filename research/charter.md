# Sales skill — research charter

Date: 2026-08-03 · Controller: main session (digital-product-skill) · Crew: 5 opus leads + ~17 sonnet workers
This is the 14th and FINAL pack of the Digital Product Skills family. 13 shipped:
design, product, architecture, frontend, backend, ai, data, automation, quality, operate,
marketing, growth, success. Shipping sales completes the family and closes every open seam.

## Mission (canonical §4.12, docs/product-lifecycle-skill-packs-exploration.md in digital-product-skill)

"Convert qualified demand into committed customers through a repeatable buying process."
Tier: Distribute (pairs with marketing). Flow: marketing → sales → success.

**Includes (14):** ICP + account selection · qualification frameworks · sales stages + exit
criteria · discovery calls · demo strategy/narrative · objection handling · proposals +
commercial collateral · pricing/packaging PRESENTATION (design is product's) · CRM structure ·
pipeline management · forecasting · marketing→sales handoff · sales→success handoff · win/loss
learning.
**Produces:** playbook, qualification framework, discovery scripts, demo narrative, objection
library, proposal templates, CRM stages/fields, pipeline reports, handoff/ownership criteria.
**Code policy:** CRM config + small automations; substantial workflows → automation.

## The axis (controller's pre-research outline — test it, don't assume it)

Sales is the family's DEAL OWNER: wherever an assisted buying process exists, sales owns who is
worth pursuing (ICP/qualification), the buying conversation (discovery, demo, objections,
proposal, pricing presentation, negotiation), the deal system (CRM structure, pipeline,
forecast), and learning from outcomes (win/loss). Marketing persuades a market; sales converts a
named account. Growth experiments on the funnel; sales runs the deals in it. Success keeps the
customer; sales obtains the commitment — including closing the expansion sale.

## Seam contracts already shipped by siblings (BINDING — verify quotes, never contradict)

- **marketing (flat, firm):** handoff.md:42 — sales receives "qualified demand — a defined
  fit-plus-intent signal on a named account"; returns pipeline/close-rate signal. Revenue
  operations, sales enablement (battlecards, objection handling), cold outbound/prospecting are
  SALES's — "the incumbent genre routinely blends these into marketing; this pack does not."
  Also SKILL.md:107, lifecycle-and-email.md:16, surface-b2b-sales-assisted.md:51,111.
- **growth (provisional):** handoff.md:42 + SKILL.md:112 — "cold outbound, CRM stages, and deal
  mechanics stay sales's regardless of which funnel stage an experiment touches." Growth owns
  the experiments, even on sales-assisted stages.
- **success (provisional + CONTESTED):** handoff.md:40, SKILL.md:101,
  renewals-and-expansion.md:50 §6 — success runs the renewal workflow "up to a complex deal
  that needs negotiation"; sales closes the expansion sale in sales-assisted motions. Lincoln
  Murphy's CS-native complexity-gated position carried as contested vocabulary, NOT adjudicated.
  Sales must reciprocate without flattening the contested mark.
- **product:** SKILL.md:27 — cedes "qualification and CRM to sales." Product owns pricing/tier
  DESIGN and dunning/billing; sales presents and negotiates pricing.
- **automation:** SKILL.md:104, process-capture.md:15,163 — sales AUTHORS business rules and
  customer-facing comms; substantial workflow implementation is automation's.
- **ai / data / operate / design / quality / frontend / backend / architecture:** zero cessions
  found — sales draws those seams from its own side. ai = agent mechanics/evals, sales = AI-sales
  POLICY (mirror success's AI-support-policy precedent). data = metric validity, sales = what a
  forecast honestly means.
- Naming collision to respect: "sales enablement" (battlecards → sales) ≠ "customer enablement"
  (education → success). Cold-email deliverability: marketing owns the doctrine
  (deliverability + consent regimes are SHIPPED strips) — sales cites, never restates.

## What research must find (per channel; leads decompose further)

1. **Incumbent census** — who ships sales/GTM skill packs today, how good, what license, what
   wedge is left. Success's research already spotted GTM-adjacent packs at ~360★ — this niche
   may be MORE contested than CS was. Rank by BREADTH not installs.
2. **Evidence bases of the named methodologies** — SPIN (Rackham's 35k-call study: traceable?),
   Challenger (CEB data + published critiques), MEDDICC/MEDDPICC, Sandler, BANT, Gap Selling.
   ALL are trademarked commercial IP: cite-never-reproduce. What we want is published EVIDENCE
   ABOUT them, not their content.
3. **Falsification strips** — "57% of the buying decision happens before sales contact"
   (CEB origin, widely misquoted); "it takes 8 touches"; Gong's "we analyzed N million calls →
   X% more likely to close" genre (method disclosed?); win-rate and quota-attainment benchmarks
   (KBCM ~70→75% AE quota attainment is already primary-verified in success's corpus — reuse,
   do not re-derive); "always be closing" lineage. Trace every figure to its primary source or
   grade it folklore.
4. **Founder-led sales canon** — the family's default reader is a SOLO builder. When does a
   sales motion even exist (price point × complexity economics — patio11-style)? Founder-led
   sales practice (Lemkin/SaaStr, YC, practitioner threads). This is the existence-gate
   candidate, mirroring success's front door.
5. **Forecasting honesty** — flagship candidate. What can a pipeline number honestly predict?
   Stage-weighted forecasts (hand-set percentages, backtested anywhere?), forecast-accuracy
   claims, published forecast methods (GitLab handbook likely has real ones). Direct heir of
   the family's measurement-honesty line: attribution → feasibility → health scores → forecast.
6. **AI-SDR / AI-outbound wave (2024–26)** — fresh, under-canonized (like AI support was for
   success). Personalization-at-scale, deliverability collapse, agent-assisted selling, where
   the honesty line sits. ai pack owns mechanics; sales owns policy.
7. **OSS artifacts** — open CRMs (Twenty, EspoCRM, …) with UPSTREAM-verified licenses, open
   playbooks/handbooks (GitLab sales handbook), qualification/forecast calculators worth
   citing or adapting as assets.
8. **Webdesign lift** — anything in the old ~/.claude/skills/webdesign relevant to sales;
   anything relevant to OTHER packs flagged (not lost), since webdesign is being abandoned.

## Standing rules (from 13 builds — violations have shipped defects before)

- **Every claim needs a permalink or an explicit FOLKLORE/CONTESTED/CONFOUNDED grade.** A
  reconstructed permalink is a fabricated citation. xrelay: ALWAYS project `id`; inline `from:`
  in search strings is SILENTLY ignored; typed `--from` drops on OR-groups — one single-term
  query per keyword.
- **Verify the SUBJECT of a metric from its local context** (the KBCM lesson: the flagged "CSM
  quota" was AE quota — disproof two lines below the quote).
- **Licensing, all 7 clauses:** verify the LICENSE file at the upstream repo (API lies);
  registry mirrors are never a shortcut; a dangling LICENSE pointer is not a license; list
  EVERY license file in multi-license repos; package manifests count; check for renames
  (redirects make stale citations pass review — cite current names).
- **R21 figure-survival rule:** a figure is worth collecting only if (a) the reader must
  recognise-and-correct it, (b) its arithmetic IS the teaching, or (c) both sides are
  permalinked. Collect accordingly; grade everything.
- **Never trust WebFetch-extracted "latest model/version" claims**; the environment and primary
  sources are authoritative.
- **skills.sh:** undocumented `GET /api/search?q=` returns 100 results (CLI caps at 6);
  30 req/min; rate-limit errors LOOK like empty results — back off and retry.
- **Raw files:** each worker writes `research/raw/_raw-<channel>-<topic>.md` — every finding
  with its source link, quote, and grade. NOTHING lives only in chat. Channel leads write
  `research/channel-<X>-report.md` synthesizing their workers' raws with pointers into them.
- Do NOT use any Jina API key found anywhere; never echo keys.

## Artifact contract

- Raw docs: `/Users/tamas/Documents/Personal/Projects/sales-skill/research/raw/_raw-<channel><n>-<topic>.md`
- Channel reports: `/Users/tamas/Documents/Personal/Projects/sales-skill/research/channel-<a|b|c|d|e>-report.md`
- Channel report must end with: coverage statement (what was NOT searched), licensing ledger
  rows (C/D), and a "candidate never-ship figures" table.
- Controller writes `research/synthesis.md` after all five channels close. Synthesis is the gate.
