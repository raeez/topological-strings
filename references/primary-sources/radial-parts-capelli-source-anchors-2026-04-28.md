# Radial-Parts and Capelli Source Anchors

Date: 2026-04-28

Scope: Worker 2 adversarial source pass for the radial-parts,
Harish-Chandra, Wallach, Levasseur-Stafford, Capelli, and Howe claims.

## Claims Attacked

### Exact bivariate triangular trace formula

Local formula:

```tex
J_N(z_1^a z_2^b) \equiv
  \sum_{r=0}^{\min(a,b)}
    \left(-\frac{\hbar N}{2}\right)^r
    r!\binom ar\binom br\,T_{a-r,b-r}.
```

Status: locally proved, not externally sourced.

Primary anchors checked:

- `howe-remarks-classical-invariant-theory.txt:1153-1223`:
  Howe, Sec. 5(f), "The Capelli identities", states the standard
  Capelli identity and begins its proof after Eq. (C).
- `howe-remarks-classical-invariant-theory.txt:1207-1220`:
  Eq. (C) is the determinant Capelli identity and source context for
  the Capelli contact phenomenon.

Failure mode: Howe/Capelli do not state the manuscript's exact
bivariate Weyl-trace triangular formula. No primary source found in this
pass states the coefficient
`(-hbar N/2)^r r! binom(a,r) binom(b,r)` for
`Tr(Op_W(z1^a z2^b)(X,Y))` after Hamiltonian reduction.

Manuscript action: `appendix-radial-parts-moyal.tex` now identifies the
formula as locally proved by the contraction count; `main.tex` no longer
calls it an externally sourced bivariate Capelli identity.

## Vandermonde-Conjugated Radial-Parts Input

Local conditional input:

```tex
Rad_0(J_N(f)) = \Delta^{-1} S_N(f) \Delta,
\qquad
S_N(f)=\sum_i Op_W(f)(\lambda_i,-\hbar\partial_{\lambda_i}).
```

Status: conditional external input.

Primary anchors checked:

- `levasseur-stafford-kernel-harish-chandra.txt:57-64`:
  the introduction records Harish-Chandra's homomorphism
  `D(g)^G -> D(h)^W` and says Levasseur-Stafford 1995 proves
  surjectivity.
- `levasseur-stafford-kernel-harish-chandra.txt:84-90`:
  Theorem 1.1 states the kernel theorem
  `J = D(g) tau(g)`, hence identifies the kernel ideal.
- `levasseur-stafford-kernel-harish-chandra.txt:239-260`:
  the text recalls the discriminant/generic locus and cites the
  isomorphism `D(g)^G/I -> D(h)^W`.
- `levasseur-stafford-kernel-harish-chandra.txt:492-500`:
  Theorem 5.5 proves the reductive algebraic statement completing the
  proof of Theorem 1.1.
- `levasseur-stafford-kernel-harish-chandra.txt:531-535`:
  the paper relates the algebraic theorem to Harish-Chandra's analytic
  theorem on invariant operators.

Failure mode: these anchors support the Harish-Chandra homomorphism,
kernel, and surjectivity context. They do not by themselves verify the
exact manuscript convention:

```tex
Rad_0(J_N(f)) = \Delta^{-1} S_N(f) \Delta
```

with the sign convention
`z_2 = -\hbar\partial_\lambda`, the cotangent/Weyl identification
`\mathcal W_N \simeq \mathcal D_\hbar(\mathfrak{gl}_N)`, and the
specific claim that the resulting reduced invariant quotient injects in
the form needed for `J_N(f)`.

Direct AMS PDF probes for Levasseur-Stafford 1995, Wallach 1993, and
Harish-Chandra 1964 returned HTTP 403 from the local shell, so no new
primary full-text page anchors were added.

Manuscript action: `main.tex` and `appendix-radial-parts-moyal.tex` now
state the finite-`N` radial-parts theorem and the degree-zero quantum
upgrade as conditional on this external input.

## Secondary Diagnostic Only

