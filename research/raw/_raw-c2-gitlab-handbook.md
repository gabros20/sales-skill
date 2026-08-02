# Raw research — C2 — GitLab handbook (sales)

Worker: sales-lead-c / C2. Channel: GitHub/OSS corpus, GitLab handbook deep-read.
Repo verified: **`gitlab-com/content-sites/handbook`** (current, active, on GitLab.com) —
NOT `gitlab-com/www-gitlab-com` (old repo; its own README still claims to source "the public
handbook" but a direct raw-fetch of its legacy path
`sites/handbook/source/handbook/sales/playbook/index.html.md` 404s — confirmed stale/dead,
2026-08-03). All permalinks below are pinned to commit
`46180fa3686c8baa55f91bf32c6e1d676eefd475` (HEAD of `main` at fetch time, 2026-08-02,
verified via `GET /projects/.../repository/commits?ref_name=main&per_page=1`).
Rendered `handbook.gitlab.com` URLs are also given where the page renders publicly — note
several rendered pages returned nav-only content to WebFetch; the raw markdown source (fetched
directly from the repo via `curl`) was the reliable path and is what's quoted below.

---

## BEST EXHIBITS (top 5, most quotable/useful)

1. **Commercial Sales Opportunity Stages — full stage-by-stage exit criteria**, 0-Pending
   Acceptance through 8-Closed Lost, verbatim, primary+secondary activities AND exit criteria
   per stage. The single best "real enterprise sales process" artifact found in this whole
   research effort. See §1.
2. **MEDDPPICC — GitLab's own qualification framework, letter-by-letter, with full qualifying
   question sets per letter** (cite, do not reproduce the question banks at length — see
   Licensing ruling). Confirms exact spelling. See §2.
3. **"Due to IP constraints, we have migrated content from this page to GitLab's internal
   Handbook."** — GitLab's own public admission that Command of the Message content was pulled
   from public view for IP reasons. Directly usable as evidence for our own cite-never-reproduce
   stance on trademarked methodologies. See §5.
4. **Forecasting and Pipeline X-Ray are NOT public** — the public handbook links to
   `internal.gitlab.com/handbook/sales/sales-forecasting/` (403 → login redirect) and to two
   analytics sub-pages (`pipeline-x-ray`, `pipeline-management-tools`) that 404 in the public
   repo. This is a first-class NULL RESULT for the flagship candidate — see §3 and Null Results.
5. **Content license is explicit and separate from code license**: CC BY-SA 4.0 for handbook
   content (quoted from `content/handbook/about/handbook-usage.md`), MIT for "the GitLab
   Software" per the repo's root `LICENSE`. Two different licenses, two different scopes. See
   Licensing section.

---

## 1. Sales stages — exact names, order, and published exit criteria

Source: `content/handbook/sales/commercial/comm-sales-opp-stages/_index.md`
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/commercial/comm-sales-opp-stages/_index.md
Rendered: https://handbook.gitlab.com/handbook/sales/commercial/comm-sales-opp-stages/

**Claim**: GitLab Commercial Sales uses 10 named opportunity stages (11 counting the terminal
"Closed Won" label separately from numbered stages), each with a description, primary/secondary
activities, and an explicit **Exit Criteria** list. Order:

`0-Pending Acceptance → 1-Discovery → 2-Scoping → 3-Technical Evaluation → 4-Proposal →
5-Negotiating → 6-Awaiting Signature → 7-Closing → Closed Won` (parallel terminal states:
`8-Closed Lost`, and — per the companion GTM-resources page — `9-Unqualified`, `10-Duplicate`).

**Verbatim quotes (exit criteria only, condensed per stage — full activities also captured in
the source and quoted at length below for the first three stages as evidence of depth)**:

> **0-Pending Acceptance** — *"This is the initial stage once an opportunity is created. The
> Sales Development team will scope business need/challenge and validate commitment from
> prospect/customer to have a discovery conversation with the GitLab Team."*
> **Exit Criteria:** *"Completion of sales qualification meeting / Validation by SAE/AE of the
> information collected by the Sales Development team member / Agreed upon next step"*

> **1-Discovery** — *"Uncover as much intelligence about the project as you can... Identify a
> business need or challenge the customer/prospect is trying to address and the potential for
> GitLab to solve."*
> **Exit Criteria:** *"Recap email sent to customer confirming pain points, key stakeholders,
> next steps, project timeline / Scoping meeting scheduled / Provide an estimate for the
> Expected Number of Users and the Expected Product for the Opportunity. This information is
> used to help the Customer Success team to predict their future workload as well as to help
> them with their hiring plans."*

> **2-Scoping** — *"Validate the pain points & determine how these pain points attach to the
> Customer/Prospect's top business challenges, the required capabilities to achieve the desired
> future state, and determine how GitLab is uniquely positioned to solve the challenge."*
> **Exit Criteria:** *"Stakeholders and engagement plan identified / Command Plan updated /
> Completed SA/AE strategy session/meeting / Channel and/or Alliances partner(s) engaged (if
> applicable) / Establish two engagement approaches to evaluation (Two-Lane Selling)"*

