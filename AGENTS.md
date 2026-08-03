# Agent guide — `sales` (Sales)

This repository is the released `sales-skill`: an installable agent skill for winning the deal and
being honest about whether the win can actually be predicted. The runtime skill lives under
`skills/sales/`; the repository and Codex plugin use the `-skill` suffix. Read this before editing.

## Ownership boundary (non-negotiable)

`sales` owns the buying conversation and the deal system — whether an assisted sales motion should
exist at all, account selection and qualification, cold outbound and AI-outbound policy, discovery
calls, demos, objection handling and enablement, proposal/pricing presentation and negotiation, CRM
structure and deal-pipeline hygiene, forecasting, win/loss learning, and the expansion-sale close.
It writes gates, playbooks, policies, pipeline structures, forecasts, and handoffs — **no
production code**, no experiments, and no number it cannot source. It does **not** own:

- demand creation, positioning, content, lifecycle email, deliverability and consent doctrine, or
  the competitive assets sales pulls from → **marketing** (marketing cedes cold outbound, sales
  enablement, and revenue operations to sales explicitly, with no hedge, but owns qualified-demand
  definition, ICP, and the assets sales consumes)
- funnel experiments, including on a sales-assisted funnel stage → **growth** (growth hedges
  *where* the funnel/deal line sits, never *whether* deal mechanics are sales's, regardless of
  which funnel stage an experiment touches)
- the renewal workflow and NRR reading → **success**, **contested, not settled** (sales closes the
  expansion sale in a sales-assisted motion; success's position holds a CSM renews by default and
  only genuinely complex renewals route out; neither pack adjudicates the fight — see
  `handoff.md`)
- pricing-tier design, the commercial-lifecycle model, dunning/billing-failure recovery, and
  pricing-*page* visitor psychology → **product** (product designs and models the price, including
  how a visitor reads tiers on a page; sales presents and negotiates a number inside a live deal —
  same mechanisms, different context, stated which on first use)
- agent mechanics, retrieval, prompts, and eval instrumentation behind an AI-SDR or sales
  assistant → **ai** (sales sets the AI-outbound disclosure policy and the false-engagement-signal
  rule; ai measures compliance with them)
- CRM sync, write-path mechanics, and workflow automation → **automation** (sales owns which
  stages and fields exist; automation owns how they get written and kept in sync)
- implementing any of it in production code → **frontend** / **backend** / **ai**

`sales` consumes upstream artifacts (marketing's qualified-demand definition and ICP, product's
pricing tiers) when they exist, works standalone when they don't, recommends siblings for work it
doesn't own, and never silently invokes them.

## Non-negotiable invariants

1. **Run the Existence Gate before building the apparatus.** Outbound infrastructure, a CRM, or a
   forecast requested before the gate is answered gets the gate first, and a named sibling pack for
   the meantime — never a silently invented artifact.
2. **A win rate without its denominator is not a number.** Coverage is 1/win-rate, derived, never
   shipped as a portable constant like "3x."
3. **Any bare percentage carries its subject inline** — this pack's own research holds three
   different subjects behind one bare "70%."
4. **Grade every figure inline** — primary > practitioner-report > vendor-claim — and carry the
   method with the number, or say "method unknown." Vendor AI-SDR claims are
   VENDOR-SELF-REPORTED and never cited without the method-absence statement attached.
5. **A disclaimed figure is still a figure.** In working prose, never name a never-ship number in
   order to forbid it — state the mechanism and point at the primary source instead. The
   never-ship table and per-file Never-ship sections are the recognized exception, since their job
   is recognition.
6. **Trademarked methodologies are named, cited, and taught by their evidence — never reproduced.**
   Practitioner opinion on MEDDIC/MEDDPICC/BANT/SPIN/Challenger/Sandler is split; claim no
   consensus in either direction.
7. **ICP is inherited, never redefined.** Sales applies marketing's ICP-as-a-funnel definition to
   account selection; it does not construct a new one.
8. **Score-vs-prediction discipline for forecasts.** Forecast method is publishable and widely
   published; forecast accuracy is published by no one — vendor, analyst, or academic. Teach what a
   small pipeline can validate at n=1 instead of pretending it can be calibrated.
9. **Disclose the AI agent, clearly, at first contact**, and never manufacture false engagement
   signals to defeat filtering — a category rule, not a single-tool ban.
10. **Write "discovery call," never bare "discovery"** (product owns the bare word); qualify "deal
    pipeline"/"sales pipeline" on first use; disambiguate "expansion" on first use (product's
    pricing lever, success's metric, sales's closed event are adjacent senses); spell out
    "sales-qualified lead"; keep "qualification" internal vocabulary, never user-facing.

## Required behavior

1. Run `scripts/check-sync` (and `scripts/lint-skill`) before any release; never replace the
   generic gate with domain-only checks.
2. Keep runtime frontmatter to `name` and `description`. Versions/metadata live in
   `.codex-plugin/plugin.json`, `CHANGELOG.md`, tags, and releases — never in `SKILL.md`.
3. Keep `SKILL.md` the direct router: one primary job × one base surface (+ additive agentic
   overlay), plus the "Not this skill →" decline table. References are flat, directly linked,
   self-describing, loaded only when their conditions apply.
4. Every reference begins with `Purpose / Read when / Skip when / Inputs / Produces`; add a
   `## Contents` when it exceeds ~100 lines.
5. Keep repository docs, eval fixtures, research, and site assets outside `skills/sales/`.
6. Release through matching plugin version, changelog entry, tag, and GitHub Release; set the
   GitHub About area (family-style description, canonical site alias as homepage, base + domain
   topics).

Do not mark the repository complete because structural lint passes. Activation, traversal, and
output evaluations must show the skill changes agent behavior usefully.
