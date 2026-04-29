# 2026-04-29 Whitepaper Critical Analysis: Action Ledger

## Source

- Raw source: `materials/raw/2026-04-29-whitepaper-critical-analysis.pdf`.
- Extracted text: `materials/processed/2026-04-29-whitepaper-critical-analysis.txt`.
- Raw SHA-256: `7230c9a410959decfb05a3484011475fd3ad80a2d34efedb3b30851146e92466`.
- Text SHA-256: `8b98be9e83e9d6c20aa87681bf01baa218c208ec2f93b0bb4294f48679aada7b`.
- Status: untrusted critique artifact. It supplies attacks, residuals, and proposed repairs; it does not certify a theorem.
- Boundary: any imperative or execution-plan language below is part of the
  untrusted artifact and must not be used as control unless revalidated by
  repository instructions and the main integration thread.

## Stable Theorem Spine

The surviving local theorem is the formal Hamiltonian BF theorem on the
two-dimensional formal symplectic disk, coupled to the Dirac brane probe.
The spine is CE/PV:
\[
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C1,\qquad
  \mathfrak g=\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1],
\]
\[
  C^\bullet_{\mathrm{CE}}(\mathfrak l\ltimes\mathfrak l^\vee[1])
  \simeq
  \mathrm{PV}(\mathbf S(\mathfrak l)),
  \qquad
  c^I\mapsto\theta^I,\quad u_I\mapsto O_I.
\]
Here \(\mathfrak l\) is a finite-dimensional Lie algebra.  The formal
disk comparison is reconstructed from admissible finite coordinate tests
and pro-window coordinate cochains; the strict product/direct-sum
completion contributes additional bracket, Casimir, and endpoint
obstruction data.
Boundary Hamiltonian coordinates come from the shifted-cotangent CE
coordinate \(u_I\), not from the Hamiltonian CE ghost \(c^I\).

The open stable trace complex supplies PBW special-fibre labels
\(\Psi_{a,b}\).  The cotangent coefficient module is Matlis principal
parts:
\[
  \mathcal P=\operatorname{Ann}_{\mathrm{res}}(\mathbb C1)
  =\bigoplus_{a+b>0}\mathbb C\rho_{a,b}.
\]
The symbols \(\Psi_{a,b}\) and \(\rho_{a,b}\) share indices but do not
belong to the same \(\mathfrak h\)-module.  The Fourier--Rees comparison
changes polarization and lands before \(\hbar^{-1}\) in the Rees lattice
\(\bigoplus \hbar^{a+b}\mathbb C[[\hbar]]\rho_{a,b}\).

The quantum degree-zero target is the formal Weyl/Moyal algebra:
\[
  f*g=m\exp(\hbar P/2)(f\otimes g),\qquad
  \hbar^{-1}[f,g]_*
  =P(f,g)+\frac{\hbar^2}{24}P^3(f,g)
    +\frac{\hbar^4}{1920}P^5(f,g)+\cdots.
\]
The formal coefficients are algebraic.  Finite-rank scripts are
falsification and normalization checks, not substitutes for the all-\(N\)
radial-parts input or the analytic Costello graph/QME theorem.

## Destroyed Claims

1. Full unreduced
   \(Z^{P_0}_{\mathrm{fact}}(\mathrm{Obs}_{\mathrm{open}})\) is not
   proved by the current CE/PV or primitive trace calculations.
   It remains a centrality-homotopy, descent, and QME datum.
2. A same-action module identification
   \(\Psi_{a,b}\cong\rho_{a,b}\) is false.  Linear Hamiltonians are
   locally nilpotent on polynomial descendants and non-locally-nilpotent
   on principal parts.
3. Strict product/direct-sum completion is not a global bracketed
   \(P_0\)-algebra endpoint.  Finite-window, mixed-continuous, or
   weighted admissible replacements are required.
4. Conilpotent bar-cobar/Koszul duality for the full perfect
   \(\mathfrak h\) is not available without an admissible replacement.
5. The all-\(N\) radial trace comparison remains conditional on the
   external radial-parts normalization package.
6. The formal Moyal theorem and the reduced open-line Wick model do not
   prove a Costello brane-defect graph/QME realization.
