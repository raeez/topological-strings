# MNOP/PT/DT Source Anchors, 2026-04-30

Scope.  This fixture records primary-source anchors for the scalar
MNOP/PT/DT facts named in `frontier_mnop_framing_volume.tex`.  It covers
Donaldson-Thomas construction, stable pairs, degree-zero DT/MacMahon
normalization, the reduced DT/PT relation, the MNOP DT/GW correspondence
statement, and the minimal GW virtual-class background needed for the
notation.  It does not cover HKQ quintic tables, CDGP periods, GV/OSV
physics, conifold resurgence, Joyce/Kinjo-Park-Safronov CoHA structure,
or Lurie center grammar except as explicit remaining gaps.

Status.  These sources supply external scalar enumerative facts and
standard virtual-class/Hall-wall-crossing frameworks.  They do not prove
the local Hamiltonian BF/Moyal theorem, construct a compact-CY
factorization algebra, build DT/PT/GW modules over such an object, define
trace maps to scalar partition functions, construct the automorphism
`\sigma_Q`, or kill `Ob_UKD(C_tar)`.

Local mirrors.  A targeted repository scan found no local MNOP/PT/DT
source PDFs or text mirrors under `references/primary-sources/`.  The
anchors below therefore use stable primary identifiers.  Durable local
copies still need to be imported before a line-level citation audit can be
closed.

Controller lane.  `GlobDesc`.  Missing or insufficient MNOP/PT/DT source
rows are an `ob_Src,MNOP` component of the compact target datum, not a
vanishing obstruction.

First local coordinate check.  For a smooth quintic
`Q subset P^4`,
`c(TQ)=(1+H)^5/(1+5H)`, hence
`c_3(TQ)=(-125+125-50+10)H^3=-40H^3`; since
`int_Q H^3=5`, `chi(Q)=int_Q c_3(TQ)=-200`.  Thus the local convention in
`frontier_mnop_framing_volume.tex:108--128` reads
`Z_DT(Q;q,v)=M(-q)^(-200) Z_PT(Q;q,v)` after combining the reduced DT/PT
identity with the degree-zero DT factor.

## Primary Source Rows

### `thomas-holomorphic-casson`

Primary anchor.  R. P. Thomas, "A holomorphic Casson invariant for
Calabi-Yau 3-folds, and bundles on K3 fibrations", arXiv
`math/9806111`.

Exact source place.  Abstract; Section 3 introduction; Theorem 3.30;
Corollary 3.39; Definition 3.54.

Source facts captured.

- The paper develops sheaf deformation theory sufficient to obtain
  virtual moduli cycles for moduli spaces of stable sheaves when the
  higher obstruction groups vanish.
- Theorem 3.30 gives perfect tangent-obstruction complexes for stable
  sheaf moduli under the stated Ext-constancy hypotheses.
- Corollary 3.39 gives virtual cycles for stable-sheaf moduli on smooth
  projective threefolds with trivial or anti-effective canonical bundle.
- For Calabi-Yau threefolds the trace-free virtual cycle has dimension
  zero; Definition 3.54 defines the holomorphic Casson invariant as the
  length of that virtual cycle.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:98--100`: source for the
  Donaldson-Thomas/ideal-sheaf scalar virtual-count package named there.
- `frontier_mnop_framing_volume.tex:96--100`: source fixture for the DT
  scalar theory only.  Thomas does not support the word "module" or
  "dualisable" in the target datum at
  `frontier_mnop_framing_volume.tex:73--86`.

Explicit non-support.

- Does not prove DT/PT equality, the MNOP DT/GW correspondence, PT stable
  pairs, the degree-zero MacMahon formula, any `E_2` center statement, or
  any compact-CY transfer into `main.tex`.

### `behrend-fantechi-intrinsic-normal-cone`

Primary anchor.  K. Behrend and B. Fantechi, "The intrinsic normal cone",
arXiv `alg-geom/9601010`; published in *Inventiones Mathematicae* 128
(1997).

Exact source place.  Introduction; Sections 4--5, especially Definition
5.1 and the construction of the virtual fundamental class in Section 5.

Source facts captured.

- The paper defines intrinsic normal cones for Deligne-Mumford stacks,
  perfect obstruction theories, and virtual fundamental classes of the
  expected dimension.
- The introduction explicitly names Gromov-Witten moduli of stable maps
  as a main example of the construction.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:103--105`: background for the
  virtual-class grammar behind the displayed `Z_GW` notation, but not by
  itself a complete GW partition-function source.
