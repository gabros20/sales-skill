# Forecasting honesty

Purpose: what a sales forecast can honestly predict, why "3x coverage" is a tautology dressed as a
finding, and what a solo pipeline can and cannot validate. The pack's flagship.

Read when: building, presenting, or auditing a deal pipeline (the set of open deals you're tracking
toward close) or bookings forecast; setting or defending a coverage ratio; deciding whether a
forecast category (Commit / Best Case / Pipeline) means anything; running a forecast-honesty pass
on your own numbers before a board or investor update.

Skip when: the stage structure and fields themselves (→ `crm-and-pipeline.md`); scoring why a
specific deal was actually lost (→ `win-loss-learning.md`); the criteria that get a deal into the
pipeline at all (→ `icp-and-qualification.md`); the expansion-sale motion (→ `handoff.md`).

Inputs: your own win-rate history, if any, and its sample size; which forecast categories your tool
uses and whether they carry checkable conditions or are just labels; how many quarters of
stage-to-close data you actually have.

Produces: an honest read on what a stage-weighted number, a coverage ratio, or a forecast category
can and cannot tell you, plus two runnable checks against your own numbers —
`assets/coverage_calc.py` and `assets/forecast_calibration_check.py`.

## Contents
1. This is prior art, not our novelty · 2. The evidence line · 3. The four-leg accuracy null ·
4. The coverage tautology · 5. The small-numbers gate · 6. Five things that work at n=1

---

## 1. This is prior art, not our novelty

Before anything else: **"name your assumptions or the forecast is theatre" is not a new idea, and
this pack does not claim it is.** A 23,656-star, MIT-licensed, health-clean incumbent already ships
exactly this posture. `alirezarezvani/claude-skills`'s `commercial-forecaster` (v2.8.0) exists to
produce a commit/best-case/pipe-only number, and its own description says so:

> "Use when building a quarterly bookings forecast, ARR projection, pipeline forecast, NRR
> projection, or commit/best-case/pipe-only board number — especially when the CRO needs to walk
> the board through funnel math + cohort ARR + per-stage conversion assumptions without the theatre
> of a single undefended number. … Every output explicitly names the conversion rate used, the data
> window, and the weighting choice."

and, from the body: "The assumption block is non-optional. If you remove it, the forecast becomes
theatre." It ships a runnable `scripts/bookings_forecaster.py` with a stated last-4Q/last-12Q 70/30
weighting. (`alirezarezvani/claude-skills`,
`commercial/skills/commercial-forecaster/SKILL.md`, read at pinned commit
`aa8d778811a557a2c28ccadda4cf3d0bd028a4cc`; PRIMARY, MIT under the repo's root grant — note the
tree carries five distinct copyright holders, so run a per-directory check before adapting
anything.) Claiming novelty on assumption-disclosure would ship a defect.

What this pack adds is narrower: the peer-reviewed evidence for *why* forecasts drift (§2); a
no-accuracy-measurement null that survives this incumbent intact (§3); the small-numbers argument
for why a solo pipeline can't validate a stage weight even if it wanted to (§5); and primitives that
work with zero CRM, zero board, and one deal at a time (§6). The incumbent is pitched at CRO/RevOps
scale, needs roughly a dozen quarters of stage-conversion history to intake, and measures nothing
about whether its own number was right — real gaps, but narrow; don't oversell them.

## 2. The evidence line

The sales canon rarely cites anyone outside itself on forecasting. Two peer-reviewed papers, both
read directly from open-access PDFs, are worth more than any vendor's accuracy claim.

**Lawrence, Goodwin, O'Connor & Önkal (2006), "Judgmental forecasting: A review of progress over the
last 25 years," *International Journal of Forecasting* 22(3):493–518, DOI
10.1016/j.ijforecast.2006.03.007** documents that forecasts used as targets get gamed toward the
target — sandbagging is peer-reviewed, not folklore:

> "In another case, sales levels were manipulated by promotional spending to ensure that sales
> targets were met. One major multi-national commented that they always ensure that sales are
> within 0.5% of the forecast — they made sure it happened that way!"

