# Local Costello BV/Kernel/QME Source Anchors

Date: 2026-04-30

Scope: source support for the local
\(\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}\)
mixed holomorphic-topological manuscript after the compact-Calabi--Yau
firewall correction.

This fixture is a support boundary, not a theorem. It records exactly
which local Costello, Costello--Gwilliam, and manuscript-local anchors
support the vocabulary used for finite-scale BV/QME, heat-kernel
renormalization, local functionals, graph/counterterm asymptotics,
factorization-current language, and kernel obstruction bookkeeping.

## Verdict

Stable core:

- Costello's local arXiv mirror supports the universal finite-scale
  elliptic BV/RG/QME package: heat-kernel propagators, regularized BV
  Laplacians, local functionals, renormalized effective actions,
  counterterms, graph asymptotics, and local obstruction calculus.
- Costello--Gwilliam local Cambridge mirrors support only metadata,
  book-level vocabulary, and table-of-contents anchors for
  factorization algebras, quantum observables, Noether currents, and
  anomalies. They do not supply theorem-level support for the
  manuscript's reduced factorization-current map.
- The factorization-current object itself is manuscript-local:
  `appendix-factorization-current-conventions.tex` constructs the
  interval-current source, Matlis principal-part current target,
  coefficient-current kernel layer, wavefront-admissible relation, and
  non-scalar obstruction maps.
- `appendix-unreduced-bv-qme.tex` supplies the local scalar QME
  geometry, scalar-contact cocycle, balanced supertrace cancellation
  habitat, and ordinary scalar obstruction criterion.

Non-support:

- No compact Calabi--Yau theorem is supported by this fixture.
- No quintic, Gopakumar--Vafa, OSV, CoHA, Abel--Jacobi, Igusa,
  Borcherds, or BKM claim is supported by this fixture.
