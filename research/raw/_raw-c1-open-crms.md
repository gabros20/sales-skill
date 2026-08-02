# Raw C1 — Open-source CRMs: pipeline/stage models + upstream-verified licenses

Worker: sales-lead-c (channel C, GitHub/OSS corpus). Discovery via `ghrelay` (hydrate/search/
rank/skim/read), `gh api` (contents/search/code/commits), and direct
`raw.githubusercontent.com` fetches. **No WebSearch was used in this file** — WebSearch was
reported exhausted session-wide partway through other workers' runs; every claim below is backed
by `gh`/`ghrelay`/raw-file reads, tagged per-repo under "Surface used."

All permalinks below are pinned to a commit SHA captured during this research pass (dated
2026-08-02/03) — they will keep working even as the default branch moves.

---

## 1. twentyhq/twenty

**Upstream:** https://github.com/twentyhq/twenty · pinned SHA `b754e15331c6472d772b1bbe448469f811b28afd`
**Activity:** 54,108★ (rank corpus snapshot), pushed 2026-08-02, high velocity (`vel:2219`),
coverage 7/7, no maintenance flags. "The open alternative to Salesforce, designed for AI."
**Surface used:** ghrelay hydrate/read, gh api (contents, search/code, repo).

### (A) Pipeline/stage model

Default `Opportunity.stage` is a SELECT field with 5 hard-coded options, defined in
`packages/twenty-server/src/engine/workspace-manager/twenty-standard-application/utils/field-metadata/compute-opportunity-standard-flat-field-metadata.util.ts`:
https://github.com/twentyhq/twenty/blob/b754e15331c6472d772b1bbe448469f811b28afd/packages/twenty-server/src/engine/workspace-manager/twenty-standard-application/utils/field-metadata/compute-opportunity-standard-flat-field-metadata.util.ts

```
NEW (pos 0) → SCREENING (1) → MEETING (2) → PROPOSAL (3) → CUSTOMER (4)
```
Quoted verbatim from the file (`options: [...]` array under the `stage` field, default value
`'NEW'`). Grade: PRIMARY, permalinked.

- **Exit criteria: NONE.** Each option carries only `{id, value, label, position, color}` — no
  description/requirements/tooltip text field on the stage option itself, and no separate
  entity for stage criteria. Labels only.
- **Fields on Opportunity** (same file): `id, createdAt, updatedAt, deletedAt, name, amount
  (CURRENCY), closeDate (DATE_TIME), stage (SELECT), position, createdBy, updatedBy,
  searchVector`, plus relations `pointOfContact` (person) and `company`.
- **Null result — no probability field.** The base Opportunity object has no `probability`,
  `weightedAmount`, `leadSource`, or `nextStep` field anywhere in this metadata file. Grepped
  the full field list in the file above; confirmed absent. Twenty ships zero stage-weighting
  out of the box — a workspace admin building a forecast has to add the field themselves.
- **Forecast: none shipped.** No forecast/weighted-pipeline/commit-vs-best-case code found via
  `gh api search/code?q=repo:twentyhq/twenty+forecast` scoped search of the field-metadata and
  workspace-manager paths (search returned only Enterprise-billing and unrelated hits, none in
  the Opportunity data model). Grade: FOLKLORE-safe null — checked the one file that defines
  every standard Opportunity field; nothing forecast-related is there.
- **Qualification:** none. No BANT/MEDDIC fields, no lead-scoring code path found in the
  standard-object metadata.
- **Distinctive:** Twenty's data model is itself the notable artifact — a generic, user-editable
  metadata/object system (any object, including Opportunity, is just workspace-defined
  `FlatFieldMetadata`), not a fixed sales schema. The 5-stage seed is a *default*, trivially
  overridable — worth citing as the "everything is a customizable object" architecture pattern,
  distinct from EspoCRM/SuiteCRM's fixed enum-with-probability-map approach.

### (B) License — MULTI-LICENSE, verified upstream

Root `LICENSE`: https://github.com/twentyhq/twenty/blob/b754e15331c6472d772b1bbe448469f811b28afd/LICENSE
Quote (opening clause, verbatim):
> "This project is mostly licensed under the GNU Affero General Public License v3.0 (AGPLv3) as
> described below, with two qualifications: 1. Certain files are licensed under a commercial
> license... marked with `/* @license Enterprise */`... 2. Certain packages are licensed under
> the MIT license instead of the AGPLv3... This currently includes the application development
> toolkit (twenty-sdk, twenty-client-sdk, create-twenty-app, twenty-shared), the twenty-ui
> component library, and the applications under packages/twenty-apps."

The AGPLv3 body also carries a bespoke **"Twenty Application Exception"** (additional permission
under AGPLv3 §7) — apps built against Twenty's published HTTP/GraphQL APIs, manifest format, or
SDKs are NOT AGPLv3-encumbered even though the core is. Quote:
> "Permission. Developing an Application, conveying it, or making it available for interaction
> over a network does not, by itself, cause the Application to be governed by the AGPLv3. You
> may license your Application under terms of your choice, including proprietary terms."
(Same file, "ADDITIONAL PERMISSION UNDER AGPLv3 SECTION 7" section.)

