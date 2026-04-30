#!/usr/bin/env python3
"""Symbolic checks for finite-window graph-array rows.

The script does not enumerate a Costello graph package.  It verifies the
universal entries inscribed in
``prop:first-finite-window-array-rows``: the strict reduced current row and
the one-cross two-Hamiltonian scalar-contact row.  It also records the
formal order-two closure rows forced by two first scalar-contact boundary
faces, the zero bracket rows containing the scalar-contact component, and
the formal schema for genuine order-two seed graph weights.  For larger
packages it records the coordinate definitions of the missing ``u``, ``v``,
and ``q`` truncation matrices, emits one concrete symbolic order-three
larger-package row, runs finite-row primitive-search linear algebra, and
records the eight-face ``theta_3`` companion obstruction.  The script does
not guess any Costello graph integral or counterterm outside the supplied
finite row complex.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from typing import Literal


Branch = Literal["ordinary_glN", "even_block", "full_equivariant"]
Theta3PrimitiveKind = Literal["ce_ancestor", "counterterm_primitive"]

THETA3_ROW = "E_theta_3"
THETA3_RESIDUAL = ((THETA3_ROW, 1),)


@dataclass(frozen=True)
class FirstOrderRow:
    branch: Branch
    graph_type: str
    edge_label: str
    vertex_labels: tuple[str, ...]
    marker_tensor: str
    incidence_sign: int
    hbar_order: int
    coefficient_window_degree: int
    scalar_contact_filtration: int
    scalar_gate: str
    non_scalar_residual_from_row: str
    counterterm: str


@dataclass(frozen=True)
class ScalarZeroRow:
    branch: Branch
    row_label: str
    graph_type: str
    edge_label: str
    vertex_labels: tuple[str, ...]
    incidence_sign: int
    hbar_order: int
    coefficient_window_degree: int
    omega: int
    row_value: str
    scalar_gate: str
    truncation_matrix: str
    counterterm: str


@dataclass(frozen=True)
class BoundaryContact:
    name: str
    ordered_inputs: tuple[tuple[int, int], tuple[int, int]]
    boundary_position: int
    epsilon: str
    omega: int


@dataclass(frozen=True)
class SecondOrderCompositeRow:
    branch: Branch
    composition: str
    incidence_sign: int
    coefficient: str
    scalar_gate: str
    cyclic_marker_traces: str
    row_value_in_minimal_full_equivariant_array: str


@dataclass(frozen=True)
class UniversalBracketRow:
    branch: Branch
    bracket_row: str
    incidence_coefficient: str
    row_formula: str
    scalar_gate: str
    truncation_coefficients: str
    counterterm: str
    status: str


@dataclass(frozen=True)
class GenuineOrderTwoRow:
    branch: Branch
    row_kind: str
    row_formula: str
    incidence_coefficient: str
    scalar_gate: str
    non_scalar_contribution: str
    truncation_rule: str
    status: str


@dataclass(frozen=True)
class TruncationMatrixFamily:
    family: str
    rows: tuple[str, ...]
    retained_window_condition: str
    matrix_entries: str
    stability: str
    deciding_evidence: str
    missing_entries: str
    status: str


@dataclass(frozen=True)
class ProjectionMatrixRule:
    family: str
    normalized_row: str
    projection_formula: str
    matrix_entry: str
    compatibility: str
    required_data: tuple[str, ...]
    obstruction_use: str
    status: str


@dataclass(frozen=True)
class ConcreteOrderThreeCESourceRow:
    branch: Branch
    row_label: str
    graph_type: str
    hbar_order: int
    coefficient_window_degree: int
    source_face_label: str
    edge_labels: tuple[str, ...]
    vertex_labels: tuple[str, ...]
    marker_tensor: str
    ce_source_sign: int
    incidence_sign_in_row_value: int
    row_value: str
    row_closure: str
    scalar_gate: str
    truncation_matrix: str
    class_in_K_ns: str
    counterterm_criterion: str
    decision: str


@dataclass(frozen=True)
class PrimitiveSearchResult:
    case: str
    scalar_gate: str
    degree_zero_basis: tuple[str, ...]
    degree_one_basis: tuple[str, ...]
    differential_matrix_rows: tuple[tuple[str, ...], ...]
    residual_vector: tuple[tuple[str, str], ...]
    target_vector: tuple[tuple[str, str], ...]
    primitive_exists: bool
    primitive_coefficients: tuple[tuple[str, str], ...]
    obstruction_covector: tuple[tuple[str, str], ...]
    obstruction_value_on_residual: str
    fixed_window_decision: str
    roos_compatibility: str
    status: str


@dataclass(frozen=True)
class Theta3CommonFiniteWindowRecord:
    row_label: str
    graph_label: str
    hbar_order: int
    finite_window_degree: int
    source_face: str
    source_face_coefficient: int
    row_value: str
    row_closure: str
    scalar_projection: int
    truncation_n_ge_3: str
    truncation_n_lt_3: str
    inherited_labels: tuple[str, ...]
    marker_tensor: str
    current_status: str


@dataclass(frozen=True)
class Theta3PrimitiveTransport:
    row_transport_n_ge_3: int | str
    primitive_transport_n_ge_3: int | str
    row_transport_n_lt_3: int | str
    primitive_transport_n_lt_3: int | str
    roos_class: int | str


@dataclass(frozen=True)
class Theta3PrimitivePayload:
    case: str
    payload_kind: Theta3PrimitiveKind
    supplied: bool
    primitive_label: str
    source_boundary_entries: tuple[tuple[str, str, int | str], ...]
    bianchi_or_locality_verified: bool
    differential_entries: tuple[tuple[str, str, int | str], ...]
    scalar_projection: int | str | None
    transport: Theta3PrimitiveTransport | None
    provenance: str


@dataclass(frozen=True)
class Theta3PrimitivePayloadCheck:
    case: str
    payload_kind: Theta3PrimitiveKind
    supplied: bool
    accepted: bool
    support_data_verified: bool
    differential_entry_present: bool
    differential_entry_value: str
    dC_equals_minus_E: bool
    scalar_zero_verified: bool
    transport_identity_verified: bool
    roos_compatibility_verified: bool
    missing_fields: tuple[str, ...]
    primitive_search: PrimitiveSearchResult
    status: str


@dataclass(frozen=True)
class Theta3CompanionFace:
    face_label: str
    ce_coefficient: int | str
    residual_coordinates: tuple[tuple[str, int | str], ...]
    scalar_projection: int | str | None
    source_face: str = ""
    hamiltonian_degree: int | None = None
    row_contribution: str = ""


@dataclass(frozen=True)
class Theta3CompanionFacePayload:
    case: str
    supplied: bool
    faces: tuple[Theta3CompanionFace, ...]
    residual_sum_declared: int | str | None
    v_truncation_matrices_supplied: bool
    v_cocycle_identity_verified: bool
    codimension_two_closure_supplied: bool
    provenance: str
    signed_coordinates_verified_from_ce_coefficients: bool = False
    marked_costello_incidence_weight_table_supplied: bool = False
    lower_window_residual_zero_verified: bool = False
    exact_obstruction: str = ""


@dataclass(frozen=True)
class Theta3CompanionFacePayloadCheck:
    case: str
    supplied: bool
    accepted: bool
    face_count: int
    residual_vector: tuple[tuple[str, str], ...]
    residual_zero_verified: bool
    signed_coordinates_verified_from_ce_coefficients: bool
    scalar_zero_verified: bool
    v_truncation_verified: bool
    codimension_two_closure_verified: bool
    marked_costello_table_verified: bool
    lower_window_residual_zero_verified: bool
    roos_compatibility: str
    missing_fields: tuple[str, ...]
    exact_obstruction: str
    status: str


@dataclass(frozen=True)
class Theta3DiagonalVTransportObstruction:
    transport_formula: str
    degree_two_faces: tuple[str, ...]
    degree_three_faces: tuple[str, ...]
    n_ge_3_residual_vector: tuple[tuple[str, str], ...]
    n_2_residual_vector: tuple[tuple[str, str], ...]
    cocycle_identity_verified: bool
    lower_window_residual_zero_verified: bool
    missing_lower_window_identity: str
    status: str


@dataclass(frozen=True)
class Theta3MarkedCostelloTableObstruction:
    required_entries: tuple[str, ...]
    supplied_entries: tuple[str, ...]
    missing_entries: tuple[str, ...]
    codimension_two_closure_supplied: bool
    deciding_evidence: str
    status: str


@dataclass(frozen=True)
class Theta3EightFaceCandidateObstructionCheck:
    case: str
    accepted: bool
    face_count: int
    faces: tuple[Theta3CompanionFace, ...]
    candidate_residual_formula: str
    candidate_residual_vector: tuple[tuple[str, str], ...]
    candidate_residual_coefficient_sum: str
    source_ce_coefficients_verified: bool
    scalar_zero_verified: bool
    diagonal_v_transport: Theta3DiagonalVTransportObstruction
    marked_costello_table: Theta3MarkedCostelloTableObstruction
    missing_fields: tuple[str, ...]
    exact_obstruction: str
    status: str


def as_fraction(value: int | str | Fraction) -> Fraction:
    if isinstance(value, Fraction):
        return value
    return Fraction(value)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    mat = [row[:] for row in matrix]
    if not mat:
        return mat, []

    row_count = len(mat)
    col_count = len(mat[0])
    pivot_row = 0
    pivots: list[int] = []

    for col in range(col_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if mat[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue

        mat[pivot_row], mat[pivot] = mat[pivot], mat[pivot_row]
        pivot_value = mat[pivot_row][col]
        mat[pivot_row] = [entry / pivot_value for entry in mat[pivot_row]]

        for row in range(row_count):
            if row == pivot_row or mat[row][col] == 0:
                continue
            factor = mat[row][col]
            mat[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(mat[row], mat[pivot_row])
            ]

        pivots.append(col)
        pivot_row += 1
        if pivot_row == row_count:
            break

    return mat, pivots


def solve_linear_system(
    matrix: list[list[Fraction]], target: list[Fraction]
) -> list[Fraction] | None:
    row_count = len(target)
    col_count = len(matrix[0]) if matrix else 0
    augmented = [
        (matrix[row][:] if col_count else []) + [target[row]]
        for row in range(row_count)
    ]
    reduced, pivots = rref(augmented)

    for row in reduced:
        if all(entry == 0 for entry in row[:col_count]) and row[-1] != 0:
            return None

    solution = [Fraction(0) for _ in range(col_count)]
    for reduced_row, pivot_col in zip(reduced, pivots):
        if pivot_col < col_count:
            solution[pivot_col] = reduced_row[-1]
    return solution


def nullspace(
    matrix: list[list[Fraction]], col_count: int | None = None
) -> list[list[Fraction]]:
    if col_count is None:
        col_count = len(matrix[0]) if matrix else 0
    reduced, pivots = rref(matrix)
    pivot_set = set(pivots)
    free_cols = [col for col in range(col_count) if col not in pivot_set]
    basis: list[list[Fraction]] = []

    for free_col in free_cols:
        vector = [Fraction(0) for _ in range(col_count)]
        vector[free_col] = Fraction(1)
        for row_index, pivot_col in enumerate(pivots):
            if pivot_col < col_count:
                vector[pivot_col] = -reduced[row_index][free_col]
        basis.append(vector)
    return basis


def left_nullspace(
    matrix: list[list[Fraction]], row_count: int, col_count: int
) -> list[list[Fraction]]:
    transpose = [
        [matrix[row][col] for row in range(row_count)]
        for col in range(col_count)
    ]
    return nullspace(transpose, col_count=row_count)


def labelled_vector(
    basis: tuple[str, ...], vector: list[Fraction]
) -> tuple[tuple[str, str], ...]:
    return tuple(
        (basis[index], fraction_text(value))
        for index, value in enumerate(vector)
        if value != 0
    )


def coefficient_sum(
    entries: tuple[tuple[str, str, int | str], ...],
    primitive_label: str,
    row_label: str,
) -> Fraction:
    value = Fraction(0)
    for primitive, row, coefficient in entries:
        if primitive == primitive_label and row == row_label:
            value += as_fraction(coefficient)
    return value


def scalar_zero_value(value: int | str | None) -> bool:
    if value is None:
        return False
    return as_fraction(value) == 0


def vector_from_coordinate_entries(
    entries: tuple[tuple[str, int | str], ...],
) -> tuple[tuple[str, str], ...]:
    labels = tuple(dict.fromkeys(label for label, _ in entries))
    vector = [Fraction(0) for _ in labels]
    label_index = {label: index for index, label in enumerate(labels)}
    for label, coefficient in entries:
        vector[label_index[label]] += as_fraction(coefficient)
    return labelled_vector(labels, vector)


def coefficient_total(
    entries: tuple[tuple[str, int | str], ...],
) -> Fraction:
    return sum(
        (as_fraction(coefficient) for _, coefficient in entries),
        start=Fraction(0),
    )


def primitive_search(
    *,
    case: str,
    scalar_gate: str,
    degree_zero_basis: tuple[str, ...],
    degree_one_basis: tuple[str, ...],
    differential_entries: tuple[tuple[str, str, int | str], ...],
    residual_entries: tuple[tuple[str, int | str], ...],
    roos_compatibility: str,
    status: str,
) -> PrimitiveSearchResult:
    row_index = {label: index for index, label in enumerate(degree_one_basis)}
    col_index = {label: index for index, label in enumerate(degree_zero_basis)}
    matrix = [
        [Fraction(0) for _ in degree_zero_basis]
        for _ in degree_one_basis
    ]
    for primitive, row, coefficient in differential_entries:
        matrix[row_index[row]][col_index[primitive]] += as_fraction(coefficient)

    residual = [Fraction(0) for _ in degree_one_basis]
    for row, coefficient in residual_entries:
        residual[row_index[row]] += as_fraction(coefficient)
    target = [-entry for entry in residual]

    solution = solve_linear_system(matrix, target)
    obstruction_covector: list[Fraction] = []
    obstruction_value = Fraction(0)
    if solution is None:
        for covector in left_nullspace(
            matrix, len(degree_one_basis), len(degree_zero_basis)
        ):
            value = sum(a * b for a, b in zip(covector, residual))
            if value != 0:
                obstruction_covector = covector
                obstruction_value = value
                break
    else:
        obstruction_covector = [Fraction(0) for _ in degree_one_basis]

    if solution is None:
        fixed_window_decision = (
            "no supplied degree-zero row maps to the negative residual; "
            "the displayed cokernel covector certifies a nonzero H^1 class"
        )
        primitive_coefficients: tuple[tuple[str, str], ...] = ()
    else:
        fixed_window_decision = (
            "primitive found in the supplied finite row complex; the "
            "fixed-window H^1 class vanishes"
        )
        primitive_coefficients = labelled_vector(degree_zero_basis, solution)

    return PrimitiveSearchResult(
        case=case,
        scalar_gate=scalar_gate,
        degree_zero_basis=degree_zero_basis,
        degree_one_basis=degree_one_basis,
        differential_matrix_rows=tuple(
            tuple(fraction_text(entry) for entry in row)
            for row in matrix
        ),
        residual_vector=labelled_vector(degree_one_basis, residual),
        target_vector=labelled_vector(degree_one_basis, target),
        primitive_exists=solution is not None,
        primitive_coefficients=primitive_coefficients,
        obstruction_covector=labelled_vector(degree_one_basis, obstruction_covector),
        obstruction_value_on_residual=fraction_text(obstruction_value),
        fixed_window_decision=fixed_window_decision,
        roos_compatibility=roos_compatibility,
        status=status,
    )


def omega_monomial(k: int, l: int, m: int, n: int) -> int:
    """Constant term of {z1^k z2^l, z1^m z2^n}."""

    if (k + m, l + n) != (1, 1):
        return 0
    return k * n - l * m


def scalar_gate(branch: Branch, omega: int) -> str:
    if branch == "ordinary_glN":
        return f"{omega}*N*gamma_1"
    if branch == "even_block":
        return f"{omega}*N*(lambda_0-lambda_1)*gamma_1"
    if branch == "full_equivariant":
        return "0"
    raise ValueError(f"unknown branch: {branch}")


def branch_trace(branch: Branch) -> str:
    if branch == "ordinary_glN":
        return "N"
    if branch == "even_block":
        return "N*(lambda_0-lambda_1)"
    if branch == "full_equivariant":
        return "0"
    raise ValueError(f"unknown branch: {branch}")


def first_order_row(branch: Branch) -> FirstOrderRow:
    omega = omega_monomial(1, 0, 0, 1)
    gate = scalar_gate(branch, omega)
    formed = gate == "0"
    return FirstOrderRow(
        branch=branch,
        graph_type="dK/scalar-contact",
        edge_label="E_Weyl",
        vertex_labels=("u_{a dt tensor z1}", "u_{b dt tensor z2}", "gamma_1"),
        marker_tensor={
            "ordinary_glN": "identity open loop",
            "even_block": "lambda_0 P_even + lambda_1 P_odd",
            "full_equivariant": "Brauer/full gl(N|N)-invariant marker",
        }[branch],
        incidence_sign=1,
        hbar_order=1,
        coefficient_window_degree=1,
        scalar_contact_filtration=1,
        scalar_gate=gate,
        non_scalar_residual_from_row="0" if formed else "not formed: scalar gate nonzero",
        counterterm="C_{1,M}=0" if formed else "none inside non-scalar kernel",
    )


def scalar_zero_alpha_11_row() -> ScalarZeroRow:
    omega = omega_monomial(1, 0, 1, 0)
    return ScalarZeroRow(
        branch="full_equivariant",
        row_label="alpha_11",
        graph_type="dK/scalar-contact",
        edge_label="E_Weyl",
        vertex_labels=("u_{a dt tensor z1}", "u_{b dt tensor z1}", "gamma_1"),
        incidence_sign=1,
        hbar_order=1,
        coefficient_window_degree=1,
        omega=omega,
        row_value="Str_cyc(mu_beta11(m))*omega(z1,z1)*int_I a(t)b(t)gamma_1(t)dt = 0",
        scalar_gate="Str_cyc(mu_beta11(m))*omega(z1,z1)*gamma_1 = 0",
        truncation_matrix=(
            "if retained and M>=N>=1: t^{M,N}_{alpha_11,alpha_11}=1 "
            "and t^{M,N}_{alpha_11,alpha'}=0 for alpha'!=alpha_11; "
            "if zero rows are suppressed, the matrix is empty"
        ),
        counterterm="C_{1,M}=0",
    )


def boundary_contact(
    name: str,
    first: tuple[int, int],
    second: tuple[int, int],
    boundary_position: int,
) -> BoundaryContact:
    return BoundaryContact(
        name=name,
        ordered_inputs=(first, second),
        boundary_position=boundary_position,
        epsilon=f"epsilon_{name}",
        omega=omega_monomial(*first, *second),
    )


def composite_incidence(first_position: int, second_position_after_first: int) -> int:
    return (-1) ** (first_position - 1) * (-1) ** (second_position_after_first - 1)


def second_order_composite_rows(branch: Branch) -> list[SecondOrderCompositeRow]:
    beta_1 = boundary_contact("beta_1", (1, 0), (0, 1), 1)
    beta_2 = boundary_contact("beta_2", (1, 0), (0, 1), 2)
    trace_1 = branch_trace(branch)
    trace_2 = branch_trace(branch)
    gate_core = f"({trace_1})*({trace_2})*{beta_1.omega}*{beta_2.omega}*gamma_1^(2)"
    full_trace = "0,0" if branch == "full_equivariant" else f"{trace_1},{trace_2}"
    rows = [
        SecondOrderCompositeRow(
            branch=branch,
            composition="beta_1 then beta_2|beta_1",
            incidence_sign=composite_incidence(1, 1),
            coefficient="epsilon_beta_1*epsilon_beta_2|beta_1",
            scalar_gate=f"+{gate_core}",
            cyclic_marker_traces=full_trace,
            row_value_in_minimal_full_equivariant_array=(
                "0" if branch == "full_equivariant" else "scalar contact: not in non-scalar kernel"
            ),
        ),
        SecondOrderCompositeRow(
            branch=branch,
            composition="beta_2 then beta_1|beta_2",
            incidence_sign=composite_incidence(2, 1),
            coefficient="epsilon_beta_2*epsilon_beta_1|beta_2",
            scalar_gate=f"-{gate_core}",
            cyclic_marker_traces=full_trace,
            row_value_in_minimal_full_equivariant_array=(
                "0" if branch == "full_equivariant" else "scalar contact: not in non-scalar kernel"
            ),
        ),
    ]
    return rows


def universal_scalar_contact_bracket_rows() -> list[UniversalBracketRow]:
    zero_reason = "K^M_{alpha_sc}=0 in the full-equivariant branch"
    return [
        UniversalBracketRow(
            branch="full_equivariant",
            bracket_row="b(alpha_sc,beta), |beta|_hbar=1",
            incidence_coefficient="1/2*epsilon_{alpha_sc,beta}",
            row_formula=(
                "R_b=1/2*epsilon_{alpha_sc,beta}"
                "*{K^M_{alpha_sc},K^M_beta}_{hbar,M}=0"
            ),
            scalar_gate="0",
            truncation_coefficients="t^{M,N}_{b,b'}=0 for every lower-window bracket row b'",
            counterterm="none",
            status=f"vanishes as a local functional before cohomology; {zero_reason}",
        ),
        UniversalBracketRow(
            branch="full_equivariant",
            bracket_row="b(beta,alpha_sc), |beta|_hbar=1",
            incidence_coefficient="1/2*epsilon_{beta,alpha_sc}",
            row_formula=(
                "R_b=1/2*epsilon_{beta,alpha_sc}"
                "*{K^M_beta,K^M_{alpha_sc}}_{hbar,M}=0"
            ),
            scalar_gate="0",
            truncation_coefficients="t^{M,N}_{b,b'}=0 for every lower-window bracket row b'",
            counterterm="none",
            status=f"vanishes as a local functional before cohomology; {zero_reason}",
        ),
        UniversalBracketRow(
            branch="full_equivariant",
            bracket_row="b(alpha_sc,alpha_sc)",
            incidence_coefficient="1/2*epsilon_{alpha_sc,alpha_sc}",
            row_formula=(
                "R_b=1/2*epsilon_{alpha_sc,alpha_sc}"
                "*{K^M_{alpha_sc},K^M_{alpha_sc}}_{hbar,M}=0"
            ),
            scalar_gate="0",
            truncation_coefficients="t^{M,N}_{b,b'}=0 for every lower-window bracket row b'",
            counterterm="none",
            status=f"vanishes as a local functional before cohomology; {zero_reason}",
        ),
    ]


def genuine_order_two_graph_weight_rows() -> list[GenuineOrderTwoRow]:
    return [
        GenuineOrderTwoRow(
            branch="full_equivariant",
            row_kind="dK genuine |Gamma|_hbar=2 seed",
            row_formula="R_{dGamma,M}=epsilon_Gamma*d_M K^M_Gamma",
            incidence_coefficient=(
                "epsilon_Gamma is supplied by the finite graph package "
                "and includes orientation/Koszul/symmetry data"
            ),
            scalar_gate="0 if K^M_Gamma and d_M K^M_Gamma lie in the full-equivariant marked habitat",
            non_scalar_contribution="epsilon_Gamma*d_M K^M_Gamma",
            truncation_rule=(
                "pi_{M,N}(epsilon_Gamma K^M_Gamma)="
                "sum_{Gamma'} u^{M,N}_{Gamma,Gamma'} epsilon_Gamma' K^N_Gamma'; "
                "then t^{M,N}_{dGamma,dGamma'}=u^{M,N}_{Gamma,Gamma'}"
            ),
            status=(
                "absent in the minimal full-equivariant package; in a larger "
                "package it is a defined cochain only after K^M_Gamma and d_M "
                "K^M_Gamma are supplied"
            ),
        ),
        GenuineOrderTwoRow(
            branch="full_equivariant",
            row_kind="CE source face of genuine |Gamma|_hbar=2 seed",
            row_formula="R_{CE(Gamma,nu),M}=-epsilon^CE_{Gamma,nu}*K^M_Gamma(zeta_{M,nu})",
            incidence_coefficient=(
                "epsilon^CE_{Gamma,nu} is the sign/coefficient of the "
                "source face in -kappa(d_CE zeta_M)"
            ),
            scalar_gate="0 if the source-face value lies in the full-equivariant marked habitat",
            non_scalar_contribution="-epsilon^CE_{Gamma,nu}*K^M_Gamma(zeta_{M,nu})",
            truncation_rule=(
                "pi_{M,N}R_{CE(Gamma,nu),M}="
                "sum_{Gamma',nu'} v^{M,N}_{Gamma,nu;Gamma',nu'} "
                "R_{CE(Gamma',nu'),N}; t=v"
            ),
            status=(
                "empty after evaluation on a strict CE cycle; otherwise "
                "missing until d_CE zeta_M and the source-face signs are supplied"
            ),
        ),
    ]


def truncation_matrix_families() -> list[TruncationMatrixFamily]:
    return [
        TruncationMatrixFamily(
            family="one-cross scalar-contact row alpha_sc",
            rows=("alpha_sc",),
            retained_window_condition="M>=N>=1; otherwise the degree-one row is omitted",
            matrix_entries=(
                "t^{M,N}_{alpha_sc,alpha_sc}=1; "
                "t^{M,N}_{alpha_sc,alpha'}=0 for alpha'!=alpha_sc"
            ),
            stability="identity row: t^{M,P}=t^{M,N} t^{N,P}",
            deciding_evidence="pi_{M,N} preserves the degree-one labels z1,z2",
            missing_entries="none for the computed labelled row",
            status=(
                "computed; in the full-equivariant branch the row value is zero, "
                "but the label-retaining matrix is the chosen transport"
            ),
        ),
        TruncationMatrixFamily(
            family="scalar-zero row alpha_11",
            rows=("alpha_11",),
            retained_window_condition="M>=N>=1 when labelled zero rows are retained",
            matrix_entries=(
                "t^{M,N}_{alpha_11,alpha_11}=1; "
                "t^{M,N}_{alpha_11,alpha'}=0 for alpha'!=alpha_11"
            ),
            stability="identity row if retained; empty matrix if zero rows are suppressed",
            deciding_evidence="omega(z1,z1)=0, so both row value and scalar gate vanish",
            missing_entries="none for the retained labelled zero row",
            status="computed zero row; no non-scalar obstruction and C_{1,M}=0",
        ),
        TruncationMatrixFamily(
            family="codimension-two scalar-contact composites",
            rows=("gamma_21=(beta_2|beta_1,beta_1)", "gamma_12=(beta_1|beta_2,beta_2)"),
            retained_window_condition="lower window contains the two degree-one Hamiltonian labels",
            matrix_entries=(
                "diagonal identity on gamma_21 and gamma_12; all off-diagonal "
                "entries from these rows are 0"
            ),
            stability="diagonal identity rows preserve the codimension-two pair cancellation",
            deciding_evidence=(
                "finite-window projection preserves output graph, coefficient product, "
                "marker transport, and incidence signs"
            ),
            missing_entries="none for the computed codimension-two pair",
            status="computed; rowwise zero in the full-equivariant branch",
        ),
        TruncationMatrixFamily(
            family="order-two bracket rows containing a zero contact row",
            rows=(
                "b(alpha_sc,beta)",
                "b(beta,alpha_sc)",
                "b(alpha_sc,alpha_sc)",
                "b(alpha_11,beta)",
                "b(beta,alpha_11)",
                "b(alpha_11,alpha_11)",
            ),
            retained_window_condition="row is present only if the chosen graph package keeps it",
            matrix_entries="t^{M,N}_{b,b'}=0 for every lower-window bracket row b'",
            stability="zero rows compose to zero",
            deciding_evidence=(
                "K^M_{alpha_sc}=0 in the full-equivariant branch and "
                "K^M_{alpha_11}=0 because omega(z1,z1)=0; the bracket is bilinear"
            ),
            missing_entries="none for bracket rows containing alpha_sc or alpha_11",
            status="computed zero family",
        ),
        TruncationMatrixFamily(
            family="genuine |Gamma|_hbar=2 seed rows",
            rows=("dGamma", "CE(Gamma,nu)"),
            retained_window_condition=(
                "empty in the minimal full-equivariant package; in a larger "
                "package only after lower-window row bases are fixed"
            ),
            matrix_entries=(
                "t^{M,N}_{dGamma,dGamma'}=u^{M,N}_{Gamma,Gamma'}; "
                "t^{M,N}_{CE(Gamma,nu),CE(Gamma',nu')}="
                "v^{M,N}_{Gamma,nu;Gamma',nu'}"
            ),
            stability=(
                "u^{M,P}=u^{M,N}u^{N,P} and v^{M,P}=v^{M,N}v^{N,P} "
                "entrywise over intermediate graph/source labels"
            ),
            deciding_evidence="actual normalized weights K^M_Gamma and source faces",
            missing_entries=(
                "the coordinate entries of pi_{M,N}(epsilon_Gamma K^M_Gamma) "
                "and pi_{M,N}(-epsilon^CE_{Gamma,nu}K^M_Gamma(zeta_{M,nu})) "
                "until row bases, weights, source faces, and signs are supplied"
            ),
            status="defined conditionally as projection-coordinate matrices",
        ),
        TruncationMatrixFamily(
            family="nonzero added order-one bracket rows",
            rows=("b(beta_1,beta_2), beta_i not in {alpha_sc,alpha_11}",),
            retained_window_condition=(
                "only after the added order-one rows and lower-window bracket "
                "row basis or presentation are supplied"
            ),
            matrix_entries=(
                "q^{M,N}_{beta_1,beta_2;beta'_1,beta'_2} is defined by "
                "projecting 1/2 epsilon_{beta_1,beta_2}{K^M_{beta_1},K^M_{beta_2}}"
            ),
            stability="q^{M,P}=q^{M,N}q^{N,P} over intermediate bracket labels",
            deciding_evidence=(
                "actual order-one row values, signs, bracket expansion, and "
                "basis-reduction matrix for lower-window bracket rows"
            ),
            missing_entries=(
                "the coordinate entries q for beta_1,beta_2 not equal to "
                "alpha_sc or alpha_11"
            ),
            status="defined conditionally as a projection-coordinate matrix",
        ),
    ]


def projection_defined_uvq_data() -> list[ProjectionMatrixRule]:
    return [
        ProjectionMatrixRule(
            family="u genuine seed projection",
            normalized_row="G^M_Gamma = epsilon_Gamma*K^M_Gamma",
            projection_formula=(
                "pi_{M,N}G^M_Gamma=sum_{Gamma'} "
                "u^{M,N}_{Gamma,Gamma'} G^N_Gamma'"
            ),
            matrix_entry=(
                "u^{M,N}_{Gamma,Gamma'} is the Gamma' coordinate of "
                "pi_{M,N}(epsilon_Gamma*K^M_Gamma) in the chosen lower-window "
                "basis {epsilon_Gamma'*K^N_Gamma'}"
            ),
            compatibility=(
                "u^{M,P}_{Gamma,Gamma''}=sum_{Gamma'} "
                "u^{M,N}_{Gamma,Gamma'} u^{N,P}_{Gamma',Gamma''}"
            ),
            required_data=(
                "finite seed sets G^{gen}_{2,M} and G^{gen}_{2,N}",
                "normalized weights epsilon_Gamma*K^M_Gamma",
                "lower-window row basis or presentation",
                "proof that pi_{M,N} of every normalized seed lies in the lower span",
            ),
            obstruction_use=(
                "defines the dGamma truncation rows because pi_{M,N}d_M=d_N pi_{M,N}"
            ),
            status="formula defined; numerical entries missing without actual weights",
        ),
        ProjectionMatrixRule(
            family="v CE source-face projection",
            normalized_row=(
                "E^M_{Gamma,nu}=-epsilon^CE_{Gamma,nu}*K^M_Gamma(zeta_{M,nu})"
            ),
            projection_formula=(
                "pi_{M,N}E^M_{Gamma,nu}=sum_{Gamma',nu'} "
                "v^{M,N}_{Gamma,nu;Gamma',nu'} E^N_{Gamma',nu'}"
            ),
            matrix_entry=(
                "v^{M,N}_{Gamma,nu;Gamma',nu'} is the (Gamma',nu') coordinate "
                "of the projected normalized source face"
            ),
            compatibility=(
                "v^{M,P}_{Gamma,nu;Gamma'',nu''}=sum_{Gamma',nu'} "
                "v^{M,N}_{Gamma,nu;Gamma',nu'} "
                "v^{N,P}_{Gamma',nu';Gamma'',nu''}"
            ),
            required_data=(
                "CE-source decomposition d_CE zeta_M",
                "source-face signs epsilon^CE_{Gamma,nu}",
                "source transport zeta_{M,nu}->zeta_{N,nu'}",
                "normalized source-face row basis or presentation",
                "proof that the projected source face lies in the lower span",
            ),
            obstruction_use=(
                "decides the CE-source summand in R^{ns,gen}_{2,M}; empty after "
                "strict CE-cycle evaluation"
            ),
            status="formula defined; numerical entries missing without CE source data",
        ),
        ProjectionMatrixRule(
            family="q nonzero added bracket projection",
            normalized_row=(
                "B^M_{beta_1,beta_2}=1/2*epsilon^M_{beta_1,beta_2}"
                "*{K^M_{beta_1},K^M_{beta_2}}_{hbar,M}"
            ),
            projection_formula=(
                "pi_{M,N}B^M_{beta_1,beta_2}=sum_{beta'_1,beta'_2} "
                "q^{M,N}_{beta_1,beta_2;beta'_1,beta'_2} "
                "B^N_{beta'_1,beta'_2}"
            ),
            matrix_entry=(
                "q is the lower-window bracket-row coordinate of the projected "
                "normalized bracket row; if raw ordered bracket rows are retained "
                "and pi K^M_beta=sum r^{M,N}_{beta,eta}K^N_eta, then "
                "q=(epsilon^M_{beta_1,beta_2}/epsilon^N_{beta'_1,beta'_2}) "
                "r_{beta_1,beta'_1} r_{beta_2,beta'_2}"
            ),
            compatibility=(
                "q^{M,P}_{beta_1,beta_2;theta_1,theta_2}=sum_{beta'_1,beta'_2} "
                "q^{M,N}_{beta_1,beta_2;beta'_1,beta'_2} "
                "q^{N,P}_{beta'_1,beta'_2;theta_1,theta_2}"
            ),
            required_data=(
                "nonzero order-one row values K^M_beta excluding alpha_sc and alpha_11",
                "order-one transport matrix r^{M,N}_{beta,beta'}",
                "BV bracket signs epsilon^M_{beta_1,beta_2}",
                "lower-window bracket row basis or basis-reduction matrix",
                "proof that pi_{M,N} is a BV-bracket map on the chosen rows",
            ),
            obstruction_use=(
                "decides the bracket summand 1/2 sum {K_1,K_2} in the "
                "order-two non-scalar QME residual"
            ),
            status="formula defined; numerical entries missing without added order-one rows",
        ),
    ]


def concrete_order_three_ce_source_row() -> ConcreteOrderThreeCESourceRow:
    return ConcreteOrderThreeCESourceRow(
        branch="full_equivariant",
        row_label="theta_3=CE(Theta_3,nu_3)",
        graph_type="CE-source face of a genuine |Theta_3|_hbar=3 marked seed",
        hbar_order=3,
        coefficient_window_degree=3,
        source_face_label=(
            "d_CE zeta_M contains +zeta_{M,nu_3}; the curvature term "
            "-kappa(d_CE zeta_M) gives the displayed minus sign"
        ),
        edge_labels=(
            "e_pp: P^{w,M}_{epsilon,L} with half-edge labels h_{2,1}=z1^2 z2 and rho_{2,1}",
            "e_ct: Delta^{w,M}_{epsilon,L} with half-edge labels h_{1,1}=z1 z2 and rho_{1,1}",
            "e_W: E_Weyl with Hamiltonian labels z1^2 and z2; omega(z1^2,z2)=0",
        ),
        vertex_labels=(
            "u_{a dt tensor z1^2}",
            "u_{b dt tensor z2}",
            "c_{B_theta,rho_{2,1}} with B_theta in D_c^reg(I)",
            "I^w_{0,M}",
            "W^{R,M}_{Theta_3,L,w}(B^Theta_bullet)",
        ),
        marker_tensor=(
            "full gl(N|N)-equivariant signed Brauer marker "
            "m_{theta_3} in M^{full}(C^{N|N}) with cyclic supertrace zero"
        ),
        ce_source_sign=1,
        incidence_sign_in_row_value=-1,
        row_value=(
            "R_{theta_3,M}^{row}=-K^M_{Theta_3}(zeta_{M,nu_3})"
            "=:E^M_{theta_3}, declared nonzero as a local functional"
        ),
        row_closure=(
            "d_{ns,M} E^M_{theta_3}=0 is supplied as the row-closure "
            "datum; without it no H^1 class is formed"
        ),
        scalar_gate=(
            "S_{theta_3,M}=0 in the full-equivariant marked habitat; "
            "the displayed Weyl scalar contact also has omega(z1^2,z2)=0"
        ),
        truncation_matrix=(
            "for M>=N: t^{M,N}_{theta_3,theta_3}=1 if N>=3; "
            "all off-diagonal entries are 0; if N<3 the row has no "
            "degree<=N representative and every t entry is 0"
        ),
        class_in_K_ns=(
            "o^{ns}_{theta_3,M}=[E^M_{theta_3}] in "
            "H^1(K^bullet_{ns,M}(I),d_{ns,M})"
        ),
        counterterm_criterion=(
            "C_{theta_3,M} exists exactly when "
            "[E^M_{theta_3}]=0 and d_M C_{theta_3,M}=-E^M_{theta_3}"
        ),
        decision=(
            "nonzero cochain with zero scalar gate; no primitive is supplied, "
            "so the row remains an explicit symbolic obstruction datum"
        ),
    )


def theta3_common_finite_window_record() -> Theta3CommonFiniteWindowRecord:
    return Theta3CommonFiniteWindowRecord(
        row_label=THETA3_ROW,
        graph_label="Theta_3",
        hbar_order=3,
        finite_window_degree=3,
        source_face="nu_3",
        source_face_coefficient=1,
        row_value="E_theta_3=-K^M_{Theta_3}(zeta_{M,nu_3})",
        row_closure="d_{ns,M}E_theta_3=0 is a supplied row-closure datum",
        scalar_projection=0,
        truncation_n_ge_3="pi_{M,N}E_theta_3,M=E_theta_3,N",
        truncation_n_lt_3="0",
        inherited_labels=(
            "P^{w,M}_{epsilon,L}(h_{2,1},rho_{2,1})",
            "Delta^{w,M}_{epsilon,L}(h_{1,1},rho_{1,1})",
            "E_Weyl(z1^2,z2)",
            "u_{a(t)dt tensor z1^2}",
            "u_{b(t)dt tensor z2}",
            "c_{B_theta,rho_{2,1}}",
            "I^w_{0,M}",
            "W^{R,M}_{Theta_3,L,w}(B^Theta_bullet)",
        ),
        marker_tensor=(
            "full gl(N|N)-equivariant Brauer marker m_theta_3 with "
            "cyclic supertrace zero"
        ),
        current_status=(
            "present as a closed scalar-zero degree-one row; no current "
            "degree-zero primitive or complete companion-face table is supplied"
        ),
    )


def theta3_identity_zero_transport() -> Theta3PrimitiveTransport:
    return Theta3PrimitiveTransport(
        row_transport_n_ge_3=1,
        primitive_transport_n_ge_3=1,
        row_transport_n_lt_3=0,
        primitive_transport_n_lt_3=0,
        roos_class=0,
    )


def theta3_primitive_payloads() -> list[Theta3PrimitivePayload]:
    identity_zero_transport = theta3_identity_zero_transport()
    return [
        Theta3PrimitivePayload(
            case="theta3_ce_ancestor_absent_payload",
            payload_kind="ce_ancestor",
            supplied=False,
            primitive_label="C_theta_3_CE",
            source_boundary_entries=(),
            bianchi_or_locality_verified=False,
            differential_entries=(),
            scalar_projection=None,
            transport=None,
            provenance="current finite row package",
        ),
        Theta3PrimitivePayload(
            case="theta3_ce_ancestor_without_differential_entry",
            payload_kind="ce_ancestor",
            supplied=True,
            primitive_label="C_theta_3_CE",
            source_boundary_entries=(("eta_theta_3", "zeta_M_nu_3", 1),),
            bianchi_or_locality_verified=True,
            differential_entries=(),
            scalar_projection=0,
            transport=identity_zero_transport,
            provenance=(
                "guard case: CE ancestor data without the required "
                "differential entry"
            ),
        ),
        Theta3PrimitivePayload(
            case="theta3_ce_ancestor_supplied_exact_payload",
            payload_kind="ce_ancestor",
            supplied=True,
            primitive_label="C_theta_3_CE",
            source_boundary_entries=(("eta_theta_3", "zeta_M_nu_3", 1),),
            bianchi_or_locality_verified=True,
            differential_entries=(("C_theta_3_CE", THETA3_ROW, -1),),
            scalar_projection=0,
            transport=identity_zero_transport,
            provenance=(
                "interface fixture for the Agent 193/197 CE-ancestor "
                "payload; not present in the current data"
            ),
        ),
        Theta3PrimitivePayload(
            case="theta3_counterterm_absent_payload",
            payload_kind="counterterm_primitive",
            supplied=False,
            primitive_label="C_theta_3_ct",
            source_boundary_entries=(),
            bianchi_or_locality_verified=False,
            differential_entries=(),
            scalar_projection=None,
            transport=None,
            provenance="current finite row package",
        ),
        Theta3PrimitivePayload(
            case="theta3_counterterm_without_differential_entry",
            payload_kind="counterterm_primitive",
            supplied=True,
            primitive_label="C_theta_3_ct",
            source_boundary_entries=(),
            bianchi_or_locality_verified=True,
            differential_entries=(),
            scalar_projection=0,
            transport=identity_zero_transport,
            provenance=(
                "guard case: local counterterm data without the required "
                "differential entry"
            ),
        ),
        Theta3PrimitivePayload(
            case="theta3_counterterm_supplied_exact_payload",
            payload_kind="counterterm_primitive",
            supplied=True,
            primitive_label="C_theta_3_ct",
            source_boundary_entries=(),
            bianchi_or_locality_verified=True,
            differential_entries=(("C_theta_3_ct", THETA3_ROW, -1),),
            scalar_projection=0,
            transport=identity_zero_transport,
            provenance=(
                "interface fixture for the Agent 193/197 local-counterterm "
                "payload; not present in the current data"
            ),
        ),
    ]


def theta3_primitive_search_for_payload(
    payload: Theta3PrimitivePayload,
) -> PrimitiveSearchResult:
    degree_zero_basis = (payload.primitive_label,) if payload.supplied else ()
    differential_entries = payload.differential_entries if payload.supplied else ()
    return primitive_search(
        case=payload.case,
        scalar_gate=(
            "sigma_sc(C_theta_3)=0 and sigma_sc(E_theta_3)=0"
            if scalar_zero_value(payload.scalar_projection)
            else "missing or nonzero scalar projection"
        ),
        degree_zero_basis=degree_zero_basis,
        degree_one_basis=(THETA3_ROW,),
        differential_entries=differential_entries,
        residual_entries=THETA3_RESIDUAL,
        roos_compatibility=(
            "identity/zero primitive transport and Roos class 0"
            if payload.transport is not None
            and scalar_zero_value(payload.transport.roos_class)
            else "not represented"
        ),
        status=payload.provenance,
    )


def theta3_transport_identity_verified(
    transport: Theta3PrimitiveTransport | None,
    differential_coefficient: Fraction,
) -> bool:
    if transport is None:
        return False
    row_ge = as_fraction(transport.row_transport_n_ge_3)
    primitive_ge = as_fraction(transport.primitive_transport_n_ge_3)
    row_lt = as_fraction(transport.row_transport_n_lt_3)
    primitive_lt = as_fraction(transport.primitive_transport_n_lt_3)
    above_degree_three = row_ge * differential_coefficient == (
        differential_coefficient * primitive_ge
    )
    below_degree_three = row_lt * differential_coefficient == (
        Fraction(0) * primitive_lt
    )
    return above_degree_three and below_degree_three


def theta3_support_data_verified(payload: Theta3PrimitivePayload) -> bool:
    if payload.payload_kind == "counterterm_primitive":
        return payload.bianchi_or_locality_verified
    return payload.bianchi_or_locality_verified and any(
        source == "eta_theta_3"
        and target == "zeta_M_nu_3"
        and as_fraction(coefficient) == 1
        for source, target, coefficient in payload.source_boundary_entries
    )


def theta3_primitive_payload_check(
    payload: Theta3PrimitivePayload,
) -> Theta3PrimitivePayloadCheck:
    differential_value = coefficient_sum(
        payload.differential_entries,
        payload.primitive_label,
        THETA3_ROW,
    )
    differential_entry_present = any(
        primitive == payload.primitive_label and row == THETA3_ROW
        for primitive, row, _ in payload.differential_entries
    )
    dC_equals_minus_E = differential_value == -1
    scalar_zero = scalar_zero_value(payload.scalar_projection)
    transport_identity = theta3_transport_identity_verified(
        payload.transport,
        differential_value,
    )
    roos_compatible = (
        payload.transport is not None
        and scalar_zero_value(payload.transport.roos_class)
    )
    support_verified = theta3_support_data_verified(payload)
    search = theta3_primitive_search_for_payload(payload)

    missing: list[str] = []
    if not payload.supplied:
        missing.append("payload")
    if not support_verified:
        if payload.payload_kind == "ce_ancestor":
            missing.append("CE boundary d_CE eta=zeta_nu3 and Hom-valued Bianchi closure")
        else:
            missing.append("locality proof for counterterm primitive")
    if not differential_entry_present:
        missing.append("differential entry dC=-E")
    elif not dC_equals_minus_E:
        missing.append("differential coefficient -1")
    if not scalar_zero:
        missing.append("scalar projection zero")
    if payload.transport is None:
        missing.append("primitive transport")
    elif not transport_identity:
        missing.append("matrix identity T A = A P")
    if not roos_compatible:
        missing.append("zero Roos class")

    accepted = (
        payload.supplied
        and support_verified
        and dC_equals_minus_E
        and scalar_zero
        and transport_identity
        and roos_compatible
        and search.primitive_exists
    )
    if accepted:
        status = (
            "accepted as a supplied payload: the named primitive has "
            "dC=-E, scalar projection zero, T A = A P, and zero Roos class"
        )
    else:
        status = (
            "rejected as a current healing datum; the listed fields are "
            "absent or insufficient"
        )

    return Theta3PrimitivePayloadCheck(
        case=payload.case,
        payload_kind=payload.payload_kind,
        supplied=payload.supplied,
        accepted=accepted,
        support_data_verified=support_verified,
        differential_entry_present=differential_entry_present,
        differential_entry_value=fraction_text(differential_value),
        dC_equals_minus_E=dC_equals_minus_E,
        scalar_zero_verified=scalar_zero,
        transport_identity_verified=transport_identity,
        roos_compatibility_verified=roos_compatible,
        missing_fields=tuple(missing),
        primitive_search=search,
        status=status,
    )


def theta3_primitive_payload_checks() -> list[Theta3PrimitivePayloadCheck]:
    return [
        theta3_primitive_payload_check(payload)
        for payload in theta3_primitive_payloads()
    ]


def theta3_eight_face_candidate_faces() -> tuple[Theta3CompanionFace, ...]:
    return (
        Theta3CompanionFace(
            face_label="nu_02",
            ce_coefficient=2,
            residual_coordinates=(("E_nu02", 2),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{0,1}}u_{b,H_{0,1}}"
                "c_{B_theta,rho_{0,2}}"
            ),
            hamiltonian_degree=2,
            row_contribution="2E_nu02",
        ),
        Theta3CompanionFace(
            face_label="nu_20",
            ce_coefficient=-2,
            residual_coordinates=(("E_nu20", -2),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{1,0}}u_{b,H_{1,0}}"
                "c_{B_theta,rho_{2,0}}"
            ),
            hamiltonian_degree=2,
            row_contribution="-2E_nu20",
        ),
        Theta3CompanionFace(
            face_label="nu_03",
            ce_coefficient=3,
            residual_coordinates=(("E_nu03", 3),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{0,2}}u_{b,H_{0,1}}"
                "c_{B_theta,rho_{0,3}}"
            ),
            hamiltonian_degree=3,
            row_contribution="3E_nu03",
        ),
        Theta3CompanionFace(
            face_label="nu_12_1",
            ce_coefficient=2,
            residual_coordinates=(("E_nu12_1", 2),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{1,1}}u_{b,H_{0,1}}"
                "c_{B_theta,rho_{1,2}}"
            ),
            hamiltonian_degree=3,
            row_contribution="2E_nu12_1",
        ),
        Theta3CompanionFace(
            face_label="nu_12_2",
            ce_coefficient=-1,
            residual_coordinates=(("E_nu12_2", -1),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{1,0}}u_{b,H_{0,2}}"
                "c_{B_theta,rho_{1,2}}"
            ),
            hamiltonian_degree=3,
            row_contribution="-E_nu12_2",
        ),
        Theta3CompanionFace(
            face_label="nu_3=nu_21_1",
            ce_coefficient=1,
            residual_coordinates=((THETA3_ROW, 1),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{2,0}}u_{b,H_{0,1}}"
                "c_{B_theta,rho_{2,1}}"
            ),
            hamiltonian_degree=3,
            row_contribution="E_theta_3",
        ),
        Theta3CompanionFace(
            face_label="nu_21_2",
            ce_coefficient=-2,
            residual_coordinates=(("E_nu21_2", -2),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{1,0}}u_{b,H_{1,1}}"
                "c_{B_theta,rho_{2,1}}"
            ),
            hamiltonian_degree=3,
            row_contribution="-2E_nu21_2",
        ),
        Theta3CompanionFace(
            face_label="nu_30",
            ce_coefficient=-3,
            residual_coordinates=(("E_nu30", -3),),
            scalar_projection=0,
            source_face=(
                "u_{a,H_{1,0}}u_{b,H_{2,0}}"
                "c_{B_theta,rho_{3,0}}"
            ),
            hamiltonian_degree=3,
            row_contribution="-3E_nu30",
        ),
    )


def theta3_eight_face_candidate_entries() -> tuple[tuple[str, int | str], ...]:
    return tuple(
        (row_label, coefficient)
        for face in theta3_eight_face_candidate_faces()
        for row_label, coefficient in face.residual_coordinates
    )


def theta3_eight_face_n2_residual_entries() -> tuple[tuple[str, int | str], ...]:
    return tuple(
        (row_label, coefficient)
        for face in theta3_eight_face_candidate_faces()
        if face.hamiltonian_degree is not None and face.hamiltonian_degree <= 2
        for row_label, coefficient in face.residual_coordinates
    )


def theta3_diagonal_v_transport_obstruction() -> Theta3DiagonalVTransportObstruction:
    faces = theta3_eight_face_candidate_faces()
    degree_two = tuple(
        face.face_label for face in faces if face.hamiltonian_degree == 2
    )
    degree_three = tuple(
        face.face_label for face in faces if face.hamiltonian_degree == 3
    )
    n_ge_3 = vector_from_coordinate_entries(theta3_eight_face_candidate_entries())
    n_2 = vector_from_coordinate_entries(theta3_eight_face_n2_residual_entries())
    return Theta3DiagonalVTransportObstruction(
        transport_formula=(
            "v^{M,N}_{nu;nu'}=1 when nu=nu' and degree(nu)<=N; "
            "otherwise 0"
        ),
        degree_two_faces=degree_two,
        degree_three_faces=degree_three,
        n_ge_3_residual_vector=n_ge_3,
        n_2_residual_vector=n_2,
        cocycle_identity_verified=True,
        lower_window_residual_zero_verified=False,
        missing_lower_window_identity=(
            "E^2_nu02=E^2_nu20 in the chosen lower-window row basis, "
            "or a recomputed lower-window presentation"
        ),
        status=(
            "diagonal source-face transport is a cocycle, but it exposes "
            "the N=2 residual 2E_nu02-2E_nu20"
        ),
    )


def theta3_marked_costello_table_obstruction() -> Theta3MarkedCostelloTableObstruction:
    required_entries = (
        "labelled d_CE zeta_M including B_theta, a, and b current labels",
        "epsilon^CE_{Theta_3,nu} after Costello orientation/Koszul signs",
        "renormalized weights K^M_{Theta_3}(zeta_{M,nu}) in one row basis",
        "marked output graph and marker transport mu_nu for every face",
        "v^{M,N}_{nu;nu'} projection coordinates after basis reduction",
        "codimension-two incidence table C^{(2)}_{nu,nu'}",
    )
    return Theta3MarkedCostelloTableObstruction(
        required_entries=required_entries,
        supplied_entries=(
            "source-algebraic monomial CE coefficients for the eight faces",
            "formal diagonal source-face cutoff v",
        ),
        missing_entries=required_entries,
        codimension_two_closure_supplied=False,
        deciding_evidence=(
            "compute the marked Costello source-face incidence/weight table "
            "and prove both R_cand=0 at M>=3 and the transported N=2 "
            "residual is zero"
        ),
        status=(
            "missing theorem-grade incidence/weight table; source "
            "coefficients alone do not determine row cancellation"
        ),
    )


def theta3_eight_face_candidate_obstruction_check(
) -> Theta3EightFaceCandidateObstructionCheck:
    faces = theta3_eight_face_candidate_faces()
    entries = theta3_eight_face_candidate_entries()
    residual_vector = vector_from_coordinate_entries(entries)
    scalar_zero = all(scalar_zero_value(face.scalar_projection) for face in faces)
    signed_coordinates_verified = theta3_companion_signed_coordinates_verified(
        Theta3CompanionFacePayload(
            case="theta3_eight_face_candidate_source_algebraic_obstruction",
            supplied=True,
            faces=faces,
            residual_sum_declared=0,
            v_truncation_matrices_supplied=True,
            v_cocycle_identity_verified=True,
            codimension_two_closure_supplied=False,
            provenance="Agent 215/221 eight-face source-algebraic table",
            signed_coordinates_verified_from_ce_coefficients=True,
        )
    )
    diagonal_v = theta3_diagonal_v_transport_obstruction()
    marked_table = theta3_marked_costello_table_obstruction()

    missing = [
        "zero residual vector in the common degree-one row basis",
        "marked Costello incidence/weight table",
        "codimension-two closure table",
        "transported lower-window residual zero",
    ]
    exact_obstruction = (
        "R_cand=2E_nu02-2E_nu20+3E_nu03+2E_nu12_1-E_nu12_2"
        "+E_theta_3-2E_nu21_2-3E_nu30; diagonal v sends it at N=2 "
        "to 2E_nu02-2E_nu20; the marked Costello incidence/weight "
        "table is absent"
    )

    return Theta3EightFaceCandidateObstructionCheck(
        case="theta3_eight_face_candidate_source_algebraic_obstruction",
        accepted=False,
        face_count=len(faces),
        faces=faces,
        candidate_residual_formula=(
            "R_cand=2E_nu02-2E_nu20+3E_nu03+2E_nu12_1"
            "-E_nu12_2+E_theta_3-2E_nu21_2-3E_nu30"
        ),
        candidate_residual_vector=residual_vector,
        candidate_residual_coefficient_sum=fraction_text(
            coefficient_total(entries)
        ),
        source_ce_coefficients_verified=signed_coordinates_verified,
        scalar_zero_verified=scalar_zero,
        diagonal_v_transport=diagonal_v,
        marked_costello_table=marked_table,
        missing_fields=tuple(missing),
        exact_obstruction=exact_obstruction,
        status=(
            "rejected as theorem-grade companion cancellation; it is an "
            "explicit obstruction datum until the marked Costello table "
            "and lower-window transport identity are supplied"
        ),
    )


def theta3_companion_face_payloads() -> list[Theta3CompanionFacePayload]:
    return [
        Theta3CompanionFacePayload(
            case="theta3_complete_companion_faces_absent_payload",
            supplied=False,
            faces=(),
            residual_sum_declared=None,
            v_truncation_matrices_supplied=False,
            v_cocycle_identity_verified=False,
            codimension_two_closure_supplied=False,
            provenance="current finite row package",
        ),
        Theta3CompanionFacePayload(
            case="theta3_companion_faces_incomplete_one_face",
            supplied=True,
            faces=(
                Theta3CompanionFace(
                    face_label="nu_3",
                    ce_coefficient=1,
                    residual_coordinates=((THETA3_ROW, 1),),
                    scalar_projection=0,
                ),
            ),
            residual_sum_declared=1,
            v_truncation_matrices_supplied=False,
            v_cocycle_identity_verified=False,
            codimension_two_closure_supplied=False,
            provenance="guard case: the current one-face table does not cancel",
            signed_coordinates_verified_from_ce_coefficients=True,
        ),
        Theta3CompanionFacePayload(
            case="theta3_eight_face_candidate_source_algebraic_obstruction",
            supplied=True,
            faces=theta3_eight_face_candidate_faces(),
            residual_sum_declared=0,
            v_truncation_matrices_supplied=True,
            v_cocycle_identity_verified=True,
            codimension_two_closure_supplied=False,
            provenance=(
                "Agent 215/221 eight-face source-algebraic candidate; "
                "not a marked Costello incidence/weight theorem"
            ),
            signed_coordinates_verified_from_ce_coefficients=True,
            marked_costello_incidence_weight_table_supplied=False,
            lower_window_residual_zero_verified=False,
            exact_obstruction=(
                "R_cand is nonzero in the displayed row basis and "
                "projects to 2E_nu02-2E_nu20 at N=2"
            ),
        ),
        Theta3CompanionFacePayload(
            case="theta3_companion_faces_cancelling_coordinates_unverified_ce",
            supplied=True,
            faces=(
                Theta3CompanionFace(
                    face_label="nu_3",
                    ce_coefficient=1,
                    residual_coordinates=((THETA3_ROW, 1),),
                    scalar_projection=0,
                ),
                Theta3CompanionFace(
                    face_label="nu_bad",
                    ce_coefficient=1,
                    residual_coordinates=((THETA3_ROW, -1),),
                    scalar_projection=0,
                ),
            ),
            residual_sum_declared=0,
            v_truncation_matrices_supplied=True,
            v_cocycle_identity_verified=True,
            codimension_two_closure_supplied=True,
            provenance=(
                "guard case: signed residual coordinates cancel, but the "
                "second coordinate is not the CE coefficient times the "
                "normalized face row"
            ),
            signed_coordinates_verified_from_ce_coefficients=False,
        ),
        Theta3CompanionFacePayload(
            case="theta3_complete_companion_faces_supplied_exact_payload",
            supplied=True,
            faces=(
                Theta3CompanionFace(
                    face_label="nu_3",
                    ce_coefficient=1,
                    residual_coordinates=((THETA3_ROW, 1),),
                    scalar_projection=0,
                ),
                Theta3CompanionFace(
                    face_label="nu_i",
                    ce_coefficient=-1,
                    residual_coordinates=((THETA3_ROW, -1),),
                    scalar_projection=0,
                ),
            ),
            residual_sum_declared=0,
            v_truncation_matrices_supplied=True,
            v_cocycle_identity_verified=True,
            codimension_two_closure_supplied=True,
            provenance=(
                "guard case: a syntactic zero-sum companion table without "
                "the marked Costello incidence/weight theorem and "
                "lower-window transport cancellation"
            ),
            signed_coordinates_verified_from_ce_coefficients=True,
        ),
    ]


def theta3_companion_signed_coordinates_verified(
    payload: Theta3CompanionFacePayload,
) -> bool:
    if not payload.signed_coordinates_verified_from_ce_coefficients:
        return False
    if not payload.faces:
        return False
    for face in payload.faces:
        try:
            ce_coefficient = as_fraction(face.ce_coefficient)
        except ValueError:
            return False
        if not face.residual_coordinates:
            return False
        for _, residual_coefficient in face.residual_coordinates:
            if as_fraction(residual_coefficient) != ce_coefficient:
                return False
    return True


def theta3_companion_face_payload_check(
    payload: Theta3CompanionFacePayload,
) -> Theta3CompanionFacePayloadCheck:
    coordinate_entries = tuple(
        entry
        for face in payload.faces
        for entry in face.residual_coordinates
    )
    residual_vector = vector_from_coordinate_entries(coordinate_entries)
    residual_zero = (
        len(residual_vector) == 0
        and scalar_zero_value(payload.residual_sum_declared)
    )
    scalar_zero = bool(payload.faces) and all(
        scalar_zero_value(face.scalar_projection)
        for face in payload.faces
    )
    v_verified = (
        payload.v_truncation_matrices_supplied
        and payload.v_cocycle_identity_verified
    )
    marked_table_verified = payload.marked_costello_incidence_weight_table_supplied
    lower_window_verified = payload.lower_window_residual_zero_verified
    signed_coordinates_verified = theta3_companion_signed_coordinates_verified(
        payload
    )

    missing: list[str] = []
    if not payload.supplied:
        missing.append("payload")
    if not payload.faces:
        missing.append("source faces")
    if not signed_coordinates_verified:
        missing.append("signed residual coordinates derived from CE coefficients")
    if not residual_zero:
        missing.append("zero signed residual sum")
    if not scalar_zero:
        missing.append("scalar projection zero for every face")
    if not v_verified:
        missing.append("v truncation matrices with cocycle identity")
    if not payload.codimension_two_closure_supplied:
        missing.append("codimension-two closure table")
    if not marked_table_verified:
        missing.append("marked Costello incidence/weight table")
    if not lower_window_verified:
        missing.append("transported lower-window residual zero")

    accepted = (
        payload.supplied
        and bool(payload.faces)
        and signed_coordinates_verified
        and residual_zero
        and scalar_zero
        and v_verified
        and payload.codimension_two_closure_supplied
        and marked_table_verified
        and lower_window_verified
    )
    if accepted:
        status = (
            "accepted as a supplied complete companion-face table; this "
            "changes the residual vector rather than supplying a primitive"
        )
        roos_compatibility = (
            "primitive Roos class is not formed; source-face tower "
            "compatibility is represented by the supplied v-cocycle"
        )
    else:
        status = (
            "rejected as a current companion-face healing datum; the "
            "complete theorem-grade face table is absent or incomplete"
        )
        roos_compatibility = "not reached"

    return Theta3CompanionFacePayloadCheck(
        case=payload.case,
        supplied=payload.supplied,
        accepted=accepted,
        face_count=len(payload.faces),
        residual_vector=residual_vector,
        residual_zero_verified=residual_zero,
        signed_coordinates_verified_from_ce_coefficients=signed_coordinates_verified,
        scalar_zero_verified=scalar_zero,
        v_truncation_verified=v_verified,
        codimension_two_closure_verified=payload.codimension_two_closure_supplied,
        marked_costello_table_verified=marked_table_verified,
        lower_window_residual_zero_verified=lower_window_verified,
        roos_compatibility=roos_compatibility,
        missing_fields=tuple(missing),
        exact_obstruction=payload.exact_obstruction,
        status=status,
    )


def theta3_companion_face_payload_checks() -> list[Theta3CompanionFacePayloadCheck]:
    return [
        theta3_companion_face_payload_check(payload)
        for payload in theta3_companion_face_payloads()
    ]


def finite_row_primitive_search_schema() -> dict[str, object]:
    return {
        "scalar_gate_first": (
            "the search is only run after sum_i r_i S_{i,M}=0; otherwise "
            "the residual is not in K^bullet_{ns,M}"
        ),
        "degree_one_rows": (
            "ordered dK, CE-source, bracket, lower-d, and lower-bracket "
            "rows rho_i in the finite graph array"
        ),
        "degree_zero_candidates": (
            "candidate counterterm rows eta_j supplied by the finite "
            "package; the script never invents eta_j"
        ),
        "boundary_matrix": (
            "A_{ij} is defined by d_{ns,M} eta_j=sum_i A_{ij} rho_i"
        ),
        "residual_vector": "R_M=sum_i r_i rho_i",
        "fixed_window_equation": "solve A c=-r over the declared coefficient field",
        "obstruction_certificate": (
            "if no solution exists, a left-null covector ell with ell A=0 "
            "and ell(r)!=0 certifies the nonzero H^1 class"
        ),
        "truncation_blocks": (
            "T^{M,N} is identity/zero on computed scalar-contact and zero "
            "rows, u on genuine seed rows, v on CE-source faces, and q on "
            "nonzero bracket rows"
        ),
        "tower_condition": (
            "T^{M,N}r_M=r_N and T^{M,N}A_M=A_NP^{M,N}; after choosing "
            "solutions c_M, the classes of P^{M,N}c_M-c_N form the Roos "
            "lim^1 cocycle"
        ),
    }


def primitive_search_results() -> list[PrimitiveSearchResult]:
    results = [
        primitive_search(
            case="minimal_full_equivariant_order_2_zero",
            scalar_gate="0; all computed scalar-contact, alpha_11, and zero-bracket rows vanish",
            degree_zero_basis=(),
            degree_one_basis=(),
            differential_entries=(),
            residual_entries=(),
            roos_compatibility=(
                "zero primitives are compatible under every truncation map; "
                "the Roos lim^1 class is 0"
            ),
            status="solved by C_{2,M}=0",
        ),
        primitive_search(
            case="theta_3_current_finite_row_subcomplex",
            scalar_gate="S_{theta_3,M}=0 in the full-equivariant marked habitat",
            degree_zero_basis=(),
            degree_one_basis=("E_theta_3",),
            differential_entries=(),
            residual_entries=(("E_theta_3", 1),),
            roos_compatibility=(
                "not reached: the fixed-window H^1 obstruction is already "
                "nonzero; if a primitive is later supplied, test "
                "[pi_{M,N}C_{theta_3,M}-C_{theta_3,N}] in H^0"
            ),
            status=(
                "exact obstruction in the displayed one-row finite complex; "
                "a larger local-functional complex may heal it only by adding "
                "a degree-zero candidate or companion rows"
            ),
        ),
    ]
    results.extend(
        check.primitive_search
        for check in theta3_primitive_payload_checks()
    )
    return results


def missing_order_two_row_types() -> list[str]:
    return [
        "actual finite seed list G^{gen}_{2,M} and the order assignment |Gamma|_hbar=2",
        "renormalized local weights K^M_Gamma=W^{R,M}_{Gamma,L,w}(B^Gamma_bullet)",
        "d_M K^M_Gamma expansions: Q, {I^w_{0,M},-}_{hbar,M}, collision, and counterterm faces",
        "orientation/Koszul/symmetry coefficients epsilon_Gamma for every genuine seed row",
        "CE-source decomposition d_CE zeta_M and coefficients epsilon^CE_{Gamma,nu}, unless evaluation is on a strict CE cycle",
        "BV/convolution bracket rows between order-1 components not containing alpha_sc or alpha_11",
        "[hbar^2] d_M C_<2,M and 1/2 [hbar^2] {C_<2,M, C_<2,M}_{hbar,M} if a nonminimal C_1,M is chosen",
        "proof that every genuine row lies in the full-equivariant marked habitat, or else its scalar projection",
        "regular-density or wavefront-admissible locality data for every external current label",
        "row bases or presentations for genuine, source-face, and nonzero bracket rows",
        "u^{M,N}_{Gamma,Gamma'} projection-coordinate matrices for normalized genuine weights",
        "v^{M,N}_{Gamma,nu;Gamma',nu'} projection-coordinate matrices for genuine CE source faces",
        "q^{M,N}_{beta_1,beta_2;beta'_1,beta'_2} projection-coordinate matrices for nonzero added bracket rows not containing alpha_sc or alpha_11",
    ]


def internal_consistency_checks() -> None:
    primitive_results = {
        row.case: row
        for row in primitive_search_results()
    }
    if primitive_results["theta_3_current_finite_row_subcomplex"].primitive_exists:
        raise AssertionError("current theta_3 obstruction case must remain unsolved")

    primitive_checks = {
        row.case: row
        for row in theta3_primitive_payload_checks()
    }
    for case in (
        "theta3_ce_ancestor_without_differential_entry",
        "theta3_counterterm_without_differential_entry",
    ):
        if primitive_checks[case].accepted:
            raise AssertionError(f"{case} must be rejected without dC=-E")
    for case in (
        "theta3_ce_ancestor_supplied_exact_payload",
        "theta3_counterterm_supplied_exact_payload",
    ):
        if not primitive_checks[case].accepted:
            raise AssertionError(f"{case} must be accepted when all fields are supplied")

    companion_checks = {
        row.case: row
        for row in theta3_companion_face_payload_checks()
    }
    if companion_checks["theta3_companion_faces_incomplete_one_face"].accepted:
        raise AssertionError("one-face companion table must not cancel theta_3")
    if companion_checks[
        "theta3_complete_companion_faces_supplied_exact_payload"
    ].accepted:
        raise AssertionError(
            "synthetic companion-face fixture must reject without marked "
            "Costello table and lower-window residual"
        )
    eight_face_companion = companion_checks[
        "theta3_eight_face_candidate_source_algebraic_obstruction"
    ]
    if eight_face_companion.accepted:
        raise AssertionError("eight-face source-algebraic candidate must reject")
    if eight_face_companion.face_count != 8:
        raise AssertionError("eight-face candidate must have exactly eight faces")

    eight_face_check = theta3_eight_face_candidate_obstruction_check()
    if eight_face_check.accepted:
        raise AssertionError("eight-face obstruction check must reject")
    if eight_face_check.face_count != 8:
        raise AssertionError("eight-face obstruction check lost a face")
    if eight_face_check.candidate_residual_coefficient_sum != "0":
        raise AssertionError("eight-face source coefficients must sum to zero")
    if not eight_face_check.candidate_residual_vector:
        raise AssertionError("eight-face row-vector residual must remain nonzero")
    if eight_face_check.diagonal_v_transport.n_2_residual_vector != (
        ("E_nu02", "2"),
        ("E_nu20", "-2"),
    ):
        raise AssertionError("diagonal v must expose the N=2 residual")
    if eight_face_check.diagonal_v_transport.lower_window_residual_zero_verified:
        raise AssertionError("N=2 residual is not theorem-grade zero")
    if eight_face_check.marked_costello_table.codimension_two_closure_supplied:
        raise AssertionError("missing marked Costello table was misrecorded")


def main() -> None:
    internal_consistency_checks()
    rows = [first_order_row(branch) for branch in Branch.__args__]  # type: ignore[attr-defined]
    order_two = {
        branch: [asdict(row) for row in second_order_composite_rows(branch)]
        for branch in Branch.__args__  # type: ignore[attr-defined]
    }
    payload = {
        "omega_z1_z2": omega_monomial(1, 0, 0, 1),
        "omega_z2_z1": omega_monomial(0, 1, 1, 0),
        "omega_z1_z1": omega_monomial(1, 0, 1, 0),
        "order_0_current_interface": {
            "curvature_row": "0",
            "scalar_gate": "0",
        },
        "order_1_scalar_contact_rows": [asdict(row) for row in rows],
        "order_1_scalar_zero_rows": [asdict(scalar_zero_alpha_11_row())],
        "order_2_boundary_composition_rows": order_two,
        "order_2_universal_scalar_contact_bracket_rows": [
            asdict(row) for row in universal_scalar_contact_bracket_rows()
        ],
        "order_2_genuine_graph_weight_rows": [
            asdict(row) for row in genuine_order_two_graph_weight_rows()
        ],
        "order_2_genuine_graph_weight_contribution": {
            "minimal_full_equivariant": "0 because G^{gen}_{2,M}=empty",
            "larger_full_equivariant_formula": (
                "R^{ns,gen}_{2,M}=sum_Gamma epsilon_Gamma*d_M K^M_Gamma "
                "-sum_{Gamma,nu} epsilon^CE_{Gamma,nu}*K^M_Gamma(zeta_{M,nu})"
            ),
            "counterterm_criterion": (
                "C^{gen}_{2,M} exists iff [R^{ns,gen}_{2,M}]=0 in "
                "H^1(K_ns,M,d_ns,M); a nonzero class is the obstruction"
            ),
            "current_status": "undecided without the missing weight/locality/truncation data",
        },
        "computed_truncation_matrix_families": [
            asdict(row) for row in truncation_matrix_families()
        ],
        "larger_package_uvq_projection_rules": [
            asdict(row) for row in projection_defined_uvq_data()
        ],
        "order_3_concrete_larger_package_row": asdict(
            concrete_order_three_ce_source_row()
        ),
        "theta_3_common_finite_window_record": asdict(
            theta3_common_finite_window_record()
        ),
        "theta_3_primitive_payload_checks": [
            asdict(row) for row in theta3_primitive_payload_checks()
        ],
        "theta_3_companion_face_payload_checks": [
            asdict(row) for row in theta3_companion_face_payload_checks()
        ],
        "theta_3_eight_face_candidate_obstruction_check": asdict(
            theta3_eight_face_candidate_obstruction_check()
        ),
        "finite_row_primitive_search_schema": finite_row_primitive_search_schema(),
        "finite_row_primitive_search_results": [
            asdict(row) for row in primitive_search_results()
        ],
        "order_2_codimension_two_pair_sum": {
            "ordinary_glN": "0 if codimension-two coefficients agree; scalar gate is not a non-scalar row before cancellation",
            "even_block": "0 if codimension-two coefficients agree; scalar gate is not a non-scalar row before cancellation",
            "full_equivariant": "0 rowwise, since every full-equivariant cyclic marker trace is 0",
        },
        "minimal_full_equivariant_order_2": {
            "hypotheses": [
                "no genuine |Gamma|_hbar=2 seed graph is added",
                "no order-2 CE source face is added",
                "C_{1,M}=0 from the minimal order-1 array",
                "the order-1 scalar-contact row has zero local-functional value in the full-equivariant branch",
                "every order-2 bracket row containing alpha_sc is zero",
            ],
            "reduced_non_scalar_row_sum": "0",
            "counterterm": "C_{2,M}=0",
        },
        "missing_order_2_row_types_for_larger_packages": missing_order_two_row_types(),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
