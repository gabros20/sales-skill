# Raw research — C0c (channel lead) — a 23.6k★ MIT incumbent that OCCUPIES our forecasting flagship

Author: Channel C lead. Date: 2026-08-03. **Priority: HIGH — this may change the pack's wedge.**

## How this was found (and why it was nearly missed)

C4 declared a coverage gap: `ghrelay code` (grep.app) returned `SOURCE_DOWN` when it tried the
code-token lane, so GitHub's larger code corpus was never searched for `pipeline_coverage` and
similar tokens. C4 was explicit that this was "a real coverage gap in part (a), not a swept
null," and recommended retrying once grep.app was confirmed up.

I retried. `ghrelay doctor` showed grep.app reachable with the breaker past its cooldown, and
the very first probe — `ghrelay code "pipeline_coverage"` — returned a hit that **falsifies C4's
headline landscape finding** and surfaces a major incumbent nobody in this channel had seen.

This is worth recording as a process lesson: C4's null ("GitHub has no established open-source
sales-math calculator") was honestly caveated, and the caveat was load-bearing. One retry of the
declared-missing lane overturned the headline.

## The repo

`alirezarezvani/claude-skills` — https://github.com/alirezarezvani/claude-skills

- **23,656 stars**, MIT (API-reported `MIT`; see licence caveat below), not archived,
  `pushed_at` 2026-07-17.
- Self-described: *"345 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custom
  commands, 330+ skills…) for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents —
  engineering, marketing, product, compliance, C-level advisory, research, business operations,
  commercial & finance, and your daily productivity skills."*
- **Star-skepticism check passed — this is not an inflated repo.** `ghrelay health`:
  coverage **7/7**, **flags: [] (none)** — no `star-burst`, no `possible-fake-stars`, no
  `ratio-anomaly`. Subscores C 0.56, D 0.59, **F 0.82** (popularity-validity high). The stars
  survive the family's standing star-skepticism rule. Treat this as a genuinely popular artifact.

Against the charter's expectation — "Success's research already spotted GTM-adjacent packs at
~360★ — this niche may be MORE contested than CS was" — this is **~65× larger than the largest
GTM-adjacent pack the family had previously found.** The charter's instinct was right and
understated.

## THE PROBLEM: `commercial-forecaster` occupies our flagship candidate

Path: `commercial/skills/commercial-forecaster/SKILL.md` (12,216 bytes, version 2.8.0,
`license: MIT` in its own frontmatter), with `assets/`, `references/`, and runnable `scripts/`.
Raw: https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/commercial-forecaster/SKILL.md

Its own description, verbatim:

> *"Use when building a quarterly bookings forecast, ARR projection, pipeline forecast, NRR
> projection, or commit/best-case/pipe-only board number — especially when the CRO needs to walk
> the board through funnel math + cohort ARR + per-stage conversion assumptions **without the
> theatre of a single undefended number**. … **Every output explicitly names the conversion rate
> used, the data window, and the weighting choice.**"*

And from the body:

> *"The skill recommends **three forecast numbers + an explicit assumption block**. The CRO
> presents the number, the board sees the assumptions, the theatre dies."*
> *"**The assumption block is non-optional.** If you remove it, the forecast becomes theatre."*

**This is, almost word for word, the forecasting-honesty flagship this channel was preparing to
recommend.** Three-tier commit/best-case/pipe-only, disclosed conversion rate, named data window,
explicit weighting choice, refusal of the single undefended number. It even ships the runnable
artifact — `scripts/bookings_forecaster.py`, whose `ForecastResult` dataclass carries
`commit`, `best_case`, `pipe_only`, `pipeline_coverage_ratio`, `pipeline_risk_pct` (the last
defined in-code as *"variance between commit and pipe-only"*), with a stated last-4Q vs last-12Q
**70/30** weighting.

Grade: **PRIMARY, verbatim, permalinked.** Any claim that our pack's forecast-honesty angle is
novel is now **false**, and would ship as a defect if asserted.

