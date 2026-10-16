# Agentic (Additive Overlay)

Purpose: State what changes when an AI agent runs prospecting, qualification, or a deal motion
itself — deciding and sending — without a human reviewing each instance. **This is an overlay**: it
stacks on [outbound-and-prospecting.md](outbound-and-prospecting.md)'s disclosure rule and
evasion-category rule, and on [icp-and-qualification.md](icp-and-qualification.md); it never replaces
either. Nothing about the underlying policy changes because a model runs the loop — if anything, an
agent that can contact prospects faster than a human reviews it makes the disclosure and evasion
rules more load-bearing, not less.

Read when:
- An AI SDR or agent drafts, sends, or follows up on outbound without per-message human review.
- Evaluating an AI-SDR vendor's claims before adopting or citing them.
- Deciding what autonomy ceiling to grant an agent running any part of a sales motion.
- A model scores leads or triages replies and decides which ones reach a human.

Skip when:
- A human reviews and approves each agent-drafted message before it sends — that's the base policy
  in [outbound-and-prospecting.md](outbound-and-prospecting.md), not this overlay.
- The question is retrieval, prompt design, the agent's turn loop, or eval methodology — that's `ai`'s
  territory throughout; this file owns policy, not mechanics.
- The question is a deterministic ceiling on a non-sales agentic step (an experiment, a support
  agent) — see growth's, success's, and automation's own agentic overlays; this file scopes to sales
  motions specifically.

Inputs: the disclosure rule and evasion-category boundary already set in
[outbound-and-prospecting.md](outbound-and-prospecting.md); which decisions in a sales motion
(prospecting, follow-up cadence, qualification, first-contact messaging) are model-decided rather than
human-approved per instance.

Produces: an honest reality check on AI-SDR vendor claims; the disclosure rule enforced as
configuration rather than left to prompt discretion; a structural ceiling on unattended agent action.

