# NeurIPS 2026 Final Peer Review -- Round 2

**Paper:** Topology-Task Alignment for Multi-Agent LLM Orchestration (OrchestraBench)
**Review round:** 2 (post-revision)
**Date:** 2026-03-15
**Prior aggregate score:** 5.6/10
**Changes since Round 1:** Real experiment data (96 runs), reduced scope to 3 topologies, all placeholder numbers replaced, Spearman misuse corrected, DIT contradictions resolved, baselines clarified, sections trimmed to NeurIPS length.

---

## Review 1: Methodology Skeptic

**Reviewer focus:** Experimental rigor, controls, statistical claims, validity of conclusions from the data.

### Scores

| Dimension    | Score | Justification |
|--------------|-------|---------------|
| Quality      | 6     | Real data now exists and the experimental traces are detailed. 96 runs across 32 tasks x 3 topologies is small but the effect sizes are large enough to be informative. The paper is honest about its limitations. However, the sample size does not support several of the finer-grained claims, and the single-run-per-cell design (no repeated trials) prevents any variance estimation. |
| Clarity      | 7     | The results section is well structured: main table, difficulty-dependent analysis, token efficiency, limitations. The admission that 32 tasks "can and cannot establish" specific things is refreshingly direct. Minor issues with notation consistency between the methods and results sections. |
| Originality  | 7     | The DIT framework remains a novel contribution. The scaled experiment's core finding -- that topology differentiation is invisible on easy tasks and dramatic on hard tasks -- is a genuinely useful insight that the community has not documented before. |
| Significance | 6     | The direction of the findings is clear and practically useful. The 85pp flat degradation on hard tasks is a striking result. But the 32-task corpus is too small for the selection guide to be trusted as a deployment tool, and the paper acknowledges this. |

**Overall recommendation: Weak Accept**

### Strengths

1. **Real experiment data with task-level detail.** Every one of the 32 tasks has full traces, failure mode analysis, and per-topology summaries in the experiment JSON. This is a major improvement over Round 1's placeholder numbers. The data is transparent enough for reviewers to verify the claims independently.

2. **Honest and specific limitations section.** The paper explicitly states: no repeated trials, single model backbone, 96 runs is enough to see the trend but not enough for tight CIs, the debate-vs-hierarchical gap (78.1% vs 71.9%) could shift with more data. This is the right level of epistemic humility for the sample size.

3. **The difficulty-dependent finding is load-bearing and well-supported.** The 12 easy tasks show ceiling effects (95.8-100% across all topologies). The 20 hard tasks show sharp separation (flat 10%, hierarchical 55%, debate 65%). This is not an artifact of cherry-picking -- the pilot explicitly demonstrates why small easy-only studies are misleading.

### Weaknesses

1. **No repeated trials means no variance estimation.** Each task-topology pair ran exactly once. The paper cannot report confidence intervals, standard errors, or p-values for any comparison. The flat vs. multi-agent gap (42.5% vs 71.9-78.1%) is large enough to survive resampling, but the hierarchical vs. debate gap (6.2 percentage points = 2 tasks) is well within the range that a single lucky/unlucky LLM sample could flip. The paper says this but should emphasize it more prominently -- a reader scanning Table 1 may take the debate > hierarchical ordering as established fact.

2. **DIT annotations were author-assigned, not independently validated.** The Round 1 review flagged annotation circularity -- that DIT scores from reference trajectories are path-dependent. Round 2 addresses this partially: the methods section defines D, I, T operationally, and the experiment JSON includes DIT values for all 20 hard tasks. But the annotations were still assigned by the paper authors. For a claim that hierarchical wins cluster on "high-D tasks (mean D=0.84)" and debate wins cluster on "high-I tasks (mean I=0.87)," the DIT values are load-bearing. Independent annotation by external raters, at least on a subset, would substantially strengthen this claim. As it stands, there is a risk that the DIT values were (consciously or unconsciously) tuned to fit the topology-win pattern.

