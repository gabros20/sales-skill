#!/usr/bin/env python3
"""
coverage_calc.py -- pipeline coverage = 1 / win rate, with the denominator forced into the open.

"Coverage" answers: how much pipeline (open deal value tracked toward close) do you need to carry
to reach a bookings target, given your own win rate? The arithmetic is a tautology, not a finding:
coverage = 1 / win_rate. GitLab's own capacity-planning page states a 33% win-rate assumption,
"This is a calculation only and should be used to set goals and plan" -- not a measurement --
(content/handbook/sales/field-operations/gtm-resources/_index.md, gitlab-com/content-sites/
handbook), and 1/0.33 ~= 3.03, which is where the "3x" a reader may have heard elsewhere comes
from. The same "3-to-1... 5-to-1" figure circulates on X with no source and no stated denominator
(https://x.com/gtmba_/status/2041174257271480446, FOLKLORE). See references/forecasting-honesty.md
SS4 for the full derivation and both citations.

**A win rate without its denominator is not a number.** This script refuses to compute a coverage
ratio unless the caller also states what is being counted -- e.g. "closed-won / total qualified
opportunities entering the pipeline in Q1" -- because the same 33% means something different
depending on whether the denominator is "opportunities that reached Discovery" or "all inbound
leads." The --denominator argument is not optional and is echoed back in the output so it travels
with the number.

Self-test anchors (run automatically at import, and again before any CLI use):
  - GitLab's 33% planning assumption -> ~3.03x coverage.
  - win_rate = 1.0 -> exactly 1x (every deal that enters the pipeline closes).
  - win_rate outside (0, 1] raises ValueError.
  - Missing or blank --denominator raises ValueError from the format_result path.
"""
import argparse


def required_coverage(win_rate):
    """coverage = 1 / win_rate. win_rate must be a fraction in (0, 1]."""
    if not (0 < win_rate <= 1):
        raise ValueError(
            f"win_rate must be greater than 0 and at most 1 (got {win_rate}); "
            "a win rate of 0 makes coverage undefined, not infinite-but-computable"
        )
    return 1 / win_rate


def format_result(win_rate, denominator):
    """Refuses to produce output without a stated denominator -- a win rate without its
    denominator is not a number (see references/forecasting-honesty.md SS4)."""
    if not denominator or not denominator.strip():
        raise ValueError(
            "denominator is required: state what is being counted, e.g. "
            "'closed-won / total qualified opportunities entering the pipeline in Q1'. "
            "Never report a win rate or a coverage ratio without it."
        )
    coverage = required_coverage(win_rate)
    return {
        "win_rate": win_rate,
        "denominator": denominator.strip(),
        "coverage_ratio": round(coverage, 2),
        "derivation": f"1 / {win_rate} = {coverage:.4f}, rounded to {round(coverage, 2)}x",
        "warning": (
            "This is arithmetic, not a validated benchmark. Never present the resulting "
            "ratio, or any other coverage figure (e.g. '3x'), as a portable constant -- "
            "derive it fresh from your own win rate and denominator every time. See "
            "references/forecasting-honesty.md SS4."
        ),
    }


def _self_test():
    # GitLab's own planning-only 33% win-rate assumption.
    gitlab_coverage = required_coverage(0.33)
    assert abs(gitlab_coverage - 3.0303030303030303) < 1e-9, (
        f"GitLab anchor failed: got {gitlab_coverage}"
    )
    assert round(gitlab_coverage, 2) == 3.03

    # win_rate = 1.0 -> exactly 1x.
    assert required_coverage(1.0) == 1.0

    # win_rate = 0.25 -> 4x. Illustrative arithmetic only, not an empirical benchmark.
    assert required_coverage(0.25) == 4.0

    # Invalid win rates must raise, never silently clamp.
    for bad in (0, -0.1, 1.5):
        try:
            required_coverage(bad)
            raise AssertionError(f"expected ValueError for win_rate={bad}")
        except ValueError:
            pass

    # format_result refuses a missing/blank denominator.
    for bad_denom in (None, "", "   "):
        try:
            format_result(0.33, bad_denom)
            raise AssertionError(f"expected ValueError for denominator={bad_denom!r}")
        except ValueError:
            pass

    # format_result succeeds with a real denominator and echoes it back verbatim.
    result = format_result(0.33, "closed-won / total qualified opportunities entering Q1")
    assert result["coverage_ratio"] == 3.03
    assert result["denominator"] == "closed-won / total qualified opportunities entering Q1"


_self_test()  # runs at import, per this asset's self-testing requirement


def main():
    p = argparse.ArgumentParser(
        description="Pipeline coverage = 1 / win rate. Refuses to compute without a stated "
        "denominator -- a win rate without its denominator is not a number."
    )
    p.add_argument("--win-rate", type=float, help="win rate as a fraction, e.g. 0.33 for 33%")
    p.add_argument(
        "--denominator",
        type=str,
        help="what the win rate is counted over, e.g. "
        "'closed-won / total qualified opportunities entering the pipeline in Q1'",
    )
    p.add_argument("--selftest", action="store_true", help="run the self-test and exit")
    args = p.parse_args()

    if args.selftest:
        _self_test()
        print("coverage_calc.py: self-test passed.")
        return

    if args.win_rate is None or args.denominator is None:
        p.error(
            "--win-rate and --denominator are both required outside --selftest. "
            "This script will not guess a denominator for you."
        )

    result = format_result(args.win_rate, args.denominator)
    print(f"win rate: {result['win_rate']} (of: {result['denominator']})")
    print(f"coverage ratio: {result['coverage_ratio']}x")
    print(f"derivation: {result['derivation']}")
    print(result["warning"])


if __name__ == "__main__":
    main()
