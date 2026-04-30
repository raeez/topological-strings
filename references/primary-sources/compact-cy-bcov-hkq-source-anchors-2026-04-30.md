# Compact-CY BCOV/HKQ Source Anchors, 2026-04-30

Scope. This fixture records the Huang--Klemm--Quackenbush compact
Calabi--Yau source lane for the quintic BCOV bootstrap. It is a
non-CoHA fixture. It supplies stable primary identifiers, remote source
anchors inspected in the arXiv source stream, exact import obligations,
and non-support statements. It does not close a theorem in `main.tex`.

Local status. The HKQ arXiv PDF, TeX source, and text extraction are now
present under `references/primary-sources`:

- `references/primary-sources/hkq-compact-cy-hep-th-0612125.pdf`
- `references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex`
- `references/primary-sources/hkq-compact-cy-hep-th-0612125.txt`

The line anchors below are repository-local source anchors into the
imported `ccy.tex` mirror.  This upgrades the HKQ table row and
boundary/gap citations to local source support.  It does not close any
compact-CY theorem in `main.tex`.

Controller lane: `GlobDesc`, source-fixture sublane
`compact-CY BCOV/HKQ`.

## Stable Primary Identifiers

| Source key | Identifier | Status |
|---|---|---|
| `HKQ-compact-CY` | Min-xin Huang, Albrecht Klemm, Seth Quackenbush, "Topological String Theory on Compact Calabi-Yau: Modularity and Boundary Conditions" | Primary target. |
| arXiv | `hep-th/0612125`, submitted 2006-12-13, source bundle containing `ccy.tex`, `castelnouvo.eps`, `contour.eps` | Stable identifier. PDF and `ccy.tex` mirror present locally. |
| arXiv DOI | `10.48550/arXiv.hep-th/0612125` | Stable remote identifier. |
| Published chapter | Lecture Notes in Physics 757, `Homological Mirror Symmetry`, pp. 45--102, 2009 | Stable bibliographic identifier. |
| Springer DOI | `10.1007/978-3-540-68030-7_3` | Stable published identifier. |

Local import command used for this fixture:

```bash
curl -L -sS https://arxiv.org/pdf/hep-th/0612125 \
  -o references/primary-sources/hkq-compact-cy-hep-th-0612125.pdf
curl -L -sS https://arxiv.org/e-print/hep-th/0612125 \
  -o /tmp/hkq-src.tar.gz
tar -xzf /tmp/hkq-src.tar.gz -C /tmp/hkq-src
cp /tmp/hkq-src/ccy.tex \
  references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex
cp references/primary-sources/hkq-compact-cy-hep-th-0612125-ccy.tex \
  references/primary-sources/hkq-compact-cy-hep-th-0612125.txt
```

Checksums:

```text
64cfea05d767d6fd07ded8a53fdb19771b9bcbf4789c6012506fb835cb973e2f  hkq-compact-cy-hep-th-0612125.pdf
26f95d4dbb5f0d8985023bb4e4353c3d882ec08e8fb7908732fc07ce6ff4910d  hkq-compact-cy-hep-th-0612125-ccy.tex
26f95d4dbb5f0d8985023bb4e4353c3d882ec08e8fb7908732fc07ce6ff4910d  hkq-compact-cy-hep-th-0612125.txt
```

## Remote Source Facts