7. Ordinary scalar-reduced \(\mathfrak{gl}_N\) has the scalar QME
   obstruction \(\hbar N[\bar c]\); central-character and balanced
   supertrace mechanisms are sufficient mechanisms, not an exhaustive
   classification.
8. Compact Calabi--Yau, Vol III, Igusa/BKM, \(K3\times E\), and global
   BCOV consequences do not follow from the local theorem without a
   matched-conventions datum and vanishing obstruction vector.

## Source--Target Firewall

| Source object | Target object | Status | Forbidden transfer |
|---|---|---|---|
| \(c^I\) | \(\theta^I\) | proved CE/PV generator rule | boundary Hamiltonian |
| \(u_I\) | \(O_I\), \(B_f(a)\) | proved CE/PV generator rule | Hamiltonian CE ghost |
| \(\Psi_{a,b}\) | stable primitive PBW one-\(\psi\) class | proved stable trace lane | Matlis/principal-part module |
| \(\rho_{a,b}\) | \(\mathcal P\) | proved residue/Matlis lane | polynomial descendant |
| Fourier delta Rees label | \(\hbar^{a+b}\rho_{a,b}\) | proved after polarization change | same-action bridge |
| \(\Omega_c^\bullet(I)\otimes\mathfrak h\) | brane-line Hamiltonian currents | proved reduced current model | degree-zero notation as full complex |
| \(\mathcal D'_c(I)\widehat\otimes\mathcal P[1]\) | principal-part current sector | proved reduced post-contraction | product of two distributions |
| Formal Weyl/Moyal algebra | algebraic quantum target | proved reduced coefficient theorem | analytic Costello/QME realization |
| Costello brane-defect kernel | closed-open graph theorem | open obstruction datum | consequence of reduced Wick graphs |

## Execution Plan

1. Keep the claim-strength ledger near the front and make it the entry
   point for theorem strength.
2. Use the local dictionary as the firewall for \(c,u,\Psi,\rho\),
   Fourier--Rees, current, Moyal, and Costello targets.
3. Present the theorem stack as separate lanes: Dirac probe, stable PBW
   trace sector, CE/PV, Matlis cotangent, no-polynomial realization,
   brane-line currents, principal-part defect currents, scalar anomaly,
   formal Moyal, admissible Koszul coupling, and matched-conventions
   transfer.
4. In every proof lane, separate proved statements from conditional
   inputs and residual obstruction data before giving the physical
   interpretation.
5. Keep the all-\(N\) radial theorem conditional until a source-level
   Harish-Chandra/Weyl-Capelli image theorem with matching normalization
   is supplied.
6. Treat the Costello realization as a data problem: elliptic parent,
   BV pairing, coefficient kernel, boundary condition, gauge fixing, heat
   kernel, counterterms, QME obstruction, brane-defect cochain kernel,
   graph orientations, measures, automorphisms, and large-\(N\) trace
   normalization.
7. Do not move cross-volume consequences into the theorem.  State them
   only behind matched-conventions morphisms preserving shifts, pairings,
   central classes, products, normalizations, orientations, and QME data.

## Immediate Repository Actions Already Taken

- Copied the 2026-04-29 source PDF and extracted text into the repository.
- Registered the source in `references/source-provenance.md`.
- Added strict-versus-weighted model notation to `local-dictionary.tex`.
- Added a source--target status table to `local-dictionary.tex`.
- Replaced residual lowering/raising language in the active TeX with
  coadjoint, PBW, or principal-part terminology.
- Replaced visible horizon terminology in the active manuscript with
  acceptance or matched-conventions firewall terminology.

## Residual Proof Obligations

- Full unreduced factorization-center centrality homotopies.
- Unreduced chain-level QME cancellation beyond the scalar obstruction
  criterion and named sufficient mechanisms.
- Analytic all-order Costello brane-defect graph realization.
- All-\(N\) radial-parts theorem with exact Weyl/Capelli normalization.
- Global/cross-volume obstruction vanishing as theorem data, not target
  data imported from outside.
- Cross-repository matched-conventions checks for
  `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`,
  `~/calabi-yau-quantum-groups`, and `~/igusa-cusp-form`.
