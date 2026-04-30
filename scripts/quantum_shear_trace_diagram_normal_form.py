#!/usr/bin/env python3
"""Free indexed trace-diagram normal form for the quantum shear defect.

This script works before finite-rank trace identities are imposed.  A
normal diagram is a colored directed graph whose edges are matrix entries;
all X-edges are multiplied before all Y-edges.  A term is

    hbar^p N^q D

where D is a finite disjoint union of nonempty connected normal diagrams.
Isolated index loops are recorded by the explicit power of N.  This is a
free indexed normal form, not a finite-N matrix-entry expansion.

For a trace word Tr(L_1 ... L_m), the normal-ordering formula sums over
partial matchings of inversions (Y-position before X-position).  Each
matched pair contributes -hbar and contracts the two matrix-index lines.
The remaining uncontracted edges form the normal diagram.  This keeps the
split-trace contraction terms which are invisible in the cyclic quotient.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial
from typing import Dict, Iterable, Iterator, List, Sequence, Tuple

from quantum_shear_primitive_search import (
    MatrixWeyl,
    Poly,
    falling,
    frac_str,
    poly_equal,
    solve_sparse,
)


Word = Tuple[str, ...]
Edge = Tuple[str, int, int]
ComponentKey = Tuple[Edge, ...]
GraphKey = Tuple[ComponentKey, ...]
DiagramKey = Tuple[int, int, GraphKey]
DiagramPoly = Dict[DiagramKey, Fraction]
FreeVector = Dict[Word, Fraction]
TaggedKey = Tuple[object, ...]
TaggedPoly = Dict[TaggedKey, Fraction]


LETTER_ORDER = {"X": 0, "Y": 1}


class DisjointSet:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def word_label(word: Sequence[str]) -> str:
    return "".join(word) if word else "I"


def parse_word(raw: str) -> Word:
    letters = tuple(raw.strip())
    if any(letter not in ("X", "Y") for letter in letters):
        raise argparse.ArgumentTypeError("words may contain only X and Y")
    return letters


def add_poly(target: DiagramPoly, key: DiagramKey, coeff: Fraction) -> None:
    if coeff == 0:
        return
    target[key] = target.get(key, Fraction(0)) + coeff
    if target[key] == 0:
        del target[key]


def merge_poly(target: DiagramPoly, source: DiagramPoly, coeff: Fraction = Fraction(1)) -> DiagramPoly:
    out = dict(target)
    for key, value in source.items():
        add_poly(out, key, coeff * value)
    return out


def add_free(vector: FreeVector, key: Word, coeff: Fraction) -> None:
    if coeff == 0:
        return
    vector[key] = vector.get(key, Fraction(0)) + coeff
    if vector[key] == 0:
        del vector[key]


def cyclic_key(word: Word) -> Word:
    if not word:
        return ()
    return min(word[pos:] + word[:pos] for pos in range(len(word)))


def free_classical_target(a: int, b: int) -> FreeVector:
    vector: FreeVector = {}
    for j in range(b + 1):
        word = tuple("Y" for _ in range(j))
        word += tuple("X" for _ in range(a))
        word += tuple("Y" for _ in range(b - j))
        add_free(vector, cyclic_key(word), Fraction(1))

    shuffles = list(words_with_counts(a, b))
    if shuffles:
        coeff = Fraction(-(b + 1), len(shuffles))
        for word in shuffles:
            add_free(vector, cyclic_key(word), coeff)
    return vector


def free_classical_column(word: Word) -> FreeVector:
    vector: FreeVector = {}
    add_free(vector, cyclic_key(word + ("Y", "X")), Fraction(1))
    add_free(vector, cyclic_key(word + ("X", "Y")), Fraction(-1))
    return vector


def tag_poly(prefix: str, poly: Dict[Tuple[object, ...], Fraction]) -> TaggedPoly:
    return {(prefix,) + key: coeff for key, coeff in poly.items()}


def merge_tagged(target: TaggedPoly, source: TaggedPoly, coeff: Fraction = Fraction(1)) -> TaggedPoly:
    out = dict(target)
    for key, value in source.items():
        new_value = out.get(key, Fraction(0)) + coeff * value
        if new_value:
            out[key] = new_value
        elif key in out:
            del out[key]
    return out


def shift_poly(poly: DiagramPoly, hbar_power: int = 0, n_power: int = 0) -> DiagramPoly:
    if hbar_power == 0 and n_power == 0:
        return dict(poly)
    return {
        (h_power + hbar_power, n_pow + n_power, graph): coeff
        for (h_power, n_pow, graph), coeff in poly.items()
    }


def scale_poly(poly: DiagramPoly, coeff: Fraction) -> DiagramPoly:
    if coeff == 0:
        return {}
    return {key: coeff * value for key, value in poly.items() if coeff * value}


def sorted_edges(edges: Iterable[Edge]) -> ComponentKey:
    return tuple(sorted(edges, key=lambda edge: (LETTER_ORDER[edge[0]], edge[1], edge[2])))


@lru_cache(maxsize=None)
def canonical_component(edges: ComponentKey) -> ComponentKey:
    vertices = sorted({src for _, src, _ in edges} | {dst for _, _, dst in edges})
    if not vertices:
        return ()

    cycle = canonical_simple_directed_cycle(edges, vertices)
    if cycle is not None:
        return cycle

    best: ComponentKey | None = None
    for perm in permutations(range(len(vertices))):
        relabel = {vertex: perm[index] for index, vertex in enumerate(vertices)}
        candidate = sorted_edges((letter, relabel[src], relabel[dst]) for letter, src, dst in edges)
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    return best


def canonical_simple_directed_cycle(edges: ComponentKey, vertices: Sequence[int]) -> ComponentKey | None:
    """Canonical form for one-in/one-out directed cycle components.

    The factorial fallback is exact but becomes the bottleneck on the
    uncontracted trace-word terms in bidegrees such as (5,5).  For a
    connected component whose underlying directed multigraph is a directed
    cycle, the directed colour necklace determines the isomorphism type.
    Enumerating the possible roots and the two ways of numbering the same
    directed cycle avoids an n! search.
    """

    if len(edges) != len(vertices):
        return None

    outgoing: Dict[int, Tuple[str, int]] = {}
    incoming_count = {vertex: 0 for vertex in vertices}
    for letter, src, dst in edges:
        if src in outgoing:
            return None
        outgoing[src] = (letter, dst)
        if dst not in incoming_count:
            return None
        incoming_count[dst] += 1

    if set(outgoing) != set(vertices) or any(count != 1 for count in incoming_count.values()):
        return None

    best: ComponentKey | None = None
    vertex_set = set(vertices)
    for start in vertices:
        order: List[int] = []
        current = start
        seen = set()
        while current not in seen:
            if current not in vertex_set:
                break
            seen.add(current)
            order.append(current)
            current = outgoing[current][1]
        if current != start or len(order) != len(vertices):
            continue

        forward = {vertex: index for index, vertex in enumerate(order)}
        reverse = {vertex: (-index) % len(order) for index, vertex in enumerate(order)}
        for relabel in (forward, reverse):
            candidate = sorted_edges((letter, relabel[src], relabel[dst]) for letter, src, dst in edges)
            if best is None or candidate < best:
                best = candidate

    return best


def canonical_graph(edges: Sequence[Edge], vertex_count: int) -> Tuple[int, GraphKey]:
    incident = set()
    for _, src, dst in edges:
        incident.add(src)
        incident.add(dst)
    n_power = vertex_count - len(incident)
    if not edges:
        return n_power, ()

    adjacency = {vertex: set() for vertex in incident}
    for _, src, dst in edges:
        adjacency[src].add(dst)
        adjacency[dst].add(src)

    components: List[ComponentKey] = []
    seen = set()
    for start in sorted(incident):
        if start in seen:
            continue
        stack = [start]
        vertices = set()
        seen.add(start)
        while stack:
            vertex = stack.pop()
            vertices.add(vertex)
            for nxt in adjacency[vertex]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        component_edges = [edge for edge in edges if edge[1] in vertices or edge[2] in vertices]
        components.append(canonical_component(tuple(component_edges)))

    return n_power, tuple(sorted(components))


def inversion_pairs(word: Word) -> List[Tuple[int, int]]:
    return [
        (left, right)
        for left, left_letter in enumerate(word)
        if left_letter == "Y"
        for right in range(left + 1, len(word))
        if word[right] == "X"
    ]


def matchings(word: Word) -> Iterator[Tuple[Tuple[int, int], ...]]:
    pairs = inversion_pairs(word)

    def rec(start: int, used: set[int], current: List[Tuple[int, int]]) -> Iterator[Tuple[Tuple[int, int], ...]]:
        yield tuple(current)
        for index in range(start, len(pairs)):
            left, right = pairs[index]
            if left in used or right in used:
                continue
            used.add(left)
            used.add(right)
            current.append((left, right))
            yield from rec(index + 1, used, current)
            current.pop()
            used.remove(left)
            used.remove(right)

    yield from rec(0, set(), [])


def diagram_from_matching(word: Word, matching: Sequence[Tuple[int, int]]) -> DiagramKey:
    length = len(word)
    if length == 0:
        return (0, 1, ())

    dsu = DisjointSet(length)
    matched_positions = set()
    for y_pos, x_pos in matching:
        matched_positions.add(y_pos)
        matched_positions.add(x_pos)
        # Y^k_l X^i_j -> -hbar delta^i_l delta^k_j.
        # Edge positions use source v_p and target v_{p+1}.
        dsu.union(x_pos, (y_pos + 1) % length)
        dsu.union(y_pos, (x_pos + 1) % length)

    root_to_vertex: Dict[int, int] = {}

    def vertex(pos: int) -> int:
        root = dsu.find(pos)
        if root not in root_to_vertex:
            root_to_vertex[root] = len(root_to_vertex)
        return root_to_vertex[root]

    for pos in range(length):
        vertex(pos)

    edges: List[Edge] = []
    for pos, letter in enumerate(word):
        if pos in matched_positions:
            continue
        edges.append((letter, vertex(pos), vertex((pos + 1) % length)))

    extra_n, graph = canonical_graph(edges, len(root_to_vertex))
    return (len(matching), extra_n, graph)


@lru_cache(maxsize=None)
def normal_form_trace_word(word: Word) -> DiagramPoly:
    if not word:
        return {(0, 1, ()): Fraction(1)}

    out: DiagramPoly = {}
    for matching in matchings(word):
        hbar_power, n_power, graph = diagram_from_matching(word, matching)
        coeff = Fraction(-1 if len(matching) % 2 else 1)
        add_poly(out, (hbar_power, n_power, graph), coeff)
    return out


@lru_cache(maxsize=None)
def normal_form_word_times_moment(word: Word) -> DiagramPoly:
    out = normal_form_trace_word(word + ("Y", "X"))
    out = merge_poly(out, normal_form_trace_word(word + ("X", "Y")), Fraction(-1))
    out = merge_poly(out, shift_poly(normal_form_trace_word(word), hbar_power=1, n_power=1))
    return out


def words_with_counts(x_count: int, y_count: int) -> Iterable[Word]:
    length = x_count + y_count
    for x_positions in combinations(range(length), x_count):
        x_set = set(x_positions)
        yield tuple("X" if pos in x_set else "Y" for pos in range(length))


@lru_cache(maxsize=None)
def weyl_trace_normal_form(x_power: int, y_power: int) -> DiagramPoly:
    length = x_power + y_power
    if length == 0:
        return {(0, 1, ()): Fraction(1)}

    out: DiagramPoly = {}
    for word in words_with_counts(x_power, y_power):
        out = merge_poly(out, normal_form_trace_word(word))
    return scale_poly(out, Fraction(1, comb(length, x_power)))


@lru_cache(maxsize=None)
def moyal_bracket_trace_normal_form(a: int, b: int) -> DiagramPoly:
    out: DiagramPoly = {}
    max_order = min(a + 1, b + 1)
    for order in range(1, max_order + 1, 2):
        coeff = Fraction(
            falling(a + 1, order) * falling(b + 1, order),
            (a + 1) * (2 ** (order - 1)) * factorial(order),
        )
        term = shift_poly(
            weyl_trace_normal_form(a + 1 - order, b + 1 - order),
            hbar_power=order - 1,
        )
        out = merge_poly(out, term, coeff)
    return out


@lru_cache(maxsize=None)
def shear_sum_normal_form(a: int, b: int) -> DiagramPoly:
    out: DiagramPoly = {}
    for j in range(b + 1):
        word = tuple("Y" for _ in range(j))
        word += tuple("X" for _ in range(a))
        word += tuple("Y" for _ in range(b - j))
        out = merge_poly(out, normal_form_trace_word(word))
    return out


@lru_cache(maxsize=None)
def shear_defect_normal_form(a: int, b: int) -> DiagramPoly:
    return merge_poly(shear_sum_normal_form(a, b), moyal_bracket_trace_normal_form(a, b), Fraction(-1))


def primitive_normal_form(coefficients: Dict[Word, Fraction]) -> DiagramPoly:
    out: DiagramPoly = {}
    for word, coeff in coefficients.items():
        out = merge_poly(out, normal_form_word_times_moment(word), coeff)
    return out


def candidate_coefficients(case: Tuple[int, int], classical_only: bool = False) -> Dict[Word, Fraction]:
    c44 = {
        parse_word("XXXYYY"): Fraction(31, 7),
        parse_word("XXYXYY"): Fraction(-4, 7),
        parse_word("XXYYXY"): Fraction(-4, 7),
        parse_word("XXYYYX"): Fraction(27, 7),
        parse_word("XYXXYY"): Fraction(23, 7),
        parse_word("XYXYXY"): Fraction(1, 7),
        parse_word("XYXYYX"): Fraction(1),
        parse_word("XYYXXY"): Fraction(-2, 7),
        parse_word("XYYXYX"): Fraction(15, 7),
    }
    if case == (4, 4) and classical_only:
        return c44

    k44 = {
        parse_word("XXYXYY"): Fraction(43, 14),
        parse_word("XYXXYY"): Fraction(-43, 14),
        parse_word("XYYXYX"): Fraction(-43, 14),
        parse_word("XYYYXX"): Fraction(43, 14),
    }

    a, b = case
    if a == 2 and b >= 2:
        return {
            tuple("Y" for _ in range(r)) + ("X",) + tuple("Y" for _ in range(b - 1 - r)): Fraction(
                b - 1 - 2 * r
            )
            for r in range((b - 2) // 2 + 1)
        }
    if b == 2 and a >= 2:
        return {
            tuple("X" for _ in range(a - 1 - r)) + ("Y",) + tuple("X" for _ in range(r)): Fraction(
                3 * (a - 1 - 2 * r), a + 1
            )
            for r in range((a - 2) // 2 + 1)
        }

    candidates: Dict[Tuple[int, int], Dict[Word, Fraction]] = {
        (2, 2): {parse_word("XY"): Fraction(1)},
        (2, 3): {parse_word("XYY"): Fraction(2)},
        (3, 2): {parse_word("XXY"): Fraction(3, 2)},
        (3, 3): {
            parse_word("XXYY"): Fraction(14, 5),
            parse_word("XYXY"): Fraction(2, 5),
            parse_word("XYYX"): Fraction(8, 5),
        },
        (2, 4): {
            parse_word("XYYY"): Fraction(3),
            parse_word("YXYY"): Fraction(1),
        },
        (4, 2): {
            parse_word("XXXY"): Fraction(9, 5),
            parse_word("XXYX"): Fraction(3, 5),
        },
        (3, 4): {
            parse_word("XXYYY"): Fraction(4),
            parse_word("XYXYY"): Fraction(2),
            parse_word("XYYXY"): Fraction(-1),
            parse_word("XYYYX"): Fraction(3),
        },
        (4, 3): {
            parse_word("XXXYY"): Fraction(16, 5),
            parse_word("XXYXY"): Fraction(-4, 5),
            parse_word("XXYYX"): Fraction(12, 5),
            parse_word("XYXXY"): Fraction(8, 5),
        },
        (3, 6): {
            parse_word("XXYYYYY"): Fraction(25, 4),
            parse_word("XYXYYYY"): Fraction(19, 4),
            parse_word("XYYXYYY"): Fraction(-3, 4),
            parse_word("XYYYXYY"): Fraction(-3, 4),
            parse_word("XYYYYXY"): Fraction(-3, 4),
            parse_word("XYYYYYX"): Fraction(11, 2),
            parse_word("YXYXYYY"): Fraction(13, 4),
            parse_word("YXYYXYY"): Fraction(1, 4),
            parse_word("YXYYYXY"): Fraction(7, 4),
        },
        (6, 3): {
            parse_word("XXXXXYY"): Fraction(25, 7),
            parse_word("XXXXYXY"): Fraction(-3, 7),
            parse_word("XXXXYYX"): Fraction(22, 7),
            parse_word("XXXYXXY"): Fraction(-3, 7),
            parse_word("XXXYXYX"): Fraction(-6, 7),
            parse_word("XXXYYXX"): Fraction(19, 7),
            parse_word("XXYXXXY"): Fraction(16, 7),
            parse_word("XXYXXYX"): Fraction(1, 7),
            parse_word("XXYXYXX"): Fraction(1),
        },
        (4, 4): merge_word_coefficients(c44, k44),
    }
    if case not in candidates:
        raise ValueError(f"no built-in candidate for case {case[0]},{case[1]}")
    return candidates[case]


def merge_word_coefficients(*vectors: Dict[Word, Fraction]) -> Dict[Word, Fraction]:
    out: Dict[Word, Fraction] = {}
    for vector in vectors:
        for word, coeff in vector.items():
            out[word] = out.get(word, Fraction(0)) + coeff
            if out[word] == 0:
                del out[word]
    return out


def finite_eval_diagram_poly(poly: DiagramPoly, rank: int) -> Poly:
    algebra = MatrixWeyl(rank)
    out: Poly = {}
    for (hbar_power, n_power, graph), coeff in poly.items():
        component_sizes = []
        flat_edges: List[Edge] = []
        offset = 0
        for component in graph:
            vertices = {src for _, src, _ in component} | {dst for _, _, dst in component}
            size = len(vertices)
            component_sizes.append(size)
            for letter, src, dst in component:
                flat_edges.append((letter, src + offset, dst + offset))
            offset += size

        term_poly: Poly = {}
        total_vertices = sum(component_sizes)
        assignments = product(range(rank), repeat=total_vertices)
        for assignment in assignments:
            xs = [0] * algebra.var_count
            ys = [0] * algebra.var_count
            for letter, src, dst in flat_edges:
                vid = algebra.vid(assignment[src], assignment[dst])
                if letter == "X":
                    xs[vid] += 1
                else:
                    ys[vid] += 1
            monomial = (hbar_power, tuple(xs), tuple(ys))
            term_poly[monomial] = term_poly.get(monomial, Fraction(0)) + coeff * (rank ** n_power)
        out = algebra.add(out, term_poly)
    return out


def self_test(rank: int, max_length: int) -> Tuple[int, List[str]]:
    failures: List[str] = []
    checked = 0
    algebra = MatrixWeyl(rank)
    for length in range(max_length + 1):
        for word in product(("X", "Y"), repeat=length):
            checked += 1
            free_nf = normal_form_trace_word(word)
            finite_nf = finite_eval_diagram_poly(free_nf, rank)
            actual = algebra.trace_word(word)
            if not poly_equal(finite_nf, actual):
                failures.append(word_label(word))
                if len(failures) >= 8:
                    return checked, failures
    return checked, failures


def graph_summary(graph: GraphKey) -> str:
    if not graph:
        return "1"
    pieces = []
    for component in graph:
        edges = ",".join(f"{letter}{src}>{dst}" for letter, src, dst in component)
        pieces.append(f"({edges})")
    return " ".join(pieces)


def format_term(key: DiagramKey, coeff: Fraction) -> str:
    hbar_power, n_power, graph = key
    factors: List[str] = []
    if hbar_power:
        factors.append("hbar" if hbar_power == 1 else f"hbar^{hbar_power}")
    if n_power:
        factors.append("N" if n_power == 1 else f"N^{n_power}")
    factors.append(f"D[{graph_summary(graph)}]")
    return f"{frac_str(coeff):>8} * " + " ".join(factors)


def print_poly(poly: DiagramPoly, max_terms: int) -> None:
    print(f"terms={len(poly)}")
    if len(poly) > max_terms:
        print(f"  omitted {len(poly)} terms; rerun with --max-terms at least {len(poly)}")
        return
    for key, coeff in sorted(poly.items(), key=lambda item: (item[0], item[1])):
        print("  " + format_term(key, coeff))


def print_word_support(support: Sequence[Tuple[Word, Fraction]], max_terms: int) -> None:
    if not support:
        return
    if len(support) > max_terms:
        print(f"  support omitted: {len(support)} terms exceeds --max-terms={max_terms}")
        return
    for word, coeff in support:
        print(f"  {frac_str(coeff):>8} * Tr({word_label(word)} M)")


@dataclass(frozen=True)
class CaseResult:
    a: int
    b: int
    classical_only: bool
    residual_terms: int
    residual: DiagramPoly
    candidate_terms: int
    target_terms: int


@dataclass(frozen=True)
class FreeSolveResult:
    a: int
    b: int
    consistent: bool
    verified: bool
    residual_terms: int
    support: List[Tuple[Word, Fraction]]
    target_terms: int
    rank: int
    rows: int
    columns: int


@dataclass(frozen=True)
class ClassicalSolveResult:
    a: int
    b: int
    consistent: bool
    support: List[Tuple[Word, Fraction]]
    rank: int
    rows: int
    columns: int


@dataclass(frozen=True)
class KernelCorrectionResult:
    a: int
    b: int
    classical_consistent: bool
    correction_consistent: bool
    corrected: bool
    classical_terms: int
    residual_terms: int
    correction_terms: int
    corrected_residual_terms: int
    support: List[Tuple[Word, Fraction]]
    rank: int
    rows: int
    columns: int


def run_case(a: int, b: int, classical_only: bool) -> CaseResult:
    target = shear_defect_normal_form(a, b)
    coeffs = candidate_coefficients((a, b), classical_only=classical_only)
    primitive = primitive_normal_form(coeffs)
    residual = merge_poly(target, primitive, Fraction(-1))
    return CaseResult(
        a=a,
        b=b,
        classical_only=classical_only,
        residual_terms=len(residual),
        residual=residual,
        candidate_terms=len(coeffs),
        target_terms=len(target),
    )


def reconstruct_primitive(words: Sequence[Word], coeffs: Dict[int, Fraction]) -> DiagramPoly:
    out: DiagramPoly = {}
    for index, coeff in coeffs.items():
        out = merge_poly(out, normal_form_word_times_moment(words[index]), coeff)
    return out


def solve_free_case(a: int, b: int) -> FreeSolveResult:
    words = list(words_with_counts(a - 1, b - 1)) if a >= 1 and b >= 1 else []
    columns = [normal_form_word_times_moment(word) for word in words]
    target = shear_defect_normal_form(a, b)
    solution = solve_sparse(columns, target)
    primitive = reconstruct_primitive(words, solution.coefficients) if solution.consistent else {}
    residual = merge_poly(target, primitive, Fraction(-1))
    support = [
        (words[index], coeff)
        for index, coeff in sorted(solution.coefficients.items())
        if coeff
    ]
    return FreeSolveResult(
        a=a,
        b=b,
        consistent=solution.consistent,
        verified=solution.consistent and not residual,
        residual_terms=len(residual),
        support=support,
        target_terms=len(target),
        rank=solution.rank,
        rows=solution.row_count,
        columns=solution.column_count,
    )


def solve_classical_case(a: int, b: int, words: Sequence[Word]):
    columns = [tag_poly("cyclic", free_classical_column(word)) for word in words]
    target = tag_poly("cyclic", free_classical_target(a, b))
    return solve_sparse(columns, target)


def solve_classical_only_case(a: int, b: int) -> ClassicalSolveResult:
    words = list(words_with_counts(a - 1, b - 1)) if a >= 1 and b >= 1 else []
    solution = solve_classical_case(a, b, words)
    support = [
        (words[index], coeff)
        for index, coeff in sorted(solution.coefficients.items())
        if coeff
    ]
    return ClassicalSolveResult(
        a=a,
        b=b,
        consistent=solution.consistent,
        support=support,
        rank=solution.rank,
        rows=solution.row_count,
        columns=solution.column_count,
    )


def solve_kernel_correction_case(a: int, b: int) -> KernelCorrectionResult:
    words = list(words_with_counts(a - 1, b - 1)) if a >= 1 and b >= 1 else []
    classical = solve_classical_case(a, b, words)
    if not classical.consistent:
        return KernelCorrectionResult(
            a=a,
            b=b,
            classical_consistent=False,
            correction_consistent=False,
            corrected=False,
            classical_terms=0,
            residual_terms=0,
            correction_terms=0,
            corrected_residual_terms=0,
            support=[],
            rank=0,
            rows=0,
            columns=len(words),
        )

    target = shear_defect_normal_form(a, b)
    classical_primitive = reconstruct_primitive(words, classical.coefficients)
    residual = merge_poly(target, classical_primitive, Fraction(-1))

    columns: List[TaggedPoly] = []
    for word in words:
        column: TaggedPoly = {}
        column = merge_tagged(column, tag_poly("cyclic", free_classical_column(word)))
        column = merge_tagged(column, tag_poly("diagram", normal_form_word_times_moment(word)))
        columns.append(column)

    tagged_target = tag_poly("diagram", residual)
    correction = solve_sparse(columns, tagged_target)
    correction_primitive = (
        reconstruct_primitive(words, correction.coefficients) if correction.consistent else {}
    )
    corrected_residual = merge_poly(residual, correction_primitive, Fraction(-1))
    support = [
        (words[index], coeff)
        for index, coeff in sorted(correction.coefficients.items())
        if coeff
    ]
    return KernelCorrectionResult(
        a=a,
        b=b,
        classical_consistent=True,
        correction_consistent=correction.consistent,
        corrected=correction.consistent and not corrected_residual,
        classical_terms=len(classical.coefficients),
        residual_terms=len(residual),
        correction_terms=len(support),
        corrected_residual_terms=len(corrected_residual),
        support=support,
        rank=correction.rank,
        rows=correction.row_count,
        columns=correction.column_count,
    )


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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        type=parse_case,
        help="case a,b to check against the built-in candidate table",
    )
    parser.add_argument(
        "--classical-only",
        action="store_true",
        help="for 4,4 use the cyclic pivot solution before adding K_44",
    )
    parser.add_argument(
        "--solve-free",
        action="store_true",
        help="solve directly for a primitive in the free indexed diagram basis",
    )
    parser.add_argument(
        "--solve-classical",
        action="store_true",
        help="solve only the cyclic hbar=0 boundary equation and print its lift",
    )
    parser.add_argument(
        "--kernel-correction",
        action="store_true",
        help="solve the cyclic equation first, then solve for a correction in ker(partial)",
    )
    parser.add_argument(
        "--edge-family-max",
        type=int,
        help="also check the edge families (2,b) and (a,2) for 2 <= a,b <= this value",
    )
    parser.add_argument(
        "--balanced-family-max",
        type=int,
        help="also check diagonal balanced cases (d,d) for 2 <= d <= this value",
    )
    parser.add_argument(
        "--family-only",
        action="store_true",
        help="start from no default cases; useful with --edge-family-max or --balanced-family-max",
    )
    parser.add_argument(
        "--progress",
        action="store_true",
        help="print a flushed BEGIN line before each case in long exact scans",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="compare the free normal-ordering formula with finite matrix Weyl normal ordering",
    )
    parser.add_argument("--self-test-rank", type=int, default=2)
    parser.add_argument("--self-test-max-length", type=int, default=5)
    parser.add_argument("--max-terms", type=int, default=24)
    args = parser.parse_args()
    solve_modes = sum(bool(flag) for flag in (args.solve_free, args.solve_classical, args.kernel_correction))
    if args.classical_only and solve_modes:
        parser.error("--classical-only is only supported by the built-in candidate checker")
    if solve_modes > 1:
        parser.error("--solve-free, --solve-classical, and --kernel-correction are separate modes")

    print("Quantum shear trace-diagram normal form")
    print("basis: free indexed normal diagrams before finite-rank trace identities")
    print("normal order: all X-edges before all Y-edges; contractions keep split diagrams")
    print()

    failed = 0
    if args.self_test:
        checked, failures = self_test(args.self_test_rank, args.self_test_max_length)
        if failures:
            failed += 1
            print(
                f"FAIL self-test rank={args.self_test_rank} "
                f"max_length={args.self_test_max_length} checked={checked}"
            )
            for failure in failures:
                print(f"  mismatch Tr({failure})")
        else:
            print(
                f"PASS self-test rank={args.self_test_rank} "
                f"max_length={args.self_test_max_length} checked={checked}"
            )
        print()

    default_cases = [
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
        (2, 6),
        (6, 2),
        (4, 4),
    ]
    cases = list(args.case or ([] if args.family_only else default_cases))
    if args.family_only and args.case:
        parser.error("--family-only is only meaningful when cases come from family options")
    if args.family_only and args.edge_family_max is None and args.balanced_family_max is None:
        parser.error("--family-only requires --edge-family-max or --balanced-family-max")
    if args.edge_family_max is not None:
        if args.edge_family_max < 2:
            parser.error("--edge-family-max must be at least 2")
        seen = set(cases)
        for value in range(2, args.edge_family_max + 1):
            for case in ((2, value), (value, 2)):
                if case not in seen:
                    cases.append(case)
                    seen.add(case)
    if args.balanced_family_max is not None:
        if args.balanced_family_max < 2:
            parser.error("--balanced-family-max must be at least 2")
        seen = set(cases)
        for value in range(2, args.balanced_family_max + 1):
            case = (value, value)
            if case not in seen:
                cases.append(case)
                seen.add(case)

    for a, b in cases:
        if args.progress:
            print(f"BEGIN a={a} b={b}", flush=True)

        if args.solve_classical:
            classical = solve_classical_only_case(a, b)
            status = "PASS" if classical.consistent else "FAIL"
            print(
                f"{status} a={a} b={b} mode=classical-solve "
                f"support={len(classical.support)} rank={classical.rank} "
                f"rows={classical.rows} cols={classical.columns}"
            )
            print_word_support(classical.support, args.max_terms)
            if not classical.consistent:
                failed += 1
            continue

        if args.solve_free:
            free_result = solve_free_case(a, b)
            status = "PASS" if free_result.verified else "FAIL"
            print(
                f"{status} a={a} b={b} mode=free-solve "
                f"target_terms={free_result.target_terms} support={len(free_result.support)} "
                f"rank={free_result.rank} rows={free_result.rows} cols={free_result.columns} "
                f"residual_terms={free_result.residual_terms}"
            )
            print_word_support(free_result.support, args.max_terms)
            if not free_result.verified:
                failed += 1
            continue

        if args.kernel_correction:
            correction = solve_kernel_correction_case(a, b)
            status = "PASS" if correction.corrected else "FAIL"
            print(
                f"{status} a={a} b={b} mode=kernel-correction "
                f"classical={'ok' if correction.classical_consistent else 'fail'} "
                f"classical_terms={correction.classical_terms} "
                f"residual_terms={correction.residual_terms} "
                f"correction={'ok' if correction.correction_consistent else 'fail'} "
                f"correction_terms={correction.correction_terms} "
                f"rank={correction.rank} rows={correction.rows} cols={correction.columns} "
                f"corrected_residual_terms={correction.corrected_residual_terms}"
            )
            print_word_support(correction.support, args.max_terms)
            if not correction.corrected:
                failed += 1
            continue

        result = run_case(a, b, classical_only=args.classical_only)
        status = "PASS" if result.residual_terms == 0 else "FAIL"
        mode = "classical-only" if result.classical_only else "candidate"
        print(
            f"{status} a={a} b={b} mode={mode} "
            f"target_terms={result.target_terms} candidate_terms={result.candidate_terms} "
            f"residual_terms={result.residual_terms}"
        )
        if result.residual_terms:
            print_poly(result.residual, args.max_terms)
            failed += 1

    print()
    if failed:
        print(f"FAIL: {failed} check(s) have nonzero free trace-diagram residuals.")
        return 1
    if args.solve_classical:
        print("PASS: all requested cyclic boundary equations have rational lifts.")
    elif args.solve_free:
        print("PASS: all requested free solves have zero free trace-diagram residual.")
    elif args.kernel_correction:
        print("PASS: all requested kernel-correction obstruction classes vanish.")
    else:
        print("PASS: all requested candidates have zero free trace-diagram residual.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
