# AI Writing Pattern Audit

**Auditor:** AI Detection Specialist
**Date:** 2026-03-16
**Scope:** All seven sections of the OrchestraBench paper
**Standard:** NeurIPS 2026 submission quality

---

## Executive Summary

This paper is well above average for AI-assisted academic writing. The voice is largely consistent, the prose avoids the worst LLM cliches, and the argumentation has a confident, opinionated quality that most AI-generated text lacks. However, specific patterns recur that a trained reviewer would flag. The most common issues are: (1) mechanical parallelism in list structures, (2) residual hedging phrases, (3) occasional "generated" transitions, and (4) a few telltale word choices. The introduction and discussion are the strongest sections; experiments and methods occasionally read like template-filled output.

**Overall paper authenticity: 7.5/10** -- reads like a strong human draft that was polished with AI assistance, which is normal and acceptable. A few targeted edits would push it to 8.5+.

---

## Section-by-Section Findings

---

### 1. Introduction (introduction.md)
**Human Authenticity Score: 8.5/10**

This is the paper's strongest section. The opening paragraph has a distinctive voice -- opinionated, concrete, and punchy. Sentences like "When the assumptions match, the topology thrives. When they don't, it fails in ways that practitioners blame on model limitations rather than architectural misfit" feel crafted, not generated.

| # | Line/Para | Problematic Text | Issue | Suggested Fix |
|---|-----------|-----------------|-------|---------------|
| 1 | Para 2, L3 | "So practitioners selecting a topology for a new deployment rely on hearsay, single-framework ablations, or marketing claims" | Slightly long compound -- reads like a list dump | Break into two sentences or tighten: "Practitioners choose topologies based on hearsay, single-framework ablations, or marketing claims." |
| 2 | Para 3, L3 | "But we think it reflects something more specific" | The hedging "we think" is fine in isolation but combined with the colon that follows, it reads slightly generated | Replace with "We argue it reflects..." -- stronger and more academic |
| 3 | Contribution 1 | "We define three evaluated topology classes (with two more characterized but not yet tested), formalize each topology's structural prior..." | Heavy parenthetical overload is a Claude pattern -- packing qualifications into nested clauses | Move the parenthetical to a footnote or a separate sentence |
| 4 | Contribution 3 | "enabling practitioners to make evidence-based orchestration decisions rather than guessing" | Mild marketing language | Drop "rather than guessing" -- the point is already made |

**Strengths to preserve:**
- Opening metaphor ("hidden bet") is original and memorable
- "The field has no principled way to detect this mismatch" -- direct, confident claim
- Short punchy sentences breaking up longer technical ones
- The Smit reinterpretation paragraph shows genuine analytical thinking

---

### 2. Related Work (related_work.md)
**Human Authenticity Score: 7.0/10**