> **3-Technical Evaluation** — *"Validate the technical qualifications are a fit for the
> customer/prospect needs."*
> **Exit Criteria:** *"Demo output shared with customer... / ROI measures determined and
> validated / Mutual agreement to move to proposal and identified next steps / Professional
> Services identified and sourced (Partner or internal) if applicable / MEDDPPICC: Decision
> Criteria, Decision Process, Paper Process"*

> **4-Proposal** — *"Business and technical challenges [have] been uncovered and resolved...
> Prepare with the champion to meet with Economic Buyer on proposal OR enable champion to sell
> internally on GitLab's behalf."*
> **Exit Criteria:** *"Agreement on mutual close plan/timeline... / Procurement process
> confirmed (consider if using a Partner) / Implementation strategy confirmed / MEDDPPICC -
> paper process"*

> **5-Negotiating** — *"Finalize the agreement, pricing, business, and legal terms."*
> **Exit Criteria:** *"Customer has agreed to business terms / Customer has agreed to legal
> terms / Quote & Agreement ready to be routed for signature / AE has a clear timeline for when
> the OA will be signed and returned and implementation start date"*

> **6-Awaiting Signature** — *"Documents are in their final state ready to be executed."*
> **Exit Criteria:** *"Fully executed documents received / Attach fully executed documents to
> SFDC opportunity... / PO (if applicable) has been received / Complete vendor registration
> process / EULA (End User License Agreement) accepted by end-user"*

> **7-Closing** — *"Verifying the completeness of the documentation and opportunity to confirm
> ready to be Closed Won. Applies to sales assisted transactions only."*
> **Exit Criteria:** *"Once Deal Desk and Billing approve the opp and change the Approval
> Status to Approved, the system automatically moves it to Closed Won"*

> **8-Closed Lost** — *"An opportunity was lost and the prospect/customer has decided not to
> pursue the purchase of GitLab"* (activities only, no separate exit criteria — terminal state).

Grade: **PRIMARY, verbatim, permalinked.** This is the flagship exhibit for our own stage/
exit-criteria design — GitLab publishes the *entire* stage-gate definition set including dollar
thresholds embedded in-line (e.g. Command Plan required at "$100K+ for Enterprise, $50K+ for
Mid-Market"; Opportunity Overview command-plan fields required "$5k SMB, $10k MM").

A companion, slightly differently-worded version of the same 10 stages (with a few extra
process notes — e.g. `9-Unqualified`, `10-Duplicate`, and the "Early Stage Deals" aging
automation) lives on the GTM Resources page — see §4. The two pages are not verbatim identical
(the opp-stages page is Commercial-Sales-specific per its own title; GTM Resources is the
cross-segment glossary/reference) but describe the same stage sequence and are mutually
consistent on stage names, order, and MEDDPPICC placement.

---

## 2. Qualification framework — MEDDPPICC (verify spelling, cite-not-reproduce)

Source: `content/handbook/sales/meddppicc.md`
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/meddppicc.md
Rendered: https://handbook.gitlab.com/handbook/sales/meddppicc/

**Spelling verified: MEDDPPICC** — nine letters, two D's, two P's. NOT MEDDIC, MEDDICC, or
MEDDPICC (single-P). Confirmed by the page's own acronym list AND by the section headers on
the page itself (`## Metrics`, `## Economic Buyer`, `## Decision Process`, `## Decision
Criteria`, `## Partner`, `## Paper Process`, `## Identify Pain`, `## Champion`, `## Competition`
— 9 sections, matching 9 letters M-E-D-D-P-P-I-C-C).

**Verbatim quote (framing/operationalization, this is what we can safely quote at length — it's
GitLab's own process description, not the trademarked methodology content itself):**

> *"MEDDPPICC is a proven methodology used for strategic opportunity management and complex
> sales process orchestration for enterprise organizations and is an acronym for: Metrics,
> Economic Buyer, Decision Process, Decision Criteria, Partner, Paper Process, Identify Pain,
> Champion, Competition."*
>
> *"Qualify your opportunities throughout the sales process (but especially during the
> '1-Discovery' and '2-Scoping' stages)... MEDDPPICC is part of the Command Plan and is
> required for all new business opportunities above a certain threshold (see Opportunity
> Management Requirements for additional details)."* — the threshold detail itself is
> internal-only (`internal.gitlab.com` link, gated).

**Letter expansions with GitLab's own one-line gloss (safe to cite as GitLab's process
vocabulary, NOT to reproduce as if it were the trademarked training content)**:

- (M) Metrics — *"the economic impact of the solution"*
- (E) Economic Buyer — *"the individual within the customer's organization who is required for
  the final 'yes'"*
- (D) Decision Process — *"the process and timeline by which the customer will evaluate,
  select, and purchase a solution"*
- (D) Decision Criteria — *"the formal solution requirements against which each participant in
  the decision process will evaluate (includes the technical and financial lens with which the
  customer views GitLab)"*
- (P) Partner — *"the process of validating the partner landscape and opportunity implications"*
- (P) Paper Process — *"the process by which the customer will document and execute the process
  of purchasing (including the MSA, order form, PO, etc.)"*