3. **The paper's framing oscillates between two scopes without resolving the tension.** The introduction and methods describe OrchestraBench as a 500-task, 5-topology, 2500-pair controlled study with Spearman correlations, bootstrap CIs, and LOO cross-validation. The results section reports a 32-task, 3-topology, 96-run pilot-plus-scaled study with no statistical tests. These are two different papers. The ambitious methods section sets expectations that the results section cannot meet. The authors should either (a) scope the entire paper to the 32-task study and rewrite the methods accordingly, or (b) acknowledge the current results as preliminary and the full OrchestraBench as future work. The current hybrid is confusing.

### Overall Assessment

The paper has improved substantially from Round 1. The real experiment data tells a clear story: topology choice is invisible on easy tasks and decisive on hard tasks, with hierarchical excelling on decomposable problems and debate excelling on iterative ones. The effect sizes are large enough to be informative despite the small sample. The main risk is the scope mismatch between the methods (which promise 2500 pairs) and the results (which deliver 96). If the authors can resolve this framing issue and add even modest repeated trials, this is a solid contribution.

---

## Review 2: Novelty Assessor

**Reviewer focus:** Contribution significance, gap validity, NeurIPS caliber, whether the findings advance the field.

### Scores

| Dimension    | Score | Justification |
|--------------|-------|---------------|
| Quality      | 7     | The core finding is supported by real data with detailed task-level traces. The experiment design (shared LLM backbone, identical prompts, controlled variables) isolates the topology variable more cleanly than any prior work. The 32-task scope is modest but the effect sizes compensate. |
| Clarity      | 7     | The paper reads well. The results section's structure (main table, difficulty analysis, token efficiency, limitations) is logical. The DIT framework is explained clearly with worked examples. The bibliography is comprehensive. |
| Originality  | 8     | This is the first paper to demonstrate, with real controlled experiments, that topology choice has near-zero impact on easy tasks and 55-85pp impact on hard tasks. The DIT-alignment finding -- that decomposable tasks favor hierarchical and iterative tasks favor debate -- is intuitive but had never been empirically validated. The routing result (90% accuracy vs 65% best single) is promising. |
| Significance | 7     | The difficulty-dependent topology advantage is a finding that will change how practitioners think about multi-agent orchestration. The common wisdom is "use the fanciest topology available." This paper shows that the fanciest topology is wasted on easy tasks and the wrong fancy topology fails on hard tasks. That is immediately actionable. |

**Overall recommendation: Weak Accept**

### Strengths

1. **The gap is real and this paper closes a meaningful piece of it.** Round 1's Novelty Assessor flagged the "zero cross-cluster citation edges" claim as potentially overstated. The Round 2 paper sidesteps this by focusing on a more defensible claim: no prior work has compared topology effectiveness under controlled conditions on the same tasks. The experiment data validates this -- even on 32 tasks, the topology differentiation is stark.

2. **The DIT-based routing result is the strongest novel contribution.** The paper reports that a simple DIT-based routing function achieves 90% accuracy in predicting the best topology, compared to 65% for always picking the best single topology (debate). On 20 hard tasks, this means DIT routing would correctly assign 18 tasks vs. 13 for debate-always. If this holds at scale, it is a genuine advance over the status quo of picking one topology and hoping.

3. **The failure mode analysis is unusually detailed and publishable on its own.** The experiment JSON contains per-task failure explanations that read as mini case studies. HARD-CODE-02 (race conditions): hierarchical decomposes by function, missing cross-function interactions that debate's union-of-perspectives catches. HARD-CODE-03 (payment refactor): debate produces two incompatible interface designs that are harder to merge than to build from scratch. These specific, mechanistic explanations of why topologies succeed or fail in particular DIT regions are more valuable than aggregate statistics.

### Weaknesses

1. **The contribution reduces from a framework to a finding.** The introduction promises "OrchestraBench: controlled cross-topology evaluation at scale" (2500 pairs) and "the first topology selection guide." The actual delivery is a 32-task, 3-topology study with qualitative selection guidance. This is still valuable, but it is a research finding ("topology matters on hard tasks, and the DIT profile predicts which wins"), not a benchmark or a selection framework. The paper's positioning should match its actual contribution.

