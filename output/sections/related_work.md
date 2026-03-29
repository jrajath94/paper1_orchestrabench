## Related Work

Multi-agent orchestration research splits into five threads that rarely cite each other. Each contributes a piece of the topology selection puzzle, but none provides an empirically grounded framework for matching topologies to task characteristics.

### 2.1 Static Topology Design

How should agents be wired together? The search-based approach to this question is now mature, with methods spanning graph optimization, tree search, and evolutionary algorithms. MASS \cite{hzhou_2025} jointly optimizes agent prompts and communication topologies. The search-based approach extends further: AFlow \cite{zhang_2025_aflow} treats workflows as code-represented nodes and uses MCTS to optimize them, while ADAS \cite{hu_2025} goes a level up, having a meta-agent iteratively program and improve new agent designs. G-Designer \cite{zhang_2025_gdesigner} generates task-aware communication graphs via graph auto-encoders, and EvoFlow \cite{zhang_2025_evoflow} evolves diverse workflows via niching algorithms. All share a constraint: the topology is fixed once selected. These methods find good topologies but cannot adapt when a task's structure shifts mid-execution.

### 2.2 Dynamic Composition Without Topology Switching

A separate line of work asks: who should be on the team? DyLAN \cite{liu_2024_dylan} selects agent teams via importance scoring, AgentVerse \cite{chen_2024_agentverse} simulates group dynamics through recruitment stages, and AutoAgents \cite{chen_2024_autoagents} generates specialized agents per task. Changing the team roster, however, is fundamentally different from changing how agents interact. These systems adjust who participates, but the coordination architecture remains fixed.

### 2.3 Trace Analysis and Model Routing

Execution traces contain the information needed to assess whether the current strategy is working. MAST \cite{cemri_2025} proves this with enough granularity to distinguish 14 failure categories across 7 frameworks, but uses the signal only for retrospective diagnosis, not for online adaptation. On the routing side, RouteLLM \cite{routellm_2025} and the bandit-based routing line \cite{bandit_route_2025, neural_bandit_2025} show that learned selection between LLM alternatives reduces cost while maintaining quality. The routing paradigm is well-established at the model level. It has never been applied at the topology level. Our work provides the empirical foundation for such routing.

### 2.4 Concurrent and Closely Related Work

Three concurrent papers validate the premise that topology choice dominates performance, though each leaves a different gap. Yu \cite{yu_2026} presents AdaptOrch, which selects among four topologies based on task metadata, but selects once per task without a controlled evaluation isolating topology from other variables. MDAgents \cite{kim_2024} adaptively assigns collaboration structure in medicine (NeurIPS 2024 Oral), supporting only binary choice (solo vs. group) in a single domain. MASFly \cite{masfly_2026} and DyTopo \cite{lu_2026} adjust roles or communication edges within fixed topology classes rather than comparing structurally different architectures.

No prior work evaluates multiple topologies head-to-head on the same tasks under identical conditions. OrchestraBench fills this gap: we formalize topology priors as positions in D-I-T space, evaluate three topologies on 82 tasks under controlled conditions, and show that task-structure alignment predicts which topology wins.
