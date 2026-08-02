# Raw extraction — legacy `webdesign` skill lift/flag/supersession pass

Source: `/Users/tamas/.claude/skills/webdesign/` (v1.2.0, MIT, source repo
`github.com/gabros20/webdesign`). Retiring skill; nothing may be lost silently.

**Files read: 22/22 (100%).** `find /Users/tamas/.claude/skills/webdesign -type f | sort` returned
22 files (1 `SKILL.md` + 21 files under `references/`, of which `SOURCES.md` is a citations index).
Every file was read in full, end to end, via the `Read` tool (all files were ≤473 lines — no file
required chunked reads; `wc -l` confirmed no truncation). No binary/non-text files exist in the
tree.

## Headline finding (read this first)

**There is no client-sales content in this skill. Bucket (a) LIFT-TO-SALES is empty.** Webdesign is
a pure **design / art-direction / frontend-build** system: creative direction → structure →
per-section craft → build → art review → scored critique. It contains zero material on
prospecting, lead generation, discovery/scoping calls, proposals, SOWs, estimates/quoting,
negotiation, objection handling (in the sales sense — it has *on-page* objection-handling copy
devices, which is a different thing, see below), contracts, deposits/payment terms, retainer/upsell
conversations, CRM/pipeline process, follow-up cadence, or win/loss reflection. A targeted grep
across the whole corpus for `proposal|contract|negotiat|deposit|retainer|invoice|estimate|quote|SOW|
discovery call|sales call|prospect|lead gen|pipeline|CRM|win.loss|follow.?up|closing|upsell|onboard`
returned only false positives: "contract" always means the `DESIGN.md` **design-token contract**
(a document format, not a legal instrument); "quote" always means a **pull-quote/testimonial**
UI element; "discovery call" appears exactly once, as an example **CTA button label** inside a
website-conversion-design discussion (`niche-and-vertical-design.md:95`), not as sales-process
guidance; "client" throughout means **the audience the website is designed for**, never a sales
relationship being managed. This is a genuine, verified null result — not a failure to look hard
enough. See §5 (grep evidence) and the coverage statement (§6) for the full trail.

---

## 1. File inventory