2. **Three topologies do not exhaust the design space, and two of the five original topologies were dropped.** The Round 1 paper studied five topologies (flat, hierarchical, role-playing, DAG-based, RL-orchestrated). Round 2 studies three (flat, hierarchical, debate). The paper does not adequately explain why the other two were dropped. If the answer is "they were too expensive to run," that is understandable but should be stated. If the answer is "they added noise without differentiation," that is itself a finding worth reporting. The silence creates a gap.

3. **The 90% routing accuracy claim needs more scrutiny.** On 20 hard tasks: hierarchical is the sole winner on 7, debate on 8, both win on 3, all win on 1, none win on 1. A routing function that picks debate for high-I and hierarchical for high-D correctly routes at least 15/20 = 75% without any learning. The 90% figure presumably comes from including the easy tasks (where any topology works, so any routing is correct). This inflates the routing accuracy with trivially correct predictions. The paper should report routing accuracy on hard tasks only, where the choice actually matters.

### Overall Assessment

Round 2 transforms this from a paper with no data to a paper with a clear, well-supported empirical finding. The topology-difficulty interaction is the key result: easy tasks mask topology differences, hard tasks reveal them, and the DIT profile predicts which topology wins. This is a genuine contribution to the multi-agent orchestration literature, even at the current scale. The main concern is the mismatch between the paper's ambitious framing (OrchestraBench as a large-scale benchmark) and its actual delivery (a 32-task controlled study). If repositioned as a focused empirical study with a clear finding rather than a benchmark launch, this is above the NeurIPS acceptance bar.

---

## Review 3: Clarity Reviewer

**Reviewer focus:** Writing quality, AI detection, page fit, presentation, consistency.

### Scores

| Dimension    | Score | Justification |
|--------------|-------|---------------|
| Quality      | 6     | The paper's empirical content is now real, which resolves the fatal flaw from Round 1. The data-to-claim ratio is reasonable -- the paper does not overclaim given 96 runs. Some structural issues remain (scope mismatch between methods and results). |
| Clarity      | 8     | Writing is strong throughout. Active voice, varied sentence structure, concrete examples. The results section is particularly well written -- the opening ("Table 1 tells the story") is direct, the difficulty-dependent analysis flows logically, and the limitations are specific rather than boilerplate. Minimal jargon, no filler paragraphs. |
| Originality  | 7     | Same as prior assessment. The DIT framework and the topology-difficulty interaction are novel. The controlled experimental design is a first in this subfield. |
| Significance | 6     | Solid contribution with clear practical implications. The finding that topology choice is a "first-class design variable" is well-supported at the current scale. Limited by the 3-topology, 32-task scope. |

**Overall recommendation: Weak Accept**

### Strengths

1. **AI pattern detection: clean.** The Round 1 Clarity Reviewer flagged one instance of "landscape" in the related work. Round 2 sections read as human-authored. No em dashes detected. No "delve," "crucial," "notably," "leveraging," or other AI-pattern vocabulary. Sentence structure varies naturally -- short declarative sentences alternate with longer explanatory ones. The opening of the results section ("Table 1 tells the story. On 12 easy tasks, all three topologies looked competitive. On 20 hard tasks, they separated sharply.") reads as confident human writing, not generated text.

2. **The limitations section is exemplary.** Five specific limitations, each with a concrete statement of what the paper can and cannot establish. "The difference between debate (78.1%) and hierarchical (71.9%) overall is 2 tasks out of 32. We do not claim that gap is statistically significant." This is the kind of honesty that builds reviewer trust. The section also correctly identifies the single-model-backbone limitation and the lack of repeated trials.

3. **Token efficiency analysis is presented with the right framing.** The paper does not simply report raw token counts (which would favor flat). Instead, it computes cost-per-correct-answer: flat spends ~24,900 tokens per success vs. ~7,250 for debate on hard tasks. This reframes efficiency correctly -- spending fewer tokens to fail is not efficiency.

### Weaknesses

