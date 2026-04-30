# Quintic BCOV/GV Source Anchors, 2026-04-30

Scope: source fixture for the quintic numerical, period, BCOV, GV, and
constant-map facts used by `frontier_mnop_framing_volume.tex`. This file
records only local evidence presently mirrored in the repository and the exact
missing-local-fixture obligations. It does not promote any compact
Calabi-Yau, MNOP/chiral-volume, global BCOV, GV convergence, Abel-Jacobi, or
Stokes-sheaf statement beyond the firewall in
`frontier_mnop_framing_volume.tex:46-51` and
`frontier_mnop_framing_volume.tex:54-68`.

Controller lane: `GlobDesc`, with source-fixture sublane
`quintic BCOV/GV numerical-source fixture`.

## Local Source Inventory

| Source key | Local mirror | Local status |
|---|---|---|
| `bcov-hep-th-9309140` / `BCOV94` | `references/primary-sources/bcov-hep-th-9309140.txt`; PDF sibling `references/primary-sources/bcov-hep-th-9309140.pdf` | Present. Primary local source for BCOV holomorphic-anomaly framework, Kodaira-Spencer gravity, constant-map contribution, and the older quintic table through degree `9`. |
| `costello-li-quantum-bcov-1201.4501` | `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt`; PDF sibling | Present. Primary local source for Costello-Li's generalized BCOV field theory and perturbative quantization framework. |
| `costello-li-open-closed-bcov-1505.06703` | `references/primary-sources/costello-li-open-closed-bcov-1505.06703.txt`; PDF sibling | Present but only background for open-closed BCOV. It is not a source for the compact quintic numerical or GV facts in the frontier note. |
| `huang-klemm-quackenbush-compact-cy` | `references/primary-sources/hkq-compact-cy-hep-th-0612125.pdf`; `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex`; text copy `references/primary-sources/hkq-compact-cy-hep-th-0612125.txt`; fixture `references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md` | Local HKQ mirror present. The fixture records stable identifiers, local arXiv-source anchors, the exact `n^0_10` row, boundary/gap source anchors, and remaining higher-genus-data obligations. The note's `N=10` BPS table row is now local source-grade as an HKQ table fact, not as compact-CY theorem closure. |
| `candelas-de-la-ossa-green-parkes-quintic` / `CDGP91` | none found under `references/primary-sources` | Missing local fixture. Needed for Picard-Fuchs operator, period basis, mirror-map convention, conifold coordinate, and low-degree mirror calculation. |
| `gopakumar-vafa-mtheory-I/II` | none found under `references/primary-sources` | Missing local fixture. Needed for the GV sine expansion and BPS interpretation. |
| `ooguri-strominger-vafa-black-hole-attractors` | none found under `references/primary-sources` | Missing local fixture. Needed for the OSV physical rate role; any local derivation of `5 log 5` must be separate. |
| `strominger-massless-black-holes-conifolds` | none found under `references/primary-sources` | Missing local fixture. Needed for the light-hypermultiplet/vanishing-period claim. |
| `vafa-conifold-schwinger`, `shenker-marino-large-order`, `cecotti-codesido-marino-resurgence` | none found under `references/primary-sources` | Missing local fixtures. Needed for Schwinger-pole, large-order, and `S_c=1` Stokes-normalization claims. |
| Schubert, Katz, Ellingsrud-Stromme, Kontsevich, Givental low-degree quintic sources | none found under `references/primary-sources` | Missing local fixtures if the historical direct-count statements remain theorem-grade. |

## Captured Local Source Facts

