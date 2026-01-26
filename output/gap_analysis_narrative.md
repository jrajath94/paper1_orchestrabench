# Research Gap Analysis: Adaptive Multi-Agent Orchestration with Runtime Topology Switching

## Executive Summary

Analysis of 56 papers across 12 clusters in the adaptive multi-agent orchestration literature reveals a consistent blind spot: every existing system that adapts orchestration does so at dispatch time (before execution begins) or through a fixed learned policy. Zero papers switch topologies mid-execution based on execution trace features. Four gaps are identified, with GAP-001 (runtime topology switching via execution trace analysis) scoring highest on the composite ranking of novelty (60%), feasibility (30%), and confidence (10%).

---

## Methodology

### Citation Graph Construction
- **Papers analyzed:** 56
- **Clusters:** 12 (adaptive-orchestration: 7, topology-optimization: 9, dynamic-composition: 4, execution-analysis: 4, model-routing: 5, multi-agent-frameworks: 7, evaluation-benchmarks: 5, reasoning-planning: 6, rl-orchestration: 3, tool-use: 2, surveys: 2, classical-mas: 2)
- **Key observation:** The adaptive-orchestration and execution-analysis clusters share zero cross-cluster citations despite being natural complements.

### Scoring Formula
```
Novelty = co-citation_proximity * 0.30 + direct_paper_absence * 0.30
        + recency * 0.20 + search_validation * 0.20

Ranking = novelty * 0.60 + feasibility * 0.30 + confidence * 0.10
```

---

## Critical Finding: The Static Adaptation Paradox

The literature reveals a paradox. Multiple papers argue for "adaptive" or "dynamic" orchestration, yet every proposed system makes adaptation decisions before or outside of task execution:

| System | Adaptation Type | When Decision Occurs | Mid-Execution Switching |
|--------|----------------|---------------------|------------------------|
| AdaptOrch (Yu, 2026) | Topology selection | Task dispatch | No |
| DyTopo (Lu et al., 2026) | Communication graph | Per reasoning round | Partial (graph, not topology) |
| MASFly (Liu, 2026) | Agent roles | Test time | Roles only, not topology |
| Evolving Orch. (Dang et al., 2025) | Agent sequencing | RL-trained policy | Fixed policy |
| MASS (Zhou, 2025) | Prompt + topology | Offline search | No |
| G-Designer (Zhang et al., 2025) | Communication graph | Task dispatch | No |
| MDAgents (Kim, 2024) | Solo vs. group | Task classification | No |
| DyLAN (Liu, 2024) | Team composition | Task dispatch | No |

The closest to runtime switching is DyTopo, which reconstructs communication graphs per reasoning round. But DyTopo adjusts edge weights within a fixed debate-like topology. It does not switch between structurally different architectures (e.g., from hierarchical to flat).

---

## Gap Rankings

### GAP-001: Runtime Topology Switching via Execution Trace Analysis (Score: 9.5)

**The core insight:** Real tasks change structure mid-execution. A SWE-bench coding task begins with high decomposability (planning phase: hierarchical wins), transitions to high iterativeness (debugging phase: debate wins), and ends with low tool diversity (testing phase: flat wins). Static topology assignment captures only the dominant phase.

**Why it matters:** MAST (Cemri et al., 2025) proves that execution traces contain rich structural signals sufficient to identify 14 failure modes. DIG (Wang et al., 2026) shows that agent interaction dynamics are time-varying and observable. Neither uses these signals for proactive topology switching.

**Concurrent work positioning:** The February 2026 AdaptOrch paper (Yu, 2602.16873) validates the core premise that topology matters more than model choice when LLM capabilities converge. However, it selects topology per-task at dispatch using task metadata. Our proposed AdaptOrch goes further by switching topologies at runtime based on execution trace features, addressing the within-task structural shifts that static assignment misses.

### GAP-002: Closed-Loop Topology-Level Optimization (Score: 8.5)

Topology optimization (MASS, AFlow, ADAS) operates offline. Model routing (RouteLLM, bandit-based) operates at query level. No system creates a closed loop where topology-level performance signals from execution feed back into routing decisions within a single task.

### GAP-003: Evaluation Protocol for Adaptive Orchestration (Score: 8.0)

No benchmark tests adaptive systems that change strategy during execution. No evaluation metric measures switching decision quality separately from task outcome.

### GAP-004: Topology Routing via the Model Routing Paradigm (Score: 8.0)

Model routing is well-established (RouteLLM: ICLR 2025, 145 citations). The identical paradigm has never been applied at the topology level.

---

## Recommended Direction

**GAP-001** is the clear winner. It combines high novelty (9.5), reasonable feasibility (7), and high confidence. The method, AdaptOrch, would:

1. Extract D-I-T features from execution traces in real time (building on MAST trace analysis)
2. Detect phase boundaries where task structure shifts (using change-point detection on feature streams)
3. Switch to the topology best suited for the new phase (using a contextual bandit trained on OrchestraBench alignment data)
4. Transfer execution state across topology boundaries (shared context protocol)

This directly extends Paper 1 (OrchestraBench), which proved topology effectiveness is task-dependent with static assignment. AdaptOrch makes the natural next step: if the right topology depends on task structure, and task structure changes mid-execution, then the topology should change too.