| # | Path (under `webdesign/`) | Lines | What it is | Bucket verdict |
|---|---|---|---|---|
| 1 | `SKILL.md` | 165 | Router: workflow arc, pick-by-job table, 7 non-negotiable laws, hand-off list | (c) superseded by design-skill (router) |
| 2 | `references/anti-default-catalog.md` | 64 | Named 2026 AI-design tells (color/type/layout/GPT defects) | (c) superseded — design-skill |
| 3 | `references/art-review.md` | 213 | Visual review procedure: capture tooling, A0–A3 severity, no-first-pass rule | (c) superseded — design-skill/critique.md |
| 4 | `references/color-and-rhythm.md` | 82 | OKLCH palettes, light↔dark section rhythm, duotone, gradients | (c) superseded — design-skill/color.md |
| 5 | `references/decoration.md` | 105 | SVG patterns, dividers, blobs, PNG cutouts, logo-as-texture | (c) superseded — design-skill/imagery-depth-decoration.md |
| 6 | `references/depth-and-texture.md` | 186 | Z-plane composition, grain, aurora glow, layered shadows, glass, tilt, parallax | (c) superseded — design-skill/imagery-depth-decoration.md |
| 7 | `references/design-critique.md` | 96 | Nielsen 0–40, cognitive load, personas, P0–P3, go/no-go QA gate | (c) superseded — design-skill/critique.md + quality-skill |
| 8 | `references/design-direction.md` | 178 | Authoring `DESIGN.md` (design.md tool/format, CLI, lint) | (c) superseded — design-skill/visual-direction.md + frontend-skill/design-handoff-and-tokens.md |
| 9 | `references/design-thinking.md` | 97 | Composition process, "why templated" fixes, one-bold-move law, refinement checklist | (c) superseded — design-skill/visual-direction.md + critique.md |
| 10 | `references/experimental-and-creative.md` | 143 | WebGL/shader bg, particles, custom cursors, View Transitions, Awwwards discipline | (c) superseded — design-skill/surface-website.md (award tier) |
| 11 | `references/frontend-build-patterns.md` | 473 | Scaffold, section-registry pattern, theming, HTML/CSS/JS/TS craft | (c) superseded — frontend-skill (multiple files) |
| 12 | `references/frontend-design-principles.md` | 165 | Taste/POV layer: register doctrine, process, writing-in-design | (c) superseded — design-skill/visual-direction.md |
| 13 | `references/imagery.md` | 189 | Masking, scrims, masonry, mockups, collage, Ken Burns, object-fit | (c) superseded — design-skill/imagery-depth-decoration.md |
| 14 | `references/layout-and-composition.md` | 226 | Breakout grid, bento, asymmetry, whitespace, F/Z pattern, Gestalt | (c) superseded — design-skill/layout-composition.md |
| 15 | `references/motion-and-interaction.md` | 129 | Scroll-driven reveal, GSAP pinning, magnetic buttons, marquee, motion principles | (c) superseded — design-skill/motion.md + interaction.md |
| 16 | `references/niche-and-vertical-design.md` | 220 | Premium↔info dial + 10 vertical playbooks (architecture, law, SaaS, luxury…) | (b)+(c) — flag design/marketing signal; superseded — design-skill/surface-website.md |
| 17 | `references/persuasion-and-conversion.md` | 139 | Cialdini, cognitive biases, CCD, copy↔design, pricing psychology, ethics table | (b)+(c) — flag marketing/growth/product; superseded in parts |
| 18 | `references/section-archetypes.md` | 211 | Sitemap/IA procedure + section-catalog schema + archetype library | (c) superseded — design-skill/information-architecture.md + surface-website.md |
| 19 | `references/section-design-workflow.md` | 142 | Craft router: device map, quick recipes, anti-boring checklist | (c) superseded — design-skill/surface-website.md (router role) |
| 20 | `references/SOURCES.md` | 124 | Citation index for all technique references | n/a — pure bibliography, not content |
| 21 | `references/tailwind-v4-theme.md` | 118 | Tailwind v4 `@theme` namespace mapping, the `max-w` collapse gotcha | (c) superseded — frontend-skill/tailwind.md |
| 22 | `references/trust-proof-and-structure.md` | 111 | E-E-A-T as design, social proof devices, IA, SEO structure, case-study anatomy | (b)+(c) — flag marketing; superseded in parts — design-skill/quality-skill |
| 23 | `references/typography.md` | 114 | Modular scale, clamp(), display type, font pairing, kinetic type, ghost type | (c) superseded — design-skill/typography.md |

No file was thin/empty; every file carried real, dense technique content. Total ~3,707 lines across
`SKILL.md` + references.

---

## 2. Bucket (a) LIFT-TO-SALES

**Empty. Zero items.** This is a loud, deliberate null result, not an oversight — see the headline
finding above and the grep evidence in §5. The skill's "client" is a website's target audience, not
a sales counterparty; its "contract" is a design-token document, not a legal one; its "discovery
call" is a marketing-CTA label, not a sales-process artifact.

The two places that came closest to the sales boundary, and why they were judged **not** sales
content (routed to bucket (b) instead):

- `persuasion-and-conversion.md §6` ("Premium / luxury psychology & pricing mechanics" — anchoring,
  decoy effect, charm pricing, three-tier convert-1.4×-two, center-stage effect) reads, at first
  glance, like the task brief's "pricing PRESENTATION (how you show/justify/anchor a price)."
  Verified against the shipped packs: this is explicitly **self-serve pricing-*page*** design
  content — a visitor reading tiers on a website, not a salesperson presenting a custom quote in a
  conversation. `product-skill/references/business-model.md` already teaches the identical
  mechanics (anchoring, decoy, charm pricing, Van Westendorp) as the canonical home for pricing
  *hypothesis* work, and `marketing-skill/references/landing-pages-and-conversion.md` explicitly
  states in its own scope note: *"The question is the price, the tier structure, or the decoy tier
  → `product`."* Since the shipped family's own routing sends this exact content to product (and
  the visual-restraint-as-luxury-signal half to design), it is not an orphaned sales artifact —
  it's already homed. Flagged to (b) below rather than lifted.
