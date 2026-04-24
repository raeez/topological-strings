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
