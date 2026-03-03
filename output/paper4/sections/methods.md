# AdaptOrch-RT: Runtime Topology Switching via Task-Structure Estimation

The core idea is straightforward: if the structural characteristics of a task change during execution, the orchestration topology should change too. Implementing this requires answering four questions. How do we estimate D-I-T characteristics from an ongoing execution? How do we detect when those characteristics have shifted enough to warrant a switch? How do we choose which topology to switch to? And how do we transfer state across topologies without losing context?

Figure~\ref{fig:system_architecture} shows AdaptOrch-RT's architecture. A monitor sits alongside whatever topology is currently active, consuming execution traces. The monitor feeds a D-I-T feature extractor that produces rolling estimates of decomposability ($\hat{D}_t$), iterativeness ($\hat{I}_t$), and tool diversity ($\hat{T}_t$). A phase boundary detector watches for significant shifts in these estimates. When a boundary is detected, a contextual bandit selects the next topology. A state transfer protocol serializes the current execution context and initializes the new topology.

## Runtime D-I-T Estimation

The D-I-T framework from our prior work \citep{anonymous_2026} assigns static labels to tasks based on their full descriptions. We need the same characterization, but computed incrementally from partial execution traces.

We define three feature families extracted from a sliding window of the most recent $w$ agent actions (we use $w = 10$ in all experiments):

**Decomposability estimate** $\hat{D}_t$. We track the fraction of recent actions that operate on independent subtasks versus actions that reference outputs from other subtasks. Concretely, if agent action $a_t$ reads from or modifies an artifact that was last written by a different subtask branch, we mark it as a cross-subtask dependency. The decomposability estimate is:

\begin{equation}
\hat{D}_t = 1 - \frac{\text{cross-subtask actions in window}}{\text{total actions in window}}
\end{equation}

When $\hat{D}_t$ is high, the task is currently in a phase where subtasks proceed independently; hierarchical orchestration is favored.

**Iterativeness estimate** $\hat{I}_t$. We count revision actions: any action that modifies an artifact previously marked as complete, re-runs a failed test, or explicitly references a prior attempt. The iterativeness estimate is the fraction of revision actions in the window:

\begin{equation}
\hat{I}_t = \frac{\text{revision actions in window}}{\text{total actions in window}}
\end{equation}

High $\hat{I}_t$ signals that the task is in a refinement loop. Debate topologies handle this well because multiple agents can propose competing fixes simultaneously.

**Tool diversity estimate** $\hat{T}_t$. We count the number of distinct tool categories used in the current window, normalized by the total number of available tool categories:

\begin{equation}
\hat{T}_t = \frac{|\text{unique tool categories in window}|}{|\text{total available tool categories}|}
\end{equation}

High $\hat{T}_t$ with low $\hat{I}_t$ suggests a breadth-first exploration phase where flat conversation (a single agent with access to all tools) often outperforms hierarchical delegation.

These estimates are noisy, especially early in execution when the window contains fewer than $w$ actions. We apply exponential smoothing with decay parameter $\alpha = 0.3$ to reduce oscillation:

\begin{equation}
\bar{D}_t = \alpha \hat{D}_t + (1 - \alpha) \bar{D}_{t-1}
\end{equation}

and analogously for $\bar{I}_t$ and $\bar{T}_t$.

## Phase Boundary Detection

Not every fluctuation in D-I-T estimates should trigger a topology switch. We need to distinguish genuine phase transitions from noise. We use a simple but effective heuristic: a phase boundary is declared at time $t$ if the Euclidean distance between the smoothed D-I-T vector at $t$ and the vector at the time of the last phase boundary exceeds a threshold $\delta$:

\begin{equation}
\| (\bar{D}_t, \bar{I}_t, \bar{T}_t) - (\bar{D}_{\text{last}}, \bar{I}_{\text{last}}, \bar{T}_{\text{last}}) \| > \delta
\end{equation}

