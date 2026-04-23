# Domain Expert Review

**Paper:** Topology-Task Alignment for Multi-Agent LLM Orchestration
**Venue:** NeurIPS 2026
**Reviewer Role:** Domain Expert (multi-agent LLM systems)
**Date:** 2026-03-16

---

## Overall Recommendation

**Weak Reject -- Interesting direction, insufficient rigor and novelty for a top venue**

This paper asks the right question: does orchestration topology interact with task structure in predictable ways? The controlled comparison design (same backbone, same tools, same budget) is methodologically sound in principle. The result that topology differentiation emerges only on hard tasks is a useful empirical observation. However, the D-I-T framework is taxonomy dressed as theory, the experiments suffer from design choices that inflate apparent predictive power, and the paper contains serious internal inconsistencies that undermine trust in the execution.

---

## Scores (NeurIPS Rubric, 1-10)

| Criterion      | Score | Rationale |
|----------------|-------|-----------|
| **Quality (Q)**    | 4     | Internal contradictions across sections (32 vs. 82 tasks, SWE-bench/WebArena/GAIA vs. custom tasks, 96 vs. 282 runs, 5 vs. 3 topologies). Single run per cell with no variance estimates. Hand-constructed tasks scored by authors create circularity risk. The related work describes a runtime-switching system ("AdaptOrch") that the methods/results never deliver. |
| **Clarity (C)**    | 5     | The introduction and D-I-T formalization are well-written. The "hidden bet" framing is effective. However, the paper reads as if it was revised from a 32-task pilot to an 82-task study without reconciling all sections. The conclusion claims Spearman rho = 0.72 which appears nowhere in the results. The related work positions against a system called "AdaptOrch" that is not the paper being presented. A reader will be confused about what this paper actually is. |
| **Originality (O)** | 4     | The claimed gap (no controlled cross-topology comparison) is partially real but overstated. MultiAgentBench (ACL 2025) evaluates multiple organizational structures. Yu's AdaptOrch (2026) selects among topologies based on task characteristics. The D-I-T dimensions are well-known concepts (subtask independence, revision frequency, tool count) repackaged into a coordinate system with weighted Euclidean distance. The alignment hypothesis -- that matching structural priors to task demands improves performance -- is a tautology once you define the priors to match what works. |
| **Significance (S)** | 4     | The practical finding (topology matters on hard tasks, not easy ones) is useful but not surprising. The selection guide reduces to: use hierarchical for decomposable tasks, debate for iterative tasks, flat when tasks are simple. Any practitioner with deployment experience already knows this. The 90% routing accuracy on 82 hand-crafted tasks with 3 choices does not establish generalization. No downstream system is built on these findings; no existing negative result is overturned with new data. |

**Overall Score: 4.3/10**

---

## Strengths

### 1. The Controlled Comparison Design Is Genuinely Needed

The field does suffer from the problem this paper identifies: each framework evaluates only its own topology on its own tasks. Holding the LLM backbone, tool suite, and token budget constant while varying only the orchestration topology is the right experimental methodology. I have looked through the 42 papers in the literature map and confirmed that no published work achieves this level of control across three or more named topology classes. This design, if executed cleanly, would be a real contribution.

### 2. The Difficulty-Dependent Finding Is the Paper's Best Result

The observation that all topologies perform equivalently on easy tasks (ceiling effect) and diverge sharply on hard tasks (18.6% vs. 52.9% vs. 64.6%) is a genuinely important empirical finding. It explains why single-framework evaluations on curated demos look impressive: they never test the regime where topology actually matters. This finding alone, if replicated with proper statistical controls, would be worth publishing.

### 3. The Failure Analysis Is Informative

The appendix documents that hierarchical fails on high-I tasks because planners fragment cross-cutting concerns (0% accuracy), while debate fails on high-D tasks because merging incompatible solutions is harder than building from a shared plan (33% accuracy). These failure mode descriptions are more informative than the D-I-T framework itself because they provide causal mechanisms, not just correlations.