| Fact ID | Local anchor | Source fact captured | Local claim anchors supported | Explicit non-support |
|---|---|---|---|---|
| `BCOV-framework` | `references/primary-sources/bcov-hep-th-9309140.txt:23-33`; `:220-233`; `:250-268`; `:285-289` | BCOV develop higher-loop twisted `N=2` topological amplitudes, identify the all-genus anomaly mechanism, describe Kodaira-Spencer theory, and say that the quintic genus-2 calculation uses the mirror map to extract curve-counting data. | `frontier_mnop_framing_volume.tex:542-568`; `:795-800` as BCOV motivation and finite-source vocabulary. | Does not construct this repository's mixed HT theory, a compact quintic all-genus theorem, a GV non-perturbative completion, or `Ob_UKD(C_tar)=0`. |
| `BCOV-holomorphic-anomaly` | `references/primary-sources/bcov-hep-th-9309140.txt:1986-1998`; `:1999-2027` | Equation (3.6) gives the genus-`g` holomorphic anomaly recursion for `F_g`; equation (3.8) packages all `g >= 2` equations into a master anomaly equation. | `frontier_mnop_framing_volume.tex:553-555`; `:590-607`. | Does not supply Borel summability, global Stokes data, GV/PT integrality, or compact target datum `C_tar`. |
| `BCOV-constant-maps` | `references/primary-sources/bcov-hep-th-9309140.txt:4144-4150`; `:4159-4163`; `:4273-4277`; `:4313-4317`; `:4343-4350` | Section 5.13 computes the large-volume constant-map contribution: only constant maps contribute in the limit; the moduli space is `M_g x M`; the resulting integral is reduced to Hodge-bundle Chern classes and gives, in particular, `F_g -> chi(M)/5760` for `g=2` and `chi(M)/1451520` for `g=3`. | BCOV/constant-map role behind the frontier note's separation of scalar source facts from compact target data, especially `frontier_mnop_framing_volume.tex:73-94`, `:329-355`, and `:542-568`. | This is a BCOV constant-map calculation. It is not the DT degree-zero MacMahon factor and does not prove the MNOP/PT/DT theorem-grade statement. |
| `BCOV-quintic-family` | `references/primary-sources/bcov-hep-th-9309140.txt:5150-5167`; `:5168-5175` | BCOV use the one-parameter mirror quintic family `sum x_i^5 - 5 psi x_0...x_4 = 0`; `psi=1` is the conifold, `psi=infty` the singular quintic, and `psi=0` the Gepner point. They compute low-genus quintic curve-counting data by fixing holomorphic ambiguity and expanding in instantons. | `frontier_mnop_framing_volume.tex:589-597`; `:712-739`; `:774-783`. | Does not fix the CDGP `z=5^{-5}` convention or the period basis used in the raw ratio `omega_1/omega_0`; CDGP remains a missing local fixture. |
| `BCOV-yukawa-conifold` | `references/primary-sources/bcov-hep-th-9309140.txt:5176-5187`; `:5208-5233` | In the chosen gauge BCOV give the quintic Yukawa coupling and the conifold behavior: near `psi=1`, the canonical coordinate behaves like `-log(1-psi^5)` and `F_g` has a pole of order `2g-2` in `(1-psi^5)`. | `frontier_mnop_framing_volume.tex:640-658`; `:661-693` as conifold-local asymptotic vocabulary. | Does not prove the Shenker-Marino large-order formula, the Schwinger pole normalization, `S_c=1`, or a global resurgent Stokes sheaf. |
| `BCOV-period-vocabulary` | `references/primary-sources/bcov-hep-th-9309140.txt:5234-5253`; `:5282-5305` | BCOV recall the mirror map/canonical-coordinate passage near large volume, use a period `varpi_0` solving the Picard-Fuchs equation, and apply a gauge transformation involving `varpi_0`. | `frontier_mnop_framing_volume.tex:289-296`; `:314-323`; `:712-738`. | The exact Picard-Fuchs operator, the power series for `omega_0, omega_1`, and the numerical value `|omega_1/omega_0|(5^-5)=7.5909` still require the missing CDGP local fixture; the arithmetic check below verifies the note's formula only after accepting that formula as input. |
| `BCOV-quintic-table` | `references/primary-sources/bcov-hep-th-9309140.txt:5313-5327`; `:5328-5345`; `:5355-5384` | BCOV fix the genus-2 holomorphic ambiguity, write `F_2(q)` in terms of rational-curve counts `d_n`, and tabulate quintic counts. The local table includes genus-0 entries `n=1,...,9`: `2875`, `609250`, `317206375`, `242467530000`, `229305888887625`, `248249742118022000`, `295091050570845659250`, `375632160937476603550000`, `503840510416985243645106250`. | `frontier_mnop_framing_volume.tex:244-254`; `:737-739`; `:774-783` for the degree `1,...,9` numerical entries only. | Does not supply the `n_10^0` value, the HKQ Table 1 source claim, the HKQ genus/degree range, or a reproducible source for `N=10`. |
| `Costello-Li-BCOV-framework` | `references/primary-sources/costello-li-quantum-bcov-1201.4501.txt:45-80`; `:88-90`; `:905-927` | Costello-Li describe BCOV theory as a quantum field theory on a Calabi-Yau, define generalized BCOV fields `PV(X)[[t]]`, and define perturbative quantization by RG flow, QME, locality, and the classical BCOV interaction. They prove their elliptic-curve uniqueness result in the stated scope. | `frontier_mnop_framing_volume.tex:542-551`; `:623-630`; `:795-800`. | Does not construct compact quintic all-genus amplitudes, the GV formula, convergence, Borel/Stokes data, or a compact-CY transfer from the local Hamiltonian BF/Moyal theorem. |