## Contents
- [AI-SDR reality, honestly](#ai-sdr-reality-honestly)
- [Disclosure becomes structural, not instructional](#disclosure-becomes-structural-not-instructional)
- [Guardrails for autonomous outbound](#guardrails-for-autonomous-outbound)
- [Model-scored qualification](#model-scored-qualification)
- [The evasion rule binds tools that don't exist yet](#the-evasion-rule-binds-tools-that-dont-exist-yet)
- [Where mechanics live](#where-mechanics-live)
- [Validation](#validation)
- [Failure modes](#failure-modes)

## AI-SDR reality, honestly

Every AI-SDR vendor claim — Artisan, 11x, Clay, Regie.ai, AiSDR, Qualified — grades
VENDOR-SELF-REPORTED. The one case an outside party actually checked did not hold up: TechCrunch
(2025-03-24,
https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/),
drawing on "nearly two dozen sources," found 11x displaying customer logos for companies
that were not customers. ZoomInfo ran only a one-month trial and is on record: *"We did not give them
permission to use our logo"*; the product *"performed significantly worse than our SDR employees."*
Airtable: *"It was never used in production and never rolled out to our sales team"* — yet its logo
kept appearing after the denial. **Never cite one side of a contested pair alone**: ARR "approaching
$10M" (company) vs. ~$3M (employee source); retention 79% (company) vs. "losing 70–80% of customers"
(employee source) — both figures sit in the same article. AI-SDR market-size figures are unsourced
and **never ship**.

The standing, unanswered challenge belongs in this pack as the evidentiary bar: *"I've still yet to
see a real world example where an AI SDR agent has booked a qualified call"*
(x.com/salesxsaas/status/2019037210805403922). Cite it as an open challenge nobody in this research
met — not as proof AI-SDR doesn't work, just as proof nobody has shown that it does at the bar the
challenge sets. The same account's dog-that-didn't-bark observation is a separate, checkable diligence
heuristic worth teaching on its own: *"every AI SDR company still uses human SDRs to sell their own
product"* (x.com/salesxsaas/status/2080037249631076775) — distinct from the unsourced market-size
figure attached to the same post, which never ships.

## Disclosure becomes structural, not instructional

[outbound-and-prospecting.md](outbound-and-prospecting.md)'s rule — disclose the agent, clearly, at
first contact — is written for a human sending AI-drafted outbound. Once an agent sends without
per-instance review, the same move the family's other agentic overlays make applies here:
**pre-commit the rule before the run, enforce it structurally, not by instruction.** A disclosure
line a prompt merely "should" include is unaudited by construction. Require it as a field the agent
cannot omit from a first-contact message — the same pattern as a required, logged typed field
elsewhere in the family for auditable agent decisions — and log every send against it, so disclosure
compliance is reviewable after the fact, not just hoped for at generation time.

Published autonomous pitch pipelines build the inverse. A second-hand account quotes an orchestrator
prompt whose checker agent "runs every message through evals for personalization, absence of AI
markers and buzzwords before sending" (x.com/browomo/status/2051747188787523825); a published
outreach-agent prompt sets "Tone: Casual, not salesy, like a human wrote it"
(x.com/HamptonAc_/status/2024846643586031966, article). An eval that scores the absence of AI
markers is non-disclosure enforced as configuration — this section's own mechanism, pointed the other
way. A tone check is fine; a check whose pass condition is that the recipient cannot tell is a
concealment gate, and the disclosure field outranks it.

## Guardrails for autonomous outbound

- **A volume ceiling** on how many prospects per day an agent may contact unsupervised, enforced by
  the sending platform's own rate control — not a prompt asking the agent to pace itself.
- **A kill switch independent of the agent's own reasoning**, able to silence a campaign or account
  from outside its decision loop.
- **A human review gate** before an agent-initiated conversation advances past first contact into
  anything binding — pricing, contract terms, a scheduled call the agent alone confirmed. Cite
  [proposals-pricing-and-negotiation.md](proposals-pricing-and-negotiation.md) and automation's own
  fail-closed irreversible-action gate (`automation/references/approval-and-authority.md:109`) for
  the mechanism; don't re-derive an approval workflow here.
- **Escalation tripwires live outside the loop too.** The same orchestrator wakes its owner only when
  a deal crosses a dollar threshold or a niche's daily reply rate drops below a floor (browomo,
  above) — a sensible pair of triggers, written into the agent's own prompt, which is exactly where
  this list says a guardrail must not live. Neither fires on disclosure, which is settled before
  first contact, not after a metric moves.

## Model-scored qualification

A model that scores leads and passes only those above a cutoff — "Score 1-10 based on: Budget
likelihood … Need likelihood … Timing … Only pass leads scoring 7+ to outreach" (HamptonAc_ article,
above) — is deciding who gets contacted, so this overlay applies. The cutoff is a hand-set assumption
with a runtime, the same species as a stage weight: log every score beside its outcome and check it
with the predict-then-score loop ([forecasting-honesty.md](forecasting-honesty.md) §6) before trusting
it. The same article reports a conversion jump for a user who "only took calls with 8+ scores";
taking fewer calls shrinks the denominator, so a higher rate among calls taken says nothing about
whether more deals closed — ask for closed deals per lead scored. Reply triage by model score ("All
three channels land in one master inbox, get AI scored, and route by tier",
x.com/coldemailchris/status/2068098788934266953) is the same decision one step later: a tier that
never reaches a human is an unreviewed qualification call.

## The evasion rule binds tools that don't exist yet

[outbound-and-prospecting.md](outbound-and-prospecting.md)'s rule against manufacturing false
engagement signals to defeat filtering applies with more force to an autonomous agent, because an
agent can produce the evasion at a volume and consistency a human copy-pasting cannot. The rule is
written against the *category* — copy-spinning, simulated engagement, account farming, manufactured
reply signals — specifically
so it still binds a capability that doesn't exist yet. An agent framework offering "vary this message
N ways to avoid detection" is offering evasion tooling regardless of how the feature is marketed; this
overlay does not carve out an exception for agent-native versions of the same three exhibits.

## Where mechanics live

`ai` owns retrieval, prompt design, the agent loop, and eval instrumentation for any agent operating
in a sales motion. This overlay owns the policy question — whether an agent may act unsupervised,
what it must disclose, and what it may never do to defeat a receiving system's filters.
`louisblythe/sales-skills` (122 skills, **no license file — cite only, never lift**) is the deepest
AI-SDR-mechanics treatment found in this research: bot behaviors like voicemail-drop-optimization,
ghost-recovery, and response-latency-management. Useful as a map of what "mechanics" covers; not
content to adapt.

## Validation

- This overlay is stacked on a named base surface, never used as one.
- Disclosure is enforced as a required, logged field the agent cannot omit — not as prompt wording.
- Every AI-SDR vendor figure ships VENDOR-SELF-REPORTED, and every contested pair ships both halves.
- The volume ceiling, kill switch, and escalation tripwires sit outside the agent's own reasoning
  loop.
- No checker in the send path passes on the recipient being unable to tell an AI sent the message.
- A model-set qualification cutoff is labelled an assumption and logged beside outcomes.
- The evasion-category rule is applied to the capability, not to the named tool that implements it.

## Failure modes

- Citing an AI-SDR vendor's ARR or retention claim without its contested counter-figure from the same
  source.
- A disclosure line left to prompt discretion rather than a required, logged field.
- Treating salesxsaas's unanswered challenge as proof AI-SDR doesn't work, rather than as a bar
  nobody in this research met.
- Teaching a "vary the message" or "simulate engagement" capability without naming it as the evasion
  category it is, because an agent generated it rather than a human.
- A volume or kill-switch guardrail enforced only by prompt instruction rather than the platform's own
  control — the same gap the family's other agentic overlays flag as the highest-consequence one.
- A "sounds human" or "no AI markers" gate in the send path — concealment configured as quality.
- Reading a higher conversion rate among calls taken as proof a lead score works — the denominator
  moved.
- The real ask is agent mechanics, retrieval, or eval design → `ai`.
