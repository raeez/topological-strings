# CoHA / Centre Source Anchors, 2026-04-30

Scope.  This fixture is the CoHA/centre source row for
`frontier_mnop_framing_volume.tex`.  It records only the source grammar
for Lurie centres, Joyce and Gross--Joyce--Tanaka Hall/vertex
structures, Joyce--Upmeier orientation data, Kinjo--Park--Safronov
3CY cohomological Hall algebras, and the Costello--Gwilliam
factorization-algebra vocabulary needed to delimit centre language.  It
does not construct the compact target datum
`C_tar=(F_X,M_DT,M_PT,M_GW,Tr_DT,Tr_PT,Tr_GW,sigma_X)` and it does not
define, kill, or null-homotope `Ob_UKD(C_tar)`.

Status.  The fixture is a source/gap ledger for the Hall/CoHA/centre
domain only.  Lurie, Joyce, Gross--Joyce--Tanaka, Joyce--Upmeier, and
Kinjo--Park--Safronov are recorded by stable primary identifiers until
local mirrors and line-level text anchors are imported.  The local
Costello--Gwilliam fixture is retained only for factorization-algebra
vocabulary; it does not verify an unrestricted centre theorem.

Provenance note.  This file fills the missing CoHA/centre source row.
The expected Agent 057 report
`reconstitution/swarm-2026-04-30-agent-057-coha-center-fixture.md`
remains absent from this checkout.

Controller lane.  `GlobDesc`.  The CoHA/centre package records a
source-obligation component for the compact target datum.  It is not a
vanishing obstruction and is not an input to the formal-local theorem in
`main.tex`.

First-principles admission criterion.  A CoHA would require a 3CY
category of brane objects, a derived moduli stack of objects,
extension/triangle correspondences defining Hall multiplication,
orientation data and vanishing-cycle cohomology, and then a comparison
from that Hall algebra to the relevant factorization centre.  The local
Hamiltonian BF/Moyal theorem supplies none of those objects: it supplies
the shifted cotangent Hamiltonian Lie algebra, CE/PV comparison,
principal-part current brackets, and weighted BV/Moyal coefficient
identities.  Therefore this fixture exists only to police compact-CY
frontier language.  It must not be cited as evidence for the local
theorem.

## Source Inventory

| Source key | Local mirror | Status |
|---|---|---|
| `lurie-higher-algebra` | none found under `references/primary-sources` | Stable identifier only: J. Lurie, *Higher Algebra*, official PDF `https://people.math.harvard.edu/~lurie/papers/HA.pdf`. Use for centre/centralizer and locally constant factorization-algebra grammar only. |
| `joyce-vertex-algebra` | none found under `references/primary-sources` | Stable identifier only: D. Joyce, "Vertex algebras and moduli stacks", arXiv `2111.04694`. |
| `gross-joyce-tanaka` | none found under `references/primary-sources` | Stable identifier only: J. Gross, D. Joyce, Y. Tanaka, "Universal structures in the homology of moduli spaces of coherent sheaves", arXiv `2005.05637`. |
| `joyce-upmeier-orientations` | none found under `references/primary-sources` | Stable identifier only: D. Joyce and M. Upmeier, "Orientation data for moduli spaces of coherent sheaves over Calabi-Yau 3-folds", arXiv `2001.00113`. |
| `kinjo-park-safronov-coha` | none found under `references/primary-sources` | Stable identifier only: T. Kinjo, H. Park, P. Safronov, "Cohomological Hall algebras for 3-Calabi-Yau categories", arXiv `2406.12838`. |
| `costello-gwilliam` | `references/primary-sources/costello-cg-source-anchors-2026-04-28.md` | Present as a section-level factorization-algebra vocabulary fixture. It does not verify an unrestricted centre theorem. |

## Captured Source Facts