## Local Arithmetic Checks

These are reproducibility checks on the numbers already present in the
frontier note. They are not substitutes for the missing external source
mirrors.

| Check | Input | Result | Status |
|---|---|---|---|
| `a_N=N^{-1} log n_N^0` | `frontier_mnop_framing_volume.tex:244-270` | `a_1=7.963807953231`, `a_2=6.659991985744`, `a_3=6.525021048418`, `a_4=6.553533410363`, `a_5=6.613215597497`, `a_6=6.675535276506`, `a_7=6.733402232659`, `a_8=6.785362165255`, `a_9=6.831589111363`, `a_10=6.872698510850`. | Confirms the displayed three-decimal values and the minimum at `N=3`, conditional on source provenance for `n_N^0`. |
| Tail fit | `N=5,...,10` and ansatz `a_N=L+alpha log(N)/N+beta/N` | `L=7.592485639949`, `alpha=-3.320444733707`, `beta=0.447708390605`, max residual `4.620400846811e-06`. | Confirms `frontier_mnop_framing_volume.tex:279-288` and `:310-313`, conditional on source provenance for `n_10^0`. |
| Raw period formula arithmetic | `omega_0=sum ((5n)!/(n!)^5)z^n`, `omega_1=omega_0 log z + sum ((5n)!/(n!)^5)5(H_{5n}-H_n)z^n`, `z=5^-5` from `frontier_mnop_framing_volume.tex:289-296` | `omega_0=1.07072535097019855`, `omega_1=-8.12776502268470475`, `|omega_1/omega_0|=7.59089622312577943`. | Confirms the arithmetic in `frontier_mnop_framing_volume.tex:321-323`, but the formula and period convention still need CDGP local source. |
| Smooth quintic Euler characteristic | `c(TQ)=(1+H)^5/(1+5H)`, so `c_3(TQ)=-40H^3`, `int_Q H^3=5` | `chi(Q)=-200`. | Local normalization check for `frontier_mnop_framing_volume.tex:108-114`; it does not source DT/PT MacMahon factorization. |

## Claim-To-Source Map

