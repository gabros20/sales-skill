# Outbound and prospecting

Purpose: Own cold outbound and prospecting as a sales discipline — marketing ceded it explicitly —
and give the honest, correctly-sourced version of the three things a reader will get wrong: the
deliverability numbers, whether "email is cooked," and what an AI-outbound policy actually requires.

Read when:
- Building or running a cold outbound or prospecting motion, or evaluating funnel math for one.
- Citing a Gmail/Yahoo deliverability threshold and needing the exact, non-collapsed numbers.
- Deciding whether — and how — to disclose that an outbound message was AI-drafted or AI-sent.
- Evaluating a technique that promises better deliverability and needing to know whether it's craft
  or evasion.

Skip when:
- Deliverability mechanics and consent regimes themselves (SPF/DKIM/DMARC setup, CAN-SPAM/GDPR
  consent bases) — marketing owns this doctrine; this file cites it, never restates it.
- CRM sync or write-path mechanics for outbound sequences — `automation`'s territory; this file owns
  what stages and fields exist, not how they sync.
- An agent runs outbound autonomously, ongoing, without per-message review — the policy here still
  applies but [agentic.md](agentic.md) is the overlay for what changes structurally.
- Which accounts are in scope for outbound in the first place — [icp-and-qualification.md](icp-and-qualification.md).

Inputs: marketing's qualified-demand definition and the ICP funnel stage a contact sits at; marketing's
already-shipped deliverability and consent doctrine.

Produces: an outbound cadence discipline that doesn't overclaim its own funnel math; deliverability
numbers cited with both halves intact; a disclosure rule with its two statutory anchors; a category
rule against manufactured engagement signals that binds tools that don't exist yet.

