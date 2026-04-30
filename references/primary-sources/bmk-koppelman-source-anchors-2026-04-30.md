# BMK / Koppelman Source Anchors, 2026-04-30

Agent: 268.

Scope: primary-source fixture for the Bochner--Martinelli,
Bochner--Martinelli--Koppelman, Koppelman, and Dolbeault homotopy kernel
statements used or alluded to by the local mixed holomorphic-topological
manuscript.  The fixture only supports external several-complex-variables
kernel identities after their hypotheses are checked.  It does not replace
the internal mixed-HT BV/QME/factorization/current construction.

Verdict: the modern kernel definition and component dbar identity are
anchored exactly in Laurent-Thiebaut 2011, Chapter III, Definition 1.2,
equation (1.1), and Lemma 1.3, pages 57-58, verified from the official
Springer preview.  A modern exact Koppelman homotopy formula is anchored
in Ruppenthal 2008/2009 arXiv v2, Section 5, Definition 5.1 and Theorem
5.2, with final journal metadata verified separately by Crossref.  The
historical Martinelli, Bochner, and Koppelman sources are verified at
metadata level only, except for DOI/page metadata where stated; their
internal theorem/equation anchors remain unverified until the original
scans are inspected.

## Source Metadata Register

| ID | Source | Verified metadata | Exact internal anchor status |
|---|---|---|---|
| `Martinelli38` | Enzo Martinelli, "Alcuni teoremi integrali per le funzioni analitiche di piu variabili complesse", reported as `Mem. R. Accad. d'Italia, Cl. Sci. Fis. Mat. Nat.` 9 (1938), 269-283. | Historical citation appears in the local missing-source plan and in secondary reference lists.  Crossref search did not locate a DOI or primary record. | Anchor still unverified.  No theorem, page scan, formula, or title typography has been checked against the primary article.  Use as lineage only. |
| `Bochner43` | S. Bochner, "Analytic and Meromorphic Continuation by Means of Green's Formula", `Annals of Mathematics` 44(4), Oct. 1943, DOI `10.2307/1969103`, JSTOR stable record. | Crossref verified title, journal, volume, issue, month, year, DOI, and first page `652`; Koppelman/Lieb references give page range 652-673. | Anchor still unverified for the Green-formula kernel statement; JSTOR access produced an access-check page.  Use as historical Green-formula lineage only. |
| `Koppelman67-forms` | Walter Koppelman, "The Cauchy integral for differential forms", `Bull. Amer. Math. Soc.` 73(4) (1967), 554-556, DOI `10.1090/s0002-9904-1967-11744-0`. | Crossref and AMS metadata verified: author, title, journal, volume, issue, year, pages, DOI, AMS URL. | Anchor still unverified for exact formula/theorem location; AMS PDF fetch returned Cloudflare 403.  Use as historical source for the differential-form Koppelman formula only after scan inspection. |
| `Koppelman67-functions` | Walter Koppelman, "The Cauchy integral for functions of several complex variables", `Bull. Amer. Math. Soc.` 73(3) (1967), 373-377, DOI `10.1090/s0002-9904-1967-11757-9`. | Crossref and AMS metadata verified.  Crossref reference list includes Bochner 1943 and other classical integral-formula sources. | Anchor still unverified for formula details; AMS PDF fetch returned Cloudflare 403.  Use as historical function-case lineage only. |
| `Range86` | R. Michael Range, `Holomorphic Functions and Integral Representations in Several Complex Variables`, GTM 108, Springer New York, 1986, DOI `10.1007/978-1-4757-1918-5`. | Springer book page and Crossref verified title, author, publisher, year, eISBN, print ISBNs, and 392-page book metadata.  Springer Chapter IV page verified "Integral Representations in C^n", pp. 144-190, DOI `10.1007/978-1-4757-1918-5_4`. | Exact theorem/equation anchors in Chapter IV, Section 1 are still unverified.  Official preview verified pp. 144-145 only, including the section heading "The Bochner-Martinelli-Koppelman Formula" and the stated scope: representation formulas for differential forms on domains with piecewise `C^1` boundary. |
| `LaurentThiebaut11` | Christine Laurent-Thiebaut, "III The Bochner-Martinelli-Koppelman kernel and formula and applications", in `Holomorphic Function Theory in Several Variables`, Universitext, Springer London, 2011, pp. 57-73, DOI `10.1007/978-0-85729-030-4_3`. | Springer chapter page and Crossref verified chapter title, author, book title, pages, publisher, year, DOI, print ISBN, and eISBN.  Official preview verified pp. 57-58. | Exact verified anchor for the BMK kernel: Definition 1.2, equation (1.1), p. 58.  Exact verified anchor for the component dbar identity: Lemma 1.3, p. 58.  The later full representation formula is not visible in the preview and remains anchor still unverified in this source. |
| `LiebMichel02` | Ingo Lieb and Joachim Michel, "The Bochner-Martinelli-Koppelman Formula", in `The Cauchy-Riemann Complex, Integral Formulae and Neumann Problem`, Vieweg+Teubner Verlag, 2002, pp. 9-57, DOI `10.1007/978-3-322-91608-2_2`. | Springer chapter page and Crossref verified chapter title, authors, book title, pages, publisher, year, DOI, print ISBN, eISBN.  Official preview verified pp. 9-10 and the chapter-level BMK scope. | Exact theorem/equation anchors remain unverified; full chapter PDF required authentication.  Crossref references verify that this chapter cites Martinelli, Bochner, Koppelman, and Range. |
| `Ruppenthal08v2-11` | Jean Ruppenthal, "Friedrichs' extension lemma with boundary values and applications in complex analysis", arXiv:0803.0092v2, updated 2009-10-14; final journal metadata: `Complex Variables and Elliptic Equations` 56(5) (2011), 423-437, DOI `10.1080/17476931003728388`. | arXiv API verified title, author, v2 date, 20-page length, and abstract.  Crossref verified final journal title, volume, issue, year, pages, DOI, and references including Koppelman 1967 and Lieb--Michel. | Exact verified arXiv anchors: Section 5, Definition 5.1 (`defn:kq`), p. 14 of the arXiv PDF, defines `B_{nq}`; Theorem 5.2 (`thm:bmk-formel`) and equation (10) / `eq:bmk`, pp. 14-15, state the classical BMK formula for `C^1` forms on bounded `C^1` domains; Theorem 5.6 (`thm:bmklp`), p. 19, gives an `L^p` weak-boundary version.  Final journal theorem placement has not been separately checked. |
| `HenkinLeiterer` | Henkin--Leiterer modern integral-formula references. | Not checked in this pass. | Anchor still unverified.  Do not cite for this manuscript until exact source, theorem, and hypotheses are loaded. |

