# Gopakumar--Vafa BPS Source Anchors, 2026-04-30

Scope. This fixture records the Gopakumar--Vafa source lane for the
BPS interpretation of topological-string amplitudes and the sine
multi-cover expansion. It is separated from CoHA, Hall, and centre
language. It supplies stable primary identifiers, local source anchors,
exact convention obligations, and non-support statements. It does not
close a theorem in `main.tex`.

Local status. GV I/II are mirrored under `references/primary-sources` as
PDF files, arXiv TeX source streams, and PDF-derived text extractions.
The line anchors below are repository-local TeX-source anchors. The
fixture supplies source-grade support for the GV physics facts listed
here, not theorem-grade support for integrality, PT/GW, MNOP, KKV,
convergence, CDGP periods, or conifold Stokes constants.

Controller lane: `GlobDesc`, source-fixture sublane
`Gopakumar--Vafa BPS`.

## Stable Primary Identifiers

| Source key | Identifier | Status |
|---|---|---|
| `GV-I` | Rajesh Gopakumar and Cumrun Vafa, "M-Theory and Topological Strings--I" | Primary source mirrored locally. |
| arXiv | `hep-th/9809187`, submitted 1998-09-25, report `HUTP-98/A069` | Stable remote identifier. Local mirror present. |
| arXiv DOI | `10.48550/arXiv.hep-th/9809187` | Stable remote identifier. |
| arXiv source payload | `https://arxiv.org/e-print/hep-th/9809187`, gzip single TeX source with original name `9809187.tex` | Mirrored as `references/primary-sources/gv-hep-th-9809187.tex`. |
| `GV-II` | Rajesh Gopakumar and Cumrun Vafa, "M-Theory and Topological Strings--II" | Primary source mirrored locally. |
| arXiv | `hep-th/9812127`, submitted 1998-12-15, report `HUTP-98/A070` | Stable remote identifier. Local mirror present. |
| arXiv DOI | `10.48550/arXiv.hep-th/9812127` | Stable remote identifier. |
| arXiv source payload | `https://arxiv.org/e-print/hep-th/9812127`, gzip single TeX source with original name `mth2.tex` | Mirrored as `references/primary-sources/gv-hep-th-9812127.tex`. |

## Local Mirror Ledger

The arXiv e-print payloads were single gzipped TeX streams, not
multi-file bundles. GV I's original source name is `9809187.tex`; GV II's
original source name is `mth2.tex`. They are mirrored under stable local
filenames with matching local line anchors.

| File | Local role | SHA-256 |
|---|---|---|
| `references/primary-sources/gv-hep-th-9809187.pdf` | GV I arXiv PDF mirror, 15 pages. | `864ed0b76d9889e14ac40d39a0d733b58f275f9239ba32220a882ad200a2578b` |
| `references/primary-sources/gv-hep-th-9809187.tex` | GV I arXiv TeX source stream. | `ddf1727d45b1def42ea9090af3c1301fd6c18af4af279dbf92a250040b9d5c16` |
| `references/primary-sources/gv-hep-th-9809187.txt` | GV I PDF text extraction by `pdftotext -layout`. | `e67fa3fb642ba100444dbbb2bc81b41fee1361b56b677ff5c2354df409501749` |
| `references/primary-sources/gv-hep-th-9812127.pdf` | GV II arXiv PDF mirror, 20 pages. | `adb9fa3dc3966cf1d02a9d767ccceb1d7318303661f05cf43162d8a176b125c2` |
| `references/primary-sources/gv-hep-th-9812127.tex` | GV II arXiv TeX source stream. | `4687315b433ff4ec6ba753809d7ba7f8f48aff44276836faef80dde7c94b1650` |
| `references/primary-sources/gv-hep-th-9812127.txt` | GV II PDF text extraction by `pdftotext -layout`. | `53521081494256978a8807658c71efe6e29499616ea6117cf1ceca5dcf9cad13` |

Local import commands:

