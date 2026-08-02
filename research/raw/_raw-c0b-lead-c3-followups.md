# Raw research — C0b (channel lead follow-up) — loose ends left by C3 and C1

Author: Channel C lead. Date: 2026-08-03.
C3 (`_raw-c3-playbooks-ai-sales.md`) explicitly invited a lead second pass on forecasting
citations and left one licence graded CONFOUNDED; C1 (`_raw-c1-open-crms.md`) handed off
EspoCRM's published documentation as unchecked and unclaimed. All three are closed here. I did
these myself rather than spawn another worker — a handful of file reads.

**Surfaces used:** `gh api` (contents, base64-decoded) and `raw.githubusercontent.com` via
`curl`, both pinned to the commits C3 resolved. No WebSearch anywhere (quota-dead session-wide).

---

## 1. RESOLVED — `iPythoning/b2b-sdr-agent-template` is genuinely MIT

C3 graded this **CONFOUNDED** ("skim reported hasLicenseFile: true and the README shows an MIT
badge, but I did not read the LICENSE file's actual text… do not cite as MIT without a follow-up
read"). Correctly cautious. Closed now by reading the file itself:

`gh api repos/iPythoning/b2b-sdr-agent-template/contents/LICENSE` → one `LICENSE` file, 1,067
bytes, decoded text opens:

> *"MIT License*
> *Copyright (c) 2026 PulseAgent*
> *Permission is hereby granted, free of charge, to any person obtaining a copy of this software
> and associated documentation files (the "Software"), to deal in the Software without
> restriction…"*

Standard MIT body. The GitHub API also reports `mit`/`MIT` for this repo, so badge and file
agree — a non-discrepancy, which is worth recording precisely because C1 found the opposite
in three other repos. **Verdict: MIT, verified upstream. CONFOUNDED grade lifted.**
The copyright holder is "PulseAgent", the paid companion product C3 flagged — the licence is
clean, the repo's *self-promotional* character that C3 noted is unaffected and still stands.

---

## 2. THE MISSING HALF OF THE FORECASTING FLAGSHIP — Sourcegraph publishes what GitLab hides

C3 found `sourcegraph/handbook` → `content/departments/sales/process/forecasting.md` and quoted
two of its categories. Reading the file in full (68 lines) shows it is substantially more
valuable than that excerpt suggests, and it lands exactly where C2's GitLab null left a hole.

Source: `content/departments/sales/process/forecasting.md`
Permalink: https://github.com/sourcegraph/handbook/blob/5752928b213a3ddbc7cee4459524f404a5b96fb4/content/departments/sales/process/forecasting.md
Licence: Apache-2.0, root `LICENSE`, full text verified upstream by C3.

### 2a. It separates the forecast into four decomposed components

> *"Forecasting is comprised of the following components:*
> *1. Sales stage = Where the opp is in the sales process*
> *2. Forecast category = Where the opportunity sits in your forecast*
> *3. iARR = The likely amount the deal will close for*
> *4. Close date = Targeted date to close"*

Teachable in its own right: **stage and forecast category are explicitly different axes.** A deal
late in the process is not automatically a confident deal. Most CRM implementations collapse
these two into one (C1's evidence: EspoCRM, SuiteCRM, Krayin and frappe/crm all derive a
probability *from* the stage via a lookup table, which is precisely the collapse this document
refuses to make).

### 2b. Two DIFFERENT taxonomies — one per opportunity, one for the roll-up

**Opportunity-level**, verbatim:

> *"**Won** - For opportunities that have been Closed/Won - should be set automatically in
> Salesforce when an opportunity is closed.*
> ***Commit** - Opportunities where you have 1) the technical win, 2) received confirmation from
> the EB that they intend to purchase at or around the Amount/iARR and by the Close date you are
> forecasting, and 3) you have full understanding of the Paper Process and are aligned with the
> customer on a clear path to closure*
> ***Best Case** - Opportunities that have a 50% and above probability to close in a period. You
> should have 1) technical win or are currently in technical validation and 2) a mutual action
> plan to close within the period, that your EB or strong champion has agreed to*
> ***Pipeline** - opportunities in earlier stages (2-3) that you have reason to believe that you
> will be able to close by the Close Date specified on the Opportunity. Rarely should a Pipeline
> deal be present in your current quarter forecast*
> ***Omitted** - early stage (0-2) opportunities that aren't qualified or shouldn't be included
> in forecast at all"*

