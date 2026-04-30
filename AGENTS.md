# AGENTS.md — topological-strings

> **Inherits `~/ecosystem/INVARIANTS.md`** — canonical ecosystem rules (model-agnostic): destructive-git forbidden list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, no-LLM-attribution in commits, deep-semantic-merges, intelligence propagation, open-source whitelist.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** — canonical Codex / GPT-5-family harness calibration: reasoning-effort per task class, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity control, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline, error-handling, git-and-worktree restatement for Codex defaults, frontend quality, no-LLM-commit-attribution, voice.
> **Mirrors this repo's `CLAUDE.md`** on substance. Before editing, `read_file ./CLAUDE.md`. `AGENTS.md` and `CLAUDE.md` must not diverge in facts; they may differ in structure and voice.
>
> **Model target.** Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model, `reasoning_effort=xhigh` for any non-trivial mathematical work (never lower than `high`). Terse, declarative voice per `INVARIANTS.md §IV`. No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## What this repository is for

This repository is an instrument for advancing the formal-local mixed
holomorphic-topological string field theory on
\[
  \mathbb R^2_{\mathrm{top}}\times \mathbb C^2_{\mathrm{hol}}.
\]
The active manuscript concerns the local Hamiltonian/Kodaira-Spencer
holomorphic sector, the topological de Rham sector, defect/brane
operator algebras, BV/QME complexes, Koszul-duality checks, and
Weyl/Moyal/radial-parts computations.  BCOV and Kodaira-Spencer gravity
are source conventions and physical motivation; compact Calabi-Yau
threefold theory is not the base geometry of the paper.

Every read, grep, edit, computation, proof repair, or retraction should
serve the manuscript `main.tex`: make the open-string Ext algebra,
AKSZ/BV action, cyclic-homology comparison, large-N single-trace limit,
and first/third-order quantum corrections precise enough to check
line by line.

## The mathematics you are working on

- Mixed holomorphic-topological SFT on
  `\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}`.
- The local holomorphic symplectic / Hamiltonian
  Kodaira-Spencer-type sector on `\mathbb C^2`, with the fixed local
  holomorphic volume form supplying BV pairing and divergence data.
- The native holomorphic `E_2` / factorization algebra on the complex
  surface `\mathbb C^2`, distinct from any curve vertex algebra.
- Topological A/B and mixed A-B local models, branes, Ext algebras, and
  open string field theory.
- Twisted M-theory motivation only where it reduces to the same local
  mixed HT model.
- Koszul duality between brane-side algebras and closed-string
  observables in the large-N limit.
- Loday-Quillen-Tsygan style comparison between matrix Lie algebra
  homology and cyclic homology.
- First-order and third-order quantum corrections on the gauge-theory
  side, with signs, shifts, and grading conventions fixed explicitly.

## What counts as progress

- A theorem, lemma, computation, or diagram in `main.tex` made
  derivable from first principles with the shifts, signs, BV degrees,
  and Ext/cyclic conventions explicit.
- A falsified statement repaired by a corrected proof, computation,
  diagram, or explicit obstruction.
- A quantum correction verified by direct local computation and a
  primary-source comparison.
- A healed statement whose natural hypotheses prevent false transfer into
  compact Calabi-Yau, CY-to-chiral, BKM, CoHA, quintic, OSV/GV, or
  Igusa-cusp-form repositories.
- A correction that removes compact-CY evidence from the core local
  theorem surface unless an explicit matched-conventions theorem is
  being proved.

## Agent rules

1. No AI attribution anywhere. Commits by Raeez Lorgat only.
2. No `git stash`.
3. Do not amend commits without explicit instruction.
4. Do not rebuild after every edit. Build at session end when useful.
5. Never guess a BV, Ext, cyclic-homology, OPE, or Feynman-integral
   formula. Derive it from `main.tex`, direct computation, or primary
   literature.
6. Claim strength must match proof strength. Mark heuristic physics
   motivation separately from proved algebraic statements.
7. User-authorized large swarms are permitted and should be run with
   disjoint scopes, explicit integration ownership, and deep semantic
   merge discipline across relevant research repositories only when the
   claim genuinely crosses those repositories.