```bash
curl -L --fail --silent --show-error https://arxiv.org/pdf/hep-th/9809187 -o references/primary-sources/gv-hep-th-9809187.pdf
curl -L --fail --silent --show-error https://arxiv.org/pdf/hep-th/9812127 -o references/primary-sources/gv-hep-th-9812127.pdf
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/9809187 | gunzip -c > references/primary-sources/gv-hep-th-9809187.tex
curl -L --fail --silent --show-error https://arxiv.org/e-print/hep-th/9812127 | gunzip -c > references/primary-sources/gv-hep-th-9812127.tex
pdftotext -layout references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.txt
pdftotext -layout references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.txt
shasum -a 256 references/primary-sources/gv-hep-th-9809187.pdf references/primary-sources/gv-hep-th-9809187.tex references/primary-sources/gv-hep-th-9809187.txt references/primary-sources/gv-hep-th-9812127.pdf references/primary-sources/gv-hep-th-9812127.tex references/primary-sources/gv-hep-th-9812127.txt
```

The line anchors below refer to the local TeX mirrors.

## Local Source Facts

| Fact ID | Local anchor | Source fact captured | Claim anchors affected | Local status |
|---|---|---|---|---|
| `GV-I-id` | arXiv abstract page `https://arxiv.org/abs/hep-th/9809187`; `references/primary-sources/gv-hep-th-9809187.tex:7-10`; `:19-38` | GV I identifies the all-genus topological-string amplitudes with an M-theory Schwinger one-loop computation involving wrapped M2 branes and Kaluza--Klein modes; the paper treats constant maps and the isolated sphere case. | `frontier_mnop_framing_volume.tex:585-597`; `:655-673`. | Stable local source fact. |
| `GV-I-Schwinger-nonperturbative` | `references/primary-sources/gv-hep-th-9809187.tex:495-523`; `:560-569`; conclusion `:708-736` | The Schwinger determinant is used as a physical source for perturbative and non-perturbative contributions, including pair creation for bound states of 2-branes and 0-branes in a graviphoton field. | `frontier_mnop_framing_volume.tex:593-597`; `:661-690`. | Local source fact for the physical Schwinger mechanism only. It does not fix conifold residue normalisation or Stokes data. |
| `GV-II-id` | arXiv abstract page `https://arxiv.org/abs/hep-th/9812127`; `references/primary-sources/gv-hep-th-9812127.tex:7-10`; `:19-27` | GV II states the BPS interpretation: topological-string amplitudes encode the wrapped-M2 BPS structure, via a five-dimensional twisted supersymmetric index receiving BPS contributions. | `frontier_mnop_framing_volume.tex:585-597`; `:607-620`; `:812-817`. | Stable local source fact. |
| `GV-II-topological-partition-function` | `references/primary-sources/gv-hep-th-9812127.tex:120-147`; `:135-146` | The topological partition function is written as `F(lambda,t_i)=sum_g lambda^(2g-2) F_g(t_i)`, after the graviphoton convention `lambda=g_s F`. | `frontier_mnop_framing_volume.tex:571-575`; `:743-745`. | Local source fact. Needs convention reconciliation before theorem use. |
| `GV-II-BPS-index` | `references/primary-sources/gv-hep-th-9812127.tex:395-418`; `:421-437`; `:462-493` | The relevant five-dimensional BPS states are arranged by curve class and left spin; the source uses integer coefficients `alpha_r^(n_i)` in the basis `I_r`. | `frontier_mnop_framing_volume.tex:593`; `:607-620`. | Local physics-source fact. It supports the BPS-index interpretation of integer coefficients, not a mathematical GV-integrality theorem. |
| `GV-II-sine-expansion` | `references/primary-sources/gv-hep-th-9812127.tex:496-522` | The final formula is a sine multi-cover expansion: sum over curve class `(n_i)`, spin index `r >= 0`, and cover `k > 0`, with coefficient `alpha_r^(n_i)`, factor `1/k`, factor `(2 sin(k lambda/2))^(2r-2)`, and exponential `exp[-2 pi k sum_i n_i t_i]`. | `frontier_mnop_framing_volume.tex:585-592`; `:607-620`; `:727-745`. | Local source fact for the formula, conditional on the convention ledger below. |
| `GV-II-integrality-physics` | `references/primary-sources/gv-hep-th-9812127.tex:524-535`; `:540-557` | GV II says the sine formula packages the integrality properties in terms of the integer BPS-index coefficients and gives an inductive extraction pattern from fixed-genus amplitudes. | `frontier_mnop_framing_volume.tex:593`; `:617-620`; `:638-646`. | Local physics-source fact. It does not prove PT/GW, MNOP, KKV, or mathematical integrality for Gromov--Witten invariants. |
| `GV-II-geometric-BPS-counting` | `references/primary-sources/gv-hep-th-9812127.tex:573-580`; `:688-710`; `:762-824`; `:864-994` | GV II sketches how wrapped M2/D2 branes over genus-`g` curves and multiwrapped branes should produce the coefficients through cohomology and Lefschetz-type decompositions. | `frontier_mnop_framing_volume.tex:607-620`; `:638-646`; `:717-723`. | Local physical/geometric proposal. It is not a source for a compact-quintic all-genus theorem or convergence. |