Web search found lecture-note statements of the desired theorem in
Cherednik/Calogero-Moser notes: the radial part has poles, conjugation
by the discriminant removes them, Harish-Chandra gives landing in
`D(h)^W`, and Levasseur-Stafford gives `D(g)//g \simeq D(h)^W`.
These notes are useful diagnostics but are not primary-source closure for
the manuscript.

## Wave 5 Re-Attack: Exact Weyl-Trace Image Normalization

Date: 2026-04-28.

Claim attacked:

```tex
\operatorname{Rad}_0(J_N(f))
  =\Delta^{-1}\left(\sum_i
    \operatorname{Op}_{\mathrm W}
      (f)(\lambda_i,-\hbar\partial_{\lambda_i})\right)\Delta.
```

Status: conditional at all \(N\); directly checked in rank \(N=2\) for
a finite family.

Primary-source comparison:

- `levasseur-stafford-kernel-harish-chandra.txt:57-64` records the
  Harish-Chandra homomorphism `D(g)^G -> D(h)^W` and the
  Levasseur-Stafford surjectivity context.
- `levasseur-stafford-kernel-harish-chandra.txt:84-90` records the
  kernel theorem context `J = D(g) tau(g)`.
- `levasseur-stafford-kernel-harish-chandra.txt:239-260` records the
  discriminant/generic-locus passage and the quotient
  `D(g)^G/I -> D(h)^W`.
- `levasseur-stafford-kernel-harish-chandra.txt:492-500` records the
  proof endpoint for Theorem 1.1.
- NUMDAM/EUDML metadata verify the published form of
  Levasseur--Stafford 1996: Annales scientifiques de l'Ecole Normale
  Superieure 29 (1996), 385--397, DOI `10.24033/asens.1743`.
- AMS issue metadata verify Levasseur--Stafford 1995:
  `Invariant differential operators and an homomorphism of
  Harish-Chandra`, JAMS 8 (1995), 365--372, DOI
  `10.1090/S0894-0347-1995-1284849-8`.
- EUDML/NUMDAM reference metadata list Wallach 1993, JAMS 6 (1993),
  779--816, as the Wallach source in the same radial-parts lineage.

Failure mode:

These anchors source the homomorphism, regular-Cartan landing,
surjectivity/kernel context, and discriminant conjugation lineage. They
still do not state the manuscript's exact Weyl-trace generator formula
with `Y^i_j=-\hbar\partial_{X^j_i}`, `z_2=-\hbar\partial_\lambda`,
total Weyl ordering, and the image `J_N(f) -> Delta^{-1}S_N(f)Delta`.

Local computation added:

`scripts/check_moyal_coefficients.py` now includes a direct \(N=2\)
radial-parts falsification harness. It applies the actual matrix Weyl
differential operator `J_2(f)` on invariant test polynomials on
`\mathfrak{gl}_2`, restricts to diagonal matrices, and compares the
result with `Delta^{-1}S_2(f)Delta`.

The checked operators are:

```text
z2, z2^2, z1 z2, z1^2 z2, z1 z2^2, z1^2 z2^2.
```

The checked invariant test functions are:

```text
1, Tr X, Tr X^2, Tr X^3, (Tr X)^2, (Tr X)(Tr X^2).
```

All 36 operator/test-polynomial comparisons pass over exact rational
coefficients with symbolic powers of `hbar`. This supports the signs
`Y=-\hbar\partial_X^t`, `z_2=-\hbar\partial_\lambda`, and the
Vandermonde conjugation normalization in rank two. It does not prove
the all-\(N\) source theorem or the all-polynomial image formula.

Manuscript action:

`appendix-radial-parts-moyal.tex` now states that the exact Weyl-trace
image normalization is part of the external radial-parts input. The
proof records the pure-power/shear generation only as an internal
convention check, not as an independent proof of the
Harish-Chandra--Wallach--Levasseur--Stafford theorem.

## Wave 6 Re-Attack: All-\(N\) Normalization and Pure-Power/Shear Reduction

