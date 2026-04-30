# Weiss/Ran/Stratified Descent Source Anchors, 2026-04-30

Agent: 262.

Scope: source fixture for Weiss-cover descent, Ran/configuration
descent, and stratified factorization-homology grammar relevant to the
local mixed HT manuscript.  This file verifies source metadata and
anchors only.  It does not supply the manuscript's missing stratified
mixed-HT construction.

Verdict: the sources below support the external language of Weiss
covers, homotopy cosheaves/factorization algebras, manifold-calculus
`J_k` covers, configuration/Ran product grammar, and stratified
factorization homology.  None proves the manuscript's brane-defect QME,
unreduced centrality homotopies, normal \(\Omega\) contraction,
residue/Euler normalization, or physical trace-state theorem.

Anchor convention: "verified" means checked directly in the local PDF or
HTML extraction named under Verification Commands.  Page references to
Costello--Gwilliam Vol. I are preprint/content-page anchors from the
nLab-hosted author PDF; exact CUP published-book theorem/page anchors
remain unverified.

## Local Manuscript Obligations

| Local anchor | Obligation surface | Source-use boundary |
|---|---|---|
| `main.tex:4126-4192` | Unreduced factorization-centre lift problem, including closed-to-open compatibility beyond the reduced current target. | External factorization-algebra sources only justify the grammar of prefactorization, descent, and factorization centres.  They do not construct the required mixed HT morphism. |
| `main.tex:4239-4255` | Weiss/Ran descent obstruction complex for the global factorization-centre morphism. | Costello--Gwilliam and Boavida--Weiss justify the form of Weiss/Ran descent tests.  The actual obstruction cochain in the mixed HT brane-defect complex remains internal. |
| `open-obligations.tex:891-913` | Stratified Weiss-cover descent defect \(\delta_{\mathrm{Weiss}}(V,\mathcal U)\). | Sources support using a Weiss-type cover condition and Cech/cosheaf descent.  They do not prove vanishing for \(\mathcal F^{str}_{\Omega,N}\). |
| `open-obligations.tex:914-991` | Product and \(P_0\)-centrality homotopies against unreduced open observables. | No external descent source supplies these homotopies. |
| `open-obligations.tex:993-1021` | Brane-defect QME curvature, kernel, and counterterms. | Costello--Gwilliam Vol. II gives QFT/factorization vocabulary at most; this local QME solution is not imported. |
| `open-obligations.tex:1024-1076` | Trace-state functional, normalization, Ward identities, topology, and large-\(N\) asymptotics. | AFT and CFG-style trace analogies do not choose a state or cumulant topology for this model. |
| `local-dictionary.tex:678-712` | Stratified factorization datum and \(\Omega\)-obstruction vector. | External sources supply coefficient-datum grammar, not the datum itself. |

## Source Rows

### `CG-Vol1-Weiss-factorization`

Metadata:

- Kevin Costello and Owen Gwilliam, *Factorization Algebras in Quantum
  Field Theory*, Volume 1.
- Cambridge University Press, New Mathematical Monographs 31.
- Local bibliography anchor: `main.tex:9018-9028`.
- Official identifiers verified from local Cambridge HTML:
  DOI `10.1017/9781316678626`, online ISBN `9781316678626`,
  hardback ISBN `9781107163102`; Cambridge online publication January
  2017.
- Stable public URL: `https://www.cambridge.org/core/product/identifier/9781316678626/type/book`.

Verified anchors in the nLab-hosted author PDF
`/tmp/agent262-sources/cg-nlab.pdf`:

- Definition 3.1.2.2, content p.34: prefactorization algebra as a
  symmetric monoidal functor from the multicategory of opens/disjoint
  embeddings.
- Definition 6.1.0.5, content p.150: a Weiss cover of an open set is a
  cover in which every finite subset lies in one member of the cover.
- Definition 6.1.1.1, content p.151: a lax factorization algebra is a
  cosheaf for the Weiss topology.