## Formula Convention Ledger

The inspected GV II source supports this formula in its own variables:

```tex
F(lambda) =
  sum_{(n_i), r >= 0, k > 0}
    alpha_r^(n_i) (1/k)
    (2 sin(k lambda / 2))^(2r-2)
    exp[-2 pi k (sum_i n_i t_i)].
```

The frontier note writes instead

```tex
F^GV(lambda,t) =
  sum_{beta > 0} sum_{g >= 0} n_beta^g
  sum_{m >= 1} (1/m)
    (2 sin(m lambda / 2))^(2g-2)
    exp[-m beta dot t].
```

Convention obligations before theorem use:

1. identify `r` with the genus label `g` only after fixing the BPS-index
   basis convention;
2. identify the class `(n_i)` with `beta`;
3. identify the cover variable `k` with `m`;
4. either set `beta dot t_frontier = 2 pi sum_i n_i t_i^GV` or retain the
   explicit `2 pi` in the frontier formula;
5. record the Wick-rotation convention from GV II, where
   `lambda -> i lambda` is made before the final sine formula;
6. treat constant maps and the `beta=0` sector as separate source data.

Until these six items are fixed in the theorem lane, the frontier
formula is source-compatible but not convention-closed.

## Claim-To-Source Map

| Frontier anchor | Claim shape | GV fixture status |
|---|---|---|
| `frontier_mnop_framing_volume.tex:585-592` | GV sine expansion with `1/m`, `2 sin(m lambda/2)`, and `exp(-m beta dot t)`. | Locally supported by `GV-II-sine-expansion`, except for the missing `2 pi`/Kahler-coordinate convention and the notation change from `alpha_r^(n_i)` to `n_beta^g`. |
| `frontier_mnop_framing_volume.tex:593` | `n_beta^g in Z` as BPS invariants. | GV II supports integer BPS-index coefficients `alpha_r^(n_i)` as physics-source data. Mathematical integrality of enumerative invariants requires separate PT/GW/KKV/MNOP-grade support and is not supplied here. |
| `frontier_mnop_framing_volume.tex:593-597` | Fixed-`beta` summands resum perturbative genera and have Schwinger-pole physics. | The all-genus BPS contribution and Schwinger mechanism are locally supported. Exact pole-residue and electric--magnetic pair-production normalisation are not closed by GV I/II alone. |
| `frontier_mnop_framing_volume.tex:607-620` | Equality between BCOV amplitudes and coefficients of the GV expansion, with integrality after KKV normalisation. | GV supplies the physics formula and BPS-index package only. HKQ, CDGP, PT/GW, and KKV normalisation remain separate source obligations. |
| `frontier_mnop_framing_volume.tex:623-627` | Nonempty convergence domain for the genus-zero BPS series. | No support in GV I/II found. This remains an asymptotic/convergence obligation. |
| `frontier_mnop_framing_volume.tex:628-634` | Conifold Stokes target and `A=2 pi i tau_c`. | No support in this fixture beyond the general Schwinger mechanism. Strominger, Vafa/Schwinger, Shenker--Marino, Cecotti--Codesido--Marino, and CDGP rows are required. |
| `frontier_mnop_framing_volume.tex:638-646` | Verification path through PT/GW, HKQ, CDGP, and GV. | GV part is source-routed. PT/GW, HKQ, and CDGP remain outside this fixture. |
| `frontier_mnop_framing_volume.tex:727-756` | Genus-zero prepotential extracted from the GV expansion should recover the CDGP period expression. | GV supports the `lambda^{-2}` extraction vocabulary after convention matching. It does not source the CDGP period basis, Picard--Fuchs operator, mirror map, or prepotential identity. |
| `frontier_mnop_framing_volume.tex:812-817` | Non-perturbative closure remains conjectural; convergence and global resurgent sheaf remain residual. | Supported as a firewall status: GV supplies a local physics source schema, not convergence or global Stokes closure. |

