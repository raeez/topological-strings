# AGENTS.md — topological-strings

> **Inherits `~/ecosystem/INVARIANTS.md`** — canonical ecosystem rules (model-agnostic): destructive-git forbidden list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, no-LLM-attribution in commits, deep-semantic-merges, intelligence propagation, open-source whitelist.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** — canonical Codex / GPT-5-family harness calibration: reasoning-effort per task class, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity control, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline, error-handling, git-and-worktree restatement for Codex defaults, frontend quality, no-LLM-commit-attribution, voice.
> **Mirrors this repo's `CLAUDE.md`** on substance. Before editing, `read_file ./CLAUDE.md`. `AGENTS.md` and `CLAUDE.md` must not diverge in facts; they may differ in structure and voice.
>
> **Model target.** Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model, `reasoning_effort=xhigh` for any non-trivial mathematical work (never lower than `high`). Terse, declarative voice per `INVARIANTS.md §IV`. No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge around Kodaira-Spencer gravity, BCOV-style topological string
amplitudes, twisted M-theory motivation, open/closed string field
theory, and Koszul-duality checks between brane operator algebras and
closed-string observables.

Every read, grep, edit, computation, proof repair, or retraction should
serve the manuscript `main.tex`: make the open-string Ext algebra,
AKSZ/BV action, cyclic-homology comparison, large-N single-trace limit,
and first/third-order quantum corrections precise enough to check
line by line.

## The mathematics you are working on

- Kodaira-Spencer gravity and BCOV quantum amplitudes.
- Topological A/B and mixed A-B models, branes, Ext algebras, and
  open string field theory.
- Twisted M-theory motivation on `\mathbb R \times X`.
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
  the CY-to-chiral, BKM, or Igusa-cusp-form repositories.

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
   merge discipline across all relevant research repositories.

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
and require deep semantic merge across
`~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`,
`~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, and
`~/topological-strings` whenever claims cross those repositories.

Every attack-heal agent must return a compact, checkable report:
claim attacked, failure mode or proof, local file anchors, primary
source anchors where needed, exact formulas/constants, claim-status
recommendation, files changed, tests or computations run, and remaining
open questions. For theorem-level work, require repeated attack/heal
cycles until convergence: no new fatal attack survives, and at least
one real mathematical improvement is inscribed.

The main thread integrates; agents do not vote truth into existence.
Preserve all mathematically substantive content, resolve conflicts by
reading both sides in context, and verify with targeted `rg`, local
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
| `reasoning_effort` | **`xhigh`** (always; never lower than `high`) | BCOV / Kodaira–Spencer / holomorphic-anomaly / $L_\infty$-renormalization — frontier mathematical physics. No downgrade permitted. |
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
   BCOV / Costello / Witten sources, and Vol III anchors before the first
   mathematical edit. Build an internal outline; do not write from memory.
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
| Attribution | Every prior result cited by author + year + equation number (BCOV 1993, Costello 2011, Costello–Li 2012, Witten 1988, Candelas–de la Ossa–Green–Parkes 1991). |
| Concrete-before-abstract | A worked $F_g$ order precedes the general claim; first-/third-order figures are the anchor. |
| Voice | Russian school + mathematical-physics frontier (`INVARIANTS.md §IV`). |
| Standalone | No version labels, no phase labels, no prior-draft references (`INVARIANTS.md §III`). |
| Convention agreement | CY degree $d$, worldsheet $\Sigma$, framing $S^3$, BV / Ext / cyclic conventions agree with Vol III (`~/calabi-yau-quantum-groups`) when stated in both. |

If any category falls short — restart that category. Do not patch.

### Long-context handling

`main.tex` + preamble / commands / macros + bibliography + figures routinely exceed 10K tokens:

1. Outline internally before responding. Do not show the outline.
2. Parallel-`read_file` every cited source and every relevant script.
3. When quoting a numerical coefficient, a sign, or a normalization, cite the TeX line or the script that produced it.

### Research constellation (cross-repo awareness)

- `~/chiral-bar-cobar` — Vol I of the chiral bar–cobar series.
- `~/chiral-bar-cobar-vol2` — Vol II ($A_\infty$ chiral algebras + 3D HT QFT).
- `~/calabi-yau-quantum-groups` — Vol III (CY-to-chiral frontier). BCOV / Kodaira–Spencer is the **physics dual** of the chiral homology of a CY threefold; conventions must agree when stated in both, and any divergence is load-bearing.
- `~/igusa-cusp-form` — Borcherds lift + BKM + $\Delta_5$. The modular generating functions that appear in the topological-string partition function (elliptic genera, $\mathcal{N}=4$ / second-quantized $K3$) tie to the Borcherds / BKM route there.

Load-bearing claims about $F_g$, the holomorphic anomaly equation, worldsheet instanton sums, or mirror-symmetric corrections must be consistent with the Vol III CY frontier. Disagreement is the deliverable; report, do not silently reconcile.

### Codex load order

1. `./CLAUDE.md`.
2. `~/ecosystem/INVARIANTS.md §IV` + `~/ecosystem/AGENTS-HARNESS.md §VIII`.
3. `main.tex` (root) + `preamble.tex` + `commands.tex` + `mathmacros.tex` + `notation.tex`.
4. Cross-repo: `~/calabi-yau-quantum-groups/FRONTIER.md` for convention alignment.
5. Figure sources (`firstorder.svg`, `thirdordera.svg`, `thirdorderb.svg`) and `scripts/` for any quoted computation.

### Escalation — research-grade triggers (additional to `AGENTS-HARNESS.md §XVI`)

- A computation cannot be closed with honest rigor → the open term, named precisely, **is** the deliverable.
- A convention disagreement with `~/calabi-yau-quantum-groups` → stop, report; let the principal decide which tree is canonical.
- A figure's contents disagree with the prose narrative → stop, report; the figure is usually the computation, overwrite only under the principal's direction.