Note that **Commit carries three named, checkable conditions** — this is an exit-criteria-shaped
definition applied to a forecast category rather than to a stage. Given C1's finding that exit
criteria are effectively absent from open CRMs (present in exactly one of eight, and shipped
empty), a criteria-bearing *forecast category* is a genuinely scarce artifact.

**Roll-up level**, verbatim — and this is the part C3 did not surface at all:

> *"**Commit** - sum of Closed + Commit. Barring a truly exceptional situation, we will be fully
> counting on this to come in.*
> ***Best Case** - roughly the sum of your Call + any upside potential on existing deals + Best
> Case opportunities. If everything goes right, you have a path to reaching this Best Case number.*
> ***Call** - roughly the sum of Closed, Commit, and Best Case opportunities that you feel will
> come in. This value serves as what you believe will be your actual forecast. If you consider
> the Commit as the floor and Best Case as the ceiling, then the Call is the number in between
> that you are forecasting as the most likely outcome."*

**This is the flagship-grade find.** A published forecast that is deliberately *three numbers,
not one* — an explicit floor, an explicit ceiling, and a judged most-likely point between them,
with the roles named in the source's own words ("the Commit as the floor and Best Case as the
ceiling, then the Call is the number in between"). It is an interval-plus-point-estimate
structure arrived at operationally, and it is the strongest published counter-example to the
single-number stage-weighted forecast that every CRM in C1's corpus computes by default.

Also note the honest asymmetry: Commit is *summed* from records, while Call is what the rep
"feel[s] will come in" — the document is explicit that the headline forecast number is a
**judgement**, not a derivation. That distinction is exactly what our pack's forecasting
flagship needs to teach, and here it is stated by a real company about its own process.

### 2c. Cadence, tooling, and the fields that actually drive the number

> *"As of FY23, Forecasting is now done through **Clari**."*
> *"It is expected that all AEs keep their opportunities updated and current in **Salesforce**,
> the following fields directly influence Forecasts: Close Date / IARR / Stage / Forecast
> Category / Stretch IARR (for Best Case Forecast Categories)"*
> *"During the first two months of the quarter, forecasts should be made for the current quarter.
> In the 3rd month of a quarter forecasts should be made for both the current and next quarter."*
> *"**Once a week,** AEs should submit a **Call**, **Best Case**, and **Commit** number in Clari…
> Managers should also submit a Call, Best Case, and Commit number each week after their reps
> have submitted forecasts."*
> *"COMPLETE forecasts are reset to UPDATE REQUIRED every Tuesday EOD… Regional Forecasts are
> reviewed weekly on Tuesday during the weekly regional forecast call."*

Two structural facts worth carrying: managers submit their **own** numbers after seeing the reps'
(so the roll-up is a re-judgement, not a sum), and the forecast **expires weekly** by design.

### 2d. CONVERGENCE — and the null that survives both companies

Cross-referencing this against `_raw-c2-gitlab-handbook.md` and `_raw-c0-lead-gitlab-gapfill.md`:

| | GitLab | Sourcegraph |
|---|---|---|
| Stages + exit criteria | **Public**, 10 stages, criteria per stage | Not found in this file |
| Forecast categories | **Internal-only** (403) | **Public**, two-level taxonomy |
| Forecast tool | Clari (public, per retain-and-expand.md §3.2.3) | Clari (public, "As of FY23") |
| Cadence | Weekly, SAE/AE | Weekly, AE + manager, Tuesday reset |
| **Forecast accuracy** | **NOT PUBLISHED** | **NOT PUBLISHED** |