### 4. Honest Limitations Section

The paper is commendably frank about what 82 single-run tasks cannot establish. The limitations section (5.6) acknowledges the absence of repeated trials, single backbone, hand-constructed tasks, and author-assigned annotations. This honesty is appreciated but does not substitute for actually addressing these limitations.

---

## Weaknesses

### 1. The D-I-T Framework Is Circular, Not Predictive

The topology priors (e.g., hierarchical = (0.8, 0.2, 0.5), debate = (0.3, 0.7, 0.3)) are stated as given. Where do they come from? The paper says they follow from each topology's "structural assumptions," but these assumptions are described informally and the prior coordinates are asserted without derivation. If I define hierarchical's prior as high-D because hierarchical performs well on high-D tasks, and then show that hierarchical performs well on high-D tasks, I have demonstrated nothing. The paper needs to derive topology priors from structural properties of the topology (e.g., communication graph properties, message routing patterns) independently of performance data, then show predictive power on held-out tasks. As written, the priors look reverse-engineered from the results.

The 90% routing accuracy is particularly suspect. With 3 choices and 82 tasks where the authors both designed the tasks to span D-I-T space AND assigned the D-I-T scores AND chose the topology priors, there are too many degrees of freedom for this number to be meaningful. A proper test would use tasks from established benchmarks with annotations from independent raters and topology priors fixed before any experiments run.

### 2. Severe Internal Contradictions Across Sections

The paper has not been reconciled after revision:

- **Introduction** claims 5 topologies, 32 tasks from SWE-bench/WebArena/GAIA, 96 topology-task pairs
- **Methods (Section 3.5)** describes 32 tasks from SWE-bench/WebArena/GAIA with Cohen's kappa from "two trained annotators"
- **Experiments (Section 4)** describes 82 custom tasks (coding/reasoning/research) with annotations by "the authors"
- **Results** report on 82 tasks, 282 runs, 3 topologies
- **Discussion (Section 6.5)** mentions "32 tasks, single run per cell, 96 total evaluations"
- **Conclusion** claims Spearman rho = 0.72 and "61.4% accuracy" which neither appear in the Results section (which reports 90% routing accuracy)

This is not a minor formatting issue. A reader cannot determine what study was actually conducted. Were the benchmarks SWE-bench/WebArena/GAIA or custom-designed? Were there 32 or 82 tasks? Were annotators independent or the authors? Was prediction accuracy 61.4% or 90%? The paper must be internally consistent on its own core claims.

### 3. The Related Work Describes a Different Paper

Section 2 is written for a paper about "AdaptOrch" -- a runtime topology switching system that uses execution trace features to detect phase boundaries and switch topologies mid-execution via a bandit algorithm. Section 2.6 explicitly says: "Our AdaptOrch bridges these two sides. It uses execution trace features to estimate D-I-T characteristics in real time, detects phase boundaries where these characteristics shift, and switches to the topology whose structural prior best matches the new phase."

The actual paper delivers nothing of the sort. There is no runtime switching, no bandit algorithm, no phase boundary detection, no execution trace features. The paper is a static benchmark comparison with a topology selection heuristic. The related work positions against a far more ambitious system that does not exist in this manuscript. This is either (a) a leftover from a different paper draft or (b) an aspirational framing that misrepresents the contribution.

### 4. Single Run Per Cell Invalidates Performance Claims

With one run per task-topology pair, every reported accuracy is a point estimate with unknown variance. LLMs are stochastic; a single run can differ substantially from the expected performance. The claimed debate advantage over hierarchical (64.6% vs. 59.8% overall, a 4.8 pp gap) is well within the range that noise alone could produce. The authors acknowledge this but then proceed to draw conclusions from these numbers as if they were reliable. The high-D vs. high-I crossover (89% vs. 33% for hierarchical; 88% vs. 0% for debate) looks dramatic, but with small subgroup sizes and single runs, these could be artifacts.

