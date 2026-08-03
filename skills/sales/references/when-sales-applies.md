# When Sales Applies

Purpose: Decide whether an assisted sales motion is worth running at all — and if so, what kind —
before writing a single outbound sequence, CRM stage, or forecast. No source in the founder-led
canon agrees on the test; this pack teaches the disagreement rather than picking a winner.

Read when:
- A request assumes a sales motion should exist and hasn't justified that yet — cold outbound, a
  CRM build, a forecast, or a "hire an SDR" plan is being asked for on a product that may not need
  one.
- Someone asks "do I need sales" or "when do I stop selling self-serve and start selling
  sales-assisted."
- A request wants enterprise sales-team vocabulary (quota, AE, SDR) applied to a solo or
  self-serve product before checking whether the product's price point and buyer even require it.

Skip when:
- The existence question is already settled and the request is about a specific job — go to
  [icp-and-qualification](icp-and-qualification.md), [outbound-and-prospecting](outbound-and-prospecting.md),
  [discovery-calls](discovery-calls.md), or the other job references.
- The request is about which *sibling* handles a post-sale motion (renewal, retention experiment,
  onboarding) — those are success's, growth's, and success's respectively; see
  [handoff](handoff.md).

Inputs: current ACV/ARPA, whether pricing already requires a live human conversation, whether
purchasing at the target account routes through a corporate card or a procurement/PO process, and
how many customers have been closed so far.

Produces: a named verdict — self-serve-only, PLG-with-a-sales-handover-threshold, or
sales-assisted — attributed to the gate(s) that produced it, plus which surface reference to read
next.

## Contents

