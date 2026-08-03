# Win/Loss Learning

Purpose: Read a buyer's stated reason for winning or losing a deal honestly — what it can support,
what it cannot, and how to build a track record that actually gets more accurate over time. This
file does not teach how to run a discovery call or how a deal is qualified; it teaches how to treat
the "why" once a deal is closed.

Read when:
- Running or designing win/loss interviews, or reading someone else's write-up of one.
- A "we lost because of X" (or "we won because of Y") story is circulating as settled fact after a
  single conversation.
- Evaluating a win/loss vendor's or tool's interview methodology before adopting it.
- Building the habit of logging a loss (or win) reason so the pattern across deals is usable later.

Skip when:
- The question is what to say or ask during an active discovery call → `discovery-calls.md`.
- The question is forecast calibration itself — the small-numbers gate, Brier-scale caveats, or
  scoring a probability against an outcome → `forecasting-honesty.md`. The predict-then-score
  *mechanism* is shared between the two files (§4 below); that file applies it to a stage
  probability, this one applies it to a stated reason.
- The question is a qualification framework's taxonomy or evidence base (MEDDIC, BANT, MEDDPICC's
  legal status) → `icp-and-qualification.md`.
- The question is turning a validated loss pattern into a battlecard or objection response →
  `objections-and-enablement.md` — this file stops at "is the pattern real," not "what do we say
  about it."
- The question is win rate as a metric and its denominator → `forecasting-honesty.md`'s
  `coverage_calc.py` owns that arithmetic.

Inputs: closed deals (won and lost), any buyer-facing exit interview, survey, or off-hand comment
captured at close, and — if one exists — the seller's own prediction logged before the outcome was
known.

Produces: a graded read of what a specific stated reason can honestly support, a corroboration
check before treating any reason as a cause, and a log format (`../assets/loss_prediction_log.md`)
that turns the habit into a testable track record.