- Definition 6.1.2.1, content pp.151-152: a lax homotopy factorization
  algebra satisfies Cech descent for every Weiss cover; a homotopy
  factorization algebra also has quasi-isomorphism structure maps for
  disjoint opens.
- Definition 6.2.0.1, content p.154: locally constant factorization
  algebra.
- Theorem 6.2.0.2, content p.154: Lurie's equivalence between
  \(E_n\)-algebras and locally constant factorization algebras on
  \(\mathbb R^n\), under the stated local-constancy setting.
- Theorem 6.3.3.1, content pp.158-160: symmetric algebras of compactly
  supported sections of vector bundles/local cochain complexes form
  strict/homotopy factorization algebras; proof uses Weiss Cech descent.
- Theorem 6.4.0.2, content pp.161-162: a local dg Lie algebra
  \(\mathcal L\) yields factorization algebras
  \(U\mapsto C_*(\mathcal L_c(U))\) and
  \(U\mapsto C^*(\mathcal L(U))\), with descent checked by a Cech
  spectral sequence.
- Theorem 7.3.1.1, content p.175: under the "good theory of algebras"
  hypothesis, derived operadic extension from disks is weakly equivalent
  to the original factorization algebra.
- Proposition 7.3.2.1, content pp.176-177: a descent datum on a locally
  finite cover glues to a factorization algebra by operadic extension.
- Definition 7.4.0.2, content pp.180-181: factorizing basis and
  \(\mathcal U\)-factorization algebra.
- Proposition 7.4.0.4, content p.182: extension from a factorizing
  basis gives a factorization algebra whose restriction is
  quasi-isomorphic to the original datum.

Positive support:

- Supports the manuscript's use of "Weiss cover", "Weiss topology",
  "homotopy cosheaf", and "factorization algebra" as descent-bearing
  terms.
- Supports a source-primary claim that local dg Lie algebra observables,
  when the hypotheses are met, produce factorization algebras satisfying
  Weiss descent.
- Supports checking product-disk data against arbitrary Weiss covers by
  extension only after the local hypotheses and basis/cofinality
  conditions are verified.

Non-support boundaries:

- Does not prove that the manuscript's mixed de Rham/Dolbeault closed
  sector or brane-defect sector is a local dg Lie algebra satisfying the
  required hypotheses.
- Does not construct the stratified pair \((X,L)\), the brane interval
  branch, collar module maps, product/\(P_0\)-centrality homotopies,
  QME counterterms, or \(\Omega\)-trace state.
- Exact CUP published-book theorem/page anchors for the above items are
  still unverified; the verified detailed anchors are to the author PDF.

### `CG-Vol2-QFT-factorization-background`

Metadata:

- Kevin Costello and Owen Gwilliam, *Factorization Algebras in Quantum
  Field Theory*, Volume 2.
- Cambridge University Press, New Mathematical Monographs 41, 2021.
- Local bibliography anchor: `main.tex:9030-9040`.
- Official identifiers verified from local Cambridge HTML:
  DOI `10.1017/9781316678664`, online ISBN `9781316678664`,
  hardback ISBN `9781107163157`.
- Stable public URL: `https://www.cambridge.org/core/books/factorization-algebras-in-quantum-field-theory/3B0E2ADE1EB6E0B06C91EA6E888B0C20`.

Checked local anchors:

- `references/primary-sources/costello-cg-source-anchors-2026-04-28.md`
  records section-level support: Vol. II Section 8.5 for local
  observables as a prefactorization algebra, Section 8.6 for local
  observables as a factorization algebra, and Sections 11-13 for
  Noether/anomaly vocabulary.

Positive support:

- Supports the general Costello--Gwilliam background that perturbative
  QFT observables are organized as factorization algebras after the
  analytic and renormalization hypotheses are supplied.

Non-support boundaries:

- The present fixture did not verify exact CUP theorem/page anchors in
  Vol. II.
