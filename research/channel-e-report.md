# Channel E report — webdesign lift + family seam audit

Lead: Channel E (opus sub-orchestrator) · Workers: 2 sonnet · Date: 2026-08-03
Raws: [`_raw-e1-webdesign-lift.md`](raw/_raw-e1-webdesign-lift.md) · [`_raw-e2-seam-audit.md`](raw/_raw-e2-seam-audit.md)

**Provenance note (WebSearch incident):** Channel E is 100% local-disk work — file reads plus
`grep` over the shipped repos. Neither worker issued a single web query. The crew-wide WebSearch
quota death (200/200) that made nulls unsafe in other channels **does not touch any finding here**;
E1's null result in particular is read-and-grep-derived over 22 local files, not a search null.

**Lead verification:** I independently re-checked the five highest-stakes claims before writing
(product's dunning/billing absence, both drifted line numbers, marketing's `handoff.md:42` and its
`:58` CRM disclaimer). All confirmed. I also closed W2's one open coverage gap myself — see §C.0.

---

## §A — Webdesign lift manifest

Source: `/Users/tamas/.claude/skills/webdesign/` (v1.2.0, MIT, `github.com/gabros20/webdesign`).
**22/22 files read in full** (~3,707 lines). No binaries. No file was thin or empty.

### A.1 — LIFT-TO-SALES — **EMPTY. VERIFIED NULL.**

**There is zero client-sales content in the retiring webdesign skill.** This is the headline, and it
should be treated as settled: the sales build must not budget any further cycles re-scanning it.

The corpus is a pure design / art-direction / frontend-build system. A targeted grep for
`proposal|contract|negotiat|deposit|retainer|invoice|estimate|quote|SOW|discovery call|sales call|
prospect|lead gen|pipeline|CRM|win.loss|follow.?up|closing|upsell|onboard` returned **only false
positives**, each verified in local context:

| Apparent hit | What it actually means |
|---|---|
| "contract" | the `DESIGN.md` **design-token contract** — a document format, never a legal instrument |
| "quote" | a **pull-quote / testimonial** UI element |
| "discovery call" | one occurrence, a **CTA button label** (`niche-and-vertical-design.md:95`), not process guidance |
| "client" | throughout means **the audience a website is designed for**, never a managed sales relationship |

Two items sat closest to the boundary and were deliberately **not** lifted; both calls are recorded
with reasoning so a writer can overturn them on inspection rather than by guess:

- **`persuasion-and-conversion.md:106–124`** (anchoring, decoy effect, charm pricing, three-tier
  psychology, center-stage effect). Reads like "pricing presentation" but is **self-serve
  pricing-*page*** content — a visitor reading tiers on a website, not a rep presenting a quote in a
  live deal. Already homed: `product-skill/.../business-model.md` teaches the identical mechanics.
  **This distinction is exactly the seam sales must draw in §C.4** — same word, two contexts.
- **`trust-proof-and-structure.md:93`** case-study anatomy — "multi-asset: a scannable web page +
  **a sales PDF one-pager** + a 60–90s video covers different buyer modes." The nearest thing to
  sales collateral in the corpus, but scoped to building the *web page*. A "how to use a case study
  inside a deal" angle is **new writing, not a lift**.

### A.2 — FLAG-TO-OTHER-PACK (~10 items, so nothing is lost on retirement)

| Destination | Item | Source |
|---|---|---|
| marketing | Premium↔information dial (governing framework: brand-presence vs proof-density, sequenced down-scroll) | `niche-and-vertical-design.md:1–27` |
| marketing | 10 vertical playbooks (architecture, law, SaaS, luxury, healthcare, real estate…) w/ audience, goal, structure, proof devices, register, pitfalls | `niche-and-vertical-design.md:60–196` |
| marketing | Brand-weight vs info-weight table across 10 verticals + each vertical's signature proof device | `niche-and-vertical-design.md:199–212` |
| marketing | Cialdini's 7 as page devices; bias→UX-device map; CCD + Attention Ratio; the color-psychology **myth-busting** section | `persuasion-and-conversion.md:1–124` (debunk at `:96–102`) |
| marketing | Mechanism / ethical-use / dark-pattern table citing FTC 2022 enforcement | `persuasion-and-conversion.md:126–139` |
| marketing | E-E-A-T as design, social-proof placement, IA conventions, case-study anatomy | `trust-proof-and-structure.md` (whole, 111 lines) |
| product | Anchoring-vs-decoy **distinction phrasing** ("anchoring sets a reference *number*, decoy adds a *dominated option*") — diff-check against business-model.md | `persuasion-and-conversion.md:106–124` |
| quality | Go/no-go gate: the "would a real user contact support over this?" P1 test; "any P0, or a P1 you can't immediately fix, is a NO-GO" | `design-critique.md:58,70–96` |
| design / frontend | Every technique file — see A.3, near-total supersession | (all) |

