# OrchestraBench

_Which Multi-Agent LLM Topology Fits Which Task?_

> A research study evaluating three orchestration topologies (flat, hierarchical, debate) on custom task suites, introducing the **DIT framework** (Decomposability, Iterativeness, Tool-diversity) for predicting topology-task fit.

**Target venue:** [NeurIPS 2026](https://neurips.cc/Conferences/2026)  •  **Status:** Submission package compiled (PDF: 305 KB)

## Abstract (excerpt)

Multi-agent LLM systems can be organized into distinct orchestration topologies, yet practitioners have no principled basis for choosing among them. We hypothesize that each topology encodes a structural prior, and that alignment between this prior and a task's measurable characteristics predicts performance. To test this, we introduce OrchestraBench and evaluate three topologies (flat conversation, hierarchical decomposition, and multi-agent debate) on 82 tasks spanning coding, research, and reasoning.

## Reproducibility

```bash
# Clone
git clone https://github.com/jrajath94/paper1_orchestrabench.git
cd paper1_orchestrabench

# Recompile the PDF (needs Tectonic or pdflatex)
tectonic output/paper.tex   # produces output/paper.pdf

# Browse the materials:
#   output/sections/   — per-section markdown + .tex
#   output/figures/    — figures (PDF + PNG)
#   experiments/       — task suite + results JSON
```


## Repository Layout

```
paper1_orchestrabench/
├── README.md              ← you are here
├── paper.pdf              ← compiled PDF
├── output/                ← LaTeX source, sections, figures, bibliography
│   ├── paper.tex / main.tex
│   ├── sections/
│   ├── figures/
│   └── bibliography.bib / references.bib
├── experiments/           ← task suite + results data
├── scripts/               ← pipeline scripts (literature retrieval, citation verification, etc.)
├── state/                 ← paper state and pipeline log
└── venues/                ← venue configs (NeurIPS / TMLR / JAIR formatting rules)
```

## Tooling

This paper was developed with a custom multi-agent research pipeline using:
- **Claude Opus 4.6 / Sonnet 4.6** (via [Claude Code](https://www.anthropic.com/claude-code)) — main author + reviewer agents
- **MiniMax-M2.7** — bulk-pass review and ideation calls
- **Tectonic** — LaTeX compilation
- **Semantic Scholar / OpenAlex / CrossRef** APIs for citation verification

## Part of the Multi-Agent Orchestration paper series

| # | Repo | Title | Venue |
|---|---|---|---|
| 1 | [`paper1_orchestrabench`](https://github.com/jrajath94/paper1_orchestrabench) | OrchestraBench: which topology fits which task? | NeurIPS 2026 |
| 2 | [`paper2_cost_routing`](https://github.com/jrajath94/paper2_cost_routing) | Cost-Aware Topology Routing | NeurIPS 2026 (W) |
| 3 | [`paper3_failure_planning`](https://github.com/jrajath94/paper3_failure_planning) | Failure-Aware Planning for LLM Agents | TMLR |
| 4 | [`paper4_paretorch`](https://github.com/jrajath94/paper4_paretorch) | ParetOrch: Cost-Quality Pareto Optimization | NeurIPS 2026 |
| 5 | [`paper5_adaptswitch`](https://github.com/jrajath94/paper5_adaptswitch) | AdaptSwitch: Runtime Topology Switching | JAIR |

## License

Code: MIT.  Paper text and figures: CC BY 4.0.

## Citation

If you use this work, please cite (BibTeX entries to be finalized at submission):

```bibtex
@article{paper1_orchestrabench_2026,
  title  = {OrchestraBench: Which Multi-Agent LLM Topology Fits Which Task?},
  author = {Rajath, J.},
  year   = {2026},
  journal= {Under review at NeurIPS 2026},
}
```