- `frontier_mnop_framing_volume.tex:96--105`: source for scalar
  virtual-cycle language only, not for `M_GW` as a dualisable module in
  `frontier_mnop_framing_volume.tex:73--86`.

Explicit non-support.

- Does not prove MNOP, DT/PT, PT/GW, stable-pair theory, Hall
  integration, or any chain-level compact factorization package.

### `li-tian-virtual-cycle`

Primary anchor.  J. Li and G. Tian, "Virtual moduli cycles and
Gromov-Witten invariants of algebraic varieties", arXiv
`alg-geom/9602007`; published in *Journal of the AMS* 11 (1998).

Exact source place.  Introduction theorem after the virtual normal cone
construction; Section 4, "Gromov-Witten Invariants of smooth varieties".

Source facts captured.

- The introduction states that for any smooth projective variety and
  choices of genus, markings, and curve class, there is a virtual moduli
  cycle for the stable-map moduli space and GW invariants are defined by
  integration against it.
- Section 4 applies the virtual moduli cycle construction to stable maps.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:103--105`: stable-map virtual-cycle
  source for the GW partition-function notation.
- `frontier_mnop_framing_volume.tex:103--105` and
  `frontier_mnop_framing_volume.tex:115--119`: source background for the
  GW side of the MNOP/PT-GW target, not for the equality itself.

Explicit non-support.

- Does not prove the MNOP DT/GW correspondence, the PT/GW substitution,
  DT/PT equality, or any compact-CY chain lift.

### `behrend-microlocal-dt`

Primary anchor.  K. Behrend, "Donaldson-Thomas type invariants via
microlocal geometry", arXiv `math/0507523`.

Exact source place.  Introduction; Section 1.3; Theorem 4.18.

Source facts captured.

- Behrend constructs the canonical constructible function `nu_X` and
  weighted Euler characteristic `chi(X,nu_X)`.
- Theorem 4.18 states that, for proper spaces in the stated classes with
  symmetric obstruction theory, the virtual count equals the
  `nu_X`-weighted Euler characteristic.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:122--133`: source for the
  Behrend-weighted scalar integration language used after Hall
  wall-crossing.
- `frontier_mnop_framing_volume.tex:96--100`: source for the weighted
  virtual-count convention underlying DT/PT scalar invariants.

Explicit non-support.

- Does not compute the degree-zero Hilbert-scheme factor, prove DT/PT,
  prove MNOP, or define a compact factorization trace map.

### `behrend-fantechi-hilb-points-threefolds`

Primary anchor.  K. Behrend and B. Fantechi, "Symmetric obstruction
theories and Hilbert schemes of points on threefolds", arXiv
`math/0512556`.

Exact source place.  Theorem 4.11 and Theorem 4.12.

Source facts captured.

- Theorem 4.11: for a smooth threefold `Y`, the weighted Euler
  characteristic of `Hilb^n Y` is `(-1)^n chi(Hilb^n Y)`, and the
  generating series is `M(-t)^{chi(Y)}`.
- Theorem 4.12: if `Y` is a projective Calabi-Yau threefold, the
  Donaldson-Thomas virtual counts of `Hilb^n Y` satisfy
  `sum_n #vir(Hilb^n Y)t^n = M(-t)^{chi(Y)}`.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:108--114`: supplies the
  degree-zero DT/MacMahon factor in the displayed quintic formula.
- `frontier_mnop_framing_volume.tex:122--133`: supplies only the scalar
  degree-zero Hilbert-scheme contribution claimed in the proof sketch.
- `frontier_mnop_framing_volume.tex:759--769`: supplies only the
  MacMahon-factor part of the scalar status summary.

Explicit non-support.

- Does not prove reduced DT/PT equality, GW/PT substitution, MNOP DT/GW,
  or any factorization-algebra refinement.

### `mnop-gw-dt-I`

Primary anchor.  D. Maulik, N. Nekrasov, A. Okounkov, and
R. Pandharipande, "Gromov-Witten theory and Donaldson-Thomas theory, I",
arXiv `math/0312059`; published in *Compositio Mathematica* 142 (2006).

Exact source place.  Sections 1.1--1.4; Conjectures 1--3 in Section 1.4.

Source facts captured.

- Section 1.3 defines the reduced Gromov-Witten potential and partition
  function `Z'_GW(X;u,v)` after removing constant maps.
