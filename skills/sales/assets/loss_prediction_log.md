# Loss Prediction Log

Template for the predict-then-score loop described in `../references/win-loss-learning.md` §4:

> "Write down 'If we lose this deal, it will be because of X.' in advance. If you lose the
> deal/account/etc, ask why you lost it. Check against your prediction, and get better at
> predicting." — @patio11, https://x.com/patio11/status/1345906043197427713

**The rule that makes this work: log the "Predicted reason" row BEFORE the deal resolves.** A reason
written after the outcome is known is not a prediction — it is another instance of the post-hoc
theorizing `win-loss-learning.md` §1 warns about. Fill "Actual reason" and "Match?" only once the
deal is closed, and note in "Actual reason" what corroborated it beyond the buyer's own words
(win-loss-learning.md §2) — a match with no corroboration is graded "Unverifiable," not "Match."

**How to use it:**
1. As soon as a deal enters a stage where you have a real read on it, add a row and write the
   predicted reason and your confidence — before anything else changes.
2. Leave "Actual reason" and "Match?" blank until the deal closes. An open deal stays "Pending."
3. At close, fill "Outcome" and "Actual reason," naming what corroborated it (a second stakeholder,
   deal activity, a contract term) or noting there was none.
4. Grade "Match?" using win-loss-learning.md §2's rule, then write the one-line "Lesson" — what you'd
   do differently in reading the *next* deal, not a restatement of what happened to this one.

| Deal | Logged | Predicted reason (if lost) | Confidence | Outcome | Actual reason (source) | Match? | Lesson |
|---|---|---|---|---|---|---|---|
| Acme Corp | 2026-06-02 | Budget freeze, not us | Med | Lost 06-20 | "Budget freeze" — confirmed by buyer's follow-up email citing a hiring freeze | Match | Corroborated beyond the buyer's own explanation — trust this one. |
| Northwind Logistics | 2026-06-05 | Losing to Competitor B on price | High | Lost 06-18 | "Stayed with existing vendor, no new tool" — buyer call | No match | Predicted a rival; real reason was status quo. Update the model, not just the score. |
| Bramble Retail | 2026-06-10 | Champion left the company | High | Lost 07-01 | Departure confirmed via LinkedIn + buyer email | Match | Corroborated by a source other than the buyer's stated reason. |
| Delta Fabrication | 2026-06-12 | No urgency, slips to next year | Low | Won 06-25 | — | Miss (timing) | Closed faster than predicted — a wrong prediction on a win still counts. |
| Ferro Systems | 2026-06-14 | Security review will stall it | Med | Open | — | Pending | Past the predicted stall point — check in rather than letting the row go stale. |
| Glasswing Media | 2026-06-18 | Price, they'll push for 20% off | High | Lost 07-05 | "Price" — buyer's stated reason only, no second source | Unverifiable | Stated reason matches the prediction, but with no corroboration this may be two people converging on the same plausible story, not evidence the story is true. |
| Harborline Insurance | 2026-06-20 | Will stall on legal redlines | Med | Won 07-10 | — | Miss | Legal was fast this time — don't assume last deal's blocker repeats. |
| Ironclad Staffing | 2026-06-22 | No access to the economic buyer | High | Lost 07-15 | Confirmed: champion never got the budget-holder on a call — visible in the deal's own activity log | Match | Strongest row in this log: predicted from deal activity before resolution, confirmed by a mechanism independent of the buyer's later account. |
| Juniper Analytics | 2026-06-25 | Timeline pressure closes it before fiscal year end | Med | Won 07-02 | — | Match | A correct WIN prediction counts too — this is a calibration record, not a loss post-mortem. |
| Kestrel Robotics | 2026-06-28 | *(none logged)* | — | Lost 07-20 | "Budget" — buyer's stated reason | Not scoreable | No advance prediction means nothing to calibrate — this is the cost of skipping the log, not a data point. |

**Reading this log:**
- Do not report a calibration verdict ("I predict losses correctly N% of the time") from a log this
  short. Calibration is a property of a track record across many same-type deals, not of any one row
  — see `../references/forecasting-honesty.md`'s small-numbers gate for the same statistical point
  applied to stage probabilities.
- "Match" requires corroboration beyond the buyer's own stated reason (win-loss-learning.md §2). If
  the only support is the buyer's own words, grade it "Unverifiable," as in the Glasswing row above.
- A "Lost, no prediction logged" row (Kestrel) is worth keeping in the log — it is a visible cost of
  not running the loop, not a row to delete.
- When the same "Lesson" recurs across several rows (for example, repeated losses to "no access to
  the economic buyer"), that is a validated pattern, not a single deal's story — it is ready to move
  to `../references/objections-and-enablement.md` as a battlecard input. This log only establishes
  that a pattern is real; it does not write the response to it.
