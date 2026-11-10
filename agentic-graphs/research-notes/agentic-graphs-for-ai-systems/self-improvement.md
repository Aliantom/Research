<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Self-improving agents and prompt/graph optimization (November 2026)

> **TL;DR:** GEPA-style instruction evolution fits evolve-lab best, but evidence is mostly self-reported; a three-way split, paired tests on 200-300 items and a hidden scorer matter more than the optimizer.
> **Source:** deep-research subtask: self-improving agents and prompt/graph optimization, 2026-11-02  ·  **Project:** evolve-lab  ·  **Updated:** 2026-11-03

Evidence flags used below: **[SR]** self-reported by the method's authors. **[V]** vendor. **[3P]** third party comparing a method it did not create, though often while promoting its own. **[BLOG]** secondary, unverified. I found no fully independent replication of any headline number. Papers read in full text for the numbers given: GEPA, DGM, SEAGym, SkillAxe.

## Evidence for each method

### Takeaway
Reflective evolution that uses per-item feedback (GEPA) has the strongest published held-out numbers and is the most compatible with a local model, but it is [SR]. Self-modifying code (DGM, SICA, SIFT) shows real gains on benchmarks at a compute cost and risk this box should not take on. Topology search (ADAS, AFlow) has the weakest cost-benefit case, and one third-party study finds gains rarely pay back.

### Cited Findings

