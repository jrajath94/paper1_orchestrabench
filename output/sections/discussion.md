Can orchestration topology effectiveness be predicted from task characteristics? The results from 82 tasks and 794 runs across three seeds say yes. The DIT routing classifier achieves 97.6% accuracy on 42 strongly-typed tasks ($D \geq 0.8$ or $I \geq 0.8$), with the effect replicated across seeds with large effect sizes (Cohen's $d > 2$ for all pairwise comparisons). Routing accuracy on the remaining 40 moderately-typed tasks is not yet committed to data. The practitioner's question shifts from "which topology is best?" to "which topology fits this task?"

### 6.1 Selection Rules

The alignment framework produces continuous predictions, but practitioners need discrete guidance. We distill the findings into a topology selection table (Table \ref{tab:topology_selection_rules}).

[TABLE: tab:topology_selection_rules --- Topology Selection Rules. Columns: Task Profile, Recommended Topology, Observed Accuracy (3-seed mean). Rows: (1) High D ($\geq$0.6) | Hierarchical SOP | 75\%. (2) High I ($\geq$0.6) | Debate | 77\%. (3) Balanced D and I | Debate or Hierarchical | 50--55\%.]

The selection rules reveal two complementary niches: hierarchical excels on high-decomposability tasks (75\%, 3-seed mean) while debate excels on high-iterativeness tasks (77\%). Flat conversation is never recommended for hard tasks; its collapse to 18.6\% confirms that multi-agent coordination justifies its overhead when tasks exceed single-agent capability.

### 6.2 Reinterpreting Prior Negative Results

Smit et al.\ \cite{smit_2024} concluded that multi-agent debate rarely outperforms chain-of-thought baselines \cite{wei_2022}. But debate is a high-iterativeness protocol tested on low-iterativeness tasks (factual recall, mathematical reasoning). From the alignment perspective, the negative result was predictable: debate's structural prior was mismatched to the tasks. Negative results about specific topologies may reflect evaluation design choices rather than fundamental topology limitations. This reinterpretation generalizes: any topology benchmark that does not control for task-structure alignment risks confounding topology quality with topology-task fit.

### 6.3 Extending the Framework

The DIT framework is designed to extend beyond the three topologies evaluated here. Two immediate extensions illustrate the point:

**More topologies.** We characterized but did not evaluate role-playing (prior: 0.5, 0.5, 0.3) and RL-orchestrated (prior: 0.5, 0.5, 0.5) topologies. The geometric formulation generates testable predictions: role-playing should perform comparably to hierarchical and debate on balanced-profile tasks (where both currently score 50--55\%), while RL-orchestrated topologies should adapt to the ambiguous middle region where our routing classifier makes its 8 errors. These are falsifiable hypotheses, not aspirational claims.

**Adaptive switching.** The failure-mode taxonomy (Section 5.7) suggests that topology mismatches produce detectable execution signatures --- context overload for flat, bad decomposition for hierarchical, merge inconsistency for debate. A runtime monitor that detects these signatures from execution traces could trigger mid-task topology switching. MAST \cite{cemri_2025} already distinguishes 14 failure modes from traces; the missing piece is the trace-to-topology feedback loop that our DIT framework now makes principled.

### 6.4 Future Work

The most immediate extensions are: (1) expanding beyond 82 tasks and three topologies to test generalizability across creative generation, long-document analysis, and embodied control domains; (2) building an adaptive orchestration system that estimates DIT coordinates from execution traces and switches topologies mid-task when the structural profile shifts \cite{kim_2024}; (3) training a lightweight classifier on task descriptions to estimate DIT coordinates without manual scoring, removing the annotation bottleneck; and (4) validating across open-source LLM backbones \cite{cemri_2025} to test whether topology-model interactions alter the DIT alignment picture.

### 6.5 Limitations

The sample size (82 tasks, three seeds, 794 runs) provides confidence intervals but may not generalize to all domains. Three topologies do not exhaust the design space. DIT scores were assigned by the authors ($\kappa \geq 0.79$, scored before experiments); third-party replication is needed. The primary evaluation used Claude Opus 4.6 with Sonnet 4.6 on easy tasks only, so topology-model interactions across model families remain untested. Three task categories do not cover creative generation, long-document analysis, or embodied control. Principled topology selection saves tokens --- debate is 40\% cheaper than flat per correct answer on hard tasks --- though precise savings depend on the deployment task mix.