| Fact ID | Local anchor | Source fact captured | Claim anchors affected | Status |
|---|---|---|---|---|
| `HKQ-id` | local PDF `hkq-compact-cy-hep-th-0612125.pdf`; arXiv abstract `https://arxiv.org/abs/hep-th/0612125`; Springer chapter `https://link.springer.com/10.1007/978-3-540-68030-7_3` | The paper is the HKQ compact Calabi--Yau BCOV/modularity source: Huang, Klemm, Quackenbush; arXiv `hep-th/0612125`; LNP 757; DOI `10.1007/978-3-540-68030-7_3`. | `frontier_mnop_framing_volume.tex:127-131`; `:597-620`; `:778-798`. | Stable identifier and local mirror present. |
| `HKQ-gap-condition` | `hkq-compact-cy-hep-th-0612125-ccy.tex:319-338` | The holomorphic anomaly recursion leaves a holomorphic ambiguity; the conifold gap has leading term `(-1)^{g-1} B_{2g}/(2g(2g-2)t_D^{2g-2})` and vanishing of the following `2g-3` negative powers; orbifold regularity gives additional boundary conditions. | `frontier_mnop_framing_volume.tex:605-608`; `:621-633`; `:812-817`. | Local source fact. |
| `HKQ-quintic-boundary-count` | `hkq-compact-cy-hep-th-0612125-ccy.tex:1718-1739` | For the quintic ambiguity count: starting from `3g-2` coefficients, the constant-map term fixes one, the conifold fixes `2g-2`, and the orbifold fixes `ceil(3(g-1)/5)`, leaving `floor(2(g-1)/5)`. HKQ state this plus Castelnuovo bounds can fix `F^{(g)}` up to genus `51`. | `frontier_mnop_framing_volume.tex:597-620`; `:645-650`; `:812-817`. | Local source fact. |
| `HKQ-quintic-table-N10` | `hkq-compact-cy-hep-th-0612125-ccy.tex:2280-2344`, especially `:2317-2322`; table caption `:2342` | HKQ Table 1 lists BPS invariants `n^g_d` on the quintic. The `g=0`, `d=10` row is `704288164978454686113488249750`, matching the displayed `n_{10}` in the frontier note. | `frontier_mnop_framing_volume.tex:247-270`; `:296-324`; `:790-800`. | Local source fact for the table row. Not a theorem proof of the chiral-volume or compact-target claims. |
| `HKQ-genus-51-boundary-data` | `hkq-compact-cy-hep-th-0612125-ccy.tex:2488-2506`; conclusion `:2680-2695` | HKQ claim the boundary-condition count plus large-volume vanishing fixes quintic amplitudes up to genus `51`; the same conclusion says explicit invariants were calculated for the quintic to genus `20` and points to an external higher-genus-data webpage. | `frontier_mnop_framing_volume.tex:609-621`; `:768-771`; `:812-817`. | Local source fact and discrepancy trigger. The frontier phrase "genus 22" is not supported by the imported arXiv source alone. |
| `HKQ-highergenus-webpage` | `hkq-compact-cy-hep-th-0612125-ccy.tex:3893` | HKQ cite `http://uw.physics.wisc.edu/~strings/aklemm/highergenusdata/` for detailed higher-genus data. | `frontier_mnop_framing_volume.tex:609-621`; `:768-771`. | Not stable enough for theorem support until mirrored or replaced by a stable archived primary source. |

## N=10 Row Status

The `N=10` row is present in the remote HKQ arXiv source as the genus-zero
BPS invariant `n^0_{10}` for the quintic:

```text
n^0_10 = 704288164978454686113488249750.
```

It matches `frontier_mnop_framing_volume.tex:270`. The row is now
repository-local source-grade for the HKQ table entry because the arXiv
source has been mirrored and text-extracted. It is a BPS/table source
fact only; it is not a proof of the chiral-volume limit, Abel--Jacobi
normalisation, OSV rate, convergence, or non-perturbative completion.

## Boundary And Gap Conditions

The HKQ boundary package, as remotely inspected, consists of:

- BCOV holomorphic anomaly recursion plus a finite holomorphic ambiguity.
- Conifold gap: one leading pole of order `2g-2` in the flat conifold
  coordinate `t_D`, followed by vanishing of the next `2g-3` negative
  powers.
- Orbifold regularity near the Gepner/orbifold point.
- Constant-map input at large radius.
- Castelnuovo-bound and large-volume vanishing constraints used to fix
  the remaining quintic ambiguity through a finite genus range.