We set $\delta = 0.4$ based on a grid search over $\{0.2, 0.3, 0.4, 0.5, 0.6\}$ on a held-out validation set of 10 tasks. Lower thresholds cause too many switches (high overhead, marginal benefit per switch); higher thresholds miss genuine transitions.

We also enforce a minimum cooldown of 5 actions between switches. Without this, the system can oscillate between topologies when D-I-T estimates hover near a boundary.

## Switching Policy

When a phase boundary is detected, the system must choose which topology to activate. We formulate this as a contextual bandit \citep{banditllm_2025} where:

\begin{itemize}
\item The \textbf{context} is the current smoothed D-I-T vector $(\bar{D}_t, \bar{I}_t, \bar{T}_t)$.
\item The \textbf{arms} are three topologies: flat conversation, hierarchical decomposition, and multi-agent debate.
\item The \textbf{reward} is a binary signal: 1 if the subtask completed after the switch, 0 otherwise.
\end{itemize}

We initialize the bandit with priors from the static D-I-T routing results in our prior work. Specifically, we seed the bandit's reward estimates with the topology-task alignment scores from OrchestraBench: hierarchical gets high prior reward in the high-$D$ region, debate in the high-$I$ region, and flat in the high-$T$/low-$I$ region. This warm start means the bandit makes reasonable decisions from the first switch rather than requiring extensive exploration.

During execution, the bandit uses an epsilon-greedy policy with $\epsilon = 0.1$ to balance exploitation of known good mappings with exploration of potentially better alternatives. After each topology segment completes, the reward is computed and the bandit's estimates are updated.

## Switch Cost Model

Switching topologies is not free. When the system transitions from, say, hierarchical to debate, it must: (1) serialize the current execution state, including all intermediate artifacts and the current subtask status; (2) construct a summary prompt that orients the new topology to the task context; and (3) initialize the new topology's agents with this context.

We measured the overhead empirically across our topology implementations. Serialization and deserialization cost approximately 200-400 tokens depending on context size. The re-prompting cost is approximately 500-800 tokens. Total switching overhead averages 800 tokens per switch, which is roughly 8\% of the mean token budget per task.

The switching policy only fires when the expected gain exceeds the cost. We estimate expected gain as the difference between the bandit's predicted reward for the best topology at the new D-I-T point and its predicted reward for the currently active topology. If this difference is below a threshold $\gamma = 0.15$ (calibrated on the validation set), the system stays with the current topology even though a phase boundary was detected.

## Convergence

As the execution trace grows, our D-I-T estimates converge to the true task-structure characteristics of the current phase. Formally, under the assumption that within-phase D-I-T characteristics are stationary, the smoothed estimates $\bar{D}_t$, $\bar{I}_t$, $\bar{T}_t$ converge to the true phase means at rate $O(1/\sqrt{w})$ where $w$ is the window size. Combined with the warm-started bandit, this means AdaptOrch-RT's switching decisions approach oracle quality as more of the task unfolds.

The practical consequence: on tasks with early phase transitions (within the first 10 actions), the system sometimes makes a suboptimal first switch because the D-I-T estimates haven't stabilized. On tasks with later transitions (after 20+ actions), switching quality is high. We revisit this in our analysis of switching precision in Section~\ref{sec:results}.

## Topology Implementations

We implement three canonical topologies, matching our prior OrchestraBench evaluation:

**Flat conversation.** A single LLM agent in a multi-turn loop with access to all tools. The agent plans, executes, and revises in a single conversation thread. This maps to an AutoGen \citep{wu_2023} single-agent configuration.

**Hierarchical decomposition.** A planner agent breaks the task into subtasks and delegates them to specialist agents via structured prompts. Specialists execute independently and report results back to the planner, who synthesizes. This follows the MetaGPT \citep{hong_2023} SOP pattern.

**Multi-agent debate.** Three LLM instances independently propose solutions, then engage in two rounds of critique and revision. A judge agent selects the best final solution. This follows the protocol from Du et al. \citep{du_2023}.

All three share a common state representation (a JSON artifact store keyed by subtask ID) that enables the state transfer protocol to move context between topologies without information loss.
