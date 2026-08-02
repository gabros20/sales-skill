# Raw research — C0 (channel lead gap-fill) — GitLab handbook, the paths C2 left unread

Author: Channel C lead. Date: 2026-08-03.
Purpose: C2's raw (`_raw-c2-gitlab-handbook.md`) closes with a coverage note naming paths it did
not open, two of which are load-bearing for this pack:
`sales-operating-procedures/retain-and-expand.md` (the sales↔success CONTESTED seam) and
`field-operations/sales-systems/salesforce-config.md` (a CRM-fields exhibit). I read them
myself rather than spawn a fifth worker. This file records what changed as a result.

**Commit pinning:** HEAD of `main` re-verified at 2026-08-03 as
`46180fa3686c8baa55f91bf32c6e1d676eefd475` — identical to the commit C2 pinned. Every permalink
in C2's raw therefore still resolves, and the permalinks below share that commit.

**Surface used:** GitLab's public REST API (`/repository/tree`, `/repository/files/:path/raw`)
via `curl`, unauthenticated. Reachability checks for the private repo used `curl` with a Chrome
User-Agent. No WebSearch was used anywhere in this file (it is quota-dead session-wide), so no
null below rests on an empty-looking exhausted search.

---

## 1. CORRECTION to C2 — the Clari reference is NOT unverified. It is public and primary.

C2 graded GitLab's use of Clari as **UNVERIFIED** ("could not confirm against primary source…
treat it as a lead only, not a citable claim", `_raw-c2-gitlab-handbook.md` §3). That grade was
correct given the pages C2 read, but it is superseded: Clari is named, and its forecast
categories described, on a **public** handbook page.

Source: `content/handbook/sales/sales-operating-procedures/retain-and-expand.md` §3.2.3
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/sales-operating-procedures/retain-and-expand.md