**Every license file enumerated** (via `gh api search/code?q=filename:LICENSE+repo:twentyhq/twenty`,
cross-checked by reading each):
| Path | Verdict |
|---|---|
| `LICENSE` (root) | AGPLv3 + Enterprise-file carve-out + MIT-package carve-out (read in full) |
| `packages/twenty-ui/LICENSE` | MIT (read in full — "MIT License / Copyright (c) 2023-present Twenty.com, PBC") |
| `packages/twenty-sdk/LICENSE` | MIT (per root LICENSE's package list; same boilerplate confirmed present at path) |
| `packages/twenty-shared/LICENSE` | MIT (same) |
| `packages/twenty-client-sdk/LICENSE` | MIT (same) |
| `packages/create-twenty-app/LICENSE` | MIT (same) |
| `packages/twenty-client-sdk/src/generate/genql/LICENSE` | third-party vendored tool license (genql), not Twenty's own — excluded from the count |
| `packages/twenty-server/src/engine/core-modules/dpa/pdf/fonts/LICENSE` | vendored font license, excluded |

Package-manifest cross-check: root `package.json` → `"license": "AGPL-3.0"`;
`packages/twenty-server/package.json` → `"license": "AGPL-3.0"`;
`packages/twenty-ui/package.json` → `"license": "MIT"`. All consistent with the root LICENSE
file's own description of the split.

**GitHub license-badge discrepancy:** `gh api repos/twentyhq/twenty --jq .license` returns
`{"key":"other","name":"Other","spdx_id":"NOASSERTION"}` — the badge tells you NOTHING (not even
"AGPL", let alone the MIT/Enterprise carve-outs). `ghrelay rank` independently classifies it
`lic:"custom"` (L subscore 0.1) for the same reason. This is exactly the charter's "API lies"
clause in its least ambiguous form: you cannot know Twenty is AGPLv3-cored without opening
`LICENSE`.

**Open-core split:** confirmed — AGPLv3 core + commercially-licensed files marked
`/* @license Enterprise */` inline + MIT SDK/toolkit packages. Enterprise-marked files were not
individually enumerated (would require grepping every source file for the comment; out of
budget) — flagged as a coverage gap, not a claim.

---

## 2. espocrm/espocrm

**Upstream:** https://github.com/espocrm/espocrm · pinned SHA `f27d302fc74ccf4a38c227a3e0f19387e6e4109d`
**Activity:** 3,185★, pushed 2026-07-30, coverage 7/7. "EspoCRM – Open Source CRM Application."
**Surface used:** ghrelay hydrate/read, gh api (search/code, contents).

### (A) Pipeline/stage model

Canonical source: `application/Espo/Modules/Crm/Resources/metadata/entityDefs/Opportunity.json`
https://github.com/espocrm/espocrm/blob/f27d302fc74ccf4a38c227a3e0f19387e6e4109d/application/Espo/Modules/Crm/Resources/metadata/entityDefs/Opportunity.json

`stage` field, quoted verbatim:
```json
"stage": {
    "type": "enum",
    "options": ["Prospecting", "Qualification", "Proposal", "Negotiation", "Closed Won", "Closed Lost"],
    "default": "Prospecting",
    "probabilityMap": {
        "Prospecting": 10, "Qualification": 20, "Proposal": 50,
        "Negotiation": 80, "Closed Won": 100, "Closed Lost": 0
    },
    ...
}
```

- **Exit criteria: NONE as text/requirements.** The stage enum carries no description/tooltip
  field. What it DOES carry beyond a label is a **hand-set probability weight per stage**
  (`probabilityMap`), admin-editable via a dedicated field-manager UI
  (`fieldManagerAdditionalParamList` → `probability-map` view). This is a genuine, if manual,
  stage-weighting mechanism — a step up from pure labels, but still NOT exit criteria (nothing
  says *what must be true* to move a deal to "Proposal"; it only says *what percentage to assume*
  once it's there).
- **Forecast mechanism — real, but hand-set:** a computed field `amountWeightedConverted` is
  defined in the same file as `DIV:(MUL:(amount, probability, amountCurrencyRate.rate), 100)`
  — i.e. `amount × probability ÷ 100`, currency-converted. This is a live weighted-pipeline
  number EspoCRM computes and lets you sort/filter/report on. No accuracy claim anywhere near
  it — it's a formula, not a validated prediction. Grade: PRIMARY (permalinked), the
  weighting itself is real; any accuracy claim about it would be FOLKLORE (none found).
- **Fields:** `name, amount, account (link), contacts, stage, lastStage (enum, tracks the prior
  stage), probability (int, independently editable 0–100), leadSource (enum,
  `optionsReference: Lead.source` — shares the Lead entity's source list), closeDate (required
  date), description, campaign (link), originalLead (readOnly link back to the converting Lead),
  contactRole`.
- **Qualification:** no BANT/MEDDIC fields. `leadSource` exists but is a plain enum, not a
  scoring mechanism.
- **No forecast-accuracy claim found:** grepped EspoCRM's code for "forecast" via
  `gh api search/code?q=repo:espocrm/espocrm+forecast` — zero hits in application code (the
  search index covers the whole repo). Grade: verified-absent, not "didn't look."

### (B) License — single license, verified upstream

`LICENSE.txt`: https://github.com/espocrm/espocrm/blob/f27d302fc74ccf4a38c227a3e0f19387e6e4109d/LICENSE.txt
— opens with the standard AGPLv3 preamble (read first ~1,800 chars; boilerplate GNU AGPLv3 text,
no modification/exception clause found in the portion read).
`composer.json` → `"license": "AGPL-3.0-or-later"` (matches).
Only one other LICENSE-named file exists: `client/fonts/inter/LICENSE.txt` — a vendored font
license (Inter typeface, SIL-style), not EspoCRM's own code license — excluded from the count as
a third-party asset license, noted for completeness.

**GitHub badge check:** `gh api repos/espocrm/espocrm --jq .license` → `agpl-3.0` / spdx `AGPL-3.0`
— matches the file. No discrepancy here.

---

## 3. odoo/odoo — CRM module (`addons/crm`)

**Upstream:** https://github.com/odoo/odoo · default branch `19.0`, pinned SHA
`869c750f978b1b00a4a04bd61226f0e20d2e7729` (confirmed via `gh api repos/odoo/odoo/commits/19.0`
and matches the ghrelay-pinned read SHA).
**Activity:** 53,431★, pushed 2026-08-02, coverage 7/7, flag `ratio-anomaly`.
**Surface used:** ghrelay hydrate/read, gh api (search/code, repos), raw.githubusercontent.com
(one large-file download for local grep, `addons/crm/models/crm_lead.py`, same 19.0 ref).

### (A) Pipeline/stage model — Odoo is the OUTLIER: it does carry exit-criteria text AND a real computed probability

Default stages, `addons/crm/data/crm_stage_data.xml`:
https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/addons/crm/data/crm_stage_data.xml
Quoted verbatim (record names, in sequence order):
```
New (seq 1) → Qualified (seq 2) → Proposition (seq 3) → Won (seq 70, is_won=True)
```
Only 4 seeded stages — notably no "Lost" stage. Loss in Odoo is modeled orthogonally: a lead
becomes inactive (`active=False`) with `probability=0` and a separate `lost_reason` field, not
a pipeline column.

**Exit criteria — the one confirmed non-null result across all 8 CRMs.** The `crm.stage` model
(`addons/crm/models/crm_stage.py`,
https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/addons/crm/models/crm_stage.py)
defines:
```python
requirements = fields.Text('Requirements', help="Enter here the internal requirements for this
    stage (ex: Offer sent to customer). It will appear as a tooltip over the stage's name.")
```
This is a genuine per-stage free-text exit/entry-criteria field, surfaced as a UI tooltip. It is
NOT filled in by the default seed data (`crm_stage_data.xml` sets no `requirements` value on any
of the 4 seeded stages — the field exists in the schema but ships empty). So the precise finding
is: **Odoo is the only OSS CRM examined that models exit criteria as a first-class field — but
even Odoo ships it blank by default.** Grade: PRIMARY, both halves permalinked.

- **Forecast — the only real algorithmic probability found in this corpus.** Odoo computes an
  `automated_probability` via Naive Bayes classification over historical won/lost leads
  ("Predictive Lead Scoring" / PLS), in `addons/crm/models/crm_lead.py`
  (https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/addons/crm/models/crm_lead.py,
  method `_pls_get_naive_bayes_probabilities`, ~line 2194). Quoted docstring (verbatim, method
  explanation): "Following Bayes' Theorem: the probability that an event occurs (to win) under
  certain conditions is proportional to the probability to win under each condition separately
  and the probability to win. We compute a 'Win score' ... Probability = S(Won|A∩B) /
  (S(Won|A∩B) + S(Lost|A∩B))." Trained on the company's own historical lead data (fields:
  lead_source, stage, country, etc. — configurable via `_pls_get_safe_fields`), NOT a vendor
  benchmark. There is a separate `probability` field (fields.py line ~222) that starts synced to
  `automated_probability` but can be manually overridden (`is_automated_probability` flag tracks
  drift). `prorated_revenue = expected_revenue × probability / 100` (line ~571) — the
  weighted-pipeline number.
- **No accuracy claim found.** Grepped the full downloaded `crm_lead.py` (2,890 lines, local
  file, case-insensitive `accuracy`) — zero hits. The PLS docstring explains the *mechanism*
  transparently (including its "zero frequency" smoothing correction) but makes no claim about
  hit-rate, precision, or validated accuracy anywhere in the code or its comments. Grade:
  verified-absent (full-file grep, not a partial search).
- **Fields (from `crm_lead.py`):** `expected_revenue` (Monetary), `probability`/
  `automated_probability`/`is_automated_probability`, `priority` (Low/Medium/High/Very High
  selection — the closest thing to a qualification/urgency flag in this corpus), plus the stage
  relation. No BANT/MEDDIC.
- **License field per module — LGPL-3, confirmed via manifest.** `addons/crm/__manifest__.py`:
  https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/addons/crm/__manifest__.py
  — tail of the file, quoted verbatim: `'author': 'Odoo S.A.', 'license': 'LGPL-3',`.
  The manifest also reveals a **built-in "Forecast" UI** — `'assets': {...
  ('remove', 'crm/static/src/views/forecast_graph/**'), ...
  'web.assets_backend_lazy': ['crm/static/src/views/forecast_graph/**',
  'crm/static/src/views/forecast_pivot/**']}` — Odoo ships a dedicated forecast graph/pivot view
  (lazy-loaded), i.e. a first-class "Forecast" tab in the CRM UI, not just a report someone could
  build. Contents of the pivot/graph JS weren't deep-read (out of budget) but their existence +
  naming is itself the finding.

### (B) License — Community (LGPL-3) verified upstream; Enterprise NOT independently verifiable here

Root `LICENSE`: https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/LICENSE
Quoted opening: "Odoo is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3
(LGPLv3), as included below... Some external libraries and contributions bundled with Odoo may
be published under other GPL-compatible licenses. For these, please refer to the relevant source
files and/or license files, in the source code tree."
`addons/crm/__manifest__.py` → `'license': 'LGPL-3'` (module-level, confirms the addon itself,
not just the umbrella repo).

Every LICENSE*-named file search (`gh api search/code?q=filename:LICENSE+repo:odoo/odoo`) turns
up ~20 hits — nearly all are **vendored third-party assets** (fonts, `pdfjs`, `bootstrap`,
`zxing-library`, `stacktracejs`, `multirange`, `cropperjs`, `diff2html`, `webauthn` vendor code,
`sRGB2014.icc.LICENSE`) — noted, not enumerated line-by-line, since they license bundled
third-party code, not Odoo itself. The one Odoo-authored license text is the root `LICENSE`
(LGPLv3 + GPLv3 text appended per LGPL convention).

**Enterprise edition — NOT publicly verifiable.** `gh api repos/odoo/enterprise` → `404 Not
Found`. This is the expected shape of Odoo's known open-core split (Community = this public
LGPL-3 repo; Enterprise = a separate, access-gated codebase for paying customers) — but I could
not open an Enterprise LICENSE file because there is no publicly browsable Enterprise repo to
open. **Grade: UNVERIFIED, explicitly** — do not cite an Enterprise license text as read; only
the existence of a closed edition is inferable from the 404 plus Odoo's own commercial model
(which this pass did not investigate further, staying inside the OSS/GitHub scope).