## Exact Non-Support Statements

This fixture does not support:

1. A mathematical proof that the GV/BPS integers exist for every compact
   Calabi--Yau threefold.
2. PT/GW equivalence, MNOP theorem-grade support, KKV normalisation, or
   any theorem identifying the source coefficients with GW invariants.
3. Compact-quintic all-genus BCOV amplitudes or equality
   `[lambda^(2g-2)]F^GV = F_g^BCOV` as a theorem.
4. HKQ finite-genus data, the `genus 22` wording, or the `N=10` row.
5. CDGP period conventions, the raw mirror-period ratio, or the
   Picard--Fuchs/prepotential normalisation used in the frontier note.
6. Abel--Jacobi normalisation or an `N_AJ` value.
7. OSV attractor-rate normalisation or the `5 log 5` comparison.
8. Strominger conifold light-hypermultiplet matching, Vafa/Schwinger
   residue normalisation, Shenker--Marino large-order constants,
   Cecotti--Codesido--Marino Stokes constants, or `S_c=1`.
9. Convergence of the genus-zero BPS series, Borel summability, or a
   global resurgent sheaf on the quintic moduli space.
10. A compact target object `C_tar`, trace map, centre automorphism,
    rigidity theorem, or `Ob_UKD(C_tar)=0`.
11. Any Hall, CoHA, or `E_2`-centre claim. Those vocabularies remain in
    their own fixtures and provide no support for GV BPS source facts.

## Completed Import And Remaining Obligations

Completed local import:

1. Added local GV I/II PDF, TeX source, and PDF-derived text mirrors.
2. Preserved the single-file arXiv TeX payloads `9809187.tex` and
   `mth2.tex` as `gv-hep-th-9809187.tex` and `gv-hep-th-9812127.tex`.
3. Recorded SHA-256 checksums for the imported PDF/source/text files.
4. Re-anchored the GV I Schwinger determinant and pair-creation claims,
   the GV II BPS index, the sine formula, the integer-coefficient
   statement, and the geometric BPS-counting proposal to local TeX lines.

Remaining source and convention obligations:

1. Decide and record the Kähler convention: either absorb `2 pi` into
   `t` or keep `exp[-2 pi k beta dot t]` explicitly.
2. Decide and record the relation between GV's `alpha_r^(n_i)` and the
   frontier notation `n_beta^g`; do not silently identify them in a
   theorem statement.
3. Keep the `beta=0` constant-map sector outside the positive-class GV
   sine formula unless a separate source row is imported.
4. Import or cite separate theorem-grade sources before promoting
   mathematical integrality, PT/GW, convergence, CDGP period recovery,
   or conifold Stokes claims.

## Fixture Status

Supported now: stable GV I/II identifiers; local PDF/source/text mirrors;
local TeX-source anchors for the BPS interpretation, Schwinger mechanism,
sine multi-cover formula, integer BPS-index coefficients, and convention
obligations.

Not supported now: theorem-grade GV integrality; PT/GW/MNOP/KKV;
compact-quintic all-genus BCOV equality; CDGP/OSV/Abel--Jacobi/Stokes
normalisations; convergence; or any compact target/null-homotopy
statement.