> *"#### 3.2.3 Weekly Account Maintenance Activities (SAE/AE)*
> *Below are the **WEEKLY TASK** you'll need to perform within Clari.*
> *- **Clari-Forecast Values (Net New)** - Document regional news, success stories, closed, won,
> and organizational issues*
> *- **Clari-Forecast Value (Renewal)** - Document and discuss field marketing details with your
> patch.*
> *For in-depth training on Clari go to the [Clari for Salespeople Instructional Videos]
> (https://internal.gitlab.com/handbook/sales/sales-forecasting/)."*

**Grade: PRIMARY, verbatim, permalinked.** Supersedes C2 §3's UNVERIFIED grade on Clari.

What this newly establishes, and its precise limits:
- GitLab's forecasting tool is **Clari** (public fact, citable).
- The forecast is split into at least **two streams — Net New and Renewal** — forecast
  separately. That is a real, citable structural fact about how a public company forecasts, and
  it matters to our pack: new-business and renewal forecasts are different objects.
- Forecast maintenance cadence is **weekly**, owned by the SAE/AE.
- **Still NULL:** the actual forecast *categories* (Commit / Best Case / Pipeline / Omitted or
  Clari's own category set), the roll-up process, and any accuracy measurement. The training
  link points at `internal.gitlab.com/handbook/sales/sales-forecasting/`, which C2 verified
  returns 302→403 to a sign-in page. **C2's headline null survives intact** — GitLab publishes
  that it forecasts weekly in Clari across two streams, and publishes nothing about whether the
  forecast is any good.

Also public, same page §3.2.1, a daily SAE/AE activity:

> *"Update the Close Plan and Close Date to ensure you're forecasting accurately"*

Note for the pack: this is an *instruction to be accurate*, not a *measurement of accuracy* —
the exact distinction our forecasting flagship exists to teach. Cite it as an illustration of
the gap, never as evidence GitLab measures forecast accuracy.

---

## 2. NEW EXHIBIT — the sales↔success contested seam, as an operating procedure

Same file, §4. This is the single most seam-relevant GitLab page found in this channel, and C2
did not open it. The charter flags sales↔success as **provisional + CONTESTED** (success runs
the renewal workflow "up to a complex deal that needs negotiation"; sales closes the expansion
sale; Lincoln Murphy's CS-native position carried as contested vocabulary, NOT adjudicated).

GitLab's published division of labour, verbatim:

**CS side owns renewal tracking and the review cadence** (§4.1):

> *"Conduct [Renewal Review Meeting] with SAE/AE. A key part of the customer relationship
> lifecycle is the renewal phase. CSMs must proactively track the renewal dates of their
> customers and align with their Strategic Account Manager (SAE) to ensure that a customer
> renewal takes place.*
> ***At the beginning of each month** a CSM should review their list of accounts in Salesforce
> and note the renewal dates for their accounts. If a renewal date is within six months the CSM
> should schedule two "Renewal Review" meetings with the appropriate SAE and Solutions Architect
> (SA). The first "Renewal Review" meeting should be scheduled five months out from the renewal
> date and the second should be scheduled three months out from the renewal date."*

**Sales side owns the expansion sale itself** (§4.3, §4.3.3):

> *"Once renewal opportunities are identified at the monthly renewal meeting, the SAE/AE should
> conduct in-depth engagements with the customer with a baseline from the account/product tier
> purchased at the original deal closure."*
>
> *"As you did in the Facilitate the Opportunity and Deal Closure, you will need an updated
> customer deck. This consists of an overall deal package to engage the economic buyer… The
> customer deck should be created with the idea that your champion can present it to the
> economic buyer."* — the four required components being current-state usage, an aligned case
> study, a justification carrying "a market thesis on where the market is currently and what
> they'll gain over time by investing now versus waiting," and *"Preliminary pricing proposal
> that aligns with the value GitLab is delivering while taking into consideration the customer's
> budget or financial constraints."*

Grade: **PRIMARY, verbatim, permalinked.**

**Why this matters and how far it may be pushed.** This is a real, published instance whose
shape matches our charter's provisional position: the CSM tracks and triggers the renewal, the
AE runs the buying conversation and puts the price in front of the economic buyer. It is
corroboration by worked example, and it is legitimate to cite as such.

It is **NOT an adjudication** of the contested seam, and must not be presented as one:
- GitLab is one enterprise, sales-assisted, high-ACV company. Murphy's contested position is
  about CS-native and lower-touch motions, which GitLab's SOP says nothing about — the sample
  does not reach the disputed cases.
- GitLab's own text keeps the roles deliberately **parallel, not sequential**: *"the roles and
  responsibilities of the CSM/PSE/AE/SAE run parallel and it is very important that all roles
  work together"* (§ intro). A pack that cited GitLab to draw a hard line would be citing a
  source that explicitly refuses to draw one.
- Expansion *strategy* is decided jointly, not by sales alone (§4.3.2): *"These questions should
  be answered as a team with the SAE/AE, CSM, and SA pulling together data to make an informed
  decision about the account expansion strategy."*

Recommended handling: cite as a worked example of the split, preserve the "run parallel"
sentence alongside it, and leave the contested mark intact.

**Related, also new — CS-side ownership markers our pack must NOT claim** (§2.2, §3.3, §4.1):
time-to-value KPI definitions (Engagement / Onboarding / Infrastructure Ready / First Value at
10% license activation / Outcome Achieved), the Stage Adoption 80%-license-activation bar,
Executive Business Reviews at least annually, and NPS/CSAT twice yearly. These sit on the
success side of the seam. Flagged so we cede rather than collide.

---

## 3. NEW EXHIBIT — a real, public CRM field data dictionary (and a forecast-honesty gem)

C2 guessed `salesforce-config.md` would carry the SFDC schema. **It does not** — see Null 5.1.
The field documentation is one directory deeper.

Source: `content/handbook/sales/field-operations/sales-systems/gtm-technical-documentation/sfdc-booking-metric-fields.md`
Permalink: https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/sales-systems/gtm-technical-documentation/sfdc-booking-metric-fields.md

Published data dictionary with real SFDC API names, verbatim:

| Field | Definition | SFDC API | Replaces |
|---|---|---|---|
| Net ARR | *"The net change to ARR of an opportunity"* | `ARR_Net__c` | iACV |
| ARR Basis | *"Current Subscription ARR (Renewals Only)"* | `ARR_Basis__c` | Renewal ACV |
| Booked ARR | *"Total ARR of Deal (Net ARR + ARR Basis)"* | `ARR__c` | ACV |

Plus Amount / Recurring Amount / True Up Amount / Pro Serv Amount / Other Non-Recurring Amount
and Subscription Start/End Date, each with its API name. The `Replaces` column is itself
teachable: it records a **metric migration** (iACV → Net ARR, ACV → Booked ARR) with the old
names retained, which is exactly the kind of definitional churn that silently breaks a
historical pipeline comparison.

**The forecast-honesty gem** — same page, verbatim:

> | Opportunity Status | Net ARR Source |
> | Sales Assisted - Quoted | Zuora Quote Data |
> | Sales Assisted - Not Quoted | Estimated Net ARR |
> | Web Directs (Current) | Estimated Net ARR -> EOM Manual Process |
>
> *"The goal of this code is populate the Bookings Metrics field on the Opportunity based on
> data from the Zuora Quote family of objects. If Zuora data is not present then use an
> estimated Net ARR amount until the deal is quoted."*

Grade: **PRIMARY, verbatim, permalinked.**

This is a public company documenting that **the dollar value attached to a deal is an estimate
until a quote exists**, with the estimate/actual boundary drawn at a named, checkable event.
Every pipeline total therefore mixes quoted and estimated amounts, and nothing in the number
itself tells you the ratio. That is a strong, permalinked, non-folklore exhibit for the
forecasting flagship — it teaches a real precision limit without needing any vendor's
accuracy claim. Recommend promoting it to a flagship exhibit alongside C2's stage/exit-criteria
set.

---

## 4. Repo identity — GitLab's Salesforce source is PRIVATE (verified, not assumed)

The field-documentation page links its implementation to
`gitlab-com/sales-team/field-operations/salesforce-src` (Apex classes, triggers, tests). If that
repo were public it would be a first-class OSS artifact for this channel — a real company's
complete CRM configuration.

**It is not public.** Verified two ways on 2026-08-03:
- `GET https://gitlab.com/api/v4/projects/gitlab-com%2Fsales-team%2Ffield-operations%2Fsalesforce-src` → **HTTP 404**
- `curl -L` with a Chrome User-Agent against both the project page and the linked
  `ZuoraQuoteClass.cls` blob URL → **HTTP 403** on both.

So the handbook publishes the *data dictionary* and the *file paths of the implementation*, but
the implementation itself is gated. Consistent with the pattern C2 identified: GitLab publishes
process and definitions, not instrumentation or outcomes. Do not cite any `salesforce-src` file
contents — nobody outside GitLab can read them, and a citation to a 403 is not a citation.

---

## 5. NULL RESULTS (each backed by a fetched status code or a grep, never by a search)

1. **`salesforce-config.md` is not a field schema.** Fetched at the pinned commit (HTTP 200,
   4,146 bytes, 50 lines) and read in full: it covers certificate and key management for SFDC
   integrations (`Certificate and Key Management` in setup, self-signed certificate rotation).
   No opportunity fields, no stage definitions. C2's guess that it would serve as a CRM-fields
   exhibit is **disproved** — the useful file is `sfdc-booking-metric-fields.md` (§3 above).
2. **No forecast categories anywhere public.** Grepped the fetched `retain-and-expand.md` for
   commit/best-case/upside/omitted vocabulary — absent. The only category split published is
   Net New vs Renewal (§1).
3. **No forecast accuracy figure.** Nothing in either newly-read file. C2's null stands, now
   with a second file checked against it.
4. **No pipeline coverage ratio.** Absent from both newly-read files; C2's 404-verified null on
   the Pipeline X-Ray and Pipeline Management Tools pages stands. The unverified "3.5x" figure
   remains uncited.
5. **`sales-operating-procedures` tree fully enumerated**, so this is a bounded null rather than
   an unsearched gap. It contains exactly: `_index.md`, `deal-closure.md`,
   `facilitate-the-opportunity.md`, `retain-and-expand.md`, and one subtree
   `engage-and-educate-the-customer/`. I read `retain-and-expand.md` only. **Remaining unread:
   `deal-closure.md`, `facilitate-the-opportunity.md`, and the `engage-and-educate-the-customer/`
   subtree** — these plausibly hold discovery/demo/negotiation process detail relevant to our
   pack's discovery and objection strips. Declared as coverage, not claimed as absent.

---

## 6. What this changes for the channel report

- Clari moves from UNVERIFIED to PRIMARY; the two-stream (Net New / Renewal) weekly forecast
  cadence becomes citable. The forecast-accuracy null is unaffected and, having now survived a
  second and third file, is stronger than when C2 wrote it.
- The estimated-vs-quoted Net ARR table is a new flagship-grade forecasting exhibit that does
  not depend on any vendor claim.
- The sales↔success seam gains a real worked example that corroborates our provisional split
  without adjudicating the contested mark — and the "run parallel" sentence must travel with it.
- One C2 speculation is disproved (`salesforce-config.md`), and one hoped-for OSS artifact is
  verified unavailable (`salesforce-src`, 403/404).