8. Do not spend attack-heal proof budget on compact-CY, quintic,
   OSV/GV, Abel-Jacobi, CoHA, Igusa, or BKM fixtures for this paper
   unless the user explicitly reopens a global comparison lane.  In the
   core manuscript, the Calabi-Yau input is local unimodularity on
   `\mathbb C^2`: holomorphic volume, BV pairing, divergence-free
   Hamiltonians, and cyclic traces.
9. Do not treat Volume II's `\mathbb C\times\mathbb R` chiral/topological
   apparatus as the native geometry of this paper.  Curve chiral
   algebras, Zhu algebras, and `SC_{ch,top}` comparisons require a
   controlled reduction from
   `\mathbb R^2_{\mathrm{top}}\times\mathbb C^2_{\mathrm{hol}}`,
   retaining the `z_2` mode or principal-part coefficient system and
   proving the pushed-forward bracket, BV pairing, brane image, and
   anomaly data.
10. For Omega-background work, use the brane-preserving normal scaling
    torus on `N_LX = R_s \oplus C_{z_1}\oplus C_{z_2}` with `t` fixed.
    Do not call a literal rotation in the `(t,s)`-plane native unless a
    different brane/fixed-locus problem has been explicitly defined.
    The theorem surface must include `Q_\Omega=Q+\iota_{V_\Omega}`,
    `Q_\Omega^2=L_{V_\Omega}`, normal-weight contraction, residue/Euler
    normalization, and stratified factorization data.

11. The late 2026-04-30 theorem-control predicates are binding before
    theorem work: native `\mathbb C^2` holomorphic `E_2` taxonomy before
    curve reduction; BMK one-pair pro-Matlis retract is not strict
    native all-window support-local current transfer, whose obstruction
    is `\operatorname{Ob}^{\Pi}_{\mathrm{BM}}`; `\theta_3` requires a CE
    ancestor, scalar-zero Costello counterterm, or complete
    companion-face table plus `\Delta^1_{M,N}` and secondary
    `\varprojlim^1H^0`; radial/Weyl means the
    `\Omega^{\mathrm{rad}}` / decorated PBW Stokes / signed-row
    obstruction surface; larger non-scalar QME means scalar projection,
    finite row arrays, `A^Mc=-r^M`, transition matrices, Roos
    compatibility, centrality homotopies, and a curved bulk-to-defect
    kernel.
12. For manuscript-proper writing, rewriting, or theorem-lane
    reconstitution, load and follow
    `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
    before editing.

13. Deep Supremum Discipline is mandatory.  Always take the harder
    route.  Never downgrade a theorem as a convenience move.  First seek
    the stronger true theorem by constructing the missing object,
    habitat, topology, comparison map, homotopy, kernel, counterterm,
    computation, verified source theorem, or obstruction class.  A
    conditional theorem is only a temporary ledger entry after the exact
    obstruction has been named.  A failed theorem surface must be
    reworked until it becomes either a proved theorem with all missing
    data supplied or a proved obstruction theorem naming the precise
    cohomology class, cokernel functional, Roos class, graph row, or
    finite-window matrix equation that blocks the original statement.
    Do not leave theorem surfaces merely `conditional', `external', or
    `expected' when a sharper construction problem can be inscribed.

## User-authorized max-effort swarm protocol

When the user explicitly asks for a large adversarial, rescue, review,
or cross-volume swarm, treat that as authorization to use the largest
useful swarm the runtime can support. Do not downshift because of old
3-agent, 5-agent, or 30-agent cautionary language. Request the strongest
available model and the highest available reasoning budget for research
agents when the host exposes those controls; when it does not, encode
the same requirement in the agent prompt: proof-grade, first-principles,
max-effort mathematical reasoning.

Swarm design must be explicit before launch: partition agents by
disjoint mathematical axes, files, or proof obligations; name the
integration owner; forbid agents from reverting work they did not make;
and require deep semantic merge across `~/chiral-bar-cobar`,
`~/chiral-bar-cobar-vol2`, and `~/topological-strings`.  Consult
`~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, or compact-CY source
fixtures only for an explicitly assigned matched-conventions comparison
or firewall audit.