- [The four gates that disagree](#the-four-gates-that-disagree)
- [The gate moving from below](#the-gate-moving-from-below)
- [The decision-already-made genre](#the-decision-already-made-genre)
- [The complexity moat, and its own falsification condition](#the-complexity-moat-and-its-own-falsification-condition)
- [The PLG boundary: a usage threshold, not a demand signal](#the-plg-boundary-a-usage-threshold-not-a-demand-signal)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## The four gates that disagree

No canonical source resolves "should a sales motion exist at all." Four serious, independently
arrived-at practitioner positions answer it with four **incompatible gate types** — a stage gate,
a price-tier gate, a purchasing-friction gate, and a founder-effort gate that isn't really about
sales-motion existence at all. **The disagreement is the finding**: a pack that adopts only one of
these will misfire for a reader whose situation fits a different gate. All four are
**SECONDARY / practitioner doctrine**, not measured evidence.

| Gate type | Who | The rule |
|---|---|---|
| **Stage gate** (count + ARR) | Jason Lemkin | Founder closes the first 10–20 customers personally — "This is non-negotiable—even if you hate sales"; transition happens around ~$1M ARR; **hire two reps, not one**, before any head of sales |
| **Price-tier gate** | Christoph Janz | Elephants ($100k+ ARPA) / deer ($10k+) / rabbits ($1k+) / mice ($100+) / flies ($10+) — the tier decides whether human sales is viable at all; "cold calling usually doesn't work at this ARPA level" (rabbits) |
| **Purchasing-friction gate** | Patrick McKenzie (patio11) | The gate is **billing approval, not deal size** — price a plan between $250 and $499/mo specifically to stay under corporate-card/PO-approval thresholds, "evading the internal purchasing controls" that would otherwise force a sales motion even at an enterprise-equivalent price |
| **Founder-effort gate** | Paul Graham | Not about motion existence at all — founders must recruit and serve users by hand regardless of channel: "You can't wait for users to come to you. You have to go out and get them." |

Sources: Lemkin — saastr.com/what-are-the-best-ways-to-transition-from-the-founder-led-sales-stage/
and saastr.com/should-a-startup-founder-handle-sales-when-first-getting-started/ ("The answer is
yes – 95% of the time"). Janz — christophjanz.blogspot.com/2014/10/five-ways-to-build-100-million-business.html.
McKenzie — training.kalzumeus.com/newsletters/archive/enterprise_sales. Graham —
paulgraham.com/ds.html.

**Cross-citation trap, not two independent confirmations:** Janz's own post quotes Lemkin's
enterprise-economics argument "from memory" inside the elephants tier. Citing both as separate
corroboration overstates the agreement — it is one voice appearing in two places, not two voices
converging.

**Reading the gates against each other, concretely:** a $40/mo product with an enterprise-only
compliance ask is "mice, no sales needed" under Janz's tiers and "you may still need a
sales-assisted upsell path for the compliance-asking segment even at a low sticker price" under
McKenzie's friction gate. Both are right, about different axes. Ask which axis is actually binding
for the product in front of you — ARPA tier, purchasing process, or founder bandwidth — rather
than defaulting to whichever gate is most familiar.

**Licensing note:** Founding Sales (Pete Kazanjy) and Chaotic Flow (Joel York) are both
all-rights-reserved despite being free to read online — cite and link, never reproduce or closely
paraphrase.

## The gate moving from below

The four gates above assume the gate is stable once set. It is not. @Shpigford, 2026-06-16
(https://x.com/Shpigford/status/2066881769027047658):

> "if you still require an enterprise sales call to give pricing, you're going to be eaten alive in
> the long run. in most cases, clever engineers just need a day or two w/ AI to build the exact
> part of your product they need. they can literally build it before you can hop on call"

Grade: OPINION, first-person practitioner claim, no measurement attached. What it adds: an
argument that gating pricing behind a sales call is being **eroded from below** by
build-it-yourself economics for buyers who are themselves engineers — the existence gate is a
moving target, not a fixed threshold you set once and revisit never. Treat this as a pressure to
account for, not a resolved forecast; no source in this corpus measures how fast or how far the
erosion runs.

## The decision-already-made genre

The claim that the buyer has largely decided before sales gets involved is the most-repeated
argument in this territory, and it arrives in at least three numbers doing one rhetorical job:
"57% of the buying decision happens before you talk to sales," "9 in 10 buyers rule a firm out
before contact," and "70–80% of the outcome is determined before you arrive." **One of the three has
a real primary.** The "9 in 10" figure traces only to industry marketing blogs (Hinge Marketing,
Archmark, ArchDaily) — not a primary study — and the "70–80%" figure has no traceable source at all
— which is why the useful skill here is recognising the shape in published material, not debunking
any single figure.

The 57% traces cleanly. CEB Marketing Leadership Council, in partnership with Google, *The Digital
Evolution in B2B Marketing* (2012), surveyed more than 1,500 customer contacts across 22 large B2B
organizations in 10 industries
(https://www.thinkwithgoogle.com/_qs/documents/677/the-digital-evolution-in-b2b-marketing_research-studies.pdf,
PRIMARY, read in full):

> "In a striking finding, the survey revealed that the average customer had completed more than
> one-half of the purchase decision-making process prior to engaging a supplier sales rep directly
> (Figure 1). At the upper limit, that number ran as high as 70% (Figure 2)."

Figure 1 gives the exact number, 57% complete, sourced to CEB's own 2011 customer-purchase survey.
**Three things get lost downstream, and each changes what the figure means.** It is
*self-reported progress through a decision process* — not a decision already made; the paper's own
average leaves 43% still to run. Its cutoff is specifically a *supplier's sales rep*, not any
contact with the supplier, so visiting a website is on the near side of the line. And the 70% is the
maximum of a *supplier-level* average across the 22 organizations, a materially different quantity
from "the average buyer" — which is how a legitimate finding becomes a bigger, wronger number.

Two further mutations are worth recognising on sight: the study gets misattributed to **Gartner**,
which acquired CEB in 2017, five years after publication; and Gartner's separate "buyers spend 17%
of their time with suppliers" figure gets cited as corroboration when it measures *time allocation*,
a different quantity entirely (same lead researcher, and the live page no longer carries it).

**How to use this here:** the genre is a real pressure on the existence gate — it argues the
buying conversation starts later than a seller assumes — and it points the same direction as the
erosion above. Cite the CEB primary with its subject attached if the point needs a number at all.
Never cite the derivatives, and never treat any of the three as evidence that a sales motion is
unnecessary; none of them measures that.

## The complexity moat, and its own falsification condition

The counter-pressure, from the seller's side. @arvidkahl, 2025-06-14
(https://x.com/arvidkahl/status/1933686087462830355):

> "I have the nagging feeling that low-price commodity SaaS (social schedulers, calendar link
> tools, job site generators) will be almost completely absorbed by people's vibecoded solutions."

The tweet continues into a sentence naming what survives, but the research capture cut off
mid-word at that point and the missing word was not recovered — it is not reconstructed or guessed
here. What was fully re-fetched and verified is the tweet's next sentence, which supplies the
load-bearing claim on its own:

> "The relationship-building of sales, the custom solution work required to land and retain a
> larger business: all of that is much less tech than it depends on interpersonal dynamics. And as
> long as humans make tech choices instead of AI systems, these companies will possess a moat that
> prevents them from being cloned by a well-written prompt."

Grade: OPINION. What makes this citable rather than just another hot take is that **it states its
own falsification condition**: the moat holds *as long as humans make the tech-buying decisions*.
That gives the gate a testable boundary instead of an assertion — the exact condition under which
this pack's founder-led assumptions would need revisiting is named in the source, not invented by
this pack. Two independent practitioners (Shpigford, arvidkahl) converging on "complexity is what
survives" from opposite sides (buyer erosion, seller moat) is a real signal, but it is a
convergence of opinion, not a measurement — grade it as such when citing it.

## The PLG boundary: a usage threshold, not a demand signal

Product-led growth complicates "does a sales motion apply" further: usage can trigger a handoff to
sales without any outbound motion ever running. PostHog's live internal handbook publishes a
concrete instance — a criteria-based, product-led handoff from self-serve onboarding into sales,
automated via a Vitally-to-Salesforce lead-creation pipeline, keyed on a **usage/spend threshold of
$1,000/mo** and an explicit "don't wait for the customer to respond" instruction
(github.com/PostHog/posthog.com, `contents/handbook/onboarding/sales-handover.md`, commit
`259e5a6921ce301f4b8efa957d33050ea34e6d36`). Licensing: the MIT permission grant, applied by
PostHog to the `/contents/` folder — the handbook lives entirely under that path, so it is
reproducible with attribution; nothing outside `/contents/` carries that grant.

This is the closest primary-source analogue in the corpus to "what counts as sales-ready" — but
read it narrowly. It is a **PLG-signal handoff** (a usage/spend threshold observed in-product), not
a marketing-MQL handoff (a fit-plus-intent signal marketing hands to sales, see
[icp-and-qualification](icp-and-qualification.md) and [handoff](handoff.md)). It corroborates the
*shape* of a usage-based handoff criterion existing and being workable at a real company; it does
not settle marketing's own contested MQL vocabulary, and it should never be cited as if it did.
Treat a usage/spend threshold as one legitimate trigger type among the four gates above, not a
fifth gate that supersedes them — it answers "when does *this specific account* need sales," a
narrower question than "does a sales motion exist for this product at all."

## Validation

- The verdict names which gate(s) actually apply to the situation described, not a default
  assumption based on company size or B2B-vs-B2C labeling alone.
- If more than one gate is in tension (e.g., low ARPA per Janz but a purchasing-friction trigger
  per McKenzie), both are named rather than silently picking one.
- Janz and Lemkin are never cited as two independent confirmations of the same claim.
- Shpigford's and arvidkahl's tweets are cited as OPINION with their falsification condition
  intact where relevant, never as settled prediction.
- Any decision-already-made figure is cited to the CEB/Google primary with its subject attached —
  self-reported progress before first engagement with a supplier *sales rep* — and never in its
  derivative forms, its Gartner misattribution, or as evidence a sales motion is unnecessary.
- The PostHog PLG threshold is cited as a usage-signal exhibit, never as evidence that settles
  marketing's MQL definition.

## Failure modes and handoff

- Building outbound infrastructure or a dedicated CRM because the product is "B2B," without
  checking which gate (if any) actually applies at the current ARPA and purchasing process.
- Treating Lemkin's numbers and Janz's tiers as two independent sources when Janz is quoting
  Lemkin from memory inside his own post.
- Citing arvidkahl's complexity-moat tweet as a settled prediction and dropping its own stated
  falsification condition.
- Repeating "57%" (or "9 in 10," or "70–80%") as a decision-is-already-made claim — the primary
  measures progress, not completion, and two of the three numbers have no source at all.
- Citing PostHog's $1,000/mo handover threshold as if it were a universal PLG rule, or as if it
  resolved marketing's MQL definition, rather than one company's own criterion.
- Once a motion is judged to apply, defaulting straight to enterprise-team vocabulary and
  machinery — read [surface-founder-led-solo](surface-founder-led-solo.md) first; it is this
  pack's default reader. See [handoff](handoff.md) for the full seam map to `marketing`, `growth`,
  and `success`.
