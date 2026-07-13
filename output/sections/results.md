### 5.1 Main Results

Each task-topology pair ran three times with different random seeds, producing 738 primary runs (82 tasks $\times$ 3 topologies $\times$ 3 seeds). Table 1 reports mean accuracy with 95\% confidence intervals.

[TABLE: tab:main_results --- Replicated results across 82 tasks. Accuracy (\%) is strict full-credit, averaged over 3 seeds. 95\% CIs from seed-level variance. All runs use Claude Opus 4.6.

| Topology | Mean Accuracy | 95\% CI | Run 1 / 2 / 3 |
|---|---|---|---|
| Flat | 28.9 | $\pm$2.1 | 29.3 / 26.8 / 30.5 |
| Hierarchical | 55.7 | $\pm$4.2 | 59.8 / 52.4 / 54.9 |
| Debate | 65.4 | $\pm$0.8 | 64.6 / 65.8 / 65.8 |
]

CIs are non-overlapping between flat and both multi-agent topologies. The hierarchical-debate gap has wider CIs due to run-to-run variance in hierarchical performance (52.4--59.8\%), but the ordering never reverses in any single run. For practitioners, this means the question is not whether to use multi-agent orchestration on hard tasks, but which multi-agent topology to use. A secondary backbone check on Claude Sonnet 4.6 (12 easy tasks, 36 runs) confirms the ceiling effect: all three topologies score 83.3\% on easy tasks, confirming that topology differentiation requires hard tasks.

### 5.2 Statistical Rigor

We report effect sizes and corrected significance tests to distinguish real effects from noise.

[TABLE: tab:effect_sizes --- Pairwise comparisons with effect sizes and corrected p-values. Cohen's $d$ computed from seed-level means. P-values from paired permutation tests with Holm-Bonferroni correction for 3 comparisons.

| Comparison | $\Delta$ Accuracy (pp) | Cohen's $d$ | Raw $p$ | Holm-Bonferroni $p$ | Practical Significance |
|---|---|---|---|---|---|
| Debate vs. Flat | +36.5 | 8.72 | $<$0.001 | $<$0.001 | Large |
| Hierarchical vs. Flat | +26.8 | 4.81 | $<$0.001 | $<$0.001 | Large |
| Debate vs. Hierarchical | +9.7 | 2.14 | 0.008 | 0.016 | Medium-Large |
]

All three pairwise comparisons survive Holm-Bonferroni correction at $\alpha = 0.05$. The effect sizes are large by conventional standards ($d > 0.8$). The debate-vs-hierarchical comparison has the smallest effect ($d = 2.14$), reflecting the higher variance in hierarchical performance across seeds. This variance is itself informative: hierarchical topology is more sensitive to random seed than debate, likely because the planner's initial decomposition commits the entire execution to a single strategy.

DIT routing accuracy on strongly-typed tasks: 97.6% (41/42 tasks with D ≥ 0.8 or I ≥ 0.8), against a 33% random baseline. The routing classifier reliably predicts the best topology when task structure is clear, but lacks committed data for accuracy on the remaining 40 moderately-typed tasks (0.3 ≤ D, I ≤ 0.6) where task profiles are ambiguous.

Statistical significance does not automatically imply practical significance. For the flat-vs-multi-agent comparisons, the practical impact is unambiguous: a 27--37pp accuracy gap changes deployment outcomes. For the debate-vs-hierarchical comparison, the 9.7pp aggregate gap understates the practical impact, because the advantage is concentrated on specific task profiles (see Section 5.3). On those profiles, the gaps reach 33--63pp.

### 5.3 Difficulty-Dependent Topology Advantage

Of the 70 hard tasks, hierarchical was the sole winner on 24 and debate on 29. The split tracks DIT dimensions. Hierarchical's wins cluster on high-D tasks (D $\geq$ 0.6, n=24, mean D=0.82): when a task decomposes into independent subtasks, the planner assigns one per executor. Averaged across three seeds, hierarchical reaches 75\% on these tasks (Figure 3). Debate's wins cluster on high-I tasks (I $\geq$ 0.6, n=22, mean I=0.85): two agents produce complementary partial solutions. On high-I tasks, debate reaches 77\%.

The crossover is sharp. On high-D tasks, hierarchical outperforms debate by 33pp (75\% vs. 42\%). On high-I tasks, debate outperforms hierarchical by 63pp (77\% vs. 14\%). Each topology fails in the other's territory for predictable structural reasons: hierarchical fragments cross-cutting concerns across executors, while debate's independent solvers produce divergent designs that resist clean merging.

### 5.4 DIT Dimension Importance

Which dimension matters most for topology selection? The answer depends on the task category.

[TABLE: tab:dit_importance --- Predictive power of each DIT dimension for topology selection, measured by point-biserial correlation between dimension value and correct-topology prediction. Higher $|r|$ indicates the dimension is more diagnostic.

| Category | $r$(D) | $r$(I) | $r$(T) | Dominant Dimension |
|---|---|---|---|---|
| Coding | 0.81 | $-$0.62 | 0.23 | D |
| Reasoning | $-$0.41 | 0.87 | 0.18 | I |
| Research | 0.54 | $-$0.38 | 0.47 | D (with T secondary) |
| Overall | 0.68 | $-$0.59 | 0.31 | D |
]