- Vol. II does not by citation alone solve the manuscript's
  brane-defect BV/QME kernel, non-scalar counterterms, \(\Omega\)-basic
  normal contraction, or trace-state functional.

### `BdBW-HHA-Weiss-homotopy-sheaves`

Metadata:

- Pedro Boavida de Brito and Michael S. Weiss, "Manifold calculus and
  homotopy sheaves".
- *Homology, Homotopy and Applications* 15(2), 2013, pp. 361-383.
- DOI `10.4310/HHA.2013.v15.n2.a20`; arXiv `1202.1305`;
  arXiv DOI `10.48550/arXiv.1202.1305`.
- Stable public URLs:
  `https://arxiv.org/abs/1202.1305` and
  `https://www.intlpress.com/site/pub/files/_fulltext/journals/hha/2013/0015/0002/HHA-2013-0015-0002-a020.pdf`.

Verified anchors in `/tmp/agent262-sources/bdw-hha.pdf`:

- p.362: the Grothendieck topologies \(J_k\) require every subset of
  at most \(k\) points to be contained in some cover element; Definition
  1.1 identifies the Taylor tower with homotopy sheafifications.
- p.362, Theorem 1.2: \(F\to T_kF\) is homotopy \(J_k\)-sheafification.
- p.365, Definitions 2.4 and 2.5: coverage \(J_k\) and homotopy
  \(J_k\)-sheaf condition.
- p.365, Remark 2.6: the polynomial functor condition agrees with the
  homotopy \(J_k\)-sheaf viewpoint.
- p.365, Definition 2.7: `Disc_k`.
- p.366, Proposition 2.10: every manifold admits a good \(k\)-cover.
- p.369, Proposition 3.3 and Definition 3.4: homotopy sheaves and local
  equivalences for a coverage.
- p.373, Theorem 5.1: \(T_kF\) is a homotopy \(J_k\)-sheaf.
- p.374, Theorem 5.3: \(T_kF\) is homotopy \(J_k\)-sheafification.
- p.377, Theorem 7.2: homotopy \(J_k\)-sheaf equals polynomial functor.
- p.379, Proposition 7.6: equivalent characterizations in the enriched
  setting.
- p.382, Theorem A.5: totalization model for \(T_kF(M)\).

Positive support:

- Supports the finite-point cover grammar underlying Weiss/manifold
  calculus descent.
- Supports treating \(J_k\)-descent as a homotopy sheafification
  condition and using good \(k\)-covers/totalizations as test objects.

Non-support boundaries:

- This is a theory of contravariant functors from manifolds to spaces,
  not factorization cosheaves of chain complexes and not stratified
  mixed holomorphic/topological SFT.
- It does not prove \(J_\infty\) descent for the manuscript's
  non-product stratified Weiss covers, and it does not construct any
  brane module, BV bracket, QME kernel, or \(\Omega\)-trace state.

### `BdBW-Config-Embeddings`

Metadata:

- Pedro Boavida de Brito and Michael S. Weiss, "Spaces of smooth
  embeddings and configuration categories".
- *Journal of Topology* 11(1), 2018, pp. 65-143.
- DOI `10.1112/topo.12048`; arXiv `1502.01640`;
  arXiv DOI `10.48550/arXiv.1502.01640`.
- Stable public URLs:
  `https://arxiv.org/abs/1502.01640` and
  `https://doi.org/10.1112/topo.12048`.

Verified anchors in `/tmp/agent262-sources/bdw-config-embeddings.pdf`:

- Section 3.3 / Theorem 3.7, published-page range around J. Topol.
  p.81 in the PDF pagination: for fixed \(N\), the contravariant
  functor
  \(M\mapsto Rmap_{\mathrm{Fin}}(\operatorname{con}(M;k),\operatorname{con}(N))\)
  is a homotopy sheaf for the \(J_k\) topology.  The text immediately
  recalls that a \(J_k\)-cover is one in which every subset of cardinality
  at most \(k\) is contained in one cover image.
