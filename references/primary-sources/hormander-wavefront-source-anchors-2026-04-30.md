# Hormander Wavefront Source Anchors, 2026-04-30

Scope.  This fixture records the primary-source status for the
Hormander wavefront calculus used by the regular-density / wavefront
current graph branch.  It is a microlocal operations fixture only.  It
does not prove any Costello graph theorem, counterterm compatibility
statement, scalar-contact projection, Roos compatibility statement, or
brane-defect QME cancellation.

Verdict.  The source supports standard external microlocal criteria for
wavefront sets, pullback/restriction, tensor product, product, proper
direct image, and kernel composition only where the corresponding
theorem anchors are closed.  The manuscript must still derive its graph
kernel wavefronts, finite-window counterterms, scalar-contact quotient,
Roos compatibility, and singular-current obstruction internally.

## Source Metadata

Verified from the official Springer book and chapter pages.

| Field | Verified value |
|---|---|
| Author | Lars Hormander |
| Title | The Analysis of Linear Partial Differential Operators I |
| Subtitle | Distribution Theory and Fourier Analysis |
| Series | Classics in Mathematics |
| Publisher | Springer Berlin, Heidelberg |
| Copyright | Springer-Verlag GmbH Germany, part of Springer Nature 2003 |
| Edition | 2 |
| Softcover ISBN | 978-3-540-00662-6 |
| Online/eBook ISBN | 978-3-642-61497-2 |
| Book DOI | `10.1007/978-3-642-61497-2` |
| Pages | XI, 440 |
| Chapter used | Chapter VIII, "Spectral Analysis of Singularities" |
| Chapter pages | pp. 251-324 |
| Chapter DOI | `10.1007/978-3-642-61497-2_9` |

Official pages:

- `https://link.springer.com/book/10.1007/978-3-642-61497-2`
- `https://link.springer.com/chapter/10.1007/978-3-642-61497-2_9`

Text-access status.  The official Springer HTML verifies the metadata,
chapter title, chapter DOI, and chapter page range.  The preview PDF
exposes only the beginning of Chapter VIII.  The full chapter PDF was
not accessible in this run; the direct PDF route returned HTML.  No
copyrighted source PDF or OCR mirror was written into the repository.

Reprint statement.  The local bibliography and secondary references
identify the 2003 Classics in Mathematics volume as a reprint of the
second 1990 edition.  The official HTML captured in this run verifies
Edition Number 2, but the exact "reprint of the second 1990 edition"
line remains an anchor still unverified in primary text.

## Anchor Register

`Verified` means that the metadata, theorem number, and page/equation
anchor were checked against an accessible source route during this run.
`Secondary-confirmed` means public references agree on the anchor, but
the primary page was not inspected.  Exact manuscript support must not
promote a secondary-confirmed row to primary-source closure.

| Manuscript need | Hormander anchor | Verification status | Hypotheses / content used | Supports in the manuscript |
|---|---|---|---|---|
| Wavefront-set vocabulary and basic conic support language | Ch. VIII, Sec. 8.1; Definition 8.1.2 | The chapter and section location are verified from Springer preview and chapter HTML. Definition number is secondary-confirmed; page 254 is secondary-confirmed; exact primary page anchor still unverified. | Distribution on an open set/manifold; `WF(u)` is a closed conic subset of `T^*X \ 0`; the projection records singular support. | Vocabulary in `appendix-factorization-current-conventions.tex:1394`, `claim-strength-ledger.tex:462`, and `tate-T1-weighted-completion.tex:2398`. |
| Pullback and submanifold restriction criterion | Thm. 8.2.4; restriction is the submanifold case via the normal/non-characteristic condition | The theorem number is secondary-confirmed; exact theorem page anchor still unverified. Springer chapter abstract verifies the restriction principle in prose but not the theorem number. | For a smooth map `f`, pullback is defined when the normal set of `f` avoids `WF(u)`; then `WF(f^*u)` is bounded by the cotangent pullback of `WF(u)`. | Incidence pullbacks and restriction steps in Definition `def:app-wavefront-admissible-defect-labels`, especially `appendix-factorization-current-conventions.tex:1417-1419`. |
| Tensor-product wavefront estimate | Thm. 8.2.9 | The theorem number is locally used and secondary-confirmed; exact primary page anchor still unverified. | `WF(T_1 tensor T_2)` is contained in the standard union of `WF(T_1) x WF(T_2)` and the two zero-section/support terms. | Tensor coefficient/base factor estimate at `tate-P1-hadamard-mittag-leffler.tex:118-123`; also graph external-label tensor formation. |
| Product criterion for distributions | Thm. 8.2.10 | The theorem number is secondary-confirmed; page 267 is secondary-confirmed; exact primary page anchor still unverified. | Product exists if no covector in one factor cancels a covector in the other over the same base point. The output wavefront is bounded by the union and fibrewise sums with zero-section terms. | Product condition in `appendix-factorization-current-conventions.tex:1420-1433` and product bound in `appendix-factorization-current-conventions.tex:1640-1652`. |
| Proper pushforward / direct image wavefront estimate | Standard Ch. VIII direct-image estimate; likely Thm. 8.2.12 or kernel-calculus consequence of Thm. 8.2.13 | Anchor still unverified.  The exact theorem number, page, and displayed formula must be checked in the primary text before a page-specific citation is used. | If `p` is proper on the relevant support, `WF(p_*T)` is bounded by covectors whose transpose pull back lies in `WF(T)`. | Final graph projection estimate in `appendix-factorization-current-conventions.tex:1653-1664` and the wavefront containment in `tate-T1-weighted-completion.tex:2499-2510`. |
| Kernel action estimate | Thm. 8.2.13 in standard citations | The theorem number is secondary-confirmed; exact primary page anchor still unverified. | Defines when a distribution kernel can act on a compactly supported distribution under a wavefront transversality condition and gives an output wavefront bound. | May support graph-kernel action language only after the exact primary anchor is closed. |
| Kernel composition estimate | Thm. 8.2.14 in standard citations | The theorem number is secondary-confirmed; exact primary page anchor still unverified. | Gives a wavefront criterion and bound for composition of distribution kernels. | May support composite incidence/kernel arguments in the wavefront branch only after the exact primary anchor is closed. |

