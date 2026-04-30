# Loday--Quillen--Tsygan Source Anchors

Date: 2026-04-30

Agent: 258

Scope: primary-source fixture for the stable matrix Lie algebra homology /
cyclic homology comparison used as an external template in the manuscript. No
PDF or text mirror is imported here.

## Stable Source Core

### LQ84

Source metadata:

- Jean-Louis Loday and Daniel Quillen, "Cyclic homology and the Lie algebra
  homology of matrices", `Commentarii Mathematici Helvetici` 59 (1984),
  565--591.
- DOI: `10.1007/BF02566367`.
- Publisher metadata checked: Springer page, published December 1984, volume
  59, pages 565--591, received 15 May 1984.
- Crossref metadata checked: same title, authors, volume 59, pages 565--591,
  print date December 1984, DOI `10.1007/bf02566367`.
- Open bibliographic/full-text routes checked: EuDML record
  `https://eudml.org/doc/139991`; GDZ full-text route from EuDML; E-Periodica
  volume record with article starting at p. 565. E-Periodica generated PDF
  exposes archival DOI `10.5169/seals-45410`.
- Local mirror: none. No checksum recorded because no local source copy was
  added.

Verified theorem anchors:

- Section 6, pp. 583--586: `Homology of Lie algebras of matrices`; standing
  hypotheses are a field `k` of characteristic zero and a unital associative
  `k`-algebra `A`.
- Lemma 6.1, p. 584: constructs the chain-level map from the cyclic quotient of
  Hochschild chains into the Chevalley--Eilenberg chain complex of
  `gl(A)`.
- Proposition 6.4, p. 585: coinvariants for a semisimple sub-Lie algebra give a
  quasi-isomorphic complex under the stated semisimplicity hypothesis.
- Proposition 6.6, pp. 585--586: the primitive part of the coinvariant CE
  complex is `C_{*-1}(A)`, the cyclic quotient complex shifted down by one.
- Theorem 6.2, p. 584, proved on p. 586: for `k` characteristic zero and
  unital associative `A`, the trace map restricts to an isomorphism
  `Prim H_n(gl(A)) = HC_{n-1}(A)`.
- Theorem 6.9, pp. 587--588: the stabilization map
  `H_i(gl_{n-1}(A)) -> H_i(gl_n(A))` is an isomorphism for `i < n-1` and an
  epimorphism for `i = n-1`; for commutative `A` it adds the displayed exact
  de Rham-form boundary term.
- Proposition 6.13, pp. 589--590: the rank filtration on `gl(A)` induces a
  first-quadrant spectral sequence converging to cyclic homology.

Hypotheses verified:

- Ground field of characteristic zero.
- `A` is an associative algebra with identity over `k`.
- `gl(A)` is the filtered colimit of the matrix Lie algebras `gl_r(A)` under
  standard inclusions.
- Homology is ordinary Lie algebra homology with trivial `k` coefficients,
  computed by the Chevalley--Eilenberg exterior complex.
- The invariant-theory argument uses classical matrix invariant theory and
  semisimplicity for the subalgebra `gl(k)`.

Supported manuscript claim:

- `main.tex:1764-1778`: the external template statement
  `Prim H_*^CE(gl_infty(A); C) = HC_{*-1}(A)` is source-supported by
  LQ84 Theorem 6.2 after base field specialization to `C`.
- `main.tex:1767-1772`: the connected Hopf-algebra form
  `H_*^CE(gl_infty(A); C) = S(HC_{*-1}(A))` is supported by combining LQ84
  Theorem 6.2 with the connected graded cocommutative Hopf algebra structure
  on Lie algebra homology in characteristic zero. LQ84 explicitly records the
  Hopf algebra structure and that the primitive part in this case is
  graded-commutative; the symmetric-algebra form is therefore a standard
  Hopf-algebra consequence rather than the literal wording of Theorem 6.2.
- `main.tex:1753-1757` is correctly phrased as a template for primitive
  large-`N` classes, not as a coordinate-ring invariant theorem.
- `theorem-lanes.tex:2079-2088` may cite LQ84 Theorem 6.9 only for the
  classical homological-degree stabilization pattern. Its manuscript
  finite-window `N >= W` comparison remains an internal construction target.

