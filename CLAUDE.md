# CLAUDE.md — topological-strings

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation. Read it first. Repo-local rules follow.

---

## Repo-local

Computations and remarks on **Kodaira–Spencer gravity and quantum string amplitudes in topological string theory** — extending the Bershadsky–Cecotti–Ooguri–Vafa (BCOV, 1993) framework for the closed topological B-model on Calabi–Yau threefolds. Physics companion to the Vol III CY-to-chiral frontier held in `~/calabi-yau-quantum-groups`.

**Source layout.**

- `main.tex` — root.
- `abstract.tex`, `preamble.tex`, `authors.tex`, `commands.tex`, `mathmacros.tex`, `notation.tex`, `nomenclature.tex` — bound parts.
- `Makefile` — `make` builds the PDF via `pdflatex`.
- `firstorder.{png,svg}`, `thirdordera.{png,svg}`, `thirdorderb.{png,svg}` — diagram assets.
- `scripts/` — computation scripts.
- `amstex-template`, `tex-documentation` — build apparatus.

**Research constellation role.** BCOV / Kodaira–Spencer gravity is the physics dual to the chiral homology of a Calabi–Yau threefold: the closed-string amplitude stratification at $\hat{s}$. Conventions ($d = \dim_{\mathbb{C}} X$, worldsheet $\Sigma$, framing datum on $S^3$) must agree with Vol III (`~/calabi-yau-quantum-groups`) when stated in both. Any divergence is load-bearing — report, do not silently reconcile.

Modular-form frontier: the generating functions that appear here tie to the Igusa cusp form $\Delta_5$ construction in `~/igusa-cusp-form` via the Borcherds / BKM route.

**Voice.** `~/ecosystem/INVARIANTS.md §IV` — Russian mathematical school + mathematical-physics frontier. Named attribution (Bershadsky–Cecotti–Ooguri–Vafa 1993, Witten 1988, Costello 2011, Polyakov 1987), honest epistemic status, physical intuition and formal rigor coexisting without either subordinating the other.

## Long-form proof harness

For Claude Code, Codex CLI, and any GPT-5.5 / GPT-5-Codex-class agent,
frontier mathematical physics runs in maximum-effort mode. Use the
deepest host-exposed model and reasoning budget. If the host offers a
GPT-5.5 Pro / Heavy or `xhigh` setting, use it for theorem repair,
cross-repo synthesis, adversarial review, and primary-source
reconstruction. The private ChatGPT Pro harness is not public; this is
the open local analogue.

Long runs are normal. A 30-60 minute agent run is acceptable when a
proof obligation requires it. Load `main.tex`, preamble / macro files,
diagram sources, compute scripts, cited BCOV / Costello / Witten
sources, and Vol III / Igusa anchors before the first mathematical
edit. Private scratch stays private; the deliverable is the checked
proof trace and the exact remaining obstruction.

After every proposed repair, run an attack-heal loop: sign, measure,
propagator, anomaly term, BV degree, graph order, large-N limit, or
false transfer into Vol III. Heal and attack again until the theorem
closes or the exact obstruction is named for the next repair cycle. Do
not downgrade the manuscript to close the loop. Subagents provide
evidence, not authority; the main thread integrates by deep semantic
merge.