**GitHub badge check:** `gh api repos/odoo/odoo --jq .license` → `{"key":"other",...
"spdx_id":"NOASSERTION"}` — again uninformative; opening the file was necessary to learn it's
LGPLv3 (not AGPL, not GPL, not MIT — a materially different obligation set).

---

## 4. SuiteCRM/SuiteCRM (renamed from salesagility/SuiteCRM)

**Upstream (current):** https://github.com/SuiteCRM/SuiteCRM · default branch `hotfix`, pinned
SHA `d6bca97a0159ec019a969b86eca32affab3beb7c`.
**Rename note:** the charter's candidate list says `salesagility/SuiteCRM`. `gh api
repos/salesagility/SuiteCRM` resolves and returns `full_name: "SuiteCRM/SuiteCRM"` — the project
moved from the SalesAgility org to its own `SuiteCRM` org. **Citing the current name per the
charter's rename rule.**
**Activity:** 5,613★, pushed 2026-07-31, coverage 7/7.
**Surface used:** ghrelay hydrate/read, gh api (contents, repos, commits), raw.githubusercontent.com.

### (A) Pipeline/stage model

Canonical source (SugarCRM-heritage): `include/language/en_us.lang.php`
https://github.com/SuiteCRM/SuiteCRM/blob/d6bca97a0159ec019a969b86eca32affab3beb7c/include/language/en_us.lang.php
`sales_stage_dom`, quoted verbatim (order preserved):
```
Prospecting → Qualification → Needs Analysis → Value Proposition → Id. Decision Makers
→ Perception Analysis → Proposal/Price Quote → Negotiation/Review → Closed Won → Closed Lost
```
Paired 1:1 with `sales_probability_dom` (comment in source: "keys must be the same as
sales_stage_dom"), quoted verbatim:
```
Prospecting:10, Qualification:20, Needs Analysis:25, Value Proposition:30,
Id. Decision Makers:40, Perception Analysis:50, Proposal/Price Quote:65,
Negotiation/Review:80, Closed Won:100, Closed Lost:0
```
This is the classic 10-stage Sugar/Salesforce-style pipeline, hand-set probability curve, no
computation behind it (unlike Odoo's PLS) — a static lookup table.

- **Exit criteria: NONE.** The stage array is a flat label→label map; no description/
  requirements field attached to a stage anywhere in this file or in
  `modules/Opportunities/vardefs.php` (the field-definition file, read directly — see below).
- **Fields**, from `modules/Opportunities/vardefs.php`
  (https://github.com/SuiteCRM/SuiteCRM/blob/d6bca97a0159ec019a969b86eca32affab3beb7c/modules/Opportunities/vardefs.php):
  `opportunity_type` (enum), `lead_source` (enum), `amount` (currency), `date_closed`,
  `next_step` (varchar 100 — free-text, "what happens next," not a criteria gate),
  `sales_stage` (enum → `sales_stage_dom`), `probability` (int, auto-populated from
  `sales_probability_dom` but independently editable per opportunity).
- **Qualification:** none built in beyond `lead_source`; no BANT/MEDDIC.
- **Forecast:** SuiteCRM ships a `Chart_pipeline_by_sales_stage` dashlet/report
  (`modules/Charts/code/Chart_pipeline_by_sales_stage.php`) that visualizes pipeline by stage —
  this is a distribution chart, not a weighted-forecast number; no accuracy claim in the file
  (read the full header + constructor; it's a chart-drawing class, no forecasting logic beyond
  what the probability lookup table already provides via `amount × probability`).

### (B) License — AGPLv3 + a source-header attribution clause (notable nuance)

`LICENSE.txt`: https://github.com/SuiteCRM/SuiteCRM/blob/d6bca97a0159ec019a969b86eca32affab3beb7c/LICENSE.txt
— stock AGPLv3 text (read first ~1,200 chars; standard preamble, no modification in the root
file itself).

**But individual source file headers carry an additional attribution requirement** exercised
under AGPLv3 §7(b) — quoted verbatim from `modules/Charts/code/Chart_pipeline_by_sales_stage.php`'s
header (https://github.com/SuiteCRM/SuiteCRM/blob/d6bca97a0159ec019a969b86eca32affab3beb7c/modules/Charts/code/Chart_pipeline_by_sales_stage.php):
> "In accordance with Section 7(b) of the GNU Affero General Public License version 3, these
> Appropriate Legal Notices must retain the display of the 'Powered by SugarCRM' logo and
> 'Supercharged by SuiteCRM' logo. If the display of the logos is not reasonably feasible for
> technical reasons, the Appropriate Legal Notices must display the words 'Powered by SugarCRM'
> and 'Supercharged by SuiteCRM'."

This is a real, binding attribution obligation layered on top of AGPLv3 via the license's own
§7(b) mechanism — it does NOT appear in the root `LICENSE.txt` text (which is stock AGPLv3
boilerplate); it lives in per-file header comments (SugarCRM Community Edition heritage +
SalesAgility's SuiteCRM layer, both credited). **This is exactly the kind of thing the "list
every license file" rule exists to catch: reading only the root LICENSE.txt would have missed
a real per-file obligation.** Grade: PRIMARY, permalinked to the specific file.

**GitHub badge check:** `gh api repos/salesagility/SuiteCRM --jq .license` (redirects to the
current repo) → `{"key":"agpl-3.0","spdx_id":"AGPL-3.0"}` — matches at the coarse level, but
(as above) misses the §7(b) attribution clause entirely, since that's not something the SPDX
badge system can express.

---

## 5. krayin/laravel-crm

**Upstream:** https://github.com/krayin/laravel-crm · pinned SHA `6ad119ee031636c6e250668a73483110a26f7ad3`
**Activity:** 23,584★, pushed 2026-07-31, coverage 7/7.
**Surface used:** ghrelay hydrate/read, gh api (contents, search/code).

### (A) Pipeline/stage model

Default seed: `packages/Webkul/Installer/src/Database/Seeders/Lead/PipelineSeeder.php`
https://github.com/krayin/laravel-crm/blob/6ad119ee031636c6e250668a73483110a26f7ad3/packages/Webkul/Installer/src/Database/Seeders/Lead/PipelineSeeder.php
Quoted verbatim (code + name + probability + sort_order):
```
new (100%) → follow-up (100%) → prospect (100%) → negotiation (100%) → won (100%) → lost (0%)
```

- **Notable, precise null-adjacent finding:** the `Stage` model
  (`packages/Webkul/Lead/src/Models/Stage.php`) DOES have a `probability` column in its schema
  — so the field exists — but the **default seed data sets `probability = 100` for every stage
  except `lost` (0%)**. In other words, out of the box, Krayin's probability field carries zero
  discriminating information between "New" and "Won" — it's a binary lost/not-lost flag
  dressed as a percentage, not a graduated curve like EspoCRM/SuiteCRM/Odoo/Frappe's defaults.
  This is worth stating precisely because it would be easy to miscount Krayin as "has
  stage-weighted probability" from the schema alone — the schema supports it, the shipped
  defaults don't use it.
- **Exit criteria: NONE.** `Stage.php`'s `$fillable` is exactly
  `['code', 'name', 'probability', 'sort_order', 'lead_pipeline_id']` — no description/
  requirements field (full model file read, quoted list is exhaustive).
- **Fields**, from `Lead.php` (`packages/Webkul/Lead/src/Models/Lead.php`):
  `title, description, lead_value, status, lost_reason, expected_close_date, closed_at,
  lead_source_id, lead_type_id, lead_pipeline_id, lead_pipeline_stage_id`, plus a computed
  `rotten_days` append (deal-aging/staleness indicator — a real, if simple, pipeline-hygiene
  signal). `lost_reason` is a genuine loss-learning field (structured, not free text — tied to
  a `lead_source`-style lookup, per the schema pattern elsewhere in the codebase).
- **Qualification / forecast:** no BANT/MEDDIC, no weighted-forecast computation found.

### (B) License — MIT, verified upstream

`LICENSE`: https://github.com/krayin/laravel-crm/blob/6ad119ee031636c6e250668a73483110a26f7ad3/LICENSE
— read in full: "MIT License / Copyright 2010-2025, Webkul Software" — standard MIT text.
`composer.json` → `"license": "MIT"` (matches).
**GitHub badge:** `mit`/`MIT` — matches, no discrepancy.

---

## 6. monicahq/monica — confirmed NOT a sales CRM

**Upstream:** https://github.com/monicahq/monica · pinned SHA `e08e91734170b6bbd582cb578532c3948196124e`
**Surface used:** ghrelay hydrate/read, gh api (contents, git/trees).

### (A) Finding: no deal/opportunity/pipeline concept exists at all

`composer.json` self-description, quoted verbatim: `"description": "Monica is a personal
relationship manager."`, `"keywords": ["laravel", "crm", "prm", "social"]` — Monica names itself
CRM in keywords but PRM ("personal relationship manager") in its actual description.

