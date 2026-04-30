# Compact-CY Source-Fixture Split, 2026-04-30

Scope.  This fixture separates compact Calabi--Yau source data into
domain lanes.  It is not a theorem in `main.tex`, not a CoHA fixture,
and not a construction of compact target data.  It records which local
mirrors and fixture files may be used as source evidence, which claims
they cannot support, and what evidence is still needed before a
theorem-grade import.

Admission rule.  A lane supports only the source facts explicitly
anchored in that lane.  No HKQ, CDGP, GV, OSV, Abel--Jacobi, or
conifold/Stokes datum is a consequence of the CoHA/centre fixture.  The
CoHA/centre fixture records Hall, Joyce/KPS, orientation, and centre
grammar only.

Stable core.  HKQ, CDGP, and GV now have repository-local primary
mirrors with checksums.  OSV has a fixture with remote arXiv-source
anchors but no repository-local primary mirror.  Abel--Jacobi
normalisation and conifold/Stokes normalisation remain unfixtured
source obligations.

## Lane Inventory

| Lane | Current fixture | Local mirror status | Admissible use | Forbidden use |
|---|---|---|---|---|
| HKQ compact BCOV/quintic bootstrap | `references/primary-sources/compact-cy-bcov-hkq-source-anchors-2026-04-30.md` | Local PDF, TeX source, and text copy present. | HKQ boundary/gap conditions, quintic `n^0_10` table row, boundary-count and finite-genus source facts. | GV formula, CDGP period basis, OSV rate, Abel--Jacobi norm, conifold Stokes constant, compact target object, CoHA consequence, or `Ob_UKD(C_tar)=0`. |
| CDGP mirror-quintic periods | `references/primary-sources/mirror-quintic-cdgp-period-source-anchors-2026-04-30.md` | Local PDF mirror and OCR text present. | Mirror-quintic family, Picard--Fuchs/period mechanism, conifold coordinate after convention translation, integral period-basis mechanism, prepotential/Yukawa source facts. | Raw numerical period ratio as a source fact, Abel--Jacobi norm, OSV rate, GV integrality, Stokes normalisation, CoHA consequence, or compact target theorem. |
| GV BPS/sine expansion | `references/primary-sources/gopakumar-vafa-bps-source-anchors-2026-04-30.md` | GV I/II local PDFs, TeX streams, and PDF text extractions present. | Physics BPS interpretation, Schwinger one-loop mechanism, GV sine multi-cover formula in GV variables, integer BPS-index coefficients as physics-source data. | Theorem-grade enumerative integrality, PT/GW/MNOP/KKV, compact-quintic all-genus equality, convergence, CDGP periods, OSV rate, Abel--Jacobi or Stokes normalisation, CoHA consequence. |
| OSV attractor/mixed ensemble | `references/primary-sources/osv-attractor-rate-source-anchors-2026-04-30.md` | Markdown fixture present; local OSV PDF/TeX/text mirror absent. | Remote-source physics vocabulary for `Z_BH=|Z_top|^2`, attractor variables, corrected free energy, mixed ensemble, and background-dependence firewall. | Repository-local source-grade use, `5 log 5` as an OSV source fact, fixed-class quintic growth, convergence, CDGP/GV/HKQ convention closure, CoHA consequence. |
| Abel--Jacobi normalisation | No fixture present. Planned path: `references/primary-sources/chiral-volume-abel-jacobi-normalization-source-anchors-2026-04-30.md`. | Absent. | Negative firewall only: CDGP raw period ratios are not Hodge-normalized Abel--Jacobi norms without `N_AJ`. | Any value of `N_AJ`, any equality between `|Omega_1/Omega_0|` and an Abel--Jacobi norm, any CoHA consequence. |
| Conifold/Stokes and resurgence | No fixture present. Planned path: `references/primary-sources/conifold-resurgence-stokes-source-anchors-2026-04-30.md`. | Absent. | Negative firewall only. CDGP supplies the conifold period/monodromy leg; HKQ supplies gap-boundary vocabulary; GV supplies Schwinger mechanism vocabulary. | `A_BCOV=A_Schwinger=A_period`, `S_c=1`, Strominger light-hypermultiplet normalisation, Vafa/Schwinger residue, Shenker--Marino large order, Cecotti--Codesido--Marino Stokes data, global resurgent sheaf, CoHA consequence. |