For the quintic, HKQ's explicit count leaves `floor(2(g-1)/5)` coefficients
after constant-map, conifold, and orbifold conditions. HKQ then use
large-volume vanishing/Castelnuovo input to claim determination up to
genus `51`.

## Genus-Range Status

Remote HKQ source support is not identical to the current frontier wording.

| Frontier wording | HKQ source status from arXiv source stream |
|---|---|
| `computed ... through genus 22` | Not supported by the inspected arXiv source alone. |
| finite boundary data up to genus `51` | Supported by the imported boundary-count discussion and conclusion. |
| explicit quintic invariants to high genus | Supported locally only as "to genus `20`" plus a cited external webpage. |

Remaining import obligation: mirror the published chapter or a stable archive
of the higher-genus data before any `genus 22` statement is treated as
source-grade.  If no such source is found, the frontier note should say
`genus 20 explicit data; genus 51 boundary determination claim`, or should
keep the genus range as an open source obligation.

## Claim-To-Source Map

| Frontier anchor | Claim shape | HKQ fixture status |
|---|---|---|
| `frontier_mnop_framing_volume.tex:127-131` | PT/GW finite-genus target evidence after HKQ row supplied. | HKQ identifier and remote boundary package are recorded. PT/GW comparison and KKV integrality are not supplied by this fixture. |
| `frontier_mnop_framing_volume.tex:247-270` | Quintic genus-zero table through `N=10`. | BCOV fixture supports `N<=9`; imported HKQ source supports the `N=10` table row. |
| `frontier_mnop_framing_volume.tex:296-324` | Conditional arithmetic through `N=10`. | HKQ is now local source support for the input `n^0_{10}` row; the arithmetic still needs a committed numerical ledger/script before promotion. |
| `frontier_mnop_framing_volume.tex:597-620` | BCOV/GV closure with HKQ finite-genus evidence. | HKQ supplies compact-BCOV boundary/gap machinery and finite tables, not GV closure or convergence. The `genus 22` number remains unsupported by the inspected arXiv source alone. |
| `frontier_mnop_framing_volume.tex:778-798` | Honest-status summary naming HKQ finite-genus evidence and `N=10`. | The `N=10` source row is locally anchored; compact-CY closure remains unsupported. |

## Exact Non-Support Statements

This fixture does not support:

1. Any all-genus compact quintic theorem.
2. The Gopakumar--Vafa sine expansion as a source fact; GV I/II remain
   separate fixture obligations.
3. PT/GW equivalence, KKV integrality, or MNOP theorem-grade support.
4. CDGP period conventions, the raw period ratio, or the Picard--Fuchs
   normalisation used in the frontier note.
5. Abel--Jacobi normalisation or an `N_AJ` value.
6. OSV attractor-rate normalisation or the `5 log 5` comparison.
7. Strominger/Vafa/Schwinger/Shenker--Marino/Cecotti--Codesido--Marino
   conifold-resurgence or Stokes normalisation.
8. Convergence of the genus-zero BPS series or Borel/Stokes summability.
9. A compact target object `C_tar`, trace map, centre automorphism,
   rigidity theorem, or `Ob_UKD(C_tar)=0`.

No Hall, centre, or CoHA input is used here. Those vocabularies remain in
their own fixture and provide no support for the HKQ numerical rows.

## Import Obligations

1. Locate a stable source for the higher-genus data webpage. If none exists,
   mark that webpage as unavailable and do not use it for theorem support.
2. Reconcile the frontier's `genus 22` wording against the imported HKQ
   source or a separate stable source.
3. Add the published Springer chapter mirror if exact published-page
   references are later needed instead of arXiv-source line anchors.

## Fixture Status

Supported now: stable HKQ identifiers; local source row for `n^0_{10}`;
local HKQ boundary/gap condition anchors; exact remaining import
obligations; non-support firewall.

Not supported now: `genus 22`, GV closure, PT/GW theorem support,
CDGP/OSV/Abel--Jacobi/Stokes normalisations, convergence, or any compact
target/null-homotopy statement.