Degree shift:

- The source shift is homological: `Prim H_n(gl(A)) = HC_{n-1}(A)`.
- The manuscript formula `HC_{*-1}(A)` has the same homological convention.
- A dual cochain presentation would appear as a cyclic-cochain complex shifted
  by `[1]`; this is a dual convention check, not an additional primary theorem
  supplied by LQ84 for the manuscript's finite-window dg algebra.

Non-support boundary:

- LQ84 does not prove the manuscript's Dirac/Koszul trace theorem for
  `Q psi = [phi_1, phi_2]`.
- LQ84 does not prove the finite-window map
  `lambda_{LQT,W}: Prim C_*^CE(gl_N(A_{psi,W})) -> CC_red(A_{psi,W})[1]`
  with `N >= W`, connected single-trace projection, scalar quotient
  compatibility, or `A_infinity` transfer.
- LQ84 does not prove the Procesi--Razmyslov stable coordinate-ring invariant
  theorem, the Hamiltonian brane-defect trace theorem, the `Psi/rho` bridge,
  Costello graph/QME realization, or any BV pairing/cyclicity theorem in the
  local mixed holomorphic-topological model.
- LQ84 is stated for ordinary unital associative algebras. A dg algebra version
  for `A_psi` requires a separate dg extension argument or a separate source
  anchor.

### Tsy83

Source metadata:

- Boris L. Tsygan, "The homology of matrix Lie algebras over rings and the
  Hochschild homology", `Russian Mathematical Surveys` 38:2 (1983), 198--199.
- DOI: `10.1070/RM1983v038n02ABEH003481`.
- Crossref metadata checked: published print 30 April 1983, volume 38,
  issue 2, pages 198--199, DOI
  `10.1070/rm1983v038n02abeh003481`.
- MathNet metadata checked from search/open records: MathNet ID `rm7171`,
  received 15 June 1982, English version PDF available, original paper language
  Russian.
- Original Russian reference, as cited by LQ84: `Uspekhi Mat. Nauk` 38 (1983),
  217--218.
- Local mirror: none. No checksum recorded because no local source copy was
  added.

Verified theorem anchors:

- English translation p. 198: starts with a unital commutative ground ring `k`
  and a unital associative `k`-algebra `A`.
- Theorem 1, p. 198: if `k` is a field of characteristic zero, the coalgebra
  built from the cyclic-invariant functors `K_i(A)` is isomorphic to
  `H_*(gl(n,A); k)` in dimensions `0 < i < n`.
- Corollary 1, p. 198: after passage to the stable matrix Lie algebra, the
  resulting homology coalgebra is identified with the coalgebra built from
  those functors.
- Proof sketch, pp. 198--199: invariant CE chains decompose as a free
  cocommutative coalgebra whose primitive subcomplex is the cyclic-permutation
  subcomplex.
- Proposition 1 and Corollary 2, p. 199: the relevant cyclic-invariant complex
  sits in an exact sequence with Hochschild homology, matching the cyclic
  homology mechanism later written in the Loday--Quillen notation.

Supported manuscript claim:

- Tsy83 independently supports the matrix-Lie-homology/cyclic-homology
  provenance and the primitive/free-cocommutative-coalgebra mechanism behind
  the LQT template.
- Tsy83 is not the cleanest source for the manuscript's exact `HC_{*-1}`
  notation; use LQ84 Theorem 6.2 as the stable source-core theorem for that
  shift.

Non-support boundary:

- Tsy83 is a two-page announcement/communication. It does not by itself supply
  the manuscript's finite-window `A_psi` acceptance map, scalar quotient,
  connected single-trace projection, `A_infinity` transfer, Hamiltonian
  brane-defect trace theorem, or BV/QME package.
- Tsy83 uses its own functor notation before the LQ84 reduced cyclic homology
  presentation; do not cite it alone for the exact manuscript formula
  `HC_{*-1}`.

## Manuscript Anchor Check

Checked anchors:

- `main.tex:1750-1778`: LQT is presented as an external template and is fenced
  from the local Hamiltonian trace proof.