| Fact ID | Source anchor | Captured fact | Local use permitted | Explicit non-support |
|---|---|---|---|---|
| `lurie-centre-grammar` | Lurie, *Higher Algebra*, centre/centralizer and factorization-algebra sections; stable official PDF above | Gives the abstract higher-categorical grammar in which associative and `E_n` central constructions are formulated, and the locally constant factorization-algebra comparison used elsewhere in this repository. | Vocabulary for writing `Z_{E_2}(A)` and for separating centre grammar from construction. | Does not construct `F_X=PhiFA_3(Perf(X))`, identify the centre of a compact CY3 factorization algebra, produce `sigma_Q`, or prove `Aut_{E_2}` rigidity. |
| `joyce-vertex-hall` | Joyce `arXiv:2111.04694`; Gross--Joyce--Tanaka `arXiv:2005.05637` | Supplies Joyce-style vertex/Hall structures attached to homology of moduli stacks of objects such as coherent sheaves. | Source vocabulary for the phrase "Joyce vertex algebra on the derived moduli stack" in `frontier_mnop_framing_volume.tex:151-159`. | Does not identify Joyce's vertex algebra with this note's `E_2` centre, does not build compact trace maps, and does not implement MNOP/PT--GW substitution. |
| `orientation-data` | Joyce--Upmeier `arXiv:2001.00113`; KPS `arXiv:2406.12838` | Orientation data are load-bearing inputs for Calabi-Yau 3-fold enumerative Hall structures and for KPS-style 3CY CoHA constructions. | Supports recording orientation data as a prerequisite rather than as a conclusion. | Does not prove the required orientation is supplied for the frontier target, does not check compatibility with trace normalisation, and does not supply `Ob_UKD` null-homotopies. |
| `kps-coha-3cy` | Kinjo--Park--Safronov `arXiv:2406.12838` | Stable source identifier for cohomological Hall algebras associated to 3-Calabi-Yau categories, with strong orientation hypotheses. | Vocabulary for a possible 3CY CoHA source lane. | Does not give a local proof that `Perf(X)` in this note maps to `F_X`, that the resulting CoHA is the `E_2` centre of `F_X`, or that the MNOP substitution is a centre automorphism. |
| `costello-gwilliam-factorization` | `references/primary-sources/costello-cg-source-anchors-2026-04-28.md` | Supplies local factorization-algebra vocabulary against which centre claims can be delimited. | Vocabulary only, especially for separating local factorization-algebra grammar from a compact `E_2`-centre theorem. | Does not verify an unrestricted centre theorem, compact CY3 factorization image, trace map, or Hall/CoHA identification. |

## Claim-To-Source Map

| Local anchor | Claim shape | Present support | Boundary |
|---|---|---|---|
| `frontier_mnop_framing_volume.tex:54-68` | The source-fixture status names the CoHA/centre row. | This fixture supplies only the Hall/CoHA/centre vocabulary row and its non-import firewall. | It no longer records the out-of-domain split rows listed below. |
| `frontier_mnop_framing_volume.tex:73-94` | `C_tar(X)` names `F_X`, DT/PT/GW modules, trace maps, and `sigma_X`. | Lurie/Joyce/GJT/Joyce--Upmeier/KPS provide only grammar/source vocabulary by stable identifier. | `F_X`, modules, traces, and `sigma_X` are unconstructed target data. |
| `frontier_mnop_framing_volume.tex:146-172` | `sigma_Q in Aut_{E_2}(Z_{E_2}(F_Q))`, uniqueness/rigidity, and the Joyce--KPS target schema. | Lurie supplies centre grammar; Joyce/GJT/KPS supply Hall/vertex/CoHA vocabulary and orientation prerequisites. | No source row proves existence, uniqueness, or rigidity of `sigma_Q`; the Joyce--KPS line remains a conditional target schema, not a theorem and not a Vol III transfer. |

## Explicit Gaps

- `F_X` / `cF_X`: no construction of
  `PhiFA_3(Perf(X))` or compact-CY factorization image is present.
- Trace maps: no construction of
  `Tr_DT`, `Tr_PT`, or `Tr_GW` from compact modules to scalar partition
  functions is present.
- `sigma_Q` / `sigma_X`: no chain-level `E_2`-centre automorphism
  implementing `-q=e^{iu}` is constructed.
- `E_2` rigidity: no uniqueness theorem for
  `Aut_{E_2}(Z_{E_2}(F_Q))` is sourced or proved.
- Orientation compatibility: no source row verifies that the Joyce--
  Upmeier or KPS orientation data required by the frontier target have
  been chosen or matched to the trace normalisations.
- `Ob_UKD(C_tar)`: no null-homotopy or vanishing proof is supplied.
- Lurie, Joyce, Gross--Joyce--Tanaka, Joyce--Upmeier, and KPS local
  mirrors remain to be imported before line-level primary-source
  citation closure.

## Domain Boundary

Out-of-domain compact-CY source rows are not listed here.  They are
routed by
`references/primary-sources/compact-cy-source-fixture-control-surface-2026-04-30.md`.
This file may be used only for Hall/CoHA/centre vocabulary and for the
firewall saying that compact target data remain unconstructed.

## Firewall Status

Supported now: source vocabulary for the CoHA/centre lane, stable
identifiers for Lurie/Joyce/GJT/Joyce--Upmeier/KPS, and
Costello--Gwilliam factorization vocabulary.

Not supported now: compact `F_X`, trace maps, `sigma_Q`, `sigma_X`,
`E_2` rigidity, orientation compatibility for the frontier target, a
CoHA-to-centre identification, a centre automorphism implementing MNOP,
or `Ob_UKD(C_tar)=0`.

Therefore the CoHA/centre package remains target data, not proof input
for `main.tex`.
