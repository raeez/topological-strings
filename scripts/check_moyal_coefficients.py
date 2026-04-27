#!/usr/bin/env python3
"""Check the monomial Moyal coefficients used in main.tex.

The script is intentionally dependency-free.  Polynomials are dictionaries
mapping exponent pairs (a, b) to rational coefficients, representing
z1^a z2^b.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


Poly = dict[tuple[int, int], Fraction]


def falling(n: int, r: int) -> int:
    out = 1
    for i in range(r):
        out *= n - i
    return out


def monomial(a: int, b: int, coeff: Fraction = Fraction(1)) -> Poly:
    if a < 0 or b < 0 or coeff == 0:
        return {}
    return {(a, b): coeff}


def add(p: Poly, q: Poly) -> Poly:
    out = dict(p)
    for exp, coeff in q.items():
        out[exp] = out.get(exp, Fraction(0)) + coeff
        if out[exp] == 0:
            del out[exp]
    return out


def scale(c: Fraction, p: Poly) -> Poly:
    return {exp: c * coeff for exp, coeff in p.items() if c * coeff}


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for (a, b), c in p.items():
        for (m, n), d in q.items():
            exp = (a + m, b + n)
            out[exp] = out.get(exp, Fraction(0)) + c * d
    return {exp: coeff for exp, coeff in out.items() if coeff}


def diff(p: Poly, dz1: int, dz2: int) -> Poly:
    out: Poly = {}
    for (a, b), coeff in p.items():
        if a < dz1 or b < dz2:
            continue
        out[(a - dz1, b - dz2)] = coeff * falling(a, dz1) * falling(b, dz2)
    return out


def p_power(f: Poly, g: Poly, r: int) -> Poly:
    """Apply P^r to f tensor g and multiply the two outputs."""
    out: Poly = {}
    for a in range(r + 1):
        term = mul(diff(f, r - a, a), diff(g, a, r - a))
        out = add(out, scale(Fraction((-1) ** a * comb(r, a)), term))
    return out


def commutator_coeff(f: Poly, g: Poly, r: int) -> Poly:
    """Coefficient of hbar^r in f*g-g*f, without the 1/(2^r r!) factor."""
    return add(p_power(f, g, r), scale(Fraction(-1), p_power(g, f, r)))


def star_commutator_coeff(f: Poly, g: Poly, r: int) -> Poly:
    """Coefficient of hbar^r in the Weyl/Moyal star commutator."""
    return scale(
        Fraction(1, 2**r),
        scale(Fraction(1, factorial(r)), commutator_coeff(f, g, r)),
    )


def expected_star_commutator_coeff(f: Poly, g: Poly, r: int) -> Poly:
    """All-order coefficient forced by P^r(g,f)=(-1)^r P^r(f,g)."""
    if r == 0 or r % 2 == 0:
        return {}
    return scale(Fraction(1, 2 ** (r - 1) * factorial(r)), p_power(f, g, r))


def expected_p1(k: int, l: int, m: int, n: int) -> Poly:
    return monomial(k + m - 1, l + n - 1, Fraction(k * n - l * m))


def expected_p3(k: int, l: int, m: int, n: int) -> Poly:
    coeff = 0
    for a in range(4):
        coeff += (
            (-1) ** a
            * comb(3, a)
            * falling(k, 3 - a)
            * falling(l, a)
            * falling(m, a)
            * falling(n, 3 - a)
        )
    return monomial(k + m - 3, l + n - 3, Fraction(coeff))


def run() -> None:
    max_exp = 10
    max_order = 11
    checked = 0
    for k in range(max_exp + 1):
        for l in range(max_exp + 1):
            for m in range(max_exp + 1):
                for n in range(max_exp + 1):
                    f = monomial(k, l)
                    g = monomial(m, n)
                    assert p_power(f, g, 1) == expected_p1(k, l, m, n)
                    assert star_commutator_coeff(f, g, 1) == expected_p1(
                        k, l, m, n
                    )
                    assert star_commutator_coeff(f, g, 2) == {}
                    assert p_power(f, g, 3) == expected_p3(k, l, m, n)
                    assert star_commutator_coeff(f, g, 3) == scale(
                        Fraction(1, 24), expected_p3(k, l, m, n)
                    )
                    for r in range(max_order + 1):
                        assert p_power(g, f, r) == scale(
                            Fraction((-1) ** r), p_power(f, g, r)
                        )
                        assert star_commutator_coeff(
                            f, g, r
                        ) == expected_star_commutator_coeff(f, g, r)
                    checked += 1
    print(
        "checked "
        f"{checked} Moyal coefficient cases with exponents <= {max_exp} "
        f"and orders <= {max_order}"
    )
    for r in range(1, max_order + 1, 2):
        print(f"r={r}: odd commutator coefficient = 1/{2 ** (r - 1) * factorial(r)}")


if __name__ == "__main__":
    run()