- Section 1.4 defines DT invariants by integration over ideal-sheaf
  moduli, the DT partition function, the degree-zero partition function,
  and the reduced DT partition function.
- Conjecture 1 states the degree-zero DT formula
  `Z_DT(X;q)_0=M(-q)^{chi(X)}`.
- Conjecture 2 states rationality and `q <-> q^{-1}` symmetry for the
  reduced DT series.
- Conjecture 3 states the GW/DT correspondence under
  `e^{iu}=-q`, i.e. `Z'_GW(X;u,v)=Z'_DT(X;-e^{iu},v)`.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:88--89` and
  `frontier_mnop_framing_volume.tex:115--119`: source for the MNOP
  DT/GW substitution as a conjectural target, not as a local theorem.
- `frontier_mnop_framing_volume.tex:96--105`: source for the displayed
  GW/DT partition-function notation.
- `frontier_mnop_framing_volume.tex:146--156`: source for why
  `-q=e^{iu}` is a named MNOP/PT-GW target datum.

Explicit non-support.

- In this primary source the compact Calabi-Yau GW/DT equality is a
  conjecture, not a theorem available for import into `main.tex`.
- It does not prove DT/PT equality, construct PT stable pairs, build
  `F_X`, define trace maps, construct `\sigma_Q`, or remove `Ob_UKD`.

### `mnop-gw-dt-II`

Primary anchor.  D. Maulik, N. Nekrasov, A. Okounkov, and
R. Pandharipande, "Gromov-Witten theory and Donaldson-Thomas theory, II",
arXiv `math/0406092`; published in *Compositio Mathematica* 142 (2006).

Exact source place.  Section 2, Conjectures 1--3 and the primary-field
correspondence; Section 4, Theorems 1--3 for degree-zero toric
localization.

Source facts captured.

- Section 2 formulates the GW/DT correspondence for general smooth
  projective threefolds with primary and descendent insertions, again
  using `e^{iu}=-q`.
- Theorems 1--3 prove degree-zero localization formulas in the toric
  setting, including the MacMahon factor in that context.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:88--89` and
  `frontier_mnop_framing_volume.tex:115--119`: supports the statement
  that the MNOP substitution is an external correspondence package.
- `frontier_mnop_framing_volume.tex:73--105`: supports the assertion
  that descendent/observable data are extra source data, not automatic
  consequences of scalar series.

Explicit non-support.

- Does not prove the all-genus compact quintic PT/GW theorem, DT/PT
  equality, or the repository's chain-level `E_2` center package.

### `pandharipande-thomas-stable-pairs`

Primary anchor.  R. Pandharipande and R. P. Thomas, "Curve counting via
stable pairs in the derived category", arXiv `0707.2348`.

Exact source place.  Section 1.1 and Lemma 1.3 for the stable-pair
definition; Theorem 2.14 for the virtual class; Definition 2.16 for PT
invariants; Section 3.2, especially Conjectures 3.2--3.3.

Source facts captured.

- In the large stability limit, a stable pair is a morphism
  `O_X -> F` with `F` pure one-dimensional and zero-dimensional cokernel.
- The moduli spaces `P_n(X,beta)` carry a virtual class; for Calabi-Yau
  threefolds the PT invariants `P_{n,beta}` are the degrees of the
  zero-dimensional virtual cycles.
- The stable-pair partition function is
  `Z_{P,beta}(q)=sum_n P_{n,beta} q^n`.