- (I) Identify Pain — *"the problems created by the customer's current state (nobody buys until
  there is pain!)"*
- (C) Champion — *"the person(s) with power and influence inside the customer's organization who
  are actively selling on your behalf and willing to give you inside information to help you win
  the deal"*
- (C) Competition — *"competitive strengths, weaknesses, and differentiators, including
  competitor's champions"*

Each letter section also carries a full "Qualifying Questions" list (5-10 questions each) — we
did NOT reproduce those question banks here at length; they are exactly the kind of granular
operational content that starts to shade into "the trademarked methodology's actual training
material" territory even if GitLab itself published it. **Ruling: cite the 9-letter expansion
and GitLab's one-line gloss per letter (above); do not reproduce the qualifying-question banks
verbatim in our own pack — paraphrase or omit.**

**How it's operationalized (Command Plan)**: Source `content/handbook/sales/command-of-the-message/command-plan.md`
(permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/command-of-the-message/command-plan.md)

> *"The Command Plan consists of the below 3 sections. The Opportunity Overview section is
> required for ALL opportunities in stage 2-Scoping or later for current quarter and next
> quarter as a minimum global standard. The remaining sections (MEDDPPICC and Close Plan
> Details) are only required for opportunities at or above defined ARR thresholds ($100K+ for
> Enterprise, $50K+ for Mid-Market)."*
>
> *"There are a total of 9 MEDDPPICC fields (see details here)."*

This confirms: MEDDPPICC is tracked as **9 discrete SFDC/Command-Plan fields**, gated by ARR
threshold ($100K+ Enterprise / $50K+ Mid-Market), and the Command Plan itself is capped at 5,000
characters in Salesforce "to encourage sales team members to be crisp and succinct."

Grade: **PRIMARY, verbatim, permalinked.** Spelling variant conflict resolved — this is
MEDDPPICC, not any of the other MEDD* variants; do not conflate.

---

## 3. Forecasting process — mostly a NULL RESULT (flagship candidate, gated)

**What the public handbook says exists**: The Sales homepage lists a "Forecasting" quick-
reference row, twice, both pointing to the same internal-only URL:

> *"[Forecasting](https://internal.gitlab.com/handbook/sales/sales-forecasting/)"* and
> *"[Forecasting Definitions and Processes](https://internal.gitlab.com/handbook/sales/sales-forecasting/)"*

Source: `content/handbook/sales/_index.md`
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/_index.md

**Verification that this is genuinely gated, not just an internal cross-link that happens to
render publicly elsewhere**: a direct `curl` to
`https://internal.gitlab.com/handbook/sales/sales-forecasting/` returns HTTP 302 → HTTP 403,
redirecting to `https://gitlab.com/users/sign_in` — i.e. it requires GitLab team-member SSO.
Checked 2026-08-03.

**Deal Desk explicitly disclaims forecasting**: Source
`content/handbook/sales/field-operations/sales-operations/deal-desk.md`
(permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/sales-operations/deal-desk.md)
lists, under "Out of Scope": *"Forecast Management"* — confirming forecasting is owned
elsewhere (Sales Strategy & Analytics / RevOps), not Deal Desk, and that "elsewhere" is the
gated internal handbook.

**What IS public and forecast-adjacent** (a genuine planning assumption, not a measured
accuracy figure): Source `content/handbook/sales/field-operations/gtm-resources/_index.md`
(permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md)

> *"The following calculation is used to measure/plan for sales capacity. This is a calculation
> only and should be used to set goals and plan... Days to close - 180 days / Months to close -
> 6 months / Win rate - 33% / Months to lose - 3 months (half of months to close, expecting
> constant fallout) / Months on average - 4... / Capacity Goal (active opportunities in Stage
> 1-6) - 40 opportunities / SCLAU per month - 10 (40 opportunities / 4 months)"*

Grade: this is a **published planning heuristic** (33% assumed win rate, 180-day assumed cycle
length, used to size AE opportunity-count capacity) — GitLab's own text is explicit that it is
"a calculation only," not a backtested/measured accuracy claim. Cite as: *"GitLab publishes a
planning-only 33% win-rate assumption for AE capacity modeling — not a forecast-accuracy
measurement."* Do not upgrade this into "GitLab's sales forecast is 33% accurate" — that would
misrepresent the source.

**MEDDPPICC's stated purpose ties directly to forecast quality** (from §1's source page):
*"Proper sales pipeline management helps you allocate your time correctly, increase deal
velocity, and increase total deal volume, size, and revenue through accurate forecasting
practices."* — this is the closest the public handbook comes to asserting a forecasting
*rationale*; it names no method, category system, or accuracy number.

**Net finding for the flagship candidate**: GitLab's actual forecast **categories** (does
GitLab use Pipeline/Best Case/Commit/Closed, or Clari's categories, or something bespoke?),
forecast **cadence**, **roll-up process**, and any **accuracy measurement** are **not
publicly published** — they live behind `internal.gitlab.com`. The public handbook confirms
Clari is in GitLab's tech stack (referenced in passing: *"use the Sales Forecasting handbook
page and Clari cheat sheet"* — this specific sentence came from an AI-search-engine summary of
search results, NOT from a page WebFetch/curl actually confirmed for me; **grade this Clari
reference as UNVERIFIED / could not confirm against primary source** — I could not locate the
sentence in any raw file I fetched, so treat it as a lead only, not a citable claim).

