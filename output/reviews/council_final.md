# Council Final Review -- 5-Persona Validation

**Date:** 2026-03-16
**Paper:** Orchestration Topology Benchmarking: Which Multi-Agent LLM Architecture Fits Which Task?
**Venue Target:** NeurIPS 2026
**Round:** Final validation (post-revision from Round 4)
**Prior Round Aggregate:** 4.97/10 (Weak Reject)

---

## Changes Since Round 4

The following Must-Fix and Should-Fix items from Round 4 have been addressed:

1. **Cross-section contradictions (Must-Fix 1):** FIXED. All sections now consistently reference 82 tasks, 3 topologies, Claude Opus 4.6, custom tasks, 794 runs. The dual-experiment confusion from R4 is resolved.
2. **Repeated trials (Must-Fix 2):** FIXED. Three-seed replication added (738 primary + 36 Sonnet + 20 flat-2x = 794 total). Confidence intervals reported for all primary comparisons.
3. **Agent-count control (Should-Fix 4):** FIXED. Flat-2x-budget experiment on 20 tasks decomposes advantage into ~1/3 compute + ~2/3 structure.
4. **Fabricated citation (wang_2026 / DIG):** FIXED. Removed from all sections.
5. **AI writing patterns:** FIXED. No hedge chains, boilerplate, or LLM-tell phrases detected.

**Remaining issues carried forward from R4:**
- Annotation circularity (Must-Fix 3): Partially addressed -- paper now acknowledges limitation explicitly, but no independent annotators recruited.
- Secondary backbone on hard tasks (Should-Fix 5): Not addressed -- Sonnet still only tested on easy tasks.

**New issues found in this review:**
- DIT mean values still inconsistent between Methods Section 3.5 and Experiments Section 4.1.
- Token efficiency calculation has minor arithmetic inconsistencies in Section 5.6.

---

## Reviewer 1: Methodology Skeptic

**Confidence:** 4/5 (deep familiarity with experimental methodology in ML)

### Scores

| Criterion | Score | Weight |
|-----------|:-----:|:------:|
| Quality | 6 | 40% |
| Clarity | 6 | 15% |
| Originality | 7 | 15% |
| Significance | 6 | 30% |
| **Weighted** | **6.2** | |

**Overall:** Borderline Accept (6)

### Strengths

**S1. Three-seed replication with confidence intervals is a genuine improvement.** The paper now reports 738 primary runs with per-seed breakdowns (Table 1: Flat 29.3/26.8/30.5, Hier 59.8/52.4/54.9, Debate 64.6/65.8/65.8). I independently verified these averages and CIs against the experiment data files -- they are correct. The flat-vs-multi-agent gap is large and never reverses across seeds.

**S2. The flat-2x-budget control is well-designed.** Giving a single agent 2x tokens on 20 stratified tasks isolates compute from structure. The result (35% vs 65% for multi-agent at comparable token cost) with a clean decomposition (15pp compute + 30pp structure) is a rigorous contribution. The per-DIT-profile breakdown (zero new solves on high-D, one on high-I, two on balanced) adds mechanistic insight.

**S3. Run count arithmetic is internally consistent.** 82 tasks x 3 topologies x 3 seeds = 738 primary runs, plus 12 x 3 x 1 = 36 Sonnet runs, plus 20 flat-2x = 794 total. This matches across Introduction, Methods, Experiments, Results, and Conclusion.

**S4. Inter-annotator agreement reported.** Cohen's kappa 0.83/0.79/0.91 for D/I/T respectively, with disagreement resolution protocol described.

### Weaknesses

**W1. DIT mean values are STILL inconsistent between Methods and Experiments.**
- Methods 3.5: Coding D=0.63, I=0.27, T=2.3; Reasoning D=0.24, I=0.59, T=1.4
- Experiments 4.1 prose: Coding D=0.72, I=0.21, T=2.8; Reasoning D=0.31, I=0.64, T=1.6
- Experiments 4.1 table (tab:benchmark_statistics): Coding D=0.63, I=0.27, T=2.3

The table in Section 4.1 matches Methods 3.5, but the prose in the same Section 4.1 contradicts both its own table and Section 3.5. This is a consistency error within the same section. It appears the prose was updated with different values (perhaps from a different computation) while the table retained the original. **Severity: moderate.** The directional claims (coding = high D, reasoning = high I) are robust to either set of numbers, but this undermines credibility.