## Anchor Register

### `BMK-Kernel-Normalization`

Verified external anchor:

- `LaurentThiebaut11`, Chapter III, Definition 1.2, equation (1.1),
  p. 58 of the official Springer preview, defines the
  Bochner--Martinelli--Koppelman kernel with the standard
  `(n-1)!/(2 i pi)^n` normalization on the complement of the diagonal in
  `C^n x C^n`.
- `Ruppenthal08v2-11`, Section 5, Definition 5.1, p. 14 of the arXiv
  PDF/source, defines the component kernels `B_{nq}` in `C^n`.

Hypotheses and content:

- Source identity is an external several-complex-variables kernel
  statement on `C^n`, away from the diagonal, with smooth forms in the
  classical formula.
- In complex dimension `n=2`, the standard full BMK kernel specializes
  to a denominator `||zeta-z||^4` and a two-term anti-holomorphic
  numerator.  Translating exactly to the manuscript convention
  `(2 pi i)^(-2) (bar eta_1 dbar eta_2 - bar eta_2 dbar eta_1)
  / r^4 wedge dzeta_1 wedge dzeta_2` requires the manuscript's
  orientation, `dbar eta`, and component-order conventions.

Supported manuscript use:

- External support for the full BMK kernel family and its normalization
  class in the finite-window construction around `main.tex:1271-1283`
  and `appendix-factorization-current-conventions.tex:410-426`.
