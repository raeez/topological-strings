# Legacy 2018 Feynman Diagram Sketches

Status: legacy archive evidence, reconciled locally on 2026-04-30.

This directory preserves the six historical Feynman-diagram sketch assets
which previously lived at the repository root:

- `firstorder.png`
- `firstorder.svg`
- `thirdordera.png`
- `thirdordera.svg`
- `thirdorderb.png`
- `thirdorderb.svg`

The assets are archived evidence, not current manuscript inputs. A usage
grep on 2026-04-30 found no direct references to these asset names in
`main.tex`; `Makefile` only has generic PNG handling. `CLAUDE.md` and
`AGENTS.md` still mention the old root paths in this checkout. Those
control-document edits belonged to Agent 060 and were not made in this
reconciliation lane.

## Provenance

Before this archive move, `git ls-files --stage` listed the six assets at
the repository root with these Git blob identifiers:

| Root path | Git blob |
|---|---|
| `firstorder.png` | `10f4a555f228ef03a6cef81e3a0d1267ef941d63` |
| `firstorder.svg` | `4bc2e45731d0d1e2e58279de2310381483352b79` |
| `thirdordera.png` | `945d0aaec4361052b4235ec3b52ff0008a21bb31` |
| `thirdordera.svg` | `0e53d44a4e14794757e32517261e684ea5f6f1ce` |
| `thirdorderb.png` | `0284d1d24c4b9357598e7b407bffe5ecb3ae0193` |
| `thirdorderb.svg` | `41f4c8d4f64d3f5772e024aebe317586a6474b0a` |

The archive move was performed with `git mv`; the cached diff reports each
asset as an `R100` rename. The SHA-256 content digests after the move are:

| Archive path | SHA-256 |
|---|---|
| `firstorder.png` | `bd9ae2e9fbed719c50214f3022f94945b924a59351cf16b08b804f39638c824b` |
| `firstorder.svg` | `5e10c16ddb780e011103db7bb9428a6ff96abf0961026433153eb52f74314206` |
| `thirdordera.png` | `2816c5237ab87afa35754496d6f77ead9de8dea269e8ebe24a667b973698c49b` |
| `thirdordera.svg` | `ea073e1f1826ff2ede60b492dcc099054b8e92772d24bf5fe28ca29b6556bdc4` |
| `thirdorderb.png` | `4df740d828c89eb6660435558a99a995d8ca41ff796b428f50f10ad81b350cfc` |
| `thirdorderb.svg` | `45ed8819f4c22335fb6c8e8507cc657feadfe1d74e1315a7c2619a83dc9c4adc` |

No asset was deleted as evidence. The root-path removals are the source
side of the recorded archive renames.
