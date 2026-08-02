#!/usr/bin/env python3
"""
forecast_calibration_check.py -- scores a prediction-then-score log (patio11's primitive:
predict before you know, check after) and refuses to render a calibration VERDICT below an
honest sample size.

Calibration is a property of a track record, not of any single forecast -- Lawrence, Goodwin,
O'Connor & Onkal (2006), "Judgmental forecasting," International Journal of Forecasting 22(3),
whose own definition is quoted in references/forecasting-honesty.md SS5. The statistical reason a
small pipeline can't validate a stage weight, verbatim from the Brier score article: "Quite large
sample sizes, i.e. n > 1000, are required for higher-skill forecasts of relatively rare events,
whereas only quite modest sample sizes are needed for low-skill forecasts of common events."
(https://en.wikipedia.org/wiki/Brier_score). This script always computes the raw Brier score --
that is just arithmetic -- but refuses to say a track record IS or ISN'T well-calibrated until the
sample is large enough that the claim would mean something, and flags the intermediate,
directional-only tier honestly rather than staying silent about it.

Two Brier scales exist and must never be conflated (references/forecasting-honesty.md SS5):
  - brier_score_binary(): the standard 0 (perfect) to 1 (worst) single-outcome formulation,
    BS = (1/N) * sum((f_t - o_t)^2), per Wikipedia's Brier score article.
  - brier_score_two_option(): Good Judgment Open's 0 to 2 multi-option formulation, which scores
    BOTH the yes-side and no-side error and sums them -- gjopen.com/faq's own worked example: a
    70% forecast on a yes/no question that resolves YES scores (1-0.7)^2 + (0-0.3)^2 = 0.18. A
    score of "0.18" on the 0-2 scale is NOT comparable to a "0.18" on the 0-1 scale.

Sample-size tiers (n = number of scored predictions in the log):
  - n < MODEST_N (30): no verdict at all. Keep logging.
  - MODEST_N <= n < STRICT_N (1000): directional-only note, explicitly not a validated
    calibration claim -- 1000 is the threshold the Brier-score literature names for reliably
    scoring skill at rare/high-skill events; most solo pipelines will live in this tier
    indefinitely, and that is the honest state to report, not a failure of the tool.
  - n >= STRICT_N: a calibration verdict may be rendered.

Self-test anchors (run automatically at import, and again before any CLI use):
  - Wikipedia's own Brier formula, single case: forecast 0.7, outcome YES (1) -> (0.7-1)^2 = 0.09
    on the 0-1 scale.
  - Good Judgment Open's own worked example: forecast 0.7, outcome YES -> 0.18 on the 0-2 scale.
  - A log of fewer than 30 entries returns verdict=None with a "keep logging" message.
  - A log of 30-999 entries returns a directional note, never a pass/fail verdict.
  - A log of >=1000 entries returns a scored verdict.
"""
import argparse

MODEST_N = 30
STRICT_N = 1000


def brier_score_binary(predictions):
    """Standard 0-1 scale. predictions: iterable of (forecast_probability, outcome) pairs,
    outcome in {0, 1}, forecast_probability in [0, 1]."""
    preds = list(predictions)
    if not preds:
        raise ValueError("predictions must not be empty")
    for f, o in preds:
        if not (0 <= f <= 1):
            raise ValueError(f"forecast probability must be in [0, 1], got {f}")
        if o not in (0, 1):
            raise ValueError(f"outcome must be 0 or 1, got {o}")
    return sum((f - o) ** 2 for f, o in preds) / len(preds)


def brier_score_two_option(predictions):
    """Good Judgment Open's 0-2 scale -- scores both sides of a binary question. Same input
    shape as brier_score_binary; NEVER compare its output to brier_score_binary's."""
    preds = list(predictions)
    if not preds:
        raise ValueError("predictions must not be empty")
    total = 0.0
    for f, o in preds:
        if not (0 <= f <= 1):
            raise ValueError(f"forecast probability must be in [0, 1], got {f}")
        if o not in (0, 1):
            raise ValueError(f"outcome must be 0 or 1, got {o}")
        total += (f - o) ** 2 + ((1 - f) - (1 - o)) ** 2
    return total / len(preds)


