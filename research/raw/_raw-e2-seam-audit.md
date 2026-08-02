# E2 — Family Seam Audit for `sales`

Verified from disk against the 13 shipped packs at
`/Users/tamas/Documents/Personal/Projects/<pack>-skill/skills/<pack>/`. Every quote below was
re-read at its actual location; none reconstructed from memory. Line numbers are as of this
session's read; packs are live repos and may drift further before `sales` ships.

Sales's mission for reference: "Convert qualified demand into committed customers through a
repeatable buying process." Tier: Distribute (pairs with marketing). Flow: marketing → sales →
success.

---

## PART 1 — Verified seam-quote table

| # | Cited location | Actual location | Drift? | Verbatim quote |
|---|---|---|---|---|
| 1 | marketing `handoff.md:42` | `handoff.md:42` | **Exact** | `\| `sales` \| Qualified demand — a defined fit-plus-intent signal on a named account or contact, per [surface-b2b-sales-assisted.md](surface-b2b-sales-assisted.md) \| Pipeline and close-rate signal that feeds positioning and message iteration \| Revenue operations, sales enablement (battlecards, objection handling), and cold outbound/prospecting are `sales`'s, not marketing's — named explicitly in [surface-b2b-sales-assisted.md](surface-b2b-sales-assisted.md), because the incumbent genre routinely blends these into marketing and the family's seam is only real if stated \|` |
| 2 | marketing `SKILL.md:107` | `SKILL.md:107` | **Exact** | `\| Pipeline, CRM stages, revenue operations, sales enablement, **cold outbound and prospecting** \| `sales`. The genre routinely absorbs these into "marketing"; this pack does not \|` |
| 3 | marketing `lifecycle-and-email.md:16` | `lifecycle-and-email.md:16` | **Exact** | `- You need the CRM/pipeline sequencing around a sales-qualified lead → `sales`.` |
| 4 | marketing `surface-b2b-sales-assisted.md:51` | same file, `:51` | **Exact** | `...Three\nadjacent disciplines belong to `sales`, not to this pack, and should be named explicitly rather than\nabsorbed by default: **revenue operations, sales enablement (battlecards, objection handling,\npricing negotiation guidance), and cold outbound/prospecting.**` (line 51 is the "adjacent disciplines belong to `sales`" line) |
| 5 | marketing `surface-b2b-sales-assisted.md:111` | same file, `:111` | **Exact** | `- Absorbing cold outbound, sales enablement, or revops content into a marketing deliverable instead\n  of naming them as `sales`'s and routing there.` (line 111 is "of naming them as `sales`'s and routing there.") |
| 6 | growth `handoff.md:42` | `handoff.md:42` | **Exact** | `\| `sales` (provisional) \| An experiment readout on a funnel stage that touches a sales-assisted deal \| Pipeline and qualification signal that shapes which stage of a sales-assisted funnel is worth testing \| This seam is drawn provisionally, the way marketing drew its own — cold outbound, CRM stages, and deal mechanics stay `sales`'s regardless of which funnel stage an experiment touches \|` |
| 7 | growth `SKILL.md:112` | `SKILL.md:112` | **Exact** | `\| Pipeline, CRM stages, cold outbound and prospecting \| `sales` — this seam is provisional; see [handoff.md](references/handoff.md) \|` |
| 8 | growth `surface-b2b-sales-assisted.md:143` | same file, **`:144`** | **DRIFTED +1** | `- **The seam between growth and sales on this surface is being treated as settled** → it is not;\n  this surface's boundary is drawn provisionally, the same posture marketing used for its own B2B\n  surface, and should be flagged as such in any handoff.` |
| 9 | success `handoff.md:40` | `handoff.md:40` | **Exact** | `\| `sales` (unbuilt, provisional) \| The renewal workflow, up to a complex deal that needs negotiation \| The expansion sale itself in a sales-assisted motion \| Provisional, like growth drew its own sales seam. Lincoln Murphy's complexity-gated CS-native position — renewals should go to a dedicated CS-native resource, not "Account Management carryover" — is cited as contested vocabulary, not adjudicated. See [renewals-and-expansion](renewals-and-expansion.md) \|` |
| 10 | success `SKILL.md:101` | `SKILL.md:101` | **Exact** | `\| Negotiating and closing an expansion sale \| `sales` — provisional and contested; see [renewals-and-expansion](references/renewals-and-expansion.md) §6 \|` |
| 11 | success `renewals-and-expansion.md` §6 (charter said "around line 50") | §6 heading is actually at **line 117**; content runs 117–124 | **DRIFTED, large (~67 lines)** | §6 heading: `## 6. The sales seam — contested, not settled` (line 117). Full text at lines 119–124, quoted in full below. |
| 12 | product `SKILL.md:27` | `SKILL.md:27` | **Exact** | `experimentation and growth loops to `growth`; qualification and CRM to `sales`; onboarding, support,` |
| 13 | product — pricing/tier DESIGN and dunning/billing ownership | grepped, not a fixed cite | N/A | See finding below: product asserts pricing-tier ownership itself (`business-model.md`); product **never mentions "dunning" or "billing" anywhere in its own pack**. The dunning/billing-to-product assignment is made by `success`, one-sidedly — see Part 3. |
| 14 | automation `SKILL.md:104` | `SKILL.md:104` | **Exact** | `\| Authoring the business rule, or customer-facing comms \| `product` · `marketing` · `sales` · `success` \|` |
| 15 | automation `process-capture.md:15` | `process-capture.md:15` | **Exact** | `- The rule already exists in writing, owned by `product`, `marketing`, `sales`, or `success` — read it\n  and cite the owner; do not recapture it here. (At this pack's launch those three commercial upstreams\n  do not yet exist as shipped skills — say that plainly rather than inventing an owner.)` |
| 16 | automation `process-capture.md:163` | `process-capture.md:163` | **Exact** | `- **No owner exists for the rule** — do not invent one. Record the gap and route to the nearest\n  commercial skill once it exists (`product`, `marketing`, `sales`, `success`).` |