immediately followed by the reviewers' own admission that "this aspect of the sales forecasting
process has been largely ignored by researchers." The same paper reports that where a forecast
doubles as a target, "the forecasts tended to be below the actual" — the mechanism behind
sandbagging, not just the label for it.
(https://repository.bilkent.edu.tr/bitstreams/0dd7098f-7171-4819-a8bb-6325ef8a8929/download,
PRIMARY.)

**Fildes & Goodwin (2007), "Against Your Better Judgment?", *Interfaces* 37(6):570–576, DOI
10.1287/inte.1070.0309** surveyed 120 forecasters (115 recruited at four international forecasting
conferences, plus 5 case-study companies — a disclosed, citable method). Asked whether they ever
review the extent to which judgmental adjustments improve accuracy: "Only 52.8% of respondents said
they did." And on error measurement generally: 25% "did not indicate that they used any error
measure at all." (https://eprints.lancs.ac.uk/id/eprint/48879/1/Document.pdf, PRIMARY.)

Read together: even professional, resourced forecasting operations — not solo founders, not
under-resourced sales teams — routinely don't check their own accuracy, and when a forecast is used
as a target, sales makes sure the forecast comes true rather than the other way around. This is a
stronger, more honest teaching hook than any vendor accuracy percentage in §3.

## 3. The four-leg accuracy null

**Forecast method is publishable. Forecast accuracy is published by no one.** Four independent legs,
none resting on a dead search:

1. **GitLab keeps it internal.** GitLab publishes a detailed, named nine-stage opportunity process
   with exit criteria per stage
   (https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/commercial/comm-sales-opp-stages/_index.md,
   PRIMARY) — but its forecasting page lives at `internal.gitlab.com/handbook/sales/sales-forecasting/`,
   which returns HTTP 302→403 to sign-in, and the Sales homepage states plainly that Sales KPIs
   "are Not Public."
   (https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/_index.md,
   PRIMARY.) The one forecast-adjacent instruction that is public — "Update the Close Plan and
   Close Date to ensure you're forecasting accurately"
   (https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/sales-operating-procedures/retain-and-expand.md,
   PRIMARY) — is an instruction to *be* accurate, not a measurement of it.
2. **Sourcegraph publishes the method GitLab hides, and still measures nothing.** Its forecasting
   handbook splits the forecast into stage, forecast category, amount, and close date, and runs two
   taxonomies — one per opportunity (Won/Commit/Best Case/Pipeline/Omitted) and one for the roll-up
   (Commit/Best Case/Call), quoted in full in §6. It is the most complete published method in this
   research, and it carries **no accuracy figure anywhere on the page** (PRIMARY — content dated
   2022/FY23, repo archived 2024-07-02; cite as history, not current practice).
3. **Eight open-source CRMs, zero accuracy claims.** Grepping the actual probability-computation
   code, not marketing copy: Odoo's 2,890-line `crm_lead.py`, a genuine Naive Bayes win-probability
   model, contains zero occurrences of "accuracy" anywhere in the file
   (https://github.com/odoo/odoo/blob/869c750f978b1b00a4a04bd61226f0e20d2e7729/addons/crm/models/crm_lead.py,
   PRIMARY). EspoCRM, SuiteCRM, Twenty, Krayin, atomic-crm, and frappe/crm compute no probability at
   all, or use a static hand-set lookup table — none validates it against outcomes.
4. **The largest incumbent structures and discloses; it does not measure.** §1's
   `commercial-forecaster` names its conversion rate, data window, and weighting choice, and never
   claims or measures whether the resulting number was right.

A fifth, practitioner-level check closes the loop: across every forecasting-related query run
against X, **zero practitioners stated a stage-weighted probability and said whether it was ever
backtested.** The hand-set stage weight is not defended there, not attacked there — it is simply
never examined. That silence, on top of four sourced legs, is the flagship's evidentiary spine.