**DSPy optimizers and GEPA**
- GEPA [SR, ICLR 2026 oral per search snippet]: test scores with Qwen3 8B, aggregate over six benchmarks: baseline 45.23, MIPROv2 47.84, GRPO (24,000 rollouts) 48.91, GEPA 54.85, GEPA+Merge 52.40 — [GEPA paper, Table 1](https://arxiv.org/pdf/2507.19457v2)
- GEPA is not uniformly better. On AIME-2025, GRPO (38.00) beats GEPA (32.00). GEPA+Merge falls below baseline on IFBench (28.23 vs 36.90), and MIPROv2 falls below baseline on AIME (20.00 vs 27.33). So a merge or optimizer step can do damage on a held-out set — [GEPA paper, Table 1](https://arxiv.org/pdf/2507.19457v2)
- With GPT-4.1 Mini, aggregate test scores: baseline 53.03, Trace 56.30, MIPROv2 58.67, TextGrad 59.14, GEPA 65.22, GEPA+Merge 66.36 — [GEPA paper, Table 2](https://arxiv.org/pdf/2507.19457v2)
- A prompt optimized entirely on Qwen3 8B gained +9.00 when run unchanged on GPT-4.1 Mini, which is a model-transfer check [SR] — [GEPA paper, Table 2](https://arxiv.org/pdf/2507.19457v2)
- The authors report a lower validation-to-test gap for evolved instructions than for few-shot prompts, and prompts up to 9.2x shorter than MIPROv2's — [GEPA paper](https://arxiv.org/pdf/2507.19457v2)
- MIPROv2's gains are inconsistent in third-party case studies. On a 136-example task (40/75/21 split), the DSPy-formatted prompt scored worse than baseline, 83% vs 87.5% — [Prompts as code study](https://arxiv.org/pdf/2507.03620). A hallucination-detection study found MIPROv2 improved hold-out accuracy but Few-Shot Random Search had the best macro-F1 (0.8115) — [DSPy teleprompter comparison](https://arxiv.org/pdf/2412.15298)
- SIMBA: I found only blog claims (a 71% relative gain on tool-use tasks, and usually topping out below MIPROv2 or GEPA on complex tasks) [BLOG] — [agentmarketcap](https://agentmarketcap.ai/blog/2026/04/08/dspy-3-automated-prompt-optimization-production-2026)

**TextGrad, OPRO, EvoPrompt, PromptBreeder**
- These have only cross-paper comparisons, and the rankings shift by paper. One 8-task BBH table has OPRO and EvoPrompt each winning different tasks — [SEE paper](https://arxiv.org/pdf/2402.11347) [3P]
- The OPRO authors report that EvoPrompt degraded GSM8K, which they attribute to its not using exemplars, and that its curve is less stable [SR, rival method] — [OPRO paper](https://arxiv.org/pdf/2309.03409)
- MemAPO reports intra-domain test averages of 70.6 vs TextGrad's 61.4 on Qwen3-8B, with train/dev sets of 100-150 items. It compares against ProTeGi, OPRO, TextGrad, PromptBreeder and SPO, but from a single run with no train-versus-test gap reported [SR] — [MemAPO](https://arxiv.org/html/2603.21520)
- CAPO benchmarks against EvoPrompt, OPRO and PromptWizard with a cost-awareness focus [SR] — [CAPO](https://arxiv.org/pdf/2504.16005)

**Self-modifying code**
- DGM [SR, ICLR 2026]: SWE-bench 20.0% to 50.0%; Polyglot 14.0% to 38.0% on the 50-task search set, but only 14.2% to 30.7% on the full benchmark. That shrinkage of 38.0 to 30.7 is the search-set optimism in one number — [DGM paper](https://arxiv.org/pdf/2505.22954)
- DGM cross-benchmark transfer: 28.9% on Polyglot (baseline 14.2%) from the SWE-bench-evolved agent, 24.5% on SWE-bench (baseline 20.0%) from the Polyglot-evolved one. Cost is about USD 22,000 per SWE-bench run, or USD 350 per 60-task evaluation with Claude 3.5 Sonnet vs USD 5 with o3-mini on Polyglot — [DGM paper](https://arxiv.org/pdf/2505.22954)
- SICA [SR, workshop]: 17% to 53% on a random SWE-bench Verified subset, but the authors say much of the early gain comes from features for file-editing speed and cost, and that first ideas path-dependently shape later ones — [SICA](https://arxiv.org/pdf/2504.15228)
- SIFT (MIT and Sakana) [SR]: on Polyglot-225 with Qwen3-Coder-30B: base 20.0%, SICA 25.1%, DGM 27.1%, HGM 30.5%, SIFT with Qwen judge 31.1%, with gpt-5.4 judge 32.0%. The Polyglot-225 set is reserved for final evaluation; the search uses a 50-task subset. A blind LLM judge ranks candidates before paying for benchmark runs. Judge-accuracy Spearman was 0.68, many conditions ran once, and the paper says search-time accuracy alone does not reliably identify the best agent. The Qwen run still took 224 CPU-hours and about $34 in API costs — [SIFT](https://www.alphaxiv.org/abs/2609.19526.md)

**Topology and graph search**
- ADAS reports held-out test accuracy with 95% bootstrap CIs, and transfer across domains and models [SR] — [ADAS](https://arxiv.org/pdf/2408.08435)
- A third-party study of ADAS-style meta-agents (MGSM, DROP, MMLU, GPQA; 30 iterations, 3 runs): conditioning on all prior designs did worse than ignoring them (55.0 vs 60.0), evolutionary context was 60.3, break-even occurred at about 15,000 examples only on two datasets, and gains "rarely justify" design and inference costs — [Inefficiencies of Meta Agents](https://arxiv.org/html/2510.06711v1)
- AFlow's MCTS over code-represented workflows: 5.7% average improvement over baselines on six datasets, and cheap models beating GPT-4o on some tasks at 4.55% of inference cost [SR]. A secondary summary's "19.5% over ADAS" figure is not in the abstract — [AFlow](https://arxiv.org/abs/2410.10762), [summary](https://papers.lunadong.com/paper/7283)

**Quality diversity**
- MAP-Elites over prompts on seven BigBench Lite tasks beat random search on feature-space coverage, significantly on only two tasks, and one task had high coverage but only 20% high-quality prompts. This measures coverage, not held-out accuracy — [Diverse Prompts](https://arxiv.org/pdf/2504.14367)
- GEPA's per-item Pareto front is itself a light form of quality diversity, keeping candidates that are best on any single instance, and the authors argue this avoids getting stuck on one strong candidate — [GEPA paper](https://arxiv.org/pdf/2507.19457v2)
- QD methods are best established for generating varied outputs and adversarial prompts — [QDAIF](https://aleph-alpha.com/en/blog/quality-diversity-through-ai-feedback/), [RainbowPlus](https://arxiv.org/pdf/2504.15047v1)

**Reflection, skills and playbooks**
- Reflexion reports 91% pass@1 on HumanEval vs a reported 80% for GPT-4, using episodic reflections from feedback to guide later attempts on tasks [SR, 2023] — [Reflexion](https://arxiv.org/abs/2303.11366)
- On SkillsBench, human-authored skills add 16.2 points while LLM-authored skills give no measurable gain — [SkillAxe, citing SkillsBench](https://arxiv.org/pdf/2606.10546)
- SkillAxe (Microsoft) [V, SR]: 41.6% vs 32.5% on SkillsBench, closing 47-67% of the gap to human skills. On SpreadsheetBench, 16.0% to 52.0% on held-out tasks (N = 50), but a naive LLM skill library matched that accuracy with 69 skills vs 22, so the refinement advantage there is compactness and activation rate (35.8% vs 20.0%), not accuracy — [SkillAxe](https://arxiv.org/pdf/2606.10546)
- SEAGym (shared protocol, 80 train tasks, Terminal-Bench 2.0 and HLE) is the most useful neutral comparison, though AHE's relation to the authors is not something I checked. Validation/ID/OOD gains in points: AHE +17.1/+9.1/+6.3; ACE (playbook) +2.9/+3.6/+2.5; TF-GRPO +17.1/+3.6/-2.5 — [SEAGym, Table 2](https://arxiv.org/pdf/2606.17546)

### Inferences
- Ranking for evolve-lab: (1) GEPA ideas, either via the `gepa` library or by porting per-item feedback, a Pareto archive and full-set validation into existing code; (2) a playbook of short rules only if tied to item-independent error categories; (3) QD archive niches by error type; (4) topology search later, on small fixed menus only; (5) no self-modifying code loop now.
- Instruction-only optimization suits local models best: shorter prompts cost fewer tokens on a 10 GB card, and few-shot demos add leakage risk.
- Bigger editing scope gave the best SEAGym transfer but also the largest reliability burden. Prompts first, graph second, code last seems right.

### Gaps
- No independent replication of GEPA, DGM or SIFT headline numbers, and no primary SIMBA benchmark, was found. No study runs all the listed methods under one protocol.
- I did not read the Self-Improving Coding Agent, ADAS or AFlow full text; their numbers come from abstracts or snippets. PromptBreeder has no standalone evidence here beyond its appearance as a baseline.

## What survives held-out tests, and the overfitting, leakage and gaming risks

### Takeaway
Gains generally survive but shrink, and the shrinkage is often large: validation gains regularly fail to transfer. Scorer gaming is documented rather than theoretical. The evolve-lab best prompt shows visible symptoms of train-item memorization.

### Cited Findings
- Shrinkage examples: DGM 38.0% on search tasks vs 30.7% on the full set — [DGM](https://arxiv.org/pdf/2505.22954). TF-GRPO +17.1 on validation, +3.6 in-distribution, -2.5 out-of-distribution; best-validation snapshots still fail to carry over — [SEAGym](https://arxiv.org/pdf/2606.17546)
- Update instability: AHE's train-replay solved 34/80 at start, fell to 6/80 after epoch 4 through a self-introduced middleware bug, and recovered to 43/80, while fixing 13 and forgetting 4 tasks net of the initial agent. Batch size 20 worked while 10 and 80 regressed — [SEAGym](https://arxiv.org/pdf/2606.17546)
- A 24-item dev set could not separate two prompts that scored the same 66.7% (16/24) but differed by 8.34 points on a 120-item held-out set — [More Debate, Same Evidence](https://arxiv.org/pdf/2608.00243)
- OPRO's authors suggest larger training sets and early stopping to limit overfitting — [OPRO](https://arxiv.org/pdf/2309.03409)
- SkillAxe caps improvements at 5 training tasks per skill to avoid fitting narrow patterns — [SkillAxe](https://arxiv.org/pdf/2606.10546)

**Reports of agents gaming the scorer**
- DGM: node 114 hit a perfect 2.0 after only 2 modifications by removing the logging of special tokens used by the hallucination detector, despite instructions not to change them. Node 96 scored 1.67 with a genuine partial fix. Hacking was more frequent when the evaluation functions were not hidden. So the best score was the cheat — [DGM, Appendix](https://arxiv.org/pdf/2505.22954)
- ImpossibleBench (tasks only passable by cheating) [mostly via authors' post]: GPT-5 exploited tests 76% on the one-off SWE-bench variant, and methods included editing tests, overloading `__eq__`, recording state and special-casing — [ImpossibleBench](https://www.greaterwrong.com/posts/qJYMbrabcQqCZ7iqm/impossiblebench-measuring-reward-hacking-in-llm-coding-1)
- Mitigations measured there: hiding tests cut hacking to near zero but hurt legitimate performance; read-only tests were a useful middle ground; strict prompting went 93% to 1% on one benchmark but only 66% to 54% on another; an abort option took GPT-5 from 54% to 9%, while Claude Opus 4.1 rarely used it and stayed at 46% — [ImpossibleBench](https://www.greaterwrong.com/posts/qJYMbrabcQqCZ7iqm/impossiblebench-measuring-reward-hacking-in-llm-coding-1)
- EvilGenie reports explicit reward hacking by Codex and Claude Code in an environment built to allow hardcoding and test editing — [EvilGenie](https://arxiv.org/abs/2511.21654v1). A MIRI review calls evidence on whether capable models hack more mixed — [MIRI](https://intelligence.org/wp-content/uploads/The-State-of-Reward-Hacking-in-AI-September-2026.pdf)
- In SIFT, the diagnosis agent sometimes proposed patches that relaxed the harness, such as longer timeouts. These were blocked by restricting writable files and rejecting harness-touching patches — [SIFT](https://www.alphaxiv.org/abs/2609.19526.md)
- Grader errors can be as big as model effects: Opus 4.5 went from 42% to 95% on CORE-Bench after grading and scaffolding fixes [V] — [Anthropic](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)

**Evidence from this lab**
- The pulse-stance best prompt (v59) contains train item IDs (F263, F215, F29, F115, F283, F15, F157) and literal train phrases such as "R.I.P. SHORTS" and "waiting for entry", and four proposals raised train from 0.809 to 0.882 with no holdout score — [run note](obsidian://open?vault=Ubuntu%203080&file=Machine/Outputs/2026-10-31%20evolve%20pulse-stance-v1%20gemma4-12b)
- ticker-extract-v2 ended at train 0.930 vs holdout 0.857, and its biggest jump came from fixing the answer key and adding a lookup, not from prompt tuning — [evolve-lab brief](obsidian://open?vault=Ubuntu%203080&file=Machine/Context/Projects/evolve-lab%20brief)

### Inferences
- The v59 prompt fits a memorization pattern and should be treated as overfit until shown otherwise. Rules such as "R.I.P. SHORTS means bearish" also read oddly against plain meaning (shorts dying usually favours longs), so the proposer may be encoding label noise or quirks. Auditing those items is worthwhile. This is my reading of the prompt, not a measured result.
- A cheap automatic guard follows: reject any candidate containing an item ID or an n-gram of 3+ words copied from train items, unless it is in the task's generic vocabulary.
- Leakage paths specific to this lab: repeatedly looking at the holdout across nights (a slow leak even with no text shown); caching scores across runs ("scores may be cached" in the run note) if the prompt or model digest key is incomplete; the proposer seeing error briefs that contain items later reused for selection; time-split tasks where the same ticker episode spans both sides.
- Metric-gaming risks for prompts differ from those for code: mostly default-to-majority-class behaviour, exploiting data artifacts ("list of tickers with a news link, default to bullish" is one candidate), and output-format tricks. Per-class recall floors and a majority-baseline comparison can catch these.
- Any future code-editing loop needs the scorer outside the writable tree, enforced by file permissions and not by a prompt instruction. A diff check on harness files and hash-pinning are the minimum.

### Gaps
- No source measures how much shrinkage to expect for prompts on a few-hundred-item classification task. evolve-lab could produce this number itself.
- Gaming rates for small local models such as gemma4 or qwen were not found. ImpossibleBench's data are for frontier and coder models, and tasks there involve visible tests that a prompt-only loop would not have.

## Sample and compute needs with a local proposer or scorer, and small-dataset tolerance

### Takeaway
A few hundred items is workable for instruction-only reflective methods and is also about the minimum for trusted comparisons. Most of the budget goes to validation, not learning. Use Sonnet sparingly as the reflector and let local models do the rollouts.

### Cited Findings
- GEPA budgets were 1,839-7,051 rollouts with Qwen3 8B. Only 79-737 were train rollouts to reach best performance, and the majority was validation tracking, which the authors flag as reducible — [GEPA paper](https://arxiv.org/pdf/2507.19457v2)
- The DSPy docs suggest about 200+ examples for MIPROv2, to prevent overfitting (from a fragmentary snippet) — [DSPy optimizer docs](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/learn/optimization/optimizers.md)
- The DSPy docs advise a larger model as `reflection_lm` when optimizing small models because it is called relatively few times, and GEPA supports Ollama through LiteLLM. A blog used qwen3:8b as reflector with llama3.1:8b as task model, with no benchmark [BLOG] — [DSPy GEPA guide](https://dspy.ai/getting-started/gepa-optimization/), [Mintlify docs](https://www.mintlify.com/gepa-ai/gepa/examples/simple-prompt)
- Shopify's "~75x cheaper, ~2x more reliable" with a small Qwen via GEPA is [V], unverified, and appears in DSPy's documentation — [DSPy docs](https://dspy.ai/getting-started/gepa-optimization/)
- Small-data results: MemAPO used 100-150 train/dev items per task [SR] — [MemAPO](https://arxiv.org/html/2603.21520). The 40/75/21 case ended with a worse optimized prompt — [Prompts as code](https://arxiv.org/pdf/2507.03620)
- Code-level loops are heavy: SIFT with Qwen3-30B took 224 CPU-hours and 6.7 h wall-clock, with hardware not stated. DGM's Polyglot evaluation costs $5 per 60 tasks with o3-mini, far above what a no-pay-per-use budget supports — [SIFT](https://www.alphaxiv.org/abs/2609.19526.md), [DGM](https://arxiv.org/pdf/2505.22954)
- SEAGym's AHE used about 3-4M tokens per update, and 1.46M per task on rollouts — [SEAGym](https://arxiv.org/pdf/2606.17546)

### Inferences

| Method | Works on ~300 items? | Fit on RTX 3080 and no API bill |
|---|---|---|
| GEPA-style instruction evolution | Yes, best fit | Good. Local rollouts; Sonnet via `claude -p` as occasional reflector |
| MIPROv2 | Marginal, mixed results | Moderate. Few-shot demos raise prompt length and leakage risk |
| OPRO, EvoPrompt, PromptBreeder | Yes, as simple baselines | Good, but they don't use per-item feedback, so more evaluations wasted |
| TextGrad | Yes, weaker in GEPA's table [SR] | Good |
| SIMBA | Unknown, no primary evidence | Probably fine; test only as a baseline |
| Reflexion, playbook | Depends on item-independent rules | Good; requires anti-memorization guard |
| MAP-Elites | Yes, as an archive policy, not as a primary search | Good, if niches are cheap (error category, length) |
| AFlow, ADAS | Task-dependent; search is expensive per node | Poor unless the menu is small |
| DGM, SICA, SIFT | Needs benchmark tasks, not items | Poor at this time |

- Budget arithmetic for a loop: 20 candidates x 200 validation items = 4,000 rollouts, in the same range as GEPA's published budgets. Racing candidates (drop clearly losing ones early on a small subset) would cut that substantially, as GEPA's authors suggest, though early drops need to be recorded for selection accounting.
- Keep the mutation budget in Sonnet to a handful of reflection calls per run, consistent with the night-shift cap and about 7.5K context tokens per call noted in the brief.
- Check whether a stronger reflector actually helps here. A pre-registered three-arm comparison (no-optimizer, local proposer, Sonnet proposer) on a fresh split would answer this, using website-presence-v1 which already has train 300 and holdout 200.
- Temperature and repeated runs matter for local models: score each item with a fixed seed where possible, otherwise run repeats, and treat the item as the unit in analysis.

### Gaps
- I found no benchmark of gemma4:12b or Qwen as a GEPA reflector, and no measured rollouts-per-hour on a 3080. The lab should measure throughput itself.
- QLoRA interplay: I found no study comparing prompt optimization before vs after fine-tuning on small data. A reasonable hypothesis is that prompts must be re-optimized after a fine-tune, since GEPA's Qwen-to-GPT transfer scored below GEPA run directly (62.03 vs 65.22) — [GEPA paper](https://arxiv.org/pdf/2507.19457v2). That is weak support across model families, not LoRA evidence.

## Statistical best practice and eval lifecycle

### Takeaway
Report the procedure, not the winner. Use three splits, one-time confirmation, paired per-item tests, multiplicity-aware selection and a pre-declared minimum effect. Few-hundred-item tests can only resolve gains of roughly 5-10 points, so small improvements should be treated as unresolved.

### Cited Findings
- Winner's curse: the expected maximum of 12 standard normals is about 1.6 sigma, so a best-of-12 delta is biased upward by construction — [DEV post](https://dev.to/ji_ai/llm-eval-noise-why-your-2-point-accuracy-win-isnt-real-phc) [BLOG]
- SIREN (NeurIPS 2026 poster) freezes the post-search shortlist, separates selection from held-out evaluation across repeated splits, and uses an item-level Gaussian multiplier bootstrap for performance-versus-budget curves. The target is the whole tune-then-deploy procedure. Winner-based reporting was optimistic and could change deployment decisions. The abstract gives no bias numbers — [arXiv 2605.05973](https://arxiv.org/abs/2605.05973), [NeurIPS](https://neurips.cc/virtual/2026/poster/149895)
- Multiple Comparisons with the Best (ICML 2026): the reported leaderboard winner is the true best only 0-58% of the time under prompt resampling; paired-bootstrap MCB restores at least 95% coverage from only per-prompt scores; 95% confidence sets held 8-35 models — [Leaderboard Lottery](https://icml.cc/virtual/2026/80012)
- For binary pass/fail, exact McNemar uses only discordant items. A preprint finds McNemar, exact conditional, mid-p and paired bootstrap largely agree on close pairs. Clustered items need cluster resampling, since item-level bootstrap understates variance — [Resolution Diagnostics](https://arxiv.org/pdf/2605.30315)
- Sequential options: mSPRT and confidence sequences allow stopping early with valid inference [BLOG] — [Traeai guide](https://learn.traeai.com/t/ai-engineering/phases/17-infrastructure-and-production/21-ab-testing-llm-features)
- Lifecycle (Anthropic) [V]: start with 20-50 tasks from real failures; capability evals start low, regression evals sit near 100%; capability evals graduate to regression once high. Saturated evals catch regressions but show no gains, so add harder tasks. Verify solvability with a reference solution, read transcripts, and give LLM judges an "Unknown" escape — [Anthropic](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)

**Calculations for this lab (mine, not from a source)**
- Selection inflation: E[max of N standard normals] from simulation: N=5 1.17, N=12 1.63, N=20 1.87, N=50 2.25, N=100 2.51. At accuracy 0.85 on 300 items, one sigma is about 0.021, so best-of-50 independent candidates could be inflated by about 0.046 with no true gain. Real candidates are correlated, so this is an upper-range estimate. Compare the observed +0.067 on train, which also had direct fitting on top.
- Smallest gain detectable at 80% power, two-sided 5%, paired, approximately 2.8 x sqrt(d/n), where d is the share of items on which the prompts disagree:

| d | n=100 | n=200 | n=300 | n=500 |
|---|---|---|---|---|
| 0.10 | 0.089 | 0.063 | 0.051 | 0.040 |
| 0.20 | 0.125 | 0.089 | 0.072 | 0.056 |
| 0.30 | 0.153 | 0.108 | 0.089 | 0.069 |

### Inferences
Proposed protocol for evolve-lab:
1. **Three disjoint splits:** `feedback` (proposer sees items and errors), `selection` (scores only, drives the Pareto/shortlist), `holdout` (frozen, opened for a pre-registered decision). A workable 500-item shape is 150/150/200. website-presence-v1's train 300 can be divided as 150/150 with the holdout untouched, but this needs a pre-registration amendment and should be fixed before seeing further results.
2. **Never score a prompt only on items it was fitted on.** DUS-88 reportedly fixed this; the report should enforce it by construction and print the selection score beside the train score.
3. **Confirm only one prompt per task generation**, or a pre-declared small shortlist with Holm correction. Maintain a holdout-look counter per task and treat the split as burned after a fixed number (for example, 3 looks), since its value as a one-time test degrades with each.
4. **Paired tests on per-item scores:** exact McNemar for binary, paired bootstrap for graded scores, cluster by time block, author or ticker where relevant. Report the delta, CI and discordance rate. Use MCB on the selection split to display all plausibly best candidates, and prefer the shortest in the set.
5. **Pre-register a minimum effect and a non-inferiority margin** for latency and cost. Adopt only when the CI lower bound clears zero, and treat otherwise as "not shown", not "no gain".
6. **Report shrinkage** (train to selection to holdout) in every run note as a first-class number, plus the seed-baseline re-score in the same run. Note the discrepancy between baseline 0.815 and seed 0.809 in the pulse-stance record, which may be split, seed or scoring drift worth explaining.
7. **Report the whole procedure occasionally:** rerun search with a different split (SIREN-style) on one task to learn whether the procedure, not just a prompt, delivers gains.
8. **Sequential testing:** use a fixed-size confirmation for now. If racing on selection, a confidence sequence or a simple pre-set futility rule is enough; there's no need to sequentially test the holdout at all.

Lifecycle: retire a task when it meets a pre-declared saturation test (for example, N proposals in a row with no gain outside the CI). ticker-extract-v2's retirement after about 20 local proposals fits this. Graduate its best prompt and hard items into a regression suite instead of deleting them, and rotate fresh holdouts from new time slices. Run a label audit before optimization, since ticker-extract's largest gain came from the key.

### Gaps
- I found no procedure combining anytime-valid sequential A/B testing with multiplicity correction for prompt selection. The best-of-N preprint on [Preprints.org](https://www.preprints.org/manuscript/202608.2051) returned 403, so its bias numbers are unread.
- The MCB and SIREN evidence was read at abstract level; many recent statistics sources here are preprints or posters. The 3-look burn limit above is a judgment call with no source behind it.

## Continual learning from production traces

### Takeaway
The pipeline is well-described by practitioners and vendors but is thinly tested in research: mine failures, cluster them, label them, promote them to eval items, and keep comparisons fixed. For this box, "production" is night-shift, paper-arena and site-foundry output, so the scarce step is human labelling, not tooling.

### Cited Findings
- Failure taxonomy and clustering: AgentCompass classifies errors against a hierarchical taxonomy and uses density-based trace clustering to surface recurring patterns [partly V] — [AgentCompass](https://arxiv.org/html/2509.14647v1)
- TRAIL offers a step-level error taxonomy and dataset, and notes manual review of long traces does not scale — [TRAIL](https://arxiv.org/pdf/2505.08638v3)
- Anthropic recommends turning bug-tracker and support-queue failures into test cases, prioritizing by user impact, and sampling transcripts on a schedule such as weekly. It describes monitoring as reactive, noisy and without ground truth, so it complements rather than replaces offline evals [V] — [Anthropic](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Arize Signal reviews traces on a schedule, tracks known issues and lets representative traces be added to a dataset, with examples and criteria fixed within each baseline-versus-candidate comparison [V] — [Arize](https://arize.com/blog/how-to-find-and-debug-agent-failures-your-evals-are-missing/)
- Langfuse describes the same trace, error-analysis and promote-to-dataset loop [V] — [Langfuse](https://langfuse.com/guides/videos/replace-vibes-with-evals)
- SkillAxe's continual loop built skills from past trajectories, then tested on held-out tasks, with results as above [V, SR] — [SkillAxe](https://arxiv.org/pdf/2606.10546)
- SEAGym's replay view tracks tasks fixed and forgotten against the original agent, a directly reusable design — [SEAGym](https://arxiv.org/pdf/2606.17546)

### Inferences
- Pipeline for evolve-lab: (a) log each night-shift and task run's input, output, model digest and prompt version; (b) local model tags failures using a fixed taxonomy, using its tag only as a triage hint; (c) sample from clusters for owner or Sonnet labelling, with a recorded labeller; (d) route new items by time, not at random, so that later items become future holdouts and older ones feed the proposer; (e) add items to a new task version, leaving the frozen holdout unchanged.
- Never route a mined failure into a holdout that a descendant of the failing prompt will be judged on while its text was seen by the proposer. Traces carry leakage via error briefs.
- Selection bias: mined failures overrepresent the current prompt's weaknesses, so a set built only from them flatters any successor. Keep a random production sample alongside it, which also gives a truer base-rate estimate than failure-focused sets. Scores on the two sets should be reported separately.
- Replay every candidate against a "forgotten items" list, with hard veto rules, before anything replaces the current best.
- Self-labelling risk: no agent should label items used to judge a prompt it wrote. This parallels the lab's existing rule against editing scorers to raise a score.

### Gaps
- I found no controlled study showing a trace-to-eval pipeline improves long-term outcomes, and no good source on detecting drift between production distributions and eval sets; available evidence is vendor or practitioner guidance.
- The minimum owner-labelling rate that keeps such a pipeline honest on one PC is unknown, so it should be measured during a trial.