**W2. Token efficiency arithmetic is slightly off.**
- Section 5.6: "flat spends 8,616 tokens per success, hierarchical 8,324, and debate 7,336"
- Using the paper's own hard-task token costs (2490/4770/4710) and overall accuracies (28.9/55.7/65.4):
  - Flat: 2490/0.289 = 8,616 (correct)
  - Hier: 4770/0.557 = 8,564 (paper says 8,324 -- off by 240)
  - Debate: 4710/0.654 = 7,202 (paper says 7,336 -- off by 134)
- The ranking (debate most efficient) is preserved, but the exact numbers do not reproduce from the paper's own inputs. Likely a rounding issue or the per-correct was computed from different underlying data.

**W3. Annotation circularity remains a methodological concern.** The authors designed the DIT framework, designed the tasks to span DIT space, assigned DIT scores, and evaluated correctness. The paper now acknowledges this in Section 6.3 ("DIT scores were assigned by the authors; independent annotation with inter-rater reliability is a priority for future work") and claims scores were assigned before running experiments. This is honest but does not eliminate the concern. The high inter-annotator agreement (kappa >= 0.79) between the authors themselves is less reassuring than agreement between independent annotators would be, since co-authors share mental models.

**W4. Hierarchical CI is wide.** The hierarchical topology shows +/-4.2% CI (runs: 59.8/52.4/54.9), meaning its true mean could be as low as 51.5% or as high as 59.9%. The debate mean of 65.4 +/- 0.8% does not overlap with the hierarchical upper bound, so the ordering is statistically meaningful. But the 7.4pp spread across three seeds for hierarchical suggests sensitivity to initial conditions that the paper does not fully explain.

**W5. Three seeds is the minimum for CIs, not a strong statistical foundation.** With n=3, the CI estimates are imprecise (wide CIs on the CIs themselves). This is adequate for a first paper establishing the phenomenon but should be acknowledged more explicitly. The paper says "the error bars now exist" -- true, but barely.

**W6. Sonnet backbone only on easy tasks.** Section 5.5 reports Sonnet at 83.3% for all topologies on 12 easy tasks. This confirms the ceiling effect but provides zero evidence about whether topology effects generalize across model capabilities on hard tasks. The Round 4 council flagged this as Should-Fix 5; it remains unaddressed.

### Questions for Authors

1. Which DIT values are correct -- Methods 3.5 / Table 4.1, or the prose in Section 4.1? Can you provide the raw computation?
2. What explains the hierarchical topology's high run-to-run variance (52.4-59.8%) compared to debate's stability (64.6-65.8%)?
3. Have you considered running even one hard-task subset on a non-Anthropic backbone (e.g., GPT-4o, Gemini)?

---

## Reviewer 2: Novelty Assessor

**Confidence:** 3/5 (familiar with multi-agent systems literature, not a deep specialist)

### Scores

| Criterion | Score | Weight |
|-----------|:-----:|:------:|
| Quality | 6 | 15% |
| Clarity | 7 | 15% |
| Originality | 7 | 40% |
| Significance | 6 | 30% |
| **Weighted** | **6.55** | |

**Overall:** Accept (7)

### Strengths

**S1. The DIT framework is a genuine conceptual contribution.** No prior work characterizes topology selection as a geometric alignment problem in a task-structure space. The three dimensions (decomposability, iterativeness, tool diversity) are intuitive, operationally defined, and predictive (90% routing accuracy). This is not a straightforward combination of existing techniques -- it is a new way to think about the problem.

**S2. The alignment hypothesis is falsifiable and tested.** Section 3.3 states two predictions (no single topology dominates; extreme DIT profiles show largest gaps) and the results confirm both. The crossover pattern (hierarchical 89% on high-D vs debate 88% on high-I, with debate at 0% on high-I tasks for hierarchical) is a clean, memorable result that provides genuine insight.

**S3. Related work is comprehensive and well-structured.** Five threads (static topology selection, dynamic composition, trace analysis, model routing, concurrent work) with clear positioning after each. The paper correctly identifies MDAgents as the closest precedent and articulates how this work differs (controlled comparison, multiple domains, continuous DIT vs binary complexity). No false "first to..." claims detected.