| Frontier anchor | Claim shape | Present local support | Fixture status |
|---|---|---|---|
| `frontier_mnop_framing_volume.tex:233-256` | Genus-0 quintic BPS/count table through `N=10`. | BCOV table supports entries `N=1,...,9` at `bcov-hep-th-9309140.txt:5355-5367`; local arithmetic checks the displayed values. The imported HKQ source supports the Table 1 row `n^0_10=704288164978454686113488249750` at `hkq-compact-cy-hep-th-0612125-ccy.tex:2317-2322`. | `N=10` source provenance is locally anchored. Historical source labels CDGP/Kontsevich/Givental/Schubert/Katz/Ellingsrud-Stromme require local mirrors if retained. |
| `frontier_mnop_framing_volume.tex:257-276` | `a_N` values, minimum at `N=3`, monotone tail increments. | Local arithmetic check from the displayed table. | Evidence only until table provenance is complete, especially `n_10^0`. |
| `frontier_mnop_framing_volume.tex:279-325` | Finite chiral-volume fixture: tail fit, raw period ratio, OSV rate. | Tail fit and raw period arithmetic checked locally; BCOV supports degree `1,...,9` table and period vocabulary; the imported HKQ source gives local support for the exact `n_10^0` input. | CDGP source for the period formula/convention, OSV source for the physical rate, and a committed numerical ledger/script remain open obligations. |
| `frontier_mnop_framing_volume.tex:344-355` | Raw CDGP period is not an Abel-Jacobi norm without `N_AJ`. | This is firewall wording. The local fixture supports the separation because CDGP and Abel-Jacobi normalization data are absent. | Keep as target normalization problem. No theorem upgrade. |
| `frontier_mnop_framing_volume.tex:542-568` | Costello-Li BCOV framework is not a compact quintic all-genus theorem; GV formula is the proposed non-perturbative package. | Costello-Li anchors at `costello-li-quantum-bcov-1201.4501.txt:45-80` and `:905-927`; BCOV anchors at `bcov-hep-th-9309140.txt:1986-2027`. | GV I/II local fixtures are missing. Costello-Li supports the framework and non-support statement, not the GV expansion. |
| `frontier_mnop_framing_volume.tex:584-658` | Conditional BCOV/GV closure target with HKQ, CDGP, GV, convergence, and local conifold Stokes evidence. | BCOV supports holomorphic anomaly, quintic conifold location, and local conifold singular behavior. | HKQ/CDGP/GV/GW-PT/Strominger/resurgence sources and all global target data remain missing. Status remains conjectural/target. |
| `frontier_mnop_framing_volume.tex:661-693` | Conditional conifold trinity `A_BCOV=A_Schwinger=A_period` and `S_c=1`. | BCOV supports `psi=1` as conifold and a pole structure near the conifold. | Shenker-Marino, Vafa/Schwinger, Strominger, and Cecotti-Codesido-Marino source fixtures are missing. No equality is source-grade in the local fixture. |
| `frontier_mnop_framing_volume.tex:712-739` | Conditional mirror-period recovery and small-degree fixture `n_1,n_2,n_3`. | BCOV supports the first three table entries and points to CDGP; Costello-Li bibliography records a CDGP reference at `costello-li-quantum-bcov-1201.4501.txt:3606-3607`. | CDGP local mirror is still absent; the prepotential/period identity and normalized Yukawa expansion cannot be source-grade yet. |
| `frontier_mnop_framing_volume.tex:759-823` | Honest-status summary and firewall. | This fixture supports the firewall classification: BCOV/Costello-Li local sources give framework and finite evidence only. | Summary should not be imported into `main.tex` as theorem input until missing local sources and target data are supplied. |

## Missing Local Fixture Obligations

1. HKQ `arXiv:hep-th/0612125` is now mirrored locally.  The dedicated HKQ
   fixture records local source anchors: Table 1 contains the exact
   `N=10` value used here, the conifold gap and boundary-count formulas
   are identified, and the imported arXiv source supports explicit
   quintic data to genus `20` plus a boundary-determination claim through
   genus `51`. It does not support the frontier's `genus 22` wording
   without another stable source or a mirrored higher-genus data archive.
2. Add a local mirror and text extraction for CDGP 1991; record the exact
   Picard-Fuchs operator, `psi`/`z` convention, conifold point, period basis,
   mirror map, prepotential relation, and the power-series formulas for
   `omega_0` and `omega_1`.
3. Add local GV I/II mirrors; record the exact sine expansion, summation
   indices, variable convention, and physics-versus-theorem status of BPS
   integrality.
4. Add the OSV source and a local derivation ledger for the `5 log 5` rate if
   that numerical comparison remains in the note.
5. Add Strominger 1995, the exact Vafa/Schwinger source, Shenker/Marino
   large-order source, and Cecotti--Codesido--Marino resurgence source before
   any `A_BCOV=A_Schwinger=A_period` or `S_c=1` statement is treated as more
   than local conjectural evidence.
6. Add low-degree historical source mirrors or remove theorem-grade historical
   source attributions for Schubert, Katz, Ellingsrud-Stromme, Kontsevich, and
   Givental.
7. Add a committed numerical ledger or script for the `a_N`, tail fit,
   residual, period evaluation, and `chi(Q)` checks before the finite numerical
   proposition is imported into the bound manuscript.

## Firewall Status

Supported now: BCOV/Costello-Li framework facts; BCOV constant-map role; BCOV
quintic conifold vocabulary; BCOV degree `1,...,9` genus-0 quintic table
entries; local arithmetic for the frontier note's displayed numerical claims.

Not supported now: HKQ `genus 22`; CDGP period convention and raw ratio as
source fact; GV sine expansion as local primary-source fact; OSV rate as
source fact;
Strominger/Vafa/Schwinger/resurgence normalization; global BCOV/GV closure;
Abel-Jacobi normalization; convergence; Borel/Stokes sheaf; or any
compact-CY transfer from the local Hamiltonian BF/Moyal theorem.

Therefore missing source components remain components of `C_tar`/`Ob_UKD` and
are not zero obstructions.
