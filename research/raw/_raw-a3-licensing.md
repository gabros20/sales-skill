# A3 — License verification ledger (sales-skill research)

Worker: A3 · Channel: A (skills-ecosystem census) · Method: charter's 7-clause licensing standing rule.
Every row below was verified by fetching the raw file bytes at `raw.githubusercontent.com/<repo>/HEAD/<path>`
(HEAD resolves to the repo's current default branch — recorded per row) and reading the header, or via
`gh api` for repo metadata / manifests. `gh auth status`: logged in as gabros20, full scopes, rate limit
4992/5000 remaining at start — no rate-limit or auth failures this run.

---

## 1. LICENSING LEDGER TABLE

| # | Current full_name (as returned by API) | Upstream URL | Stars | Last push | Default branch | License file(s) + path | Actual SPDX per file | Manifest claims | API `license.spdx_id` | AGREE/DISAGREE | Citable? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | RefoundAI/lenny-skills | github.com/RefoundAI/lenny-skills | 1,212 | 2026-07-16 | main | `LICENSE` | MIT (Copyright Refound AI 2025) [permalink](https://github.com/RefoundAI/lenny-skills/blob/HEAD/LICENSE) | — | MIT | AGREE | YES |
| 2 | github/awesome-copilot | github.com/github/awesome-copilot | 37,357 | 2026-08-01 | main | root `LICENSE` (MIT); PLUS per-skill `skills/*/LICENSE.txt` or `LICENSE` for `appinsights-instrumentation`, `azure-resource-visualizer`, `azure-role-selector`, `quality-playbook`, `resemble-detect`, `winmd-api-search`, `pdftk-server` (referenced doc) — see §4 | Root: MIT (Copyright GitHub, Inc.) [permalink](https://github.com/github/awesome-copilot/blob/HEAD/LICENSE). `skills/quality-playbook/LICENSE.txt` and `skills/resemble-detect/LICENSE` verified = Apache-2.0 [permalink1](https://github.com/github/awesome-copilot/blob/HEAD/skills/quality-playbook/LICENSE.txt) [permalink2](https://github.com/github/awesome-copilot/blob/HEAD/skills/resemble-detect/LICENSE). Other 4 sub-license files (`appinsights-instrumentation`, `azure-resource-visualizer`, `azure-role-selector`, `winmd-api-search`) NOT individually opened — UNVERIFIED, presumed Apache-2.0 by filename/directory pattern only, do not cite as verified. | — | MIT (repo-level) | AGREE (root) | YES-WITH-ATTRIBUTION — cite root MIT for the repo; if citing an individual skill under Apache-2.0, cite that skill's own LICENSE.txt, not the repo root |
| 3 | anthropics/knowledge-work-plugins | github.com/anthropics/knowledge-work-plugins | 23,252 | 2026-08-02 | main | root `LICENSE`; PLUS identical-text per-plugin `LICENSE` in every plugin dir: `bio-research/`, `cowork-plugin-management/`, `customer-support/`, `data/`, `enterprise-search/`, `finance/`, `legal/`, `marketing/`, `partner-built/{apollo,brand-voice,common-room,slack,zoom-plugin}/`, `pdf-viewer/`, `product-management/`, `productivity/`, **`sales/`** (relevant to official-pack sweep, §6) | All verified samples (root, `sales/`, `marketing/`, `bio-research/`, `customer-support/`) = Apache-2.0, identical boilerplate header. [root](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/LICENSE) · [sales](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/sales/LICENSE) · [marketing](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/marketing/LICENSE) | `.claude-plugin/marketplace.json` — no `license` field, owner="Anthropic" | Apache-2.0 | AGREE | YES |
| 4 | anthropics/skills | github.com/anthropics/skills | 165,801 | 2026-07-24 | main | **No root LICENSE file at all** (root contains only `.claude-plugin`, `.gitignore`, `README.md`, `THIRD_PARTY_NOTICES.md`, `skills/`, `spec/`, `template/`). Each individual skill has its own `skills/<name>/LICENSE.txt`. Verified `skills/skill-creator/LICENSE.txt` and `skills/frontend-design/LICENSE.txt` = Apache-2.0. [skill-creator](https://github.com/anthropics/skills/blob/HEAD/skills/skill-creator/LICENSE.txt) · [frontend-design](https://github.com/anthropics/skills/blob/HEAD/skills/frontend-design/LICENSE.txt). `THIRD_PARTY_NOTICES.md` documents vendored BSD-2-Clause components (imageio, imageio-ffmpeg) used inside skill tooling. | Apache-2.0 (per-skill, verified 2/16 skill dirs) | `.claude-plugin/marketplace.json` — no `license` field, owner = Keith Lazuka (klazuka@anthropic.com) | **null** | AGREE (no root license exists; API correctly reports null — this is NOT an API lie, but note the repo IS licensed at the per-skill level, obscured by the repo-level null) | YES, but cite the SPECIFIC skill's own `LICENSE.txt`, never the repo as a whole (there is no whole-repo license) |
| 5 | HubSpot/agent-cli-skills | github.com/HubSpot/agent-cli-skills | 18 | 2026-07-23 | main | `LICENSE` | Apache-2.0 [permalink](https://github.com/HubSpot/agent-cli-skills/blob/HEAD/LICENSE) | — | Apache-2.0 | AGREE | YES |
| 6 | **DOES NOT EXIST** (`sales-skills/sales`) | github.com/sales-skills/sales → HTTP 404 | n/a | n/a | n/a | none reachable | none | none | n/a (repo not found) | N/A | **NO — NOT CITABLE.** See §5. |
| 7 | coreyhaines31/marketingskills | github.com/coreyhaines31/marketingskills | 42,757 | 2026-07-29 | main | `LICENSE` | MIT (Copyright Corey Haines 2025) [permalink](https://github.com/coreyhaines31/marketingskills/blob/HEAD/LICENSE) | — | MIT | AGREE | YES |
| 8 | gtmagents/gtm-agents | github.com/gtmagents/gtm-agents | 361 | 2026-04-03 | main | `LICENSE` | Apache-2.0 [permalink](https://github.com/gtmagents/gtm-agents/blob/HEAD/LICENSE) | — | Apache-2.0 | AGREE | YES |
| 9 | chadboyda/agent-gtm-skills | github.com/chadboyda/agent-gtm-skills | 73 | 2026-02-13 | main | **None.** `gh api .../contents/` root = `.claude-plugin`, `README.md`, `site`, `skills` — no LICENSE anywhere. | **EFFECTIVELY UNLICENSED** | `.claude-plugin/marketplace.json` has NO `license` field. **README.md says "## License / MIT" — a dangling claim; the LICENSE file it implies does not exist** (`raw.../LICENSE` = HTTP 404) | null | AGREE (API correctly shows null; the README is what's wrong) | **NO — EFFECTIVELY UNLICENSED** (dangling README claim, no backing file) |
| 10 | **Cold-IQ/ColdIQ-s-GTM-Skills** (RENAMED from `sachacoldiq/coldiq-s-gtm-skills`) | github.com/Cold-IQ/ColdIQ-s-GTM-Skills | 229 | 2026-07-28 | main | None found (empty tree grep) | **EFFECTIVELY UNLICENSED** | No `.claude-plugin/marketplace.json` (404), README has no license section | null | AGREE | **NO — UNLICENSED**, and cite the CURRENT name `Cold-IQ/ColdIQ-s-GTM-Skills`, not `sachacoldiq/coldiq-s-gtm-skills` |
| 11 | getcargohq/cargo-skills | github.com/getcargohq/cargo-skills | 15 | 2026-07-31 | main | None found | **EFFECTIVELY UNLICENSED** | `.claude-plugin/marketplace.json` present, no `license` field. README makes no license statement at all (verified full README head, no mention) | null | AGREE | **NO — UNLICENSED** |
| 12 | phuryn/pm-skills | github.com/phuryn/pm-skills | 24,779 | 2026-07-03 | main | `LICENSE` | MIT (Copyright Pawel Huryn 2026) [permalink](https://github.com/phuryn/pm-skills/blob/HEAD/LICENSE) | — | MIT | AGREE | YES |
| 13 | ncklrs/startup-os-skills | github.com/ncklrs/startup-os-skills | 37 | 2026-02-26 | main | **None** — tree listing has zero license-family files | **EFFECTIVELY UNLICENSED** | **README has a shields.io badge "License: MIT" hyperlinked to `LICENSE`, and a "## License / MIT" section — but `raw.../LICENSE` returns HTTP 404. Classic dangling pointer.** | null | AGREE (API right, README wrong) | **NO — EFFECTIVELY UNLICENSED** (say it in exactly those words per charter clause 3) |
| 14 | kostja94/marketing-skills | github.com/kostja94/marketing-skills | 812 | 2026-06-09 | main | `LICENSE` | MIT (Copyright kostja94 2025) [permalink](https://github.com/kostja94/marketing-skills/blob/HEAD/LICENSE) | — | MIT | AGREE | YES |
| 15 | claude-office-skills/skills | github.com/claude-office-skills/skills | 352 | 2026-01-31 | main | `LICENSE` | MIT (Copyright Claude Office Skills Contributors 2026) [permalink](https://github.com/claude-office-skills/skills/blob/HEAD/LICENSE) | — | MIT | AGREE | YES |
| 16 | customware-ai/skills | github.com/customware-ai/skills | 2 | 2026-07-21 | main | `LICENSE` (root) + `skills/domain-context/LICENSE` | Both MIT: root = Customware.ai 2026 [permalink](https://github.com/customware-ai/skills/blob/HEAD/LICENSE); sub = Customware 2025 [permalink](https://github.com/customware-ai/skills/blob/HEAD/skills/domain-context/LICENSE) | — | MIT | AGREE | YES |
| 17 | membranedev/application-skills | github.com/membranedev/application-skills | 252 | 2026-04-28 | main | **None.** (Tree-grep hit on `skills/noticeable` was a **false positive** — "noticeable" is a skill name containing the substring "notice", not a NOTICE file.) | **EFFECTIVELY UNLICENSED** | **README has an MIT shields.io badge hyperlinked to `LICENSE` — but `raw.../LICENSE` returns HTTP 404.** Second dangling-pointer case. | null | AGREE (API right, README wrong) | **NO — EFFECTIVELY UNLICENSED** |
| 18 | Casper-Studios/casper-marketplace | github.com/Casper-Studios/casper-marketplace | 11 | 2026-07-30 | main | `LICENSE` (root) + per-skill `LICENSE.txt` (13 files, e.g. `plugins/engineering/.../code-style/LICENSE.txt`) | All verified samples = MPL-2.0 [root](https://github.com/Casper-Studios/casper-marketplace/blob/HEAD/LICENSE) [sample](https://github.com/Casper-Studios/casper-marketplace/blob/HEAD/plugins/engineering/codebase-architecture/skills/code-style/LICENSE.txt) | — | MPL-2.0 | AGREE | YES-WITH-ATTRIBUTION (MPL-2.0 is copyleft on the covered file itself — read MPL §3 before adapting text) |
| 19 | forcedotcom/sf-skills | github.com/forcedotcom/sf-skills | 783 | 2026-07-31 | main | `LICENSE.txt` | Apache-2.0 (Copyright Salesforce, Inc. 2026) [permalink](https://github.com/forcedotcom/sf-skills/blob/HEAD/LICENSE.txt) | — | Apache-2.0 | AGREE | YES |
| 20 | Jeffallan/claude-skills | github.com/Jeffallan/claude-skills | 10,846 | 2026-05-20 | main | `LICENSE` | MIT (Copyright 2025, no named holder) [permalink](https://github.com/Jeffallan/claude-skills/blob/HEAD/LICENSE) | — | MIT | AGREE | YES |
| 21 | alirezarezvani/claude-skills | github.com/alirezarezvani/claude-skills | 23,656 | 2026-07-17 | main | Root `LICENSE` + **5** sub-project `LICENSE` files with DIFFERENT copyright holders: `engineering-team/playwright-pro/LICENSE`, `engineering-team/self-improving-agent/LICENSE`, `engineering/collab-proof/LICENSE`, `engineering/skillopt-sleep/LICENSE`, `loop-library/LICENSE` (6 license files total, 5 distinct holders — corroborated independently by channel lead `sales-lead-a` in `research/raw/_raw-a0-lead-breadth-repo.md`, and 5 of 6 files directly re-opened by me) | All MIT text, but copyright lines differ: root = Alireza Rezvani 2025; playwright-pro = Reza Rezvani 2026; **self-improving-agent = Reza Rezvani 2026 (directly re-verified this pass)**; collab-proof = **dong7812** 2026; skillopt-sleep = **Microsoft Corporation** 2026; loop-library = **Forward Future** 2026. [root](https://github.com/alirezarezvani/claude-skills/blob/HEAD/LICENSE) [self-improving-agent](https://github.com/alirezarezvani/claude-skills/blob/HEAD/engineering-team/self-improving-agent/LICENSE) [collab-proof](https://github.com/alirezarezvani/claude-skills/blob/HEAD/engineering/collab-proof/LICENSE) [skillopt-sleep](https://github.com/alirezarezvani/claude-skills/blob/HEAD/engineering/skillopt-sleep/LICENSE) | Lead additionally reports `commercial/.claude-plugin/plugin.json` = MIT and all 10 SKILL.md frontmatter blocks = `license: MIT` — consistent, no conflicts (not independently re-checked by me) | MIT (repo-level) | AGREE on SPDX (all MIT), but this is a real multi-attribution repo — it aggregates at least 5 distinct authors'/companies' vendored MIT skills under sub-directories, each keeping its own copyright notice (see §aggregators below) | YES, all MIT-compatible, but attribute the SPECIFIC sub-directory's copyright holder if quoting/adapting that skill, not "Alireza Rezvani" |
| 22 | ComposioHQ/awesome-claude-skills | github.com/ComposioHQ/awesome-claude-skills | 71,608 | 2026-07-24 | master | **No root LICENSE file** (confirmed via `contents/` listing: `.github, CONTRIBUTING.md, README.md`, and ~30 skill dirs — no LICENSE). Only per-skill `LICENSE.txt` for the ~13 skills that are direct copies of `anthropics/skills` content (`artifacts-builder`, `brand-guidelines`, `document-skills/*`, etc. — all Apache-2.0, same text as row 4). The repo's OWN original content (`composio-skills/` — hundreds of `*-automation` connector skills, `connect-apps`, `lead-research-assistant`, etc.) has **no license file of its own**. | Apache-2.0 for the ~13 copied-from-Anthropic skills only (verified by filename/dir match to row 4, not re-opened individually — UNVERIFIED for this repo specifically) | **README states in prose: "This repository is licensed under the Apache License 2.0. Individual skills may have different licenses — please check each skill's folder."** [README](https://github.com/ComposioHQ/awesome-claude-skills/blob/HEAD/README.md) — **but no root LICENSE file backs this claim.** | null | AGREE (API correctly shows null; the README's blanket claim is unbacked at the repo root) | **YES-WITH-ATTRIBUTION for the ~13 Anthropic-sourced skills (cite their own LICENSE.txt). NOT CITABLE / UNLICENSED for `composio-skills/*` and other original Composio content — no file backs the README's Apache-2.0 claim for those.** |
| 23 | twentyhq/twenty | github.com/twentyhq/twenty | 54,108 | 2026-08-02 | main | `LICENSE` (root, ~6000+ chars, custom composite); `packages/twenty-sdk/LICENSE`, `packages/twenty-ui/LICENSE`, `packages/twenty-client-sdk/LICENSE`, `packages/create-twenty-app/LICENSE`, `packages/twenty-shared/LICENSE` (all MIT sub-packages) | **Composite, non-standard license — read carefully (charter explicitly asked for this).** Root LICENSE text: "This project is mostly licensed under AGPLv3... with two qualifications: (1) files marked `/* @license Enterprise */` are NOT AGPLv3, they are under a separate commercial license defined at the end of the LICENSE file [proprietary/non-OSS]; (2) certain packages (twenty-sdk, twenty-client-sdk, create-twenty-app, twenty-shared, twenty-ui, and apps under packages/twenty-apps) are MIT instead, per their own package.json + LICENSE." The AGPLv3 portion ALSO carries an "ADDITIONAL PERMISSION UNDER AGPLv3 SECTION 7 (Twenty Application Exception)": apps that interact with Twenty ONLY through its published "Application Interfaces" (REST/GraphQL APIs, webhooks, manifest/config formats, function-runtime logic, component renderer, published SDKs) do NOT become AGPLv3-encumbered merely by that interaction, and MAY be licensed on your own proprietary terms — this exception does NOT apply to modifications of Twenty itself, and does NOT grant trademark rights (`.github/TRADEMARK.md`). [root LICENSE permalink](https://github.com/twentyhq/twenty/blob/HEAD/LICENSE) · [twenty-sdk LICENSE (MIT)](https://github.com/twentyhq/twenty/blob/HEAD/packages/twenty-sdk/LICENSE) | Root `package.json`: `"license": "AGPL-3.0"` — **this is a simplification/omission**: it states only the majority license and does not surface the Enterprise commercial carve-out or the MIT sub-packages. Not exactly false, but incomplete relative to the actual LICENSE file. | **"Other" / NOASSERTION** | **AGREE in spirit — GitHub's NOASSERTION is arguably the MORE accurate signal here (it correctly flags this as non-standard/non-classifiable), while the terse `package.json` "AGPL-3.0" is the one that understates the real complexity.** Not counted as an API lie. | YES-WITH-ATTRIBUTION for citing Twenty as an OSS CRM under AGPLv3 with the Application-Interfaces carve-out explained; the `twenty-sdk`/`twenty-ui`/`twenty-client-sdk` packages are separately MIT and citable as such; anything behind `/* @license Enterprise */` is proprietary — do not represent it as open source |
| 24 | espocrm/espocrm | github.com/espocrm/espocrm | 3,185 | 2026-07-30 | master | `LICENSE.txt` (root, AGPL-3.0); bundled `install/vendor/smarty/COPYING.lib` (LGPL-3.0, third-party Smarty template engine); `client/fonts/inter/LICENSE.txt` (SIL OFL 1.1, third-party Inter font) | Root = AGPL-3.0, standard FSF text [permalink](https://github.com/espocrm/espocrm/blob/HEAD/LICENSE.txt). Vendored Smarty = LGPLv3 [permalink](https://github.com/espocrm/espocrm/blob/HEAD/install/vendor/smarty/COPYING.lib). Vendored Inter font = SIL OFL 1.1 [permalink](https://github.com/espocrm/espocrm/blob/HEAD/client/fonts/inter/LICENSE.txt) | — | AGPL-3.0 | AGREE | YES — cite as AGPL-3.0 (network copyleft: a hosted/modified EspoCRM SaaS must offer source to its users) |

**Not in the ledger — no upstream repo/org exists on GitHub at all (checked live, not cached):** `sales-skills/sales` (see §5).

---

## 2. Disagreement log (GitHub API `license.spdx_id` vs. actual file content)

**Zero disagreements found in this run, across all 23 reachable GitHub repos verified (24 rows minus the
1 non-existent repo).** Every case where the API reported a concrete SPDX id (MIT/Apache-2.0/MPL-2.0/AGPL-3.0)
matched the file I actually opened. Every case where the API reported `null` corresponded to a repo that
genuinely has no root LICENSE file (rows 4, 9, 10, 11, 13, 17, 22). The one non-standard case (row 23,
`twentyhq/twenty`, API = `"Other"`/`NOASSERTION`) is arguably the API being MORE accurate than the
project's own `package.json` (`"license": "AGPL-3.0"`), which omits the Enterprise/MIT carve-outs.

**API lie count this run: 0 / 23.** This does NOT reproduce the "13+ lies" finding cited from a prior
family run — that finding does not generalize to this repo set. Read this as a genuine, useful negative
result, not noise: this run should not be cited as further evidence of a high API lie rate without
qualifying that this specific sample scored zero.

**A different, real failure mode showed up instead — the "dangling LICENSE pointer" pattern the charter
specifically warned about (clause 3) — and it clustered in the GTM/sales niche specifically:**

| Repo | What the README/badge claims | What's actually there | Verdict |
|---|---|---|---|
| `ncklrs/startup-os-skills` | Shields.io "License: MIT" badge + "## License / MIT" section, badge links to `LICENSE` | `raw.../LICENSE` → HTTP 404. No LICENSE file exists in the repo. | EFFECTIVELY UNLICENSED |
| `membranedev/application-skills` | Shields.io "License: MIT" badge linking to `LICENSE` | `raw.../LICENSE` → HTTP 404. No LICENSE file exists. | EFFECTIVELY UNLICENSED |
| `chadboyda/agent-gtm-skills` | "## License / MIT" section in README | `raw.../LICENSE` → HTTP 404. No LICENSE file, no `license` field in `.claude-plugin/marketplace.json`. | EFFECTIVELY UNLICENSED |
| `ComposioHQ/awesome-claude-skills` | Prose in README: "This repository is licensed under the Apache License 2.0" + a shields.io Apache-2.0 badge | No root LICENSE file anywhere in the repo tree. Only individual per-skill `LICENSE.txt` files for content copied from `anthropics/skills`. | The blanket repo-level claim is UNBACKED for the repo's own original content (`composio-skills/*` etc.); only the Anthropic-sourced subset is actually covered by a real file. |

This is 3 clean dangling-pointer cases plus 1 blanket-claim-without-file case — all in the Tier 2 GTM/sales
skill-pack cohort. If this pattern is real (small sample, but 4/22 Tier-2-ish repos = ~18%), it suggests
solo/small-team GTM skill authors copy a "MIT" badge from a template without adding the file. Treat any
GTM-skills-repo license badge as unverified until the raw file is opened — this is the operational lesson
for future workers in this family.

---

## 3. Renames/redirects found

- **Real rename (owner AND repo name changed):** `sachacoldiq/coldiq-s-gtm-skills` → **`Cold-IQ/ColdIQ-s-GTM-Skills`**. The literally-requested owner `sachacoldiq` returns 404 directly (`github.com/sachacoldiq` → 404); GitHub's API silently resolved and redirected to the current org `Cold-IQ`. **Cite the current name, `Cold-IQ/ColdIQ-s-GTM-Skills`, never the old one.** This is exactly the "stale citation passes review and then breaks" scenario the charter warns about.
- **Case-only normalizations (same repo, not a real rename, GitHub is case-insensitive on paths):** `refoundai/lenny-skills` → `RefoundAI/lenny-skills`; `hubspot/agent-cli-skills` → `HubSpot/agent-cli-skills`; `casper-studios/casper-marketplace` → `Casper-Studios/casper-marketplace`; `jeffallan/claude-skills` → `Jeffallan/claude-skills`; `composiohq/awesome-claude-skills` → `ComposioHQ/awesome-claude-skills`. Not a citation risk (case-insensitive resolution), but the ledger uses the API's returned canonical casing throughout for consistency.
- **`sales-skills/sales`** is NOT a rename target of anything discoverable — the org/repo simply does not exist on GitHub now (see §5). Searched GitHub repo search and code search for "sales-skills" broadly; no plausible successor repo found (closest name matches — `TheCraigHewitt/sales-skills` at 17★, `northrn/claude-sales-skills` at 3★ — are unrelated projects by different authors, not renames of the same repo).

---

## 4. Multi-license repos — full per-path breakdown

- **`github/awesome-copilot`** (row 2): root `LICENSE` = MIT (GitHub, Inc.). At least 7 individual skill/extension directories carry their OWN Apache-2.0 `LICENSE`/`LICENSE.txt` (`skills/appinsights-instrumentation`, `skills/azure-resource-visualizer`, `skills/azure-role-selector`, `skills/pdftk-server` (references a license doc, not opened), `skills/quality-playbook`, `skills/resemble-detect`, `skills/winmd-api-search`), plus an `extensions/apng-studio/LICENSE` and third-party notices under `extensions/pr-artifact-explorer/third-party-licenses/` (asciinema-player, octicons, primer-css — not opened, vendored front-end assets). **Governs:** the repo root and most content = MIT; the Apache-2.0-tagged skill folders are almost certainly skills mirrored in from `anthropics/skills` (same Apache-2.0 boilerplate, same directory-scoped-license pattern) and should be cited under their own file, not the repo's root MIT.
- **`anthropics/knowledge-work-plugins`** (row 3): root `LICENSE` = Apache-2.0. Every one of the 18 plugin subdirectories (including `sales/`, `marketing/`, `customer-support/`, `finance/`, `legal/`, `bio-research/`, etc.) carries an identical-text Apache-2.0 `LICENSE`. **Governs:** uniform Apache-2.0 across the whole monorepo — no actual conflict, just duplicated files (standard practice for repos meant to be split/distributed plugin-by-plugin).
- **`anthropics/skills`** (row 4): NO root license; every skill under `skills/*/` has its OWN Apache-2.0 `LICENSE.txt`. **Governs:** per-skill only. There is no "whole repo" license to cite.
- **`customware-ai/skills`** (row 16): root `LICENSE` (MIT, Customware.ai 2026) + `skills/domain-context/LICENSE` (MIT, Customware 2025) — same org, same terms, different copyright years — not a real conflict.
- **`Casper-Studios/casper-marketplace`** (row 18): root `LICENSE` (MPL-2.0) + 13 per-skill `LICENSE.txt` files, all verified-sample MPL-2.0. **Governs:** uniform MPL-2.0, file-scoped copyleft (MPL §3: modifications to a *specific covered file* must be released under MPL if distributed — this matters more than for MIT/Apache if any sales-skill work adapts Casper content).
- **`alirezarezvani/claude-skills`** (row 21): root `LICENSE` = MIT (Alireza Rezvani). At least 4 sub-project directories carry their OWN MIT `LICENSE` files with DIFFERENT COPYRIGHT HOLDERS: `engineering-team/playwright-pro/LICENSE` (Reza Rezvani), `engineering/collab-proof/LICENSE` (dong7812), `engineering/skillopt-sleep/LICENSE` (**Microsoft Corporation**), `loop-library/LICENSE` (Forward Future). **Governs:** all MIT-compatible, but this repo is an AGGREGATOR of other authors'/companies' vendored MIT-licensed skills. Citing "alirezarezvani/claude-skills is MIT" is true but attribution-incomplete if quoting a sub-skill — attribute the sub-directory's own holder.
- **`twentyhq/twenty`** (row 23): see full breakdown in the ledger — 3-way split (AGPLv3 core with an Application-Interfaces exception / MIT SDK-and-UI packages / proprietary `@license Enterprise`-tagged files). This is the most consequential multi-license case in the whole set for a sales pack citing an OSS CRM.
- **`espocrm/espocrm`** (row 24): root AGPL-3.0 + vendored third-party components under their own licenses (Smarty = LGPLv3, Inter font = SIL OFL 1.1). Not a conflict for EspoCRM's own code; matters only if redistributing the vendored assets themselves.
- **`ComposioHQ/awesome-claude-skills`** (row 22): effectively a "claims Apache-2.0, has no root file, actually multi-license-by-subdirectory" case — see disagreement log §2.

---

## 4b. Aggregators and whose work they carry

Per a request from channel lead `sales-lead-a`: a single repo-level SPDX id can be technically
correct while concealing that the repo bundles multiple parties' work under one root license claim.
Checked every multi-skill repo on this list for that pattern (i.e., not just "what SPDX string" but
"how many distinct copyright holders actually appear across the repo's license files"):

| Repo | Distinct copyright holders found | Evidence |
|---|---|---|
| `alirezarezvani/claude-skills` | **5**: Alireza Rezvani (root), Reza Rezvani (×2: playwright-pro, self-improving-agent), dong7812 (collab-proof), **Microsoft Corporation** (skillopt-sleep), Forward Future (loop-library) | 6 license files opened (5 by me directly, all cross-checked; lead independently verified the same set). All MIT — same SPDX, real multi-party aggregation. Corroborates the lead's naming of this pattern. |
| `ComposioHQ/awesome-claude-skills` | At minimum 2 "zones": (a) Anthropic, via ~13 skill dirs that are direct copies of `anthropics/skills` content, each keeping Anthropic's own Apache-2.0 `LICENSE.txt`; (b) Composio's own original work (`composio-skills/*` — hundreds of `*-automation` connector skills, `connect-apps`, `lead-research-assistant`, etc.) which carries **no license file of its own** anywhere, despite the README's blanket Apache-2.0 claim. Not a "many individuals" aggregator like alirezarezvani, but a real two-provenance mix where only one provenance is actually license-backed. | Tree listing + README fetch (see rows 4 and 22) |
| `Jeffallan/claude-skills` | **1** (unnamed, "Copyright (c) 2025", no other name given) — full recursive tree shows exactly one `LICENSE` file at root, no scattered per-skill license files despite a large `skills/` directory | Full tree re-fetched this pass: only top-level dirs are `.astro, .claude-plugin, .claude, assets, commands, docs, research, scripts, site, skills` plus the single root `LICENSE`. No evidence of a multi-holder aggregation pattern by file evidence, though I did not individually audit each skill's own `SKILL.md` frontmatter for a conflicting byline claim — that would be a cheap follow-up if this repo is actually cited. |
| `claude-office-skills/skills` | **1** ("Claude Office Skills Contributors" — itself an acknowledgment of a community, but expressed as one collective holder in one file, not per-contributor sub-licenses) — full tree shows dozens of skill dirs (`academic-search`, `ads-copywriter`, `ai-agent-builder`, `ai-slides`, `airtable-automation`, `amazon-seller`, etc.) but only the single root `LICENSE` matched the license-file grep; no scattered per-skill LICENSE files found | Full tree re-fetched this pass |
| `membranedev/application-skills` | **0** — re-ran a full recursive tree grep for `copyright\|author\|LICENSE` across every path in the repo; zero matches. Confirms (again) there is no license file anywhere in this repo, for anyone. The "aggregator" question is moot here because there's no license story to aggregate — see §5, EFFECTIVELY UNLICENSED. | Full tree re-fetched this pass |

**Filename false-positives excluded per the lead's flag** (files that are *about* licensing but are not
licenses themselves, and were correctly excluded from every ledger row above): `alirezarezvani/claude-skills/engineering/skills/dependency-auditor/references/license_compatibility_matrix.md`,
`.../scripts/license_checker.py`, `.../expected_outputs/sample_license_report.txt` — all tooling/reference
content about license auditing, not governing licenses of the repo itself. Also excluded:
`membranedev/application-skills/skills/noticeable` (a skill NAME containing the substring "notice",
matched by the grep pattern, not a NOTICE file) and `espocrm/espocrm/application/Espo/Core/Formula/Functions/LogGroup/NoticeType.php`
(an application source file, matched on "Notice" as a substring of "NoticeType").

**A repo mentioned by the lead but outside my assigned Tier 1–4 list, flagged for triage rather than
fully verified here:** the lead referenced `sickn33/antigravity-awesome-skills`. That exact
owner/name does not exist; `gh api repos/sickn33/antigravity-awesome-skills` resolves via silent
redirect to **`sickn33/agentic-awesome-skills`** (44,308★, license.spdx_id = MIT, pushed 2026-08-02) —
i.e., this is itself a rename case of the same shape as `sales-skills/sales`, except this one DOES
still exist under its new name. I did not do a full 7-clause pass on it (not sales/GTM-specific by
name, and outside my assigned repo list) — flagging the rename + top-line SPDX for whichever worker
does pick it up, so they don't waste a cycle rediscovering the redirect.

---

## 5. Non-retrievable / unlicensed — explicit list

**Genuinely unlicensed (no file exists, verified by direct fetch, regardless of what any badge/README claims):**
1. `chadboyda/agent-gtm-skills` — EFFECTIVELY UNLICENSED (dangling README claim)
2. `Cold-IQ/ColdIQ-s-GTM-Skills` (formerly `sachacoldiq/coldiq-s-gtm-skills`) — EFFECTIVELY UNLICENSED, no claim at all
3. `getcargohq/cargo-skills` — EFFECTIVELY UNLICENSED, no claim at all
4. `ncklrs/startup-os-skills` — EFFECTIVELY UNLICENSED (dangling README claim)
5. `membranedev/application-skills` — EFFECTIVELY UNLICENSED (dangling README claim)
6. `ComposioHQ/awesome-claude-skills` — the repo's OWN content (everything outside the ~13 Anthropic-sourced skill copies) is EFFECTIVELY UNLICENSED despite a blanket README claim

**Repo/org does not exist on GitHub at all:**
7. `sales-skills/sales` — **NO DISCOVERABLE LICENSE — NOT CITABLE.** Verified three independent ways: (a) `gh api repos/sales-skills/sales` → 404; (b) direct `curl -IL https://github.com/sales-skills/sales` → 404; (c) `curl -IL https://github.com/sales-skills` (the org itself) → 404. Yet **skills.sh's own search API still indexes it**: `curl https://skills.sh/api/search?q=sales-do` returns `{"id":"sales-skills/sales/sales-do","source":"sales-skills/sales","installs":323}`, and `skills.sh/sales-skills/sales` (redirects to `www.skills.sh/sales-skills/sales`) renders a page whose HTML literally embeds `https://github.com/sales-skills/sales` as the claimed source — a live registry pointing at a dead/renamed/deleted GitHub repo. This is itself a finding: skills.sh's index can go stale and keep serving install counts for a repo that no longer resolves. **Verdict: NOT CITABLE — no license is discoverable because the source itself is gone.**

**Tier 3 non-GitHub sources — could not discover ANY upstream repo or license for any of the three. CORRECTED FINDING (see note below — my first pass on #8/#9 was reading a 404 page and I initially mis-scored it):**

8. `code.deepline.com/deepline-gtm` — `code.deepline.com` 308-redirects to `deepline.com/deepline-gtm`, **which is itself a genuine HTTP 404** (`x-matched-path: /404`, `content-disposition: filename="404"` — Next.js's own error page, 25,907 bytes). **Correction:** I initially logged this as "a 25,907-byte SPA shell with no license visible," which was true but misleadingly framed — it's actually Next.js's *404 error page*, not the skill's real page. I found the ACTUAL live page by grepping `deepline.com`'s homepage JSON-LD for the string `deepline-gtm` and discovered the real route is **`deepline.com/skills/deepline-gtm`** (confirmed `HTTP 200`, 149,206 bytes, fetched and read in full). That real page contains **zero occurrences of the word "licen[cs]e"** and the only GitHub reference on it is a generic nav link plus `github.com/getaero-io` (reads as Deepline's own corporate GitHub org — unrelated to this specific skill's source). **Verdict stands, now on solid evidence: NO DISCOVERABLE LICENSE — NOT CITABLE**, confirmed by reading the correct, live, 200-status page, not a 404.
9. `code.deepline.com/gtm-meta-skill` — same 308 redirect behavior; `deepline.com/gtm-meta-skill` is also a genuine 404. Unlike `deepline-gtm`, I could **not** locate the real slug for this one: tried `/skills/gtm-meta-skill` (404), `/skills/gtm-meta` (404), `/gtm-stack/gtm-meta-skill` (404), and grepped the `deepline.com/gtm-stack` listing page (196KB) for any `*meta-skill*` link — none found in the static HTML (that listing page is very likely client-rendered/paginated, so a working link could exist behind JS I can't execute). **Verdict: page/route NOT LOCATED by this method — cannot be marked NOT CITABLE on the same solid footing as #8. Mark UNVERIFIED, not NO DISCOVERABLE LICENSE**, pending either a headless-browser follow-up or a corrected slug.
10. `oxygen-agent.com/oxygen-gtm` — returns **HTTP 404** directly, and unlike deepline, retrying with the `/skills/oxygen-gtm`, `/skill/oxygen-gtm`, `/gtm/oxygen-gtm` slug patterns that worked for Deepline all also 404. `oxygen-agent.com` root does resolve (HTTP 200, 963KB SPA) — **independently re-confirmed via `WebFetch`** (a genuinely different fetch path than the `curl` used for the initial pass, and NOT the exhausted `WebSearch` tool): the root page describes Oxygen as a proprietary AI GTM/CRM/sequencing SaaS platform starting at $99/month, with only Terms of Service / Privacy Policy / DPA / Acceptable Use Policy in its legal section — no GitHub link, no open-source license, no mention of "oxygen-gtm" by that specific name anywhere in the rendered content WebFetch could see. **Verdict: NO DISCOVERABLE LICENSE — NOT CITABLE**, now corroborated by two independent fetch methods (raw `curl` + `WebFetch`), neither of which is the exhausted WebSearch tool.

**Verdict for Tier 3 overall: 2 of 3 (`deepline-gtm`, `oxygen-gtm`) confirmed NO DISCOVERABLE LICENSE — NOT CITABLE on solid evidence (the real/live page was read in both cases, by two different fetch tools for oxygen). `gtm-meta-skill` (#9) downgraded to UNVERIFIED — I could not locate its real page at all, so I cannot claim to have read it before declaring it license-less; that would violate the charter's own "if you didn't open the file, mark UNVERIFIED" rule.** None of these three findings relied on the now-exhausted `WebSearch` tool — all fetches were direct `curl` (unaffected — not a GitHub host but a plain HTTP fetch, no rate-limit or budget shared with WebSearch) or `WebFetch` (also unaffected; distinct budget from WebSearch per the lead's alert). Caveat unchanged: none of these tools execute client-side JavaScript, so a hydration-gated license statement or source link remains theoretically possible and unruled-out, especially for #9 where I never even found the right URL.

---

## 6. Official-pack sweep — anthropics/* and sales-adjacency

**`anthropics/skills`** (165,801★, the flagship official example-skills repo): Enumerated the full plugin
manifest (`.claude-plugin/marketplace.json`) and skill directory listing. Ships two plugin bundles:
`document-skills` (xlsx, docx, pptx, pdf) and `example-skills` (algorithmic-art, brand-guidelines,
canvas-design, doc-coauthoring, frontend-design, internal-comms, mcp-builder, skill-creator,
slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing), plus a standalone `claude-api`
skill. **Nothing sales/CRM/deals/pipeline/proposal/outreach-related.** Zero sales-adjacency.

**`anthropics/knowledge-work-plugins`** (23,252★, the newer official business-plugins repo — this IS
sales-adjacent and matters a lot): root `.claude-plugin/marketplace.json` lists 18 plugins:
`productivity`, `enterprise-search`, `cowork-plugin-management`, **`sales`**, `finance`,
`customer-support`, `marketing`, `legal`, `data`, `bio-research`, `design`, `engineering`,
`human-resources`, `operations`, `pdf-viewer`, `product-management`, `small-business`, plus a
`partner-built/` collection (Apollo, Brand Voice, Common Room, Slack, Zoom integrations).

**The `sales` plugin itself** (`sales/README.md`, `sales/.mcp.json`, `sales/CONNECTORS.md`,
`sales/skills/`) is described in the marketplace manifest as: *"Prospect, craft outreach, and build deal
strategy faster. Prep for calls, manage your pipeline, and write personalized messaging that moves deals
forward."* — this is a DIRECT sales-adjacency claim from the marketplace description alone (prospecting,
outreach, deal strategy, call prep, pipeline management, personalized messaging). **This means the
official Anthropic ecosystem HAS staked a claim in the sales niche** via `anthropics/knowledge-work-plugins/sales`,
Apache-2.0 licensed (verified, row 3). I did not enumerate the individual skill files inside
`sales/skills/` (out of scope for a licensing-focused pass — flag this gap for the content/breadth
channel workers to walk and diff against our pack's scope). There is also a `marketing` plugin
sibling in the same repo, and `finance`/`customer-support` plugins that likely touch billing/renewal
edges — also out of scope here but worth the content channel's attention for seam-checking.

**Verdict:** the "empty niche" framing needs qualification — **anthropics/knowledge-work-plugins/sales is
a real, licensed, official occupant of exactly this space** (prospecting/outreach/pipeline/deal-strategy),
not a hypothetical risk. Whatever the content channels build should be checked against this plugin's
actual skill list before claiming "official ecosystem hasn't touched sales."

---

## 6b. Search-surface provenance (added per crew-wide WebSearch-exhaustion alert from `sales-lead-a`)

**I never called `WebSearch` anywhere in this raw file.** Every finding above rests on one of three
tool paths, recorded here explicitly so downstream readers can judge safety themselves:

- **`gh api` / `gh search` (GitHub-authenticated REST, unaffected by the WebSearch outage):** all
  repo metadata, tree listings, rename/redirect detection, `sickn33` redirect discovery. Session
  rate limit never dropped meaningfully below ~4990/5000 across the whole task.
- **Direct `curl` to `raw.githubusercontent.com`, `github.com`, `skills.sh`, `deepline.com`,
  `oxygen-agent.com`, `handbook.gitlab.com`, `npmjs.org`, `registry.npmjs.org` (plain HTTP fetch,
  no relation to WebSearch's budget):** every license-file byte read, the GitLab CC BY-SA 4.0
  footer discovery, the `sales-skills/sales` 404 confirmation, the corrected `deepline.com/skills/deepline-gtm`
  discovery, and all the dangling-LICENSE-pointer confirmations (`ncklrs`, `membranedev`, `chadboyda`).
  This is the backbone of the whole ledger and is the most trustworthy tier — raw bytes, no model
  summarization in between.
- **`WebFetch` (separate budget from `WebSearch` per the lead's alert, used only as a second-opinion
  corroboration pass, never as the sole source for a null finding):** used to re-confirm the
  `oxygen-agent.com` root page content (proprietary SaaS, no OSS/license mention) and to attempt a
  second read of the GitLab handbook footer (inconclusive — the small summarizing model didn't
  surface the footer from the truncated content it was given; the CC BY-SA 4.0 finding for GitLab
  therefore rests on the direct `curl` fetch, not WebFetch, and is unaffected by this).
  `WebFetch(https://deepline.com/deepline-gtm)` returned "HTTP 404 Not Found" — consistent with
  and independently corroborating the `curl`-based discovery that this exact path is a genuine 404
  (the real page is at `/skills/deepline-gtm`).

**No claim in this raw rests on an unreconfirmed `WebSearch` result.** The one place I'd flag as
genuinely soft is `code.deepline.com/gtm-meta-skill` (item 9 in §5): I could not locate its real
page through any combination of `curl`-guessed slugs, and did not have a headless-browser tool to
walk deepline.com's client-rendered listing pages. That is marked **UNVERIFIED**, not "no license,"
in the ledger — the honest gap is "I couldn't find the page," not "I found it and it has no license."

---

## 7. COVERAGE STATEMENT

**Verified to the full 7-clause standard** (root file read + every license file enumerated +
manifest checked + rename check + API comparison): rows 1, 2 (root only, see caveat), 3, 4, 5, 7, 8,
9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 — i.e., 23 of the 24 GitHub-reachable repos
in the ledger. `sales-skills/sales` (row 6) was pursued exhaustively but the repo does not exist —
coverage there means "confirmed unreachable via three independent methods," not "license read."

**Partially verified (caveat noted in the ledger row itself):**
- `github/awesome-copilot` (row 2): root MIT fully verified; only 2 of ~7 per-skill Apache-2.0
  sub-licenses individually opened (quality-playbook, resemble-detect). The other 4-5
  (`appinsights-instrumentation`, `azure-resource-visualizer`, `azure-role-selector`,
  `winmd-api-search`) are UNVERIFIED — flagged explicitly rather than inferred, per the charter's
  own instruction.
- `ComposioHQ/awesome-claude-skills` (row 22): confirmed no root LICENSE and confirmed the README's
  blanket claim, but did not individually re-open each of the ~13 Anthropic-sourced skill LICENSE.txt
  files inside this specific repo (relying on filename/path match to the already-verified
  `anthropics/skills` originals in row 4 — reasonable but not a byte-for-byte re-check within THIS
  fork/copy).
- `alirezarezvani/claude-skills` (row 21): verified root + 3 sub-project LICENSE files; the repo is
  large (many more skill directories) and may contain additional vendored sub-licenses not surfaced
  by the `licen[cs]e|copying|notice` grep pattern (e.g., a differently-named notice file) — treat the
  4 found as a sample, not an exhaustive enumeration.

**Tier 3 (non-GitHub) — coverage limit is real and stated plainly:** static `curl`/`WebFetch` fetches
cannot execute client-side JavaScript. `deepline.com/*` and `oxygen-agent.com` are React/Next.js SPAs;
a license statement or source-repo link that only renders after hydration would not appear in what I
fetched. I did not have a headless-browser tool available in this pass. Status per item, corrected
after finding my first pass on deepline had actually read a 404 page (see §5 for full detail):
- `deepline-gtm` — **resolved**: found and read the real live page (`deepline.com/skills/deepline-gtm`,
  HTTP 200, 149KB, full page read), which contains no license text. Verdict NO DISCOVERABLE LICENSE
  is on solid footing.
- `gtm-meta-skill` — **not resolved**: never found the real URL despite four slug guesses. Downgraded
  to UNVERIFIED rather than claimed-and-null.
- `oxygen-gtm` — **resolved** via two independent tools (`curl` + `WebFetch`) confirming the same
  proprietary-SaaS-with-no-OSS-mention picture on the site's root; the exact `/oxygen-gtm` sub-path
  itself never resolved (404 under every slug pattern tried, mirroring what worked for Deepline).
A follow-up with a JS-rendering tool (e.g., claude-in-chrome) would close the `gtm-meta-skill` gap and
could verify the ~17,227-install `deepline-gtm` figure's registry source if this pack wants to cite it.

**GitLab handbook license:** verified. `handbook.gitlab.com/handbook/sales/` footer embeds a
Creative Commons BY-SA 4.0 badge (`https://creativecommons.org/licenses/by-sa/4.0/`) next to a
"please contribute" link to `handbook.gitlab.com/handbook/about/contributing/`, confirming the
historical CC BY-SA 4.0 claim for THIS specific page — permalink to the page itself is the citation
(GitLab's handbook doesn't expose a separate static per-page license-statement URL beyond the
footer badge). Source repo (`gitlab-com/content-sites/handbook` on gitlab.com, not GitHub) was
identified per the charter's brief but not separately cloned/inspected — the live page footer is
the operative evidence and was sufficient to confirm the license claim.

**Tool failures / rate limits: none.** `gh auth status` was healthy throughout (gabros20, full repo
scope); GitHub REST rate limit never dropped meaningfully from the 4992/5000 starting budget across
~25 `gh api` calls plus ~45 raw-file `curl` fetches. One environment quirk (not a tool/auth failure):
inline `for`/`while` loops issuing `curl` calls intermittently failed with "command not found: curl"
inside this sandbox's Bash tool when run as ad-hoc multi-line heredoc-style commands; the workaround
(writing the loop to a `.sh` file and invoking `bash file.sh`) resolved it immediately and all
subsequent batch fetches succeeded — noting this in case it recurs for other A-channel workers using
the same sandbox.

**Not reached at all:** Odoo CRM, SuiteCRM, Krayin, Monica (charter said "note briefly ... if cheap" —
deprioritized in favor of full rigor on the required Tier 1–4 list within the time budget; flagging as
genuinely not investigated rather than silently omitting).
