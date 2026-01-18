# OrchestraBench

_Which Multi-Agent LLM Topology Fits Which Task?_

> A 794-run benchmark across flat / hierarchical / debate topologies on Claude Opus 4.6 + Sonnet 4.6, plus the **DIT framework** (Decomposability, Iterativeness, Tool-diversity) for predicting which topology fits which task.

**Target venue:** [NeurIPS 2026](https://neurips.cc/Conferences/2026)  •  **Status:** Submission package compiled (PDF: 298 KB)

---

## 📋 Headline Numbers

| Metric | Value |
|---|---|
| Topologies evaluated | 3 (flat, hierarchical, debate) |
| Tasks | 82 across coding / research / reasoning |
| Total runs | 794 (3-seed replication) |
| Best topology overall | Debate — 65.4% (±0.8) |
| DIT routing accuracy | 90% |
| Topology vs compute split | ~2/3 of multi-agent gains attributable to topology, 1/3 to compute |

## 📄 Abstract (excerpt)

Multi-agent LLM systems can be organized into distinct orchestration topologies, yet practitioners have no principled basis for choosing among them. We hypothesize that each topology encodes a structural prior, and that alignment between this prior and a task's measurable characteristics predicts performance. To test this, we introduce OrchestraBench and evaluate three topologies (flat conversation, hierarchical decomposition, and multi-agent debate) on 82 tasks spanning coding, research, and reasoning, with three-seed replication producing 738 primary runs on Claude Opus 4.6, plus secondary-backbone and agent-count controls totaling 794 runs.

## 🤖 Independent Review (Sakana AI Scientist v2)

This paper has been reviewed by [Sakana AI Scientist v2](https://github.com/SakanaAI/AI-Scientist-v2)'s `perform_llm_review` module via the MiniMax-M2.7 backend. The review uses NeurIPS-style reviewer guidelines.

| Metric | Score |
|---|---|
| Overall | **7** / 10 |
| Decision | **Accept** |
| Soundness | 3 / 4 |
| Confidence | 4 / 5 |

**Top weaknesses identified:**

- Only 3 of 5 characterized topologies evaluated; role-playing and RL-orchestrated topologies remain unvalidated
- Tasks are author-created with no third-party annotation; potential for authorship bias
- Primary evaluation uses only Claude Opus 4.6; Sonnet 4.6 check limited to 12 easy tasks (ceiling effect)
- DIT scores assigned by authors (κ≥0.79 but no external validation); annotator agreement may not hold across different annotator populations
- Limited domain coverage (coding, research, reasoning); missing creative generation, long-document analysis, embodied control

> _Full review JSON: [`ai_scientist/reviews/minimax_review.json`](ai_scientist/reviews/minimax_review.json)._

## 🔬 Reproducibility

```bash
# Clone
git clone https://github.com/jrajath94/paper1_orchestrabench.git
cd paper1_orchestrabench

# Recompile the PDF (needs Tectonic or pdflatex)
tectonic output/paper.tex   # produces output/paper.pdf

# Browse the materials:
#   output/sections/   — per-section markdown + .tex
#   output/figures/    — figures (PDF + PNG)
#   output/reviews/    — citation, data, math, figure, AI-pattern audits
#   experiments/       — task suite + results JSON
#   ai_scientist/      — Sakana AI Scientist v2 review pipeline outputs
```


## 📁 Repository Layout

```
paper1_orchestrabench/
├── README.md              ← you are here
├── paper.pdf              ← compiled PDF
├── output/                ← LaTeX source, sections, figures, reviews, bibliography
│   ├── paper.tex / main.tex
│   ├── sections/
│   ├── figures/
│   ├── reviews/           (audits: citation, data, math, figure, consistency, AI patterns)
│   └── bibliography.bib / references.bib
├── experiments/           ← task suite + results data
├── scripts/               ← pipeline scripts (literature retrieval, citation verification, etc.)
├── ai_scientist/          ← Sakana AI Scientist v2 outputs (independent review JSON)
├── state/                 ← paper state and pipeline log
└── venues/                ← venue configs (NeurIPS / TMLR / JAIR formatting rules)
```

## 🛠️ Tooling

This paper was developed with a custom multi-agent research pipeline using:
- **Claude Opus 4.6 / Sonnet 4.6** (via [Claude Code](https://www.anthropic.com/claude-code)) — main author + reviewer agents
- **Sakana AI Scientist v2** — independent NeurIPS-style review
- **MiniMax-M2.7** — bulk-pass review and ideation calls
- **Tectonic** — LaTeX compilation
- **Semantic Scholar / OpenAlex / CrossRef** APIs for citation verification

## 📚 Part of the Multi-Agent Orchestration paper series

| # | Repo | Title | Venue |
|---|---|---|---|
| 1 | [`paper1_orchestrabench`](https://github.com/jrajath94/paper1_orchestrabench) | OrchestraBench: which topology fits which task? | NeurIPS 2026 |
| 2 | [`paper2_cost_routing`](https://github.com/jrajath94/paper2_cost_routing) | Cost-Aware Topology Routing | NeurIPS 2026 (W) |
| 3 | [`paper3_failure_planning`](https://github.com/jrajath94/paper3_failure_planning) | Failure-Aware Planning for LLM Agents | TMLR |
| 4 | [`paper4_paretorch`](https://github.com/jrajath94/paper4_paretorch) | ParetOrch: Cost-Quality Pareto Optimization | NeurIPS 2026 |
| 5 | [`paper5_adaptswitch`](https://github.com/jrajath94/paper5_adaptswitch) | AdaptSwitch: Runtime Topology Switching | JAIR |

## 📜 License

Code: MIT.  Paper text and figures: CC BY 4.0.

## 🤝 Citation

If you use this work, please cite (BibTeX entries to be finalized at submission):

```bibtex
@article{paper1_orchestrabench_2026,
  title  = {OrchestraBench: Which Multi-Agent LLM Topology Fits Which Task?},
  author = {Rajath, J.},
  year   = {2026},
  journal= {Under review at NeurIPS 2026},
}
```
