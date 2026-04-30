#!/usr/bin/env python3
"""Search for hbar-free universal word primitives for the quantum shear defect.

This script is the next layer above ``quantum_shear_primitive_search.py``.
For fixed ``a,b`` it keeps the unknown primitive in the free word span

    sum_W c_W Tr(W M),

where ``W`` has ``a-1`` letters ``X`` and ``b-1`` letters ``Y`` and

    Tr(W M) = sum_{i,j} W^j_i M^i_j

is always interpreted as a left-ideal expression.  The search first imposes
the universal cyclic trace identity at ``hbar = 0``.  It may also impose exact
finite-rank Weyl-algebra rows with the same coefficients.  The finite rows are
evidence for the quantum lift; they are not an all-N proof.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Dict, Iterable, List, Sequence, Tuple

from quantum_shear_primitive_search import MatrixWeyl, frac_str, poly_equal, solve_sparse


Word = Tuple[str, ...]
FreeVector = Dict[Word, Fraction]
TaggedKey = Tuple[object, ...]
TaggedPoly = Dict[TaggedKey, Fraction]


DEFAULT_CASES: Tuple[Tuple[int, int], ...] = (
    (2, 2),
    (2, 3),
    (3, 2),
    (3, 3),
    (2, 4),
    (4, 2),
    (3, 4),
    (4, 3),
    (2, 5),
    (5, 2),
    (4, 4),
)


def words_with_counts(x_count: int, y_count: int) -> Iterable[Word]:
    length = x_count + y_count
    for x_positions in combinations(range(length), x_count):
        x_set = set(x_positions)
        yield tuple("X" if pos in x_set else "Y" for pos in range(length))


def cyclic_key(word: Word) -> Word:
    if not word:
        return ()
    return min(word[pos:] + word[:pos] for pos in range(len(word)))


def word_label(word: Word) -> str:
    return "".join(word) if word else "I"


def add_free(vector: FreeVector, key: Word, coeff: Fraction) -> None:
    if coeff == 0:
        return
    vector[key] = vector.get(key, Fraction(0)) + coeff
    if vector[key] == 0:
        del vector[key]


def add_tagged(target: TaggedPoly, source: TaggedPoly) -> TaggedPoly:
    out = dict(target)
    for key, coeff in source.items():
        out[key] = out.get(key, Fraction(0)) + coeff
        if out[key] == 0:
            del out[key]
    return out


def tag_free(prefix: str, vector: FreeVector) -> TaggedPoly:
    return {(prefix, key): coeff for key, coeff in vector.items()}


def tag_finite(rank: int, poly: Dict[object, Fraction]) -> TaggedPoly:
    return {("rank", rank, key): coeff for key, coeff in poly.items()}


def free_classical_target(a: int, b: int) -> FreeVector:
    """Classical cyclic trace vector of the shear defect.

    This is

        sum_j Tr(Y^j X^a Y^{b-j})
        - (b+1) / binom(a+b,a) * sum_{shuffle} Tr(shuffle(X^a,Y^b))

    in the cyclic word vector space.
    """

    vector: FreeVector = {}
    for j in range(b + 1):
        word = tuple("Y" for _ in range(j))
        word += tuple("X" for _ in range(a))
        word += tuple("Y" for _ in range(b - j))
        add_free(vector, cyclic_key(word), Fraction(1))

    shuffles = list(words_with_counts(a, b))
    if not shuffles:
        return vector
    coeff = Fraction(-(b + 1), len(shuffles))
    for word in shuffles:
        add_free(vector, cyclic_key(word), coeff)
    return vector


def free_classical_column(word: Word) -> FreeVector:
    """Classical cyclic vector of Tr(W(YX-XY))."""

    vector: FreeVector = {}
    add_free(vector, cyclic_key(word + ("Y", "X")), Fraction(1))
    add_free(vector, cyclic_key(word + ("X", "Y")), Fraction(-1))
    return vector


def tagged_reconstruct(columns: Sequence[TaggedPoly], coeffs: Dict[int, Fraction]) -> TaggedPoly:
    out: TaggedPoly = {}
    for index, coeff in coeffs.items():
        if coeff == 0:
            continue
        scaled = {key: coeff * value for key, value in columns[index].items()}
        out = add_tagged(out, scaled)
    return out


@dataclass(frozen=True)
class FiniteCheck:
    rank: int
    verified: bool
    target_terms: int
    primitive_terms: int


@dataclass(frozen=True)
class Candidate:
    a: int
    b: int
    words: List[Word]
    coefficients: Dict[int, Fraction]
    consistent: bool
    combined_verified: bool
    rank: int
    rows: int
    columns: int
    solve_ranks: Tuple[int, ...]
    include_classical: bool
    classical_verified: bool
    finite_checks: List[FiniteCheck]

    @property
    def support(self) -> List[Tuple[Word, Fraction]]:
        return [
            (self.words[index], coeff)
            for index, coeff in sorted(self.coefficients.items())
            if coeff
        ]


def auto_solve_ranks(a: int, b: int) -> Tuple[int, ...]:
    total = a + b
    if total <= 7:
        return (2, 3)
    return (2,)


def auto_verify_ranks(a: int, b: int) -> Tuple[int, ...]:
    total = a + b
    ranks: List[int] = [2]
    if total <= 7:
        ranks.append(3)
    if total <= 5:
        ranks.append(4)
    return tuple(ranks)


def parse_rank_list(raw: str) -> Tuple[int, ...]:
    try:
        ranks = tuple(int(part) for part in raw.split(",") if part)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("ranks must be comma-separated integers") from exc
    if not ranks or any(rank < 1 for rank in ranks):
        raise argparse.ArgumentTypeError("ranks must be positive")
    return ranks


def parse_case(raw: str) -> Tuple[int, int]:
    pieces = raw.split(",")
    if len(pieces) != 2:
        raise argparse.ArgumentTypeError("case must have form a,b")
    try:
        a, b = (int(piece) for piece in pieces)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("case entries must be integers") from exc
    if a < 0 or b < 0:
        raise argparse.ArgumentTypeError("require a,b >= 0")
    return a, b


def solve_candidate(
    a: int,
    b: int,
    solve_ranks: Sequence[int],
    verify_ranks: Sequence[int],
    include_classical: bool,
) -> Candidate:
    if a <= 1 or b <= 1:
        finite_checks = []
        for rank in verify_ranks:
            algebra = MatrixWeyl(rank)
            target = algebra.shear_defect(a, b)
            finite_checks.append(FiniteCheck(rank, not target, len(target), 0))
        return Candidate(
            a=a,
            b=b,
            words=[],
            coefficients={},
            consistent=all(check.verified for check in finite_checks),
            combined_verified=all(check.verified for check in finite_checks),
            rank=0,
            rows=0,
            columns=0,
            solve_ranks=tuple(solve_ranks),
            include_classical=include_classical,
            classical_verified=not free_classical_target(a, b),
            finite_checks=finite_checks,
        )

    words = list(words_with_counts(a - 1, b - 1))
    algebras = {rank: MatrixWeyl(rank) for rank in solve_ranks}
    columns: List[TaggedPoly] = []

    for word in words:
        column: TaggedPoly = {}
        if include_classical:
            column = add_tagged(column, tag_free("classical", free_classical_column(word)))
        for rank, algebra in algebras.items():
            column = add_tagged(column, tag_finite(rank, algebra.trace_word_times_moment(word)))
        columns.append(column)

    target: TaggedPoly = {}
    if include_classical:
        target = add_tagged(target, tag_free("classical", free_classical_target(a, b)))
    for rank, algebra in algebras.items():
        target = add_tagged(target, tag_finite(rank, algebra.shear_defect(a, b)))

    solution = solve_sparse(columns, target)
    reconstructed = tagged_reconstruct(columns, solution.coefficients) if solution.consistent else {}
    combined_verified = solution.consistent and reconstructed == target

    classical_verified = True
    if include_classical and solution.consistent:
        classical_sum: FreeVector = {}
        for index, coeff in solution.coefficients.items():
            for key, value in free_classical_column(words[index]).items():
                add_free(classical_sum, key, coeff * value)
        classical_verified = classical_sum == free_classical_target(a, b)
    elif include_classical:
        classical_verified = False

    finite_checks = verify_candidate(a, b, words, solution.coefficients, verify_ranks)
    return Candidate(
        a=a,
        b=b,
        words=words,
        coefficients=solution.coefficients,
        consistent=solution.consistent,
        combined_verified=combined_verified,
        rank=solution.rank,
        rows=solution.row_count,
        columns=solution.column_count,
        solve_ranks=tuple(solve_ranks),
        include_classical=include_classical,
        classical_verified=classical_verified,
        finite_checks=finite_checks,
    )


def verify_candidate(
    a: int,
    b: int,
    words: Sequence[Word],
    coefficients: Dict[int, Fraction],
    ranks: Sequence[int],
) -> List[FiniteCheck]:
    checks: List[FiniteCheck] = []
    for rank in ranks:
        algebra = MatrixWeyl(rank)
        target = algebra.shear_defect(a, b)
        primitive = {}
        for index, coeff in coefficients.items():
            primitive = algebra.add(
                primitive,
                algebra.scale(coeff, algebra.trace_word_times_moment(words[index])),
            )
        checks.append(
            FiniteCheck(
                rank=rank,
                verified=poly_equal(primitive, target),
                target_terms=len(target),
                primitive_terms=len(primitive),
            )
        )
    return checks


def format_support(candidate: Candidate, max_terms: int) -> List[str]:
    support = candidate.support
    if not support:
        return []
    if len(support) > max_terms:
        return [f"  support omitted: {len(support)} terms exceeds --max-terms={max_terms}"]
    lines = []
    for word, coeff in support:
        lines.append(f"  {frac_str(coeff):>7} * Tr({word_label(word)} M)")
    return lines


def print_candidate(candidate: Candidate, max_terms: int) -> None:
    ok = (
        candidate.consistent
        and candidate.combined_verified
        and candidate.classical_verified
        and all(check.verified for check in candidate.finite_checks)
    )
    status = "PASS" if ok else "FAIL"
    classical = "yes" if candidate.include_classical else "no"
    solve_ranks = ",".join(str(rank) for rank in candidate.solve_ranks) or "none"
    checks = " ".join(
        f"N={check.rank}:{'ok' if check.verified else 'fail'}"
        f"[{check.target_terms}->{check.primitive_terms}]"
        for check in candidate.finite_checks
    )
    print(
        f"{status} a={candidate.a} b={candidate.b} "
        f"unknowns={candidate.columns} rank={candidate.rank} rows={candidate.rows} "
        f"solve_classical={classical} solve_ranks={solve_ranks} "
        f"classical={'ok' if candidate.classical_verified else 'fail'} "
        f"support={len(candidate.support)} verify={checks}"
    )
    for line in format_support(candidate, max_terms):
        print(line)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        type=parse_case,
        help="case a,b. May be repeated. Defaults to the expanded low-degree window.",
    )
    parser.add_argument(
        "--solve-ranks",
        type=parse_rank_list,
        help="comma-separated finite ranks imposed while solving. Default is automatic per case.",
    )
    parser.add_argument(
        "--verify-ranks",
        type=parse_rank_list,
        help="comma-separated finite ranks verified after solving. Default is automatic per case.",
    )
    parser.add_argument(
        "--no-classical",
        action="store_true",
        help="do not impose the universal hbar=0 cyclic trace equation.",
    )
    parser.add_argument(
        "--classical-only",
        action="store_true",
        help="solve only the universal hbar=0 cyclic trace equation, then run finite verification.",
    )
    parser.add_argument(
        "--max-terms",
        type=int,
        default=16,
        help="maximum primitive support terms printed per case.",
    )
    args = parser.parse_args()
    if args.classical_only and args.solve_ranks is not None:
        parser.error("--classical-only cannot be combined with --solve-ranks")
    if args.classical_only and args.no_classical:
        parser.error("--classical-only cannot be combined with --no-classical")

    cases = args.case if args.case else list(DEFAULT_CASES)
    print("Quantum shear universal formula search")
    print("unknowns: hbar-free free words W with #X=a-1 and #Y=b-1")
    print("left convention: Tr(W M)=sum_{i,j} W^j_i M^i_j")
    print("finite rows are evidence only; all-N proof requires a free indexed normal-ordering lemma")
    print()

    failed = 0
    for a, b in cases:
        if args.classical_only:
            solve_ranks = ()
        else:
            solve_ranks = args.solve_ranks if args.solve_ranks is not None else auto_solve_ranks(a, b)
        verify_ranks = args.verify_ranks if args.verify_ranks is not None else auto_verify_ranks(a, b)
        candidate = solve_candidate(
            a,
            b,
            solve_ranks=solve_ranks,
            verify_ranks=verify_ranks,
            include_classical=not args.no_classical,
        )
        print_candidate(candidate, args.max_terms)
        if not (
            candidate.consistent
            and candidate.combined_verified
            and candidate.classical_verified
            and all(check.verified for check in candidate.finite_checks)
        ):
            failed += 1

    print()
    if failed:
        print(f"FAIL: {failed} case(s) did not produce a verified free-word candidate.")
        return 1
    print(f"PASS: {len(cases)} case(s) produced verified free-word candidates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