---

## 4. Pipeline management — hygiene/aging rules ARE public; coverage ratio is NOT

Source: `content/handbook/sales/field-operations/gtm-resources/_index.md` (same file as §3)
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md

**Pipeline aging / auto-close automation — a real, numeric, citable hygiene rule:**

> *"To help keep our pipeline clean and ensure that early stage deals are moving through the
> pipe at the desired velocity, all New Business opportunities in stage 1-Discovery and
> 2-Scoping are governed under the below process. Timelines: Inactivity Warning Day & Auto
> Closure Day by Segment — Large/PubSec: Day 45 / Day 90 — Mid-Market: Day 21 / Day 45 — SMB:
> Day 7 / Day 15."*
>
> *"If there's no activity between the warning day and auto closure day: The opportunity gets
> automatically closed (8-Closed Lost) with a Closed Lost/Unqualified Reason of 'No
> Progression-Auto Close'."*

This is a genuinely citable, numeric, segment-differentiated aging/hygiene rule with an
automated enforcement mechanism (not just a guideline) — strong exhibit for our pack's pipeline-
hygiene section.

**"At risk" locking — note this is a false-friend, not deal-health risk:** the handbook's only
public use of "at risk" language for opportunities (`### Locking Opportunities as a result of
their "At Risk" potential`) is about **US export-compliance screening** (Visual Compliance /
Denied Party Lists), not deal-health or forecast risk:

> *"In order to be in compliance with US Regulations there is a need to screen opportunities
> against known individuals and organizations with whom we are not allowed to do business...
> Visual Compliance is a dynamic screening tool..."*

**Flag this explicitly if citing GitLab on "at-risk deals"**: their public "at risk" vocabulary
≠ our pack's deal-health-risk vocabulary. No public GitLab page defines deal-health "at risk"
criteria (e.g. no activity, no next step, stalled stage) as a named/flagged concept — the
closest is the aging/auto-close mechanism above, which is a different mechanism (hard automated
closure, not a soft "at risk" flag).

**Pipeline coverage ratio — NULL RESULT, confirmed by 404, not by absence-of-search:**
The public Sales Strategy & Analytics handbook page names two reports that would carry a
coverage ratio (Pipeline X-Ray: *"Pipeline coverage & generation by segment, region, order type
& sales qualified source for current and future fiscal quarters"*; and a "Pipeline Management
Tools" page) — Source: `content/handbook/sales/field-operations/sales-strategy/_index.md`
(permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/sales-strategy/_index.md)
— **but both linked sub-pages 404 when fetched directly from the repo**
(`content/handbook/sales/field-operations/sales-strategy/analytics/pipeline-x-ray.md` → 404;
rendered `handbook.gitlab.com/.../analytics/pipeline-management-tools/` → 404). Checked
2026-08-03. **No numeric coverage ratio (e.g. "3x" or "3.5x") could be verified against any
primary GitLab source I could read.** An AI-search-engine summary surfaced a "3.5x pipe
coverage" figure for GitLab Enterprise Sellers during this research, but I could not locate that
sentence on any page I fetched directly — **grade: UNVERIFIED, do not cite as a GitLab figure.**

**Opportunity types** (public, citable) — four types from the same source:
*"New account (new account, new subscription, new amount)... New subscription (existing
account, new subscription, new amount)... Add On Business (existing account, existing
subscription, new amount)... Renewal (existing subscription, existing subscription, existing
amount)... New business is the combination of new account and new subscription."*

---

## 5. Command of the Message / value framing — trademarked, IP-redacted by GitLab itself

Source: `content/handbook/sales/command-of-the-message/_index.md`
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/command-of-the-message/_index.md
Rendered: https://handbook.gitlab.com/handbook/sales/command-of-the-message/

**This is the standout finding for methodology IP-handling**: GitLab's own public page states,
verbatim:

> *"GitLab has adopted and operationalized Force Management's Command of the Message
> value-based sales messaging methodology. Due to IP constraints, we have migrated content from
> this page to GitLab's internal Handbook. GitLab team members may access additional content and
> resources on the Command of the Message Internal GitLab Handbook page..."*

This is GitLab **naming the vendor** (Force Management), **naming the methodology**, and
**explicitly stating they redacted the methodology's operational content from the public page
for IP/trademark reasons** — i.e. GitLab has independently reached the exact "cite, don't
reproduce" conclusion our charter mandates. Excellent supporting citation for our own licensing
posture on SPIN/Challenger/MEDDPPICC-family/Command-of-the-Message content.

**What remains public** (safe to cite — this is GitLab's own product-value framing, not Force
Management's IP): four "Customer Value Drivers" (*Increase Operational Efficiencies*, *Deliver
Better Products Faster*, *Reduce Security and Compliance Risk*, *Accelerate Cloud Adoption &
Transformation*) and an 11-row "GitLab Differentiators" table — both are GitLab's own product-
positioning content, not the Command-of-the-Message methodology itself, and are safe to cite as
"how GitLab frames its own value" (not "how Command of the Message works").