- External support that the `dbar z`-containing terms belong to the full
  differential-form kernel, so deleting them is a scalar/contact
  projection, not the BMK form kernel.

Non-support:

- Does not prove the cutoff current limit `H_chi`, the finite-window
  moment projection `p_N`, support-at-zero currents, or collar quotient.
- Does not prove any BV propagator or Costello graph realization.

### `BMK-Component-dbar-Identity`

Verified external anchor:

- `LaurentThiebaut11`, Chapter III, Lemma 1.3, p. 58 of the official
  Springer preview, gives the kernel closedness and component
  `dbar_z`/`dbar_zeta` identity for the BMK kernel components.

Hypotheses and content:

- The identity is stated for the BMK kernel on the complement of the
  diagonal in the product space.
- It is a differential-form identity before cutoff, extension across the
  diagonal, or current regularization.

Supported manuscript use:

- External support for the local algebraic step that the uncut kernel
  has the Koppelman differential relation needed before the manuscript's
  cutoff and finite-window current operations.

Non-support:

- Does not establish the distributional equation with the diagonal
  current under the manuscript's specific cutoff, nor the collar error
  `E_{chi,N}`.

### `Koppelman-Homotopy-Formula`

Verified modern anchor:

- `Ruppenthal08v2-11`, Section 5, Theorem 5.2 (`thm:bmk-formel`) and
  equation (10) / `eq:bmk`, pp. 14-15 of the arXiv PDF/source.  It
  states the classical BMK formula for a bounded `C^1` domain
  `D compactly contained in C^n`, `1 <= q <= n`, and
  `f in C^1_{0,q}(bar D)`:
  the form is the boundary BMK term minus the interior BMK term applied
  to `dbar f` minus `dbar_z` applied to the previous BMK operator.

Partially verified textbook anchors:

- `Range86`, Chapter IV, Section 1, pp. 144-145 preview, verifies that
  the section derives the BMK kernels from the Newtonian potential and
  establishes representation formulas for differential forms on domains
  with piecewise `C^1` boundary.  Exact theorem/equation anchor still
  unverified.
- `LiebMichel02`, Chapter I preview, verifies the chapter-level scope:
  BMK formulas for arbitrary smooth functions and differential forms of
  arbitrary degree.  Exact theorem/equation anchor still unverified.
- `Koppelman67-forms` is the historical citation for the differential
  form formula; exact formula anchor still unverified.

Hypotheses and content:

- The verified exact formula requires a bounded domain with at least
  `C^1` boundary and `C^1` forms in the classical statement.  It includes
  a boundary term and an interior homotopy term.
- It is an external Dolbeault homotopy formula on complex domains.

Supported manuscript use:

- Supports citation of a Koppelman-type external homotopy identity
  behind `main.tex:1422-1452` after translating signs and component
  conventions.
- Supports the broad legitimacy of replacing a closed-form local
  calculation by a BMK homotopy formula only under the domain and
  regularity hypotheses above.

Non-support:

- Does not provide the finite-window projection `i_N p_N`.
- Does not provide the manuscript's relative quotient by collar-supported
  currents.
- Does not prove the native `E_2` factorization transfer, arity-two
  Hamiltonian action, or all-window limit.

### `Weak-Boundary-BMK`

Verified modern anchor:

- `Ruppenthal08v2-11`, Section 5, Theorem 5.6 (`thm:bmklp`), p. 19 of
  the arXiv PDF/source, extends the BMK formula to `L^p` forms with weak
  `dbar` boundary values under the stated bounded smooth-domain
  hypotheses.