## Contents
- [Cold outbound is sales's](#cold-outbound-is-saless)
- [The funnel math, honestly](#the-funnel-math-honestly)
- [Deliverability: cite, never restate](#deliverability-cite-never-restate)
- [Email is cooked — contested, not settled](#email-is-cooked--contested-not-settled)
- [The AI-outbound disclosure rule](#the-ai-outbound-disclosure-rule)
- [The evasion-category rule](#the-evasion-category-rule)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## Cold outbound is sales's

Marketing ceded this ground with no hedge word, three times over: *"Three adjacent disciplines belong
to `sales`, not to this pack, and should be named explicitly rather than absorbed by default: revenue
operations, sales enablement (battlecards, objection handling, pricing negotiation guidance), and
cold outbound/prospecting"* (marketing's `surface-b2b-sales-assisted.md:51-53`), and drawn again in
that pack's own `handoff.md:42` and `SKILL.md:107`. Marketing states why, and it matters for how this pack
should read its own differentiation: *"nearly every surveyed competitor pack folds prospecting and
cold-email into 'marketing,' and the family's declared seam is a real differentiator only if it is
drawn here explicitly, not assumed"* (`:54-56`). The same file draws the line precisely at the
handoff: marketing "does not run the outbound sequence or own the CRM pipeline stage" (`:58`). This
pack's job starts exactly where that sentence ends.

## The funnel math, honestly

A rare cold-email post exposes every intermediate conversion rate instead of quoting one headline
number — chained, this is the shape any outbound funnel estimate should take: 500–1,000 leads per
opportunity, 6 opportunities per qualified call, 5 calls per closed deal
(x.com/levikmunneke/status/2083588733228745109). Checking the chained arithmetic against the author's
own stated range is itself the teaching: 500 × 6 × 5 = 15,000 leads per deal at the low end, 1,000 × 6
× 5 = 30,000 at the high end — but the post states the range as "20k–30k." The upper bound is exactly
right; his own numbers imply a funnel one-third better than he claims at the low end. The lesson to
teach is the **chaining method with the reader's own rates**, not the "20k–30k leads per deal" figure
— a funnel quoted from memory drifts even when the author is being honest and shows all their work.
Never ship the specific figure as a benchmark.

## Deliverability: cite, never restate

Marketing owns deliverability doctrine and consent regimes, and has already shipped both:
`marketing/references/lifecycle-and-email.md` §1 ("Deliverability is engineering, not copywriting" —
SPF/DKIM/DMARC, the RFC layer, per-mailbox-provider behavior) and its runnable
`marketing/assets/email-compliance-checklist.md`. Cite those; do not restate them here. What this
file adds is the outbound-specific reading of two numbers that must always travel together for
Gmail, never collapsed to one: **0.30%** is the hard
compliance requirement ("Keep spam rates reported in Postmaster Tools below 0.30%"), **0.10%** is
Google's own recommended target ("avoid ever reaching a spam rate of 0.30% or higher" — stay under
0.10% for margin). Reporting only the first loses the actionable guidance; reporting only the second
overstates the hard requirement. The **5,000/day** bulk-sender threshold
(support.google.com/a/answer/81126, effective 2024-02-01, SPF or DKIM required for all senders,
SPF+DKIM+DMARC for bulk senders) is Google-primary — Yahoo's own page states no numeric volume threshold at
all, so the widely repeated "Google and Yahoo both use 5,000/day" fuses a primary fact with a
secondary-sourced one. Cite the Google number with confidence; attribute the Yahoo figure to secondary
reporting, or don't ship it.

## Email is cooked — contested, not settled

The collapse thesis has a real structural signal behind it and a real first-person counter-exhibit
against it — hold both. Structural: an entire paid product category (dedicated sending
infrastructure, inbox warmup, placement monitoring) exists, which is a revealed-preference signal that
senders pay recurring fees to fight a real deliverability problem — stronger evidence than any single
vendor's headline reply-rate stat, because it's what customers pay for rather than what a vendor
claims. First-person, and the sharper exhibit: *"We went from 0.1% to 1% reply rate in 3 days. (No
auto-replies counted) No new copy. No new offer"* (x.com/harsh_biz/status/2075218419927122424) — a
10× swing with copy and offer explicitly held constant, isolating deliverability as the cause, and
carrying its own denominator caveat unprompted. **The teaching: a reply rate is a deliverability
artifact before it is a copy artifact** — and the 3-day recovery argues against permanent collapse,
not for it. Against the collapse thesis (*"email as a channel is done"*,
x.com/jeffreyhuber/status/2033577620793925656): two practitioners attribute failure to configuration
and offer, not channel death (x.com/NickAbraham12/status/2083915025115201597,
x.com/seanlongden/status/2083627610546864595). Both poles are permalinked, so grade the thesis
**CONTESTED** — and note the asymmetry honestly: the skeptics offer a diagnosis, the collapse side
offers an assertion. Never cite a vendor case-study reply rate (e.g. one vendor's "60–70% positive
reply rates") as a market benchmark; it is one customer's best-case story.

## The AI-outbound disclosure rule

**Disclose the agent, clearly, at first contact.** Two statutes converge on this without a
practitioner debate to referee — nobody on X argues either side of AI-disclosure in sales, so this is
open ground the pack is staking out, not adjudicating. EU AI Act Art. 50(1)
(eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689, PRIMARY, Official Journal text):
providers must ensure people "are informed that they are interacting with an AI system, unless this is
obvious from the point of view of a natural person who is reasonably well-informed, observant and
circumspect"; Art. 50(5) sets the timing — "at the latest at the time of the first interaction or
exposure." California SB 1001 (Cal. Bus. & Prof. Code §§ 17940–17943,
leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=7.&title=&part=3.&chapter=6.&article=,
PRIMARY, statute text) targets bots used "in order to incentivize a purchase or sale of goods or
services in a commercial transaction" — literally AI-SDR conduct — and is a **safe-harbour statute:
disclosure cures liability.** Correct a widely repeated misreading here: the "10 million monthly
visitors" threshold does **not** gate the prohibition — § 17941(a) triggers on communicating "online"
with no threshold at all; the threshold-bearing term "online platform" appears in the operative text
of this chapter in exactly one place, § 17942(c)'s service-provider carve-out. A solo founder running
AI-drafted or AI-sent outbound to EU or California recipients is within scope on the face of both
texts. This mirrors the family's existing AI-disclosure precedent for support agents; the same posture
applies here to outbound.

## The evasion-category rule

**Never manufacture false engagement signals to defeat filtering.** Rule the category, not one prompt
or tool, so it binds tools that don't exist yet. Three independent, unrelated exhibits establish this
is a pattern, not an edge case: **copy-spinning** to defeat fingerprinting — a ready-made prompt
instructing "Take this cold email copy and create 25 variations. Same meaning, different structure.
Vary: sentence order, word choice, punctuation, line breaks" (x.com/seanlongden/status/2083901909979521259)
— same meaning, 25 shapes, offered as personalization when it is detection evasion. **Simulated human
engagement** — a warmup tool that can "scroll on your emails to mimic human behavior," "star your
emails," and "click the links in your email to mark them as safe" for "Perfect email deliverability"
(x.com/NickAbraham12/status/1416026033422315523). **Account farming behind proxies** — 30 accounts run
through proxies "so it keeps real" (x.com/webjuice_ie/status/1801280371771715820). It is a funded industry: one warmup tool alone
"generates 1.2 million a year" (x.com/staticmaker1/status/2046044489593348568). This is the cleanest
available statement of where this pack's AI *policy* differs from `ai`'s *mechanics*: `ai` owns how to
generate 25 variants of a message; this pack owns whether you should. **Decline to teach the
technique**; cite the exhibits as the boundary instead.

## Validation

- [ ] No cold-outbound or prospecting content is absorbed silently into a marketing deliverable —
      it's named and routed here.
- [ ] Any Gmail spam-rate citation carries both 0.30% and 0.10%, never one alone.
- [ ] "5,000/day" is attributed to Google as primary; attributed to Yahoo only as secondary, or
      omitted for Yahoo.
- [ ] The "email is cooked" thesis is presented as contested, not settled in either direction.
- [ ] Any AI-outbound disclosure statement names both the EU AI Act Art. 50 timing rule and California
      SB 1001's safe-harbour structure, and does not repeat the false 10M-visitor exemption.
- [ ] The evasion-category rule is stated as a category, not tied to one prompt or vendor.

## Failure modes and handoff

- **Restating marketing's deliverability or consent doctrine instead of citing it** — cite the shipped
  strip; this pack adds outbound practice and policy, not the underlying tutorial.
- **Shipping "20k–30k leads per deal" as a benchmark** — teach the chaining method with the reader's
  own rates instead.
- **Collapsing the Gmail spam-rate guidance to one number**, or fusing the Google and Yahoo bulk
  thresholds into one claim.
- **Treating "email is cooked" as settled** in either direction — it's contested, with permalinks on
  both poles.
- **Teaching a copy-variation or engagement-simulation technique without naming it as evasion** — the
  category rule exists precisely so a new tool doesn't slip past it.
- **The real ask is CRM sync mechanics for the outbound sequence** → `automation`.
- **The real ask is agent mechanics, prompt design, or generating message variants** → `ai`; this file
  only owns whether to.
- **An agent is running the outbound motion unattended** → [agentic.md](agentic.md).