- No automatic \(\mathcal D'_c\)-valued Costello target, no automatic
  \(\mathcal D'_c\) wavefront/counterterm theorem, and no automatic
  bulk-to-defect kernel is supported by the Costello mirrors.
- Costello--Li BCOV/open-closed BCOV mirrors are quarantine/exclusion
  checks only. They may show what a different flat BCOV/HCS theorem
  proves, and what ordinary \(\mathfrak{gl}_N\) anomaly must be
  handled; they do not prove the local
  \(\mathbb R^2\times\mathbb C^2\) Hamiltonian brane-defect theorem.

## Local Source Inventory

| Source | Local mirror | SHA-256 | Admissible use |
|---|---|---:|---|
| Costello, *Renormalisation and the Batalin-Vilkovisky formalism* | `references/primary-sources/costello-renormalisation-bv-0706.1533.pdf` | `03fc69467694162e7da40a7cf6df445cdbdb4ecd165e67158fb0dbc283e13cd1` | Primary line-anchored source for finite-scale BV/RG/QME graph calculus. |
| Costello, text extraction of the same arXiv mirror | `references/primary-sources/costello-renormalisation-bv-0706.1533.txt` | `8475eff6bd5e81f2e8edc9cc453ec150a74d66aa386414034d8f29055f2a1d0a` | Local line anchors below. |
| Costello--Gwilliam, *Factorization Algebras in Quantum Field Theory*, Vol. I | `references/primary-sources/costello-gwilliam-vol1-cambridge.html` | `725c140a1fbd3637e07bc71fc031e320a8a80345cda8d57437db802d649211ac` | Metadata and book-level vocabulary only. |
| Costello--Gwilliam, *Factorization Algebras in Quantum Field Theory*, Vol. II | `references/primary-sources/costello-gwilliam-vol2-cambridge.html` | `ea23fecd48f6eacfb93a92a0f1c8cfb6f7ed37456c628128322fe2a12109e818` | Metadata, table-of-contents, and book-level vocabulary only. |

Quarantined local mirrors read only for exclusion checks:

| Source | Local mirror | SHA-256 | Boundary |
|---|---|---:|---|
| Costello--Li, *Quantum BCOV theory on Calabi-Yau manifolds and the higher genus B-model* | `references/primary-sources/costello-li-quantum-bcov-1201.4501.pdf` | `adc585ae21185778883e438b053c3ce0a3c2ab845aa33fabddf5b5ce66c5280b` | External BCOV source; not local theorem support. |
| Costello--Li, text extraction of `1201.4501` | `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt` | `71161565f2efc19e5fb26fee952e5ed35e49809a57321f8bb6a5b2ce8ed305b8` | Only small-diagonal locality and obstruction-convention comparison when explicitly quarantined. |
| Costello--Li, *Quantization of open-closed BCOV theory, I* | `references/primary-sources/costello-li-open-closed-bcov-1505.06703.pdf` | `034ee34548724ef175c81b77baf665ba02b2668a9c250a92451f880c8e274a40` | External flat BCOV/HCS theorem; exclusion check only. |
| Costello--Li, text extraction of `1505.06703` | `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt` | `8560a4576b8a282a13355d40127d38f58d600ff1363d271ded8a56bfbbae9327` | Only the flat \(\mathbb C^d\), odd \(d\), \(\mathfrak{gl}(N|N)\) scope and ordinary \(\mathfrak{gl}_N\) anomaly warning. |

## Supported Costello Anchors

### C1. Finite-scale heat-kernel propagator

Supported. Costello defines
\[
  P(\epsilon,T)=\int_\epsilon^T (Q^{\mathrm{GF}}\otimes 1)K_t\,dt
\]
and records that \(P(0,\infty)\) is distributional because of the
\(t=0\) singularity:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:77-90`.
The heat kernel for a generalized Laplacian and the smoothing operator
\(L_t=(Q^{\mathrm{GF}}\otimes1)K_t\) are anchored at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1549-1558`.

Admissible manuscript use: the finite-scale heat-kernel vocabulary in
`main.tex:6666-6682` and the operator-versus-BV-kernel distinction in
`main.tex:6749-6805`.

### C2. Regularized BV Laplacian and renormalized QME

Supported. The regularized BV operators \(\Delta_t=-\partial K_t\) for
\(t>0\), and the ill-defined physical \(\Delta_0\), are anchored at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:407-423`
and
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2084-2118`.
RG transport preserves the scale-\(T\) QME:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2139-2161`.
The renormalized QME is defined by the scale-\(T\) effective action:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2162-2190`.

Admissible manuscript use: the QME/RG framework in
`main.tex:6666-6682`, not the local Hamiltonian specialization.

### C3. Local functionals, locality, counterterms, and RG flow

Supported in the general elliptic setting. Costello's local functionals
factor through polydifferential operators into densities:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1122-1151`.
The counterterm theorem constructs local counterterms and the
renormalized effective action:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1746-1807`.
The RG equation and locality condition for systems of effective actions
are anchored at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:1967-2001`.

Admissible manuscript use: "local counterterm", "local functional",
"renormalized effective action", and "RG compatibility" vocabulary in
the local analytic problem, especially `main.tex:6808-6970` and
`main.tex:7558-7597`.

### C4. Connected graph expansion and asymptotics

Supported. Costello records the finite graph expansion of
\(\Gamma_{i,k}(P(\epsilon,T),S)\):
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3610-3625`.
The general graph-integral theorem gives small-\(\epsilon\) and small-\(T\)
asymptotics with local-functional coefficients:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3547-3568`
and
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:3660-3679`.

Admissible manuscript use: graph/counterterm vocabulary and finite graph
tests in `main.tex:7772-8018`, subject to the explicit hypothesis that a
Hamiltonian specialization has been supplied.

### C5. Local obstruction calculus

Supported. Costello constructs obstructions to solving the renormalized
QME:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2376-2420`.
The inductive lifting step says the obstruction is closed and must be
made exact:
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2469-2483`.
The simplicial obstruction map and lift criterion are anchored at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2554-2581`.
The local-to-global obstruction and cohomology-class criterion appear at
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2915-2938`
and
`references/primary-sources/costello-renormalisation-bv-0706.1533.txt:2975-3014`.

Admissible manuscript use: obstruction-complex grammar in
`main.tex:7389-7418` and `appendix-factorization-current-conventions.tex:1163-1241`.

## Costello--Gwilliam Vocabulary Boundary

Vol. I local Cambridge metadata verifies DOI, authorship, and book-level
factorization-algebra vocabulary:
`references/primary-sources/costello-gwilliam-vol1-cambridge.html:112-123`.
The book description says factorization algebras are local-to-global QFT
objects and identifies their local structure with associative and vertex
algebra examples:
`references/primary-sources/costello-gwilliam-vol1-cambridge.html:2838-2844`.

Vol. II local Cambridge metadata verifies DOI, authorship, and the
book-level vocabulary connecting interacting field theories with
operator product expansions, Noether currents, anomalies, and the BV
formalism:
`references/primary-sources/costello-gwilliam-vol2-cambridge.html:112-123`
and
`references/primary-sources/costello-gwilliam-vol2-cambridge.html:2825`.
The local table of contents anchors quantum observables and Noether
theorem chapters:
`references/primary-sources/costello-gwilliam-vol2-cambridge.html:4187-4201`,
`references/primary-sources/costello-gwilliam-vol2-cambridge.html:4475-4489`,
`references/primary-sources/costello-gwilliam-vol2-cambridge.html:4547-4563`,
and
`references/primary-sources/costello-gwilliam-vol2-cambridge.html:4619-4634`.

Boundary: these local Cambridge mirrors do not contain theorem statements
for the manuscript's reduced current map, \(\mathcal D'_c\)-valued
graph theorem, or central-operation comparison. The earlier ledger
`references/primary-sources/costello-cg-source-anchors-2026-04-28.md:20-24`
and `:46-63` remains binding: exact published theorem-number support is
not locally verified.

## Manuscript-Local Factorization-Current Anchors

These are local mathematical anchors, not external primary sources.

- `appendix-factorization-current-conventions.tex:4-34`: reduced
  factorization-current interface, local
  \(\mathbb R^2_{\mathrm{top}}\times\widehat{\mathbb C^2}_{0,\mathrm{hol}}\)
  geometry, and compact/global non-support.
- `appendix-factorization-current-conventions.tex:36-120`: interval
  Hamiltonian currents, distributional Matlis current dual, and current
  action by \(B\mapsto aB\).
- `appendix-factorization-current-conventions.tex:122-135`: local
  unimodular input \(\Omega_{\mathrm{loc}}=dz_1\wedge dz_2\).
- `appendix-factorization-current-conventions.tex:578-684`: local
  coefficient-current kernel layer, finite-window compatibility, and the
  residual \(\mathcal D'_c\) wavefront/counterterm theorem.
- `appendix-factorization-current-conventions.tex:943-1015`:
  wavefront-admissible defect-current labels.
- `appendix-factorization-current-conventions.tex:1163-1241`:
  obstruction maps necessary for a non-scalar current lift.
- `appendix-unreduced-bv-qme.tex:4-23`: formal-local BV/QME appendix
  firewall.
- `appendix-unreduced-bv-qme.tex:53-90`: local scalar shadow geometry.
- `appendix-unreduced-bv-qme.tex:365-430`: distributional locality of
  principal-part currents.
- `appendix-unreduced-bv-qme.tex:2142-2185`: ordinary scalar-reduced
  obstruction criterion.

## Manuscript Use Boundary

The source package supports these manuscript uses:

- `main.tex:6615-6630`: Costello supplies general BV/RG formalism under
  its hypotheses; Costello--Li does not identify this mixed Hamiltonian
  sector.
- `main.tex:6656-6682`: finite-scale perturbative BV construction
  vocabulary.
- `main.tex:6685-6705`: Costello--Li flat open-closed BCOV theorem is an
  exclusion check, not a local theorem input.
- `main.tex:6749-6805`: the linear heat operator is not yet a Costello
  BV kernel without a coefficient coevaluation kernel.
- `main.tex:6808-6970`: Hamiltonian specialization data remain theorem
  obligations.
- `main.tex:7228-7345`: the componentwise quantum coefficient surface
  proves only weighted coefficient/BV kernel convergence, balanced
  scalar-contact zero projection, reduced current target, and
  degree-zero Moyal comparison.
- `main.tex:7389-7418`: the non-scalar quantum \(P_0\)-operation is an
  obstruction complex, not a proved graph theorem.
- `main.tex:7558-7597`: counterterms, bulk-to-defect kernel, and reduced
  non-scalar class remain open.
- `main.tex:7772-8018`: first/third graph-normalization tests are
  conditional on a supplied Costello specialization.
- `main.tex:8044-8068`: compact-CY/CoHA/quintic/GV/OSV/Abel--Jacobi/
  Igusa/BKM material is external comparison only.

## Negative Source Checks

The following local searches were run over the Costello,
Costello--Gwilliam, and Costello--Li mirrors listed above.

```bash
rg -n -F "current-valued" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n -F "D'_c" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n -F "bulk-to-defect" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
rg -n -F "compactly supported distributions" references/primary-sources/costello-renormalisation-bv-0706.1533.txt references/primary-sources/costello-gwilliam-vol1-cambridge.html references/primary-sources/costello-gwilliam-vol2-cambridge.html references/primary-sources/costello-li-quantum-bcov-1201.4501.txt references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt
```

Results: no hits.

The wavefront scan has one relevant local hit, and it is not a
\(\mathcal D'_c\)-valued theorem:
`references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:619`
states the ordinary BCOV small-diagonal wavefront condition.

The compact-frontier keyword scan returned only BCOV/Vafa bibliographic
or external-BCOV references inside the quarantined Costello--Li mirrors
and one Vafa--Witten reference in Costello--Gwilliam Vol. II metadata.
It returned no local support for CoHA, Igusa, BKM, OSV, quintic,
Gopakumar--Vafa, or Abel--Jacobi claims.

## Inscription Rule

Use this fixture to support only:

1. finite-scale elliptic BV/RG/QME vocabulary;
2. heat-kernel propagators and regularized BV Laplacians;
3. local functionals, counterterms, graph asymptotics, and obstruction
   calculus in Costello's general setting;
4. factorization-algebra, quantum-observable, Noether-current, and
   anomaly vocabulary at the metadata/section level;
5. the manuscript-local factorization-current and scalar-QME
   constructions listed above.

Do not use this fixture to assert a compact Calabi--Yau theorem, compact
BCOV theorem, quintic/GV/OSV arithmetic statement, CoHA/centre theorem,
Abel--Jacobi normal function statement, Igusa/Borcherds/BKM statement,
or the full non-scalar Hamiltonian Costello graph/QME theorem. The latter
starts only after the current-compatible wavefront/counterterm theorem,
bulk-to-defect kernel, scalar-projection lift, finite-window counterterms,
and residual \(H^1(\ker\widehat\sigma_{\mathrm{sc}},d_{\mathrm{QME}})\)
vanishing have been supplied.