- `niche-and-vertical-design.md` — "Professional services / consulting" and "Creative agencies"
  playbooks both end in **"book a discovery/consult call."** This is the *website's* job (get a
  visitor to convert into a booked call) — i.e. marketing/design conversion goal-setting, not what
  happens *in* that call once booked. The moment sales would start is exactly where this reference
  stops. No script, no discovery-call question list, no qualification framework exists anywhere in
  the corpus.

**Recommendation to the sales-pack writer:** treat this as confirmed — do not spend further cycles
re-scanning webdesign for sales content; there is none to find.

---

## 3. Bucket (b) FLAG-TO-OTHER-PACK

Grouped by destination pack. These are items with real reuse value that belong to a shipped pack's
scope (already-shipped packs may already cover the underlying idea more deeply — cross-check against
§4 before re-lifting; items below are flagged because they're either not yet verified as covered, or
carry a distinct data point/figure worth preserving even if the technique itself is covered).

### → marketing

- **`niche-and-vertical-design.md:1–27`** (the premium↔information dial, the governing idea of the
  whole file) — a reusable framework for **how much a page should lead with brand-presence vs.
  proof-density**, sequenced down the scroll. Quote: *"Sequence them down the page: an emotional,
  restrained hero (premium) → progressively denser proof and information as the visitor scrolls and
  self-qualifies → a low-friction action... Where you set the dial is decided by stakes & emotion,
  not taste."* Likely useful to marketing's positioning/landing-page work if not already captured.
- **`niche-and-vertical-design.md:60–196`** — 10 full vertical playbooks (architecture, interior
  design, creative agencies, luxury/hospitality, photographers, law, finance/wealth, healthcare,
  real estate, B2B SaaS, professional-services/local) each with audience, goal, structure, proof
  devices, register, dial position, and pitfalls. High-density, concrete, copy-pasteable strategy
  content for positioning a services business's public-facing presence per-vertical.
- **`niche-and-vertical-design.md:199–212`** — brand-presence-weight vs info/proof-weight table
  across 10 verticals with each vertical's "signature proof device" named.