### 5. The "Tool Diversity" Dimension Carries No Weight

Throughout the paper, D and I do all the explanatory work. The results section never reports T-conditioned accuracy. The DIT-conditioned accuracy table in the appendix splits only by high-D, high-I, and balanced -- no high-T subset. The topology selection rules in the discussion only reference D and I conditions. T is defined, measured, included in the distance formula, and then ignored in the analysis. This suggests D-I-T is really D-I with a vestigial third dimension included for aesthetic completeness. If T does not predict topology performance, the framework should be D-I, and the honest acknowledgment of this would be more scientifically valuable than carrying a dead dimension.

---

## Questions for Authors

### 1. How were topology priors derived?

The prior coordinates (e.g., flat = (0.2, 0.8, 0.3)) determine the entire alignment prediction. Were these set before or after seeing any experimental results? Can you provide a derivation from topology structure (graph properties, message routing rules, coordination overhead) that does not reference task performance? If the priors were tuned to fit the data, the 90% accuracy is a fitting result, not a prediction result.

### 2. Why does the related work describe a runtime switching system that the paper does not deliver?

Section 2.6 positions the paper as closing a gap between static topology selection and execution trace diagnosis by introducing a bandit-based runtime switching mechanism. The methods and results contain no such mechanism. Is this a different paper? If so, the related work needs to be rewritten to position the actual contribution (static benchmark comparison + selection heuristic) rather than a planned but unimplemented system.

### 3. What is the actual task corpus?

The introduction and methods (Section 3.5) describe tasks from SWE-bench, WebArena, and GAIA. The experiments (Section 4) describe 82 custom tasks in coding/reasoning/research categories. These cannot both be true. Which is the actual study? If custom tasks, how do you address the concern that hand-constructed tasks designed to span D-I-T space will trivially confirm a D-I-T-based predictor?

---

## What Would I Cite This Paper For?

If forced to cite it, I would cite it narrowly for the **empirical finding that topology differentiation is difficulty-dependent** -- that is, topology choice is invisible on easy tasks and consequential on hard ones. This observation, while not deeply surprising, has not been documented with this clarity before. I would not cite the D-I-T framework itself, because (a) it is not predictive in a non-circular way, (b) the three dimensions are standard concepts without a theoretical justification for their sufficiency, and (c) the weighted Euclidean distance formulation is ad hoc.

I would not cite OrchestraBench until the internal inconsistencies are resolved and I know what study was actually conducted.

---

## Is This Genuinely Novel or Incremental?

**Incremental, with a kernel of useful empirical work buried under overclaiming.**

The genuine novelty is modest: holding everything constant except topology and measuring the interaction between topology choice and task difficulty. That is a clean experimental idea. But the paper wraps this in a framework (D-I-T) that adds formal apparatus without formal content. The alignment distance is a weighted nearest-neighbor classifier in a 3D space with author-chosen coordinates for both the tasks and the topologies. The weights are fit on the data. The routing accuracy is evaluated on the training distribution. This is not a contribution to understanding why topologies succeed or fail; it is a lookup table with a geometric interpretation.

Compare to MDAgents (NeurIPS 2024 Oral), which in a narrower domain (medicine) actually built and validated a working adaptive system. Compare to G-Designer (ICML 2025), which learned topology structure from data rather than asserting it from intuition. Compare to MAST (NeurIPS 2025), which identified 14 causal failure modes from trace analysis. Each of those papers delivered a working mechanism. This paper delivers a benchmark comparison with a heuristic overlaid, positioned as if it were a theoretical framework.

---

## Confidence

**4/5** -- I am confident in my assessment. I have published in this area and am familiar with the majority of the papers in the literature map. I verified the gap claim against the cited works. My uncertainty is limited to whether the internal contradictions reflect sloppy editing of a sound underlying study (fixable) or deeper methodological confusion (harder to fix).