**Vendor accuracy claims are the same pattern with a number attached.** Gong's forecast page quotes
a customer saying "our forecast accuracy has grown to the point that we're at 95%" and separately
claims "20% more precision" than "algorithms based on CRM data" — neither discloses a measurement
period, a baseline, or what "precision" means (https://gong.io/forecast/, VENDOR-SELF-REPORTED,
method not disclosed). Aviso's marketing headline claims "29 Quarters of Highly Accurate Forecasts"
with no accuracy metric stated anywhere it appeared (VENDOR-SELF-REPORTED; no permalink was captured
for this one — treat it as uncited). **Never ship a bare vendor accuracy percentage without the
method-absence statement attached — it is vendor-self-reported either way.**

## 4. The coverage tautology

"3x pipeline coverage" is not an empirically discovered threshold. It is the reciprocal of an
assumed win rate, restated: **coverage = 1 / win rate.** At a 33% win rate you need roughly 3x; at
25%, 4x; at 20%, 5x. There is no separate "3x" finding — every source that states the number derives
it from this identity, whether or not it says so.

GitLab's own capacity-planning page makes the derivation concrete without meaning to. It states a
33% win rate as an explicit planning input: "Win rate - 33% … This is a calculation only and should
be used to set goals and plan."
(https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/gtm-resources/_index.md,
PRIMARY.) 1/0.33 ≈ 3 — the "3x" a reader might have heard elsewhere falls straight out of this one
assumption. **Ship this only as "a planning-only assumption, explicitly not a measurement." Never
write "GitLab's forecast is 33% accurate," and never attribute a Commit/Best-Case percentage table
to GitLab — it doesn't publish one.**

The same number circulates as unsourced folklore on the practitioner side, with no derivation
attached: "For years, 3-to-1 quota coverage was solid. 5-to-1 was world class."
(https://x.com/gtmba_/status/2041174257271480446, FOLKLORE — no source, no definition of what
"coverage" is measured against.) Pair the two: the identity is real arithmetic; the constant that
circulates instead has no origin on either the incumbent-pack surface or the practitioner surface.
**Never ship "3x" as a portable constant. Derive your own coverage from your own win rate — a win
rate without its denominator is not a number — and show the arithmetic, not the folklore.**

## 5. The small-numbers gate

Even a reader with a real, honestly-measured win rate cannot validate a stage weight from their own
pipeline. Calibration — "the correspondence of forecast probabilities with the realized proportion
of correct predictions," in the peer-reviewed literature's own definition (Lawrence et al. 2006,
§2) — is a property of a *track record*, not of any single forecast. The statistical reason, stated
plainly by the Brier score's own reference article: "Quite large sample sizes, i.e. n > 1000, are
required for higher-skill forecasts of relatively rare events, whereas only quite modest sample
sizes are needed for low-skill forecasts of common events." (https://en.wikipedia.org/wiki/Brier_score,
PRIMARY.) A solo founder's open deal count is nowhere near that, at either end of the scale.