## External Criterion vs. Internal Derivation

The Hormander fixture supplies only the external microlocal grammar:

- Non-characteristic pullback/restriction of distributions.
- Tensor-product wavefront enlargement.
- Product transversality and the product wavefront bound.
- Proper-support pushforward/direct-image wavefront bound, once the
  exact primary anchor is closed.
- Kernel action/composition estimates, once exact primary anchors are
  closed.

The following manuscript components remain internal graph/kernel
derivations and cannot be cited to Hormander:

- The finite-window graph spaces `X_Gamma(I)` and their incidence maps.
- The actual wavefront computation for the Hadamard graph coefficients
  `K^M_{Gamma,alpha}`.
- The construction of `B_Gamma` from defect-current labels.
- The finite scaling-degree hypothesis along graph collision diagonals.
- The existence, support, and compatibility of graph counterterms.
- The scalar-contact quotient and regular-density subcomplex.
- The singular quotient class `eta^{reg}_{n_0,M}`.
- The Roos / inverse-limit compatibility obstruction.
- The brane-defect BV/QME cancellation.

## Manuscript Map

| Local anchor | Source role | Internal obligation |
|---|---|---|
| `appendix-factorization-current-conventions.tex:1394-1480` | Uses Hormander Ch. 8 grammar to define graphwise wavefront-admissible current labels. | Must compute the graph incidence maps, admissible conic sets, finite-scaling class, and examples. |
| `appendix-factorization-current-conventions.tex:1482-1555` | Uses product, pullback/pushforward, and tensor estimates as operation criteria. | Must build the finite-window Costello graph layer and counterterms. |
| `appendix-factorization-current-conventions.tex:1633-1665` | Uses the product and pushforward wavefront bounds. | Must show the displayed bounds are the only ones used by the distributional graph layer. |
| `appendix-factorization-current-conventions.tex:1729-1742` | Uses product transversality to explain why arbitrary `D'_c(I)` is not available. | Must keep the coincident-current counterexample and absence of an all-`D'_c` theorem as an internal obstruction. |
| `claim-strength-ledger.tex:462-478` | Records Hormander transversality, finite scaling degree, diagonal extension, counterterms, and pushforward bounds as prerequisites. | Must not state a theorem for arbitrary `D'_c(I)`. |
| `tate-T1-weighted-completion.tex:2398-2582` | Uses microlocal containment for the wavefront singular-current obstruction. | Must prove the quotient class, kill criterion, and Roos handoff internally. |
| `tate-P1-hadamard-mittag-leffler.tex:118-123` | Cites Thm. 8.2.9 for the tensor-product wavefront estimate. | Must keep the finite-window Hadamard/Mittag-Leffler graph computation internal. |

## Non-Support Boundary

Hormander does not supply:

- Costello counterterms or the Costello finite-scale BV/RG/QME graph
  theorem.
- Graph-specific Hadamard coefficient wavefront calculations.
- Finite scaling-degree extension across graph collision diagonals.
- Scalar-contact projection or the regular-density quotient.
- Roos compatibility or any `lim^1` primitive statement.
- Brane-defect QME cancellation.
- The theorem that all compactly supported currents `D'_c(I)` are
  admissible graph labels.
- The non-scalar current lift, closed-exchange obstruction, or
  distributional primitive cone.

Thus the allowed citation form is: Hormander supplies microlocal
operation criteria.  The manuscript supplies the graph calculus,
counterterm construction, compatibility equations, and obstructions.

## Remaining Source Gaps

1. Primary-page verification for Definition 8.1.2, commonly located at
   p. 254.
2. Primary-page verification for Theorem 8.2.4 and its exact
   pullback/restriction statement.
3. Primary-page verification for Theorem 8.2.9.
4. Primary-page verification for Theorem 8.2.10, commonly located at
   p. 267.
5. Exact primary anchor for the proper direct-image wavefront estimate:
   likely Ch. VIII, Sec. 8.2, but theorem/page/equation anchor still
   unverified.
6. Exact primary anchors and statements for Theorems 8.2.13 and 8.2.14
   if kernel action/composition estimates are cited.
7. A separate scaling-degree / extension source fixture if the
   manuscript wants external support for finite scaling-degree extension
   and extension ambiguity formulas.