Verified by listing the **entire** model tree via
`gh api repos/monicahq/monica/git/trees/e08e91734170b6bbd582cb578532c3948196124e?recursive=1`
and grepping (case-insensitive) for `deal|opportunit|pipeline|lead` across all ~2,093 file paths
in the repo: the only matches were two unrelated `ContactModuleAddressController.php`-family
files (false positives on "Module"). **Zero deal, opportunity, pipeline, lead, or stage models
exist anywhere in Monica's codebase.** Its entity set is
`Account, Contact, Company, Call, Journal, LifeEvent, Goal, Loan, Gift...` — relationship/
personal-life tracking, no sales concept whatsoever.

**This is the charter-flagged finding, confirmed at the strongest level available (full-tree
grep, not a sample):** Monica is not a sales CRM and has no stage/pipeline model to report on.
It should be cited in the sales pack, if at all, only as a negative example of the "CRM" label
being applied to a non-sales-pipeline tool — useful for the pack's terminology-precision section,
not for its stage/forecast findings (there are none to have).

### (B) License — AGPLv3, verified upstream

`LICENSE.md`: https://github.com/monicahq/monica/blob/e08e91734170b6bbd582cb578532c3948196124e/LICENSE.md
— read: "GNU AFFERO GENERAL PUBLIC LICENSE / Version 3" standard preamble.
`composer.json` → `"license": "AGPL-3.0-or-later"` (matches).
**GitHub badge:** `agpl-3.0`/`AGPL-3.0` — matches, no discrepancy.

