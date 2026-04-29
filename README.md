# Closed Hamiltonian BF Theory as a Derived Poisson Centre

This repository contains a research manuscript on the formal local
mixed holomorphic-topological Dirac brane model on
\(\mathbb R^2\times\mathbb C^2\).  The source of the paper is
`main.tex`, with front matter and support files split into the adjacent
`.tex` files.

The manuscript builds a universal formal-local Koszul duality theory:
finite cotangent CE/PV, completed formal-disk CE/PV, the closed-open
generator map \(c^I\mapsto\theta^I\), \(u_I\mapsto O_I\), the
admissible Tate bar-cobar/Quillen envelope, primitive higher-\(\psi\)
Koszul sectors, the \(\mathcal D_\hbar\) Fourier--Rees bridge and its
same-action obstruction, weighted finite-window regulator independence,
endpoint criteria, unreduced factorization-current lift data, and
global/descent acceptance criteria.  Analytic and global claims enter
through named obstruction complexes rather than by transfer from the
formal disk alone.

## Build

Prerequisites: a TeX installation with `pdflatex`, `makeindex`, GNU
`make`, and the local style files available to TeX.

Common targets:

```bash
make pdf
make quick
make standalone
make help
```

The main PDF is written to `out/main.pdf`.  Build success is a TeX
integrity check; it is not a mathematical certification.

## Source Layout

- `main.tex` is the root file.
- `abstract.tex`, `claim-strength-ledger.tex` (programme theorem interface),
  and `local-dictionary.tex` are rendered before the table of contents.
- `mathmacros.tex`, `commands.tex`, `notation.tex`, and
  `nomenclature.tex` hold notation and macro support.
- `scripts/` contains finite checks for local computations.
- `standalone/` holds standalone TeX artifacts built by
  `make standalone`.
