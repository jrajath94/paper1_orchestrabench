# Appendix

---

## Appendix A: Task Descriptions

### A.1 Pilot Study Tasks (12 tasks, medium difficulty)

| Task ID | Category | D | I | T | Difficulty | Prompt (abbreviated) |
|---------|----------|-----|-----|-----|------------|----------------------|
| CODE-01 | Coding | 0.80 | 0.20 | 0.30 | Medium | Write a heap-based merge function for sorted lists with O(n log k) complexity. Include type hints and edge-case handling. |
| CODE-02 | Coding | 0.30 | 0.80 | 0.20 | Easy | Debug a longest-palindromic-substring function that misses palindromes including the last character. Fix and verify with four test cases. |
| CODE-03 | Coding | 0.90 | 0.10 | 0.60 | Medium | Implement a key-value store with get/set/delete, TTL-based expiration, and a cleanup method. Use only stdlib. |
| CODE-04 | Coding | 0.50 | 0.60 | 0.40 | Easy | Flatten a nested JSON object into dot-notation keys, handling lists with index notation. Include tests. |
| REASON-01 | Reasoning | 0.20 | 0.90 | 0.10 | Easy | Solve the fox-chicken-grain river crossing. Find the minimum number of crossings and the full sequence. |
| REASON-02 | Reasoning | 0.40 | 0.70 | 0.20 | Medium | Three switches, three bulbs in another room, one visit allowed. Determine which switch controls which bulb. |
| REASON-03 | Reasoning | 0.60 | 0.50 | 0.30 | Hard | Twelve coins, one counterfeit (heavier or lighter). Identify it and its weight direction in exactly three balance-scale weighings. |
| REASON-04 | Reasoning | 0.30 | 0.80 | 0.10 | Hard | Five pirates split 100 gold coins by majority vote with sequential elimination. Determine pirate A's optimal proposal via backward induction. |
| RESEARCH-01 | Research | 0.50 | 0.60 | 0.80 | Medium | Find the top 3 open-source LLM agent frameworks by GitHub stars. Report stars, topology, and one key limitation each. |
| RESEARCH-02 | Research | 0.70 | 0.30 | 0.90 | Medium | Report the SWE-bench Verified SOTA as of March 2026: top 3 systems, scores, and single- vs. multi-agent classification. |
| RESEARCH-03 | Research | 0.40 | 0.70 | 0.70 | Medium | Compare NeurIPS 2025 and ICML 2025 acceptance rates, submission counts, and LLM-agent paper representation. |
| RESEARCH-04 | Research | 0.80 | 0.20 | 0.80 | Hard | Find 3 papers from 2025--2026 that compare multi-agent orchestration strategies. Report titles, venues, topologies compared, and main findings. |

### A.2 Scaled Study Tasks (20 tasks, hard difficulty)

