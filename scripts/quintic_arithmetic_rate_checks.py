#!/usr/bin/env python3
"""Reproducible arithmetic checks for the quintic rate ledger.

The checks separate three kinds of evidence.

1. Source-row checks: the local BCOV and HKQ mirrors contain the finite
   genus-zero entries used in the small-degree table, and the local OSV mirror
   contains no source line for ``5 log 5`` or ``5^{-5}``.
2. Elementary finite arithmetic: the values a_N = log(n_N)/N, the monotone
   tail increments, and the three-parameter least-squares fit.
3. CDGP-coordinate numerical arithmetic: after accepting the coordinate
   convention z_c = 5^{-5} and the displayed raw logarithmic-period formula,
   evaluate the boundary period ratio by high-precision accelerated summation.

The script does not prove CDGP formula transcription, Abel-Jacobi
normalisation, OSV fixed-class growth, GV convergence, or CoHA transfer.
Those are source/theorem obligations recorded in the companion ledger.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import mpmath as mp
except ImportError as exc:  # pragma: no cover - explicit runtime dependency.
    raise SystemExit("mpmath is required for the boundary period check") from exc


ROOT = Path(__file__).resolve().parents[1]

BPS_COUNTS = {
    1: 2875,
    2: 609250,
    3: 317206375,
    4: 242467530000,
    5: 229305888887625,
    6: 248249742118022000,
    7: 295091050570845659250,
    8: 375632160937476603550000,
    9: 503840510416985243645106250,
    10: 704288164978454686113488249750,
}

OSV_FORBIDDEN_PATTERNS = (
    "5 log 5",
    r"5\log 5",
    r"5\log",
    r"\log 5",
    "log(5",
    "5^{-5}",
    "5^-5",
    "5^(-5)",
)

# Previous local fixture value. Kept only to expose the attack: accelerated
# boundary summation does not reproduce this last-six-decimal value.
LEGACY_PERIOD_RATIO = "7.59089622312577943"


def require_file(relative: str) -> str:
    path = ROOT / relative
    if not path.exists():
        raise AssertionError(f"missing required local file: {relative}")
    return path.read_text(encoding="utf-8", errors="replace")


def source_row_checks() -> dict[str, str | bool]:
    bcov = require_file("references/primary-sources/bcov-hep-th-9309140.txt")
    hkq = require_file(
        "references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex"
    )
    osv_tex = require_file("references/primary-sources/osv-hep-th-0405146.tex")
    osv_txt = require_file("references/primary-sources/osv-hep-th-0405146.txt")
    osv = osv_tex + "\n" + osv_txt

    missing_bcov = [n for n in range(1, 10) if str(BPS_COUNTS[n]) not in bcov]
    if missing_bcov:
        raise AssertionError(f"BCOV mirror lacks entries: {missing_bcov}")

    if str(BPS_COUNTS[10]) not in hkq:
        raise AssertionError("HKQ mirror lacks the n^0_10 row")

    osv_hits = [pattern for pattern in OSV_FORBIDDEN_PATTERNS if pattern in osv]
    if osv_hits:
        raise AssertionError(f"OSV mirror contains forbidden rate hits: {osv_hits}")

    return {
        "bcov_n1_to_n9_present": True,
        "hkq_n10_present": True,
        "osv_5log5_hits": False,
    }


def a_values() -> dict[int, mp.mpf]:
    return {n: mp.log(value) / n for n, value in BPS_COUNTS.items()}


def fit_tail(values: dict[int, mp.mpf]) -> tuple[mp.mpf, mp.mpf, mp.mpf, list[mp.mpf]]:
    rows = []
    rhs = []
    for n in range(5, 11):
        rows.append([mp.mpf(1), mp.log(n) / n, mp.mpf(1) / n])
        rhs.append(values[n])

    matrix = mp.matrix(rows)
    target = mp.matrix(rhs)
    coeffs = mp.lu_solve(matrix.T * matrix, matrix.T * target)
    residuals = [
        rhs[i] - sum(rows[i][j] * coeffs[j] for j in range(3))
        for i in range(len(rhs))
    ]
    return coeffs[0], coeffs[1], coeffs[2], residuals


def base_period_term(n: mp.mpf) -> mp.mpf:
    fifth = mp.mpf(1) / 5
    return (
        mp.rf(fifth, n)
        * mp.rf(2 * fifth, n)
        * mp.rf(3 * fifth, n)
        * mp.rf(4 * fifth, n)
        / (mp.factorial(n) ** 4)
    )


def period_values() -> dict[str, mp.mpf]:
    z_c = mp.power(5, -5)
    log_z = mp.log(z_c)

    omega0_nsum = mp.nsum(lambda k: base_period_term(k), [0, mp.inf])
    omega0_hyper = mp.hyper(
        [mp.mpf(1) / 5, mp.mpf(2) / 5, mp.mpf(3) / 5, mp.mpf(4) / 5],
        [1, 1, 1],
        1,
    )
    if abs(omega0_nsum - omega0_hyper) > mp.mpf("1e-60"):
        raise AssertionError("omega0 nsum and hypergeometric evaluations disagree")

    def combined_log_term(k: mp.mpf) -> mp.mpf:
        return base_period_term(k) * (
            log_z + 5 * (mp.digamma(5 * k + 1) - mp.digamma(k + 1))
        )

    omega1 = log_z + mp.nsum(lambda k: combined_log_term(k), [1, mp.inf])
    ratio = abs(omega1 / omega0_nsum)
    return {
        "z_c": z_c,
        "omega0": omega0_nsum,
        "omega1": omega1,
        "ratio": ratio,
        "legacy_ratio_delta": mp.mpf(LEGACY_PERIOD_RATIO) - ratio,
    }


def check_rate_identity(z_c: mp.mpf) -> mp.mpf:
    left = 5 * mp.log(5)
    right = -mp.log(z_c)
    delta = left - right
    if abs(delta) > mp.mpf("1e-70"):
        raise AssertionError("5 log 5 identity failed")
    return left


def fmt(value: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(value, digits)


def main() -> int:
    mp.mp.dps = 80

    scans = source_row_checks()
    values = a_values()
    l_value, alpha, beta, residuals = fit_tail(values)
    periods = period_values()
    rate = check_rate_identity(periods["z_c"])

    increments = {n: values[n + 1] - values[n] for n in range(3, 10)}
    if not all(delta > 0 for delta in increments.values()):
        raise AssertionError("tail monotonicity from N=3 to N=10 failed")

    max_residual = max(abs(residual) for residual in residuals)
    if max_residual >= mp.mpf("5e-6"):
        raise AssertionError("tail-fit residual exceeds ledger tolerance")

    print("source_row_checks")
    for key, value in scans.items():
        print(f"  {key}: {value}")

    print("a_N")
    for n in range(1, 11):
        print(f"  a_{n}: {fmt(values[n], 24)}")

    print("tail_increments")
    for n in range(3, 10):
        print(f"  a_{n + 1}-a_{n}: {fmt(increments[n], 24)}")

    print("tail_fit_N_5_to_10")
    print(f"  L: {fmt(l_value, 24)}")
    print(f"  alpha: {fmt(alpha, 24)}")
    print(f"  beta: {fmt(beta, 24)}")
    print(f"  max_abs_residual: {fmt(max_residual, 24)}")

    print("period_at_z_c")
    print(f"  z_c: {fmt(periods['z_c'], 24)}")
    print(f"  omega0: {fmt(periods['omega0'], 24)}")
    print(f"  omega1: {fmt(periods['omega1'], 24)}")
    print(f"  abs_omega1_over_omega0: {fmt(periods['ratio'], 24)}")
    print(f"  legacy_ratio_delta: {fmt(periods['legacy_ratio_delta'], 24)}")

    print("rate_identity")
    print(f"  5_log_5: {fmt(rate, 24)}")
    print(f"  -log_z_c: {fmt(-mp.log(periods['z_c']), 24)}")
    print("all_checks_passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