## Local Mirror Checksums

HKQ local mirrors:

```text
64cfea05d767d6fd07ded8a53fdb19771b9bcbf4789c6012506fb835cb973e2f  references/primary-sources/hkq-compact-cy-hep-th-0612125.pdf
26f95d4dbb5f0d8985023bb4e4353c3d882ec08e8fb7908732fc07ce6ff4910d  references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
26f95d4dbb5f0d8985023bb4e4353c3d882ec08e8fb7908732fc07ce6ff4910d  references/primary-sources/hkq-compact-cy-hep-th-0612125.txt
```

CDGP local mirrors:

```text
5c5033bfe291e9a8f77e1d6543aa9be9134681c93106c8258fe9375926d8d617  references/primary-sources/cdgp-nucl-phys-b359-1991.pdf
c07473e9a72595b712a839a8cd35c1938d04e3b5469be7e68a5604afe785cc9a  references/primary-sources/cdgp-nucl-phys-b359-1991.txt
```

GV local mirrors:

```text
864ed0b76d9889e14ac40d39a0d733b58f275f9239ba32220a882ad200a2578b  references/primary-sources/gv-hep-th-9809187.pdf
ddf1727d45b1def42ea9090af3c1301fd6c18af4af279dbf92a250040b9d5c16  references/primary-sources/gv-hep-th-9809187.tex
e67fa3fb642ba100444dbbb2bc81b41fee1361b56b677ff5c2354df409501749  references/primary-sources/gv-hep-th-9809187.txt
adb9fa3dc3966cf1d02a9d767ccceb1d7318303661f05cf43162d8a176b125c2  references/primary-sources/gv-hep-th-9812127.pdf
4687315b433ff4ec6ba753809d7ba7f8f48aff44276836faef80dde7c94b1650  references/primary-sources/gv-hep-th-9812127.tex
53521081494256978a8807658c71efe6e29499616ea6117cf1ceca5dcf9cad13  references/primary-sources/gv-hep-th-9812127.txt
```

OSV has no repository-local primary mirror.  The OSV fixture records
remote checksums from the inspected arXiv pass:

```text
9120c64fdf9c57bbb0fd3d1421295be9c25ac0b4889087524a7e86b2f2241a90  osv-v2.eprint
e9b25649b656597dae7f7ade2964700d399135b6ab555f44a88018f49b67405f  black.tex
c112f937de2d795722676958080bd709fc8cc8a0aa6f9af8add0027b35681faa  arXiv PDF hep-th/0405146v2
```

These OSV checksums are not local-mirror checksums until the files are
tracked under `references/primary-sources`.

## Lane Facts And Non-Support

### HKQ Compact BCOV/Quintic

Local anchors:

- `hkq-compact-cy-hep-th-0612125-ccy.tex:319-338`: conifold gap and
  holomorphic-ambiguity boundary condition.
- `hkq-compact-cy-hep-th-0612125-ccy.tex:1718-1739`: quintic
  ambiguity count and boundary constraints.
- `hkq-compact-cy-hep-th-0612125-ccy.tex:2317-2322`: Table 1 row
  `n^0_10=704288164978454686113488249750`.
- `hkq-compact-cy-hep-th-0612125-ccy.tex:2488-2506` and
  `:2680-2695`: boundary-determination claim through genus `51`,
  while explicit local text supports quintic invariants only to genus
  `20` plus an external higher-genus data webpage.

Admissible support.  HKQ supports finite compact-BCOV bootstrap source
facts and the `N=10` table row.  It does not prove the chiral-volume
limit, GV/PT integrality, convergence, a compact target object, or any
CoHA statement.  It also does not support the frontier phrase
`genus 22` from the local arXiv mirror alone.

Theorem-grade deciding evidence.  Mirror or replace the HKQ
higher-genus data webpage with a stable primary archive before using any
genus range beyond the local `genus 20 explicit data; genus 51 boundary
determination` distinction.

### CDGP Mirror-Quintic Periods

Local anchors:

- `cdgp-nucl-phys-b359-1991.txt:163-184` and `:275-282`:
  quintic family and true complex coordinate.