### What it does NOT do — where honest room remains

Two gaps I can state from what I read, and they are narrower than I'd like:

1. **It still publishes no accuracy measurement.** The skill structures and discloses the
   forecast; nothing in the SKILL.md I read claims or measures whether the resulting number was
   right. The corpus-wide null (see below) survives this incumbent intact.
2. **It is pitched at CRO/RevOps/board scale** — "for Head of Commercial, RevOps, VP Sales, and
   CRO at quarterly forecast or board prep," requiring a ≈20-minute intake of 12 quarters of
   stage-conversion history and per-cohort retention data. The family's default reader is a
   **solo builder** who has neither 12 quarters of history nor a board. The existence-gate
   question — *does a forecast mean anything at your volume?* — is untouched by this skill.

Those are real but narrow. Do not overstate them into "the flagship is still open."

## THE OPPORTUNITY: grep-verified, the buying conversation is completely absent

I enumerated **every** `SKILL.md` in the repo (excluding the mirrored `.gemini/`, `.codex/`,
`.claude/`, `.hermes/`, `.vibe/` copies) — **346 unique skill names** — and grepped that list for
the vocabulary of our pack's Includes list.

Sales-adjacent skills that DO exist:
- `commercial/`: **channel-economics, commercial-forecaster, commercial-policy, deal-desk,
  partnerships-architect, pricing-strategist, rfp-responder**
- `business-growth/`: **contract-and-proposal-writer, customer-success-manager,
  revenue-operations, sales-engineer**
- `c-level-advisor/`: **cro-advisor, competitive-intel** (plus ~35 other C-suite advisory skills)

Grep across all 346 names for `discovery|qualif|meddic|bant|objection|demo|icp|win-loss|crm|
stage|prospect|cold|outbound|negotiat|close|territor|quota` returned exactly **three** hits, and
**all three belong to other disciplines** (paths verified):

| Hit | Actual path | Whose? |
|---|---|---|
| `cold-email` | `marketing-skill/skills/cold-email/SKILL.md` | **marketing's** |
| `demo-video` | `engineering/demo-video/skills/demo-video/SKILL.md` | engineering (video production, not demo narrative) |
| `product-discovery` | `product-team/skills/product-discovery/SKILL.md` | product (not sales discovery calls) |

**Grep-verified absent from all 346 skills:** qualification frameworks (no MEDDIC/BANT/MEDDPICC),
discovery calls, demo strategy/narrative, objection handling, sales stages and exit criteria,
CRM structure, pipeline hygiene, ICP/account selection, win/loss learning, negotiation,
territory, quota design, and both handoffs.

**So the largest incumbent in the ecosystem covers the RevOps/commercial-finance end of sales
thoroughly — forecast, deal desk, pricing, proposals/RFP, partnerships, channel economics — plus
a C-suite advisory layer, and has ZERO coverage of the buying conversation or the deal system.**

**SCOPE LIMIT — this is a coverage map of ONE repo, not a uniqueness proof.** Channel A's census
independently found other occupants of exactly this ground (a 9-skill Apache-2.0 Anthropic/KWP
sales pack; `awesome-copilot` reproducing MEDDICC letter-by-letter) and recorded the matching
self-correction: *"deep-read of N repos is not a uniqueness proof."* So the honest statement is
"absent from the largest repo's 346 skills," never "absent from the ecosystem." Whether the
buying conversation is genuinely open is Channel A's call, and A's current verdict is that
novelty is NOT available.

## BONUS: independent corroboration of marketing's BINDING seam claim

The charter carries marketing's shipped, flat-and-firm handoff position: cold outbound and
prospecting are **sales's**, and *"the incumbent genre routinely blends these into marketing;
this pack does not."*

The largest incumbent in the ecosystem files `cold-email` under **`marketing-skill/`**. That is
exactly the blending marketing's pack claimed the genre does. A shipped seam contract just
received independent empirical support from the biggest available sample. Worth telling the
marketing-seam owner; it strengthens a claim that was previously asserted from the pack's own
side only.