The two companies are almost perfect complements — each publishes the half the other withholds,
so together they give the pack a complete published picture of a real enterprise forecast
process. **Both independently use Clari**, which makes the vocabulary convergence more than
coincidence, though I want to be careful about the inference: I have **not** verified that
Commit/Best Case/Pipeline/Omitted originates with Clari or with Salesforce's standard forecast
categories. C1 describes it in passing as "the pipeline/best-case/commit/closed taxonomy
Salesforce popularized" — that attribution is **plausible but UNVERIFIED in this corpus**; no
primary source establishing its origin was read. Flag it as an open question for whichever
channel can reach a Salesforce primary; do not assert lineage in the pack without one.

**The null is the headline.** Two real companies publish their forecast process in operational
detail — categories, definitions, cadence, tooling, which fields feed the number — and **neither
publishes a single measurement of whether the forecast was right.** That is now verified across
three files at GitLab (all gated or silent) and the entirety of Sourcegraph's forecasting doc.
Combined with C1's finding that **no open CRM publishes a forecast-accuracy claim either**
(eight repos, targeted greps at the probability-computation code itself), the pattern holds
across both the process literature and the tooling: **forecast method is publishable; forecast
accuracy is not published by anyone in this corpus.** That is a strong, multiply-sourced,
negative finding and it is the natural spine of the forecasting flagship.

### 2e. STALENESS CAVEATS — mandatory if this is cited

Three, all verifiable and all must travel with any citation:

1. The file is a **Google-Docs export**. Its own leading HTML comment reads *"Docs to Markdown
   version 1.0β33 / Tue Jul 05 2022 10:33:38 GMT-0700 (PDT) / Source doc: Untitled document"* —
   so the content dates to **July 2022**, four years before this research.
2. It says *"As of FY23"* — a fiscal-year marker that was current at authoring and is now
   historical.
3. The repo is **archived** (C3: `archived: true`, `pushed_at: 2024-07-02`), and its README
   carries Sourcegraph's own warning that content was migrated to Notion and *"You need to scrub
   content from the handbook (incorrect content has been added before the repo was archived)."*

Cite it as **"a real company's published forecast method, as of 2022, from a since-archived
handbook"** — never as current Sourcegraph practice. The teaching value is in the *structure*
(three numbers, floor/ceiling/judged-middle, criteria-bearing categories), which does not decay
with the fiscal year; the org-specific details do.

---

## 3. CLOSED — EspoCRM's own documentation confirms C1's exit-criteria null (and is UNLICENSED)

C1 flagged EspoCRM's published sales-process documentation as explicitly **not checked** ("this
pass stayed inside the GitHub repo… Flagging for whichever channel covers published
playbooks/handbooks to pick up if not already covered"). C3's scope did not include open CRMs, so
nobody picked it up. Closing it here, because it is the one place a vendor could have documented
exit criteria that its *code* does not model — which would have weakened C1's null #2.

**Route note:** I first probed three plausible docs.espocrm.com URLs and all three returned
**404**. Guessed URLs are not citations, so I abandoned that approach and went to the
documentation's source repo instead, which is verifiable and pins.

Repo: `espocrm/documentation` (public, `pushed_at` 2026-08-01), pinned SHA
`9ff984348d31b0fc51bfa1c5bdf83aec83a0d051`.

### 3a. The finding — pipelines are structure, not criteria

Source: `docs/general/pipelines.md`
Permalink: https://github.com/espocrm/documentation/blob/9ff984348d31b0fc51bfa1c5bdf83aec83a0d051/docs/general/pipelines.md

The whole page (55 lines) documents the Pipelines feature *"As of v10.0."* — verbatim:

> *"The Pipelines feature allows you to configure multiple pipelines for the same entity type.
> While the status field can serve as a pipeline stage by default, with the Pipelines feature
> enabled, each record is assigned to a specific pipeline. The assigned pipeline determines the
> stages available for the record."*
>
> *"Each pipeline has its unique stages. Each stage is mapped to the Status field value. Each
> stage is stored as an entity."*
>
> *"The reordering is limited by the order of the Mapped Status field options. For example, if
> there are two statuses, Open and Closed, each with multiple stages, you cannot move stages
> belonging to the Closed status before stages belonging to the Open status."*

**A stage is a named entity mapped to a status value, with an ordering constraint. Nothing
more.** No requirements text, no entry/exit conditions, no gating on advancement — a user can
drag a card between any two stages the ordering permits. **C1's null #2 survives contact with
the vendor's own documentation**, which is the strongest place it could have failed. The null is
therefore about the product category, not about where C1 happened to look.

### 3b. One genuinely useful design idea, worth citing

The v10.0 feature exists because **one pipeline does not fit every deal type** — EspoCRM lets a
single entity type (Opportunities, Leads) carry *multiple* pipelines, each with its own stages,
scoped *"as available for all users or only for specific teams."* That is a real, shipped answer
to a question our pack has to address (new business vs renewal vs expansion vs channel deals do
not share a stage set), and it comes from a product rather than from folklore. Cite as an
existence proof that multi-pipeline modelling is mainstream, not exotic.

### 3c. LICENSING — the docs repo is UNLICENSED. Trap.

Per the charter's "list every license file" clause, I enumerated the full tree:

- `git/trees/HEAD?recursive=1` filtered for `licen|copying` → **zero matches**. No `LICENSE`,
  no `LICENSE.md`, no `COPYING`, anywhere in the repo.
- `README.md` read in full → build instructions only, **no license statement**.
- `mkdocs.yml` grepped for `licen|copyright` → **no license or copyright key**.

**Verdict: UNLICENSED CONTENT — do not reproduce.** This is a distinct and easily-missed trap:
EspoCRM's *code* repo is cleanly AGPLv3 (C1 verified `LICENSE.txt` upstream), so it would be
natural to assume the documentation inherits it. **It does not** — different repo, no license
grant, all rights reserved by default. We may cite, link, and quote minimally for commentary;
we may not reproduce the page or build a derivative asset from it. Same category as C3's
findings on `basecamp/handbook` and `Salesably/awesome-ai-agents-for-sales`, and worth stating
in the channel report as a pattern: **in this corpus, vendor documentation is systematically
less well licensed than vendor code.**

---

## 4. INDEPENDENTLY VERIFIED — the PostHog licence split is real, and it is MIT by TEXT not by NAME

The controller asked the channel lead to re-verify C3's PostHog licence-split claim personally
before the channel report asserts it, since it carries weight at synthesis. Done — I read the
file myself rather than relying on C3's quote. **C3's reading is correct**, and three details
worth adding.

Repo: `PostHog/posthog.com`, pinned to C3's SHA `259e5a6921ce301f4b8efa957d33050ea34e6d36`.
Permalink: https://github.com/PostHog/posthog.com/blob/259e5a6921ce301f4b8efa957d33050ea34e6d36/LICENSE

**Every licence file enumerated** (full recursive tree filtered for `LICEN[SC]E|COPYING`,
case-insensitive): exactly **one** — root `LICENSE`, 1,490 bytes. No per-package licences, no
`LICENCE` misspelling, nothing under `contents/`. So the entire split lives inside a single
file, which is precisely why it is easy to miss.

The file in full is two headed sections:

> *"# For all content except the /contents/ folder*
> *Copyright (c) 2020-2025 PostHog Inc.*
> *Please do not duplicate, copy, or use our website for commercial or non-commercial use. We
> put have put a lot of effort into a unique design, so we'd be sad if it became non-unique!*
> *We're happy for you to use our logo for the purposes of referencing PostHog, but not for you
> to pretend to be us."*
>
> *"# For content in the /contents/ folder*
> *Copyright (c) 2020-2025 PostHog Inc.*
> *Permission is hereby granted, free of charge, to any person obtaining a copy of this software
> and associated documentation files (the "Software"), to deal in the Software without
> restriction…"* [standard MIT permission grant, notice-retention condition, and all-caps
> warranty disclaimer follow verbatim]