**S4. The reinterpretation of Smit et al. is insightful.** Section 6.2 argues that prior negative results about debate reflect evaluation design (low-I tasks) rather than fundamental topology limitations. This reframing is well-supported by the DIT framework and adds value beyond the empirical results.

**S5. Concurrent work section is honest.** The paper discusses Yu (AdaptOrch), MASFly, and DyTopo without overclaiming differentiation. It acknowledges that AdaptOrch "validates our central premise" while identifying the controlled-evaluation gap.

### Weaknesses

**W1. Three topologies is a limited design space.** The paper acknowledges five topology classes but only evaluates three (flat, hierarchical, debate). Role-playing and RL-orchestrated are "characterized but not yet evaluated." With only three points in topology space, the geometric alignment framework is essentially fitting a line through three points -- any reasonable metric would show correlation. The framework's value would be much more convincing with five or more evaluated topologies. This is acknowledged in limitations but it constrains the significance claim.

**W2. 90% routing accuracy against a 33% random baseline is a low bar.** With three topologies, random selection gets 33%. A simple heuristic ("use debate for reasoning, hierarchical for coding") would likely achieve similar accuracy without the DIT framework. The paper does not report what a naive category-based heuristic would score, making it hard to assess the DIT framework's added value over simpler approaches.

**W3. The "first controlled cross-topology comparison" claim needs qualification.** While OrchestraBench is controlled in important ways (same LLM, same tools, same budget), the topologies are implemented by the same authors who designed the framework. Implementation quality differences could confound results. The paper mentions wrappers are 200-600 lines of Python -- the 3x size difference suggests non-trivial variation in implementation sophistication.

**W4. Contribution framing could be sharper.** The paper straddles benchmark paper and systems paper. The main contribution is the DIT framework + controlled comparison, not a new system. But the writing sometimes veers toward system-building language ("OrchestraBench implements...") that creates expectation for a reusable artifact. The code release promise helps, but the contribution would read more cleanly as "an empirical study establishing topology-task alignment" rather than "a benchmarking framework."

### Questions for Authors

1. What accuracy does a naive category-to-topology mapping achieve (e.g., "if coding, use hierarchical; if reasoning, use debate")?
2. Could you add a brief analysis of the 10% DIT routing errors -- are they systematic or random?

---

## Reviewer 3: Clarity Reviewer

**Confidence:** 4/5 (experienced in evaluating technical writing quality)

### Scores

| Criterion | Score | Weight |
|-----------|:-----:|:------:|
| Quality | 6 | 15% |
| Clarity | 7 | 40% |
| Originality | 7 | 15% |
| Significance | 6 | 30% |
| **Weighted** | **6.55** | |

**Overall:** Accept (7)

### Strengths

**S1. The introduction is exceptionally well-written.** The opening paragraph ("Every multi-agent orchestration topology carries a hidden bet...") immediately establishes the problem in concrete terms. The progression from problem statement to the alignment hypothesis to OrchestraBench is logical and efficient. No wasted paragraphs.

**S2. The writing is direct and free of AI patterns.** I searched for common LLM-tell phrases (delve, landscape, tapestry, leveraging, furthermore, notably, it is worth noting) and found none. Sentences are declarative and specific. Claims are accompanied by numbers. The voice is consistent throughout.

**S3. The three contributions are crisply stated.** Each contribution in the introduction maps to a specific section and is falsifiable. Contribution 2 states exact numbers (82 tasks, 794 runs). Contribution 3 states a specific accuracy claim (90% vs 33% baseline). This is good scientific writing.

**S4. Limitations are honest and well-placed.** Section 5.7 leads with "We want to be direct about what 82 tasks can and cannot establish." This sets an appropriate tone. The limitations are specific (not "sample size may be small" but "three seeds per cell means CIs are imprecise") and the paper does not try to explain them away.

**S5. The discussion reinterpretation of Smit et al. is a highlight.** Section 6.2 takes a published negative result and shows how the DIT framework reinterprets it. This demonstrates the framework's explanatory power beyond the paper's own experiments.

### Weaknesses

**W1. DIT mean values contradict between Methods prose and Experiments prose/table.** This is the most significant clarity issue in the paper. Section 3.5 gives coding D=0.63, and in Section 4.1 the table repeats D=0.63 but the paragraph text says D=0.72. A reader encountering both will be confused about which values are authoritative. This was supposed to have been fixed in the cross-section consistency pass after Round 4. (See Methodology Skeptic W1 for details.)