- `cdgp-nucl-phys-b359-1991.txt:313-328`, `:1201-1206`, and
  `:1968-1975`: conifold branch and shrinking cycle vocabulary.
- `cdgp-nucl-phys-b359-1991.txt:767-793` and `:804-836`:
  fundamental period and Picard--Fuchs mechanism.
- `cdgp-nucl-phys-b359-1991.txt:1023-1069`, `:1078-1115`,
  `:1778`, and `:2405`: integral period-basis/monodromy mechanism
  and the OCR-poor relation (3.23).
- `cdgp-nucl-phys-b359-1991.txt:1119-1179` and `:1643-1813`:
  prepotential and mirror-map mechanism.
- `cdgp-nucl-phys-b359-1991.txt:1332-1367`, `:1824-1832`, and
  `:1893-1953`: Yukawa instanton expansion and Table 4.

Admissible support.  CDGP supports the mirror-period/conifold/prepotential
source lane after translating CDGP's `psi` convention to
`z=(5 psi)^(-5)`, so the conifold branch gives `z_c=5^{-5}`.  The raw
period value `|Omega_1/Omega_0|(5^{-5})=7.590896...` is a local
arithmetic claim once the period convention is accepted; it is not a
CDGP source quotation.

OCR warning.  The local `cdgp-nucl-phys-b359-1991.txt` file is an OCR
navigation layer from a journal scan.  It is formula-poor.  Exact
formula transcription, especially relation (3.23) and any displayed
period-basis identity used in theorem-grade prose, is PDF-visual
required.  The local PDF, not the OCR text, controls glyph-level formula
checks.

Theorem-grade deciding evidence.  Before any CDGP formula is imported as
a theorem-grade identity, record a PDF-visual transcription with page
and equation anchors for the exact period vector, relation (3.23),
period-basis matrix, prepotential constants, and all `2 pi i`
normalisations.  A publisher or AMS/IP PDF mirror would strengthen
provenance; absent that, the Utrecht mirror checksum and PDF-visual
audit are the admissible local path.

### GV BPS/Sine Expansion

Local anchors:

- `gv-hep-th-9809187.tex:495-523`, `:560-569`, and `:708-736`:
  Schwinger determinant and non-perturbative pair-creation mechanism.
- `gv-hep-th-9812127.tex:120-147`: topological partition-function
  convention.
- `gv-hep-th-9812127.tex:395-418`, `:421-437`, and `:462-493`:
  BPS index and integer coefficients `alpha_r^(n_i)`.
- `gv-hep-th-9812127.tex:496-522`: sine multi-cover expansion with
  `1/k`, `(2 sin(k lambda/2))^(2r-2)`, and
  `exp[-2 pi k sum_i n_i t_i]`.
- `gv-hep-th-9812127.tex:524-535` and `:540-557`: physics-source
  integrality packaging and inductive extraction.

Admissible support.  GV supports the physics BPS interpretation and the
sine expansion in GV variables.  It does not prove theorem-grade
enumerative integrality, PT/GW equivalence, MNOP, KKV normalisation,
compact-quintic all-genus equality, convergence, or any CoHA/centre
statement.

Theorem-grade deciding evidence.  Fix the convention bridge
`alpha_r^(n_i)` versus `n_beta^g`, `k` versus `m`, class notation, the
`2 pi` in `exp[-2 pi k sum_i n_i t_i]`, the Wick-rotation convention,
and the constant-map sector.  Then import separate theorem-grade
PT/GW/MNOP/KKV sources before using GV coefficients as mathematical
integrality data.

### OSV Attractor/Mixed Ensemble

Remote anchors recorded in the OSV fixture:

- `black.tex:338-356` and `:363-364`: OSV conjectural comparison
  `Z_BH=|Z_top|^2`.
- `black.tex:522-594`: attractor equations and entropy normalisation.
- `black.tex:617-684`: corrected free energy and Legendre-transform
  normalisation.
- `black.tex:693-729`: mixed ensemble and the warning that the
  microcanonical entropy is not the mixed entropy except in a
  large-charge steepest-descent approximation.
- `black.tex:763-868`: topological-string normalisation.
- `black.tex:874-930`: heuristic derivation warning.
- `black.tex:1688-1801`: background-dependence and wall-crossing
  discussion.

