#!/usr/bin/env python3
"""W12 Wave-3 independent verification at 10x scale of W3 finding W3-W3-02.

Tests the corrected indicator-free bi-infinite Lie-module formula

    z_1^p z_2^q . v_{a, b} = (p b - q a) v_{a + p - 1, b + q - 1}

on Z^2 \\ {(0, 0)}, with mod-constants projection (target (0, 0) -> 0).

Cross-tested against the W3-flagged buggy indicator formula

    z_1^p z_2^q . v_{a, b} = (p b - q a - (p - q) * 1[a < 0])
                              v_{a + p - 1, b + q - 1},

verifying [z_1^{p1} z_2^{q1}, z_1^{p2} z_2^{q2}] . v_{a, b}
   ?=  (p_1 q_2 - p_2 q_1) z_1^{p1+p2-1} z_2^{q1+q2-1} . v_{a, b}
on rational/integer arithmetic (no float).

Scale: at least 50,000 commutator instances. Concretely we run two
sweeps with different (max_pq, max_abs) windows. Counts and a sample
of failures are printed to stdout.

Findings rationale: the corrected formula coincides with the standard
Hamiltonian Poisson action of bar A = C[z_1^pm, z_2^pm] / C on itself
on the punctured plane Z^2 \\ {(0, 0)}, which IS a Lie module of bar A
by abstract nonsense (associative algebra acting on itself by Poisson
bracket and projecting). The indicator-broken formula cannot be a Lie
module, since Lie consistency fails on a positive-density subset of
commutators. We re-verify both in this script.
"""

from __future__ import annotations

from fractions import Fraction


# ---------------------------------------------------------------------------
# Two candidate bi-infinite v-frame actions
# ---------------------------------------------------------------------------


def biinf_corrected(p: int, q: int, a: int, b: int):
    """W3-corrected indicator-free formula with mod-constants projection.

    Returns (target_a, target_b, integer_coefficient) or None if the
    output is zero (origin source, zero coefficient, or origin target).
    """
    if a == 0 and b == 0:
        return None
    coeff = p * b - q * a
    if coeff == 0:
        return None
    ta = a + p - 1
    tb = b + q - 1
    if ta == 0 and tb == 0:
        return None  # mod-constants projection
    return (ta, tb, coeff)


def biinf_buggy(p: int, q: int, a: int, b: int):
    """Wave-2 W4 §4 indicator formula. Same truncations as above."""
    if a == 0 and b == 0:
        return None
    indicator = 1 if a < 0 else 0
    coeff = p * b - q * a - (p - q) * indicator
    if coeff == 0:
        return None
    ta = a + p - 1
    tb = b + q - 1
    if ta == 0 and tb == 0:
        return None
    return (ta, tb, coeff)


# ---------------------------------------------------------------------------
# Commutator vs Poisson-bracket-action consistency
# ---------------------------------------------------------------------------


def left_action(action_fn, p: int, q: int, vec):
    """Apply action_fn(p, q, ., .) to a finite linear combination.

    vec is a dict {(a, b): coeff} with integer / Fraction coeffs.
    Returns a new dict. Uses Fraction for safety though all inputs
    here are integer.
    """
    out = {}
    for (a, b), c in vec.items():
        r = action_fn(p, q, a, b)
        if r is None:
            continue
        ta, tb, ck = r
        out[(ta, tb)] = out.get((ta, tb), Fraction(0)) + Fraction(c) * Fraction(ck)
    return {k: v for k, v in out.items() if v != 0}


def commutator_action(action_fn, p1: int, q1: int, p2: int, q2: int, a: int, b: int):
    """Compute [(p1, q1), (p2, q2)] acting on v_{a, b} in the prescribed action.

    Returns dict {(ta, tb): coeff}.
    """
    base = {(a, b): Fraction(1)}
    # First order: (p2 q2) then (p1 q1)
    inner1 = left_action(action_fn, p2, q2, base)
    outer1 = left_action(action_fn, p1, q1, inner1)
    # Second order: (p1 q1) then (p2 q2)
    inner2 = left_action(action_fn, p1, q1, base)
    outer2 = left_action(action_fn, p2, q2, inner2)
    out = {}
    keys = set(outer1.keys()) | set(outer2.keys())
    for k in keys:
        out[k] = outer1.get(k, Fraction(0)) - outer2.get(k, Fraction(0))
    return {k: v for k, v in out.items() if v != 0}