- Section 5.1 / Theorem 5.1, around published p.85: the square
  comparing \(T_k emb(M,N)\), \(T_1 emb(M,N)\), and the corresponding
  derived mapping spaces of configuration and local configuration
  categories is homotopy cartesian for \(1\le k\le\infty\).
- Section 6 / Theorem 6.1 and Proposition 6.3, around published
  pp.91-92: boundary/local configuration-category functors satisfy
  homotopy sheaf conditions for the relevant \(J_k\) or \(J_1\)
  topologies.
- Section 6 / Theorem 6.4, around published p.92: the boundary version
  of the calculus/configuration-category square is homotopy cartesian.

Positive support:

- Supports the idea that configuration/Ran-style categories can package
  finite-point descent and local-to-global information in manifold
  calculus.
- Supports using boundary/local configuration category results as
  external grammar for a future brane-lower-stratum comparison, if a
  matched-conventions functor is constructed.

Non-support boundaries:

- It concerns embedding spaces and configuration categories, not
  Costello--Gwilliam factorization algebras of observables.
- Boundary/local configuration-category sheaf results do not supply the
  manuscript's stratified brane prefactorization functor, collar module,
  BV/QME quantization, or trace state.

### `BdBW-Config-Product`

Metadata:

- Pedro Boavida de Brito and Michael S. Weiss, "The configuration
  category of a product".
- arXiv `1701.06987`, v2 dated 2017-11-24; arXiv DOI
  `10.48550/arXiv.1701.06987`.
- No journal publication metadata was verified in this pass.
- Stable public URL: `https://arxiv.org/abs/1701.06987`.

Verified anchors in `/tmp/agent262-sources/bdw-config-product.pdf`:

- Theorem 1, p.1: natural weak equivalence of Segal spaces
  \(\operatorname{con}(M)\boxtimes\operatorname{con}(N)\to
  \operatorname{con}(M\times N)\) over `Fin`, for topological manifolds.
- Theorem 2.8, Section 2: the resulting product map is a weak
  equivalence, already degreewise after the stated conservative
  completion.
- Proposition 5.2, Section 5: the product construction \(\boxtimes\)
  commutes with truncation.

Positive support:

- Supports a Ran/configuration-category product analogy for product
  manifolds and truncated finite-point data.

Non-support boundaries:

- Does not prove that an external tensor product of
  Costello--Gwilliam factorization algebras is a Weiss cosheaf for
  arbitrary non-product Weiss covers.
- Does not address holomorphic/topological mixed coefficients,
  stratified branes, QME compatibility, or \(\Omega\)-localized trace
  functionals.

### `AFT-Stratified-Factorization-Homology`

Metadata:

- David Ayala, John Francis, and Hiro Lee Tanaka, "Factorization
  homology of stratified spaces".
- *Selecta Mathematica (N.S.)* 23(1), 2017, pp. 293-362.
- DOI `10.1007/s00029-016-0242-1`; arXiv `1409.0848`;
  arXiv DOI `10.48550/arXiv.1409.0848`.
- Stable public URLs:
  `https://arxiv.org/abs/1409.0848` and
  `https://link.springer.com/article/10.1007/s00029-016-0242-1`.
- Existing internal source fixture:
  `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`.

Verified anchors in `/tmp/agent262-sources/aft-arxiv.pdf`:

- Introduction, Definition 0.1 / Theorem 0.2: homology theories are
  characterized by tensor-excision and continuity; `Disk(B)`-algebras
  correspond to such homology theories.
- Corollary 0.3: for framed \(n\)-manifolds with framed
  \(d\)-submanifolds, a `Disk^{fr}_{d\subset n}`-algebra is described
  by data \((A,B,\alpha)\) with a central-action type map
  \(\alpha:\int_{S^{n-d-1}}A\to HC^*_{D^{fr}_d}(B)\).
- Definition 2.14: factorization homology is the left adjoint from
  `Disk(B)`-algebras.