Nothing mapped to backend, ai, data, automation, operate, architecture, growth, or success.

### A.3 — SUPERSEDED (24 rows, near-total)

Every substantive file maps cleanly onto design-skill or frontend-skill — **which is the family's
own architecture decision, not a gap**: webdesign merged design+build into one skill; the family
split that scope into two peer packs. Representative rows (full 24-row table at
`_raw-e1-webdesign-lift.md` §4, with per-row confidence marks):

| webdesign | Superseded by | Confidence |
|---|---|---|
| `anti-default-catalog.md` | `design/references/visual-direction.md` ("canonical home of the anti-default catalog" — its own words) | verified (content) |
| `art-review.md` + `design-critique.md` | `design/references/critique.md` + `quality/references/release-gate-and-claims.md` | verified (content) |
| `layout-and-composition.md` / `typography.md` / `color-and-rhythm.md` | design's `layout-composition.md` / `typography.md` / `color.md` | verified (content) |
| `depth-and-texture.md` + `decoration.md` + `imagery.md` | `design/references/imagery-depth-decoration.md` | verified (content) |
| `niche-and-vertical-design.md` | `design/references/surface-website.md` (names "the premium↔information dial, per-vertical register") | verified (content) |
| `frontend-build-patterns.md` (473 lines) | frontend's `nextjs.md`, `css-craft.md`, `web-platform-css.md`, `js-dom-craft.md`, `design-handoff-and-tokens.md` | verified (content) |
| `tailwind-v4-theme.md` | `frontend/references/tailwind.md` (names "the container-token collision") | verified (content) |
| `persuasion-and-conversion.md §6` | `product/references/business-model.md` | verified (content) |

**Nothing was left without a home.** Retirement is safe once §A.2's flags are routed.

---

## §B — Verified seam table

**14 fixed line-cites checked: 12 exact, 2 drifted.** Full verbatim quotes in `_raw-e2-seam-audit.md`
Part 1. Corrected line numbers below are what the build must cite.

| Pack | Charter cite | **Actual** | Status |
|---|---|---|---|
| marketing | `handoff.md:42` | `:42` | exact |
| marketing | `SKILL.md:107` | `:107` | exact |
| marketing | `lifecycle-and-email.md:16` | `:16` | exact |
| marketing | `surface-b2b-sales-assisted.md:51,111` | `:51`, `:111` | exact |
| growth | `handoff.md:42` | `:42` | exact |
| growth | `SKILL.md:112` | `:112` | exact |
| growth | `surface-b2b-sales-assisted.md:143` | **`:144`** | **DRIFT +1** |
| success | `handoff.md:40` | `:40` | exact |
| success | `SKILL.md:101` | `:101` | exact |
| success | `renewals-and-expansion.md` §6 "~line 50" | **`:117`** (content `:119–124`) | **DRIFT ~+67** |
| product | `SKILL.md:27` | `:27` | exact |
| automation | `SKILL.md:104` | `:104` | exact |
| automation | `process-capture.md:15,163` | `:15`, `:163` | exact |

**The load-bearing quotes**, verbatim from disk:

- **marketing, the firmest cession in the family** (`surface-b2b-sales-assisted.md:51–53`): "Three
  adjacent disciplines belong to `sales`, not to this pack... **revenue operations, sales enablement
  (battlecards, objection handling, pricing negotiation guidance), and cold outbound/prospecting.**"
  Repeated identically at `handoff.md:42` and `SKILL.md:107`. **No hedge word appears anywhere near
  it.** Marketing even states *why*: "nearly every surveyed competitor pack folds prospecting and
  cold-email into 'marketing,' and the family's declared seam is a real differentiator only if it is
  drawn here explicitly, not assumed" (`:54–56`).
- **marketing's clearest CRM statement** (`:58`, lead-verified): "it does not run the outbound
  sequence or own the CRM pipeline stage."