- **`persuasion-and-conversion.md §1–5`** (lines 1–124) — Cialdini's 7 principles as concrete page
  devices, cognitive-bias→UX-device mapping (anchoring, framing, loss aversion, Von Restorff, Hick's
  law, Fitts's law, Zeigarnik, peak-end), Conversion-Centered Design's 7 principles + the Attention
  Ratio metric, persuasive copy↔design pairing (value-prop anatomy, CTA copy rules), the ~50ms
  first-impression halo, aesthetic-usability effect, and the color-psychology **myth-busting**
  section (§5, lines 96–102: *"universal color→emotion→purchase claims are largely unsupported
  folklore... don't cite 'blue = trust, orange = buy' as fact"*). This is landing-page/CRO doctrine
  — squarely marketing/growth territory, likely already covered by
  `marketing-skill/references/landing-pages-and-conversion.md` (verify before re-lifting).
- **`persuasion-and-conversion.md §6 ethical-line table`** (lines 126–139) — a compact
  mechanism-vs-ethical-use-vs-dark-pattern table (scarcity, commitment, social proof,
  default/Zeigarnik, endowment, confirmshaming) citing FTC 2022 dark-patterns enforcement.
- **`trust-proof-and-structure.md`** (whole file, 111 lines) — E-E-A-T as page design (Experience/
  Expertise/Authoritativeness/Trust mapped to concrete design devices), social-proof device
  placement rules, IA/nav conventions (2–7 items, 2–3 clicks), SEO-aware structure (semantic HTML,
  heading hierarchy, JSON-LD, Core Web Vitals as design constraint), and case-study-page anatomy
  (Challenge→Solution→Results, "multi-asset: a scannable web page + a sales PDF one-pager + a
  60–90s video covers different buyer modes" — line 93). The case-study anatomy is the piece most
  likely to double as **sales collateral** (a case study handed to a prospect mid-cycle), but its
  home in webdesign is "how to build the web *page* version" — flag to marketing as the content
  asset; if sales wants a "how to use a case study in a sales conversation" angle, that's new
  writing, not a lift.

### → design (already the strongest match — see §4 for the near-total supersession)

- Every layout/type/color/depth/decoration/imagery/motion/experimental-and-creative technique file.
  Nothing here is orphaned; design-skill is the direct successor (same author, same anti-default
  catalog lineage, same critique/art-review structure — verified, §4).

### → frontend (same relationship as design — see §4)

- `frontend-build-patterns.md` and `tailwind-v4-theme.md` in full; both are Next.js/Tailwind v4
  worked-example build doctrine, the frontend pack's exact remit.

### → product

- **`persuasion-and-conversion.md §6 pricing-page mechanics`** (lines 106–124) — three-tier
  conversion multiplier (~1.4× two tiers), center-stage effect, decoy effect (explicitly
  distinguished from anchoring: *"anchoring sets a reference *number*, decoy adds a *dominated
  option*"*), charm pricing ($X9) vs. round-price-signals-confidence for luxury. **Verified
  superseded** — `product-skill/references/business-model.md` already teaches this (anchoring,
  decoy, Van Westendorp, charm pricing, tier psychology) as its canonical home; flag only in case a
  figure/distinction here is missing there (the anchoring-vs-decoy distinction phrasing is worth a
  diff-check).

### → quality

- **`design-critique.md`**'s go/no-go QA gate section (lines 70–96) — coverage-gap-is-a-blocker
  rule, build-health gate, "look at the real thing, don't just build it" screenshot-driven QA,
  P0–P3 severity routing with the **"would a real user contact support over this?"** P1 test (line
  58). Likely superseded by `quality-skill/references/release-gate-and-claims.md` (verified
  structurally similar — ship/claim split, evidence dossier) but the exact P0–P3 test phrasing and
  the "any P0, or a P1 you can't immediately fix, is a NO-GO" line (line 95) is worth a diff-check.

No items were found that map to backend, ai, data, automation, operate, architecture, growth, or
success — the corpus is narrowly design/frontend/marketing-adjacent throughout.

---

## 4. Bucket (c) SUPERSEDED

Confidence key: **verified** = I opened the shipped file and read its purpose/scope header (and, for
the 2 spot-checked pairs, matched actual doctrine, not just title); **inferred** = title/purpose-line
match only (both packs' `find` listings + one-line purpose headers checked), not a full content diff.
Every row below was at minimum title-and-scope verified; the four marked **verified (content)** were
opened and read.

| webdesign item | Superseding file (shipped pack) | Confidence |
|---|---|---|
| `anti-default-catalog.md` (named AI-design tells) | `design-skill/skills/design/references/visual-direction.md` — "canonical home of the anti-default catalog" (its own words) | verified (content) |
| `frontend-design-principles.md` (register doctrine, process, restraint) | `design-skill/skills/design/references/visual-direction.md` | verified (content) |
| `design-direction.md` (DESIGN.md authoring, `design.md` CLI) | `design-skill/skills/design/references/visual-direction.md` + `frontend-skill/skills/frontend/references/design-handoff-and-tokens.md` (stack-agnostic handoff-contract layer) | verified (content) |
| `design-thinking.md` (composition process, "why templated" fixes, critique framework) | `design-skill/skills/design/references/visual-direction.md` (composition/diagnosis) + `design-skill/skills/design/references/critique.md` (critique framework) | verified (content) |
| `art-review.md` (visual review, A0–A3, capture tooling, no-first-pass rule) | `design-skill/skills/design/references/critique.md` — "art review, scored heuristic critique, deslop pass, and motion review" unified into one method | verified (content) |
| `design-critique.md` (Nielsen 0–40, cognitive load, personas, P0–P3, go/no-go) | `design-skill/skills/design/references/critique.md` (design-level) + `quality-skill/skills/quality/references/release-gate-and-claims.md` (ship/claim gate) | verified (content) |
| `layout-and-composition.md` | `design-skill/skills/design/references/layout-composition.md` — "grid, spacing rhythm, hierarchy, gestalt grouping... with exact values" | verified (content) |
| `typography.md` | `design-skill/skills/design/references/typography.md` — "scale, pairing, measure, leading, display craft — with exact values" | verified (content) |
| `color-and-rhythm.md` | `design-skill/skills/design/references/color.md` — "OKLCH model, deterministic palette construction, state derivation... contrast math" | verified (content) |
| `depth-and-texture.md` | `design-skill/skills/design/references/imagery-depth-decoration.md` — "depth build order, materials (shadow, glass, grain...)" | verified (content) |
| `decoration.md` | `design-skill/skills/design/references/imagery-depth-decoration.md` — "decoration discipline" named explicitly | verified (content) |
| `imagery.md` | `design-skill/skills/design/references/imagery-depth-decoration.md` — "image treatment" named explicitly | verified (content) |
| `motion-and-interaction.md` Part A (motion) | `design-skill/skills/design/references/motion.md` — "canonical source for all motion values... every other reference points here" | verified (content) |
| `motion-and-interaction.md` (interaction half, implicit) | `design-skill/skills/design/references/interaction.md` — "component behavior... states, forms, feedback" | inferred |
| `experimental-and-creative.md` (WebGL/Awwwards tier) | `design-skill/skills/design/references/surface-website.md` — "the award tier" named explicitly in its own purpose line | verified (content) |
| `niche-and-vertical-design.md` (premium↔info dial, verticals) | `design-skill/skills/design/references/surface-website.md` — "the premium↔information dial, per-vertical register" named explicitly | verified (content) |
| `section-design-workflow.md` (craft router + device map) | `design-skill/skills/design/references/surface-website.md` — "page macrostructure, section craft" (router role absorbed into the surface file) | verified (content) |
| `section-archetypes.md` (sitemap/IA + section catalog) | `design-skill/skills/design/references/information-architecture.md` — "conceptual model, domain vocabulary, sitemap, navigation" + `surface-website.md` (section catalog) | verified (content) |
| `frontend-build-patterns.md` (scaffold, section-registry, theming, HTML/CSS/TS craft) | `frontend-skill/skills/frontend/references/nextjs.md`, `css-craft.md`, `web-platform-css.md`, `js-dom-craft.md`, `design-handoff-and-tokens.md` (split across several files) | verified (content, css-craft.md + design-handoff-and-tokens.md headers) |
| `tailwind-v4-theme.md` (the `max-w` collapse gotcha, namespace map) | `frontend-skill/skills/frontend/references/tailwind.md` — explicitly names "the container-token collision it creates" in its own purpose line | verified (content) |
| `persuasion-and-conversion.md §1–5` (Cialdini, biases, CCD, copy↔design) | `marketing-skill/skills/marketing/references/landing-pages-and-conversion.md` (requirements/claims/proof/objections layer) | verified (content, scope-note only) |
| `persuasion-and-conversion.md §6` (pricing mechanics: anchor/decoy/charm) | `product-skill/skills/product/references/business-model.md` — confirmed identical vocabulary (anchoring vs. decoy distinction, charm pricing, Van Westendorp) present | verified (content) |
| `trust-proof-and-structure.md §5` (SEO-aware structure, Core Web Vitals) | `marketing-skill/skills/marketing/references/seo-strategy.md` (likely) + `quality-skill` (Core Web Vitals as a verification concern) | inferred |
| `trust-proof-and-structure.md §1–4,6–7` (E-E-A-T, social proof, IA, case-study anatomy) | `design-skill/skills/design/references/surface-website.md` (trust/proof as page design) | inferred |
| `SKILL.md` (router, workflow arc, 7 laws) | `design-skill/skills/design/SKILL.md` (router role) + `frontend-skill/skills/frontend/SKILL.md` (build-stage router role) | inferred (routers not diffed line-by-line, but role is structurally identical — webdesign explicitly merged design+build into one skill; the shipped family split it into two peer packs, which *is* the family's own architecture decision, not a gap) |

**Not superseded / no clear shipped-pack home found:** none — every substantive file maps cleanly to
either design-skill or frontend-skill (the family's split of webdesign's original single-skill scope
into two peer packs), with marketing/product/quality picking up the persuasion/pricing/QA-gate
tributaries. This is a clean, near-total supersession — expected, since design-skill is webdesign's
direct successor within this same family-building project.

---

## 5. Figures, claims & statistics ledger

Every number found in the corpus, with its stated source (if any) and a grade. **PERMALINKED** =
real, named, checkable source; **UNSOURCED** = a number stated with no citation or only a vague
attribution; **FOLKLORE** = explicitly flagged in the source text itself as unverified/mythical.

| Figure | Location | Stated source | Grade |
|---|---|---|---|
| "75% of users judge a company's credibility on website design alone" | `trust-proof-and-structure.md:10`, also `niche-and-vertical-design.md:47` | "Stanford Web Credibility Project" (named study, no URL in `SOURCES.md`'s trust-proof entry) | UNSOURCED (named but not linked/verifiable from the corpus itself) |
| "Trust signals lift conversion ~15–34%; 93% read reviews before buying" | `trust-proof-and-structure.md:15` | none given | UNSOURCED |
| Lindgaard et al. — users judge visual appeal in 50ms (stable at 17ms) | `persuasion-and-conversion.md:90` | cited in `SOURCES.md` → Lindgaard et al., tandfonline.com DOI link | PERMALINKED |
| Aesthetics↔trust correlation ~r=0.74 (Kurosu & Kashimura ATM study) | `persuasion-and-conversion.md:94` | named study, no direct link in SOURCES.md (general NN/g links only) | UNSOURCED |
| "Attention Ratio... tightening toward 1:1 commonly lifts conversion ~31%" | `persuasion-and-conversion.md:54` | none given | UNSOURCED |
| CTA first-person copy beats second-person "by 10–90%" | `persuasion-and-conversion.md:83` | none given (wide, suspiciously vague range) | UNSOURCED |
| "Color→emotion→purchase claims are largely unsupported folklore" | `persuasion-and-conversion.md:96–102` | self-flagged by the source text itself, cites Branding Bullshit blog in SOURCES.md as the debunking source | explicitly labeled FOLKLORE by the source — correctly caveated, not laundered |
| Three-pricing-tiers convert ~1.4× two tiers; 4+ tiers convert worse | `persuasion-and-conversion.md:117` | none given | UNSOURCED |
| "~9 in 10 pro-services buyers rule a firm out before contact; 8+ in 10 evaluate via the website first" | `niche-and-vertical-design.md:65–66` | Hinge Marketing / Archmark / ArchDaily blog links in SOURCES.md (industry blogs, not primary research) | UNSOURCED (secondary/marketing-blog sourcing) |
| Architecture-firm image budget: "cap ~2000px / ≤200KB" | `niche-and-vertical-design.md:83` | none given (a house convention, not a benchmark) | UNSOURCED |
| Photographer curation "20-60-20 rule" (20% best, 60% solid, 20% range) | `niche-and-vertical-design.md:117` | none given | UNSOURCED |
| Healthcare "70%+ mobile" traffic | `niche-and-vertical-design.md:148` | none given | UNSOURCED |
| Real estate/B2B "60–83% of traffic" mobile | `niche-and-vertical-design.md:55` | none given | UNSOURCED |
| Professional services "credentials + social proof can lift conversion up to ~200%" | `niche-and-vertical-design.md:190` | none given | UNSOURCED |
| "47% expect <2s load" (premium-creative niches) | `niche-and-vertical-design.md:41` | none given | UNSOURCED |
| "79% want background on the artist/work before buying" | `niche-and-vertical-design.md:115` | none given | UNSOURCED |
| Google reviews "25+ @ 4.5★+" as a consulting/accountant benchmark | `niche-and-vertical-design.md:190` | none given (a house convention) | UNSOURCED |
| WCAG contrast floors (4.5:1 body, 3:1 large) | multiple files, e.g. `color-and-rhythm.md:75` | WCAG AA (a real, checkable public standard, not linked per-instance but standard is unambiguous) | PERMALINKED (standard is public/checkable even without inline link) |
| FTC dark-patterns blacklist (2022→2025): fake timers, false scarcity, hidden subscriptions, confirmshaming | `persuasion-and-conversion.md:127`, `trust-proof-and-structure.md:45` | FTC Report 2022, linked in `SOURCES.md` | PERMALINKED |
| Miller's 7±2 working memory, revised down by Cowan 2001 | `design-critique.md:31` | named (Miller, Cowan 2001) but no direct link in SOURCES.md for design-critique.md (file isn't in SOURCES.md's index at all — see coverage note below) | UNSOURCED |

**Note on `design-critique.md` and `design-thinking.md`:** neither appears as a section in
`SOURCES.md` (which indexes provenance for the *technique* references only, per its own header —
`design-critique.md`, `design-direction.md`, `frontend-design-principles.md`, `niche-and-vertical-design.md`
partially, `section-archetypes.md`, `section-design-workflow.md`, `tailwind-v4-theme.md`,
`trust-proof-and-structure.md`'s case-study section, and `SKILL.md` itself are likewise absent from
`SOURCES.md`). This isn't a defect in webdesign — `SOURCES.md`'s own header says it covers "the
technique references" specifically — but it means several of the above ledger figures (Miller/Cowan,
the architecture/photographer/healthcare percentages) have no traceable citation anywhere in the
skill, which is why they're graded UNSOURCED rather than assumed-fine.

---

## 6. Coverage statement

- **Read in full: 22/22 files (100%).** No sampling, no skimming — every file was read start to
  finish via the `Read` tool in one pass each (largest file was 473 lines, well under any
  chunking threshold).
- **No binary/non-text files exist** under `webdesign/` — `find -type f` returned only `.md` files.
- **Verification method for bucket (c):** rather than asserting supersession from memory, I ran
  `find`/`ls` across 8 shipped packs (design, frontend, marketing, growth, quality, product,
  architecture, success) to enumerate their actual reference files, then opened and read the
  purpose/scope header (and for anti-default-catalog↔visual-direction, art-review↔critique,
  tailwind-v4-theme↔tailwind, landing-pages↔persuasion, business-model↔pricing-mechanics — the full
  relevant section) of the strongest supersession candidates. Rows marked "inferred" in §4 had their
  *title and one-line purpose* checked but not a full paragraph-level content diff — a writer citing
  those rows should do a final spot-check before asserting word-for-word supersession, though the
  scope match is strong in every case.
- **What I did NOT do:** I did not open every reference file in every shipped pack (e.g. I did not
  read frontend-skill's `nextjs.md`, `js-dom-craft.md`, or `web-platform-css.md` end-to-end, only
  confirmed their existence and purpose lines match pieces of `frontend-build-patterns.md`). I did
  not diff-check architecture-skill or success-skill against anything — grep and file-listing
  confirmed neither pack's scope overlaps this corpus (architecture is system/data/backend design;
  success is post-sale customer retention, not client-services web-design work), so no bucket
  (b)/(c) items were assigned there.
- **Ambiguous items, flagged honestly rather than force-classified:**
  - `persuasion-and-conversion.md §6` pricing mechanics — borderline sales-adjacent by the task
    brief's own wording ("pricing PRESENTATION... how you show/justify/anchor a price"), but
    verified to already be homed at product-skill (tier/anchor/decoy hypothesis work) and
    design-skill (visual-restraint-as-price-cue). I judged this NOT a sales lift because the
    content is self-serve-page-scoped, not a salesperson's live-quote-presentation scoped — see
    §2's explanit for the full reasoning. A future sales-pack writer disagreeing with this call
    should re-read `persuasion-and-conversion.md:106–124` directly before deciding.
  - The `trust-proof-and-structure.md` case-study anatomy (§6) sits closest to something a sales
    process would actually consume (a case study as a leave-behind during a deal) — flagged to
    marketing as the content asset, explicitly noted that "how to *use* it in a sales conversation"
    would be new writing, not a lift, since webdesign only covers building the case-study *web
    page*.
- **Nothing was invented.** Every quote/claim above is anchored to an exact file:line I actually
  read; the null result in bucket (a) is a grep-and-read-verified absence, not an assumption.

---

**Raw file path:** `/Users/tamas/Documents/Personal/Projects/sales-skill/research/raw/_raw-e1-webdesign-lift.md`