**Score: 14 fixed line-cites checked, 12 exact, 2 drifted** (growth surface file: +1 line; success
renewals-and-expansion §6: the charter's "around line 50" estimate was off by ~67 lines — §6 is the
6th of 7 numbered sections in a 167-line file, not near the top).

### Note on automation's historical framing (items 14–16)

`process-capture.md:15` explicitly states that **at automation's launch, `product`, `marketing`,
and `sales` did not yet exist as shipped skills** ("those three commercial upstreams do not yet
exist as shipped skills — say that plainly rather than inventing an owner"). That statement is now
stale for `product` and `marketing` (both have since shipped) but still literally true for `sales`.
This is scaffolding automation left for exactly this moment — sales should not need to change
anything in automation to close this; the sentence self-resolves once sales ships (a future
automation edit, not sales's problem to fix).

### Product's pricing/dunning/billing ownership — full picture

- Product **claims pricing-tier structure itself**, in detail, in `business-model.md` (`## 2.
  Pricing hypothesis`, lines 60–102): value-based pricing method, Van Westendorp price-sensitivity,
  and "Tier psychology" (center-stage effect, decoy effect, anchoring) — explicitly framed as
  *"it shapes presentation of an already-justified price, not the price itself"* (`business-model.md`,
  end of the Tier psychology block). This is page-level/pricing-page psychology, not a sales rep's
  live price presentation in a deal.
- Product's own pack contains **zero occurrences of "dunning"** and **zero occurrences of
  "billing"** (`grep -rn "dunning" product-skill/skills/product/` and `grep -rn "billing"
  product-skill/skills/product/` both return nothing).
- The assignment of "dunning and billing-failure recovery" to `product` is made **only from
  success's side**: `success/skills/success/SKILL.md:99` — `\| Pricing tiers and the
  commercial-lifecycle model, the metric tree, PRD acceptance criteria, dunning and
  billing-failure recovery \| `product`. \|` — and `marketing/references/lifecycle-and-email.md:17`
  — `- The email is dunning/billing-failure recovery → `product`.` Product itself never states this
  ownership. This is a one-directional cession pattern the family already tolerates elsewhere (see
  success's own "Three rows this file originates" — packs sometimes get assigned territory in a
  later-shipped sibling's docs without reciprocating language in their own file, because they
  shipped first and the assigning pack shipped after).

---

## PART 2A — Full read: marketing's `surface-b2b-sales-assisted.md`

Path: `/Users/tamas/Documents/Personal/Projects/marketing-skill/skills/marketing/references/surface-b2b-sales-assisted.md` (114 lines). This is marketing's single most sales-relevant file — the closest thing in the shipped family to a pre-drawn spec for `sales`.

### Structure (every heading, in order)

1. `# Surface: B2B Sales-Assisted` (title, purpose, read-when/skip-when, inputs/produces — lines 1–24)
2. `## Contents` (line 26)
3. `## The 95-5 reality` (line 35)
4. `## The marketing→sales seam` (line 47)
5. `## ABM-lite, honestly` (line 60)
6. `## Longer cycles change what attribution can answer` (line 69)
7. `## The B2B brand/activation split: what is and isn't known` (line 82)
8. `## Failure modes` (line 105)

### Every statement about what `sales` does, owns, receives, or returns (verbatim, with lines)

- **Line 3–4 (Purpose):** "State how the marketing jobs reshape when a human sales conversation gates the deal — the 95-5 reality, the marketing/sales handoff, and where B2B-specific evidence runs out."
- **Line 22–24 (Produces):** "demand-generation and qualified-lead output framed for a sales handoff, with the attribution honesty this cycle length requires, and an explicit statement of which B2B numbers are evidence-backed and which are not."
- **Lines 41–45 (§ The 95-5 reality):** "...most B2B marketing activity is necessarily **memory-building for a future buying window, not capture of a buyer who is in-market today**, and a demand-gen program judged purely on this-quarter pipeline will systematically undercount its own value to the large majority of accounts not yet ready to talk to sales."
- **Lines 49–58 (§ The marketing→sales seam — the core statement):**
  - Line 49–51: "Marketing's job on this surface ends at a qualified handoff — a defined signal (fit + intent) that a named account or contact is ready for a sales conversation, not a name added to a list. Three adjacent disciplines belong to `sales`, not to this pack, and should be named explicitly rather than absorbed by default:"
  - Line 51–53: "**revenue operations, sales enablement (battlecards, objection handling, pricing negotiation guidance), and cold outbound/prospecting.**"
  - Line 53–56: "A pack that blends these into marketing content is repeating the incumbent genre's most common boundary failure — nearly every surveyed competitor pack folds prospecting and cold-email into "marketing," and the family's declared seam is a real differentiator only if it is drawn here explicitly, not assumed."
  - Line 56–58: "Marketing supplies the qualified-demand definition and the assets sales pulls from (case studies, competitive positioning); it does not run the outbound sequence or own the CRM pipeline stage."
- **Lines 62–67 (§ ABM-lite, honestly):** ABM-lite ("a handful of named target accounts, no dedicated ABM platform") is marketing's territory as a *resourcing decision* ("concentrate content, outreach, and even paid spend on a short named list"), explicitly framed as craft, not evidence-backed method — this is marketing's own call, not ceded to sales.
- **Lines 76–80 (§ Longer cycles...):** "self-reported attribution ('how did you hear about us,' asked **at the point closest to the sales conversation**) becomes proportionally more valuable" — implies marketing instruments a question near/at the sales handoff point, but the conversation itself is sales's.
- **Line 96–99 (§ B2B brand/activation split):** cites Jason Lemkin distinguishing a market where you must displace an entrenched competitor vs. one where the contest is for discretionary budget — "the GTM motion **and the sales hire profile** should match which situation is actually in play" — the only place this file touches sales *hiring*, framed as GTM strategy input, not sales's own operating doctrine.
- **Lines 107–111 (§ Failure modes, the sales-relevant ones):**
  - Line 107–109: "Judging a demand-gen program purely on this-quarter pipeline when most of the addressable category is provably not in-market this quarter — report memory-building contribution alongside pipeline, not instead of it."
  - Line 110–111: "Absorbing cold outbound, sales enablement, or revops content into a marketing deliverable instead of naming them as `sales`'s and routing there."

### What this file establishes about sales's territory, synthesized

Marketing cedes exactly three named disciplines to sales, verbatim and repeated in three places in
this file (lines 51–53, 107–111, and echoed in the `Not this skill` table of `SKILL.md:107`):
**(1) revenue operations, (2) sales enablement — explicitly including battlecards, objection
handling, and pricing negotiation guidance, (3) cold outbound/prospecting.** Marketing additionally
states, once, that it **does not own the CRM pipeline stage** (line 58) — this is the clearest
disk-verified statement that CRM/pipeline structure is sales's. Marketing's own boundary is a
**qualified handoff** — "a defined signal (fit + intent) that a named account or contact is ready
for a sales conversation" (line 49–50) — which is the literal artifact marketing→sales handoff rows
describe across marketing, growth, and (by inheritance) success.

---

## PART 2B — Bonus full read: growth's own `surface-b2b-sales-assisted.md`

Growth ships a same-named file (146 lines) that is nearly as sales-relevant and was not explicitly
requested but is directly load-bearing for sales's handoff — full content captured here since it
answers Part 3 Q4 in full.

Structure: `## 1. Why the feasibility gate bites hardest here` → `## 2. What's still testable, and
what isn't` → `## 3. Randomization gets harder, not just smaller` → `## 4. The three levers, applied
doubly hard` → `## 5. The marketing seam` → `## 6. Retention means the account, not the user` →
`## Failure modes and handoff`.

Key sales-relevant statements:
- Line 14: "The funnel being diagnosed spans deal stages (MQL → SQL → opportunity → closed-won), not page views or signups." — the only place in the family that spells out a B2B funnel stage sequence.
- Lines 64–65: bottom-of-funnel artifacts named explicitly as sales's: "a demo script variant, a proposal template, how a rep frames pricing on a call."
- Lines 73–78: "a rep, not a system, often decides in practice who sees which script or which proposal structure, which threatens clean random assignment... sales attention itself is a scarce, human resource, withholding a treatment from a 'control' account can carry a real relationship cost."
- Lines 94–96: "MQL-to-SQL or demo-booked conversion has far more volume than closed-won" — names the funnel checkpoints growth can test vs. sales-owned closed-won.
- Lines 99: "the decision should be made on qualitative signal (rep feedback, win/loss interviews)" — names win/loss interviews as an existing sales artifact growth consumes qualitatively, never formally tests.
- Lines 110–112: "Marketing hands growth a qualified hypothesis for a funnel experiment; growth reads back a result scoped to the funnel stage it could actually power, and does not extend that result's confidence to a deal-stage outcome it didn't test." — growth explicitly declines to extend test confidence into sales's deal stage.
- Lines 141–143: "The question is the qualified-lead definition, ABM strategy, or the marketing/sales handoff itself → `marketing`'s surface-b2b-sales-assisted.md and, for prospecting/outbound/pipeline, `sales` — growth does not own either."
- Lines 144–146 (already quoted in Part 1 #8): the provisional-seam flag.

---

## PART 2C — Full-family term sweep

Swept all 13 packs (`grep -rin` recursive, case-insensitive) for the requested terms. Results
below, grouped by genuine commercial-sales relevance vs. noise, then two derived lists.

### Noise report (terms dominated by unrelated hits)

| Term | Total hits (13 packs) | Noise source |
|---|---|---|
| `pipeline` | 340 | CI/CD pipelines, data pipelines, build pipelines, handoff-routing "pipeline" (design/product/architecture/backend/data/automation/operate). Genuine sales-pipeline hits are confined to marketing/growth/success handoff rows already quoted in Part 1/2A/2B. |
| `contract` | 591 | API/service contracts (architecture, backend), design-system "component contracts," legal-adjacent but non-sales contract law only appears inside success's renewal-notice-period discussion (already captured). |
| `SQL` | 137 | Structured Query Language (data, backend) almost entirely. Genuine "SQL" = Sales-Qualified-Lead hits are exactly 2, both in growth's `surface-b2b-sales-assisted.md` (MQL → SQL funnel stage, line 14) plus marketing's spelled-out "sales-qualified lead" (`lifecycle-and-email.md:16`, already in Part 1). |
| `quota` | 61 | 100% API rate-limit / resource-quota noise (automation's `cost-and-quota.md`, Salesforce API allocation, k8s-style resource quotas). **Zero packs anywhere in the family mention a sales rep's quota.** |
| `commission` / `contract` stem match | 35 | Almost entirely "**de**commission**ing**" (operate's decommissioning.md, quality's inherited severity scale note, architecture's ADR lifecycle). **Zero genuine sales-commission-plan content anywhere in the family.** |
| `demo` | 57 total, 4 outside marketing/growth/success | Mostly "demonstrate," design's onboarding "sample-data demo," architecture's "not a demo or a deadline." Genuine sales-demo content lives in marketing's and growth's B2B surface files (already captured). |
| `discovery` | 90 | Dominated by product's own JTBD/user-research "discovery" (an entire `discovery.md` file) and UX-research "discovery" in design. Zero hits for "sales discovery call" as a term anywhere in the family — the concept exists (growth's demo-booked/proposal-sent funnel) but the phrase "discovery call" is never used. |
| `lead` (word-boundary) | 99 total, 25 outside the three commercial packs | Verb "lead" (design/critique "lead with," "design lead"), "lead agent" (ai/architecture multi-agent), "lead time" (operate DORA metric), "on-call lead." Two borderline hits: design's `journeys.md:39` uses "Lead Qualification" as a **negative example** of internal jargon to avoid in a customer journey map's phase names (not an ownership claim); product's `surface-website.md:39,41` uses "lead quality" and "visit→lead vs. lead→customer" as PRD success metrics for a website surface — descriptive funnel vocabulary, not a claim on lead *definition* (product already cedes "qualification" to sales at `SKILL.md:27`). |
| `AE`, `SDR`, `close rate`, `upsell`, `cross-sell`, `account executive` | 0 | Not used anywhere in the shipped family. |
| `buyer` | 61 total, 7 outside marketing/growth/success | Generic UX/market-sizing usage (design's "industrial buyer reads more," product's "buyer power" in Porter's Five Forces, "the buyer is not the user" in product's internal-tools surface). None claims sales territory. |
| `expansion` | 66 total, 15 outside success/growth | Mostly i18n text-expansion (frontend, design) and RTL/locale budget language — unrelated. One genuine near-hit: product's `business-model.md:76`, "Name one expansion lever (usage overage, add-on, seat growth) as a secondary revenue path" — product's own pricing-hypothesis language, related to but distinct from success's NRR "expansion" and sales's "expansion sale." See collision note in Part 3. |
| `selling` | 17 outside the three commercial packs | Licensing language ("blocks reselling as a hosted service," ai/backend/data DB-license discussions) — unrelated to sales-the-discipline. |
| `qualif` | 73 | Mostly "unqualified claim" (quality's conformance-claim vocabulary), "disqualify" (design's research screener), TS type-narrowing "qualified name" (data lineage). Genuine hits already captured in Part 1/2A (product SKILL.md:27, marketing/growth handoff rows). |

### Genuine hits, grouped by pack

**`marketing`** — the deepest source; every genuine hit already quoted in full in Part 1 and Part
2A (`handoff.md:42`, `SKILL.md:9,79,92,107`, `lifecycle-and-email.md:16`,
`surface-b2b-sales-assisted.md` in full, `audience-and-segmentation.md:72` — "through those stages —
PLG motion, outbound, SEO, paid, sales-assisted — is secondary to whether the funnel reaches...",
`email-compliance-checklist.md:55` — "Contact details were obtained **in the course of a sale** (or
negotiations for one)" as a CAN-SPAM consent-basis checklist item).

**`growth`** — `handoff.md:42`, `SKILL.md:9,112,137,160`, `surface-b2b-sales-assisted.md` in full
(Part 2B).

**`success`** — `SKILL.md:10,73,101`, `handoff.md:40,64`, `renewals-and-expansion.md` §1 and §6 in
full (Part 3), `surface-b2b-high-touch.md` §5 in full (Part 3), `support-process-design.md:53,55`
("a first-class bucket for contacts that are **not support at all**" includes "spam, sales
reroute"/"sales leads" as things a support taxonomy must not misclassify), `onboarding-and-adoption.md:111`
(routes account-level QBR/executive-sponsorship cadence in a sales-assisted motion to
`surface-b2b-high-touch.md`).

**`product`** — `SKILL.md:27` (the CRM/qualification cession), `business-model.md:60–102` (pricing
tier structure and page-psychology, product's own territory, adjacent to but not the same as sales's
"pricing presentation" in a deal), `discovery.md:71` ("a sales conversation with a real ask for
money or a signed pilot" as product's cheapest-probe validation method — product *uses* a sales
conversation as evidence, does not claim to own selling), `surface-website.md:39,41` (lead-quality
metric language, descriptive).

**`automation`** — `SKILL.md:104`, `process-capture.md:15,163` (Part 1), plus a distinct and
important overlap: automation owns **CRM sync mechanics as a system-of-record**, not CRM
*structure*. Genuine quotes: `sync-semantics.md:206` — "owns **the write path into an operational
system of record** — a CRM, a support tool, a ledger"; `surface-code-first-durable.md:12,48` — CRM
writes as an example of an irreversible early step needing a durable-execution resume guarantee;
`compensation-and-recovery.md:62,114` — a CRM record delete/correct as a compensating action;
`cost-and-quota.md:160-166` — Salesforce's API rate-limit mechanics (a vendor-quota fact, not a
sales-quota fact); `assets/handoff.yaml:18` — "Stripe payment → CRM record → Slack" as a workflow
shape example.

**`design`** — no genuine ownership claims. Two descriptive mentions: `journeys.md:39` (jargon
example, see noise table), `surface-webapp.md:62,72` (Salesforce/SLDS cited purely as a design-system
reference point for enterprise-webapp visual conventions, not the business).

**`architecture`, `frontend`, `backend`, `ai`, `data`, `quality`, `operate`** — **zero genuine
sales-relevant ownership claims found.** `quality` in particular never mentions "sales" anywhere in
its pack (`grep -rin "sales" quality-skill/skills/quality/` returns nothing) — it is the one shipped
pack with no opinion on the sales seam at all. `data`'s only relevant material is reverse-ETL "sync
into CRM" as an *activation* mechanism (`surface-operational-activation.md:8,86`), the analytics-side
mirror of automation's sync-mechanics point above, not a claim on CRM structure.

### Derived list 1 — Cessions TO sales (binding)

These are places a sibling explicitly hands something to sales or states it is sales's:

1. **marketing** — revenue operations, sales enablement (battlecards, objection handling, pricing
   negotiation guidance), cold outbound/prospecting (`surface-b2b-sales-assisted.md:51-53`,
   restated `handoff.md:42`, `SKILL.md:107`).
2. **marketing** — does not own the CRM pipeline stage (`surface-b2b-sales-assisted.md:58`) — the
   clearest statement that CRM/pipeline structure is sales's.
3. **marketing** — the CRM/pipeline sequencing around a sales-qualified lead
   (`lifecycle-and-email.md:16`).
4. **growth** — pipeline, CRM stages, cold outbound and prospecting (`SKILL.md:112`), and deal
   mechanics on any funnel stage an experiment touches (`handoff.md:42`) — both marked
   **provisional**.
5. **growth** — the marketing/sales handoff itself and prospecting/outbound/pipeline
   (`surface-b2b-sales-assisted.md:141-143`) — growth "does not own either."
6. **product** — qualification and CRM (`SKILL.md:27`) — the one *unqualified* (non-provisional)
   cession to sales found anywhere in the family.
7. **success** — negotiating and closing an expansion sale (`SKILL.md:101`), the expansion sale
   itself in a sales-assisted motion (`handoff.md:40`) — marked **provisional and contested**.
8. **automation** — authoring the business rule or customer-facing comms, shared among
   `product`/`marketing`/`sales`/`success` (`SKILL.md:104`).

### Derived list 2 — Claims that OVERLAP sales's scope (potential contradictions, to adjudicate)

1. **product owns pricing-tier structure and pricing-page psychology** (decoy, anchoring,
   center-stage — `business-model.md:60-102`). Sales's mission claims "pricing/packaging
   PRESENTATION (design is product's)" — read together, this is consistent (product designs the
   tiers and the page-level psychology; sales presents/negotiates price within a live deal — a
   different presentation context), but it is a seam sales must state explicitly, because the word
   "presentation" is used by both in different senses.
2. **automation owns CRM sync/write-path mechanics** as an operational system of record
   (`sync-semantics.md:206`, `surface-code-first-durable.md:12,48`,
   `compensation-and-recovery.md:62,114`). Sales's mission claims "CRM structure." These are
   different layers (automation = how data gets written/synced reliably; sales = what
   fields/stages/pipeline definition exist) but the word "CRM" is claimed by both — needs an
   explicit line in sales's own handoff.
3. **success owns dunning/billing-failure recovery language, attributed to product, but product
   never claims it itself** (see Part 1 item 13). Not sales's territory either way, but a live
   unreciprocated cession sales should note, not repeat.
4. **product's "expansion lever" (business-model.md:76) vs. success's NRR "expansion"
   (renewals-and-expansion.md) vs. sales's "expansion sale" (success's cession)** — three packs use
   "expansion" for adjacent but distinct things: product = a secondary pricing/revenue path
   designed into the tier structure; success = the NRR metric and the renewal-cycle account
   conversation; sales (per success's cession) = closing the expansion sale when a negotiation
   exists. Not contradictory, but the same word needs sales to be precise about which sense it
   means on first use.
5. **growth's B2B surface names bottom-of-funnel sales artifacts (demo script, proposal template,
   rep-framed pricing) as things it evaluates but does not own or test formally**
   (`surface-b2b-sales-assisted.md:64-65,91-93`) — confirms these are sales's content to author;
   growth only comments on their testability.

---

## PART 3 — Contradiction hunt

### 1. Does any shipped pack claim territory that sales's mission list claims?

**No firm claim found.** Every sibling that touches sales's claimed territory (CRM, pipeline,
outbound, qualification, deal mechanics, expansion-sale closing) either explicitly cedes it to
`sales` or marks its own position as provisional/contested pending sales's arrival. The two
closest things to a live overlap are not ownership claims but **adjacent-layer** claims that need a
stated boundary, not a fight:
- **automation** owns CRM *sync/write-path mechanics* (a system-of-record integration concern), not
  CRM *structure* — see Derived list 2, item 2.
- **product** owns pricing-tier *design and psychology*, not price *presentation/negotiation inside
  a live deal* — see Derived list 2, item 1.

Neither is a contradiction; both are boundary lines sales should draw explicitly on its own side,
the same way marketing drew "does not own the CRM pipeline stage" on its side
(`surface-b2b-sales-assisted.md:58`).

### 2. Does success's "contested" renewal/expansion position actually read as contested, or was it flattened?

**Genuinely contested, not flattened.** `renewals-and-expansion.md` §6 (lines 117–124), quoted in
full:

> `## 6. The sales seam — contested, not settled`
>
> `§1's "sales closes the expansion sale" clause is provisional, and it is directly contested by the`
> `canon's own co-author. lincolnmurphy's position is complexity-gated, not role-based: a CSM renews`
> `by default; only genuinely complex renewals route to a dedicated CS-native resource, explicitly`
> `*not* "Account Management carryover" (x.com/lincolnmurphy/status/1084526744290369537 and`
> `x.com/lincolnmurphy/status/1084522527991480325, both Jan 13 2019). Cite both positions in any handoff that touches`
> `this seam; this file does not adjudicate the industry fight.`

This is reinforced in three more places on disk, not just asserted once: `SKILL.md:101` ("provisional
and contested"), `handoff.md:40` ("cited as contested vocabulary, not adjudicated"), and
`surface-b2b-high-touch.md:139-143` (near-identical restatement, citing the same two tweets). The
Validation section of `renewals-and-expansion.md` even makes it a checked invariant: "Renewal
ownership on this surface states the sales clause as provisional, not settled" (line 154). Success
did not flatten this — it is unusually careful to keep both sides live and to cite primary sources
(dated tweets) for the contest.

### 3. Is marketing's cession genuinely "flat and firm"?

**Yes.** Quoted three times verbatim, identically in substance each time:
- `surface-b2b-sales-assisted.md:51-53`: "Three adjacent disciplines belong to `sales`, not to this
  pack... **revenue operations, sales enablement (battlecards, objection handling, pricing
  negotiation guidance), and cold outbound/prospecting.**"
- `handoff.md:42`: "Revenue operations, sales enablement (battlecards, objection handling), and cold
  outbound/prospecting are `sales`'s, not marketing's."
- `SKILL.md:107`: "Pipeline, CRM stages, revenue operations, sales enablement, **cold outbound and
  prospecting** | `sales`. The genre routinely absorbs these into 'marketing'; this pack does not."

No hedge word ("provisional," "contested," "for now") appears anywhere near this cession. Marketing
also states, unprompted, *why* it draws the line this hard: "nearly every surveyed competitor pack
folds prospecting and cold-email into 'marketing,' and the family's declared seam is a real
differentiator only if it is drawn here explicitly, not assumed" (`surface-b2b-sales-assisted.md:54-56`).
This is the firmest, least-hedged cession in the entire audit.

### 4. Does growth really say deal mechanics stay sales's "regardless of which funnel stage an experiment touches"?

**Yes, verbatim, `handoff.md:42`:**

> "This seam is drawn provisionally, the way marketing drew its own — cold outbound, CRM stages, and
> deal mechanics stay `sales`'s **regardless of which funnel stage an experiment touches**."

Note the row itself is marked `(provisional)` in the Sibling column — so the *seam* is provisional,
but within that provisional seam, the stated rule ("regardless of which funnel stage...") reads as
unconditional. This is a nuance sales should preserve precisely: growth hedges *whether it drew the
line in the right place*, not *whether deal mechanics are sales's* — those are two different kinds
of hedge, and collapsing them into one would misrepresent growth's position.

### 5. Naming collisions — same term, different meaning across packs

| Term | Pack A meaning | Pack B meaning | Files |
|---|---|---|---|
| "expansion" | success: NRR/GRR net-revenue-retention metric and the renewal-cycle account conversation | product: a secondary pricing/revenue lever named in the tier design (usage overage, add-on, seat growth) | `success/renewals-and-expansion.md` vs `product/business-model.md:76` |
| "expansion" (again) | growth: an experiment run on a retention/resurrection mechanic | success/sales (per cession): the account-level commercial event sales closes | `growth/handoff.md:42` ("(provisional)" retention-experiment row) vs `success/handoff.md:40` |
| "qualification" | product/marketing: lead/account fit-plus-intent signal ceded to sales | design: explicitly rejected as a customer-journey *phase name* ("Research", not "Lead Qualification") because it's internal jargon, not user vocabulary | `product/SKILL.md:27`, `marketing/surface-b2b-sales-assisted.md` vs `design/journeys.md:39` |
| "pipeline" | marketing/growth/sales: sales deal pipeline / CRM pipeline stage | design/product/architecture/backend/data/automation/operate: CI/CD, data, or build pipeline; also design's "pipeline routing" for the handoff.yaml machine companion | pervasive — see noise table |
| "CRM" | marketing/growth/sales: pipeline stages, deal structure, revenue operations | automation/data: an operational *system of record* to sync into/out of (reverse-ETL, durable writes) | `marketing/surface-b2b-sales-assisted.md:58` vs `automation/sync-semantics.md:206`, `data/surface-operational-activation.md:8,86` |
| "sales enablement" | marketing: explicitly ceded to `sales`, includes battlecards/objection handling | (no sibling uses "customer enablement" or a colliding second sense on disk — searched, not found) | `marketing/handoff.md:42` |
| "SQL" | data/backend: Structured Query Language (137 raw hits) | growth: Sales-Qualified Lead, in the MQL→SQL funnel-stage sequence (2 hits) | `growth/surface-b2b-sales-assisted.md:14` |
| "discovery" | product: JTBD/user-research discovery (an entire file) | growth/marketing (implicitly, via "demo booked" language): no pack on disk uses the phrase "discovery call" for a sales meeting — the concept exists in growth's funnel-stage language but the term itself is unclaimed | `product/references/discovery.md` vs nowhere |
| "lead" | design: rejected internal-jargon example ("Lead Qualification") | product: descriptive PRD metric ("lead quality," "visit→lead") | `design/journeys.md:39` vs `product/surface-website.md:39,41` |

"Discovery call" as a *term* is genuinely unclaimed — no pack uses that exact phrase — which means
sales can define it without contradicting anyone, but should be careful not to collide with
product's much heavier, already-shipped use of bare "discovery" for JTBD research.

### 6. Anything on disk that CONTRADICTS the sales axis — do not smooth

Two findings worth flagging loudly rather than smoothing:

- **Contradiction candidate, resolved on inspection:** success's `handoff.md:40` calls the sales row
  "(unbuilt, provisional)" — accurate at time of writing, since sales did not exist. This is not a
  contradiction sales needs to fix; it is a placeholder that self-resolves the moment sales ships
  (the same way automation's `process-capture.md:15` self-resolves). No sibling file needs editing
  for these two mentions to become true.
- **A real asymmetry, not a contradiction, but load-bearing:** the dunning/billing-to-product
  assignment (Part 1, item 13) is made unilaterally by `success` and `marketing`, with zero
  reciprocal statement inside `product`'s own pack. If sales ever needs to route a
  billing-failure-adjacent question (e.g., a deal that stalls on a failed initial payment, or a
  renewal that fails to process), the two siblings that *would* route it (success, marketing) both
  say "product," but product's own file is silent — sales should route to `product` per the two
  siblings' documented position, but should not claim product "says so itself," because it doesn't.
- **No genuine contradiction of the sales mission's explicit ownership list was found** — ICP/account
  selection, qualification frameworks, sales stages, discovery calls, demo strategy, objection
  handling, proposals, CRM structure, pipeline management, forecasting, win/loss learning are all
  either explicitly ceded (Derived list 1) or simply never claimed by any shipped sibling (forecast:
  only 2 non-sales-forecast hits found family-wide, in product's TAM disclaimer and success's
  churn-forecast disclaimer — neither claims sales forecasting; ICP: exclusively marketing's, framed
  as *marketing's own segmentation model*, not sales's territory-of-selection — worth flagging as
  the one place sales's mission list ("ICP/account selection") and marketing's shipped content most
  need a precise joint boundary, since marketing owns "ICP-as-a-funnel" model
  (`audience-and-segmentation.md:65-103`) while sales's mission claims "ICP/account selection" — these
  are likely the same thing looked at from two ends of one funnel, and sales should state explicitly
  that it inherits marketing's ICP *definition* and applies it to *account selection/prioritization*,
  rather than defining ICP from scratch).

---

## Handoff-row format — precise structure, for sales to match exactly

Read `handoff.md` in full for marketing, growth, and success (all three; success also gave the
"three rows this file originates" structural device, useful precedent since sales, like success,
ships after siblings that already reference it).

**Universal table shape**, identical across all three packs:

```
| Sibling | What [pack] hands it | What [pack] consumes from it | The line [pack] does not cross |
|---|---|---|---|
```

Four columns, always in this order: (1) the sibling pack name in backticks, optionally suffixed with
a **parenthetical hedge tag** — `(provisional)`, `(unbuilt, provisional)`, or no tag for a firm row;
(2) what flows downstream *to* the sibling; (3) what flows back *from* the sibling; (4) an explicit
negative statement — "the line X does not cross" — almost always containing the phrase "X does not
[own/set/build/run/etc.]" and usually citing the specific file:line where the sibling itself made
the cession, in backticked-filename form.

**Representative rows, verbatim:**

- Firm row (no hedge), marketing→design:
  `| `design` | Landing-page requirements (goal, claims, proof, objections), copy, E-E-A-T content requirements, structured-data requirements | Page composition, design's surface-website product-narrative question chain — the 8 beats — cited by name and never restated here, the copy-fidelity ladder, in-product voice/tone (design owns it; marketing owns the external voice) | Marketing does not compose the page or design the interaction; it supplies what the page must claim and prove |`
  (`marketing/references/handoff.md:37`)

- Provisional row, growth→sales:
  `| `sales` (provisional) | An experiment readout on a funnel stage that touches a sales-assisted deal | Pipeline and qualification signal that shapes which stage of a sales-assisted funnel is worth testing | This seam is drawn provisionally, the way marketing drew its own — cold outbound, CRM stages, and deal mechanics stay `sales`'s regardless of which funnel stage an experiment touches |`
  (`growth/references/handoff.md:42`)

- Doubly-hedged row, success→sales:
  `| `sales` (unbuilt, provisional) | The renewal workflow, up to a complex deal that needs negotiation | The expansion sale itself in a sales-assisted motion | Provisional, like growth drew its own sales seam. Lincoln Murphy's complexity-gated CS-native position — renewals should go to a dedicated CS-native resource, not "Account Management carryover" — is cited as contested vocabulary, not adjudicated. See [renewals-and-expansion](renewals-and-expansion.md) |`
  (`success/references/handoff.md:40`)

**How a hedge is written, precisely:**
- In the **Sibling column** (first column), as a parenthetical immediately after the backticked
  name: `` `sales` (provisional) `` or `` `sales` (unbuilt, provisional) ``. Never in a separate
  column, never as a footnote.
- In the **"line does not cross" column** (fourth column), the hedge is *restated in prose*, usually
  opening the cell: "This seam is drawn provisionally, the way marketing drew its own..." or
  "Provisional, like growth drew its own sales seam..." — each pack that hedges explicitly compares
  its hedge to a prior sibling's hedge, building a citation chain (marketing → growth → success, all
  provisional in the same style, each one naming the one before it).
- A **contested** (as opposed to merely provisional) seam gets extra weight: both named positions are
  cited with primary sources (success cites two dated tweets by name), and the file states in its own
  Validation/invariant section that the contested status must not be silently resolved (`renewals-and-expansion.md:154`,
  `surface-b2b-high-touch.md:154`).

**Success's structural precedent most relevant to sales:** because success shipped after
product/operate/automation but those packs' own `handoff.md` files don't reciprocate a success row,
success added a `## Three rows this file originates` section explicitly stating "these three cede
work to success in prose and router tables, but none of their own `handoff.md` files carries a
success row... State that plainly rather than treating the absence as an oversight"
(`success/references/handoff.md:42-45`). **Sales does not need this device** — unlike success, sales
already has pre-drawn (if provisional) rows in all three packs that would plausibly reference it
(marketing, growth, success), verified in Part 1. Sales's handoff.md can therefore write firm
mirror-rows back to marketing, growth, and success from day one, rather than needing an
"originates" section — but should note in its own file, once, that automation's and product's
silence on sales (no sales row in either's handoff.md) is not an oversight either — automation named
the gap explicitly and it self-resolves; product's cession lives in prose (`SKILL.md:27`) rather than
a handoff row, which is consistent with how product's `handoff.md` is structured generally (worth a
quick check by whoever writes sales's actual handoff.md, not performed here since product's own
handoff.md file was not part of this charter's cite list).

---

## Coverage statement — what this audit did NOT check

- **Did not read every reference file in every pack end-to-end.** Full reads were performed only for:
  marketing's `surface-b2b-sales-assisted.md` (required), growth's `surface-b2b-sales-assisted.md`
  (bonus, high-value), success's `renewals-and-expansion.md` §§1 and 6 (not the full file — §§2-5,7
  and Validation/Failure-modes were read but not exhaustively quoted), success's
  `surface-b2b-high-touch.md` §5 and surrounding context (not the full 169-line file).
- **Did not read product's, automation's, marketing's, growth's, or success's `handoff.md` files
  end-to-end beyond the sections quoted** — the seam-map table and immediately adjacent sections were
  read in full for marketing/growth/success; product's and automation's own `handoff.md` files (if
  they exist as separate from SKILL.md's Not-this-skill table) were not located/read in this pass —
  worth a follow-up grep by whoever writes sales's own handoff.md.
- **Did not check design, architecture, frontend, backend, ai, data, quality, or operate's
  `handoff.md` files for a sales row** beyond the single confirming grep in Part 2C ("no other pack's
  handoff.md mentions sales") — that grep covered all 10 remaining packs' `handoff.md` files and
  found nothing, so this gap is narrow, but individual reference files in those 10 packs were only
  searched by keyword, not read end-to-end.
- **Did not verify every SOURCES.md/licensing file** for sales-adjacent citations (e.g., whether any
  pack's sourced research touches CRM vendors, sales methodology books, or B2B sales content) — out
  of scope for a seam audit, flagged only in case a later research phase needs it.
- **Did not check assets/, agents/, or evals/ directories exhaustively** — spot-checked only where a
  grep hit landed there (e.g., growth's `evals/routing/cases.json`, automation's
  `assets/handoff.yaml`). A full eval-case sweep for sales-adjacent test cases was not performed.
  worth noting: `growth/skills/growth/evals/never-ship/cases.json:52` and `evals/stats-cases/cases.json:12`
  both surfaced in the "win rate" grep — these are growth's own eval fixtures, not doctrine, and were
  not analyzed further.
- **Line numbers throughout are as-read in this session** — packs are live repos; if any sibling pack
  is edited before sales writes its own SKILL.md/handoff.md, these line numbers should be
  re-verified, though the verbatim quotes themselves should still be findable by `grep -n` even if
  shifted.