def assess_calibration(predictions, scale="0-1"):
    """Computes the raw score (always) and a verdict (only above MODEST_N, and only a real
    calibration claim above STRICT_N). Refuses to pretend a small log is a track record."""
    preds = list(predictions)
    n = len(preds)
    score_fn = brier_score_binary if scale == "0-1" else brier_score_two_option
    score = score_fn(preds)

    if n < MODEST_N:
        verdict = None
        note = (
            f"n={n} is below {MODEST_N}. No calibration claim of any kind -- keep logging "
            "predictions before you know the outcome (patio11's prediction-then-score loop, "
            "references/forecasting-honesty.md SS6)."
        )
    elif n < STRICT_N:
        verdict = "directional-only"
        note = (
            f"n={n} is below the {STRICT_N} the Brier-score literature names for reliably "
            "scoring skill at rare/high-skill events (Wikipedia's Brier score article). This "
            "score is directional, not a validated calibration claim. Most solo pipelines will "
            "sit in this tier indefinitely -- that is the honest state, not a tool limitation."
        )
    else:
        verdict = "scored"
        note = (
            f"n={n} meets the {STRICT_N}-sample threshold; a calibration verdict is supportable."
        )

    return {"n": n, "scale": scale, "score": round(score, 4), "verdict": verdict, "note": note}


def _self_test():
    # Wikipedia's 0-1 scale, single case.
    s = brier_score_binary([(0.7, 1)])
    assert abs(s - 0.09) < 1e-9, f"Wikipedia 0-1 anchor failed: got {s}"

    # Good Judgment Open's 0-2 scale, same input, documented worked example -> 0.18.
    s2 = brier_score_two_option([(0.7, 1)])
    assert abs(s2 - 0.18) < 1e-9, f"GJ Open 0-2 anchor failed: got {s2}"

    # The two scales must never silently agree on a nontrivial case -- confirms they are
    # genuinely different formulas, not the same code path under two names.
    assert abs(s - s2) > 1e-9

    # Below MODEST_N: no verdict.
    small = assess_calibration([(0.6, 1)] * 10)
    assert small["verdict"] is None
    assert small["n"] == 10

    # Between MODEST_N and STRICT_N: directional-only, never a pass/fail claim.
    mid = assess_calibration([(0.6, 1)] * 100)
    assert mid["verdict"] == "directional-only"

    # At or above STRICT_N: a verdict may be rendered.
    big = assess_calibration([(0.6, 1)] * 1000)
    assert big["verdict"] == "scored"

    # Invalid inputs raise rather than silently coercing.
    try:
        assess_calibration([])
        raise AssertionError("expected ValueError for empty predictions")
    except ValueError:
        pass


_self_test()  # runs at import, per this asset's self-testing requirement


def main():
    p = argparse.ArgumentParser(
        description="Score a prediction-then-score log. Refuses a calibration verdict below "
        "an honest sample size; always computes the raw score."
    )
    p.add_argument(
        "--predictions",
        nargs="+",
        required=False,
        help="space-separated forecast,outcome pairs, e.g. 0.7,1 0.3,0 0.9,1 "
        "(outcome: 1=closed won, 0=closed lost)",
    )
    p.add_argument(
        "--scale",
        choices=["0-1", "0-2"],
        default="0-1",
        help="0-1 = standard single-outcome Brier (default); 0-2 = Good Judgment Open's "
        "multi-option formulation. Never compare scores across scales.",
    )
    p.add_argument("--selftest", action="store_true", help="run the self-test and exit")
    args = p.parse_args()

    if args.selftest:
        _self_test()
        print("forecast_calibration_check.py: self-test passed.")
        return

    if not args.predictions:
        p.error("--predictions is required outside --selftest, e.g. --predictions 0.7,1 0.3,0")

    parsed = []
    for entry in args.predictions:
        try:
            f_str, o_str = entry.split(",")
            parsed.append((float(f_str), int(o_str)))
        except ValueError:
            p.error(f"malformed prediction '{entry}', expected 'forecast,outcome' e.g. '0.7,1'")

    result = assess_calibration(parsed, scale=args.scale)
    print(f"n={result['n']}  scale={result['scale']}  brier_score={result['score']}")
    print(f"verdict: {result['verdict'] or '(none)'}")
    print(result["note"])


if __name__ == "__main__":
    main()