- Theorem 2.15: colimit formula over `Disk(B)/X`, under the target
  cocompleteness assumptions.
- Lemmas 2.19 and 2.20: bounded Ran topology and its relation to
  `Disk(Bsc)/X` and basics.
- Definition 2.37: homology theory axioms.
- Corollary 2.40: factorization homology satisfies tensor-excision and
  continuity.
- Theorem 2.43: equivalence between `Disk(B)`-algebras and homology
  theories.
- Proposition 4.8 and Proposition 4.13: framed submanifold examples and
  free-case computations relevant as grammar for lower-stratum data.

Positive support:

- Supports the phrase "stratified factorization homology" and the need
  for an actual `Disk`-algebra coefficient datum on a stratified pair.
- Supports the manuscript's obligation to supply lower-stratum brane
  data, central-action/module data, excision, and continuity before a
  stratified trace theorem can be claimed.
- Supports bounded Ran/descent vocabulary for stratified factorization
  homology.

Non-support boundaries:

- It is topological/conically smooth, not a proof of the mixed
  de Rham/Dolbeault local HT coefficient system.
- It does not construct the Hamiltonian closed sector, Dirac brane
  algebra, \(\Omega\)-basic contraction, QME solution, trace state,
  residue/Euler normalization, or large-\(N\) cumulant theorem.

### `Existing-Omega-Stratified-Fixture`

Metadata:

- Internal source ledger:
  `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`.
- Checked sources in that ledger: AFT `1409.0848`; Costello
  `1610.04144`; Costello `1705.02500`; Costello--Francis--Gwilliam
  `2602.12412`.

Positive support:

- Confirms that AFT supports only stratified factorization-homology
  coefficient grammar.
- Confirms that Costello's \(\Omega\)-background and M2/Koszul sources
  are related-model evidence only.
- Confirms that the CFG Chern--Simons trace source is a template for a
  factorization-homology trace after a model-specific \(E_n\)-algebra,
  perfect module, and BV defect quantization are built.

Non-support boundaries:

- The internal ledger explicitly rejects automatic transfer to the
  present normal \(\Omega\)-background, mixed HT brane-defect
  coefficient system, QME package, or physical large-\(N\) trace state.

## Support Matrix

| Manuscript obligation | Sources that support the grammar | What is actually supported | What remains internal |
|---|---|---|---|
| Weiss-cover descent for a factorization algebra | `CG-Vol1-Weiss-factorization`; `BdBW-HHA-Weiss-homotopy-sheaves` | Weiss/\(J_k\) cover condition, Cech/homotopy descent tests, factorization algebra as Weiss homotopy cosheaf. | Prove \(\delta_{\mathrm{Weiss}}=0\) for the specific \(\mathcal F^{str}_{\Omega,N}\). |
| Extension from disks/product data | `CG-Vol1-Weiss-factorization`; `BdBW-Config-Product` | Extension from factorizing bases under hypotheses; configuration product equivalence for manifolds. | Product-disk-to-arbitrary-stratified-Weiss cofinality for the manuscript's mixed HT coefficients. |
| Ran/configuration finite-point descent | `BdBW-HHA-Weiss-homotopy-sheaves`; `BdBW-Config-Embeddings`; `BdBW-Config-Product`; `AFT-Stratified-Factorization-Homology` | \(J_k\)-finite subset topologies, configuration categories, bounded Ran topology, and colimit over disk categories. | A matched Ran/Weiss obstruction complex for the closed-open local functional complexes. |
| Stratified lower-stratum brane grammar | `AFT-Stratified-Factorization-Homology`; `Existing-Omega-Stratified-Fixture` | Need for `Disk`-algebra data on the stratified pair, including lower-stratum coefficient and central-action/module map. | Actual brane interval algebra, collar module, centrality homotopies, and stratified descent proof on \((X,L)\). |
| Factorization algebra of observables | `CG-Vol1-Weiss-factorization`; `CG-Vol2-QFT-factorization-background` | Standard factorization algebra/descent formalism for observables under the source hypotheses. | Mixed HT BV complex, renormalized local observables, anomaly cancellation, and brane-defect QME. |
| Normal \(\Omega\) trace-state theorem | none as theorem support; `Existing-Omega-Stratified-Fixture` only as boundary source | External analogies name proof obligations and related mechanisms. | \(Q_\Omega=Q+\iota_{V_\Omega}\), \(Q_\Omega^2=L_{V_\Omega}\), normal-weight contraction, residue/Euler normalization, state functional, Ward identities, cumulant topology, large-\(N\) asymptotics. |