- Conjecture 3.3 states the conjectural equality of stable-pair, reduced
  DT, and GW partition functions after `-q=e^{iu}`.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:101--102`: direct source for the PT
  stable-pair theory and partition-function notation.
- `frontier_mnop_framing_volume.tex:115--119` and
  `frontier_mnop_framing_volume.tex:138--142`: source for the PT/GW
  substitution as a conjectural target datum.
- `frontier_mnop_framing_volume.tex:146--158`: supports only the
  necessity of separate DT/PT/GW objects before any chain-level package.

Explicit non-support.

- Does not prove DT/PT equality; it states the equality as Conjecture
  3.3.  It does not construct `F_X`, trace maps, `\sigma_Q`, or
  `E_2`-rigidity.

### `bridgeland-hall-curve-counting`

Primary anchor.  T. Bridgeland, "Hall algebras and curve-counting
invariants", arXiv `1002.4374`; published in *Journal of the AMS* 24
(2011).

Exact source place.  Introduction and Theorem 1.1; Section 5.1 for the
Hall algebra/integration map; Section 6.4 for the DT/PT correspondence.

Source facts captured.

- The standing setup is a smooth projective Calabi-Yau threefold, with
  `H^1(M,O_M)=0` included in the introduction; the quintic satisfies this
  hypothesis.
- Theorem 1.1 states that for every curve class `beta`, the reduced DT
  series equals the PT series, `DT'_beta(q)=PT_beta(q)`, and that the
  reduced DT series is a Laurent expansion of a rational function
  invariant under `q <-> q^{-1}`.
- Section 6.4 proves the DT/PT part by a Hall-algebra identity and then
  applies the integration map to obtain the scalar generating-series
  identity.
- The introduction records the degree-zero DT factor as
  `DT_0(q)=M(-q)^{chi(M)}` and defines `DT'_beta=DT_beta/DT_0`.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:108--114`: main source for the
  reduced scalar DT/PT equality used in the quintic theorem.
- `frontier_mnop_framing_volume.tex:122--133`: source for the
  Hall-integration proof sketch, together with the separate
  degree-zero row above.
- `frontier_mnop_framing_volume.tex:759--769` and
  `frontier_mnop_framing_volume.tex:809--811`: supports only the scalar
  Hall-integrated DT/PT theorem-grade part of the summary.

Explicit non-support.

- Does not prove the GW/PT leg, compact BCOV, `F_X`, an
  `E_2`-center recognition theorem, `\sigma_Q`, or any global descent
  theorem in this repository.

### `toda-dt-pt-correspondence`

Primary anchor.  Y. Toda, "Curve counting theories via stable objects I.
DT/PT correspondence", arXiv `0902.4371`; published in *Journal of the
AMS* 23 (2010).

Exact source place.  Introduction; Theorem 3.14; Appendix Theorem 8.12
and Remark 8.13.

Source facts captured.

- The main body proves the Euler-characteristic version of DT/PT
  correspondence by weak stability conditions and wall-crossing.
- Theorem 3.14 states the equality of generating series
  `DT'(X)=PT(X)` for Euler characteristics.
- Appendix Theorem 8.12 proves the Behrend-weighted Conjecture 1.1 in
  the appendix framework, and Remark 8.13 records the degree-zero
  MacMahon factor `DT_0(X)=M(-x)^{chi(X)}`.

Local claim anchors supported.

- `frontier_mnop_framing_volume.tex:130--131`: auxiliary source for the
  wall-crossing route named in the proof sketch.
- `frontier_mnop_framing_volume.tex:108--128`: corroborating DT/PT
  source when paired with Bridgeland and the Behrend-weighted
  degree-zero rows.

Explicit non-support.

- The Euler-characteristic theorem alone is not the Behrend-weighted
  scalar DT/PT theorem.  This fixture treats Bridgeland as the primary
  theorem anchor for the scalar DT/PT equality used locally, with Toda as
  an independent wall-crossing source and auxiliary weighted appendix
  reference.
- Does not prove MNOP DT/GW, PT/GW, `E_2` center recognition, or
  compact-CY transfer.

## Local Claim-To-Source Map

