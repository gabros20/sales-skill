# ICP and qualification

Purpose: State how account selection works once marketing has defined who the ideal customer is —
sales inherits that definition rather than redrafting it — and give the qualification-framework
landscape its correct evidence grades: which named frameworks exist, what they actually claim, and
the current legal status of the one that just went through federal court.

Read when:
- Deciding which named accounts get sales attention, and needing the ICP definition to filter by.
- Ordering accounts that already fit by evidence of timing, or weighting a lead score.
- Choosing whether to impose a qualification framework (MEDDIC/MEDDPICC/BANT) on a deal, or deciding
  one isn't warranted yet.
- Citing a named methodology and needing to know whether it's a qualification framework or a selling
  method — the two get conflated constantly, including in this pack's own source corpus.
- Citing MEDDPICC/MEDDICC and needing the current trademark and litigation status.

Skip when:
- Defining ICP from scratch — that's marketing's job
  (`marketing/references/audience-and-segmentation.md`); this file only applies an existing
  definition to account selection.
- The actual discovery conversation and its evidence base — [discovery-calls.md](discovery-calls.md).
- Whether a sales motion should exist at all for this business — [when-sales-applies.md](when-sales-applies.md).
- Enterprise-scale qualification mechanics at ARR-gated thresholds — [surface-enterprise-team.md](surface-enterprise-team.md)
  carries the full operationalization; this file carries the exhibit and the ruling.

Inputs: marketing's ICP-as-funnel model (already defined, not re-derived here); the account list a
reader wants to prioritize; whatever surface the reader is on (founder-led-solo vs enterprise-team
changes how much qualification structure is proportionate).

Produces: an account-selection filter keyed to marketing's existing ICP stages, ordered by timing
signals scored with stated discipline; a qualification
framework choice — or an explicit, defensible decision to skip one — with its evidence grade stated;
disambiguated vocabulary that keeps "framework" and "method" from collapsing into each other.