def bracket_poisson_target(p1: int, q1: int, p2: int, q2: int):
    """Poisson bracket of monomials:
       {z_1^{p1} z_2^{q1}, z_1^{p2} z_2^{q2}} = (p1 q2 - p2 q1) z_1^{p1+p2-1} z_2^{q1+q2-1}.
    Returns (P, Q, coeff) or None if vanishing or out-of-range exponents.
    """
    coeff = p1 * q2 - p2 * q1
    if coeff == 0:
        return None
    P = p1 + p2 - 1
    Q = q1 + q2 - 1
    if P < 0 or Q < 0:
        return None  # not a polynomial monomial; treat as zero in this sweep
    return (P, Q, coeff)


def expected_commutator(action_fn, p1, q1, p2, q2, a, b):
    """Apply (Poisson bracket of generators) acting on v_{a, b}."""
    bracket = bracket_poisson_target(p1, q1, p2, q2)
    if bracket is None:
        return {}
    P, Q, c0 = bracket
    r = action_fn(P, Q, a, b)
    if r is None:
        return {}
    ta, tb, ck = r
    return {(ta, tb): Fraction(c0) * Fraction(ck)}


# ---------------------------------------------------------------------------
# Sweeps
# ---------------------------------------------------------------------------


def sweep(action_fn, max_pq: int, max_abs: int, label: str):
    """Sweep all (p1, q1, p2, q2, a, b) with |p_i|, |q_i| <= max_pq,
    |a|, |b| <= max_abs, (a, b) != (0, 0), (p_i, q_i) != (0, 0).

    Returns (checked, failures, first_examples).
    """
    failures = 0
    checked = 0
    first_examples = []
    for p1 in range(0, max_pq + 1):
        for q1 in range(0, max_pq + 1):
            if p1 + q1 == 0:
                continue
            for p2 in range(0, max_pq + 1):
                for q2 in range(0, max_pq + 1):
                    if p2 + q2 == 0:
                        continue
                    for a in range(-max_abs, max_abs + 1):
                        for b in range(-max_abs, max_abs + 1):
                            if a == 0 and b == 0:
                                continue
                            actual = commutator_action(
                                action_fn, p1, q1, p2, q2, a, b
                            )
                            expected = expected_commutator(
                                action_fn, p1, q1, p2, q2, a, b
                            )
                            checked += 1
                            if actual != expected:
                                failures += 1
                                if len(first_examples) < 5:
                                    first_examples.append({
                                        "p1q1p2q2_ab": (p1, q1, p2, q2, a, b),
                                        "actual": dict(actual),
                                        "expected": dict(expected),
                                    })
    print(f"[{label}] checked = {checked}, failures = {failures}")
    return checked, failures, first_examples