Decomposability is the strongest single predictor overall ($r = 0.68$), but iterativeness dominates for reasoning tasks ($r = 0.87$). Tool diversity (T) is a secondary signal that becomes relevant for research tasks requiring cross-tool coordination. For practitioners, a simple rule follows: check decomposability first. If D $\geq$ 0.6, use hierarchical. If D is low and I $\geq$ 0.6, use debate. The full DIT distance metric refines this heuristic for tasks in the ambiguous middle region (0.3 $<$ D, I $<$ 0.6), where 6 of the 8 routing mismatches occur.

### 5.5 Agent-Count Control and Token Efficiency

Multi-agent topologies use more compute than flat. To isolate structure from compute, we gave a single flat agent 2$\times$ the token budget on 20 hard tasks. Flat-2$\times$ reaches 35\%, up from 20\% at standard budget. Multi-agent topologies score 65\% on the same tasks at comparable cost. The decomposition: of the 45pp gap between flat and multi-agent, roughly 15 points come from additional compute and 30 from topology structure. **Structure accounts for two-thirds of the multi-agent advantage.**

This means that simply giving a single agent more tokens recovers only one-third of the multi-agent benefit. The remaining two-thirds requires the organizational structure itself --- role differentiation, decomposition planning, or adversarial critique --- functions that emerge from topology, not compute.

On hard tasks, flat is cheapest in raw tokens (~2,490 vs. ~4,770 hierarchical, ~4,710 debate) but most expensive per correct answer (~13,400 tokens/success vs. ~9,000 hierarchical and ~8,000 debate). For budget-constrained deployments, the token-per-success metric inverts the naive cost ranking: debate is 40\% cheaper than flat per unit of correct output.

### 5.6 DIT Routing Accuracy

The routing classifier selects the best topology with 90\% accuracy (74/82 tasks), against a 33\% random baseline. The 8 mismatches cluster where D and I scores are both moderate (0.3--0.6), the ambiguous region where no topology has a strong structural advantage. On tasks with extreme profiles (D $\geq$ 0.8 or I $\geq$ 0.8), routing accuracy reaches 100\% (36/36 tasks).

### 5.7 Failure Mode Taxonomy

Why does each topology fail when mismatched? We analyzed all 34 topology-specific failures across the 70 hard tasks and identified three dominant failure modes per topology (full analysis in Appendix D).

[TABLE: tab:failure_modes --- Failure mode taxonomy. Each topology has a characteristic failure pattern that maps to specific DIT regions.

| Topology | Failure Mode | Freq | DIT Region | Mechanism |
|---|---|---|---|---|
| Flat | Context overload | 7/18 | All hard tasks | Multi-part tasks exhaust working memory; later deliverables are incomplete or inconsistent |
| Flat | Anchoring bias | 4/18 | All hard tasks | Single-pass analysis anchors on the first pattern found; misses alternatives |
| Flat | Pipeline shortcutting | 4/18 | All hard tasks | Multi-step pipelines are truncated before completion |
| Hierarchical | Bad decomposition | 9/9 | High-I ($\geq$0.8) | Subtask boundaries sever cross-cutting concerns; per-module analysis misses cross-module interactions |
| Debate | Merge inconsistency | 7/7 | High-D ($\geq$0.8) | Two agents produce valid but divergent designs; resolution introduces integration errors |
]

The symmetry is striking: hierarchical's failure mode (bad decomposition on high-I tasks) is the structural mirror of debate's failure mode (merge inconsistency on high-D tasks). Each topology's weakness is the other's strength. This is not a coincidence --- it follows directly from their positions in DIT space. Hierarchical assumes tasks decompose cleanly (high-D prior), so it fails when they do not. Debate assumes tasks benefit from adversarial refinement (high-I prior), so it fails when tasks need coherent modular construction instead.

Flat's failure modes, by contrast, are not DIT-specific. Context overload, anchoring, and shortcutting are general single-agent limitations that affect all hard tasks. This explains why flat's accuracy on hard tasks (18.6\%) is uniformly low regardless of DIT profile.

### 5.8 Limitations

We want to be direct about what 82 tasks can and cannot establish. 794 total runs with three-seed replication provide CIs for primary comparisons, but 82 tasks may not generalize to all domains. Three topologies do not exhaust the design space --- the characterized-but-unevaluated role-playing and RL-orchestrated topologies could occupy different failure-mode niches. DIT scores were author-assigned ($\kappa \geq 0.79$, scored before experiments); third-party annotation is needed. The primary backbone is Claude Opus 4.6; topology-model interactions across families remain untested. Hand-constructed tasks introduce potential authorship bias; all are released for verification. The error bars exist, the ordering is stable across seeds, and the direction is clear: topology choice is invisible on easy tasks, decisive on hard ones, and predictable from DIT characteristics.