**Command Plan as the operationalization vehicle** — already quoted in full in §2; the Command
Plan explicitly says it operationalizes *both* Command of the Message and MEDDPPICC into SFDC
fields (Opportunity Overview: 5 fields; MEDDPPICC: 9 fields; Close Plan Details: 3 fields — 17
fields total, capped at 5,000 characters).

Grade: **PRIMARY, verbatim, permalinked.** Ruling: cite GitLab's naming of Force Management +
their IP-redaction statement; cite the public Value Drivers/Differentiators content freely
(GitLab's own IP); do not attempt to reconstruct or paraphrase Force Management's methodology
content from any secondary source — GitLab itself pulled it, and so should we.

---

## 6. Win/loss — partial: categories named, full picklist is gated to a Google Slides deck

Source: `content/handbook/sales/field-operations/gtm-resources/_index.md` (`8-Closed Lost`
section)
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md

**Verbatim process quote:**

> *"Select the applicable Closed Lost Reason as defined here [links to a Google Slides deck,
> not publicly readable without a GitLab account] — If the loss is due to Competitive Loss, you
> are required to select the competitor(s) from the opportunity's Competitor field. If the loss
> is due to Product Maturity, you are required to select the product stage(s) from the
> opportunity's Product Maturity: Product Line field."*
>
> *"Closed Lost/Unqualified Details is required all opportunities with a Net ARR value of
> $25,000 or greater OR opportunities where Closed Lost Reason = Other. Enter as much detail as
> you can as to why we lost the deal."*
>
> *"Please note that for new business deals where the opportunity is with a Large/PubSec
> Account OR the Net ARR is equal or greater than $12,000, then a notification will be sent to
> the #lost-deals Slack channel."*

**What we can cite**: two named loss-reason categories (**Competitive Loss**, **Product
Maturity**) each with a required follow-up field (competitor name; product-line stage); a
dollar-gated requirement to write qualitative loss detail ($25k+ Net ARR); and an internal
notification/review mechanism (`#lost-deals` Slack channel) for larger new-business losses.
This is a real, structured win/loss *process* — but the **full picklist of Closed Lost Reasons
is not in the public handbook**; it lives in a Google Slides deck that is not publicly
accessible (the link resolves to a Google Docs URL requiring auth). **Grade: partial — process
confirmed PRIMARY/verbatim; the complete reason taxonomy is NULL (gated, not reproducible).**

`9-Unqualified` stage (a separate concept from Closed Lost — used only when an opportunity
never should have entered the pipeline): *"A notification will be sent to the Sales Development
Team Lead and a feedback session should be scheduled between AE and Team Lead."* — a direct,
citable feedback-loop mechanism from lost/disqualified deals back to the sourcing team.

No dedicated "win/loss review" cadence or program (e.g. quarterly win/loss interviews,
third-party win/loss analysis) was found published anywhere in the handbook — **NULL RESULT**:
GitLab's public handbook describes CRM-level loss capture, not a narrative win/loss review
program.

---

## 7. Handoffs — marketing→sales (MQL/SAL/SAO/SQO) and sales→success

### 7a. Marketing → Sales: the lead/opportunity lifecycle, verbatim

Source: `content/handbook/sales/field-operations/gtm-resources/_index.md` (`## Customer
Lifecycle` and `## Glossary` sections)
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md

**The full lifecycle table, verbatim:**

> | Funnel stage | Record Type | Status or Stage |
> | Raw | Lead or Contact | Raw |
> | Inquiry | Lead or Contact | Inquiry |
> | Marketo Qualified Lead | Lead or Contact | MQL |
> | Accepted Lead | Lead or Contact | Accepted |
> | Qualifying | Lead or Contact | Qualifying |
> | Qualified | Lead or Contact | Qualified (converted) |
> | Pending Acceptance | Opportunity | 0 - Pending Acceptance |
> | Sales Accepted Opportunity | Opportunity | 1 - Discovery |
> | Sales Qualified Opportunity | Opportunity | 2 Scoping - 6 Awaiting Signature |
> | Customer | Opportunity | Closed Won |

**Glossary definitions, verbatim:**

> *"MQL | Marketo Qualified Lead - an inquiry that has been qualified through systematic means
> (e.g. through demographic/firmographic/behavior lead scoring)"*
>
> *"SAO | Sales Accepted Opportunity - an opportunity Sales agrees to pursue following an
> Initial Qualifying Meeting"*
>
> *"SQO | Sales Qualified Opportunity"* (glossed only as the acronym expansion in this table;
> the lifecycle table above defines SQO operationally as stages `2-Scoping` through
> `6-Awaiting Signature`)
>
> *"Qualified Lead | A lead a Business Development Rep or Sales Development Rep has qualified,
> converted to an opportunity and assigned to a Sales Representative (Stage
> 0-Pending Acceptance)"*

Note: our charter's outline mentions "SAL" (Sales Accepted Lead) as a term to expect — **GitLab
does not use SAL**; their lead-to-opportunity chain is MQL → Accepted → Qualifying → Qualified
(lead/contact side) → SAO → SQO (opportunity side). Flag this as a naming difference from the
generic MQL/SAL/SAO funnel-stage vocabulary our charter's outline assumed — GitLab skips "SAL"
as a distinct named stage.