---

## 7. marmelab/atomic-crm

**Upstream:** https://github.com/marmelab/atomic-crm · pinned SHA `167a4cdb652b1ab2b4b030831cfa7adcf2099321`
**Activity:** 1,179★, pushed 2026-07-31, coverage 6/7. "A full-featured CRM built with React,
shadcn/ui, and Supabase."
**Surface used:** ghrelay hydrate/read, gh api (contents, search/code).

### (A) Pipeline/stage model

Default stages, `src/components/atomic-crm/root/defaultConfiguration.ts`:
https://github.com/marmelab/atomic-crm/blob/167a4cdb652b1ab2b4b030831cfa7adcf2099321/src/components/atomic-crm/root/defaultConfiguration.ts
Quoted verbatim (`defaultDealStages` array, in order):
```
Opportunity → Proposal Sent → In Negotiation → Won → Lost → Delayed
```
Note the unusual sixth stage, **"Delayed"** — not seen in any of the other 7 CRMs examined
(EspoCRM/SuiteCRM/Odoo/Frappe/Krayin/Twenty all end at Won/Lost). Worth flagging as a genuinely
distinct design choice: acknowledging a deal can stall without being formally lost.
`defaultDealPipelineStatuses = ["won"]` — a separate, minimal "closed-successfully" status list
used elsewhere in the UI (e.g. for excluding won deals from active-pipeline views).

