# arXiv Submission Metadata

## Title
Orchestration Topology Benchmarking: Which Multi-Agent LLM Architecture Fits Which Task?

## Authors
[Your name(s) here — add before submission]

## Abstract
Multi-agent LLM systems can be organized into distinct orchestration topologies, yet practitioners have no principled basis for choosing among them. We hypothesize that each topology encodes a structural prior, and that alignment between this prior and a task's measurable characteristics predicts performance. To test this, we introduce OrchestraBench and evaluate three topologies (flat conversation, hierarchical decomposition, and multi-agent debate) on 82 tasks spanning coding, research, and reasoning, with three-seed replication producing 738 primary runs on Claude Opus 4.6, plus 36 secondary-backbone runs (Claude Sonnet 4.6) and 20 agent-count control runs, totaling 794 runs. The results split cleanly by difficulty, with non-overlapping 95% confidence intervals between flat and both multi-agent topologies. Debate achieves the highest overall accuracy at 65.4% (+-0.8), followed by hierarchical at 55.7% (+-4.2) and flat at 28.9% (+-2.1). The pattern of wins tracks task structure: hierarchical reaches 75% on high-decomposability tasks versus 42% for debate (+33pp), while debate reaches 77% on high-iterativeness tasks versus 14% for hierarchical (+63pp). A routing classifier built on our decomposability-iterativeness-tool-diversity (DIT) framework achieves 97.6% accuracy on 42 strongly-typed tasks. A flat-2x-budget control experiment shows that topology structure accounts for roughly two-thirds of the multi-agent advantage over flat baselines, with additional compute explaining the remaining third. We release our task suite and a topology selection guide mapping task characteristics to recommended architectures.

## Categories (pick during submission)
- **Primary:** cs.MA (Multi-Agent Systems)
- **Cross-list:** cs.AI (Artificial Intelligence), cs.CL (Computation and Language)

## Comments field
13 pages (9 main + 2 appendix + 2 references), 5 figures, 6 tables. Under review at NeurIPS 2026. Code and task suite to be released upon acceptance.

## MSC classes (optional)
68T42 (Agent technology), 68T05 (Learning from experience)

## ACM classes (optional)
I.2.11 (Distributed Artificial Intelligence -- Multi-agent systems)

---

# Submission Checklist

## Before uploading to arXiv:

- [ ] **Add real author names** to paper.tex (line 20: currently "Anonymous")
  - For arXiv preprint: use real names
  - For NeurIPS submission: keep "Anonymous" (double-blind)
  - **Strategy:** Submit to arXiv with real names, submit to NeurIPS with anonymous version

- [ ] **Switch NeurIPS package mode** for arXiv version:
  - Change `\usepackage[preprint]{neurips_2025}` (shows "Preprint" header)
  - Keep `\usepackage{neurips_2025}` for NeurIPS blind submission (no header)

- [ ] **Verify PDF compiles clean:** `cd paper/output && tectonic paper.tex`

- [ ] **Check file size:** arXiv limit is 50MB for single upload (we're at 178KB -- no issue)

- [ ] **Prepare source bundle:**
  ```bash
  cd paper/output
  tar -czf orchestrabench-arxiv.tar.gz \
    paper.tex \
    bibliography.bib \
    neurips_2025.sty \
    sections/*.tex \
    figures/fig1_dit_space.pdf \
    figures/fig2_main_results.pdf \
    figures/fig3_crossover.pdf \
    figures/fig4_routing_ablation.pdf \
    figures/fig5_agent_control.pdf
  ```

- [ ] **Upload to https://arxiv.org/submit** (requires arXiv account)

- [ ] **Post-submission:** Share the arXiv link on:
  - Twitter/X with #NeurIPS2026 #MultiAgent #LLM tags
  - r/MachineLearning (weekly "What are you working on?" thread)
  - ML Collective Discord

---

# Dual Submission Strategy

| Version | Author | Package | Where |
|---------|--------|---------|-------|
| arXiv preprint | Real names | `[preprint]{neurips_2025}` | arxiv.org |
| NeurIPS submission | "Anonymous" | `{neurips_2025}` | openreview.net |

NeurIPS allows concurrent arXiv posting. From the NeurIPS policy:
> "We do not consider a paper submitted to arXiv.org to be a dual submission."

So you can post to arXiv with your name AND submit anonymously to NeurIPS simultaneously.

---

# Timeline

| Date | Action |
|------|--------|
| Now (March 2026) | Post to arXiv, collect feedback |
| April 2026 | Incorporate feedback, finalize |
| ~May 2026 | NeurIPS 2026 submission deadline |
| ~Sep 2026 | NeurIPS reviews back |
| Dec 2026 | NeurIPS 2026 conference |