**SAO qualification criteria — inbound vs outbound, both fully specified, verbatim (condensed
here; full text in the source)**:

> Inbound SAO required criteria: *"Authority"* (prospect directly involved in a project/team
> tied to the purchase, as evaluator/decision-maker/technical-buyer/influencer), *"Initiative"*
> (an identified company initiative GitLab could help with), *"Fit"* (current tools, entry-point
> use case, potential seats identified), *"Timing"* (a next step scheduled within 60 days of the
> initial qualifying meeting).
>
> Outbound SAO required criteria: same four-part shape but *"Internal Decision-Making Unit and
> Procurement Process"* replaces "Authority," and *"Identified Need"* replaces "Initiative" —
> otherwise Fit and Timing criteria are near-identical to inbound.
>
> *"Required field settings to identify an SAO are: The 'SDR Sales Accepted Date' is defined /
> The 'Is EDU/OSS Opportunity flag' is 'N' / Stage <> 10-Duplicate."*

This AITF (Authority/Initiative/Timing/Fit)-shaped inbound criteria and the outbound variant are
GitLab's own qualification bar for the marketing→sales (SDR/BDR→AE) handoff — a genuinely
citable, structured, dual (inbound/outbound) qualification framework, distinct from MEDDPPICC
(which governs *within*-opportunity qualification, not the lead→opportunity handoff gate).

Grade: **PRIMARY, verbatim, permalinked.** Directly load-bearing for our pack's
marketing→sales seam contract (charter cites marketing's own handoff.md defining "qualified
demand — a defined fit-plus-intent signal on a named account"; GitLab's SAO criteria is a real,
operationalized instance of exactly that fit+intent signal, safe to cite as a worked example).

### 7b. Sales → Customer Success handoff — staged, role-explicit, with a "why this stage"
rationale

Source: `content/handbook/customer-success/pre-sales-post-sales-transition.md`
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/customer-success/pre-sales-post-sales-transition.md
Rendered: https://handbook.gitlab.com/handbook/customer-success/pre-sales-post-sales-transition/

**Verbatim quote-table (the whole handoff summarized by GitLab in a Who/When/Why/How/Where
table):**

> *"Who coordinates the CSM introduction? Solutions Architect."*
> *"When does the introduction happen? 3-Technical Evaluation or 4-Proposal."*
> *"Why does the introduction happen at this stage? Introduce the CSM when business value
> discussions are still being had within the account, allowing them to build relationships with
> the key strategic decision-makers and help the customer visualize their implementation
> journey. This sets the CSM up for continued engagement at the right level within the
> account."*
> *"How does the introduction get scheduled? SA will schedule a 'Welcome to GitLab' call with
> the customer team, after having synced internally with the full account team (inc. CSM)."*
> *"Where can the CSM access account information? Customer Meeting Notes Doc / Command Plan /
> Account Plan / Customer Strategy/Value Plan."*

**Explicit dollar/role thresholds for the handoff, verbatim (from the stages page, §1's
source):**

> *"6-Awaiting Signature ... $50K+ deals - SA/AE introduce CSM (introducing Partner where
> applicable). Under $50K: SA and AE can begin preparing the contacts for receiving digital
> onboarding emails upon closing of a deal."*

**Full responsibility transfer at Closed Won, verbatim:**

> *"Once the opportunity moves stage to Closed Won the CSM should schedule the kickoff meeting
> with the customer... Now that the account is in post-sales, the CSM takes primary
> responsibility for guidance & best practices conversations, customer enablement, and product
> usage. Most responsibilities of the SAE & SA will transition to the CSM at this point."*

**Re-engagement triggers back to sales/SA** (a genuine "when does the pre-sales role
re-enter post-sales" list — directly relevant to our sales↔success contested-seam vocabulary):

> *"Development of expansion plans with the SAE and CSM leading to tier upgrades / A POV,
> product evaluation, RFP, or security [review] begins for a 'new' single team or an
> enterprise-wide tier upgrade not for renewal purposes / SAs may assist CSMs with an existing
> customer team on an exception basis. SA leadership approval is required."*

Grade: **PRIMARY, verbatim, permalinked.** This is a strong, concrete, real-world exhibit for
our pack's sales→success seam — it names the exact stage the handoff begins (3-Technical
Evaluation/4-Proposal), the exact stage responsibility fully transfers (Closed Won), a dollar
threshold ($50K) that changes the handoff's formality, and named re-engagement triggers that
mirror (without adjudicating) the "complex deal needing negotiation" contested boundary our
charter flags with success's pack.

**Companion page** — `content/handbook/customer-success/comm-sales/_index.md` (Commercial-Sales
segment specific version) — permalink:
https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/customer-success/comm-sales/_index.md
— adds an explicit "Seamless Customer Journey" framing: *"A seamless customer journey requires a
continuous flow of relevant information between the roles at GitLab with customer outcomes in
focus."* and names three handoff types (CSM-to-CSM, Pre-Sales-to-CSM, SA-to-SA).