Date: 2026-04-28.

Claim attacked:

```tex
\operatorname{Rad}_0(J_N(f))
  =\Delta^{-1}\left(\sum_i
    \operatorname{Op}_{\mathrm W}
      (f)(\lambda_i,-\hbar\partial_{\lambda_i})\right)\Delta
```

with the sign conventions
`Y^i_j=-\hbar\partial_{X^j_i}` and
`z_2=-\hbar\partial_\lambda`.

Status: still conditional at all \(N\).  The conditional input is now
sharper: it is enough to source the pure \(z_1\)- and \(z_2\)-power
images and compatibility with the Weyl adjoint shears
`Y -> Y + p(X)`, equivalently
`-\hbar d_lambda -> -\hbar d_lambda + p(lambda)`.

Primary-source comparison added:

- `levasseur-stafford-symmetric-spaces-aif-1999.txt:27-38`
  restates the Harish-Chandra homomorphism context and records that
  Levasseur--Stafford [17], [18] prove surjectivity and the kernel
  statement.
- `levasseur-stafford-symmetric-spaces-aif-1999.txt:83-88`
  identifies the diagonal case with the adjoint action and points to the
  stronger kernel theorem in Levasseur--Stafford 1996.
- `levasseur-stafford-symmetric-spaces-aif-1999.txt:151-156`
  states the radial component map, its kernel, and its image algebra in
  the symmetric-space setting.
- `levasseur-stafford-symmetric-spaces-aif-1999.txt:1194-1198`
  recalls the radial component map by restriction plus the Chevalley
  isomorphism and again records `Ker rad = Z(p)`.
- `levasseur-stafford-symmetric-spaces-aif-1999.txt:1474-1480`
  gives the official AIF bibliography entries for Levasseur--Stafford
  1995 and 1996.
- `levasseur-stafford-kernel-harish-chandra.txt:57-64`,
  `:84-90`, `:239-260`, and `:492-500` remain the local anchors for
  the reductive Lie algebra Harish-Chandra map, the kernel theorem, the
  discriminant/generic-locus passage, and the proof endpoint.

Failure mode:

The added AIF/NUMDAM source strengthens the primary-source chain for
radial component maps and the diagonal adjoint case.  It still does not
state the manuscript's exact Weyl-trace generator image, total Weyl
ordering, or the pure-power/shear compatibility needed to derive all
mixed monomials.  No all-\(N\) source closure was found.

Local computation added:

`scripts/check_moyal_coefficients.py` now has a generic direct
radial-restriction harness for \(N=2\) and \(N=3\).  It compares the
polynomial identity

```text
Delta * (J_N(f)F)|_t = S_N(f)(Delta * F|_t)
```

so the test does not depend on a division algorithm for `Delta`.  The
checked operators in each rank are:

```text
z1, z1^2, z1^3, z2, z2^2, z2^3,
z1 z2, z1^2 z2, z1 z2^2, z1^2 z2^2.
```

The checked invariant test functions in each rank are:

```text
1, Tr X, Tr X^2, Tr X^3, (Tr X)^2, (Tr X)(Tr X^2),
(Tr X)^3, 2(Tr X)^3 - 3(Tr X)(Tr X^2) + Tr X^3.
```

All \(80\) operator/test-polynomial comparisons pass for \(N=2\) and
all \(80\) pass for \(N=3\), over exact rational coefficients with
symbolic powers of `hbar`.  These tests support the signs
`Y=-\hbar d_X^t`, `z_2=-\hbar d_lambda`, and Vandermonde conjugation in
ranks two and three.  They do not prove injectivity or image
normalization at all \(N\).

Manuscript action:

`appendix-radial-parts-moyal.tex` now contains
Lemma `lem:app-radial-nonlinear-shear-obstruction`, which shows that
pure powers plus classical nonlinear shears do not determine the exact
mixed Weyl-trace image.  The theorem remains explicitly conditional
because the cited primary sources do not supply the required
quantum-corrected radial-parts normalization package.