**W2. Section 4 (Experiments) partially duplicates Section 3.** Section 3.5 describes task sampling and annotation. Section 3.6 describes the evaluation protocol. Section 4.1 then re-describes task sampling and annotation, and Section 4.3 re-describes the evaluation design. While the overlap is not verbatim, a reader going sequentially encounters the same information twice. The Methods section should describe the framework design; the Experiments section should describe how it was applied. Currently both sections describe both.

**W3. The topology selection table (Section 6.1) uses only two rows of guidance.** For practitioners -- the paper's stated audience for Contribution 3 -- the table reduces to: "high D -> hierarchical, high I -> debate, balanced -> either." This is useful but could be more nuanced. What about high-T tasks? The T dimension is part of the framework but barely appears in the selection rules.

**W4. Figure placeholders need resolution.** The paper contains [FIGURE: ...] and [TABLE: ...] markers rather than actual figures and tables. For a final review, I evaluate the described content: the DIT scatter plot, architecture diagrams, and topology selection table are well-conceived. But submission requires rendered figures. Axis labels, font sizes, and color choices cannot be evaluated from text descriptions.

**W5. The paper refers to "82 custom tasks (12 easy, 70 hard)" but Extended tasks include "23 medium, 27 hard" per the JSON metadata.** If there is a medium difficulty tier, it is never mentioned in the paper text. This is either a metadata inconsistency or the paper collapsed medium and hard into a single "hard" category without stating so.

### Questions for Authors

1. Which DIT mean values are canonical?
2. Can Section 4 be trimmed to avoid duplicating Section 3?
3. Is there a medium difficulty tier or not?

---

## Reviewer 4: Domain Expert

**Confidence:** 5/5 (leading researcher in multi-agent LLM systems)

### Scores

| Criterion | Score | Weight |
|-----------|:-----:|:------:|
| Quality | 6 | 25% |
| Clarity | 7 | 15% |
| Originality | 7 | 25% |
| Significance | 7 | 35% |
| **Weighted** | **6.75** | |

**Overall:** Accept (7)

### Strengths

**S1. This paper addresses a real gap in the field.** As someone who works with multi-agent systems daily, the lack of controlled cross-topology comparisons is a genuine problem. Every framework paper evaluates its own design on its own tasks. OrchestraBench is the first work I have seen that holds LLM backbone, tools, and budget constant while varying only the topology. This is a necessary contribution.

**S2. The difficulty-dependent finding is the paper's strongest result.** The fact that topology choice is invisible on easy tasks but decisive on hard ones (flat drops from ~92% to ~18.6%) is both intuitive in hindsight and empirically novel. No prior work has demonstrated this with controlled experiments. The 73pp degradation for flat on hard tasks is a headline number the community will cite.

**S3. The crossover pattern is clean and actionable.** Hierarchical 89% on high-D vs debate 88% on high-I, with each topology scoring 0-33% in the other's territory, is exactly the kind of result practitioners need. Combined with the DIT routing classifier's 90% accuracy, this gives a principled basis for topology selection that currently does not exist.

**S4. The flat-2x control resolves a key confound.** The prior Round 4 review correctly identified agent-count confounding. The flat-2x experiment (20 tasks, comparable token budget) cleanly decomposes the advantage: structure contributes ~2/3, compute ~1/3. The per-DIT-profile analysis (zero new solves on high-D from extra compute) is particularly illuminating -- it shows that the structural advantage is not merely about "more thinking time."

**S5. The positioning against MDAgents, Smit et al., and concurrent work is accurate.** MDAgents (NeurIPS 2024 Oral) is correctly identified as the closest precedent, with clear differentiation on scope (one domain vs three), topology granularity (binary vs three), and evaluation methodology (uncontrolled vs controlled). The Smit et al. reinterpretation adds theoretical depth.

### Weaknesses

**W1. Only Anthropic models tested.** Claude Opus 4.6 primary, Claude Sonnet 4.6 secondary (easy tasks only). The field needs to know whether topology effects hold for GPT-5, Gemini, and open-weight models. This is acknowledged in limitations but remains a significant scope restriction for a benchmarking paper aimed at the community.

**W2. The three evaluated topologies do not include some of the most practically important ones.** Role-playing (used by CAMEL, ChatDev), ReAct-based pipelines, and mixture-of-experts patterns are widely deployed but not evaluated. The paper positions role-playing and RL-orchestrated topologies in DIT space (Section 3.2) but does not test them. This limits the framework's practical applicability.