Admissible support.  OSV currently supports remote-source physics
vocabulary only.  It is not local source-grade until the OSV PDF, TeX
source, and text extraction are tracked under `references/primary-sources`.
It does not source `5 log 5`; the OSV fixture records a negative search
for `5 log 5`, `log 5`, and `5\log` in `black.tex`.  The identity
`5 log 5=-log(5^{-5})` is a local arithmetic fact after accepting the
CDGP conifold coordinate, not an OSV entropy theorem.

Theorem-grade deciding evidence.  Import local OSV mirrors with
checksums and local line anchors; add a separate rate ledger deciding
whether `5 log 5` is only `-log z_c` or a primary physical rate from
another source; prove the variable bridge from OSV's
`(p, phi, C X, t^A, g_top)` to the CDGP/HKQ/GV/frontier variables.

### Abel--Jacobi Normalisation

Present support.  None, beyond the firewall that CDGP raw periods are
not Abel--Jacobi norms without a normalisation datum `N_AJ`.

Required fixture.  A theorem-grade Abel--Jacobi lane must supply:

- primary Hodge-theoretic source anchors for the Abel--Jacobi map and
  metric normalisation used here;
- the exact CDGP period basis and `2 pi i` convention against which the
  Abel--Jacobi period is compared;
- an explicit scalar `N_AJ`, or a proof that the proposed comparison is
  ill-posed;
- a local computation matching the selected basis, metric, monodromy,
  and period coordinate.

Until then, `|Omega_1/Omega_0|(z_c)` remains a raw mirror-period
quantity, not a Hodge-normalized Abel--Jacobi norm.

### Conifold/Stokes And Resurgence

Present support.  CDGP supplies conifold location, branch-period, and
monodromy source facts.  HKQ supplies conifold gap/boundary data.  GV
supplies Schwinger mechanism vocabulary.  These three facts do not imply
one another and do not produce a Stokes constant.

Required fixture.  A theorem-grade conifold/Stokes lane must supply
local primary anchors for:

- Strominger's light-hypermultiplet conifold mechanism and its period
  normalisation;
- the Vafa/Schwinger residue normalisation used by the BPS one-loop
  term;
- Shenker--Marino large-order constants in the topological-string
  setting;
- Cecotti--Codesido--Marino resurgence/Stokes data;
- the exact equality, if true, between `A_BCOV`, `A_Schwinger`, and
  `A_period` under one `2 pi i` convention;
- a proof or source that the local Stokes constant is `S_c=1`.

Until then, the conifold trinity and global resurgent sheaf are target
claims only.

## CoHA Exclusion Proposition

Proposition.  None of the six lanes above is supported by the
CoHA/centre fixture.

Proof.  The CoHA/centre fixture is restricted to Lurie centre grammar,
Joyce and Gross--Joyce--Tanaka Hall/vertex vocabulary, Joyce--Upmeier
orientation prerequisites, Kinjo--Park--Safronov 3CY CoHA vocabulary,
and Costello--Gwilliam factorization vocabulary used only to delimit
centre language.  HKQ, CDGP, GV, OSV, Abel--Jacobi normalisation, and
conifold/Stokes data require different primary sources and different
conventions.  No map in the present repository constructs compact
target data, trace maps, `sigma_X`, an `E_2` rigidity theorem, or an
`Ob_UKD(C_tar)` null-homotopy from CoHA.  Therefore any use of these
compact-CY facts as CoHA consequences is inadmissible.

## Residual Source Obligations

1. Add local OSV PDF, TeX source, and text extraction with checksums.
2. Add an Abel--Jacobi normalisation fixture or remove theorem-grade
   Abel--Jacobi comparisons.
3. Add a conifold/Stokes fixture with Strominger, Vafa/Schwinger,
   Shenker--Marino, and Cecotti--Codesido--Marino anchors.
4. Add a committed arithmetic ledger for `a_N`, tail fit, raw period
   evaluation, `5 log 5=-log(5^{-5})`, and error control.
5. Visually audit OCR-poor CDGP formulas before formula-level theorem
   use.
6. Keep all compact-CY source facts outside the CoHA/centre stable core.