## Contents
- [ICP is inherited, not redefined](#icp-is-inherited-not-redefined)
- [Timing signals: which fitting accounts to contact now](#timing-signals-which-fitting-accounts-to-contact-now)
- [Frameworks and methods are not the same category](#frameworks-and-methods-are-not-the-same-category)
- [MEDDIC/MEDDPICC: evidence and legal status](#meddicmeddpicc-evidence-and-legal-status)
- [GitLab's MEDDPPICC — the enterprise exhibit](#gitlabs-meddppicc--the-enterprise-exhibit)
- [The reproduction hazard](#the-reproduction-hazard)
- [Qualification-first vs. friction-gate](#qualification-first-vs-friction-gate)
- [What discovery evidence does not validate](#what-discovery-evidence-does-not-validate)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## ICP is inherited, not redefined

Sales does not own the definition of "ideal customer." Marketing does, and treats it as a funnel, not
a checkbox: **aware → interested → considering → chosen → enterprise-adopted**, with channel
(PLG, outbound, SEO, paid, sales-assisted) secondary to whether the funnel actually reaches and
converts the right profile at every stage. This is a named-practitioner framework (Kyle Poyar,
2024-07-25) — a useful lens, not an evidence-graded law, and marketing already carries that caveat.
Sales's job is narrower and later: take that funnel and apply it to **account selection and
prioritization** — which named accounts have reached "considering" or later, and therefore warrant
sales attention, not which criteria make an account fit in the first place. Product's own router
confirms the split cleanly, ceding "qualification and CRM to `sales`" without qualification — the
only unqualified, non-provisional cession to sales found anywhere in the family's routing tables.

This is the single most likely place a sales build accidentally contradicts a shipped sibling, because
"ICP" and "qualification" sound like the same job seen once. They are two ends of the same funnel:
marketing defines fit and drives a contact into it; sales reads the funnel stage and decides which
accounts already in it earn attention now. **Never draft a new ICP definition inside a sales
deliverable** — if the funnel stage a contact should be filtered at isn't clear, that's marketing's
segmentation model to consult, not a gap to fill here.

Two vocabulary notes follow: spell out **"sales-qualified lead"** on first use rather than the bare
initialism, and treat "qualification" as fine internally but not as customer-facing journey
vocabulary — design has already ruled a "Lead Qualification"-named step unfit for a journey-phase
name, and surfacing the word to a buyer repeats that mistake.

## Timing signals: which fitting accounts to contact now

Marketing's funnel says who fits; it does not say whom to contact this week. That ordering — which
fitting accounts show evidence of having reached "considering" — is sales's, and published practice
converges on **timing** evidence an outsider can see. Three classes, each
OPINION or VENDOR-SELF-REPORTED, none with a measured lift:

- **A stated need** — a public request for a recommendation or an alternative ("anyone got
  recommendations for [service]", x.com/scaling_shields/status/2042324679759978780); an owner asking for help in a local group
  (x.com/everestchris6/status/2069504396501926262).
- **Dissatisfaction with the incumbent** — a recent negative review of a competitor
  (x.com/scaling_shields/status/2037983111091491225).
- **Spend already in motion** — paying for the adjacent thing (prospects already running ads, who
  "were already spending money on marketing", x.com/axtalks/status/2071239871298207770), or hiring
  into the function you sell to (an opener built on a hiring post,
  x.com/NickAbraham12/status/2086451710617162198; "the listing is the buying signal",
  x.com/dimitarangg/status/2081968140083482917).

A hand-raise opens the discovery call; it does not replace it. "the declaration is the qualifier"
with "no discovering pain points" (scaling_shields, above) mistakes a stated need for a decision
process — the post names a problem, not who signs, how they buy, or what else they are weighing.
Using the signal in the message is [outbound-and-prospecting.md](outbound-and-prospecting.md)'s.

**Four checks before any signal weight ships:**
1. **A decay signal is not a demand signal.** A page unchanged for years reads at least as well as
   evidence nobody is trying to change it as evidence of suppressed demand. Weight evidence of
   recent action (how often the account acts), not time since it last acted — a reasoning check; no
   outcome measured.
2. **Check how often a signal fires before weighting it.** One that fires on almost nobody in the
   pool ranks nobody; one that fires on almost everybody belongs in marketing's fit filter, not the
   timing score — also a reasoning check.
3. **A hand-set weight is an assumption with a runtime** — the same species as a stage weight; log
   it and score it against outcomes ([forecasting-honesty.md](forecasting-honesty.md) §6). A
   data vendor's industry filter is a fit guess too: a short human check before contact catches the
   misfiled account.
4. **Segment-versus-segment reply rates at founder volume hit the small-numbers gate**
   ([forecasting-honesty.md](forecasting-honesty.md) §5); designing that comparison is an experiment,
   which is `growth`'s — sales owns the account-selection call it informs.

**A prospective partner's footprint is a partner list, not a prospect list.** Accounts harvested
from a channel partner's public work — an agency's portfolio credits, say — are that partner's
customers; prospecting them while courting the partner poisons the partner deal. The Partner letter
in GitLab's MEDDPPICC (below) is the qualification-side home for that landscape.

## Frameworks and methods are not the same category

MEDDIC, MEDDPICC, and BANT are **qualification / deal-health frameworks** — checklists for whether a
deal is worth pursuing and where it stands. SPIN, Challenger, and Sandler are **selling methods** —
how a rep runs the conversation itself. The research corpus this pack draws on files them together
routinely, including its own methodology raw file; treating a qualification checklist as if it were a
selling method is a category error, and a pack that repeats it teaches the wrong lesson to a reader
trying to decide which one they actually need.

A framework vendor's own practitioner community makes the same correction independently: *"MEDDPICC is
not a sales methodology. MEDDPICC is a deal qualification and deal health framework. If you tell your
reps 'follow the steps in MEDDPICC' without giving them the skills to do it? You're destined for some
disappointing pipeline reviews"* (x.com/Chris_Orlob/status/1972230446781227215). Contrast the genre
this pack should not repeat — a framework vendor's own account asserting a forecast-accuracy benefit
with no evidence attached: *"You can't forecast when you're not aligned. Partner-sourced pipeline
without MEDDPICC can be unpredictable. ❌ No Champion = no internal voice… ❌ No process = no
predictability"* (x.com/meddpicc/status/1965397852869275721) — a CONFOUNDED claim, cited here as the
shape to avoid, not as support.

Practitioner opinion on all of these is genuinely split, and individuals move within it — never claim
a consensus in either direction. One account posted *"I agree with many sensible sales methodologies:
1) Sandler 2) GAP selling 3) SPIN selling"* (x.com/BowTiedSalesGuy/status/1459230799283339272, 2021)
and, fourteen months later, *"BANT MAN FAB MEDDIC / NGMI"*
(x.com/BowTiedSalesGuy/status/1542578172188819456, 2022) — same person, opposite positions. **Never
describe Sandler or Gap Selling as "research-backed" or "debunked"** — neither makes an empirical
claim to evaluate in the first place, which is a different, quieter null result than SPIN's (an
unpublished 35,000-call study) or MEDDIC's (no study located at all).

## MEDDIC/MEDDPICC: evidence and legal status

No published empirical study of MEDDIC exists — searched to exhaustion, found nowhere. Its origin is
internal pattern-analysis at Parametric Technology Corporation (PTC), **early 1990s**; in **2005**,
former PTC employees coined the extended MEDDPICC, adding Paper Process and Competition. This dating
comes from the best available primary source: a 2026 federal court opinion, not vendor lore.

**MEDDICC LTD. v. 01 CONSULTING LLC**, No. 2:24-cv-01836 (E.D. Pa.), Opinion ECF 99 and Order ECF 100,
filed 2026-04-21, Chief Judge Wendy Beetlestone — cite the opinion, never the winning party's press
release, which foregrounds its own expert and omits that he was excluded (see below). The holding: a
jury "would be compelled to find" that **MEDDPICC is a generic term for business education services
and content** — always carry that qualifier; this is not a ruling that the word is generic in the
abstract. The order directs the PTO to cancel Registration No. 6,489,058. **Two corrections that must
travel with any citation of this case:** it is not a clean win and the case is not over — the order
states the motion "is DENIED in all other respects," summary judgment was "granted in part and denied
in part," and tortious-interference and trade-libel claims survive with a briefing schedule set (last
known docket activity 2026-07-16) — never describe this as concluded. And **John McMahon's expert
testimony was excluded**, not relied upon — the order granted a motion to exclude him across nine
enumerated topics; the genericness holding rests on the court's own analysis, not his testimony. A
press-release-sourced account inverted this exact point; the opinion itself corrects it.

**MEDDICC** (the commercial mark, Andy Whyte, founded 2020) remains live and commercial — cite it,
never reproduce its training materials. "MEDDIC," the original six-letter acronym, was never shown in
this research to be currently trademark-registered to anyone. No academic critique of MEDDIC exists
either — a null in its own right, distinct from Challenger, which did attract a real peer-reviewed
critique (Rapp, Bachrach, Panagopoulos & Ogilvie, 2014, *JPSSM* 34(4):245–259).

## GitLab's MEDDPPICC — the enterprise exhibit

GitLab publishes its own qualification framework in full, letter-by-letter, as handbook prose (CC
BY-SA 4.0 — quotable with attribution): **MEDDPPICC** — nine letters, two D's and two P's, confirmed
against the page's own section headers, not against a search summary. Metrics — "the economic impact
of the solution." Economic Buyer — "the individual within the customer's organization who is required
for the final 'yes.'" Decision Process — "the process and timeline by which the customer will
evaluate, select, and purchase a solution." Decision Criteria — "the formal solution requirements
against which each participant in the decision process will evaluate (includes the technical and
financial lens with which the customer views GitLab)." Partner — "the process of validating the
partner landscape and opportunity implications." Paper Process — "the process by which the customer
will document and execute the process of purchasing (including the MSA, order form, PO, etc.)."
Identify Pain — "the problems created by the customer's current state (nobody buys until there is
pain!)." Champion — "the person(s) with power and influence inside the customer's organization who
are actively selling on your behalf and willing to give you inside information to help you win the
deal." Competition — "competitive strengths, weaknesses, and differentiators, including competitor's
champions" (gitlab.com/gitlab-com/content-sites/handbook, `content/handbook/sales/meddppicc.md`).

It is operationalized as **9 discrete Command-Plan fields**, required only above a stated ARR
threshold — **$100K+ for Enterprise, $50K+ for Mid-Market**
(`content/handbook/sales/command-of-the-message/command-plan.md`) — which is exactly
[surface-enterprise-team.md](surface-enterprise-team.md)'s territory, not this pack's founder-led-solo
default. GitLab's own qualifying-question banks per letter are **not reproduced here** — they shade
into the trademarked methodology's actual training content even though GitLab itself published them;
cite the nine-letter expansion and gloss above, paraphrase or omit the rest.

## The reproduction hazard

GitLab redacted a third party's methodology itself: its handbook states it adopted Force Management's
Command of the Message, then *"Due to IP constraints, we have migrated content from this page to
GitLab's internal Handbook"* — an incumbent independently reaching the cite-never-reproduce posture
this file follows. The cautionary counter-example: `github/awesome-copilot`'s
`skills/gtm-enterprise-account-planning/SKILL.md` (MIT, 37,357★) reproduces MEDDICC letter-by-letter —
Metrics, Economic Buyer, Decision Criteria, Decision Process, Identified Pain, Champion, Competition —
as a first-class "Core Framework," zero attribution to MEDDICC Ltd or PTC. Contrast
`refoundai/lenny-skills`, which reproduces MEDDIC's six letters but cites an external source —
meaningfully lower risk from the same act. **Name a framework, cite it, teach evidence about it; never
reproduce its content as though it were original.**

## Qualification-first vs. friction-gate

A founder-led-solo reader may not need a named framework at all. [surface-founder-led-solo.md](surface-founder-led-solo.md)
carries patio11's purchasing-friction argument in full — pricing itself can obviate formal
qualification. A lighter alternative that imports no branded framework: KyleAsay's three **negative**
exit criteria — no velocity, no concerns ("no concerns often means no consideration"), no
next-best-option — reasons to *refuse* forecasting a deal rather than a checklist to qualify it in
(full primitive in [forecasting-honesty.md](forecasting-honesty.md)). A solo reader can run on
negative criteria alone; GitLab's nine-field Command Plan becomes proportionate only once a deal
clears the enterprise ARR threshold above.

## What discovery evidence does not validate

Real peer-reviewed evidence shows question-asking builds rapport — but in **non-sales dyads**
(speed-dating, get-to-know-you conversations), not sales discovery calls. No published evidence shows
any *branded* sales questioning methodology improves win rates, and a qualification or discovery
framework may never borrow the rapport papers' authority to imply that second, different claim. Full
treatment: [discovery-calls.md](discovery-calls.md); this file only flags the boundary.

## Validation

- [ ] ICP language points back to marketing's existing funnel definition; no fit criteria are
      redrafted inside this pack.
- [ ] Every timing-signal weight passes the four checks, and a hand-raise is never treated as a
      completed discovery call.
- [ ] MEDDIC/MEDDPICC/BANT are named as frameworks; SPIN/Challenger/Sandler as methods — never
      conflated, never presented as one category.
- [ ] Any MEDDPICC legal-status reference cites the opinion (ECF 99/100), carries "generic for
      business education services and content," and states the case is live, not concluded.
- [ ] No qualifying-question bank is reproduced verbatim from GitLab or any incumbent framework.
- [ ] No claim of practitioner consensus on a named methodology, in either direction.
- [ ] "Sales-qualified lead" is spelled out on first use; "qualification" does not appear as
      customer-facing journey vocabulary.

## Failure modes and handoff

- **Redefining ICP inside this pack** — route to marketing's segmentation model; this file only
  applies an existing definition to account selection.
- **Scoring staleness as demand**, or weighting a signal that fires on everyone — run the four
  checks under "Timing signals."
- **Prospecting a prospective partner's clients from its portfolio** — that list is the partner's.
- **Treating the MEDDPICC ruling as concluded** — restate its live-case, partial-summary-judgment
  status every time it's cited.
- **The reader wants the actual discovery-call technique**, not the qualification checklist that
  precedes it → [discovery-calls.md](discovery-calls.md).
- **The reader is enterprise-tier and needs full Command Plan / buying-group mechanics** →
  [surface-enterprise-team.md](surface-enterprise-team.md).
- **A framework feels like overkill for a solo reader** →
  [surface-founder-led-solo.md](surface-founder-led-solo.md) plus the negative-criteria primitive in
  [forecasting-honesty.md](forecasting-honesty.md).