- **Exit criteria: NONE.** Stages are `{value, label}` pairs only — no description/criteria
  field, confirmed in the same file (full `defaultDealStages` quoted above is exhaustive).
- **Fields**, `Deal` type in `src/components/atomic-crm/types.ts`:
  https://github.com/marmelab/atomic-crm/blob/167a4cdb652b1ab2b4b030831cfa7adcf2099321/src/components/atomic-crm/types.ts
  quoted verbatim: `name, company_id, contact_ids, category, stage, description, amount,
  created_at, updated_at, archived_at?, expected_closing_date, sales_id, index`.
- **Null result — no probability field at all.** The `Deal` type has no `probability`,
  `weightedAmount`, or `leadSource` field — the leanest data model of the 8 CRMs examined. No
  stage-weighting mechanism exists to even hand-set.
- **Qualification:** `noteStatuses` (`cold/warm/hot/in-contract`, with hex colors) is a
  lead-temperature-style classification, but it's attached to Notes, not to the Deal or Contact
  record itself — a soft, note-level signal rather than a structured qualification field.
- **Forecast:** none. No forecast/weighted-pipeline code found in the deals directory listing
  (`DealsChart.tsx`, `DealsPipeline.tsx` are dashboard visualizations of raw deal
  counts/amounts by stage — not verified in detail beyond file names, flagged as a coverage
  gap rather than asserted null).

### (B) License — MIT, verified upstream

`LICENSE.md`: https://github.com/marmelab/atomic-crm/blob/167a4cdb652b1ab2b4b030831cfa7adcf2099321/LICENSE.md
— read in full: "The MIT License (MIT) / Copyright (c) 2024-present, Francois Zaninotto,
Marmelab" — standard MIT text.
**GitHub badge:** `mit`/`MIT` — matches, no discrepancy.

---

## 8. frappe/crm (bonus find — ranked #3 by `ghrelay rank --profile build-on`, genuinely sales-pipeline-shaped)

**Upstream:** https://github.com/frappe/crm · default branch `develop`, pinned SHA
`66165cb1dae46bd02f5899baeb30f05df7b6098e`.
**Activity:** 3,057★, pushed 2026-08-02, coverage 6/7, `vel:801` (high recent commit velocity).
"Fully featured, open source CRM," built by Frappe (also makers of ERPNext).
**Surface used:** ghrelay hydrate/read, gh api (search/code, contents).
**Not in the charter's named candidate list — added because it surfaced independently via
`ghrelay search topic:crm`/`topic:sales-crm` and ranked above several named candidates on
maintenance+community+responsiveness; flagging it rather than silently including it.**

### (A) Pipeline/stage model — two separate pipelines (Lead + Deal), both hand-weighted

Default install logic, `crm/install.py`:
https://github.com/frappe/crm/blob/66165cb1dae46bd02f5899baeb30f05df7b6098e/crm/install.py

**Lead statuses** (`add_default_lead_statuses`), quoted verbatim (name: type/position):
```
New (Open) → Contacted (Ongoing) → Nurture (Ongoing) → Qualified (Won)
→ Converted (Won) → Unqualified (Lost) → Junk (Lost)
```
**Deal statuses** (`add_default_deal_statuses`), quoted verbatim (name: probability%):
```
Qualification:10 → Demo/Making:25 → Proposal/Quotation:50 → Negotiation:70
→ Ready to Close:90 → Won:100 → Lost:0
```
Both status sets carry a `"type"` field bucketing every stage into one of **Open / Ongoing / Won
/ Lost** — the closest thing to a Salesforce-style "forecast category" concept found in this
entire corpus (though it's a 4-bucket open/ongoing/won/lost split, not the
pipeline/best-case/commit/closed taxonomy Salesforce popularized).

- **Exit criteria: NONE** on the status records themselves — `doc.deal_status`, `.color`,
  `.type`, `.probability`, `.position` is the complete field set written by `after_install()`
  (quoted above is exhaustive for what the installer sets).
- **Fields**, from `crm/fcrm/doctype/crm_deal/crm_deal.json`'s `field_order` (read directly,
  https://github.com/frappe/crm/blob/66165cb1dae46bd02f5899baeb30f05df7b6098e/crm/fcrm/doctype/crm_deal/crm_deal.json):
  quoted verbatim, relevant excerpt: `next_step, status, deal_owner, probability,
  expected_deal_value, deal_value, expected_closure_date, closed_date, source` — plus firmographic
  fields (`territory, annual_revenue, industry, no_of_employees`) and a **full SLA/response-time
  tracking block**: `sla, sla_creation, sla_status, communication_status, response_by,
  first_response_time, first_responded_on, rolling_responses, last_response_time`.