- `main.tex:8861-8880`: bibliography metadata for `loday-quillen` and
  `tsygan` agrees with Springer/Crossref/EUDML/MathNet on title, venue,
  volume, year, pages, and DOI.
- `theorem-lanes.tex:2079-2088`: the finite-window `lambda_{LQT,W}` map is
  listed as required theorem data, not as already supplied by the primary
  source.
- `claim-strength-ledger.tex:364-388` and
  `reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md:88-115`
  correctly keep the finite-window LQT comparison in the acceptance/obstruction
  ledger.

Metadata correction note:

- A secondary local Costello--Li text bibliography line gives LQ84 as
  `59(4), 569--591`. The primary publisher page, Crossref, EuDML, and
  E-Periodica all give pages 565--591. The manuscript bibliography already
  uses 565--591 and should not be changed on this point.

## Fixture Decision

Stable source core:

- LQ84 Theorem 6.2, with the hypotheses above, supports the manuscript's
  external-template shift `HC_{*-1}`.
- LQ84 Theorem 6.9 supports only a classical homological-degree stabilization
  statement. It does not discharge the finite-window word-degree comparison in
  `A_psi`.
- Tsy83 is recorded as an independent primary precursor and provenance anchor,
  not as the clean source for the manuscript's exact `HC_{*-1}` notation.

Internal derivation still required:

- The finite-window map `lambda_{LQT,W}` for
  `A_psi = T(x,y,psi), d psi = xy - yx`.
- Compatibility with connected single-trace projection and scalar quotient.
- The reduced cyclic chain model and any dg extension of the primary theorem.
- The open `A_infinity` transfer, cyclicity, BV pairing, and cone/Roos
  obstruction comparison.

## Remaining Source Gaps

- No exact theorem/page anchor was checked in Loday's book `Cyclic Homology`,
  2nd ed.; it is not part of this stable source core.
- No exact primary-source anchor was checked for the dg-algebra extension of
  LQT. Keep dg uses out of the stable source core until separately verified or
  derived.
- No local source PDF/text was imported; therefore no local checksum exists.

## Verification Commands

Commands run from `/Users/raeez/topological-strings`:

```bash
rg -n "Loday|Quillen|Tsygan|LQT|cyclic|stable matrix|matrix Lie|Lie algebra homology|primitive|HC_\\{|HC|cyclic homology|single-trace|large-?N" main.tex commands.tex mathmacros.tex notation.tex preamble.tex *.tex reconstitution references -g '!out/**' -g '!*.pdf'
rg --files references reconstitution scripts | rg -i 'loday|quillen|tsygan|lqt|cyclic|lie|matrix|source|provenance'
sed -n '1728,1786p' main.tex
sed -n '2060,2088p' theorem-lanes.tex
sed -n '8848,8876p' main.tex
rg -n "loday-quillen|tsygan|Loday--Quillen|Tsygan|Loday-Quillen|LQT|HC_\\{\\*-1\\}|HC_\\{n-1\\}|HC\\^\\*|cyclic cochain|cyclic homology" main.tex theorem-lanes.tex claim-strength-ledger.tex open-obligations.tex local-dictionary.tex references/source-provenance.md reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md
curl -L -s https://api.crossref.org/works/10.1007/BF02566367 | python3 -m json.tool | sed -n '1,220p'
curl -L -s https://api.crossref.org/works/10.1070/RM1983v038n02ABEH003481 | python3 -m json.tool | sed -n '1,240p'
curl -L -I -s 'https://doi.org/10.1070/RM1983v038n02ABEH003481' | sed -n '1,100p'
nl -ba main.tex | sed -n '1738,1778p'
nl -ba theorem-lanes.tex | sed -n '2079,2092p'
nl -ba claim-strength-ledger.tex | sed -n '360,390p'
nl -ba main.tex | sed -n '8861,8880p'
nl -ba reconstitution/open-ainfty-koszul-cyclic-acceptance-construction-target-2026-04-30.md | sed -n '84,118p'
```

Network/source lookup used:

- Springer DOI page for LQ84.
- Crossref API for LQ84 and Tsy83.
- EuDML/GDZ/E-Periodica open bibliographic/full-text routes for LQ84.
- MathNet/Crossref/DOI metadata and public English-translation excerpts for
  Tsy83.