- **growth** (`handoff.md:42`): "cold outbound, CRM stages, and deal mechanics stay `sales`'s
  **regardless of which funnel stage an experiment touches**." Row tagged `(provisional)`.
- **success** (`renewals-and-expansion.md:117`): "## 6. The sales seam — contested, not settled" —
  full §6 quoted in the raw.
- **product** (`SKILL.md:27`): "qualification and CRM to `sales`" — **the only unqualified,
  non-provisional cession to sales anywhere in the family.**

### B.1 — Eight binding cessions TO sales

marketing ×3 (the three named disciplines; not-the-CRM-pipeline-stage; CRM/pipeline sequencing
around an SQL) · growth ×2 (pipeline/CRM/outbound; the handoff itself — both *provisional*) ·
product ×1 (qualification + CRM — *firm*) · success ×1 (the expansion sale — *provisional AND
contested*) · automation ×1 (authoring business rules + customer-facing comms, shared four ways).

### B.2 — Marketing's `surface-b2b-sales-assisted.md` is a pre-drawn partial spec

Read in full (114 lines). Marketing's boundary is a **qualified handoff** — "a defined signal (fit +
intent) that a named account or contact is ready for a sales conversation, not a name added to a
list" (`:49–50`). It supplies "the qualified-demand definition and the assets sales pulls from (case
studies, competitive positioning)" (`:56–58`). Its 95-5 section and its attribution-honesty framing
are the doctrine sales inherits rather than restates. Growth ships a same-named file (146 lines)
that is nearly as load-bearing: it contains **the only B2B funnel-stage sequence written anywhere in
the family** — "MQL → SQL → opportunity → closed-won" (`growth/.../surface-b2b-sales-assisted.md:14`)
— and names bottom-of-funnel artifacts as sales's to author: "a demo script variant, a proposal
template, how a rep frames pricing on a call" (`:64–65`).

---

## §C — Reciprocal-row spec: what sales must ship

### C.0 — Which packs need a mirror row (lead-verified, closes W2's open gap)

W2 could not locate product's and automation's `handoff.md`; **both exist**, and I checked them:

```
grep -rln "`sales`" */skills/*/references/handoff.md
→ growth, marketing, success   (exactly three)
product/references/handoff.md    → NO sales mention
automation/references/handoff.md → NO sales mention
```

So: **sales writes three mirror rows** (marketing, growth, success). Product and automation cede in
prose/router tables only (`product/SKILL.md:27`, `automation/SKILL.md:104`), never as a handoff row.

**Sales does NOT need success's `## Three rows this file originates` device.** Success needed it
because no sibling reciprocated. Sales is the opposite case — all three relevant packs pre-drew rows
for it. Sales should instead note *once* that product's and automation's silence is deliberate, not
an oversight: automation named the gap explicitly and it self-resolves on ship.

### C.1 — The row format sales must match exactly

Identical four-column shape across all three packs:

```
| Sibling | What [pack] hands it | What [pack] consumes from it | The line [pack] does not cross |
```

Hedges are written in **two** places, never one: as a parenthetical in column 1 (`` `sales`
(provisional) ``, `` `sales` (unbuilt, provisional) ``) **and restated in prose opening column 4**.
Each hedging pack names the prior sibling's hedge, building a chain: marketing → growth → success.
Column 4 is always an explicit negative ("X does not own/run/set…"), usually citing the sibling's
own file where the cession was made.

### C.2 — The three rows, specified

**→ `marketing` — FIRM, no hedge.** Marketing's cession carries no hedge word; **mirroring it with a
hedge would weaken a seam marketing deliberately drew hard, and would be a defect.** Hands back:
pipeline and close-rate signal that feeds positioning and message iteration (marketing names exactly
this in its own row — match the term). Consumes: qualified demand, the fit-plus-intent signal on a
named account, plus the assets sales pulls from (case studies, competitive positioning). Line not
crossed: sales does not create or capture demand, does not own the ICP *definition* (see §D.1), and
**cites marketing's deliverability and consent doctrine, never restates it** (charter standing rule;
those are shipped strips).