**W3. Debate topology implementation details matter.** The paper describes debate as "adversarial reviewers who propose, critique, and refine solutions through multiple rounds." But debate performance is highly sensitive to the number of rounds, whether there is a judge, and how convergence is defined. The implementation section says wrappers are 200-600 lines but does not specify these critical parameters. For reproducibility, we need to know: how many debate rounds? What is the convergence criterion? Is the judge the same LLM?

**W4. The 82 tasks are hand-crafted, not sampled from established benchmarks.** This gives the authors control over DIT coverage but introduces potential bias. Tasks designed to "span DIT space" may inadvertently favor the alignment hypothesis. Testing on SWE-bench, GAIA, or WebArena tasks (with post-hoc DIT annotation) would provide stronger external validity.

**W5. The paper does not examine failure modes at the trace level.** MAST (cited in related work) shows that execution traces contain rich signal about coordination failures. The paper records full traces but only reports aggregate accuracy. A qualitative analysis of representative failure traces (e.g., why hierarchical fails on high-I tasks) would strengthen the mechanistic claims.

### Questions for Authors

1. How many debate rounds per task? What convergence criterion?
2. Have you computed DIT scores for any SWE-bench or GAIA tasks to check external validity?
3. What does a hierarchical failure look like on a high-I task? Can you provide a representative trace excerpt?

---

## Reviewer 5: Ethics and Reproducibility

**Confidence:** 4/5 (familiar with reproducibility standards and research ethics)

### Scores

| Criterion | Score | Weight |
|-----------|:-----:|:------:|
| Quality | 6 | 20% |
| Clarity | 7 | 20% |
| Originality | 6 | 20% |
| Significance | 6 | 20% |
| Reproducibility | 6 | 20% |
| **Weighted** | **6.2** | |

**Overall:** Borderline Accept (6)

### Strengths

**S1. Data release commitment.** The paper states "Code and annotation data will be released under an open-source license upon publication." All 82 tasks with DIT annotations, topology implementations, and evaluation harness would enable independent replication.

**S2. Experimental controls are well-described.** Same LLM, same tools, same token budget, same temperature. The controlled-variable design is clearly articulated. Run count arithmetic is verifiable (82 x 3 x 3 = 738 + 36 + 20 = 794).

**S3. Confidence intervals from three seeds.** While three seeds is minimal, it is a substantial improvement over the single-run design in earlier rounds. All primary comparisons report CIs, and the paper explicitly states when CIs overlap vs do not.

**S4. Broader impact statement exists.** Section 6.6 discusses resource implications and warns against treating the three studied topologies as exhaustive. The call to "treat DIT as extensible" is appropriate.

**S5. No harmful applications identified.** The work is a benchmarking methodology -- it helps practitioners make better topology choices. There are no dual-use concerns.

### Weaknesses

**W1. Annotation circularity is the primary reproducibility concern.** Authors designed DIT, assigned scores, and evaluated results. Even with kappa >= 0.79 between co-authors, this is agreement between people who share a theoretical framework. Section 6.3 acknowledges this and promises third-party annotation as future work. For a NeurIPS paper, this is honest but the lack of external validation weakens the reproducibility claim. An independent annotator following the Section 3.1 definitions might assign systematically different DIT scores.

**W2. Single vendor backbone.** Reproducibility requires that others can run the experiments. Claude Opus 4.6 is a proprietary API model. If Anthropic deprecates or changes the model, exact replication becomes impossible. The paper should note model version identifiers and consider whether results might vary with API updates.

**W3. The difficulty tier inconsistency needs resolution.** The experiment JSON files label tasks as "easy," "hard," and "medium" (extended_tasks.json: "23 medium, 27 hard"). The paper text only references "easy" and "hard." Either the medium tier exists (and should be documented) or the JSON metadata is incorrect. For reproducibility, the task difficulty labels must be unambiguous.

**W4. No pre-registration or analysis plan.** The DIT framework, task design, and analysis approach were not pre-registered. Combined with W1 (annotation circularity), this means the hypothesis, data collection, and analysis were all conducted by the same team without external commitments. This is standard in ML but worth noting given the framework's claim to predictive validity.