## Contents
- [1. The problem: a stated reason is a theory, not a measurement](#1-the-problem-a-stated-reason-is-a-theory-not-a-measurement)
- [2. The observer test — why one more interview doesn't fix it](#2-the-observer-test--why-one-more-interview-doesnt-fix-it)
- [3. The boundary condition, carried honestly](#3-the-boundary-condition-carried-honestly)
- [4. The corrective: predict, then score](#4-the-corrective-predict-then-score)
- [5. No authoritative owner — the claim here is quality, not first](#5-no-authoritative-owner--the-claim-here-is-quality-not-first)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## 1. The problem: a stated reason is a theory, not a measurement

**Nisbett, R. E., & Wilson, T. D. (1977). "Telling More Than We Can Know: Verbal Reports on Mental
Processes." *Psychological Review*, 84(3), 231–259.** PRIMARY, full text read directly from
https://home.csulb.edu/~cwallis/382/readings/482/nisbett%20saying%20more.pdf
(https://psycnet.apa.org/record/1978-00295-001 is the bibliographic record only). One of the
most-cited papers in the history of psychology, and its own examples are purchase-choice questions.

> "Evidence is reviewed which suggests that there may be little or no direct introspective access
> to higher order cognitive processes… It is proposed that when people attempt to report on their
> cognitive processes… they do not do so on the basis of any true introspection. Instead, their
> reports are based on a priori, implicit causal theories, or judgments about the extent to which a
> particular stimulus is a plausible cause of a given response."

The decisive experiment is a consumer-choice study, not a lab abstraction. SUBJECT CHECK: the ratio
below is the **stockings** study only (n=52, four *identical* pairs) — do not merge it with the
paper's separate nightgown study (n=378, four *different* nightgowns).

> "…passersby were invited to evaluate articles of clothing—four different nightgowns in one study
> (378 subjects) and four identical pairs of nylon stockings in the other (52 subjects). Subjects
> were asked to say which article of clothing was the best quality and, when they announced a
> choice, were asked why they had chosen the article they had. There was a pronounced left-to-right
> position effect, such that the right-most object in the array was heavily overchosen. For the
> stockings, the effect was quite large, with the right-most stockings being preferred over the
> left-most by a factor of almost four to one. When asked about the reasons for their choices, no
> subject ever mentioned spontaneously the position of the article in the array."

Asked directly about a possible effect of the position of the article, the paper reports that
virtually all subjects denied it — the raw capture of this sentence stops there, mid-source-sentence
and unrecovered elsewhere in the corpus, so that last clause is paraphrased here rather than quoted.

Applied to win/loss: "we went with the other vendor because of price" is evidence about what sounds
like a plausible reason to the buyer — not evidence about what caused the decision. The items in
the stockings study were identical; every stated reason was necessarily invented after the fact.

## 2. The observer test — why one more interview doesn't fix it

The sharper result is not "buyers are sometimes wrong." It is that people who never experienced the
choice at all generate the *same* wrong reasons:

> "The observer subjects made predictions that in every case were similar to the erroneous reports
> given by the actual subjects." And, from the paper's word-association study: "the judgments of
> the probability that particular word cues would affect particular target responses were
> positively correlated with the original subjects' 'introspective reports' of the effects of the
> word cues on the target responses. (Both subject reports and observer predictions were slightly
> negatively correlated with true cuing effects.)"

A stated reason therefore carries no privileged information about the actual cause — an outsider
with no access to the deal can generate the same plausible story. The practical consequence: a
second buyer-side interview about the same loss does not corroborate the first one. Both are drawing
on the same pool of plausible theories, not on independent knowledge of the cause. Corroboration has
to come from something other than another person's stated reason — a second stakeholder's
independently observed behavior, the actual product or contract terms the buyer chose, a timeline
that confirms or contradicts the story, or your own deal activity from before the outcome was known.

## 3. The boundary condition, carried honestly

The authors do not claim self-report is always wrong, and the pack must not either:

> "This suggests that though people may not be able to observe directly their cognitive processes,
> they will sometimes be able to report accurately about them. Accurate reports will occur when
> influential stimuli are salient and are plausible causes of the responses they produce, and will
> not occur when stimuli are not salient or are not plausible causes."

The honest teaching is not "win/loss interviews are worthless." It is that a stated reason is least
reliable for exactly the subtle, competitive, or relational factors win/loss analysis most wants to
learn about — and there is no way to tell, from the answer alone, whether you are in the reliable
case or not. Treat every stated reason as a hypothesis to corroborate, never as a finding to record.

**Spot check, scoped narrowly.** The leading win/loss vendor's own published buyer-interview
guidance — Clozd, "Win-Loss 101: What to Ask Buyers in Win-Loss Interviews"
(https://www.clozd.com/blog/win-loss-101-what-to-ask-buyers-in-win-loss-interviews) — contains no
acknowledgment of self-report limitations; its stated rationale for more interviews is consistency
("you don't have enough consistent data to identify any meaningful trends"), not validity.
VENDOR-SELF-REPORTED, and this is one page from one vendor, checked once — it supports "the leading
vendor's flagship how-to treats a buyer's stated reason as data, not as testimony to corroborate."
It does not support "the whole win/loss industry ignores validity"; that broader claim was not
checked and must not ship.

## 4. The corrective: predict, then score

The one mechanism found anywhere in this research that turns a stated reason into something
checkable is a habit, not a framework:

> "Write down 'If we lose this deal, it will be because of X.' in advance. If you lose the
> deal/account/etc, ask why you lost it. Check against your prediction, and get better at
> predicting." — @patio11, 2021-01-04, https://x.com/patio11/status/1345906043197427713

The mechanic: log a predicted reason **before** the outcome is known, using whatever signal is
available at the time (deal activity, stakeholder engagement, competitive intel) — not the buyer's
future explanation. When the deal resolves, collect the buyer's stated reason as one input, weigh it
against §§1–3, and check it against your own prediction. This inverts the failure mode above: you
are not trusting a post-hoc story, you are testing whether your own read of the deal, made in
advance, tracks reality.

This does not fix Nisbett & Wilson's problem on its own — the buyer's stated reason at resolution
still carries the same limits. What it buys you is a second, independent signal (your own prediction)
to weigh the buyer's story against, and — across many deals — a track record. One deal's "match" or
"mismatch" proves nothing; calibration is a property of a track record over many same-type deals,
not of any single prediction (see `forecasting-honesty.md`'s small-numbers gate, which states this
for stage probabilities — the same statistical fact applies here). Use
`../assets/loss_prediction_log.md` to run the loop; that file is the template, this section is why
it works.

## 5. No authoritative owner — the claim here is quality, not first

Several incumbent packs already ship win/loss content by name, and none has meaningful adoption:
`TheCraigHewitt/sales-skills` ships a `win-loss-analysis` skill (MIT per one census pass, not
independently file-verified) at single- to low-double-digit installs; `gtmagents/gtm-agents` ships a
`win-loss-dataset` with a `run-win-loss-program` command and a `win-loss-analyst` agent inside a
broad, ~12–13-of-14-item pack graded generic and templated after a full SKILL.md read;
`louisblythe/sales-skills` ships `deal-review-win-loss` and
`win-loss-reason-extraction` skills with no license file — cite the fact of their existence, never
their content. `LeadMagic/gtm-skills` (~130 skills) was checked directory-by-directory and has none
of this. Win/loss learning is a genre several people have built pieces of; the differentiator this
file offers is evidentiary grounding and the predict-then-score corrective, not a claim of
precedence.

## Validation

- Every stated win or loss reason is corroborated by something other than another stated reason
  before it is treated as a finding (§2).
- The stockings 4:1 figure, if cited, always carries its subject (n=52, four identical pairs) — never
  generalized to "buyers prefer X 4:1" (§1).
- The Clozd finding is scoped to "one vendor's flagship guidance," never generalized to "the win/loss
  industry" (§3).
- A prediction in the log (`../assets/loss_prediction_log.md`) was written before the outcome was
  known — a reason added after the fact is not a prediction.
- No calibration verdict ("I predict losses correctly N% of the time") is drawn from fewer resolved
  predictions than the small-numbers gate in `forecasting-honesty.md` allows.

## Failure modes and handoff

- **A single interview's stated reason is repeated as "why we lost this deal."** Apply §§1–2:
  corroborate with an independent signal or hold it as a hypothesis, not a finding.
- **A second interview is used to "confirm" the first.** Apply §2 — both interviews draw on the same
  pool of plausible post-hoc theories; that is not independent confirmation.
- **A vendor's win/loss methodology is adopted on the strength of "we ask more questions."** Apply
  §3's spot check: more interviews answer a consistency question, not a validity one.
- **A predicted-then-scored match or mismatch from one deal is used to declare "our forecasting is
  accurate."** Route to `forecasting-honesty.md`'s small-numbers gate — one deal is not a track
  record.
- **A validated loss pattern needs to become a battlecard or a response to a live objection.** Route
  to `objections-and-enablement.md` — this file stops at establishing the pattern is real.
- **The question is actually about what to ask on the call itself, before a deal closes.** Route to
  `discovery-calls.md`.
