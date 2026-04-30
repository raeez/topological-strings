# CLAUDE.md — topological-strings

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation. Read it first. Repo-local rules follow.

---

## Repo-local

Computations and remarks on the **mixed holomorphic-topological string
field theory on**
\[
  \mathbb R^2_{\mathrm{top}}\times \mathbb C^2_{\mathrm{hol}},
\]
with its local Hamiltonian/Kodaira-Spencer-type holomorphic sector,
topological de Rham sector, defect/brane operator algebras, BV/QME
complexes, and Weyl/Moyal/radial-parts computations.  BCOV and
Kodaira-Spencer gravity supply source conventions and physical
motivation; the active theorem surface is the formal-local
two-real-by-two-complex-dimensional mixed HT SFT, not compact
Calabi-Yau threefold theory.

**Source layout.**

- `main.tex` — root.
- `abstract.tex`, `preamble.tex`, `authors.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`, `nomenclature.tex` — bound parts.
- `Makefile` — `make` builds the PDF via `pdflatex`.
- `firstorder.{png,svg}`, `thirdordera.{png,svg}`, `thirdorderb.{png,svg}` — diagram assets.
- `scripts/` — computation scripts.
- `amstex-template`, `tex-documentation` — build apparatus.

**Where Calabi-Yau enters.** The only Calabi-Yau datum in the core local
model is the trivial holomorphic volume / holomorphic symplectic datum on
\(\mathbb C^2\), used to write the BV pairing, divergence-free
Hamiltonian fields, and cyclic trace densities.  This is a local
unimodularity/orientation input.  It is not a compact target
assumption, not a compact CY\(_3\) BCOV theorem, and not a licence to
import quintic, OSV, GV, MNOP, Abel-Jacobi, CoHA, Igusa, or BKM claims.

**Native versus reduced chiral structures.** The native holomorphic
object of this repository lives on the complex surface \(\mathbb C^2\):
it is a holomorphic \(E_2\)-type / factorization algebra built from
\[
  \Omega_c^{0,\bullet}(B)\widehat\otimes
  (\mathfrak h\ltimes\mathfrak h^\vee_{\mathrm{cont}}[1]),
  \qquad
  \mathfrak h=\mathbb C[[z_1,z_2]]/\mathbb C\cdot1 .
\]
Do not import a curve vertex algebra, Zhu algebra, or Volume-II
\(\mathbb C\times\mathbb R\) chiral/topological theorem directly into
this six-real-dimensional model.  Such objects enter only after a
controlled reduction datum is supplied: the reduced directions, the
compact-support or residue pushforward, the surviving \(z_2\)-mode or
principal-part coefficient system, the brane image, the induced BV
pairing and bracket, and anomaly matching.  A Dirac BRST curve chiral
algebra or Zhu bridge is admissible only on that reduced surface, not as
the native \(\mathbb C^2\) factorization algebra.

**Late 2026-04-30 theorem-control predicates.** Future theorem work must
retain the native \(\mathbb C^2\) holomorphic \(E_2\) taxonomy before any
curve-chiral reduction.  The BMK lane separates the one-pair analytic
pro-Matlis retract from strict native all-window support-local current
transfer, whose obstruction is
\(\operatorname{Ob}^{\Pi}_{\mathrm{BM}}\).  The first certified larger
non-scalar row is \(\theta_3\): a named \(C_{\theta_3}\) is evidence only
with a CE ancestor, a scalar-zero Costello local counterterm, or a
complete companion-face table, and tower compatibility passes through
\(\Delta^1_{M,N}=-\pi_{M,N}\mathfrak b^M+\mathfrak b^N\) plus the
secondary \(\varprojlim^1H^0\) primitive class.  The radial/Weyl theorem
surface is \(\Omega^{\mathrm{rad}}_{a,b}\), equivalently decorated PBW
Stokes for \(D^\square_{a,b}=C^+_{a,b}\partial_2\), with failure exactly
a signed row in \(\ker B_{a,b}^*\).  The larger non-scalar Costello/QME
theorem requires the filtered scalar projection, finite row arrays, the
primitive matrix \(A^Mc=-r^M\), transition matrices, Roos compatibility,
centrality homotopies, and a curved bulk-to-defect kernel.