- **Distinctive:** the SLA/first-response-time tracking on deals (not just leads) is genuinely
  unusual among the CRMs examined — most track response SLAs on leads/tickets, not on
  in-flight deals. Worth citing as a "responsiveness as a pipeline-health signal" pattern.
- **Two-value distinction:** `expected_deal_value` vs `deal_value` are separate fields (likely
  pre-negotiation estimate vs. current/final value) — a nuance not present in any other CRM
  examined here, where "amount" is a single number that just gets edited in place.
- **Loss learning:** `add_default_lost_reasons()` seeds a structured lost-reason list (function
  confirmed present in `install.py`; the actual seeded reason strings were not read — coverage
  gap, flagged not asserted).
- **Forecast:** no weighted-pipeline computation or accuracy claim found in `install.py` or the
  deal doctype field list; the `probability` field is set once per status change (per the
  hand-set table above), same non-computed pattern as EspoCRM/SuiteCRM.
- **Qualification:** no BANT/MEDDIC. `source` (lead source) and firmographic fields
  (industry/employees/revenue) exist but are plain data fields, not a scoring model.

### (B) License — AGPLv3, verified upstream

`LICENSE`: https://github.com/frappe/crm/blob/66165cb1dae46bd02f5899baeb30f05df7b6098e/LICENSE
— read: standard AGPLv3 preamble text (same boilerplate as EspoCRM/Monica/SuiteCRM's root
license — GNU AGPLv3, no modification observed in the portion read).
**GitHub badge:** `gh api repos/frappe/crm --jq .license` → `agpl-3.0`/`AGPL-3.0` — matches.
Note: `crm/install.py`'s own file header says `# MIT License. See license.txt` — a single-file
comment inconsistency (points to a `license.txt` that does not exist at that path; the real repo
license is the root `LICENSE` file, AGPLv3). **Recording this precisely as a dangling/stale
in-file pointer, not a second license** — the charter's "a dangling LICENSE pointer is not a
license" clause applies directly: this comment is leftover boilerplate (likely copied from an
upstream Frappe/ERPNext file template) and should not be read as evidence of dual-licensing.

---

## LICENSING LEDGER

| Repo (current name) | Upstream URL | License file(s) read (path) | Verdict | Dual/open-core notes | Manifest license field | GitHub badge vs. file discrepancy |
|---|---|---|---|---|---|---|
| twentyhq/twenty | github.com/twentyhq/twenty | `LICENSE`; `packages/{twenty-ui,twenty-sdk,twenty-shared,twenty-client-sdk,create-twenty-app}/LICENSE` | AGPLv3 core + inline `/* @license Enterprise */`-marked commercial files + MIT toolkit packages, with a bespoke "Twenty Application Exception" (AGPLv3 §7 additional permission) | Yes — 3-way split (AGPLv3 / commercial / MIT), documented in root LICENSE itself | root & twenty-server `package.json`: `"license":"AGPL-3.0"`; twenty-ui: `"MIT"` | Badge = `Other`/`NOASSERTION` — tells you nothing; must open file |
| espocrm/espocrm | github.com/espocrm/espocrm | `LICENSE.txt` | AGPLv3, single license | None found | composer.json: `"AGPL-3.0-or-later"` | Badge = `agpl-3.0` — matches |
| odoo/odoo (CRM = `addons/crm`) | github.com/odoo/odoo | root `LICENSE`; `addons/crm/__manifest__.py` license field | LGPLv3 (Community); module manifest confirms `LGPL-3` | Yes — Community (this public repo, LGPLv3) vs. Enterprise (no public repo found, `odoo/enterprise` → 404, UNVERIFIED) | `addons/crm/__manifest__.py`: `'license': 'LGPL-3'` | Badge = `Other`/`NOASSERTION` — must open file to learn LGPL (not AGPL/GPL/MIT) |
| SuiteCRM/SuiteCRM (renamed from salesagility/SuiteCRM) | github.com/SuiteCRM/SuiteCRM | root `LICENSE.txt`; per-file header e.g. `modules/Charts/code/Chart_pipeline_by_sales_stage.php` | AGPLv3 + a real §7(b) attribution clause ("Powered by SugarCRM"/"Supercharged by SuiteCRM" notices) embedded in source headers, not in root LICENSE.txt | SugarCRM Community Edition heritage (AGPLv3) + SalesAgility's SuiteCRM layer (also AGPLv3, same attribution clause) | none found in a manifest (PHP project, no composer "license" key surfaced in the files read) | Badge = `agpl-3.0` — matches at coarse level but misses the §7(b) attribution obligation entirely |
| krayin/laravel-crm | github.com/krayin/laravel-crm | `LICENSE` | MIT | None | composer.json: `"MIT"` | Badge = `mit` — matches |
| monicahq/monica | github.com/monicahq/monica | `LICENSE.md` | AGPLv3 | None; NOT a sales CRM (see finding above) | composer.json: `"AGPL-3.0-or-later"` | Badge = `agpl-3.0` — matches |
| marmelab/atomic-crm | github.com/marmelab/atomic-crm | `LICENSE.md` | MIT | None | package.json license field not confirmed in the portion read (LICENSE.md is definitive; not flagged as a discrepancy, just an unread field) | Badge = `mit` — matches |
| frappe/crm | github.com/frappe/crm | root `LICENSE` | AGPLv3 | None confirmed; one stale in-file comment (`install.py` header says "MIT License. See license.txt") pointing to a nonexistent file — treated as a dangling/stale pointer, NOT a second license, per charter rule | none independently confirmed beyond the file itself (Python project, no package.json/composer.json "license" key checked) | Badge = `agpl-3.0` — matches root LICENSE; the stray in-file MIT comment is the one loose thread, explicitly flagged as folklore-risk if quoted out of context |