Every attack-heal agent must return a compact, checkable report:
claim attacked, failure mode or proof, local file anchors, primary
source anchors where needed, exact formulas/constants, claim-status
recommendation, files changed, tests or computations run, and remaining
open questions. For theorem-level work, require repeated attack/heal
cycles until convergence: no new fatal attack survives, and at least
one real mathematical improvement is inscribed.  If the attack breaks a
theorem surface, the heal step must not stop at demotion: it must build
the missing theorem data or prove the exact obstruction theorem and
queue the next construction target.

The main thread integrates; agents do not vote truth into existence.
Preserve all mathematically substantive content, resolve conflicts by
examining both sides in context, and verify with targeted `rg`, local
computations, and session-end builds only when appropriate.

## How to work

Read `main.tex`, `mathmacros.tex`, and `commands.tex` in context before
editing. Use `rg` for symbols, theorem environments, graph-order
references, and bibliography keys. Preserve the manuscript's derivation
style: state the physical motivation, isolate the precise algebraic
claim, compute it in coordinates or complexes, then only afterwards
interpret it physically.

Prefer small, checkable patches. If changing a formula, record the
verification path in nearby prose or a concise comment only when it
helps future checking.

## Build

Use the Makefile at session end when needed:

```bash
make pdf
```

---

## Research-grade Codex / GPT-5 scaffolding (maximum settings)

Systematic restatement of the settings, discipline, and load order that already live in the narrative rules above — written for a Codex / GPT-5-family agent loading this file at session start.

### Harness — maximum always

| Parameter | Setting | Rationale |
|---|---|---|
| `reasoning_effort` | **`xhigh`** (always; never lower than `high`) | Mixed HT SFT / Kodaira-Spencer-type local BV / Costello graph-QME / $L_\infty$-renormalization — frontier mathematical physics. No downgrade permitted. |
| `model` | **Deepest host-exposed model**: GPT-5.5 Pro / Heavy in ChatGPT when available; GPT-5.5 or latest GPT-5-Codex-family model in Codex; API fallback latest GPT-5.4 / GPT-5-Codex model with `xhigh` where supported. | Pro-class mathematics + physics harness. |
| `verbosity` | As the argument requires | No abridgment of load-bearing expansions, anomaly-equation terms, or Feynman-graph sums. |
| Token budget | **Unbounded** for research tasks | If context fills, compact side work. Never elide a propagator term, a Feynman graph, or a named anomaly. |
| Tool use | **Parallel reads** for TeX + `scripts/` + figure sources | Batch `read_file` before writing. |
| Persistence | **Absolute** | Do not yield on a partial computation. Either close the calculation or name the open term precisely. |
| Self-reflection rubric | **Required** before any inscription | See `~/ecosystem/AGENTS-HARNESS.md §VIII`; instantiation below. |

### Long-form proof harness — GPT-5.5 Pro / Heavy analogue

Public OpenAI material describes GPT-5.5 Pro as the ChatGPT
research-grade option for the hardest long-running workflows and
GPT-5.5 in Codex as a 400K-context agentic coding model. The private
ChatGPT Pro harness is not public. This repo encodes the open analogue:
deepest model, maximum reasoning effort, large context, tool-grounded
verification, and repeated attack-heal cycles.

1. **Deliberation budget.** For theorem repair, cross-volume synthesis,
   adversarial review, or primary-source reconstruction, a 30-60 minute
   agent run is normal. Do not stop because the first plan is plausible.
   Stop only when the proof closes, a computation decides the point, or
   the exact open obligation is named.
2. **Private scratch, public proof trace.** Use private reasoning for
   search and synthesis; never expose raw scratchpad as an answer. The
   deliverable is the checked proof path: definitions, reductions,
   cited theorems, computations, and the remaining obstruction if any.
3. **Context before invention.** Load `CLAUDE.md`, this file, `main.tex`,
   preamble / macros / notation, diagram sources, compute scripts, cited
   local BV / Costello / Hamiltonian / Witten sources before the first
   mathematical edit. Load Vol III or compact-CY anchors only for an
   explicit comparison or firewall audit. Build an internal outline; do
   not write from memory.
4. **Multiple routes.** For any load-bearing identity, seek independent
   derivations: low-order amplitude, BV-degree check, graph computation,
   primary literature, local script, and cross-repo consistency.
   Agreement is evidence; disagreement is the deliverable.
5. **Adversarial loop.** After a proposed repair, attack the strongest
   failure mode: sign, measure, propagator, anomaly term, BV degree,
   large-N limit, or false transfer into Vol III. Heal, then attack again
   until no fatal objection survives.