| Task ID | Category | D | I | T | Prompt (abbreviated) |
|---------|----------|-----|-----|-----|----------------------|
| HARD-CODE-01 | Coding | 0.95 | 0.30 | 0.50 | Implement three rate-limiting algorithms (sliding window, token bucket, fixed window) conforming to a shared ABC, plus a benchmark harness measuring acceptance rate, latency percentiles, and Gini fairness. Thread-safe with unit tests. |
| HARD-CODE-02 | Coding | 0.30 | 0.95 | 0.20 | Debug an async producer-consumer pipeline with three race conditions: unsynchronized shared counter, partial reads across stages, and shutdown data loss. Identify all three, explain each, provide fixed code with reproducing tests. |
| HARD-CODE-03 | Coding | 0.85 | 0.50 | 0.30 | Refactor a monolithic payment processor into a Strategy pattern: ABC, four concrete strategies, context class, backward-compatible wrapper, and a fifth Apple Pay strategy demonstrating extensibility. |
| HARD-CODE-04 | Coding | 0.70 | 0.70 | 0.20 | Implement a mini SQL parser handling SELECT, FROM, WHERE (with AND/OR/NOT and correct operator precedence), JOIN, GROUP BY, ORDER BY, and LIMIT. Produce an AST with dataclasses, a pretty-printer, and positional error messages. |
| HARD-CODE-05 | Coding | 0.40 | 0.90 | 0.20 | Find and fix all 5 bugs in an AVL tree implementation: missing height update in rotate\_right, duplicate handling, wrong child in RL rotation, wrong subtree for in-order successor, and mismatched delete subtree. |
| HARD-CODE-06 | Coding | 0.90 | 0.30 | 0.60 | Build a production-grade LRU cache with 7 features: O(1) operations, max\_size eviction, per-key TTL, thread-safety, statistics, decorator factory, and a 100K-operation load test from 10 threads. |
| HARD-REASON-01 | Reasoning | 0.70 | 0.90 | 0.10 | Schedule 8 university courses across 4 time slots and 3 rooms subject to 10 constraints (professor sharing, room requirements, student overlaps, temporal ordering, daily limits). Find a valid schedule or prove impossibility. |
| HARD-REASON-02 | Reasoning | 0.20 | 0.80 | 0.10 | Prove or disprove: any simple graph with n >= 3 vertices and more than n(n-1)/4 edges contains a triangle. If true, show the bound is tight by constructing a triangle-free graph achieving it. |
| HARD-REASON-03 | Reasoning | 0.50 | 0.85 | 0.30 | Given a clinical presentation (fatigue, weight loss, lymphadenopathy, WBC 45K with 80% lymphocytes, smudge cells), perform a differential diagnosis, arrive at the most likely diagnosis, and specify flow cytometry markers and staging workup. |
| HARD-REASON-04 | Reasoning | 0.30 | 0.90 | 0.10 | Analyze a modified second-price auction with a gap penalty. Determine whether truthful bidding remains dominant, derive the Bayesian Nash equilibrium, and compare expected revenue to standard Vickrey. |
| HARD-REASON-05 | Reasoning | 0.80 | 0.60 | 0.30 | Solve a system of four equations in three unknowns (power sums and elementary symmetric polynomials). Find all real solutions with x <= y <= z and verify. |
| HARD-REASON-06 | Reasoning | 0.60 | 0.85 | 0.10 | Analyze a three-player sequential game with incomplete information (B cannot observe A's move). Draw the extensive form, find all pure-strategy NE, find all PBE, and discuss sequential equilibrium refinement. |
| HARD-RESEARCH-01 | Research | 0.85 | 0.50 | 0.90 | Compare 5 attention mechanism variants (MLA, Gated DeltaNet, Differential Attention, Gated Attention, Mamba2 hybrids): innovation, complexity, benchmarks, and whether improvements validated at >70B parameters. |
| HARD-RESEARCH-02 | Research | 0.50 | 0.80 | 0.90 | Find 3+ contradictory claim pairs across recent scaling-law papers. For each: cite both papers, assess evidence strength, and propose reconciliation. |
| HARD-RESEARCH-03 | Research | 0.90 | 0.30 | 0.95 | Build a timeline of LLM agent benchmark results (Jan 2025--Mar 2026) across 6+ benchmarks with 15+ entries. Identify 3 methodology changes that invalidate cross-temporal score comparisons. |
| HARD-RESEARCH-04 | Research | 0.70 | 0.70 | 0.85 | Synthesize findings from technical alignment, ML safety, and AI governance research (2 papers each) to assess whether RLHF is sufficient for frontier model safety. |
| HARD-MULTI-01 | Multi-skill | 0.90 | 0.60 | 0.95 | Perform a 6-step data analysis pipeline on 24 months of revenue data: descriptive statistics, dual model fitting (linear + exponential), anomaly detection, hypothesis generation, statistical test design, and projections with confidence intervals. |
| HARD-MULTI-02 | Multi-skill | 0.95 | 0.20 | 0.70 | Design and implement a task management REST API: OpenAPI 3.0 spec (7 endpoints), Flask implementation, input validation with proper HTTP codes, and 15+ pytest cases. All deliverables must be internally consistent. |
| HARD-MULTI-03 | Multi-skill | 0.85 | 0.50 | 0.90 | Design a chatbot evaluation suite: research eval frameworks (cite 2+), define 5 scoring dimensions, implement scoring functions, create a 10-item test dataset, and build a runner producing a summary report. |
| HARD-MULTI-04 | Multi-skill | 0.60 | 0.85 | 0.50 | Analyze an ambiguous requirement ("build a notification system"): enumerate 4+ interpretations, assess complexity, ask 5 clarifying questions, implement the most likely interpretation with Strategy pattern extensibility, and demonstrate adding a new channel. |

---

## Appendix B: Full Results Table

### B.1 Pilot Study Results

All pilot tasks used medium-difficulty prompts. Ceiling effects dominated: flat achieved 11/12 correct, hierarchical 12/12, and debate 12/12.

| Task ID | Flat | Hier | Debate | Flat Tokens | Hier Tokens | Debate Tokens |
|---------|------|------|--------|-------------|-------------|---------------|
| CODE-01 | correct | correct | correct | 800 | 1,200 | 1,800 |
| CODE-02 | correct | correct | correct | 600 | 1,500 | 2,200 |
| CODE-03 | correct | correct | correct | 2,500 | 1,800 | 2,400 |
| CODE-04 | correct | correct | correct | 2,000 | 1,100 | 1,900 |
| REASON-01 | correct | correct | correct | 400 | 800 | 800 |
| REASON-02 | correct | correct | correct | 350 | 600 | 600 |
| REASON-03 | correct | correct | correct | 1,500 | 1,500 | 1,200 |
| REASON-04 | correct | correct | correct | 1,000 | 800 | 900 |
| RESEARCH-01 | correct | correct | correct | 1,500 | 2,000 | 1,100 |
| RESEARCH-02 | correct | correct | correct | 1,800 | 2,200 | 900 |
| RESEARCH-03 | partial | correct | correct | 4,000 | 2,000 | 1,100 |
| RESEARCH-04 | correct | correct | correct | 4,000 | 2,500 | 1,000 |
| **Totals** | **11/12** | **12/12** | **12/12** | **20,450** | **18,000** | **15,900** |

### B.2 Scaled Study Results

| Task ID | Flat | Hier | Debate | Flat Tokens | Hier Tokens | Debate Tokens |
|---------|------|------|--------|-------------|-------------|---------------|
| HARD-CODE-01 | partial | correct | correct | 2,800 | 5,200 | 5,600 |
| HARD-CODE-02 | partial | partial | correct | 1,800 | 3,800 | 4,200 |
| HARD-CODE-03 | partial | correct | partial | 2,400 | 4,600 | 4,800 |
| HARD-CODE-04 | partial | correct | partial | 2,600 | 5,400 | 5,000 |
| HARD-CODE-05 | partial | partial | correct | 1,600 | 3,600 | 3,800 |
| HARD-CODE-06 | partial | correct | correct | 3,200 | 6,200 | 5,800 |
| HARD-REASON-01 | partial | partial | correct | 2,200 | 4,000 | 4,600 |
| HARD-REASON-02 | correct | partial | correct | 1,800 | 3,200 | 3,400 |
| HARD-REASON-03 | partial | partial | correct | 2,000 | 3,800 | 4,000 |
| HARD-REASON-04 | partial | partial | correct | 2,400 | 3,600 | 4,400 |
| HARD-REASON-05 | correct | correct | correct | 1,400 | 3,000 | 2,800 |
| HARD-REASON-06 | partial | partial | correct | 2,600 | 4,200 | 4,800 |
| HARD-RESEARCH-01 | partial | correct | partial | 3,200 | 6,000 | 5,400 |
| HARD-RESEARCH-02 | partial | partial | correct | 2,800 | 4,400 | 5,200 |
| HARD-RESEARCH-03 | partial | correct | partial | 3,600 | 7,200 | 5,800 |
| HARD-RESEARCH-04 | partial | correct | correct | 3,000 | 5,600 | 5,200 |
| HARD-MULTI-01 | partial | correct | partial | 2,400 | 5,400 | 4,600 |
| HARD-MULTI-02 | partial | correct | partial | 3,000 | 6,400 | 5,200 |
| HARD-MULTI-03 | partial | correct | partial | 2,800 | 5,800 | 5,000 |
| HARD-MULTI-04 | partial | partial | correct | 2,200 | 4,000 | 4,600 |
| **Totals** | **2/20** | **11/20** | **13/20** | **49,800** | **95,400** | **94,200** |
| **Avg tokens** | | | | **2,490** | **4,770** | **4,710** |

---

## Appendix C: D-I-T Alignment Distances

For each task, we compute the Euclidean distance from its D-I-T coordinate to each topology's structural prior. The topology with the minimum distance is the D-I-T prediction for that task's best-fit topology.

**Structural priors:**
- Flat: (D=0.2, I=0.8, T=0.3)
- Hierarchical: (D=0.8, I=0.2, T=0.5)
- Debate: (D=0.3, I=0.7, T=0.3)

### C.1 Pilot Study (ceiling effects prevent meaningful winner analysis)

| Task ID | d(Flat) | d(Hier) | d(Debate) | Predicted | Actual Winner |
|---------|---------|---------|-----------|-----------|---------------|
| CODE-01 | 0.849 | **0.200** | 0.806 | Hier | All correct |
| CODE-02 | **0.141** | 0.837 | 0.173 | Flat | All correct |
| CODE-03 | 1.034 | **0.173** | 0.990 | Hier | All correct |
| CODE-04 | 0.374 | 0.510 | **0.332** | Debate | All correct |
| REASON-01 | **0.224** | 1.005 | 0.283 | Flat | All correct |
| REASON-02 | 0.245 | 0.707 | **0.224** | Debate | All correct |
| REASON-03 | 0.500 | **0.412** | 0.447 | Hier | All correct |
| REASON-04 | **0.224** | 0.878 | 0.245 | Flat | All correct |
| RESEARCH-01 | 0.616 | **0.583** | 0.592 | Hier | All correct |
| RESEARCH-02 | 0.927 | **0.424** | 0.900 | Hier | All correct |
| RESEARCH-03 | 0.458 | 0.671 | **0.447** | Debate | Hier/Debate |
| RESEARCH-04 | 0.985 | **0.300** | 0.949 | Hier | All correct |

Pilot tasks exhibit near-universal ceiling effects, preventing assessment of predictive validity. The one differentiating case (RESEARCH-03, where flat produced a partial result) aligns with the D-I-T prediction: the task's coordinates are closest to debate, and debate was among the correct topologies.

### C.2 Scaled Study

| Task ID | d(Flat) | d(Hier) | d(Debate) | Predicted | Actual Winner | Match? |
|---------|---------|---------|-----------|-----------|---------------|--------|
| HARD-CODE-01 | 0.924 | **0.180** | 0.838 | Hier | Hier, Debate | Yes |
| HARD-CODE-02 | 0.206 | 0.950 | **0.150** | Debate | Debate | Yes |
| HARD-CODE-03 | 0.716 | **0.364** | 0.602 | Hier | Hier | Yes |
| HARD-CODE-04 | 0.520 | 0.592 | **0.374** | Debate | Hier | **No** |
| HARD-CODE-05 | 0.245 | 0.860 | **0.100** | Debate | Debate | Yes |
| HARD-CODE-06 | 0.911 | **0.173** | 0.837 | Hier | Hier, Debate | Yes |
| HARD-REASON-01 | 0.548 | 0.812 | **0.361** | Debate | Debate | Yes |
| HARD-REASON-02 | **0.200** | 0.938 | 0.300 | Flat | Flat, Debate | Yes |
| HARD-REASON-03 | 0.304 | 0.743 | **0.112** | Debate | Debate | Yes |
| HARD-REASON-04 | 0.245 | 0.949 | **0.224** | Debate | Debate | Yes |
| HARD-REASON-05 | 0.632 | **0.447** | 0.500 | Hier | All correct | Yes |
| HARD-REASON-06 | 0.450 | 0.789 | **0.287** | Debate | Debate | Yes |
| HARD-RESEARCH-01 | 0.934 | **0.502** | 0.851 | Hier | Hier | Yes |
| HARD-RESEARCH-02 | 0.671 | 0.781 | **0.616** | Debate | Debate | Yes |
| HARD-RESEARCH-03 | 1.078 | **0.471** | 1.016 | Hier | Hier | Yes |
| HARD-RESEARCH-04 | 0.750 | **0.618** | 0.658 | Hier | Hier, Debate | Yes |
| HARD-MULTI-01 | 0.976 | **0.611** | 0.874 | Hier | Hier | Yes |
| HARD-MULTI-02 | 1.040 | **0.250** | 0.976 | Hier | Hier | Yes |
| HARD-MULTI-03 | 0.934 | **0.502** | 0.851 | Hier | Hier | Yes |
| HARD-MULTI-04 | 0.450 | 0.680 | **0.287** | Debate | Debate | Yes |

**Summary:** The D-I-T minimum-distance heuristic correctly predicts the winning topology on 19 of 20 scaled tasks (95.0%). The single mismatch is HARD-CODE-04 (SQL parser), where D-I-T predicted debate (d=0.374) over hierarchical (d=0.592). This task sits in a balanced region (D=0.7, I=0.7) where the decomposable structure of a parser (tokenizer/AST/parser are separable modules) gave hierarchical an advantage despite the task's non-trivial iteration requirement for operator precedence.

If we route high-D tasks (D >= 0.8) to hierarchical and high-I tasks (I >= 0.8) to debate, the routing achieves 18/18 correct on those tasks (100%). Combined with heuristic routing for the two balanced tasks, overall D-I-T routing accuracy reaches 19/20 (95%), compared to the best single topology at 65% (debate).

---

## Appendix D: Failure Analysis

We analyze every scaled-study task where topologies produced different outcomes. Only HARD-REASON-05 (algebraic system of equations) saw all three topologies succeed; it is excluded from this analysis.

### D.1 Flat Topology Failures (18 partial results out of 20 tasks)

Flat's failures cluster into three modes, documented in the table below.

| Failure Mode | Count | Representative Tasks | Description |
|--------------|-------|---------------------|-------------|
| Context overload | 7 | HARD-CODE-01, CODE-06, MULTI-02 | Multi-part tasks exhaust the agent's working memory. Later deliverables are incomplete or inconsistent with earlier ones. CODE-01: forgot design decisions by the third algorithm; CODE-06: lock vs. RLock confusion after implementing 4 features; MULTI-02: dropped subtask endpoints entirely. |
| Anchoring bias | 4 | HARD-CODE-02, CODE-05, REASON-03, MULTI-04 | Single-pass analysis anchors on the first pattern found and misses alternatives. CODE-02: found 2 of 3 race conditions, anchored on obvious bugs; CODE-05: found 3 of 5 AVL bugs; REASON-03: anchored on CLL without thorough differential; MULTI-04: anchored on first interpretation without exploring the full space. |
| Pipeline shortcutting | 4 | HARD-MULTI-01, RESEARCH-01, RESEARCH-03, MULTI-03 | Multi-step pipelines are truncated. MULTI-01: completed statistics and basic anomaly detection, then shortcut the remaining 4 steps; RESEARCH-03: covered 3 of 6 benchmarks; MULTI-03: implemented 3 of 5 scoring functions. |
| Other | 3 | HARD-CODE-03, REASON-01, REASON-04 | Miscellaneous single-pass limitations. CODE-03: backward-compat wrapper forwarded kwargs incorrectly; REASON-01: greedy constraint assignment without backtracking; REASON-04: incomplete BNE derivation. |

The two tasks where flat succeeded (HARD-REASON-02 and HARD-REASON-05) share a common trait: both have well-known solutions accessible through a single insight (Turan's theorem and Vieta's formulas, respectively). This suggests flat topology remains viable when a task reduces to pattern recognition rather than sustained multi-step construction or iterative refinement.

### D.2 Hierarchical Topology Failures (9 partial results)

All 9 hierarchical failures occurred on high-I tasks (I >= 0.8). The consistent failure pattern is that decomposition boundaries fail to capture cross-cutting concerns.

| Task ID | Decomposition Used | Why It Failed | D-I-T Prediction |
|---------|--------------------|---------------|------------------|
| HARD-CODE-02 | Per-function (fetch, transform, load) | Race conditions are cross-function interactions. Per-function analysis missed the partial-read bug that spans two stages. | Debate (I=0.95) |
| HARD-CODE-05 | Per-method (rotations, insert, delete, helpers) | Bug 5 depends on understanding how bug 4's fix changes delete semantics. The delete subtask accidentally "fixed" it by coincidence. | Debate (I=0.90) |
| HARD-REASON-01 | Constraint propagation phases (identify, propagate, search) | Integration step failed to backtrack when the search subtask's solution violated the daily-limit constraint. CSP requires holistic backtracking. | Debate (I=0.90) |
| HARD-REASON-02 | Proof components (prove bound, show tightness, construct example) | The proof subtask attempted a counting argument assuming regularity instead of citing Turan's theorem. Mathematical proofs resist decomposition. | Flat (I=0.80) |
| HARD-REASON-03 | Diagnostic pipeline (candidate generation, evaluation, workup) | Evaluation subtask ranked CLL highest but failed to articulate exclusion criteria for hairy cell leukemia. Omitted FISH from staging. | Debate (I=0.85) |
| HARD-REASON-04 | Problem components (dominance check, BNE derivation, revenue comparison) | BNE derivation cannot be separated from revenue computation: they share the equilibrium strategy. Subtask 2 produced an approximation. | Debate (I=0.90) |
| HARD-REASON-06 | Game analysis phases (extensive form, find NE, find PBE) | Information sets create interdependencies between belief specification and strategy analysis. The NE subtask treated it as a complete-information game. | Debate (I=0.85) |
| HARD-RESEARCH-02 | By topic (compute-optimal, data quality, scaling wall) | The data-quality subtask found complementary claims rather than genuine contradictions. The precision-data trade-off spans topic boundaries. | Debate (I=0.80) |
| HARD-MULTI-04 | By deliverable (enumerate, implement, extensibility) | Ambiguity analysis requires holding multiple interpretations simultaneously. Decomposition into sequential steps produced only 3 questions (needed 5). | Debate (I=0.85) |

### D.3 Debate Topology Failures (7 partial results)

Debate's failures cluster around a single dominant mode: merge inconsistency. When two agents produce independently valid solutions with divergent design choices, the resolution step introduces integration errors.

| Task ID | Agent A Approach | Agent B Approach | Merge Problem | D-I-T Prediction |
|---------|-----------------|-----------------|---------------|------------------|
| HARD-CODE-03 | Strategy ABC: validate/calculate\_fee/process | Strategy ABC: validate/compute\_total/generate\_receipt | Incompatible ABCs. Resolution picked A's interface but Apple Pay followed B's signatures. | Hier (D=0.85) |
| HARD-CODE-04 | Recursive descent with explicit precedence | Left-to-right evaluation (wrong precedence) | A's precedence was correct, B's JOIN syntax was used. Merged parser had JOIN regression. | Debate (D=0.70) |
| HARD-RESEARCH-01 | Covered 4 of 5 mechanisms | Covered 4 of 5 mechanisms (different 4) | Aggregation succeeded (5/5 covered), but critical assessments from the two agents contradicted each other; resolution was muddled. | Hier (D=0.85) |
| HARD-RESEARCH-03 | 12 entries across 3 benchmarks | 10 entries across 3 benchmarks (different 3) | Merged to 16 entries across 5 benchmarks, but missed one benchmark and one methodology change. Parallel research gave breadth, not depth. | Hier (D=0.90) |
| HARD-MULTI-01 | Linear model, 4 anomalies | Exponential model, 3 anomalies | Correctly identified exponential as better fit, but computed confidence intervals using linear prediction-error formula on the exponential model. | Hier (D=0.90) |
| HARD-MULTI-02 | URL structure: /api/v1/tasks | URL structure: /tasks | Adopted A's spec with B's tests. 12 of 15 tests referenced wrong URL prefix, producing internal inconsistency. | Hier (D=0.95) |
| HARD-MULTI-03 | RAGAS-style metrics (faithfulness, relevancy) | Custom metrics (accuracy, helpfulness, safety) | Merged B's dimensions with A's dataset. Two scoring functions expected different input formats than the runner provided. | Hier (D=0.85) |

The pattern is clear: debate excels when two perspectives on the same problem surface complementary insights (bug finding, adversarial analysis, differential diagnosis). It struggles when the task requires a single coherent design, because merging two independently valid designs is harder than building one.

### D.4 Summary of Failure-Mode / D-I-T Alignment

| Topology | Dominant Failure Mode | D-I-T Region of Failure | Explanation |
|----------|-----------------------|-------------------------|-------------|
| Flat | Context overload, anchoring, shortcutting | Everywhere except single-insight tasks | A single agent cannot sustain coherence across complex multi-part tasks or escape its initial analytical frame. |
| Hierarchical | Bad decomposition of cross-cutting concerns | High-I (I >= 0.8) | Tasks requiring iterative refinement or holistic reasoning resist decomposition. Subtask boundaries sever the dependencies that matter most. |
| Debate | Merge inconsistency from design divergence | High-D (D >= 0.8) | Tasks with clear modular structure benefit from a unified design. Two agents producing independently valid but divergent designs create integration debt. |

---

## Appendix E: Reproducibility

### E.1 Model and Infrastructure

| Parameter | Value |
|-----------|-------|
| Model | Claude Opus 4.6 (claude-opus-4-6) |
| Context window | 1M tokens |
| Temperature | Model default (not manually specified) |
| Interface | Claude Code CLI (Anthropic's official agent interface) |
| Execution environment | macOS (Darwin 25.2.0), local machine |

### E.2 Tools Available to All Topologies

All agents had access to the same tool set, ensuring that performance differences arise from orchestration strategy rather than tool access.

| Tool | Purpose |
|------|---------|
| Read | Read files from local filesystem |
| Write | Create or overwrite files |
| Edit | Exact string replacement in existing files |
| Bash | Execute shell commands |
| Grep | Regex search across files (ripgrep-based) |
| Glob | File pattern matching |
| WebSearch | Web search via multiple providers |
| WebFetch | Fetch and process web page content |

### E.3 Topology Configurations

**Flat (single-agent).** One Claude Opus 4.6 instance receives the task prompt and produces a response using a ReAct-style reasoning loop. No explicit decomposition or revision phase is imposed.

**Hierarchical (planner-executor).** A planner agent receives the task, decomposes it into 2--6 subtasks, and spawns independent executor agents. Each executor solves its subtask in isolation. A final integration pass combines subtask outputs and verifies consistency.

**Debate (multi-agent critique).** Two solver agents (Agent A and Agent B) independently receive the full task prompt and produce complete solutions. A resolution phase compares both solutions, identifies disagreements, and produces a final merged output.

### E.4 Evaluation Protocol

Each task was evaluated as **correct** (all requirements met), **partial** (some requirements met, no major errors in completed portions), or **incorrect** (fundamental errors or missing most requirements). Token counts are estimates based on output length and observed API usage patterns. A single human evaluator (first author) performed all grading against the expected-answer rubrics defined in the task specifications.

### E.5 Artifact Availability

All task prompts, expected answers, topology configurations, and raw results are available in the supplementary materials accompanying this paper. The complete dataset includes:

- `pilot_tasks.json`: 12 pilot task specifications with D-I-T scores and expected answers
- `scaled_tasks.json`: 20 scaled task specifications with D-I-T scores, expected answers, and differentiation hypotheses
- `results/flat_batch1.json`, `results/flat_batch2.json`: Flat topology results for all 12 pilot tasks
- `results/hierarchical_all.json`: Hierarchical topology results for all 12 pilot tasks
- `results/debate_all.json`: Debate topology results for all 12 pilot tasks
- `results/scaled_experiment.json`: Complete scaled-study results for all 20 tasks across all 3 topologies, including per-task summaries, failure-mode annotations, and aggregate analysis

### E.6 Limitations of Reproducibility

Three factors limit exact reproducibility:

1. **Non-deterministic generation.** LLM outputs are stochastic at default temperature. Re-running the same prompts will produce different outputs. Our results represent a single trial per task-topology pair.

2. **Temporal dependence of research tasks.** Research-category tasks query live web data. Results depend on the state of the web as of March 15, 2026. Leaderboards, star counts, and paper availability change over time.

3. **Evaluator subjectivity.** The correct/partial/incorrect rubric involves human judgment, particularly for partial results where completeness is a spectrum. We mitigate this by defining expected answers in advance and applying them consistently, but a different evaluator might draw different boundaries.