| Local anchor | Claim shape | Source support | Boundary |
|---|---|---|---|
| `frontier_mnop_framing_volume.tex:54--68` | Source-fixture status names the scalar fixtures and the reconstructed CoHA/centre fixture while recording no compact-target `F_X`, trace maps, `sigma_Q`, `E_2` rigidity, `N_AJ`, or `Ob_UKD` null-homotopy as imported. | No positive support in this scalar fixture. | Requires a separate construction of the compact-CY factorization image and a Lurie/Joyce/KPS fixture; scalar MNOP/PT/DT sources do not construct `F_X`. |
| `frontier_mnop_framing_volume.tex:73--86` | Three dualisable `F_X`-modules `M_DT`, `M_PT`, `M_GW` are target data, not constructed source facts. | Thomas, PT, Li-Tian, Behrend-Fantechi, and MNOP source scalar moduli and partition functions only. | "Module", "dualisable", and "canonical over `F_X`" remain unproved local target data. |
| `frontier_mnop_framing_volume.tex:108--119` | Quintic scalar `Z_DT=M(-q)^{chi} Z_PT`, plus PT/GW conditional finite-genus claim. | Bridgeland Theorem 1.1 gives `DT'_beta=PT_beta`; Behrend-Fantechi Hilb points gives `DT_0=M(-q)^{chi}`; local Chern-class check gives `chi(Q)=-200`. | The scalar DT/PT part is supported. KKV/HKQ/PT-GW finite-genus claims are not covered by this fixture. |
| `frontier_mnop_framing_volume.tex:122--136` | Proof sketch: Bridgeland/Toda wall-crossing, MacMahon as degree-zero Hilbert-scheme factor, and no fixture lift to `F_Q`. | Bridgeland Sections 5.1 and 6.4; Toda Theorem 3.14 and Appendix 8.12 as auxiliary; Behrend Theorem 4.18; Behrend-Fantechi Theorems 4.11--4.12; PT Theorem 2.14. | The fixture supports only scalar Hall integration and degree-zero Hilbert schemes. It does not source a KS lift to `F_Q` or any factorization-algebra identity. |
| `frontier_mnop_framing_volume.tex:115--142` | PT/GW/MNOP identity, KKV equivalence, HKQ genus-22 evidence. | MNOP I Conjecture 3, MNOP II Conjecture 3, and PT Conjecture 3.3 source the substitution as a conjectural correspondence target. | KKV/HKQ are outside this fixture. The PT/GW leg is not made theorem-grade here. |
| `frontier_mnop_framing_volume.tex:146--158` | Guarded `E_2` center package and `sigma_Q`. | No direct support in this fixture except the negative fact that scalar enumerative sources do not supply the chain-level package. | Requires construction of `F_X`, modules, trace maps, `\sigma_Q`, and rigidity. |
| `frontier_mnop_framing_volume.tex:161--172` | Joyce/KPS remark and Vol III pointer. | No positive support in this fixture. | Requires a separate CoHA/center fixture and cross-repo convention audit. |
| `frontier_mnop_framing_volume.tex:759--769` | Honest-status summary: DT/PT theorem-grade; PT/GW KKV-conditional; `E_2` automorphism target data. | Scalar DT/PT part supported by Bridgeland plus Behrend-Fantechi Hilb points. PT/GW target sourced as conjectural MNOP/PT source fact only. | Summary must not be imported into `main.tex` as compact-CY transfer. |
| `frontier_mnop_framing_volume.tex:809--823` | Theorem-grade list and frontier evidence. | This fixture supports only the scalar DT/PT item. | The firewall remains active: no compact CY, global BCOV, MNOP/chiral-volume, Vol III, Igusa/BKM, or sister-volume consequence follows without `C_tar` and `Ob_UKD` null-homotopies. |

## Explicit Gaps

- Local MNOP/PT/DT PDFs and text mirrors are absent; import remains a
  durable provenance obligation.
- No standalone bibliography or `amsrefs` keys were added in this lane.
- KKV, HKQ, CDGP, GV, OSV, conifold, Joyce, Kinjo-Park-Safronov, and
  Lurie center sources are outside this fixture.
- The scalar DT/PT theorem requires the reduced/unreduced convention to
  stay explicit: `Z_DT = Z_DT,0 Z'_DT`, `Z_DT,0=M(-q)^{chi(X)}`, and
  `Z'_DT=Z_PT`.
- The PT/GW or GW/DT substitution remains an external conjectural target
  in the sources listed here, not a local theorem.
- No source row constructs compact support functoriality, factorization
  centrality homotopies, BV/QME compatibility, physical large-`N` states,
  or global descent.
