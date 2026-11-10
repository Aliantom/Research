<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Empirical evidence on multi-agent graph topologies versus single agents (as of November 2026)

> **TL;DR:** Topology gains are conditional: decomposable tasks gain, sequential planning loses 39-70%, one agent usually ties on equal budgets; verify with deterministic oracles first, then a different reviewer.
> **Source:** Deep-research assignment, Agentic graphs for AI systems, 2026-11-02  ·  **Updated:** 2026-11-03

Evidence grades used below:
- **[A]** controlled, multiple benchmarks, large n.
- **[B]** controlled but small, single task, single author, or a preprint with visible confounds.
- **[C]** vendor or practitioner report, no control group or n of about 1.
- "abstract only" or "via search summary" means I did not read the paper's results directly.

## What do controlled studies show for each pattern?

### Takeaway
There is no general multi-agent benefit. In the largest controlled study the mean multi-agent change was -3.5% with a very wide spread: about +81% on decomposable finance tasks, and -39% to -70% on sequential planning. On general suites, 5 of 6 re-implemented multi-agent frameworks lost to a single agent, and debate mostly fails to beat sampling plus voting. The most defensible positive results are a verification step, voting on reasoning tasks, and centralized or hierarchical structures for containing errors.

### Cited Findings

**Cross-topology studies**
- [A] Kim et al. (Google Research/MIT), *Nature Machine Intelligence* 8:1157-1172, July 2026. 260 configurations, 6 benchmarks, 5 architectures, 3 LLM families, with prompts, tools and compute budgets held fixed. Single-agent baseline performance is the strongest predictor of whether coordination helps. Cross-validated R2 is only 0.373 (0.413 with a task-grounded capability metric), and it selects the best architecture in 87% of held-out configurations — [MIT abstract page](https://www.media.mit.edu/publications/capable-language-models-can-outgrow-the-benefits-of-collaboration/)
- Same study, preprint v3 per-benchmark change versus single agent — [arXiv 2512.08296v3](https://arxiv.org/html/2512.08296v3):

| Benchmark (single-agent mean) | Independent | Decentralized | Centralized | Hybrid |
|---|---|---|---|---|
| Finance Agent (0.349) | about +57% | +74.5% | +80.8% | +73.1% |
| BrowseComp-Plus (0.318) | -35% | +9.2% | +0.2% | not extracted |
| Workbench (0.629) | range -11% to +6% | +5.6% | -1.2% | -1.2% |
| PlanCraft (0.568) | -70.0% | -41.5% | -50.3% | -39.1% |
| SWE-bench Verified (0.522, 20 instances) | -14.9% | -5.4% | -3.1% | -2.1% |
| Terminal-Bench (0.344, 20 instances) | +1.7% | not extracted | -19.2% | not extracted |

- The v1 preprint (180 configurations, 14,742 instance runs, mean 4,800 reasoning tokens per trial, matched across architectures) reports overall mean multi-agent change of -3.5% (95% CI -18.6% to +25.7%) — [arXiv 2512.08296v1](https://arxiv.org/html/2512.08296v1)
- [A/B] BenchAgent (Fu et al., preprint), GPT-4.1, 3,302 instances over 10 benchmarks, 3 runs on fixed task sets, shared harness, tools and scorer. Pooled accuracy against a single-agent reference of 76.65%: EvoAgent 79.70% (+3.05, 1.27x tokens), LLM-Debate 74.69% (-1.96, 1.39x), ChatEval 74.94% (-1.71, 4.34x), Jarvis 69.32% (-7.33, 0.36x), CAMEL 68.59% (-8.06, 0.33x), AutoGen 67.89% (-8.76, 0.49x) — [arXiv 2606.05670v2](https://arxiv.org/html/2606.05670v2)
- BenchAgent shows large task-specific swings: ChatEval +22.25 on IFEval but 4.44% versus 48.89% on AIME, and LLM-Debate +9.67 on HumanEval. On GAIA (165 tasks, single run) Jarvis scored 46.67% against 37.58%. The authors caution that results are limited to their re-implementations, and that step limits rather than a fixed budget govern token use — [arXiv 2606.05670v2](https://arxiv.org/html/2606.05670v2)

**Orchestrator-worker / centralized**
- [A] Centralized matched the best result on finance (+80.8%), was flat on BrowseComp (+0.2%), and lost on planning (-50.3%) and Terminal-Bench (-19.2%) — [arXiv 2512.08296v3](https://arxiv.org/html/2512.08296v3)
- [B] Orchestrator capacity drives results: reasoning at the orchestrator gives the largest gains, while sub-agent reasoning gives limited or negative benefit (abstract only; models and effect sizes not on the page) — [arXiv 2601.11327](https://arxiv.org/abs/2601.11327)
- [C] Anthropic: Opus 4 lead with Sonnet 4 subagents beat single-agent Opus 4 by 90.2% on an internal research eval whose size is not reported, with parallelism cutting research time by up to 90% on complex queries — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)

**Planner-executor-verifier**
- [C] Anthropic's planner, generator and evaluator harness: solo 20 min and $9 versus harness 6 hr and $200 on one prompt with one run each, and the quality difference is a qualitative judgment. On a later Opus 4.6 run the sprint construct was removed, while the planner and evaluator were kept — [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [B] Adding a high-level objective verification step to ChatDev gave +15.6% absolute on ProgramDev, and improved role specifications gave +9.4% (GPT-4o). These are interventions on one framework, not a comparison with a single agent — [MAST v2](https://arxiv.org/html/2503.13657v2)
- [C] agyn (manager, researcher, engineer, reviewer) reports 72.2% on SWE-bench Verified versus 65.0% for mini-SWE-agent at medium reasoning. Single-agent systems at higher reasoning reach 71.8% (OpenHands, mini-SWE-agent). No variance, tests or ablation are reported, and the authors are the vendor — [agyn write-up](https://dev.to/nikita_benkovich_eb86e54d/coding-agent-teams-outperform-solo-agents-722-on-swe-bench-verified-4of5); paper at [arXiv 2602.01465](https://arxiv.org/abs/2602.01465)

**Critic / reviewer loops**
- [C] Cognition: Devin Review finds an average of 2 bugs per Devin-written PR, about 58% severe. No false-positive rate, merge rate or control arm is reported — [Cognition](https://cognition.com/blog/multi-agents-working)
- [B] Injected-fault study: an Inspector or Challenger agent recovered much of the loss on code generation. Self-collab under AutoTransform went 43.3 to 75.0 with both defenses, against a vanilla 76.2 (the paper's 96.4% recovery). Camel recovered only about 55-59% by the extractor's calculation. GPT-3.5 and GPT-4o era — [arXiv 2408.00989v3](https://arxiv.org/html/2408.00989v3)

**Debate**
- [A/B] Five debate methods, 9 benchmarks, 4 models: debate "often fail[s] to outperform" Chain-of-Thought and Self-Consistency despite using more compute. Model heterogeneity is described as a consistent improver (abstract only; body not accessible) — [arXiv 2502.08788v3](https://arxiv.org/html/2502.08788v3)
- [B] Smit et al. (GPT-3.5, 7 datasets): no protocol dominates. Medprompt was best overall. Best-configuration debate versus self-consistency: MedQA 0.64/0.60, MMLU 0.73/0.78, CIAR 0.56/0.56, GPQA 0.29/0.24 — [arXiv 2311.17371v3](https://arxiv.org/html/2311.17371v3)
- [B] Math reasoning: debate gives "limited advantages over self-agent scaling", more useful on harder problems and weaker models; agent diversity gave little benefit; refinement can increase vulnerability to attacks (abstract only) — [arXiv 2505.22960v2](https://arxiv.org/abs/2505.22960v2). This conflicts on diversity with [arXiv 2502.08788v3](https://arxiv.org/html/2502.08788v3)

**Voting / ensembles**
- [B] ACL Findings 2025, seven decision protocols: voting improves reasoning tasks by 13.2%, consensus improves knowledge tasks by 2.8%, relative to other protocols. More agents help, while more discussion rounds before voting hurt (abstract only). Models in the bookmarks are Llama 3 8B and 70B — [arXiv 2502.19130](https://arxiv.org/abs/2502.19130)
- [B] With 3 responses on GSM8K, debate scored 83.2% and self-consistency 82.5%. At an equal response count debate fell behind plain majority voting (via search summary, not opened) — [arXiv 2310.01798](https://arxiv.org/pdf/2310.01798)
- [A] Independent parallel agents with no communication were the worst-containing structure on errors and lost on 3 of 6 benchmarks, with 58% overhead — [arXiv 2512.08296v3](https://arxiv.org/html/2512.08296v3)

**Blackboard**
- [B] Salemi et al. (Google, preprint): blackboard coordination gave 13-57% relative improvement in end-to-end success and up to 9% relative F1 for data discovery over the best baseline, on KramaBench and modified DSBench and DA-Code. The baselines are controller-led multi-agent systems, not single agents (abstract only) — [arXiv 2510.01285v2](https://arxiv.org/abs/2510.01285v2)
- [B] LbMAS reports competitive accuracy with lower tokens than some baselines (via search summary, not verified) — [arXiv 2507.01701](https://arxiv.org/html/2507.01701v1)

**Hierarchical**
- [B] With injected faults (GPT-3.5, AutoInject), hierarchical dropped 9.2% versus flat 26.0% and linear 31.2%. Code and math were most affected, and translation and text evaluation under 4%. Measures resilience, not baseline superiority: vanilla scores were 53.00, 54.37 and 55.62 respectively — [arXiv 2408.00989v3](https://arxiv.org/html/2408.00989v3). A search summary reported different figures (5.5/10.5/23.7%) for one version, so cite the version — [arXiv 2408.00989](https://arxiv.org/pdf/2408.00989)

**Automated research (close to the applied case)**
- [B] One ML training-script task on an RTX 3090 (GLM models, about 50 rounds at 300 s): subagents had 7 effective improvements versus 3 for agent teams. Single agent plateaued after moderate gain. Teams suffered multi-author code fragility, with errors compounding across handoffs. No repeated seeds reported — [arXiv 2603.29632](https://arxiv.org/html/2603.29632)

### Inferences
- Task structure outweighs the graph's name. Decomposable, information-gathering work gains; tightly sequential state-dependent work loses under every topology tested.
- The coding results (-2% to -15%) rest on 20 instances per configuration, so one task moves a score by 5 points. Treat them as "no evidence of benefit", not as a measured harm size.
- Finance's large gain sits on a low single-agent baseline (0.349), yet BrowseComp and Terminal-Bench also have low baselines and show no such gain. A low baseline is therefore not sufficient, and task and baseline are confounded across only six benchmarks.
- For overnight coding: keep one writer and add read-only parallel exploration plus a verification step. For overnight research: orchestrator-worker is the pattern with the best fit, though the strongest number supporting it is a vendor's.

### Gaps
- No controlled multi-level hierarchy study (depth above 2) was found. "Hierarchical" evidence is about shallow structure and fault tolerance.
- No study found that compares blackboard directly against a single agent on a matched budget.
- No controlled ablation of planner, executor and verifier against a single agent on long-running coding tasks.
- I could not read Nature MI's final text (paywall redirect), so per-benchmark numbers come from preprint v3, which could differ from the published version. The numeric threshold in the journal version is unconfirmed.

## What are the failure taxonomies, rates and token costs?

### Takeaway
MAST is the main taxonomy: 14 modes, 3 categories, with 41% to 86.7% task failure across six to seven frameworks. It has no single-agent control, so those rates describe weak 2024-25 frameworks and hard benchmarks, not a multi-agent penalty. Costs range from about 1.3x to 6x in controlled settings, up to about 15x chat and 20x+ in vendor reports.

### Cited Findings
- [A for taxonomy, descriptive for rates] MAST (Cemri et al., NeurIPS 2025 Datasets and Benchmarks): 1,642 annotated traces, 7 frameworks, 14 modes, human kappa 0.88, LLM annotator accuracy 94% and kappa 0.77 — [arXiv 2503.13657v3](https://arxiv.org/pdf/2503.13657.pdf), [NeurIPS](https://neurips.cc/virtual/2025/poster/121528)
- Failure rates (GPT-4o and Claude 3.7 Sonnet), which the authors state are not comparable because benchmarks differ: AppWorld 86.7% (Test-C), HyperAgent 74.7% (SWE-bench Lite), ChatDev 66.7% (ProgramDev), Magentic-One 62.0% (GAIA), MetaGPT 60.0% (ProgramDev), AG2 41.0% (OlympiadBench) — [arXiv 2503.13657v3](https://arxiv.org/pdf/2503.13657.pdf)
- v3 Figure 1 shares: System Design 44.2%, Inter-Agent Misalignment 32.3%, Task Verification 23.5%. Largest modes: step repetition 15.7%, reasoning-action mismatch 13.2%, unaware of termination 12.4%, disobey task spec 11.8%, incorrect verification 9.1%, no or incomplete verification 8.2%, task derailment 7.4%, fail to clarify 6.8%, premature termination 6.2% — [arXiv 2503.13657v3](https://arxiv.org/pdf/2503.13657.pdf)
- The same PDF also contains 41.8/36.9/21.3 in a section figure, and v2's text uses those numbers (with step repetition 17.14%) on a smaller 150+ trace base — [arXiv 2503.13657v2](https://arxiv.org/html/2503.13657v2). Cite the version when quoting.
- [A] Google/MIT coordination overhead versus single agent: Independent 58%, Decentralized 263%, Centralized 285%, Hybrid 515%. Mean turns: single 7.2, Independent 11.4, Decentralized 26.1, Centralized 27.7, Hybrid 44.3 — [arXiv 2512.08296v1](https://arxiv.org/html/2512.08296v1), [v3](https://arxiv.org/html/2512.08296v3)
- [A] Trace-level error amplification: Independent 17.2x, Decentralized 7.8x, Hybrid 5.1x, Centralized 4.4x. The task-level metric is only about 1.1-1.3x, and the main effect loses significance after controlling for other metrics in v3 — [arXiv 2512.08296v3](https://arxiv.org/html/2512.08296v3). The journal reports baseline-scaled error amplification surviving cluster-robust inference (P = 0.030) — [MIT abstract page](https://www.media.mit.edu/publications/capable-language-models-can-outgrow-the-benefits-of-collaboration/)
- [A/B] BenchAgent token multiples range from 0.33x to 4.34x of the single reference; the lowest-token systems were also among the least accurate — [arXiv 2606.05670v2](https://arxiv.org/html/2606.05670v2)
- [B] Three-agent checking team: 2.2-2.4x tokens — [arXiv 2610.27488](https://arxiv.org/abs/2610.27488)
- [C] Anthropic: agents use about 4x the tokens of chat, multi-agent about 15x. Token usage alone explained 80% of BrowseComp performance variance. Listed failures: spawning 50 subagents for simple queries, endless searching for nonexistent sources, duplicate work — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- [C] Anthropic harness cost: $9 to $200 on one prompt. Opus 4.6 run $124.70 total over 3 hr 50 min — [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [C, opinion, no data] Cognition's June 2025 "Don't Build Multi-Agents": parallel subagents make conflicting implicit decisions, so share full traces and default to a single thread. No measurements — [Cognition 2025](https://cognition.com/blog/dont-build-multi-agents)
- [C] Cognition's April 2026 revision: what works is writes staying single-threaded, with extra agents contributing intelligence. Unstructured swarms remain a distraction. Open delegation problems: managers over-prescribe, agents assume shared state with children, and children do not report back by default — [Cognition 2026](https://cognition.com/blog/multi-agents-working)

### Inferences
- Anthropic's 15x is relative to chat. Against its own 4x agent figure that is roughly 3.75x relative to a single agent (my arithmetic, mixing two rough figures). Do not quote 15x as "versus single agent".
- If tokens explain 80% of variance, some of the 90.2% gain may simply be more search rather than topology. This is a confound in the vendor claim, not something Anthropic isolated.
- On the Anthropic DAW run, the three QA passes cost $10.39 of $124.70, about 8% of spend and 11% of wall time (my arithmetic from its table). Rebuilds, not evaluation, dominate cost.
- The MAST modes most relevant to unattended runs (step repetition, unaware of termination, premature termination, missing or wrong verification) together are about 51% of v3 failures (my sum). They are all addressable with harness controls: loop detection, explicit stop conditions, and tests. These modes are not unique to multi-agent systems, though MAST has no single-agent arm to confirm that.

### Gaps
- No study found gives a matched single-agent failure taxonomy with the same rates, so "multi-agent-specific" share of failure is unmeasured.
- Failure rates on 2026 frontier models with the MAST method were not found.

## Is independent verification by a separate agent better than self-checking, and by how much?

### Takeaway
Yes in direction, but size depends on what "independent" means. The ranking best supported is: deterministic oracle first, then a differently trained model, then the same model without authorship cues, then same-session self-review. The effect of a fresh context alone has one weak controlled test, and its gain versus a first self-review was not significant across runs.

### Cited Findings
- [A/B] ICLR 2025, GPT-4 on Game of 24, Graph Coloring and STRIPS planning: "significant performance collapse with self-critique" and "significant performance gains with sound external verification" — [ICLR poster](https://iclr.cc/virtual/2025/poster/31014). A secondary listing gives graph coloring as 16% direct, 2% with LLM self-verification, 38% with a sound verifier (secondary, primary table not checked) — [paper listing](https://papers.lunadong.com/paper/11553); primary at [arXiv 2402.08115](https://arxiv.org/abs/2402.08115v2)
- [A/B] Lu et al. (NYU, preprint): 37 open-weight models, 9 datasets. Verifier gain (precision minus solver accuracy) ordering: self is smallest, roughly negligible for strong post-trained Qwen3 and DeepSeek models; same-family slightly larger; cross-family largest. The text gives ordering only, from figures, no numbers — [arXiv 2512.02304v1](https://arxiv.org/html/2512.02304v1)
- [A/B] AWS authors (preprint): 1,980 modernization calls, 11 models, 7 families, behavioral oracle. The producer model silently endorsed 31.7% of its own semantic drift (83/262). Per-model miss rate ranges from 0% on five models to 100% on one. Drift is non-monotone in model capability (5.6-46.7%). No separate reviewer arm exists — [arXiv 2605.21537](https://arxiv.org/pdf/2605.21537)
- [B] Khullar, Hopkins, Roger: self-attribution bias. Code correctness AUROC falls from 0.99 off-policy to 0.89 on-policy. Computer-use risk ratings of 9-10/10 sometimes drop to 0/10, with reversals about 5-10x more common than the opposite direction. Insecure-code PR approval rises "substantially" (no figure). Effect reported as stronger for previous-turn attribution — [LessWrong summary of arXiv 2603.04582](https://www.lesswrong.com/posts/Y4rFNoLaCd7GwdpZj/self-attribution-bias-when-ai-monitors-go-easy-on-themselves)
- [B, weak] Cross-Context Review: 30 synthetic artifacts, 150 injected errors, Opus 4.6. F1: fresh session 28.6, first self-review 27.1, subagent with generation prompt 23.8, second same-session review 21.7. Run 1: fresh beats self-review (d = 0.52, p = 0.008). Three-run: fresh versus self-review p = 0.26, fresh versus second self-review p = 0.004, fresh versus subagent p = 0.057. Author withdrew the v1 claim that ranking held across all runs. Confounds: Korean versus English review, one excluded run, heuristic matcher, single author — [arXiv 2603.12123](https://arxiv.org/html/2603.12123)
- [B] Credit-memo check: a 3-agent team (same model) caught 0.08-0.10 more explained defects than a single agent on three of four models, significant after Bonferroni on two. False alarms rose on all four, significant on three. Balanced accuracy changed by 0.02 or less; 300 synthetic memos — [arXiv 2610.27488](https://arxiv.org/abs/2610.27488)
- [C] Anthropic: agents "reliably skew positive when grading their own work", and tuning a standalone evaluator is "far more tractable", but the evaluator itself needed several tuning rounds and initially talked itself into approving flawed work — [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [C] Cognition argues a clean-context reviewer works by reasoning backward from the diff without the spec, and that shared bias comes from training — [Cognition 2026](https://cognition.com/blog/multi-agents-working)
- [B] MAST: verification failures are 23.5% of failures, and a verification step improved ChatDev by 15.6% — [arXiv 2503.13657v3](https://arxiv.org/pdf/2503.13657.pdf)

### Inferences
- Best-supported numeric anchors: self-review misses about a third of real drift on average, with very large model variance; a second same-session pass adds little or hurts; cross-family beats same-family beats self in verifier gain.
- Reviewer gain is likely to trade recall against false alarms. An unattended loop that acts on every finding could be driven by false positives, so gate fixes on a reproducing test or oracle.
- Because the bias is triggered by attribution, reviewers should see the artifact presented as someone else's, with no authorship framing and no producer reasoning. This is cheap and supported by the mechanism, though not directly tested as a design.
- For code, the executable test suite is the "sound verifier" of the Kambhampati line of work, and should run before any LLM reviewer.

### Gaps
- No controlled study found directly comparing same-model fresh-context review with cross-model review on natural bugs in real repositories.
- No measured false-positive rate for production review loops (Cognition gives none).
- The self-attribution paper's n and full model list were not visible in the summary I read; check the arXiv paper before quoting more than the figures above.

## When does a single agent with better context beat a graph? Do results differ with very strong or weak local models?

### Takeaway
On equal budgets with context the agent can actually use, a single agent ties or wins. Graphs become competitive when context is degraded, when extra compute is genuinely spent, or when the task decomposes. Gains shrink as model capability rises, but the assumption that weak local models automatically benefit is not reliable: one direct check with Qwen3-32B found all multi-agent systems worse.

### Cited Findings
- [A/B] Tran and Kiela (Stanford, preprint): matched thinking budgets on FRAMES and MuSiQue 4-hop, with Qwen3-30B, DeepSeek-R1-Distill-Llama-70B and Gemini 2.5. Single versus best multi-agent: 100 tokens 0.290/0.370, 500 tokens 0.390/0.380, 1k 0.418/0.388, 2k 0.421/0.403, 5k 0.427/0.420, 10k 0.426/0.423. Text only, no tools; budgets are caps; Gemini accounting approximate — [arXiv 2604.02460v1](https://arxiv.org/html/2604.02460v1)
- Same paper: with heavily degraded context (masking or substitution at alpha 0.7), Sequential multi-agent beats single; at mild degradation single leads; with distractors single stays ahead. One model and dataset only, figure-only numbers. Their data-processing argument predicts multi-agent competes only when effective context use degrades — [arXiv 2604.02460v1](https://arxiv.org/html/2604.02460v1)
- [A] Returns turn negative above a single-agent baseline of about 45% (coefficient -0.408, p < 0.001 in v1). The authors call the threshold a practical selection rule rather than a universal principle, and it predicted coordination effects in 94% of validation configurations on SWE-bench Verified and Terminal-Bench — [arXiv 2512.08296v1](https://arxiv.org/html/2512.08296v1), [MIT abstract page](https://www.media.mit.edu/publications/capable-language-models-can-outgrow-the-benefits-of-collaboration/)
- [A] Per-agent capacity becomes "prohibitively thin beyond 3-4 agents" under matched budgets, and turns scale with exponent about 1.72 with agent count — [arXiv 2512.08296v3](https://arxiv.org/html/2512.08296v3), [v1](https://arxiv.org/html/2512.08296v1)
- [A/B, single run] Weak model check: on GAIA with Qwen3-32B, the single reference scored 30.91%, every multi-agent system 17.58-26.06%. EvoAgent's GPT-4.1 gain did not carry over — [arXiv 2606.05670v2](https://arxiv.org/html/2606.05670v2)
- [B] Contrary direction: small multi-agent systems outperform substantially larger single models with direct tool access, with benefit concentrated at the orchestrator (abstract only) — [arXiv 2601.11327](https://arxiv.org/abs/2601.11327)
- [B] Debate more useful on harder problems and weaker models — [arXiv 2505.22960v2](https://arxiv.org/abs/2505.22960v2)
- [B] Voting improved reasoning on Llama 3 8B and 70B era models by 13.2% relative to other protocols — [arXiv 2502.19130](https://arxiv.org/abs/2502.19130)
- [A/B] Open-weight verifiers: strong post-trained Qwen3 and DeepSeek get almost no gain from verifying themselves; cross-family gain is largest for those — [arXiv 2512.02304v1](https://arxiv.org/html/2512.02304v1)
- [C] Cognition's "smart friend" (small primary calls big model): a too-weak primary did not know when to escalate or what to ask, while cross-frontier setups worked as capability routers — [Cognition 2026](https://cognition.com/blog/multi-agents-working)
- [C] Anthropic: an evaluator is worth it "beyond what the current model does reliably solo" and becomes "unnecessary overhead" inside the solo range. Context resets were dropped at Opus 4.5 and sprints at Opus 4.6. Model upgrade (Sonnet 3.7 to 4) gave more gain than doubling the token budget — [Harness](https://www.anthropic.com/engineering/harness-design-long-running-apps), [Multi-agent post](https://www.anthropic.com/engineering/multi-agent-research-system)
- [C] Claude Code configuration on GAIA reached 66.67% (110/165) with about 53k tokens versus single reference 459,653, but with a different runtime and unmatched limits, so observational. It suggests harness quality can dwarf topology — [arXiv 2606.05670v2](https://arxiv.org/html/2606.05670v2)

### Inferences
- Default rule for strong models: start with a single agent. Add a graph edge only if it supplies parallel independent information, an uncorrelated check, or relief from context overflow.
- For long overnight runs, context degradation is the natural trigger for handoffs. Sequential handoff with distilled state is the one topology that beat single under degradation, though on one model and dataset only.
- Local high-volume text: prefer repeated sampling with a vote and a schema or deterministic check over debate or role teams. Evidence for voting is moderate and debate weak. A cross-family spot-check by a second model, local or hosted, has mechanism support, though Lu et al. tested verifier gain in rejection sampling, not this pipeline.
- Fine-grained decomposition into per-requirement agents raises recall and false alarms roughly equally. Use it only where misses cost much more than false alarms.
- A 3080 running one model at a time pays latency for each extra agent, which the token-based studies do not measure.

### Gaps
- Almost all evidence on "very strong" models stops around GPT-5, Gemini 2.5 Pro and Sonnet 4.5. I found no controlled topology study on the current top frontier tier.
- Small-model evidence (below about 10B parameters) specific to topology is thin; Voting paper's Llama 3 8B and the Qwen3 checks are the nearest. No study measures local throughput or energy cost.
- No controlled study found of multi-hour or overnight agent runs across topologies; all controlled tasks are short. This is the biggest gap for the applied case.

## Which claims failed replication?

### Takeaway
I found no formal pre-registered replication. What exists is re-evaluation under better controls, which substantially deflates debate and framework claims and raises doubt about several headline numbers.

### Cited Findings
- **Debate beats single-agent.** Deflated by Smit et al., Zhang et al. and Yang et al., and by the equal-response comparison with majority voting — [arXiv 2311.17371v3](https://arxiv.org/html/2311.17371v3), [arXiv 2502.08788v3](https://arxiv.org/html/2502.08788v3), [arXiv 2505.22960v2](https://arxiv.org/abs/2505.22960v2), [arXiv 2310.01798](https://arxiv.org/pdf/2310.01798). Agreement prompt tuning alone moved Multi-Persona about +15% and took it from worst to best, showing that comparisons are hyperparameter-sensitive — [arXiv 2311.17371v3](https://arxiv.org/html/2311.17371v3)
- **Framework gains (AutoGen, CAMEL, ChatEval and others).** 5 of 6 fall below a normalized single agent. This is not a formal replication, because authors did not compare with original papers and re-implemented in a shared harness — [arXiv 2606.05670v2](https://arxiv.org/html/2606.05670v2)
- **Multi-agent wins on multi-hop.** Reversed at matched budgets above very low budgets, and part of the Gemini gap is an accounting artifact — [arXiv 2604.02460v1](https://arxiv.org/html/2604.02460v1)
- **Agent team +7 points on SWE-bench Verified.** Gap shrinks to 0.4 points against single agents with higher reasoning. Different configurations, so not controlled — [agyn write-up](https://dev.to/nikita_benkovich_eb86e54d/coding-agent-teams-outperform-solo-agents-722-on-swe-bench-verified-4of5). The controlled study shows -2% to -15% on 20 instances — [arXiv 2512.08296v3](https://arxiv.org/html/2512.08296v3)
- **17.2x error amplification.** Headline is trace-level; task-level is about 1.1-1.3x, and the main effect loses significance with controls; v1 also has an unreconciled "+4.6%" figure — [arXiv 2512.08296v3](https://arxiv.org/html/2512.08296v3), [v1](https://arxiv.org/html/2512.08296v1)
- **Scaling model fit.** R2_CV was 0.513 on 4 benchmarks in v1, and 0.373 on 6 once coding benchmarks were added. v1's leave-one-domain-out R2 of 0.89 should not be quoted as generalization — [v1](https://arxiv.org/html/2512.08296v1), [arXiv 2512.08296](https://arxiv.org/abs/2512.08296)
- **Fresh-context review wins in all runs.** Withdrawn by its own author in a later version — [arXiv 2603.12123](https://arxiv.org/html/2603.12123)
- **Reflexion.** A multi-agent paper reports stagnation in single-agent Reflexion and a multi-agent fix. Self-reported, unverified, and not a replication in the strict sense (via search summary) — [arXiv 2512.20845](https://arxiv.org/html/2512.20845v1)
- **Benchmark validity.** OpenAI stopped reporting SWE-bench Verified in February 2026: at least 59.4% of 138 audited, hard problems had flawed tests, plus training contamination — [OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/). Successor SWE-bench Pro reportedly has grader problems, from an unverified secondary source — [aiweekly](https://aiweekly.co/alerts/openai-drops-swe-bench-verified-backs-pro-after-flaw-audit). Tran and Kiela also saw paraphrase sensitivity suggesting memorized questions — [arXiv 2604.02460v1](https://arxiv.org/html/2604.02460v1)
- **Unconfirmed circulating claim.** "75% of self-correction gains come in the first two iterations" appears only in a blog with no primary source, per my search; do not use — [tianpan.co](https://tianpan.co/blog/2026/06/02/the-self-correction-loop-that-shared-its-verifiers-blind-spot)

### Inferences
- Claims that held up across several independent groups: debate has little or no edge over sampling and voting, gains depend on task structure, and capability reduces the marginal value of coordination.
- Claims resting on vendor evidence alone and still unreplicated: Anthropic's 90.2%, Cognition's review numbers, and the Anthropic harness's quality gain.
- Any coding-topology claim using SWE-bench Verified, including the Nature MI validation on it, inherits the benchmark's flaws. An owner-specific eval on own tasks is more informative than these published coding numbers.

### Gaps
- No independent replication of the Google/MIT study by an unaffiliated group was found.
- No third-party replication of BenchAgent or of Tran and Kiela was found. I did not search exhaustively for rebuttals.
- Most recent studies are preprints from the past 12 months; only MAST, Kim et al., Stechly et al., Kaesberg et al. and Huang et al. (resilience, [ICML 2025](https://icml.cc/virtual/2025/poster/44721)) have confirmed peer-reviewed venues in my reading.
