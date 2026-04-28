# Matlis / Local Cohomology / Grothendieck Residue Anchor

Date: 2026-04-28

Scope: source-anchor metadata for the reduced principal-part cotangent
module. No copyrighted full text is copied here.

## Local Formula

For \(R=\mathbb C[[z_1,z_2]]\), \(\mathfrak m=(z_1,z_2)\), and
\(\omega_R=R\,dz_1dz_2\),
\[
H^2_{\mathfrak m}(R)\,dz_1dz_2
  \cong E_R(\mathbb C).
\]
The Cech model is
\[
H^2_{\mathfrak m}(R)
  =R[z_1^{-1},z_2^{-1}]/(R[z_1^{-1}]+R[z_2^{-1}])
  =\bigoplus_{a,b\ge 0}\mathbb C z_1^{-a-1}z_2^{-b-1}.
\]
The residue functional extracts the coefficient of
\[
z_1^{-1}z_2^{-1}\,dz_1dz_2.
\]
The reduced principal-part space is the scalar-annihilator
\[
\mathcal P=\operatorname{Ann}(\mathbb C\cdot 1)
  =\bigoplus_{a+b>0}\mathbb C\rho_{a,b},
  \qquad
\rho_{a,b}=z_1^{-a-1}z_2^{-b-1}dz_1dz_2.
\]
It is a \(\mathbb C\)-linear Hamiltonian-coadjoint module, not an
\(R\)-submodule and not the literal \(R\)-module Matlis dual of
\(R/\mathbb C\cdot1\).

## Publisher / Primary Anchors

- Matlis, Eben, "Injective modules over Noetherian rings", Pacific
  Journal of Mathematics 8 (1958), no. 3, 511--528.
  Official MSP/Pacific Journal PDF:
  `https://msp.org/pjm/1958/8-3/pjm-v8-n3-p13-p.pdf`.
  Local text anchors already verified in
  `matlis-injective-modules-noetherian-rings.txt`: Proposition 3.1
  (printed pp. 518--519), Theorem 4.2 (printed pp. 526--528), and
  Corollary 4.3 (printed p. 528).
- Hartshorne, Robin, *Local Cohomology: A Seminar Given by
  A. Grothendieck, Harvard University, Fall 1961*, Lecture Notes in
  Mathematics 41, Springer-Verlag, 1967. DOI `10.1007/BFb0073971`.
  Springer page verifies the publisher, DOI, series, chapter structure,
  and pages for the local-cohomology seminar.
- Kunz, Ernst; Cox, David A.; Dickenstein, Alicia, *Residues and
  Duality for Projective Algebraic Varieties*, University Lecture
  Series 47, American Mathematical Society, 2008. AMS page verifies
  Chapter 5, "Residues and local cohomology for power series rings";
  the AMS endmatter index anchors the residue-induced linear map at
  p. 40 and the local duality theorem for power series rings at p. 45.

## Modern Cross-Check Anchors

- Stacks Project, Dualizing Complexes, Section 47.19: a canonical module
  \(K\) satisfies \(\operatorname{Hom}_A(K,E)\cong H^{\dim A}_{\mathfrak m}(A)\)
  for \(E\) the injective hull of the residue field.
- Stacks Project, Dualizing Complexes, Lemma 47.21.3: a regular local
  ring is Gorenstein; hence \(A[0]\) supplies the dualizing complex.
- Stacks Project, Cohomology of Schemes, Lemma 30.8.1: the Cech
  calculation leaves exactly the all-negative Laurent monomials in top
  degree and uses the coefficient-of-\((T_0\cdots T_n)^{-1}\) pairing.

## Status

The source residual for
\[
E_R(\mathbb C)\cong H^2_{\mathfrak m}(\mathbb C[[z_1,z_2]])\,dz_1dz_2
\]
and the Cech-Laurent/residue basis is closed at publisher-grade source
level. The manuscript's theorem status remains local and algebraic:
the proof is the displayed coordinate Cech/residue calculation plus the
bounded script check of the Hamiltonian coadjoint formula.