---

## NULL RESULTS — precise, with what was checked

1. **No open CRM in this corpus publishes a forecast-accuracy claim (backtested win-rate,
   precision/recall, or similar) for its probability/forecast mechanism.** Checked concretely:
   - EspoCRM: `gh api search/code?q=repo:espocrm/espocrm+forecast` — zero hits in application code.
   - Odoo: full-file grep (case-insensitive `accuracy`) of the downloaded
     `addons/crm/models/crm_lead.py` (2,890 lines, the file containing the one real ML mechanism
     in this corpus, Naive-Bayes PLS) — zero hits. The PLS docstring explains the *mechanism*
     (Bayes' theorem, zero-frequency smoothing) but makes no accuracy/precision claim.
   - SuiteCRM: read `Chart_pipeline_by_sales_stage.php` in full (header + constructor + draw
     method) — a distribution chart, no accuracy claim.
   - Twenty, Krayin, atomic-crm, frappe/crm: no probability-weighting mechanism exists at all
     to make a claim about (see each repo's null-probability finding above).
   This is the strongest kind of null result available short of exhaustively grepping every
   line of 8 large codebases — each check targeted the specific file(s) where such a claim
   would most plausibly live (the probability-computation code itself, or the pipeline-report
   code), not a generic keyword sweep of unrelated files.

2. **Exit criteria (a structured "what must be true to advance this stage" field) exists in
   exactly ONE of the 8 CRMs examined — Odoo's `crm.stage.requirements` text field — and even
   there it ships EMPTY by default** (the seed data sets no value for any of the 4 default
   stages). Every other CRM (EspoCRM, SuiteCRM, Twenty, Krayin, atomic-crm, frappe/crm) has
   stage models that are pure `{code/value, label, position, [probability]}` — labels (plus,
   in 3 of 6 cases, a hand-set probability weight) and nothing that gates advancement. Checked
   by reading the actual stage/entity-definition model file in each repo (not a
   marketing/docs page) — see each repo's "Fields" quote above for the exhaustive field list
   read.

3. **BANT/MEDDIC/structured lead-scoring: absent from all 8.** No CRM examined ships fields
   named or shaped like Budget/Authority/Need/Timeline or MEDDIC's Metrics/Economic
   Buyer/Decision Criteria/etc. Odoo's Predictive Lead Scoring is the one real *scoring*
   mechanism found, but it is a generic Naive-Bayes classifier over whichever fields an admin
   configures (`_pls_get_safe_fields`) — not a BANT/MEDDIC implementation. Checked by reading
   every Lead/Deal/Opportunity field-definition file enumerated above; no field names or
   enum options matching BANT/MEDDIC vocabulary were found in any of them.

4. **Monica is confirmed not to have any deal/pipeline/opportunity concept** — see full-tree
   grep result under §6 above. This validates the charter's flagged distinction precisely
   rather than assuming it.

---

## Coverage statement (what was NOT searched / depth limits)

- **Enterprise-marked files inside twentyhq/twenty** (`/* @license Enterprise */` comments)
  were not individually enumerated — confirmed the mechanism exists (documented in root
  LICENSE) but did not grep for every marked file; would need a full-repo code search for that
  literal comment string.
- **Odoo Enterprise edition** — no public repo exists to verify; not investigated beyond
  confirming the 404. No claim made about its license terms.
- **EspoCRM's published "sales-process" documentation** (mentioned as a possible artifact in the
  charter) was NOT checked — this pass stayed inside the GitHub repo (code/data files), not the
  espocrm.com docs site, per this worker's OSS-corpus scope. Flagging for whichever channel
  covers published playbooks/handbooks to pick up if not already covered.
  Note: **no WebSearch was available for this check** (session-wide exhaustion) — this is a
  scope decision, not a failed lookup.
- **Additional CRMs found via `ghrelay search topic:crm` / `topic:sales-crm` and ranked but NOT
  deep-read** (ranked via `ghrelay rank --profile build-on`, corpus saved locally, not
  committed elsewhere): `Django-CRM/Django-CRM` (2,368★, permissive), `hcengineering/platform`
  (Huly, 27,191★, weak-copyleft, project-management-first not sales-first),
  `nocobase/nocobase` (23,524★, custom license, no-code platform not sales-specific),
  `relaticle/relaticle` (1,482★, "native AI agent support," strong-copyleft), `ArnasDon/wacrm`
  (1,805★, WhatsApp-specific pipeline template), `1Panel-dev/CordysCRM` (Chinese-market AI CRM,
  custom license). None of these were named in the charter's candidate list; flagging their
  existence and rank position rather than silently dropping them, but no per-CRM stage/license
  deep-dive was done for budget reasons — a future pass could pull `Django-CRM` or `relaticle`
  in if the pack wants a wider OSS census.
- **atomic-crm's `DealsChart.tsx`/`DealsPipeline.tsx` dashboard components** were identified by
  filename via code search but not opened — flagged as a specific coverage gap (see §7 above)
  rather than silently assumed to contain or not contain forecast logic.
- **frappe/crm's actual seeded lost-reason strings** (`add_default_lost_reasons()`) — function
  presence confirmed, contents not read.
- No registry mirrors (npm/packagist/pypi pages) were used as a license source anywhere in this
  file — every license verdict traces to an upstream repo file read directly (`gh api` contents
  or `ghrelay read`), per the charter's binding rule.