### The three details

1. **The permissive half is MIT by its TEXT, never by its NAME.** The words "MIT License" do not
   appear anywhere in the file. It is the verbatim MIT grant, condition, and disclaimer under a
   heading that only says which folder it covers. Calling it "MIT" is a correct characterisation
   of the terms and the safest way to describe it is *"the MIT permission grant, applied by
   PostHog to the `/contents/` folder"* — not *"PostHog licenses its handbook under MIT"*, which
   implies a label the file never uses. This matters for the same reason the charter's rename
   clause does: we should describe what the file says, not the shorthand.
2. **The path claim checks out.** The LICENSE scopes the grant to *"the /contents/ folder"*; the
   handbook really does live at `contents/handbook/growth/sales/` — verified by fetching
   `contents/handbook/growth/sales/overview.md` at the pinned SHA (**HTTP 200**) and by counting
   the tree: **54 files** under that prefix, matching C3's "~55". The grant therefore does cover
   the sales handbook. Had the folder been named anything else, the grant would not have reached
   it.
3. **A third live "API lies" exhibit.** `gh api repos/PostHog/posthog.com --jq .license` returns
   `{"key":"other","name":"Other","spdx_id":"NOASSERTION"}`. The badge cannot express "one half
   proprietary, one half MIT", so it says nothing at all — exactly as it did for Twenty and Odoo
   in C1's corpus.

**Actionable obligation** (this is the part a downstream author will trip over): the MIT half
carries the standard notice-retention condition — *"The above copyright notice and this
permission notice shall be included in all copies or substantial portions of the Software."* So
if the pack reproduces substantial portions of PostHog handbook content, it must carry PostHog's
copyright and permission notice. Short quotation with attribution is unproblematic; lifting a
page into a shipped asset is not free of conditions.

**Do not touch anything outside `/contents/`.** The other half is an explicit prohibition on
duplicating the site for *"commercial or non-commercial use"*. Its informal, friendly register
("we'd be sad if it became non-unique!") does not soften it — it is still a reservation of
rights, and the informality is a trap for anyone skimming for legalese and concluding there
isn't any.

---

## 5. What this changes for the channel report

- One CONFOUNDED licence resolved to a clean MIT verdict; C3's ledger can be closed out.
- The forecasting flagship gains its missing half. GitLab supplies public stages with exit
  criteria and a gated forecast; Sourcegraph supplies a public, unusually honest forecast
  structure. The Call-as-judgement and floor/ceiling/most-likely framing is the single most
  teachable forecasting artifact found anywhere in this channel.
- The accuracy null now rests on three independent legs — GitLab (gated), Sourcegraph (published
  process, no accuracy), and eight open CRMs (no accuracy claim at the probability code). It
  should be stated as a corpus-wide pattern, not as a per-source observation.
- One inference is explicitly NOT made: the origin of the Commit/Best Case/Pipeline/Omitted
  vocabulary. Left as an open question with a named next step.
- C1's exit-criteria null is upgraded from "absent in eight codebases" to "absent in eight
  codebases *and* in the one vendor's own published documentation that was most likely to
  contradict it."
- A new licensing pattern for the ledger: vendor DOCS repos are systematically less well
  licensed than vendor CODE repos (EspoCRM code AGPLv3 / EspoCRM docs unlicensed). Anyone
  reasoning "the project is open source, so its docs are too" would ship a violation.
- PostHog's split is lead-verified and safe to assert, with one wording correction: it is the
  MIT grant applied to `/contents/`, not a repo labelled MIT. The badge-vs-file discrepancy
  count rises to three (Twenty, Odoo, PostHog), plus OpenOutreach's `LICENCE.md` spelling —
  four distinct mechanisms by which the licence API misleads, all in one channel.