## LICENCE — RESOLVED (was provisional). Read at a pinned SHA, every file enumerated.

Pinned SHA `aa8d778811a557a2c28ccadda4cf3d0bd028a4cc`. Full recursive tree filtered for
`LICEN[SC]E|COPYING|NOTICE` → **six licence files**, not one. All six read:

| Path | Licence | Copyright holder |
|---|---|---|
| `LICENSE` (root) | MIT | **Alireza Rezvani**, 2025 |
| `engineering-team/playwright-pro/LICENSE` | MIT | Reza Rezvani, 2026 |
| `engineering-team/self-improving-agent/LICENSE` | MIT | Reza Rezvani, 2026 |
| `engineering/collab-proof/LICENSE` | MIT | **dong7812**, 2026 |
| `engineering/skillopt-sleep/LICENSE` | MIT | **Microsoft Corporation**, 2026 |
| `loop-library/LICENSE` | MIT | **Forward Future**, 2026 |

(Two further matches — `dependency-auditor/references/license_compatibility_matrix.md` and
`scripts/license_checker.py` — are *content about* licensing, not licence grants. Excluded.)

**This independently replicates Channel A's 8th-clause candidate exactly**: six MIT files, five
distinct copyright holders including Microsoft. Two channels reached it separately, so
*identical SPDX ≠ single owner* should be treated as confirmed rather than proposed.

**Verdict for our purposes — narrower and more useful than "the repo is MIT":**

- The root `LICENSE` **is** a real MIT grant, present and readable, in Alireza Rezvani's name.
- **`commercial/` carries no licence file of its own**, so `commercial-forecaster` falls under
  the root grant on its face, corroborated by its own frontmatter `license: MIT`. Nothing
  contradicts an MIT reading of that specific skill.
- **But the repo demonstrably aggregates third-party work** under other parties' copyright —
  Microsoft's among them. That is proof, not suspicion, that the root grant does **not**
  uniformly speak for everything beneath it. So the licence file establishes the *terms* while
  saying nothing about *provenance*: whether the commercial skills are Rezvani's to license is
  not answerable from the licence tree, and Channel A's finding that this repo attributes a
  30-cell stage table to "KeyBanc/OpenView/Bessemer" with no link is a live reason to doubt that
  everything in it originated there.

**Practical ruling:** citing and describing this repo is unproblematic. **Adapting** anything
from it requires per-directory checking, because a root MIT in one person's name sitting above
Microsoft-copyrighted subdirectories is exactly the pattern that makes blanket reliance unsafe.

## What this changes

1. **The forecasting flagship is CONTESTED, not open.** Recommend the pack does not claim
   novelty on forecast-honesty framing. Either differentiate hard (solo-scale existence gate;
   accuracy that nobody measures) or move the flagship.
2. **A grep-verified coverage map, offered to the census — not a wedge on its own**: the buying
   conversation and the deal system are absent from all 346 skills of the largest repo, while the
   RevOps/finance end is well covered. Must be combined with Channel A's census before anyone
   states a wedge (see SCOPE LIMIT above).
2b. **Probable cross-channel duplicate exhibit**: A found this repo attributing a 30-cell stage
   table to "KeyBanc/OpenView/Bessemer" with no link and executing it as Python priors; C found
   `bookings_forecaster.py` with a stated 70/30 last-4Q/last-12Q weighting and per-stage
   conversion assumptions. Likely the same artifact from two angles — an uncitable figure
   compiled into running code. Worth merging into one jointly-owned exhibit.
3. **C4's part-(a) headline needs correcting**: "GitHub has no established open-source sales-math
   calculator" is false as stated. `scripts/bookings_forecaster.py` inside a 23.6k★ MIT repo is
   exactly that, and it was missed only because grep.app was down during C4's window.
4. **Channel A (incumbent census) must see this immediately** — it is their territory and this is
   almost certainly the largest single incumbent in the census.
