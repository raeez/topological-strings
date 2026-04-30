# Costello Finite-Scale BV/QME Graph Source Fixture

Date: 2026-04-30

Scope: source support for the non-scalar Costello graph/QME realization
problem. This fixture records what the local Costello mirrors support and
what they do not support for the Hamiltonian brane-defect theorem surface.

## Verdict

Costello's local mirror supports the general finite-scale elliptic BV
graph calculus: heat-kernel propagator, regularized BV Laplacian,
renormalized effective actions, RG flow, locality/counterterms, graph
integral asymptotics, and a local obstruction calculus. Costello--Li
supports the BCOV/open-closed use of the same package and the convention
that first-order quantization obstructions live in \(H^1\) of the
local-functional obstruction complex.

None of these sources supplies the extra Hamiltonian brane-defect data:
no automatic current-valued target, no automatic \(\mathcal D'_c\)
wavefront/counterterm theorem, and no automatic bulk-to-defect kernel.
Those are manuscript proof obligations.

## Local Mirrors And Stable Identifiers

| Source | Local mirror | Stable identifier | Supported use |
|---|---|---|---|
| Costello, *Renormalisation and the Batalin-Vilkovisky formalism* | `references/primary-sources/costello-renormalisation-bv-0706.1533.txt`; PDF sibling | arXiv `0706.1533`; published book record in `main.tex:8087-8098` gives AMS MSM 170, DOI `10.1090/surv/170` | Primary line-anchored source for finite-scale BV/RG/QME graph calculus. |
| Costello--Li, *Quantum BCOV theory on Calabi-Yau manifolds and the higher genus B-model* | `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt`; PDF sibling | arXiv `1201.4501` | BCOV quantization axioms and \(H^1\) obstruction convention. |
| Costello--Li, *Quantization of open-closed BCOV theory, I* | `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt`; PDF sibling | arXiv `1505.06703` | Open-closed BCOV scale-\(L\) QME, RG/QME compatibility, and supergroup scope. |
| Costello--Gwilliam, *Factorization Algebras in Quantum Field Theory*, Vols. I--II | `references/primary-sources/costello-gwilliam-vol1-cambridge.html`; `references/primary-sources/costello-gwilliam-vol2-cambridge.html`; earlier source ledger | DOIs `10.1017/9781316678626`, `10.1017/9781316678664` | Metadata/section-level vocabulary only in this checkout; not theorem-level proof support for this fixture. |

Import caution: `references/primary-sources/costello-cg-source-anchors-2026-04-28.md:20-24`
already records that exact AMS book theorem numbers remain unverified.
Until a published-book page mirror is imported, cite the local arXiv
mirror line anchors rather than unverified book theorem numbers.

## Supported Facts

### C1. Finite-scale heat-kernel propagator

Supported. Costello defines
\[
P(\epsilon,T)=\int_\epsilon^T(Q^{\mathrm{GF}}\otimes 1)K_t\,dt
\]
with \(K_t\) the heat kernel of \(H=[Q,Q^{\mathrm{GF}}]\), and distinguishes
the finite-scale smooth kernel from the singular \(P(0,\infty)\):
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90`.
Heat kernels for generalized Laplacians are recorded at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1549-1557`.

Manuscript consequence: `main.tex:6641-6658` may use this as the general
Costello BV package. The Hamiltonian sector still needs the additional
coefficient-kernel datum isolated in `main.tex:6724-6781`.

### C2. Regularized BV Laplacian

Supported. Costello defines regularized BV operators \(\Delta_t=-\partial
K_t\) for \(t>0\), while the physical \(\Delta_0\) is ill-defined in the
infinite-dimensional theory:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:407-423`.
The finite-dimensional odd Laplacian and bracket formula are recalled at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2088-2118`.

Manuscript consequence: the non-scalar theorem may demand a finite-scale
BV Laplacian, but it may not assert that the Hamiltonian
\(\mathcal D'_c\)-valued current target already has one.

### C3. QME/RG compatibility

Supported. Costello proves that \(QP(\epsilon,T)=-K_T+K_\epsilon\) and
that RG flow from \(T_1\) to \(T_2\) carries the scale-\(T_1\) QME to the
scale-\(T_2\) QME:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2121-2161`.
The renormalized QME is then defined by the scale-\(T\) equation for
\(\Gamma^R(P(0,T),S)\), independent of \(T\):
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2162-2190`.

Costello--Li use the same BCOV axioms: RG flow, QME, locality, and
classical limit in
`references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:890-927`.
For open-closed BCOV, the scale-\(L\) QME and RG/QME compatibility are
anchored at
`references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:1895-1950`.

### C4. Locality and counterterms

Supported in the general elliptic BV setting. Costello defines local
functionals by polydifferential factorization through densities:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1124-1149`.
The counterterm theorem constructs local counterterms and a renormalized
effective action:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1746-1807`.
The resulting systems of effective actions satisfy the RG equation and a
locality condition, and Theorem C gives the converse:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1967-2001`.

Graphwise locality is supported by the appendix: Costello writes the
connected graph expansion for \(\Gamma_{i,k}\) and proves asymptotic
expansions whose \(T\)-coefficients are local functionals:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3544-3569`,
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3610-3625`,
and
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3660-3685`.

### C5. Local obstruction complex and \(H^1\)

Supported with a two-source bridge. Costello constructs local obstructions
to solving the renormalized QME:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2376-2420`.
The inductive step says that a partial solution lifts exactly when the
closed obstruction is made exact:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2469-2483`.
The simplicial obstruction map and lift criterion are anchored at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2554-2581`.
The local-to-global obstruction appears as a closed element in local
functionals:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2915-2938`,
with the cohomology-class criterion at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2975-3014`.

Costello--Li make the grading convention explicit: the
obstruction-deformation complex is \(O_{\mathrm{loc}}(\mathcal E)\) with
differential \(Q+\{I,-\}\), \(H^0\) describes deformations, and \(H^1\)
contains obstructions:
`references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:2493-2505`.
The open-closed BCOV obstruction lifting proposition is anchored at
`references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:2338-2345`
and
`references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:2394-2412`.

Manuscript consequence: the residual non-scalar class in
\[
H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})
\]
at `main.tex:7407-7426` has the right Costello--Li obstruction-theory
shape. Its vanishing is not supplied by the sources.

### C6. Open-closed BCOV precedent and its scope

Supported only in its stated scope. Costello--Li's abstract states a
unique quantization of open-closed BCOV/HCS on flat \(\mathbb C^d\), \(d\)
odd, with gauge supergroup \(GL(N|N)\):
`references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:8-15`.
The introduction emphasizes \(gl(N|N)\)-compatibility:
`references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:75-87`.
It also warns that ordinary \(gl(N)\) has a one-loop anomaly term related
to \(\operatorname{Tr}(1)\), while \(gl(N|N)\) kills it:
`references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt:803-809`.

Manuscript consequence: `main.tex:6660-6670` is correctly scoped when it
says ordinary \(\mathfrak{gl}_N\) and the mixed
\(\mathbb R^2\times\mathbb C^2\) Hamiltonian brane model are not covered
without an additional reduction or summand argument.

## Exact Non-Support

### N1. No automatic current-valued target

Not supported. Costello's local functionals are polydifferential
local functionals on the field bundle, not a theorem producing the
principal-part current target
\(\mathcal D'_c(I)\widehat\otimes\mathcal P\). Costello--Li define
locality for BCOV distributional Taylor coefficients supported on the
small diagonal with conormal wavefront:
`references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:611-626`.
That does not produce the interval-current target used in the manuscript.

RG verification:

```bash
rg -n -F "current-valued" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
```

Result: no hits.

### N2. No automatic \(\mathcal D'_c\) wavefront theorem

Not supported. The source mirrors contain no `D'_c` target and no theorem
saying Costello counterterms remain local after inserting compactly
supported distributional defect currents. The only local mirror hit for
`wave-front` is Costello--Li's ordinary BCOV small-diagonal locality
definition at
`references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:619`.

RG verification:

```bash
rg -n -F "D'_c" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n -F "compactly supported distributions" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n "wave.?front|wave front|wavefront" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
```

Results: `D'_c` no hits; `compactly supported distributions` no hits;
`wave.?front` one hit at Costello--Li `1201.4501.txt:619`, not for a
\(\mathcal D'_c\)-valued target.

### N3. No automatic bulk-to-defect kernel

Not supported. The local source mirrors do not contain a
`bulk-to-defect` construction. The manuscript therefore correctly records
the kernel as an explicit obligation:
`main.tex:6875-6890`,
`main.tex:7384-7426`, and
`theorem-lanes.tex:1551-1572`.

RG verification:

```bash
rg -n -F "bulk-to-defect" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n -F "bulk to defect" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
```

Result: no hits.

## Import Obligations

1. Import a published-book page/theorem-number mirror for Costello 2011
   before using exact AMS theorem numbers beyond the already verified
   arXiv line anchors.
2. Prove or import a current-compatible Costello local-functional theorem
   for \(\mathcal D'_c\)-valued defect coefficients, including wavefront,
   counterterm, finite-window, and RG compatibility; otherwise restrict
   the defect current \(B\) to regular compactly supported densities.
3. Construct the continuous bulk-to-defect kernel
   \(\kappa_{\hbar,w,I}\) in the Costello local-functional category.
4. Prove the filtered scalar projection lift and kill all
   \(o_{\sigma,w}^{(r)}(I)\) before forming
   \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\).
5. At each finite-window order, prove the inverse-limit \(H^1\)
   obstruction vanishes and the \(\varprojlim^1H^0\) primitive
   compatibility class vanishes.

## Inscription Rule

Use this fixture to support only the universal finite-scale Costello
BV/RG/QME graph calculus and the Costello--Li obstruction-complex
grammar. Do not use it to assert the non-scalar Hamiltonian graph/QME
theorem. That theorem starts after the current-valued target,
\(\mathcal D'_c\) wavefront/counterterm theorem, scalar-projection lift,
finite-window counterterms, and bulk-to-defect kernel have been supplied.