Good Judgment Open's own tournament explainer makes the same point operationally: individual scores
are "averaged across the question's lifespan and across many questions" — a single scored forecast
tells you almost nothing (https://gjopen.com/faq, PRIMARY). Note the scale caveat: Brier is 0–1 in
the Wikipedia formulation and 0–2 in Good Judgment's multi-option one — don't conflate the two when
citing a score.

**The pack's rule: a single deal's "60% probability" is not falsifiable and cannot be validated on
n=1 or n=5. Only a large number of same-type deals, scored the same way and tracked over time,
produces a checkable calibration curve.** This frees a small pipeline from pretending otherwise —
the honest move is not to fake a track record you don't have, it's to use one of §6's primitives
that don't need one.

## 6. Five things that work at n=1

None of the following need a CRM, a board, or twelve quarters of history.

**Predict the loss before it happens, then score yourself.** Write down, in advance, "if we lose
this deal it will be because of X." When it's lost (or won), check the prediction against the
outcome.

> "Write down 'If we lose this deal, it will be because of X.' in advance. If you lose the
> deal/account/etc, ask why you lost it. Check against your prediction, and get better at
> predicting."
> — @patio11 (https://x.com/patio11/status/1345906043197427713)

This is the only calibration mechanism found on any surface in this research, and it works at any
volume. It also serves win-loss learning (→ `win-loss-learning.md`) — one primitive, two jobs.

**Refuse to forecast on negative criteria, not positive ones.** A practitioner's self-authored,
falsifiable exit criteria — reasons to *decline* a deal rather than probabilities to assign it:

> "1) No velocity — When a prospect delays next steps for weeks (or longer) they aren't spending
> that time justifying your product - they are spending that time working on more important
> issues. And if your product doesn't address their most important problems, it's not getting
> purchased. 2) No concerns — Buying carries risk. If your prospect isn't asking you to help
> address concerns, they aren't really considering buying. No concerns often means no
> consideration. 3) No 'next best option' — Execs rarely put all eggs in one basket… No alternative
> options to your product most likely means they haven't committed to solve the problem you
> address."
> — @KyleAsay_ (https://x.com/KyleAsay_/status/1909618149621653983)

The inversion is the point: instead of hand-setting a stage percentage nobody has validated, name
the conditions under which you refuse to count a deal at all.

**Report a floor, a ceiling, and an honest judgment call — not one number.** Sourcegraph's roll-up
taxonomy names the shape explicitly: "If you consider the Commit as the floor and Best Case as the
ceiling, then the Call is the number in between that you are forecasting as the most likely
outcome." Commit is summed from records; Call is what the rep "feel[s] will come in" — the document
says so itself, making explicit that the headline number is a judgment, not a derivation
(https://github.com/sourcegraph/handbook/blob/5752928b213a3ddbc7cee4459524f404a5b96fb4/content/departments/sales/process/forecasting.md,
PRIMARY; Apache-2.0, repo archived 2024-07-02 — the staleness caveat travels with every citation).

**Disclose what fraction of your pipeline total is a real number.** GitLab's own booking-metrics
documentation states that a deal's dollar value is an estimate until a formal quote exists:

> "Sales Assisted - Quoted → Zuora Quote Data / Sales Assisted - Not Quoted → Estimated Net ARR /
> … If Zuora data is not present then use an estimated Net ARR amount until the deal is quoted."
> (https://gitlab.com/gitlab-com/content-sites/handbook/-/blob/46180fa3686c8baa55f91bf32c6e1d676eefd475/content/handbook/sales/field-operations/sales-systems/gtm-technical-documentation/sfdc-booking-metric-fields.md,
> PRIMARY)

Every pipeline total mixes quoted and estimated amounts, and the total alone never tells you the
ratio. Say the ratio out loud instead of letting the total imply false precision.

**Name your metric, define what it comprises, and label your own rule of thumb as rough.** The
positive model against "3x coverage": a practitioner who defines a custom metric inline, states what
it accounts for, and explicitly calls his own shortcut a "Rough heuristic" rather than a rule.

> "Sales Output is the more relevant metric. It accounts for capacity (number of ramped
> quota-carrying reps) combined with their relative performance (measured by quota attainment) on a
> YoY basis."
> — @thaAdamLittle (https://x.com/thaAdamLittle/status/2008940390385152153)

The discipline transfers even without his specific metric: name what a number measures before you
report it, and flag a shortcut as a shortcut.

## Validation

- Every figure in this file, or in output modeled on it, carries a permalink or an explicit grade —
  never a bare percentage.
- No forecast-category percentage is ever attributed to GitLab; its only public number is the 33%
  planning-only win-rate assumption (§4), and it must carry that qualifier every time.
- Any coverage ratio shown is derived from the reader's own win rate, with the arithmetic visible —
  never "3x" presented as a portable constant.
- A calibration or accuracy claim about a stage weight is checked against §5 before it ships: is the
  sample size anywhere near what calibration requires?

## Failure modes and handoff

- **Wants a defensible single forecast number** — there isn't one; give the floor/ceiling/judgment
  shape (§6) and `assets/coverage_calc.py`'s derivation instead of a point estimate.
- **Wants to validate a stage-weight scheme against their own pipeline** — route to §5 and
  `assets/forecast_calibration_check.py`, which refuses a verdict below an honest sample size.
- **Asks why a deal was actually lost, not how to forecast the next one** — → `win-loss-learning.md`.
- **Asks about stage fields, exit criteria, or CRM structure itself** — → `crm-and-pipeline.md`.