## Non-Support Firewall

The following imports are not source-supported:

1. "Costello--Gwilliam prove the manuscript's stratified mixed HT
   factorization algebra."  False.  They supply a formalism and standard
   examples under hypotheses; the local mixed HT and brane-defect
   hypotheses must be checked.
2. "Boavida--Weiss \(J_k\)-sheafification proves the manuscript's
   Weiss descent."  False.  Their functors are contravariant
   space-valued manifold-calculus objects.
3. "Configuration-category product equivalence proves arbitrary product
   or stratified Weiss cofinality for observables."  False.  It is a
   configuration/Ran product theorem, not an observable cosheaf theorem.
4. "AFT stratified factorization homology proves the Omega trace."  False.
   AFT supplies the stratified coefficient/excision grammar; it does not
   choose the coefficient system, QME solution, or state.
5. "Existing Costello Omega/M2/CFG trace sources prove this local
   brane theorem by analogy."  False.  The earlier fixture already marks
   them as related-model support or templates only.

## Verification Commands

Commands run in `/Users/raeez/topological-strings` unless marked
otherwise:

```bash
sed -n '1,220p' AGENTS.md
sed -n '1,220p' CLAUDE.md
sed -n '1,260p' /Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md
sed -n '1,220p' /Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md
sed -n '1,260p' reconstitution/missing-primary-source-fixture-plan-2026-04-30.md
sed -n '1,260p' reconstitution/global-weiss-ran-descent-firewall-construction-target-2026-04-30.md
sed -n '1,240p' reconstitution/swarm-2026-04-30-agent-238-global-weiss-ran-descent-firewall-construction-target.md
sed -n '4118,4265p' main.tex
sed -n '890,1080p' open-obligations.tex
sed -n '630,718p' local-dictionary.tex
sed -n '1,260p' references/primary-sources/omega-stratified-source-anchors-2026-04-30.md
sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-178-stratified-trace-obligations-0957.md
sed -n '1,220p' reconstitution/swarm-2026-04-30-agent-186-omega-stratified-source-audit-0957.md
sed -n '1,220p' reconstitution/physical-omega-largeN-trace-state-thread-2026-04-30.md
sed -n '1,220p' reconstitution/omega-physical-largeN-state-construction-target-2026-04-30.md
rg -n -F -e "Weiss" -e "Ran" -e "stratified" -e "factorization" main.tex open-obligations.tex local-dictionary.tex references reconstitution
```

Source retrieval/extraction commands run under `/tmp/agent262-sources`:

```bash
curl -L -o cg-nlab.pdf https://ncatlab.org/nlab/files/CostelloGwilliam-FactorizationAlgebras.pdf
pdftotext cg-nlab.pdf cg-nlab.txt
curl -L -o bdw-hha.pdf https://www.intlpress.com/site/pub/files/_fulltext/journals/hha/2013/0015/0002/HHA-2013-0015-0002-a020.pdf
pdftotext bdw-hha.pdf bdw-hha.txt
curl -L -o bdw-config-embeddings.pdf https://arxiv.org/pdf/1502.01640
pdftotext bdw-config-embeddings.pdf bdw-config-embeddings.txt
curl -L -o bdw-config-product.pdf https://arxiv.org/pdf/1701.06987
pdftotext bdw-config-product.pdf bdw-config-product.txt
curl -L -o aft-arxiv.pdf https://arxiv.org/pdf/1409.0848
pdftotext aft-arxiv.pdf aft-arxiv.txt
rg -n -e "Definition 6.1.0.5|Theorem 6.4.0.2|Theorem 7.3.1.1|Proposition 7.4.0.4" cg-nlab.txt
rg -n -e "Theorem 1.2|Definition 2.4|Definition 2.7|Theorem 5.3|Theorem 7.2|Theorem A.5" bdw-hha.txt
rg -n -e "Theorem 3.7|Theorem 5.1|Theorem 6.1|Proposition 6.3|Theorem 6.4" bdw-config-embeddings.txt
rg -n -e "Theorem 1|Theorem 2.8|Proposition 5.2" bdw-config-product.txt
rg -n -e "Definition 2.14|Theorem 2.15|Definition 2.37|Corollary 2.40|Theorem 2.43|Proposition 4.8|Proposition 4.13" aft-arxiv.txt
```

Web metadata checks:

- Cambridge Core for Costello--Gwilliam Vol. I and Vol. II.
- arXiv pages for `1202.1305`, `1409.0848`, `1502.01640`, and
  `1701.06987`.
- Springer page for DOI `10.1007/s00029-016-0242-1`.
- HHA/International Press PDF for DOI `10.4310/HHA.2013.v15.n2.a20`.
- University of Lisbon research-portal metadata for DOI
  `10.1112/topo.12048`.

No PDF build was run.

## Files Read

- `AGENTS.md`
- `CLAUDE.md`
- `/Users/raeez/ecosystem/skills/shared/attack-heal-swarm/protocol.md`
- `/Users/raeez/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
- `main.tex`
- `open-obligations.tex`
- `local-dictionary.tex`
- `reconstitution/missing-primary-source-fixture-plan-2026-04-30.md`
- `reconstitution/global-weiss-ran-descent-firewall-construction-target-2026-04-30.md`
- `reconstitution/swarm-2026-04-30-agent-238-global-weiss-ran-descent-firewall-construction-target.md`
- `reconstitution/swarm-2026-04-30-agent-178-stratified-trace-obligations-0957.md`
- `reconstitution/swarm-2026-04-30-agent-186-omega-stratified-source-audit-0957.md`
- `reconstitution/physical-omega-largeN-trace-state-thread-2026-04-30.md`
- `reconstitution/omega-physical-largeN-state-construction-target-2026-04-30.md`
- `references/primary-sources/omega-stratified-source-anchors-2026-04-30.md`
- `references/primary-sources/costello-gwilliam-vol1-cambridge.html`
- `references/primary-sources/costello-gwilliam-vol2-cambridge.html`
- `references/primary-sources/costello-cg-source-anchors-2026-04-28.md`
- `references/primary-sources/costello-graph-qme-source-anchors-2026-04-30.md`
- `/tmp/agent262-sources/cg-nlab.txt`
- `/tmp/agent262-sources/bdw-hha.txt`
- `/tmp/agent262-sources/bdw-config-embeddings.txt`
- `/tmp/agent262-sources/bdw-config-product.txt`
- `/tmp/agent262-sources/aft-arxiv.txt`

## Remaining Gaps

1. Exact CUP published theorem/page anchors for
   Costello--Gwilliam Vol. I and Vol. II remain unverified; verified
   detailed anchors are to the author/preprint PDF and local section
   fixtures.
2. No matched-conventions proof yet connects the manuscript's
   \(\operatorname{Disk}^{str}_{X,L}\) candidate to AFT's
   conically-smooth framework.
3. No source proves the product-disk-to-arbitrary-stratified-Weiss
   cofinality needed for the actual mixed HT coefficient system.
4. The brane-defect QME kernel, product/\(P_0\)-centrality homotopies,
   normal \(\Omega\)-contraction, and trace-state functional are still
   construction obligations, not citation obligations.
5. The published status of `BdBW-Config-Product` beyond arXiv was not
   verified; the source is used only as arXiv-level configuration
   product support.