def sweep_negative_pq(action_fn, max_pq: int, max_abs: int, label: str):
    """Same sweep but allows negative p, q in the range [-max_pq, max_pq].

    This pushes us off the polynomial cone into the LAURENT cone, where the
    action z_1^p z_2^q for p, q < 0 is the standard Hamiltonian action of
    Laurent monomials. The formula (p b - q a) is the same; the bracket-
    target formula is (p1 + p2 - 1, q1 + q2 - 1) which can have negative
    exponents (the corresponding generator is a Laurent monomial).
    """
    failures = 0
    checked = 0
    first_examples = []
    for p1 in range(-max_pq, max_pq + 1):
        for q1 in range(-max_pq, max_pq + 1):
            if p1 == 0 and q1 == 0:
                continue
            for p2 in range(-max_pq, max_pq + 1):
                for q2 in range(-max_pq, max_pq + 1):
                    if p2 == 0 and q2 == 0:
                        continue
                    for a in range(-max_abs, max_abs + 1):
                        for b in range(-max_abs, max_abs + 1):
                            if a == 0 and b == 0:
                                continue
                            actual = commutator_action(
                                action_fn, p1, q1, p2, q2, a, b
                            )
                            # Expected: (p1 q2 - p2 q1) z^{p1+p2-1} z^{q1+q2-1}
                            # acting via biinf_corrected. Note the bracket
                            # target may itself land on (0, 0) in exponents,
                            # in which case the corresponding action is zero.
                            coeff0 = p1 * q2 - p2 * q1
                            if coeff0 == 0:
                                expected = {}
                            else:
                                P = p1 + p2 - 1
                                Q = q1 + q2 - 1
                                # If (P, Q) = (0, 0) the bracket monomial is
                                # the constant 1, which acts trivially after
                                # mod-constants reduction. So expected = {}.
                                if P == 0 and Q == 0:
                                    expected = {}
                                else:
                                    r = action_fn(P, Q, a, b)
                                    if r is None:
                                        expected = {}
                                    else:
                                        ta, tb, ck = r
                                        expected = {(ta, tb): Fraction(coeff0) * Fraction(ck)}
                            checked += 1
                            if actual != expected:
                                failures += 1
                                if len(first_examples) < 5:
                                    first_examples.append({
                                        "p1q1p2q2_ab": (p1, q1, p2, q2, a, b),
                                        "actual": dict(actual),
                                        "expected": dict(expected),
                                    })
    print(f"[{label}] checked = {checked}, failures = {failures}")
    return checked, failures, first_examples


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main():
    print("=" * 76)
    print("W12 Wave-3: independent verification of corrected indicator-free")
    print("bi-infinite Lie-consistency at >=50,000 commutator instances")
    print("=" * 76)
    print()

    # Sweep 1: positive (polynomial) cone of generators with broad bidegree
    # window. (p, q) in [0, 3]^2 \\ {(0,0)} with (a, b) in [-7, 7]^2 \\ {(0,0)}
    # gives 15 * 15 * (15*15 - 1) = 50,400 instances.
    print(">>> Sweep A: polynomial generators (p, q) in [0,3]^2, (a,b) in [-7,7]^2")
    cA, fA, eA = sweep(biinf_corrected, max_pq=3, max_abs=7,
                       label="corrected indicator-free")
    cAb, fAb, eAb = sweep(biinf_buggy, max_pq=3, max_abs=7,
                          label="buggy indicator (wave-2 W4 §4)")
    print()

    # Sweep 2: smaller bidegree window but with (p, q) up to 4 and Laurent
    # generators allowed.
    print(">>> Sweep B: polynomial generators (p, q) in [0,4]^2, (a,b) in [-5,5]^2")
    cB, fB, eB = sweep(biinf_corrected, max_pq=4, max_abs=5,
                       label="corrected indicator-free")
    cBb, fBb, eBb = sweep(biinf_buggy, max_pq=4, max_abs=5,
                          label="buggy indicator (wave-2 W4 §4)")
    print()

    # Sweep 3 (Laurent): negative p, q allowed.
    print(">>> Sweep C: Laurent generators (p, q) in [-2,2]^2 \\ {0}, (a,b) in [-4,4]^2")
    cC, fC, eC = sweep_negative_pq(biinf_corrected, max_pq=2, max_abs=4,
                                   label="corrected indicator-free (Laurent)")
    print()

    total_corrected = cA + cB + cC
    total_corrected_fail = fA + fB + fC
    total_buggy = cAb + cBb
    total_buggy_fail = fAb + fBb

    print("=" * 76)
    print("AGGREGATE")
    print("=" * 76)
    print(f"corrected indicator-free formula:")
    print(f"  total instances checked: {total_corrected}")
    print(f"  total Lie-consistency failures: {total_corrected_fail}")
    print()
    print(f"buggy indicator (wave-2 W4 §4) formula:")
    print(f"  total instances checked: {total_buggy}")
    print(f"  total Lie-consistency failures: {total_buggy_fail}")
    print()

    if eAb:
        print("First buggy-indicator failures (sweep A):")
        for ex in eAb[:3]:
            print(f"  {ex}")
        print()
    if eBb:
        print("First buggy-indicator failures (sweep B):")
        for ex in eBb[:3]:
            print(f"  {ex}")
        print()

    if total_corrected_fail == 0 and total_buggy_fail > 0:
        print("VERDICT: W3 finding W3-W3-02 INDEPENDENTLY CONFIRMED at scale.")
        print("The corrected indicator-free formula is Lie-consistent on")
        print(f"all {total_corrected} commutator instances tested.")
        print(f"The buggy indicator formula fails Lie consistency on")
        print(f"{total_buggy_fail} of {total_buggy} instances.")
    elif total_corrected_fail > 0:
        print("ALERT: corrected formula ALSO fails. Investigate.")
    else:
        print("Both formulas pass — unexpected; investigate.")
    print("=" * 76)


if __name__ == "__main__":
    main()