Supported manuscript use:

- At most a modern regularity cross-check if the manuscript ever invokes
  weak boundary values.

Non-support:

- The manuscript's current quotient and finite-window principal-part
  transfer are not weak-boundary BMK regularity statements.  Do not use
  this theorem to prove local mixed-HT current descent without an
  explicit construction.

### `Residue-Euler-Normalization`

Verified source state:

- No new BMK/Koppelman source in this pass proves the manuscript's
  residue-current normalization
  `Delta_{a,b}=(-1)^{a+b}/(a! b!) partial_{z1}^a partial_{z2}^b
  delta_0 dbar z1 wedge dbar z2`.
- The relevant primary-source support for residue and Matlis duality
  remains the existing local fixture
  `references/primary-sources/matlis-local-cohomology-residue-anchor.md`,
  together with the internal residue calculation in the manuscript.

Supported manuscript use:

- The BMK sources are compatible with the standard Cauchy normalization
  but do not by themselves prove the finite-window derivative-delta
  residue basis or Euler/residue normalization in local `C^2`.

Non-support:

- No Omega trace-state theorem.
- No Roos compatibility.
- No scalar-contact projection.

## Manuscript Obligation Map

| Manuscript locus | Kernel obligation | External support from this fixture | Internal obligation remaining |
|---|---|---|---|
| `main.tex:1242-1420` | Finite-window BMK transfer theorem. | External BMK kernel and homotopy formula only. | Cutoff, current limit, finite window, moment projection, collar quotient, and arity maps remain internal. |
| `main.tex:1271-1283` | Full BMK kernel on `C^2`. | `LaurentThiebaut11` Definition 1.2 and `Ruppenthal08v2-11` Definition 5.1 support the kernel family and normalization class. | Exact sign, orientation, and component-order match to the manuscript formula must be checked locally. |
| `main.tex:1284-1299` | `dbar z` terms, cutoff `K_{chi,epsilon}`, current limit `H_chi`. | Laurent-Thiebaut Lemma 1.3 supports pre-cutoff component identities. | Distributional extension across diagonal, cutoff regularization, and collar support are internal. |
| `main.tex:1310-1349` | Support-at-zero residue currents and finite-window moment functional. | No direct BMK support. | Matlis/residue fixture plus internal computation. |
| `main.tex:1351-1378` | Arity-two Hamiltonian/Matlis coadjoint formula. | No direct BMK support beyond the external kernel environment. | Internal mixed-HT/native `E_2` algebra calculation. |
| `main.tex:1380-1405` | All-window obstruction vector. | No BMK source closes the obstruction. | Internal obstruction entries `ob_mom`, `ob_collar`, `ob_3`, and `ob_unif`. |
| `main.tex:1407-1419` | Two-variable principal-part face and no curve VOA/Zhu transfer. | Classical Cauchy/BMK normalization is compatible only after residue translation. | Native `C^2` principal-parts, no scalar-contact projection, no all-arity transfer. |
| `appendix-factorization-current-conventions.tex:399-475` | Appendix finite-window BMK current transfer. | Same external kernel and homotopy support as above. | Appendix theorem's current-level and factorization-level constructions remain internal. |

Line anchors are from the read pass in the shared checkout on
2026-04-30 and may drift under concurrent swarm edits.

## Non-Support Boundary

These sources do not support any of the following manuscript claims
unless a separate internal construction or primary-source theorem is
provided:

- Costello graph realization.
- Brane-defect QME counterterms.
- Scalar-contact projection.
- Roos compatibility.
- Omega trace-state theorem.
- Native `E_2` factorization transfer.
- All-window uniform estimate or all-arity transfer.
- Finite-window moment projection and collar-error removal.
- Hamiltonian/Matlis arity-two action.
- Brane, defect, large-`N`, or single-trace statement.
- Compact Calabi-Yau, global BCOV, CoHA, BKM, OSV/GV, or Igusa
  consequence.