1. **The methods section describes a different (larger) study than what was executed.** Section 3 describes 500 tasks, 5 topologies, 2500 pairs, Spearman correlations, bootstrap CIs, and LOO cross-validation. Section 5 reports 32 tasks, 3 topologies, 96 runs, and no statistical tests. A NeurIPS reviewer encountering this mismatch will wonder whether the methods section was written before the experiments were scoped down and never updated. This is the single most important revision needed: either (a) rewrite Section 3 to describe the actual 32-task, 3-topology experiment, or (b) clearly label the current results as "Phase 1" of the full OrchestraBench and state that the 500-task study is forthcoming. The current state undermines trust.

2. **The paper has two simultaneous identities that create reader confusion.** Identity 1: "OrchestraBench, a large-scale benchmark for topology evaluation." Identity 2: "An empirical study showing topology matters on hard tasks." These require different structures. A benchmark paper needs: implementation details, task curation protocol, scoring rubrics, leaderboard design, and reproducibility infrastructure. An empirical study needs: hypothesis, controlled experiment, results, interpretation. The current paper attempts both and delivers the empirical study well but the benchmark incompletely. The strongest version of this paper leans fully into the empirical finding and treats the benchmark as a tool for producing that finding, not as a standalone contribution.

3. **Numerical consistency between sections has improved but is not fully resolved.** The methods section (3.5) reports SWE-bench mean D = 0.72, I = 0.21, T = 0.47. The experiments section (4.1) reports SWE-bench mean D = 0.72, I = 0.21, T = 2.8. T is reported as a normalized value in methods and a raw count in experiments. The paper needs to pick one convention and use it consistently. Given that the alignment distance formula operates on normalized values, all reported T values should be normalized, with raw counts in parentheses for interpretability.

### Overall Assessment

The writing quality is strong and substantially improved from Round 1. The paper reads as human-authored, the results are presented honestly, and the limitations are handled with appropriate rigor. The blocking issue is the scope mismatch between methods (500 tasks, 5 topologies) and results (32 tasks, 3 topologies). A focused rewrite that aligns the framing with the actual experimental scope would resolve this and produce a clean, honest, NeurIPS-quality paper.

---

## Aggregate Score Computation

| Dimension    | R1: Methodology | R2: Novelty | R3: Clarity | Mean |
|--------------|-----------------|-------------|-------------|------|
| Quality      | 6               | 7           | 6           | 6.33 |
| Clarity      | 7               | 7           | 8           | 7.33 |
| Originality  | 7               | 8           | 7           | 7.33 |
| Significance | 6               | 7           | 6           | 6.33 |

**Aggregate score: (6.33 + 7.33 + 7.33 + 6.33) / 4 = 6.83**

### Threshold Assessment

| Metric | Value | Status |
|--------|-------|--------|
| Aggregate score | 6.83 | BELOW 7.0 threshold |
| Distance to threshold | -0.17 | Close but not met |
| Prior round score | 5.6 | Improvement: +1.23 |
| Unanimous recommendation | 3x Weak Accept | Consistent across reviewers |

### What Would Push to 7.0+

The aggregate is 0.17 below threshold. Three changes would close this gap:

1. **Resolve the scope mismatch.** Rewrite the methods section to describe the actual 32-task, 3-topology experiment rather than the aspirational 500-task study. This would raise Quality scores by 0.5-1.0 across all three reviewers because the paper would no longer set expectations it cannot meet.

2. **Add repeated trials (even 3 seeds).** Running each task-topology pair 3 times would yield 288 runs and enable variance estimation, confidence intervals, and basic significance testing. This would raise the Methodology Skeptic's Quality score by at least 1 point.

3. **Report routing accuracy on hard tasks only.** The 90% routing accuracy is inflated by easy tasks where any topology works. Reporting hard-task routing accuracy (likely 75-85%) is more honest and still impressive. This tightens the significance claims.

If items 1 and 2 are addressed, the aggregate would likely reach 7.0-7.5, putting the paper in the "borderline accept" to "accept" range for NeurIPS.

---

*Review generated: 2026-03-15*
*Context: Round 2 post-revision review, evaluating against NeurIPS 2026 criteria*
