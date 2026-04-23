# Council Review Round 4 — Consensus Report

**Date:** 2026-03-16
**Paper:** Orchestration Topology Benchmarking: Which Multi-Agent LLM Architecture Fits Which Task?
**Venue Target:** NeurIPS 2026

## Consensus Scores

| Dimension | Avg | Weighted | Std | Agreement |
|-----------|:---:|:--------:|:---:|:---------:|
| Quality | 4.0 | 3.90 | 0.9 | Low |
| Clarity | 5.2 | 5.25 | 1.0 | Low |
| Originality | 6.2 | 6.20 | 1.2 | Medium |
| Significance | 4.6 | 4.55 | 0.8 | Medium |

**Aggregate: 4.97 / 10** (threshold: 7.0)
**Agreement: 0.68** (threshold: 0.60) — meets agreement bar
**Verdict: DOES NOT PASS** (2.03 points below threshold)

## Consensus Recommendation

| Reviewer | Recommendation |
|----------|---------------|
| Methodologist | Weak Reject |
| Domain Expert | Weak Reject |
| Practitioner | Borderline |
| Writing Critic | Weak Reject |
| Devil's Advocate | Reject |

**Mode: Weak Reject** (3/5 agree)

## Revision Directives (Ranked by Priority)

### MUST-FIX (All 5 reviewers flagged — blocks acceptance)

**1. Reconcile cross-section contradictions**
The paper describes two different experiments. Introduction, Methods 3.4-3.6, Related Work, and Conclusion reference: 32 tasks, 5 topologies, GPT-4o, SWE-bench/WebArena/GAIA benchmarks, Spearman rho=0.72, 96 runs. Results and Experiments reference: 82 tasks, 3 topologies, Claude Opus 4.6, custom tasks, Spearman rho=-0.417, 282 runs. Every reviewer flagged this. A single consistency pass touching Introduction, Methods, Related Work, and Conclusion would fix it.

**2. Add repeated trials and statistical validity**
Single run per task-topology pair means zero error bars. The paper makes quantitative claims (90% routing accuracy, rho=-0.417 with p<0.0001) without the statistical foundation to support them. Add at least 3 runs per cell (82 tasks x 3 topologies x 3 seeds = 738 runs), report confidence intervals, and run paired significance tests.

**3. Address annotation circularity**
Authors designed D-I-T, designed tasks, assigned D-I-T scores, ran experiments, and scored correctness. This creates a self-fulfilling prophecy risk. Fix: recruit 2 independent annotators for D-I-T scores, report inter-rater reliability. Have a separate evaluator score correctness.

### SHOULD-FIX (3-4 reviewers flagged — significantly improves paper)

**4. Control for agent count confound**
Flat = 1 agent, Hierarchical = 3-4 agents, Debate = 2 agents. The topology variable is confounded with compute budget. The Devil's Advocate and Methodologist both identified this. Fix: add a "flat with 2x token budget" baseline to show topology structure (not just more compute) drives the advantage.

**5. Test secondary backbone on hard tasks**
Sonnet was only tested on easy tasks where ceiling effects make topology invisible. This is uninformative. Run Sonnet on at least 20 hard tasks to see if topology effects generalize across capability levels.

**6. Remove "AdaptOrch" from Related Work**
The Related Work positions against a runtime-adaptive system that the paper never builds or tests. This misleads readers about the paper's scope. Cut it or clearly label as future work.

### CONSIDER (1-2 reviewers flagged — optional improvements)

**7. Add real benchmark tasks alongside hand-crafted ones**
The Practitioner wants tasks sampled from existing benchmarks (SWE-bench, GAIA) to complement hand-crafted tasks. This would address external validity.

**8. Formalize D-I-T annotation protocol**
Provide a rubric with worked examples so independent annotators can replicate the scoring. Currently the annotations are described but not operationalized.

**9. Report task-level results in the appendix**
Per-task breakdown (which specific tasks each topology won/lost) would enable readers to assess whether the D-I-T framework predicts at the individual task level, not just in aggregate.

### STRENGTHS TO PRESERVE (All reviewers praised)

1. **The D-I-T structural-prior framing** — every reviewer called it genuinely novel (O scores: 7, 4, 6, 7, 7). Even the Domain Expert who scored O:4 acknowledged "no prior work characterizes topologies as geometric positions."

2. **The difficulty-dependent finding** — the 73pp flat degradation on hard tasks is striking and well-evidenced. This is the paper's headline result.

3. **Honest limitations section** — all reviewers praised the honesty about sample size, single backbone, no error bars. Don't cut this.

4. **Cost-per-correct analysis** — the Practitioner specifically highlighted Section 5.5 as "the kind of thinking I want to see more of."

5. **The crossover pattern** — Hierarchical 89% on high-D vs Debate 88% on high-I is a clean, memorable result.

## Path to Acceptance

The gap from 4.97 to 7.0 is large (2.03 points). The three Must-Fix items would each contribute roughly:

- Consistency fix: +0.5 Clarity, +0.5 Quality = ~+0.5 aggregate
- Repeated trials: +1.5 Quality, +0.5 Significance = ~+1.0 aggregate
- Independent annotation: +1.0 Quality = ~+0.5 aggregate

Total projected improvement: ~+2.0, bringing the aggregate to ~7.0.

The paper has a strong conceptual core. The D-I-T framework and the difficulty-dependent topology finding are real contributions. But the execution needs significant work before this is NeurIPS-ready.

## Timeline Assessment

With NeurIPS 2026 deadline May 4-6 (~7 weeks):
- Must-Fix 1 (consistency): 1 day
- Must-Fix 2 (repeated trials): 1-2 weeks (need 738 additional runs)
- Must-Fix 3 (independent annotation): 1 week (need to recruit annotators)
- Should-Fix 4-6: 1 week each

This is achievable but tight. Start with Must-Fix 1 (consistency) immediately — it's pure editing.