## Remaining Gaps

1. Obtain and inspect a primary scan of Martinelli 1938.  Record exact
   title typography, pages, theorem/formula numbers, and the original
   normalization.
2. Obtain a readable copy of Bochner 1943.  Confirm page range 652-673
   and identify the precise Green-formula statement used in the BMK
   lineage.
3. Obtain AMS PDFs or scans for Koppelman 1967 forms/functions papers.
   Record the exact formula and page anchors rather than relying on
   metadata.
4. Inspect full Range 1986 Chapter IV and full Lieb--Michel 2002 Chapter
   I.  Record exact theorem/equation anchors for the BMK formula, domain
   hypotheses, and constants.
5. If Henkin--Leiterer is to be used, load the exact volume and theorem.
6. Perform a local sign/orientation check translating the verified modern
   BMK conventions to the manuscript's `K_BM(zeta,z)` convention in
   dimension two.

## Verification Commands

Representative commands run from `/Users/raeez/topological-strings` or
with temporary outputs in `/tmp/agent268-sources`:

```bash
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,240p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,240p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,220p' reconstitution/missing-primary-source-fixture-plan-2026-04-30.md
rg -n "Bochner|Martinelli|Koppelman|BMK|K_BM|Koppelman|kernel" .
nl -ba main.tex | sed -n '1180,1510p'
nl -ba appendix-factorization-current-conventions.tex | sed -n '380,490p'
nl -ba appendix-matlis-principal-parts.tex | sed -n '1,230p'
sed -n '1,240p' references/primary-sources/matlis-local-cohomology-residue-anchor.md
curl -L -sS 'https://api.crossref.org/works/10.1090%2Fs0002-9904-1967-11744-0'
curl -L -sS 'https://api.crossref.org/works/10.1090%2FS0002-9904-1967-11757-9'
curl -L -sS 'https://api.crossref.org/works/10.2307%2F1969103'
curl -L -sS 'https://api.crossref.org/works/10.1007%2F978-1-4757-1918-5'
curl -L -sS 'https://api.crossref.org/works/10.1007%2F978-0-85729-030-4_3'
curl -L -sS 'https://api.crossref.org/works/10.1007%2F978-3-322-91608-2_2'
curl -L -sS 'https://api.crossref.org/works?query.title=Friedrichs%20extension%20lemma%20with%20boundary%20values%20and%20applications%20in%20complex%20analysis&rows=3'
curl -L -sS 'https://link.springer.com/chapter/10.1007/978-1-4757-1918-5_4'
curl -L -sS 'https://link.springer.com/chapter/10.1007/978-0-85729-030-4_3'
curl -L -sS 'https://link.springer.com/chapter/10.1007/978-3-322-91608-2_2'
curl -L --fail -sS https://arxiv.org/pdf/0803.0092 -o /tmp/agent268-sources/ruppenthal-0803.0092.pdf
pdftotext /tmp/agent268-sources/ruppenthal-0803.0092.pdf /tmp/agent268-sources/ruppenthal-0803.0092.txt
gzip -cd /tmp/agent268-sources/ruppenthal-0803.0092.tar > /tmp/agent268-sources/friedrichs-arxiv2.tex
rg -n "Definition 5\\.1|Theorem 5\\.2|Theorem 5\\.6|Bochner|Koppelman|BMK" /tmp/agent268-sources/friedrichs-arxiv2.tex
```

Failed or partial access notes:

- AMS PDF requests for Koppelman returned Cloudflare 403 HTML.
- JSTOR access for Bochner returned an access-check page.
- Springer full chapter PDF requests for Laurent-Thiebaut and
  Lieb--Michel redirected to authentication HTML; only official preview
  pages were used for exact anchors.
- Temporary files in `/tmp/agent268-sources` were not imported into the
  repository.