---

## 8. Repo identity, structure, and a stale-cross-reference gotcha

**Repo confirmed current**: `gitlab-com/content-sites/handbook` (verified live via GitLab API
`GET /projects/gitlab-com%2Fcontent-sites%2Fhandbook`, and via a working commits-list call).
**Repo confirmed old/wrong**: `gitlab-com/www-gitlab-com` — still exists and has recent commit
activity (its own scope is now the marketing site / about.gitlab.com, per its own README:
*"This is the source for some of the https://about.gitlab.com/ site such as the public
handbook, blog, and jobs"* — this README line is itself stale, since a direct raw-fetch of its
legacy sales-handbook path 404s). **Do not cite www-gitlab-com URLs for sales-handbook content
— they are dead paths even though the repo itself is not archived.**

**Stale internal cross-reference found (a genuine gotcha, not a citation of ours)**: the
Commercial Sales Opportunity Stages page (§1) links to
`/handbook/marketing/sales-development/#qualification-criteria-and-saos` for SAO qualification
criteria — but that anchor does not exist on that page (verified by `grep` against the full raw
markdown of `content/handbook/marketing/sales-development/_index.md`); the actual, current SAO
criteria live on the GTM Resources page instead (§7a). This is GitLab's own handbook carrying a
broken internal link — worth noting only as evidence that even a mature, actively-maintained
public sales handbook accumulates stale cross-references; not something to cite as a finding
about sales process itself.

---

## LICENSE — every license file found, with path and ruling

1. **Root `LICENSE`** (repo: `gitlab-com/content-sites/handbook`) — **MIT License**, scoped
   explicitly to code, not content. Verbatim:
   > *"Copyright (c) 2011-present GitLab B.V. With regard to the GitLab Software: Permission is
   > hereby granted, free of charge, to any person obtaining a copy of this software and
   > associated documentation files (the 'Software'), to deal in the Software without
   > restriction..."*
   Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/LICENSE
   **Scope ruling: this licenses the Hugo site/build code (layouts, scripts, config), NOT the
   handbook prose content.** The phrase "With regard to the GitLab Software" is the repo's own
   scoping language.