**→ `growth` — PROVISIONAL, and preserve the *shape* of growth's hedge.** Growth hedges *whether the
line sits in the right place*, not *whether deal mechanics are sales's* — those are two different
hedges and **collapsing them into one misrepresents growth's position.** The row must keep
"regardless of which funnel stage an experiment touches" unconditional while marking the seam
provisional. Hands back: pipeline and qualification signal shaping which stage is worth testing.
Consumes: experiment readouts on sales-assisted funnel stages — noting growth explicitly declines to
extend a funnel-stage result's confidence into a deal-stage outcome it didn't test (`:110–112`).

**→ `success` — CONTESTED. Do not flatten.** This is the highest-risk row in the build. Success's
contested mark is not decoration: it is a **checked invariant** in success's own Validation section
("Renewal ownership on this surface states the sales clause as provisional, not settled",
`renewals-and-expansion.md:154`), reinforced in four places on disk, and cites two dated primary
sources (Lincoln Murphy, both Jan 13 2019). Sales's row must carry **both** positions — sales closes
the expansion sale in a sales-assisted motion, AND Murphy's complexity-gated CS-native position
(a CSM renews by default; only genuinely complex renewals route out, explicitly *not* "Account
Management carryover") — and must state that sales does not adjudicate the industry fight either.
**A sales pack that quietly resolves this in its own favour breaks a shipped sibling's invariant.**

---

## §D — Description-collision notes

Terms siblings already own, which sales's description and first-use prose must disambiguate:

| Term | Already claimed by | Sales must |
|---|---|---|
| **"discovery"** | product — an entire `references/discovery.md` for JTBD/user research | Use the full phrase **"discovery call"**, never bare "discovery". The exact phrase "discovery call" is **unclaimed family-wide** — sales can define it freely, but bare "discovery" collides hard. |
| **"pipeline"** | 340 hits — CI/CD, data, build pipelines across 7 packs | Always qualify: "deal pipeline" / "sales pipeline" on first use. |
| **"CRM"** | automation (`sync-semantics.md:206` — "the write path into an operational system of record") and data (reverse-ETL activation) | State the layer split explicitly: **automation owns sync/write-path mechanics; sales owns what stages and fields exist.** Different layers, same word. |
| **"expansion"** | product (`business-model.md:76` — a pricing lever), success (NRR metric + renewal conversation), growth (a retention experiment) | Three adjacent senses. Say which on first use: sales = the account-level commercial event it closes. |
| **"qualification"** | product/marketing cede it to sales; design (`journeys.md:39`) **rejects "Lead Qualification"** as internal jargon unfit for a customer-journey phase name | Free to own — but don't use it as user-facing vocabulary, which design already ruled against. |
| **"SQL"** | data/backend — 137 hits, Structured Query Language | Spell out "sales-qualified lead" on first use; growth's 2 hits are the only funnel-sense usage. |
| **"sales enablement"** | marketing cedes it explicitly (battlecards, objection handling) | Free. The feared "customer enablement" collision **does not exist on disk** — searched, not found. |

**Terms with ZERO family-wide usage — sales defines them from scratch, no collision risk:**
`AE`, `SDR`, `close rate`, `upsell`, `cross-sell`, `account executive`. Also: **no pack anywhere
mentions a sales rep's quota** (all 61 "quota" hits are API/resource quotas) and **no pack contains
any sales-commission content** (all "commission" hits are "de**commission**ing").

---

## §E — Contradictions and asymmetries — flagged, not smoothed

**E.1 — NO contradiction of the sales axis was found.** Every sibling touching sales's claimed
territory either cedes it explicitly or marks its own position provisional pending sales's arrival.
The charter's axis survives the disk audit intact.

**E.2 — Two adjacent-layer overlaps that need a stated boundary, not a fight.** Neither is a
contradiction, but both use a word sales also uses, so **silence would read as a collision**:
product owns pricing-tier *design and page psychology* while sales presents/negotiates price *inside
a live deal*; automation owns CRM *sync mechanics* while sales owns CRM *structure*.

**E.3 — LOUD: the dunning/billing assignment is unreciprocated.** `product` contains **zero
occurrences of "dunning" and zero of "billing"** — I re-verified this myself. Yet success
(`SKILL.md:99`) and marketing (`lifecycle-and-email.md:17`) both route dunning/billing-failure
recovery to product. **Two packs assign territory a third pack never claims.** Not sales's
territory either way, but if sales routes a deal that stalls on a failed payment, it should route to
`product` *per the two siblings' documented position* and must **not** claim product says so itself.
This extends a known family follow-up and is worth a family ruling.

**E.4 — The ICP boundary is the one genuinely underspecified seam.** Sales's mission claims "ICP +
account selection"; marketing ships "ICP as a funnel, not a checkbox"
(`audience-and-segmentation.md:65–103`, lead-verified) as *marketing's own segmentation model*.
These are almost certainly one funnel seen from two ends — but **no shipped file draws this line**.
Sales should state explicitly that it **inherits marketing's ICP definition and applies it to
account selection and prioritization**, rather than defining ICP from scratch. This is the single
place where the sales build is most likely to accidentally contradict a shipped pack.

**E.5 — Two placeholders that self-resolve on ship (no sibling edit needed).** Success's
`handoff.md:40` tags its row "(unbuilt, provisional)" and automation's `process-capture.md:15` says
the commercial upstreams "do not yet exist as shipped skills." Both were accurate when written; both
become true statements the moment sales ships. Automation's sentence is now **stale for product and
marketing** (both shipped) — an automation-side edit, not sales's problem.

---

## §F — Candidate never-ship figures (from the webdesign corpus)

Per the R21 rule, these are collected because a reader may **recognise-and-correct** them. All are
UNSOURCED in the retiring skill and would be defects if lifted. The first is directly relevant to
Channel A/B's falsification work:

| Figure | Source in webdesign | Grade | Note |
|---|---|---|---|
| "~9 in 10 pro-services buyers rule a firm out before contact; 8+ in 10 evaluate via the website first" | `niche-and-vertical-design.md:65–66` | **UNSOURCED** (industry marketing blogs only) | **A direct cousin of the charter's "57% of the buying decision happens before sales contact" strip.** Same claim genre, same rhetorical job. Whoever writes that strip should treat this as a second instance of the pattern, not an independent datum. |
| "credentials + social proof can lift conversion up to ~200%" | `niche-and-vertical-design.md:190` | UNSOURCED | no citation anywhere in the corpus |
| "three pricing tiers convert ~1.4× two tiers; 4+ convert worse" | `persuasion-and-conversion.md:117` | UNSOURCED | pricing-adjacent; do not lift |
| "CTA first-person copy beats second-person by 10–90%" | `persuasion-and-conversion.md:83` | UNSOURCED | suspiciously wide range |
| "Attention Ratio tightening toward 1:1 commonly lifts conversion ~31%" | `persuasion-and-conversion.md:54` | UNSOURCED | — |
| "75% of users judge credibility on website design alone" | `trust-proof-and-structure.md:10` | UNSOURCED | Stanford Web Credibility Project named but never linked |

**Correctly handled in the source (worth emulating, not never-shipping):** webdesign's own
color-psychology section self-flags as folklore — "universal color→emotion→purchase claims are
largely unsupported folklore... don't cite 'blue = trust, orange = buy' as fact"
(`persuasion-and-conversion.md:96–102`). Two figures in the corpus are genuinely PERMALINKED
(Lindgaard et al. 50ms; FTC 2022 dark-patterns report).

---

## §G — Coverage statement

**Searched:** all 22 webdesign files end-to-end; the 13 shipped packs by recursive keyword grep
across ~35 sales terms; full reads of marketing's and growth's `surface-b2b-sales-assisted.md`,
and marketing/growth/success `handoff.md`; all 13 packs' `handoff.md` checked for a sales row.
**Search surface was local disk only — no web queries were issued by this channel, so no finding
here is exposed to the WebSearch quota incident.**

**NOT searched:**
- Reference files in the 10 non-commercial packs were keyword-searched, **not read end-to-end**.
- Success's `renewals-and-expansion.md` §§2–5,7 and `surface-b2b-high-touch.md` read but not
  exhaustively quoted.
- `assets/`, `agents/`, and `evals/` directories were only spot-checked where a grep hit landed.
  **A full eval-case sweep for sales-adjacent routing cases was not performed** — worth doing before
  sales writes its own eval set, since growth's `evals/never-ship/cases.json` and
  `evals/stats-cases/cases.json` both surfaced on "win rate".
- No licensing verification was performed (Channel E ships **no licensing ledger rows** — that is
  Channels C/D's contract).
- **Line numbers are as-read on 2026-08-03.** Packs are live repos; two of fourteen cites had already
  drifted. Re-verify by `grep -n` on the verbatim quote before citing in shipped prose — the quotes
  will survive drift, the numbers will not.