6. **Agent topology.** Large swarms are partitioned by disjoint proof
   obligations or files. Subagents provide evidence, not authority. The
   main thread integrates by deep semantic merge and heals the proof,
   statement, or construction rather than voting truth into existence or
   degrading the manuscript.
7. **Progress reports.** Long runs emit compact `commentary` checkpoints:
   what has been read, what has been ruled out, what proof obligation
   remains. The final answer is short unless the proof itself is the
   requested artifact.

### Self-reflection rubric (before any revision, inscription, or merge)

| Category | Top-marks test |
|---|---|
| Correctness | Every expansion term, sign, measure, and BV degree verified. |
| Rigor | Every load-bearing claim carries *proved / conjectured / expected / heuristic / computed / folklore*. |
| Attribution | Every prior result cited by author + year + equation number when available (BCOV 1993 for source convention only, Costello 2011, Costello--Li 2012 when actually used, Witten 1988, and local BV / Hamiltonian references). |
| Concrete-before-abstract | A worked $F_g$ order precedes the general claim; first-/third-order figures are the anchor. |
| Voice | Russian school + mathematical-physics frontier (`INVARIANTS.md §IV`). |
| Standalone | No version labels, no phase labels, no prior-draft references (`INVARIANTS.md §III`). |
| Convention agreement | Local dimension \(2_{\mathbb R}+2_{\mathbb C}\), BV / Ext / cyclic / Weyl-Moyal conventions agree across this repo and Vol II. Vol III compact-CY conventions are checked only when a comparison theorem is explicitly in scope. |

If any category falls short — restart that category. Do not patch.

### Long-context handling

`main.tex` + preamble / commands / macros + bibliography + figures routinely exceed 10K tokens:

1. Outline internally before responding. Do not show the outline.
2. Parallel-`read_file` every cited source and every relevant script.
3. When quoting a numerical coefficient, a sign, or a normalization, cite the TeX line or the script that produced it.

### Research constellation (cross-repo awareness)

- `~/chiral-bar-cobar` — Vol I of the chiral bar–cobar series.
- `~/chiral-bar-cobar-vol2` — Vol II ($A_\infty$ chiral algebras + 3D HT QFT).
- `~/calabi-yau-quantum-groups` — Vol III (CY-to-chiral frontier). External comparison only. No compact CY$_3$, Vol III, or global BCOV theorem follows from this repository without a separate matched-conventions proof.
- `~/igusa-cusp-form` — Borcherds lift + BKM + $\Delta_5$. External comparison only. No BKM consequence follows from the local Hamiltonian BF/Moyal calculation alone.

Load-bearing claims in the core paper are local mixed-HT claims.  Claims
about compact \(F_g\), the holomorphic anomaly equation, worldsheet
instanton sums, mirror-symmetric corrections, CoHA, quintic arithmetic,
OSV/GV, or BKM are external comparison claims and must not be imported
into the core theorem surface without a separate theorem.

### Codex load order

1. `./CLAUDE.md`.
2. `~/ecosystem/INVARIANTS.md §IV` + `~/ecosystem/AGENTS-HARNESS.md §VIII`.
3. `~/chiral-bar-cobar-vol2/.agents/skills/chriss-ginzburg-rectify/SKILL.md`
   before manuscript-proper writing, rewriting, or theorem-lane
   reconstitution.
4. `main.tex` (root) + `preamble.tex` + `commands.tex` + `mathmacros.tex` + `notation.tex`.
5. Figure sources (`firstorder.svg`, `thirdordera.svg`, `thirdorderb.svg`) and `scripts/` for any quoted computation.
6. Cross-repo Vol III / Igusa / compact-CY sources only when an explicit comparison or firewall task requires them.

### Escalation — research-grade triggers (additional to `AGENTS-HARNESS.md §XVI`)

- A computation cannot be closed with honest rigor → the open term, named precisely, **is** the deliverable.
- A compact-CY, Vol III, CoHA, Igusa, or BKM claim appears inside the core local theorem surface → stop, report, and quarantine it unless the principal explicitly assigns a comparison theorem.
- A figure's contents disagree with the prose narrative → stop, report; the figure is usually the computation, overwrite only under the principal's direction.