**W5. Cost reporting is incomplete.** The paper reports token counts but not API costs. At current Opus pricing, 794 runs consuming the reported token volumes would cost a specific dollar amount that should be disclosed to help others budget for replication.

### Questions for Authors

1. What is the total API cost of the 794 runs?
2. Can you provide model version identifiers (e.g., exact API model string) for both Opus and Sonnet?
3. Would you be willing to share the raw execution traces (not just aggregate results) to enable trace-level analysis by others?

---

## Aggregate Assessment

### Score Summary

| Criterion | Methodology | Novelty | Clarity | Domain | Ethics | Average |
|-----------|:----------:|:-------:|:-------:|:------:|:------:|:-------:|
| Quality | 6 | 6 | 6 | 6 | 6 | **6.0** |
| Clarity | 6 | 7 | 7 | 7 | 7 | **6.8** |
| Originality | 7 | 7 | 7 | 7 | 6 | **6.8** |
| Significance | 6 | 6 | 6 | 7 | 6 | **6.2** |
| **Overall** | **6** | **7** | **7** | **7** | **6** | **6.6** |

### Recommendations

| Reviewer | Recommendation | Confidence |
|----------|:-------------:|:----------:|
| Methodology Skeptic | Borderline Accept (6) | 4/5 |
| Novelty Assessor | Accept (7) | 3/5 |
| Clarity Reviewer | Accept (7) | 4/5 |
| Domain Expert | Accept (7) | 5/5 |
| Ethics & Reproducibility | Borderline Accept (6) | 4/5 |

### Consensus: **BORDERLINE ACCEPT**

- Three reviewers score Accept (7), two score Borderline Accept (6).
- No reviewer scores below 6. No fatal flaws identified.
- All criteria meet the >= 6.0 threshold.
- Quality is at exactly 6.0 -- the minimum threshold.

### Inter-Reviewer Agreement

Score spread is tight (max disagreement = 1 point on any criterion). All five reviewers agree on the paper's core strengths (DIT framework novelty, difficulty-dependent finding, controlled design) and core weaknesses (DIT value inconsistency, annotation circularity, limited topology/model coverage). This is **high agreement**.

### Critical Issues Remaining (Would Block Accept at Strict Venues)

1. **DIT mean value contradictions (W1 across multiple reviewers).** Methods 3.5 and Experiments 4.1 prose give different DIT means for all three categories. This is a fixable consistency error but must be fixed before submission.
2. **Token efficiency arithmetic (Methodology Skeptic W2).** Hierarchical and debate cost-per-correct do not reproduce from the paper's own numbers. Minor but sloppy.
3. **Difficulty tier metadata mismatch.** "Medium" tier exists in data but not in paper text.

### Issues Acknowledged but Not Blocking

1. Annotation circularity -- honestly disclosed, with mitigation (scores assigned before experiments, kappa reported).
2. Single vendor backbone -- standard limitation for API-based research.
3. Three topologies -- acknowledged as initial study, future work clearly scoped.
4. Three seeds -- minimal but adequate for establishing the phenomenon.

### Improvement from Round 4

| Criterion | R4 Avg | Final Avg | Delta |
|-----------|:------:|:---------:|:-----:|
| Quality | 4.0 | 6.0 | +2.0 |
| Clarity | 5.2 | 6.8 | +1.6 |
| Originality | 6.2 | 6.8 | +0.6 |
| Significance | 4.6 | 6.2 | +1.6 |
| **Aggregate** | **4.97** | **6.6** | **+1.63** |

The paper improved substantially (+1.63 aggregate points). The three-seed replication and flat-2x control addressed the two largest methodological gaps. Cross-section consistency fixes eliminated the dual-experiment confusion. The remaining issues (DIT value inconsistency, annotation circularity, limited model coverage) are either fixable in hours (DIT values) or honestly acknowledged limitations.

### Verdict

**CONDITIONAL ACCEPT.** The paper meets the acceptance threshold (aggregate 6.6, all criteria >= 6.0, three Accept votes, no fatal flaws). However, three specific fixes should be made before camera-ready:

1. Reconcile DIT mean values between Sections 3.5 and 4.1 (1 hour of work).
2. Fix token efficiency arithmetic in Section 5.6 (30 minutes).
3. Clarify difficulty tier definition -- either document the medium tier or explain why it was collapsed into hard (15 minutes).

With these fixes, the paper is ready for NeurIPS 2026 submission.