**Normal \(\Omega\)-background discipline.** The brane-preserving
equivariant deformation is normal scaling of
\[
  N_LX=\mathbb R_s\oplus\mathbb C_{z_1}\oplus\mathbb C_{z_2},
  \qquad
  T_\Omega=\mathbb C^*_{\varepsilon_s}\times
  \mathbb C^*_{\varepsilon_1}\times
  \mathbb C^*_{\varepsilon_2},
\]
with \(t\) fixed.  A literal rotation in the \((t,s)\)-plane does not
preserve the brane line as fixed locus in this model.  Any
\(\Omega\)-background theorem must state the vector field, the
equivariant differential \(Q_\Omega=Q+\iota_{V_\Omega}\), the
\(Q_\Omega^2=L_{V_\Omega}\) mechanism, the inverted normal weights, the
residue-versus-Euler normalization, and the resulting stratified
factorization algebra on \((X,L)\).  This is a theorem surface; it does
not by itself prove Costello graph/QME convergence, non-scalar
centrality, or physical large-\(N\) trace asymptotics.

**Research constellation role.** BCOV / Kodaira-Spencer gravity supplies
motivation and convention checks only.  The Vol III CY-to-chiral
frontier in `~/calabi-yau-quantum-groups`, the compact-CY/quintic source
fixtures, and the Igusa/BKM program are external comparison surfaces.
Treat them as quarantined context unless a local theorem states and
proves a precise matched-conventions comparison.  Future attack-heal
cycles for this paper should spend proof budget on the local
\(\mathbb R^2\times\mathbb C^2\) SFT unless the user explicitly reopens a
global compact-CY frontier lane.  Any divergence is load-bearing:
report, do not silently reconcile.

Modular-form frontier: generating functions in topological-string theory motivate comparison with the Igusa cusp form $\Delta_5$ construction in `~/igusa-cusp-form` via the Borcherds / BKM route. This is a heuristic and convention-checking bridge here, not a BKM consequence of the local Hamiltonian BF/Moyal calculation.

**Voice.** `~/ecosystem/INVARIANTS.md §IV` — Russian mathematical school + mathematical-physics frontier. Named attribution (Bershadsky–Cecotti–Ooguri–Vafa 1993, Witten 1988, Costello 2011, Polyakov 1987), honest epistemic status, physical intuition and formal rigor coexisting without either subordinating the other.

## Long-form proof harness

For Claude Code, Codex CLI, and any GPT-5.5 / GPT-5-Codex-class agent,
frontier mathematical physics runs in maximum-effort mode. Use the
deepest host-exposed model and reasoning budget. If the host offers a
GPT-5.5 Pro / Heavy or `xhigh` setting, use it for theorem repair,
cross-repo synthesis, adversarial review, and primary-source
reconstruction. The private ChatGPT Pro harness is not public; this is
the open local analogue.

For manuscript-proper writing, rewriting, or theorem-lane
reconstitution, load and follow
`~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
before writing. Its unique-survivor, instant-computation, and hostile
Beilinson-audit loop is mandatory under this repository's Supremum
Discipline.

Long runs are normal. A 30-60 minute agent run is acceptable when a
proof obligation requires it. Load `main.tex`, preamble / macro files,
diagram sources, compute scripts, and the cited local BV / Costello /
Hamiltonian / Witten sources before the first mathematical edit. Load
Vol III, compact-CY, or Igusa anchors only when the specific task is a
matched-conventions comparison or a firewall audit. Private scratch stays
private; the deliverable is the checked proof trace and the exact
remaining obstruction.

After every proposed repair, run an attack-heal loop: sign, measure,
propagator, anomaly term, BV degree, graph order, large-N limit, or
false transfer into Vol III. Heal and attack again until the theorem
closes or the exact obstruction is named for the next repair cycle. Do
not downgrade the manuscript to close the loop. Subagents provide
evidence, not authority; the main thread integrates by deep semantic
merge.

## Supremum discipline

Repair is not demotion.  Always take the harder route first: reconstruct
the strongest true theorem by adding the missing mathematical object,
habitat, topology, comparison map, homotopy, kernel, counterterm,
coordinate computation, verified source theorem, or obstruction class.
Do not lower a theorem merely because the present proof is incomplete.
Only record a conditional statement or proof-ledger obstruction after the
stronger formulation has been seriously attacked and the exact missing
construction has been named.  The manuscript should be strictly
upgraded: false strength is removed only by replacing it with deeper
true structure.

A failed theorem surface is not a stopping category.  It must be
reworked until it becomes one of two pristine objects: either a proved
theorem with the missing habitat, maps, kernels, homotopies,
counterterms, signs, and source fixtures supplied, or a proved
obstruction theorem identifying the exact cohomology class, cokernel
functional, Roos class, graph row, or finite-window matrix equation that
prevents the original statement.  Do not leave a theorem as merely
``conditional'', ``external'', or ``expected'' when a sharper
construction problem can be inscribed.  Every attack-heal cycle must
push the failed surface upward toward this supremum form.