2. **Content license — CC BY-SA 4.0**, stated in `content/handbook/about/handbook-usage.md`,
   not in a file literally named LICENSE, but this is the repo's own explicit, in-content
   license declaration for the handbook prose:
   > *"Remember that, like virtually everything we do, our handbook is open source, and we
   > expect that other companies may use it as inspiration for their own documentation and
   > practices... Our handbook falls under the [Attribution-ShareAlike 4.0 International
   > license](https://creativecommons.org/licenses/by-sa/4.0/)."*
   Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/about/handbook-usage.md
   (quote is at line 310 of the raw file as fetched).

3. No other LICENSE-named files were found at the repo root (root directory listing captured in
   full: `.devfile.yaml .editorconfig .gitignore .gitlab-ci.yml .hugolint.yaml
   .markdownlint-cli2.jsonc .tool-versions .vale.ini CONTRIBUTING.md Dangerfile LICENSE Makefile
   README.md compose.yml go.mod go.sum markdownlint-cli2-formatter-prettier.js package-lock.json
   package.json` — one `LICENSE` file, no `LICENSE-*` variants, no per-directory license files
   found in the paths I read).

**RULING (dual-license, per the standing "list every license file" rule):**
- **Handbook prose/content (what we actually want to quote — stages, MEDDPPICC framing, Command
  Plan, handoff pages, etc.)**: **CC BY-SA 4.0** — we may quote at length, reproduce structured
  content (e.g. full stage tables), and even adapt it, PROVIDED we attribute GitLab and
  ShareAlike any adaptation we publish (i.e. if we build a derivative "stage/exit-criteria
  template" clearly inspired by this, our own artifact inherits ShareAlike obligations if it's a
  close derivative — paraphrasing our own template design is the safer path for anything we ship
  as a reusable asset; direct quotation with attribution is safe for teaching/citation use,
  which is what this raw file and any downstream skill content does).
- **Site code (Hugo templates, build scripts, CI config)**: **MIT** — irrelevant to our content
  use, only relevant if we ever borrowed their Hugo build tooling (we are not).
- **Third-party trademarked methodology content that GitLab itself did NOT license permissively
  and in fact redacted** (Command of the Message, per §5's explicit "Due to IP constraints, we
  have migrated content..." statement): **not GitLab's to license at all** — this content is
  Force Management's IP; GitLab's CC BY-SA license does not and cannot extend to it, and GitLab
  visibly agrees (they pulled it from the public repo). **We must not treat any Command-of-the-
  Message-adjacent public GitLab page as implicitly CC-BY-SA-licensing Force Management's
  methodology — only GitLab's own value-driver/differentiator content on that page is
  CC-BY-SA-covered.**

---

## NULL RESULTS — what was searched for and not found

1. **Forecast accuracy figure**: no accuracy percentage, hit-rate, or backtested-accuracy claim
   for GitLab's own sales forecast was found anywhere in the public handbook. The forecasting
   process page itself is gated (`internal.gitlab.com`, 403). **This null result is itself the
   finding**: a company that publishes its entire stage-gate/exit-criteria system, its
   qualification framework down to the SFDC field level, and its aging/hygiene automation still
   does not publish forecast accuracy — consistent with our family's broader pattern that
   forecast-accuracy is measured privately (if at all) even by process-transparent
   organizations.

2. **Pipeline coverage ratio (e.g. "Nx pipe coverage")**: searched for and not found in any
   primary source I could fetch. The two handbook pages that would carry this number
   ("Pipeline X-Ray", "Pipeline Management Tools") both 404 in the current repo. A "3.5x"
   figure surfaced via an AI-search-engine summary during this research could not be traced to
   any GitLab page I could read directly — **do not cite it**.

3. **Full Closed Lost Reason picklist**: only two categories were nameable from context
   (Competitive Loss, Product Maturity); the full picklist lives in a non-public Google Slides
   deck.

4. **A named/published win-loss review program** (e.g. periodic win/loss interviews, a
   third-party win/loss firm, a structured review cadence): not found. What exists publicly is
   CRM-level loss-reason capture plus a Slack notification for large new-business losses
   (`#lost-deals`), not a review *program*.

5. **A "SAL" (Sales Accepted Lead) stage**: GitLab's lifecycle does not use this term (see §7a)
   — flagging in case our charter's outline assumed it's universal; it is not, at least not at
   GitLab.

6. **Clari-specific process detail**: an AI-search summary asserted GitLab sales teams "use...
   a Clari cheat sheet," but I could not verify this sentence against any page I fetched
   directly — grade UNVERIFIED, not cited above as fact.

7. **Sales KPIs / Sales Strategy accuracy dashboards**: the Sales homepage explicitly states
   *"[Sales KPIs](...) are [Not Public](/handbook/communication/confidentiality-levels/#not-public)
   and documented in [the Internal handbook]"* — confirming GitLab deliberately classifies its
   own sales KPI set (which would presumably include forecast-accuracy-adjacent metrics) as
   Not Public, a distinct confidentiality tier from the rest of the (public) handbook.
   Permalink for this statement: same as §1's `content/handbook/sales/_index.md`.

---

## Surfaces used (per-claim-area backing, for the channel coverage ledger)

- **Repo/file discovery and structure** (which files exist under `content/handbook/sales/...`,
  `content/handbook/customer-success/...`, `content/handbook/marketing/...`): GitLab's own
  public REST API (`gitlab.com/api/v4/projects/.../repository/tree`), unauthenticated,
  read-only, zero quota concerns — this is the surface behind essentially every file path cited
  above.
- **All verbatim quotes** (§1-§7, LICENSE section): direct `curl` fetch of raw markdown from
  `gitlab.com/gitlab-com/content-sites/handbook/-/raw/main/<path>` — i.e. reading the actual
  source file, not a rendered page and not a search summary. This is the most reliable surface
  found this session: `WebFetch` against rendered `handbook.gitlab.com/...` pages repeatedly
  returned nav-only content (documented failures early in this run) and was abandoned in favor
  of raw-file `curl`.
- **404/403 verification for NULL RESULTS** (forecasting page, Pipeline X-Ray, Pipeline
  Management Tools, old `www-gitlab-com` sales path, the stale `#qualification-criteria-and-saos`
  anchor): direct `curl` HTTP-status checks and `grep` against fetched raw content — not
  inferred from a search engine returning nothing.
- **WebSearch**: used twice, both *before* the session-wide quota was exhausted (confirmed by
  the later, explicit "budget exhausted" response on a third call). Those two calls (1) helped
  identify the current repo (`content-sites/handbook`, corroborated immediately afterward by a
  direct API existence check) and confirmed the MEDDPPICC spelling as a discovery lead (later
  independently confirmed against the primary source page's own section headers in §2 — the
  citation in this file rests on the primary-source confirmation, not the search summary); (2)
  surfaced two unverified secondary claims (a "3.5x pipe coverage" figure and a "Clari cheat
  sheet" reference) that I could **not** trace to any primary page I fetched — both are
  explicitly labeled UNVERIFIED / not cited as fact in §3, §4, and the Null Results section, per
  standing rules on reconstructed/unconfirmed citations. No null result in this file rests on a
  WebSearch call returning empty/exhausted — every NULL RESULT above is backed by a direct
  404/403/absence-in-fetched-content check.

## Coverage note (what I did not search)

I did not deep-read: the Enterprise-segment-specific playbook (`content/handbook/sales/playbook/`
— largely a discovery-methodology sub-tree, only skimmed its directory listing), the full
`sales-operating-procedures` tree (deal-closure/retain-and-expand pages, referenced but not
opened), the `command-of-the-message/metrics.md` and `proof-points.md` sub-pages (ROI/metrics
conversation guidance — named but not read in full), the `training/` tree (onboarding
curriculum), or `field-operations/sales-systems/salesforce-config.md` (the literal SFDC schema
— would be useful for a CRM-fields exhibit but was out of time budget for this pass). A
follow-up worker could mine `sales-operating-procedures/retain-and-expand` specifically for
sales-owned expansion-sale process detail relevant to the sales↔success contested seam.