The weakest section for authenticity. It reads like a well-organized literature survey that was generated section-by-section, then stitched together. Each subsection follows the same template: [describe N papers in a paragraph] -> [synthesize a pattern from them] -> [state what's missing]. This is correct structure, but the mechanical repetition across six subsections is detectable.

| # | Line/Para | Problematic Text | Issue | Suggested Fix |
|---|-----------|-----------------|-------|---------------|
| 5 | L3, opening | "Research on multi-agent LLM orchestration has advanced along five largely independent threads" | Boilerplate survey opener. Nearly every AI-generated related work starts with "Research on X has advanced along N threads/directions" | Try: "Multi-agent orchestration research splits into five threads that rarely cite each other:" |
| 6 | Sec 2.1, L7 | "G-Designer uses a variational graph auto-encoder to generate task-aware communication topologies, producing custom graphs for each task at dispatch time. AFlow automates workflow generation through Monte Carlo Tree Search over code-represented nodes, outperforming manual pipelines by 5.7%. ADAS introduces Meta Agent Search..." | **Mechanical sentence structure.** Every sentence follows "[System] [verb]s [technique] to [goal], [achieving/producing] [result]." This is the single most detectable AI pattern in the paper. Five consecutive sentences use identical structure. | Vary the syntax. Lead with the insight, not the system name. E.g.: "The search-based approach extends further: AFlow treats workflows as code-represented nodes and uses MCTS to optimize them, while ADAS goes a level up, having a meta-agent iteratively program and improve new agent designs." |
| 7 | Sec 2.1, L9 | "A consistent pattern runs through all these systems: the topology is fixed once selected." | Good synthesis sentence, but "A consistent pattern runs through" is a Claude-ism | Try: "All these systems share a constraint: the topology is fixed once selected." |
| 8 | Sec 2.2, L13 | "DyLAN selects agent teams via unsupervised importance scoring, achieving up to 25% accuracy improvement on MMLU subsets. AgentVerse simulates human group dynamics through recruitment, communication, and decision-making stages. AutoAgents generates specialized agents tailored to each input task." | **Same pattern as #6.** Three consecutive [System] [verb]s [thing] sentences. | Mix in a sentence that starts with the problem or insight, not the system name |
| 9 | Sec 2.2, L15 | "These systems adjust who participates and what roles they play, but the underlying coordination structure remains fixed." | Clean sentence, but "These systems adjust..." followed by "DyLAN selects... AgentVerse adjusts... AutoAgents generates..." is a repeated template: [group summary] then [system-by-system enumeration] then [group limitation]. It happens in every subsection. | Restructure at least 2 of the 6 subsections to break the template. One option: lead with the limitation, then cite the evidence. |
| 10 | Sec 2.3, L19 | "A growing body of work" | Classic AI hedge phrase | Drop. Start with the concrete: "Several recent systems extract structural signals from execution traces..." |
| 11 | Sec 2.3, L21 | "The key insight from this thread is that..." | Mechanical meta-commentary. Human researchers don't usually announce "the key insight from this thread is" -- they just state the insight. | Try: "Execution traces contain the information needed to assess whether the current strategy is working -- MAST proves this with enough granularity to distinguish 14 failure categories." |
| 12 | Sec 2.3, L21 | "The diagnostic capability exists; the closed-loop connection to topology decisions does not. The trace-to-topology feedback loop is missing." | The semicolon structure is fine, but the last sentence ("The trace-to-topology feedback loop is missing") is redundant -- it restates what was just said. | Cut the last sentence. The semicolon sentence already makes the point. |
| 13 | Sec 2.4, L25 | "Model routing demonstrates that learned selection between alternatives reduces cost while maintaining quality, providing the algorithmic template for topology switching." | Heavy clause-stacking: [X demonstrates that Y], [providing Z]. This is a Claude pattern -- trying to pack two ideas into one sentence via a participial phrase. | Split: "Model routing demonstrates that learned selection between alternatives reduces cost while maintaining quality. It also provides the algorithmic template for topology switching." |
| 14 | Sec 2.5, L31 | "Three concurrent papers approach runtime adaptation from different angles without closing the gap." | "without closing the gap" is dismissive boilerplate | Try: "Three concurrent papers approach runtime adaptation from different angles." Then state what each does before noting the remaining gap. |
| 15 | Sec 2.6, L37 | "The literature reveals a structural gap" | "reveals a structural gap" is AI survey boilerplate | "The literature leaves a structural gap:" or "No prior work provides..." |

**Structural concern:** The six subsections (2.1-2.6) all follow an identical three-beat template: (a) describe systems, (b) note the pattern, (c) state the gap. This regularity is a strong AI signal. A human researcher would vary the structure -- some subsections might lead with a question, others with a controversy, others with a historical progression. Recommend restructuring at least 2 of the 6 subsections to break the template.

---

### 3. Methods (methods.md)
**Human Authenticity Score: 7.5/10**

Solid technical writing. The formalism (D, I, T definitions) is clean and the examples are well-chosen. However, the section has a "filled template" quality in places -- particularly the topology descriptions in 3.2, which follow a rigid pattern.

| # | Line/Para | Problematic Text | Issue | Suggested Fix |
|---|-----------|-----------------|-------|---------------|
| 16 | L1 | "The introduction argued that every orchestration topology carries implicit assumptions about task structure, and the related work established that no prior study makes these assumptions explicit or tests them under controlled conditions." | **Mechanical transition.** "The introduction argued... and the related work established..." is meta-narrative that reads like a template connector. | Drop the meta-reference. Start with: "Every orchestration topology carries implicit assumptions about task structure. This section formalizes both sides..." |
| 17 | Sec 3.2, Flat | "Flat conversation organizes agents as equal participants... This topology assumes low decomposability and high iterativeness, sitting at approximately (D, I, T) = (0.2, 0.8, 0.3). It handles iterative refinement naturally but struggles when tasks decompose into parallel tracks." | The three topology descriptions follow an identical template: [Name] [organizes/assigns/structures] [description]. [Prior coordinates]. [Strength] but [weakness]. | Vary the structure for at least one topology. E.g., lead with the failure mode: "When tasks decompose into parallel tracks, flat conversation breaks down. Its agents are..." |
| 18 | Sec 3.5, L51 | "We evaluate on 82 custom tasks (12 easy + 70 hard) spanning three categories selected for complementary D-I-T coverage." | "spanning three categories selected for complementary coverage" is a generated-sounding qualification chain | Simpler: "We evaluate on 82 custom tasks (12 easy, 70 hard) across three categories chosen for structural diversity." |
| 19 | Sec 3.5, L53-57 | "**Coding** (30 tasks): implementation, debugging, and refactoring tasks. These cluster at high D (mean 0.72)... **Research** (26 tasks): information synthesis... These cluster at high T (mean 4.1)... **Reasoning** (26 tasks): logic, game theory... These cluster at high I (mean 0.64)..." | Three parallel descriptions with identical structure: [Category] (N tasks): [types]. These cluster at [high X], [moderate Y], [low Z], because [reason]. | OK for a methods section to be structured, but add one sentence of narrative color to at least one category to break the pattern. E.g., "Reasoning tasks proved hardest to annotate -- multi-hop logic required judgment calls about where revision begins and sequential extension ends." |
| 20 | Sec 3.4, L47 | "The wrappers range from 200 to 600 lines of Python, deliberately lightweight to minimize the risk that implementation quality rather than topological differences drives performance variation." | Good content but the clause "to minimize the risk that implementation quality rather than topological differences drives performance variation" is a long subordinate clause that reads generated | Shorter: "The wrappers are 200-600 lines of Python, kept deliberately lightweight so implementation quality doesn't confound the topology comparison." |

**Strengths to preserve:**
- Operational definitions of D, I, T with concrete examples
- The alignment hypothesis formalization (Sec 3.3) is clean
- Falsifiability claim is a strong, confident move
- "Tasks are hand-constructed to cover the full D-I-T space rather than sampled from existing benchmarks, giving us control over structural diversity at the cost of external validity" -- honest, self-aware

---

### 4. Experiments (experiments.md)
**Human Authenticity Score: 7.0/10**

The shortest section and the most template-like. It largely restates content from Methods, which itself is a red flag (generated text often doesn't track what was already said). The prose is functional but flat.

| # | Line/Para | Problematic Text | Issue | Suggested Fix |
|---|-----------|-----------------|-------|---------------|
| 21 | L1-5 | "We construct a suite of 82 tasks across three categories: coding (implementation, debugging, refactoring), reasoning (logic, game theory, constraint satisfaction), and research (information synthesis, cross-source verification)." | **Near-duplicate of Methods 3.5.** This sentence restates almost verbatim what was already established. | Since Methods and Experiments are separate sections, the Experiments section should reference Methods, not repeat it. "Using the 82-task suite described in Section 3.5, we..." |
| 22 | L5, mid-para | "Getting annotators to agree on D and I proved harder than expected." | Good -- this is the most human-sounding sentence in the section. Preserve it. | No change needed. This is the kind of candid, experience-based observation that AI doesn't produce. |
| 23 | L13-15 | "All three evaluated topologies are implemented as Python wrappers around Claude Opus 4.6 (primary backbone)." | Restates Methods 3.4 almost exactly. | Reference: "Implementation details are in Section 3.4; here we describe..." |
| 24 | L15 | "Each wrapper exposes a uniform interface: solve(task_prompt, tools, budget) -> (answer, trace)." | Good, concrete detail. Preserve. | N/A |
| 25 | L19 | "Code and annotation data will be released under an open-source license upon publication" | Standard boilerplate, fine for a methods section, but feels like a template-inserted sentence | Consider moving to a footnote or the supplementary section |

**Structural concern:** Sections 3.5/3.6 (Methods) and 4.1/4.2/4.3 (Experiments) overlap heavily. This is a common AI pattern: each section is generated somewhat independently, leading to redundancy. Recommend merging or clearly delineating what each section covers vs. references.

---

### 5. Results (results.md)
**Human Authenticity Score: 8.0/10**

Returns to the confident voice of the introduction. The data is presented clearly, and the analysis feels authored rather than generated. The difficulty-dependent analysis (5.2) is particularly strong -- specific numbers tied to specific mechanisms.

| # | Line/Para | Problematic Text | Issue | Suggested Fix |
|---|-----------|-----------------|-------|---------------|
| 26 | L14 | "What was a single-run observation in our pilot is now a replicated structural effect." | Good sentence. Preserve. | N/A |
| 27 | L24 | "The crossover is stark." | Fine as emphasis, but "stark" is slightly overused in AI writing | Minor -- could replace with "sharp" or "clean" for variety |
| 28 | L30 | "This decomposes the multi-agent advantage as follows:" | "as follows:" before a colon-formatted breakdown is a mild AI pattern | Try: "The decomposition: of the 45-percentage-point gap..." |
| 29 | L30 | "**Structure accounts for approximately two-thirds of the multi-agent advantage; compute accounts for one-third.**" | Good, bold claim with evidence. Preserve. | N/A |
| 30 | L48 | "We want to be direct about what 82 tasks can and cannot establish." | Excellent. Human voice. Preserve. | N/A |
| 31 | L50-58 | Limitations subsection | The limitations are admirably honest and specific. This reads like a researcher who has thought about the weaknesses, not AI listing generic caveats. | Preserve as-is |
| 32 | L58 | "The direction remains clear: topology choice is invisible on easy tasks, decisive on hard ones, and predictable from DIT characteristics." | Strong closing. The tricolon (invisible/decisive/predictable) is a human rhetorical device, not an AI pattern. | Preserve |

**Strengths to preserve:**
- Specific numbers throughout (89% vs. 33%, 88pp gap)
- The agent-count control section (5.3) is well-reasoned
- Limitations section is genuinely candid
- The mechanism-level analysis ("hierarchical fragments cross-cutting concerns across executors") shows domain understanding

---

### 6. Discussion (discussion.md)
**Human Authenticity Score: 7.5/10**

Mixed. The opening and the Smit reinterpretation (6.2) are strong. The future work section (6.4) and limitations (6.5) have AI patterns.

| # | Line/Para | Problematic Text | Issue | Suggested Fix |
|---|-----------|-----------------|-------|---------------|
| 33 | L1 | "Can orchestration topology effectiveness be predicted from task characteristics? The results from 82 tasks and 282 runs say yes." | Strong opening. Question-answer structure is effective here. | Preserve |
| 34 | L1 | "These results establish the direction of the effect; future work with repeated trials and more topologies will quantify it precisely." | Hedging that contradicts the confidence of the preceding sentences | Either commit to the claim or put the hedge elsewhere. The juxtaposition of "say yes" and "establish the direction" is jarring. |
| 35 | L1 | "The practitioner's question shifts from 'which topology is best?' to 'which topology fits this task?'" | Good reframing. Preserve. | N/A |
| 36 | L9 | "Two patterns stand out." | Mild AI transition phrase. | Try: "The selection rules reveal two complementary niches." |
| 37 | L13 | "From the alignment perspective, the negative result was predictable" | Good analytical insight. Preserve. | N/A |
| 38 | L17 | "DIT scores were assigned by the authors; independent annotation with inter-rater reliability is a priority for future work." | Candid. Preserve. | N/A |
| 39 | L21-24 | Future work bullet points | **Mechanical parallelism.** Each bullet starts with a bold label then follows the same structure: [Bold label]. [One sentence of setup]. [One sentence naming a prior work]. [One sentence of aspiration]. | Vary the bullets: make one longer with a specific research question, make another shorter and more speculative. Break the template. |
| 40 | L28 | "The limitations reflect the study's scope." | Empty throat-clearing. | Cut entirely. Start with the first substantive sentence. |
| 41 | L28-29 | "The sample size (82 tasks, single run per cell, 282 total runs) rules out confidence intervals and pairwise significance tests" | Wait -- Results 5.1 says "three times with different random seeds" and reports CIs. Discussion 6.5 says "single run per cell" and "rules out confidence intervals." **This is a factual contradiction**, likely from an earlier draft version that was not fully updated. | Fix the contradiction. The results section describes 3-seed replication; the discussion limitations should reflect that. |
| 42 | L32 | "Principled topology selection has a direct resource implication: our pilot results suggest potential token savings compared to default single-topology strategies, though precise estimates require the full-scale study with repeated trials." | Heavy hedging chain: "suggest potential... though precise estimates require..." | Tighter: "Principled topology selection saves tokens -- our results show debate is 15% more cost-efficient per correct answer on hard tasks -- though precise savings depend on the deployment mix." |

---

### 7. Conclusion (conclusion.md)
**Human Authenticity Score: 8.0/10**

Tight and confident. Avoids the worst conclusion clichs ("In conclusion," "This paper has presented"). The final sentence is memorable.

| # | Line/Para | Problematic Text | Issue | Suggested Fix |
|---|-----------|-----------------|-------|---------------|
| 43 | L1 | "The multi-agent orchestration field offers practitioners dozens of frameworks and no principled basis for choosing among them." | Strong opening. Preserve. | N/A |
| 44 | L1 | "This paper addressed that gap through three contributions." | "This paper addressed" is a mild AI pattern but acceptable in a conclusion | Could replace with "We addressed that gap with three contributions." for slightly more active voice |
| 45 | L3 | "This turns topology selection from guesswork into geometry." | Excellent. Memorable, concise, human. Preserve. | N/A |
| 46 | L5 | "No single topology dominates; each topology's advantage concentrates where its structural prior matches the task." | Clean summary. Preserve. | N/A |
| 47 | L7 | "meaning topology effectiveness tracks a measurable geometric property, not merely model capability or engineering effort" | Slightly long subordinate clause | Minor. Could end at "which topology wins" and start a new sentence: "Topology effectiveness tracks a measurable geometric property..." |
| 48 | L9 | "Orchestration topology is not a detail to be decided by convention. It is a first-class design variable with measurable impact, and the tools to choose it well now exist." | Strong closing. Confident without being grandiose. Preserve. | N/A |

---

## Cross-Section Patterns

### Em Dashes
**Count: 0 used as sentence connectors.** The paper uses standard dashes correctly. No issues.

### Flagged Vocabulary
| Word | Occurrences | Verdict |
|------|-------------|---------|
| "delve" | 0 | Clean |
| "landscape" | 0 | Clean |
| "paradigm" | 1 (Sec 2.4 header "Bandit Paradigm") | Acceptable in context -- refers to a specific technical paradigm |
| "groundbreaking" | 0 | Clean |
| "transformative" | 0 | Clean |
| "moreover" | 0 | Clean |
| "furthermore" | 0 | Clean |
| "additionally" | 0 | Clean |
| "in conclusion" | 0 | Clean |
| "notably" | 0 | Clean |
| "remarkably" | 0 | Clean |
| "impressively" | 0 | Clean |
| "interestingly" | 0 | Clean |
| "it is worth noting" | 0 | Clean |
| "building on this" | 0 | Clean |
| "turning to" | 0 | Clean |

**Verdict:** The paper has been scrubbed of the most common AI vocabulary tells. This is well above average.

### Hedging Patterns
| Pattern | Occurrences | Location |
|---------|-------------|----------|
| "we think" | 1 | Introduction para 3 |
| "suggest potential" | 1 | Discussion 6.6 |
| "establish the direction of the effect" | 1 | Discussion L1 |

**Verdict:** Low hedging count. The paper is mostly confident and direct.

### Paragraph Opener Patterns
No paragraphs open with "Moreover," "Furthermore," "Additionally," "In conclusion," "It is important to note," or similar AI defaults. Openers vary between questions, declarative claims, and system descriptions. Good.

### Sentence Structure Repetition
**Primary concern:** The Related Work section (2.1, 2.2) contains chains of 3-5 consecutive sentences with identical "[System Name] [verb]s [technique]" structure. This is the paper's most detectable AI pattern. See findings #6, #8, #13.

**Secondary concern:** The topology descriptions in Methods 3.2 and the task category descriptions in 3.5 / 4.1 follow rigid parallel templates. See findings #17, #19.

### "This paper presents" / "We propose" overuse
| Phrase | Count |
|--------|-------|
| "This paper" | 3 (intro L11, conclusion L1, conclusion L5) |
| "We propose" | 1 (intro para 4) |
| "Our approach" | 0 |
| "Our work" | 2 (related work 2.4, 2.5) |

**Verdict:** Within acceptable range. Not overused.

### Passive Voice
Minimal passive voice detected. The paper predominantly uses active constructions. No action needed.

---

## Factual Contradiction (Critical)

**Finding #41 is a consistency error, not just a style issue.**

- **Results (5.1):** "Each task-topology pair ran three times with different random seeds, producing 738 primary runs"
- **Results (5.7):** "Seven-hundred-ninety-four total runs (738 primary Opus, 36 Sonnet, 20 flat-2x control) with three-seed replication"
- **Discussion (6.5):** "The sample size (82 tasks, single run per cell, 282 total runs) rules out confidence intervals and pairwise significance tests"

The Discussion limitations section describes the pre-replication state of the paper. This must be updated to reflect the 3-seed replication described in Results.

---

## Section Authenticity Scores

| Section | Score | Assessment |
|---------|-------|------------|
| Introduction | 8.5/10 | Strong human voice, confident claims, distinctive opening |
| Related Work | 7.0/10 | Template-driven structure, mechanical sentence patterns in survey paragraphs |
| Methods | 7.5/10 | Clean formalism, but topology/category descriptions are rigidly parallel |
| Experiments | 7.0/10 | Heavy overlap with Methods, functional but flat prose |
| Results | 8.0/10 | Returns to confident voice, specific analysis, candid limitations |
| Discussion | 7.5/10 | Mixed -- strong analysis in 6.1-6.2, template-like future work, one critical contradiction |
| Conclusion | 8.0/10 | Tight, memorable closing line, avoids boilerplate |
| **Overall** | **7.5/10** | |

---

## Priority Fixes (Ranked)

### Critical
1. **Fix the factual contradiction between Results and Discussion.** Discussion 6.5 says "single run per cell, 282 total runs" but Results reports 738 primary runs with 3-seed replication. This will confuse reviewers and raise red flags about whether the authors read their own paper. (Finding #41)

### High Priority
2. **Break the [System] [verb]s pattern in Related Work.** Rewrite at least the Sec 2.1 and 2.2 survey paragraphs to vary sentence structure. Lead with insights or problems, not system names. (Findings #6, #8)
3. **Vary the subsection template in Related Work.** At least 2 of the 6 subsections should deviate from the [describe systems] -> [state pattern] -> [identify gap] template. (Finding #9)
4. **Eliminate the Methods/Experiments redundancy.** Section 4.1 restates 3.5; Section 4.2 restates 3.4. Either merge them or have Experiments reference Methods without repeating. (Findings #21, #23)

### Medium Priority
5. **Remove the meta-narrative transition opening Methods.** "The introduction argued... and the related work established..." is unnecessary scaffolding. (Finding #16)
6. **Vary the topology description template in Methods 3.2.** At least one of the three should break the [Name] [organizes] [agents]... [Prior coordinates]... [Strength] but [weakness] pattern. (Finding #17)
7. **Cut empty throat-clearing in Discussion.** "The limitations reflect the study's scope" and "A growing body of work" add nothing. (Findings #10, #40)
8. **Tighten hedging in Discussion 6.6.** "suggest potential... though precise estimates require" can be replaced with a concrete number. (Finding #42)

### Low Priority
9. **Replace "we think" with "we argue" in Introduction.** (Finding #2)
10. **Vary "stark" to "sharp" or "clean" in Results.** (Finding #27)
11. **Cut redundant sentence in Related Work 2.3.** "The trace-to-topology feedback loop is missing" restates what the semicolon sentence just said. (Finding #12)
12. **Break the future work bullet template.** Vary length and structure across the four bullets. (Finding #39)

---

## What the Paper Does Well (Preserve These)

1. **Opening metaphor** ("hidden bet") -- distinctive, non-generic
2. **Confident claims** ("The field has no principled way," "Orchestration topology is not a detail")
3. **Candid limitations** ("We want to be direct about what 82 tasks can and cannot establish")
4. **Specific mechanisms** ("hierarchical fragments cross-cutting concerns across executors")
5. **Memorable closing** ("the tools to choose it well now exist")
6. **Zero use of** "delve," "landscape," "groundbreaking," "moreover," "furthermore," "additionally," "notably," "remarkably"
7. **Active voice throughout** -- minimal passive constructions
8. **Human-sounding observations** ("Getting annotators to agree on D and I proved harder than expected")
9. **Tricolon rhetoric** ("invisible on easy tasks, decisive on hard ones, predictable from DIT characteristics")
10. **Guesswork into geometry** -- a phrase that could anchor the paper's identity

---

*End of audit. 48 findings across 7 sections. 1 critical factual contradiction. 3 high-priority structural issues. 4 medium-priority style fixes. 4 low-priority word-level tweaks.*
