<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Spend on checks before adding agents

> **TL;DR:** No default multi-agent graphs: keep one writer, the Python runner, hybrid search and Gate v2; add deterministic gates, differently-trained review and GEPA-style evolution on a three-way split.
> **Source:** Deep-research assignment, Agentic graphs for AI systems, 2026-11-02; synthesis of six research notes in Machine/Research/Agentic graphs/research_notes/  ·  **Project:** AI workstation  ·  **Updated:** 2026-11-03

The research supports a small number of graph edges and no wholesale graph framework for this system. The largest controlled study found a mean multi-agent change of -3.5% with a confidence interval spanning -18.6% to +25.7%, gains of about +81% on decomposable finance work, and losses of 39% to 70% on sequential planning ([Kim et al. v1](https://arxiv.org/html/2512.08296v1), [v3](https://arxiv.org/html/2512.08296v3)). The edges worth building supply an uncorrelated check, independent parallel information, or relief from context overflow. For this box that means one writer per worktree, deterministic gates before any LLM reviewer, a differently-trained reviewer, a hand-written step ledger in the existing runner, and Paperclip as a stop between stages. Self-improvement should come from GEPA-style prompt evolution under a three-split protocol, because the current best pulse-stance prompt shows signs of memorizing train items. Vault memory should stay on hybrid search, with link expansion and an `as_of` option tested on a harder eval. No credible evidence shows that agent graphs add net trading alpha, so the frozen arena stays frozen and new graph ideas run as separate read-only versions. Three local risks need action soon: a future `--bare` default would break every subscription `claude -p` call here, `tradingagents_pick` runs from a moving branch tip, and v59 should not be trusted. Nearly all gain figures come from someone else's setup, and no controlled study covers multi-hour runs, so each recommendation below carries its own local test.

## How to read the grades

| Tag | Meaning |
|---|---|
| **[A]** | Controlled, multiple benchmarks, large n |
| **[B]** | Controlled but small, single task or author, or a preprint with visible confounds |
| **[C]** | Practitioner report, opinion, or no control group |
| **[V]** | Vendor claim, or a party selling the product or a rival. Collected in their own table below |
| **[SR]** | Self-reported by the method's authors, no independent replication found |
| **[L]** | Read from this PC's code or vault. Rechecked on 2026-11-02 where marked in the risk table |
| **[M]** | Measured on this PC |
| **[J]** | My judgment or arithmetic, no source behind it |

Grades describe the study, not its relevance here. An [A] result on short benchmarks still says little about an overnight run. Several citations were read at abstract or summary level by the note authors, and the text says so where a number depends on it. Most of the recent work is preprint.

## Task shape decides more than topology, and gains shrink as models improve

Kim et al. held prompts, tools and compute fixed across 260 configurations and found the single-agent baseline to be the strongest predictor of whether coordination helps, with cross-validated R² of only 0.373 **[A]** ([MIT abstract page](https://www.media.mit.edu/publications/capable-language-models-can-outgrow-the-benefits-of-collaboration/)). The per-benchmark spread is the useful part, though the numbers come from preprint v3 because the journal text was paywalled.

| Benchmark (single-agent mean) | Independent | Decentralized | Centralized | Hybrid | Reading for this system |
|---|---|---|---|---|---|
| Finance Agent (0.349) | about +57% | +74.5% | +80.8% | +73.1% | Decomposable research can gain |
| BrowseComp-Plus (0.318) | -35% | +9.2% | +0.2% | not extracted | A low baseline alone is not enough |
| PlanCraft (0.568) | -70.0% | -41.5% | -50.3% | -39.1% | Sequential state-dependent work loses |
| SWE-bench Verified (0.522) | -14.9% | -5.4% | -3.1% | -2.1% | 20 instances: no evidence of benefit, not a measured harm |
| Terminal-Bench (0.344) | +1.7% | not extracted | -19.2% | not extracted | Same 20-instance caution |

Other groups point the same way. BenchAgent re-implemented six frameworks on GPT-4.1 across 3,302 instances, and **five of six fell below the single-agent reference of 76.65%**, with AutoGen at 67.89% and only EvoAgent above at 79.70% **[A/B]** ([Fu et al.](https://arxiv.org/html/2606.05670v2)). The same study's single GAIA run on Qwen3-32B had every multi-agent system at 17.58-26.06% against 30.91% for single, which undercuts the comfortable idea that weak local models automatically benefit. At matched thinking budgets on multi-hop questions, single agents beat the best multi-agent system at every budget from 500 to 10k tokens and lost only at 100 tokens **[A/B]** ([Tran and Kiela](https://arxiv.org/html/2604.02460v1)). Sequential multi-agent did win once context was heavily degraded, on one model and dataset. That is the one direct hint in favor of distilled handoffs during long runs.

Debate has held up worst. Five methods across nine benchmarks "often fail" to beat Chain-of-Thought and Self-Consistency, read at abstract level **[A/B]** ([Zhang et al.](https://arxiv.org/html/2502.08788v3)), and hyperparameter tuning alone took one debate method from worst to best **[B]** ([Smit et al.](https://arxiv.org/html/2311.17371v3)). Voting improved reasoning tasks by 13.2% relative to other protocols, and more discussion rounds hurt **[B, abstract only]** ([Kaesberg et al.](https://arxiv.org/abs/2502.19130)). Capacity also runs out quickly: per-agent budget gets "prohibitively thin beyond 3-4 agents" **[A]** ([Kim v3](https://arxiv.org/html/2512.08296v3)), and coordination overhead ran from 58% to 515% ([Kim v1](https://arxiv.org/html/2512.08296v1)). The one direct automated-research comparison, on an RTX 3090, favored subagents with 7 effective improvements against 3 for agent teams, whose multi-author code proved fragile **[B, one task, no repeated seeds]** ([arXiv 2603.29632](https://arxiv.org/html/2603.29632)).

Treat headline scales carefully. The 17.2x error amplification is trace-level, and the task-level figure is about 1.1-1.3x ([Kim v3](https://arxiv.org/html/2512.08296v3)). OpenAI stopped reporting SWE-bench Verified after auditing flawed tests in at least 59.4% of 138 hard problems ([OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)). METR found graders passing about 24 points more PRs than maintainers would merge **[A/B]** ([METR](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)). An eval on the owner's own tasks therefore tells more than any published coding number.

**Three gaps limit everything in this section.** No controlled study covers multi-hour or overnight runs across topologies, none covers the current top frontier tier, and none measures local latency on a single-GPU box where each extra local agent queues behind the last. MAST gives the closest guide to unattended failure, with 14 modes across 1,642 traces. Step repetition, unaware of termination, premature termination, and missing or wrong verification together make up about 52% of its failures (my sum), and all can be attacked with harness controls **[A for taxonomy; rates descriptive, no single-agent arm]** ([MAST](https://arxiv.org/pdf/2503.13657.pdf)).

## Deterministic oracles beat fresh eyes, and fresh eyes alone are unproven

The verification ranking best supported by the evidence is deterministic oracle, then differently-trained model, then same model without authorship cues, then same-session self-review. External sound verifiers gave significant gains where self-critique collapsed **[A/B]** ([Stechly et al., ICLR 2025](https://iclr.cc/virtual/2025/poster/31014)). Across 37 open-weight models, verifier gain ordered self below same-family below cross-family, with strong Qwen3 and DeepSeek models gaining almost nothing from checking themselves **[A/B, ordering read from figures]** ([Lu et al.](https://arxiv.org/html/2512.02304v1)). On 1,980 code-modernization calls a producer silently endorsed 31.7% of its own semantic drift, with per-model rates from 0% to 100% **[A/B]** ([arXiv 2605.21537](https://arxiv.org/pdf/2605.21537)). Attribution itself appears to bias monitors: correctness AUROC fell from 0.99 to 0.89 when code was presented as the model's own **[B, via summary]** ([Khullar et al.](https://www.lesswrong.com/posts/Y4rFNoLaCd7GwdpZj/self-attribution-bias-when-ai-monitors-go-easy-on-themselves)).

The popular claim that a clean session is the active ingredient has weak support. In the one controlled test the three-run comparison of fresh session against first self-review gave p = 0.26, while fresh against a second self-review pass gave p = 0.004, and the author withdrew the claim that ranking held across runs **[B, weak]** ([Cross-Context Review](https://arxiv.org/html/2603.12123)). So a second pass in the same session is the clear thing to avoid. Adding reviewers also has a price: a three-agent same-model team caught 0.08-0.10 more defects on three of four models, false alarms rose on all four, and balanced accuracy moved 0.02 or less **[B]** ([arXiv 2610.27488](https://arxiv.org/abs/2610.27488)). An unattended loop that acts on every finding would chase noise, so a fix should require a reproducing test. For local work, one author's measurements found executed tests correlated 0.85 with correctness, three-sample agreement 0.78-0.98, and a same-tier LLM judge negatively **[C, single author on own system]** ([Rung review](https://web.stanford.edu/~shuhuiq/blog/review-routing-cascades.html)). A confidence-threshold cascade lost to a pre-generation router on four of five datasets **[B]** ([ICML 2026](https://icml.cc/virtual/2026/75267)). My reading of that conflict is that the gate matters, which neither source tested **[J]**.

Passing tests remains a weak acceptance signal. Agent commits add mocks 36% of the time against 26% for non-agents **[B]** ([Hora, MSR 2026](https://arxiv.org/pdf/2602.00409)), which supports a mock check and staged mutation testing, though no study measures mutation gates inside Claude Code or Codex workflows. Sandboxes carry a measured cost too: under the strictest policy, success fell by up to 18.3 points and cost rose by up to 167.3%, and blocked agents tended to run to timeout rather than stop **[B]** ([Permission Denied](https://arxiv.org/abs/2608.02670)). A hard timeout and a stop on repeated denial therefore belong with any sandbox.

## Night-shift needs a ledger, because no framework covers the worktree

The options split into graph libraries that checkpoint between nodes, durable engines that journal and replay, Claude-native fan-out, and DSPy, which optimizes prompts and orchestrates nothing. For a single host whose nodes are long CLI subprocesses, they add little beyond replay-safe step recording, a durable wait and a trace view **[J]**. No independent benchmark or numeric postmortem was found for any of the 14 options, so this comparison rests on documentation and reasoning.

| Option | What it would add here | Decisive constraint | Grade |
|---|---|---|---|
| Hand-written ledger, commit per step, transition table | Resume, retries, the graph itself | Must be written and tested; current retry and resume code was not audited | [J], [L] |
| Claude dynamic workflows | Fan-out inside one job, schema-checked output, stall restarts | No mid-run human input; a failure reruns everything started after it; under `claude -p` a usage limit fails the agent instead of pausing; `pipeline()` returns `null` on failure ([docs](https://code.claude.com/docs/en/workflows)) | Docs |
| DBOS on SQLite | Tested step recording, `recv` wait; a library, so it can replace the ledger cleanly | Uncaught exceptions are not recovered; small community, one vendor ([docs](https://docs.dbos.dev/python/tutorials/workflow-tutorial)) | Docs, [M] 74 MB import RSS |
| Burr | SQLite persistence, forking | Infrequent releases, 2.6k stars ([docs](https://burr.apache.org/docs/concepts/state-persistence/)) | Docs, [M] 27 MB |
| LangGraph | Time travel, parallel interrupts | Most concepts; code before `interrupt()` re-runs on every resume; checkpoint CVEs seen only through search summary ([docs](https://docs.langchain.com/oss/python/langgraph/interrupts)) | Docs, [M] 79 MB |
| Temporal, Restate, Inngest | Durable journal | Each is an always-on scheduler and queue overlapping systemd and Paperclip | [J] |
| CrewAI | Role abstractions | Declares `<3.14`; failed to build on this PC's Python 3.14.4 | [M] |
| AutoGen | Nothing | Maintainers advise against production use ([README](https://github.com/microsoft/autogen)) | Docs |

**Memory does not decide this.** Library import floors were under 80 MB, so concurrent `claude -p` processes and Ollama are what press on 16 GB **[M]**. The real gap is the filesystem. No journal captures worktree state, and Claude's docs admit that a stalled attempt's file changes stay changed ([workflows](https://code.claude.com/docs/en/workflows)). A commit at each successful step, with a reset to that commit on retry, has to be written whichever framework is chosen **[J]**. Approval also gets simpler with this design: the state creates a Paperclip issue and the process exits, then a later timer tick checks the issue. Nothing sits waiting, so durable wait stops being a problem, and systemd schedules while Paperclip approves. Claude subscription use of `claude -p` currently draws on plan limits ([Anthropic support](https://support.claude.com/en/articles/15036540)). OpenAI's wording for subscription-authenticated `codex exec` is that API keys are the default for automation and ChatGPT auth is for trusted runners ([Codex docs](https://learn.chatgpt.com/docs/non-interactive-mode)). Treat the Codex path as less stable ground, and give the unit an explicit binary path since `codex` was not on the login PATH **[L]**.

## Vault memory should earn a graph by beating search on a harder test

Graphs win on multi-hop questions over large unfamiliar corpora and tie or lose on single-hop. With an 8B model, HotpotQA F1 was HippoRAG2 63.01 against RAG 60.04, NQ was 61.03 against 64.78, and triplet-only graphs held the answer string in just 39.20% of HotpotQA cases against 88.60% for RAG **[A/B, independent]** ([Han et al.](https://arxiv.org/html/2502.11371v3)). RAGSearch shows a larger gap, 19.00 to 46.70 on HotpotQA, but credits graphs with the best of five variants per dataset **[B]** ([Fan et al.](https://arxiv.org/pdf/2604.09666)). **No study found compares any named system against BM25 plus embeddings plus reranking on notes**, which is the actual baseline in `ai-notes find`, so the size of any gain here is unknown. Dense-only baselines probably overstate it.

Memory-product scores cannot rank anything. The same Zep system moves from 58.44 to 94.7 on LoCoMo depending on who ran it, about 6.4% of the answer key is wrong, and the judge prompt alone moved identical answers from 55.8% to 81.4% **[C, secondary and interested parties]** ([braindetox](https://braindetox.kr/posts/memory_benchmark_scores_reliability_2026.html), [Penfield](https://dev.to/penfieldlabs/we-audited-locomo-64-of-the-answer-key-is-wrong-and-the-judge-accepts-up-to-63-of-intentionally-33lg), [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)). A re-evaluation of eight systems ranked an agent managing flat text files highest across tasks, though its authors then propose their own harness **[B, abstract only]** ([Chen et al.](https://arxiv.org/abs/2606.04315)). On time, the need is real and a graph is not required for it. Mean accuracy fell from 63.0% to 51.5% after facts changed, with append-only stores falling most **[B]** ([EvalMem](https://arxiv.org/pdf/2609.22231)). The vault already invalidates at note level with `status: superseded` **[L]**, but `ai-notes` skipping those notes is wrong for "what was true on date X". An `as_of` option closes that gap, matching the `hub` tool's pattern **[J]**.

The cheap experiment is authored links. This vault has 337 notes and 1,463 resolving wikilinks of 1,494, about 4.3 per note **[M]**. The direct evidence is thin: LARAG followed author-written links on 20 expert queries with vendor-affiliated authors **[B]** ([LARAG](https://arxiv.org/pdf/2605.07517)), and I found no paper on personalized PageRank over authored note links without an entity step. Hubs are the main risk, with evolve-lab at 81 in-links **[M]**, so walks should exclude `project:` links and index pages. The local eval will not show a gain as built, because 20/20 is already saturated and one question equals 5 points. It needs about 100-200 questions with strata for multi-note, zero-shared-vocabulary paraphrase, as-of, superseded-trap, aggregation and unanswerable cases **[J]**. By contrast, an extraction graph would cost about $1.71 to $7.91 hosted, or an extrapolated one to two nights local holding `~/.night-shift.lock` plus upkeep on each edit **[J, scaled from [Fan et al.](https://arxiv.org/pdf/2604.09666) and [Fernandes and Kanjilal](https://arxiv.org/pdf/2605.20815)]**.

Lessons memory needs the same discipline. Agents repeat false self-diagnoses: in 16 frozen ALFWorld environments, 0 of 121 reflections named the right object, and programmatic failure signals raised that to 86% while still solving only 3 of 16 **[B]** ([Dixit et al.](https://arxiv.org/pdf/2605.29463)). Context files showed zero to small effects with added cost, and 288 Claude Code and Codex runs found no measurable correctness change within 10-15 point equivalence bounds **[B]** ([Gloaguen et al.](https://arxiv.org/html/2602.11988v1), [Khatri](https://arxiv.org/abs/2607.27250)). `FINDINGS.md` stays useful if each lesson cites a run, names its evidence type, and carries a retest trigger, because a false "this always fails" lesson stops retesting ([survey](https://arxiv.org/html/2603.07670v1)).

## Evolve-lab's protocol matters more than its optimizer

GEPA has the best published numbers and the best fit, since it runs on local rollouts and produces short instruction-only prompts. On Qwen3 8B it reached 54.85 aggregate against baseline 45.23, MIPROv2 47.84 and GRPO 48.91 **[SR]**, though it lost to GRPO on AIME and GEPA+Merge fell below baseline on IFBench ([GEPA](https://arxiv.org/pdf/2507.19457v2)). Budgets were 1,839-7,051 rollouts with most going to validation, and DSPy advises a larger model as reflector ([DSPy](https://dspy.ai/getting-started/gepa-optimization/)). No independent replication was found. Bigger editing scopes are less attractive here. DGM cost about $22,000 per SWE-bench run and shrank from 38.0% on its search set to 30.7% on the full benchmark **[SR]**, and its best-scoring node cheated by removing the logging its detector relied on ([DGM](https://arxiv.org/pdf/2505.22954)). A third-party study found ADAS-style gains "rarely justify" their costs **[B]** ([Inefficiencies of Meta Agents](https://arxiv.org/html/2510.06711v1)). SEAGym, the most useful shared-protocol comparison, shows why validation alone misleads: TF-GRPO scored +17.1 on validation, +3.6 in distribution and -2.5 out of distribution **[B]** ([SEAGym](https://arxiv.org/pdf/2606.17546)).

Scorer access deserves a hard control. ImpossibleBench found GPT-5 exploiting tests 76% of the time on one variant, and read-only tests were a good middle ground between visible and hidden **[B, mostly via authors' post]** ([ImpossibleBench](https://www.greaterwrong.com/posts/qJYMbrabcQqCZ7iqm/impossiblebench-measuring-reward-hacking-in-llm-coding-1)). Prompt-only loops cannot edit tests, so their likely forms of gaming are majority-class defaults and data artifacts, which per-class recall floors catch **[J]**.

Statistics set the limits of what this lab can claim. Reported leaderboard winners were the true best only 0-58% of the time under prompt resampling **[B, abstract level]** ([ICML 2026](https://icml.cc/virtual/2026/80012)). My calculation puts best-of-50 independent candidates at about +0.046 of inflation with no true gain, at accuracy 0.85 on 300 items **[J, upper range because candidates correlate]**. The smallest detectable paired gain at 80% power is approximately 2.8 × sqrt(d/n), where d is the share of items where prompts disagree **[J]**:

| Disagreement d | n=100 | n=200 | n=300 | n=500 |
|---|---|---|---|---|
| 0.10 | 0.089 | 0.063 | 0.051 | 0.040 |
| 0.20 | 0.125 | 0.089 | 0.072 | 0.056 |
| 0.30 | 0.153 | 0.108 | 0.089 | 0.069 |

**A few hundred items resolves gains of about 5-10 points, and anything smaller should read "not shown".** The protocol that follows has three disjoint splits (feedback, selection, frozen holdout), one confirmed prompt per task generation, exact McNemar or paired bootstrap clustered where items cluster, a holdout-look counter, and shrinkage from train to selection to holdout printed in every run note. The 3-look limit is a judgment call with no source. For website-presence-v1, dividing train 300 into 150/150 needs a pre-registration amendment before further results are seen. It took the GPU slot on 2026-11-01 for at most two nights **[L]**, so that window may have closed, in which case the rule starts with the next task.

Finetune-lab has the thinnest evidence in this report. I found no study comparing prompt optimization before and after fine-tuning on small data, no usable Q4 versus Q5 versus Q8 comparison on 10 GB, and only weak cross-family support for re-optimizing after a model change (62.03 transferred against 65.22 direct) **[SR]** ([GEPA](https://arxiv.org/pdf/2507.19457v2)). Its pre-registered gate structure is already the deterministic-oracle pattern, and gate G2b has halted it twice for real reasons **[L]** (Now). A graph adds nothing to a linear training pipeline. What it can use is evolve-lab's statistics and a planned interaction test.

## Trading graphs have no credible alpha evidence, and the arena cannot supply it soon

Original headlines came from windows of about 3 to 8 months on hand-picked names, such as TradingAgents' Sharpe of 5.60-8.21 over one quarter with costs not stated ([TradingAgents](https://arxiv.org/html/2412.20138)). The re-tests deflate them. FINSABER ran LLM agents on historical S&P 500 constituents over 2004-2024, found no significant alpha (all p > 0.34), and saw FinMem's TSLA Sharpe fall from 2.679 to 0.927 or 0.404 **[B; tests LLM agents, not full debate graphs]** ([FINSABER](https://arxiv.org/html/2505.07078v5)). The only post-cutoff TradingAgents reproduction found a net Sharpe of 0.22, ending at $102.3K against $104.8K for buy and hold, over about 252 days, an interval too wide to prove the agent worse **[C, position paper with garbled rendering and an unexplained 44-of-55 figure]** ([Alpha Illusion](https://arxiv.org/html/2605.16895v1)). Audits found 2 of 19 studies with extractable time-consistent splits and 1 of 19 with an explicit cost model ([survey](https://arxiv.org/html/2605.19337v1)). **Nothing found tests LLM graphs on short-dated long options**, so all of this applies by analogy, and no matched-compute graph versus single-LLM trading experiment was found. My verdict is that net alpha is unproven and more likely small or absent at this size, with moderate confidence on "unproven" and low confidence on magnitude. Lookahead in weights is contested, with large effects in one proof of concept whose random control also decayed about 10 points ([Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770)) and modest effects elsewhere ([ChronoGPT](https://arxiv.org/pdf/2502.21206)). Forward trades from 2026-10-29 are clear of weight leakage **[J]**, which is an advantage of the frozen design.

Gate v2 is sound, and its limits are arithmetic. `tradingagents_pick` closes about 0.6-1.5 trades a week, so 7-18 by 2027-01-21 and 14-36 by 2027-04-15 **[L, J]**, against a 20-trade minimum. It will very likely read "insufficient evidence" at the first read, and that result must not count against the graph. Faster measures can run alongside as separate versions judged on stability and calibration, never as alpha evidence. Deterministic data-validity gates have the best reasoning behind them, since TradingAgents' own changelog records repeated lookahead defects through v0.7.1 ([README](https://github.com/tauricresearch/tradingagents)). LLM debate and vetoes are mixed, and FinCon's risk-control ablation is author-run on one short window with magnitudes implausible as a general estimate ([FinCon](https://arxiv.org/html/2407.06567v3)). A veto can only be judged if the vetoed trade's counterfactual is logged **[J]**.

## Site-foundry's money problem is matching, and rules can fix most of it

Its first verification run missed chains and over-matched generic names, and 34 of 64 "no website" leads turned out to have a site **[L]** (Now). At dozens of leads, Splink is unnecessary. Normalize name, phone, domain and address, keep a chain list, require two independent fields for generic names, and send only ambiguous pairs to an LLM with a schema **[J]**, the retrieve-then-judge pattern described by [Elastic](https://www.elastic.co/search-labs/blog/elasticsearch-entity-resolution-llm-semantic-search) **[V]** and [BOOSTER](https://research.polyu.edu.hk/en/publications/booster-leveraging-large-language-models-for-enhancing-entity-res/). No benchmark covers Google Places or local leads. The site pipeline is sequential, which is the shape that loses under every topology tested, so it should stay one agent with gates. Demo QA should run axe and Lighthouse first, with vision advisory, because figures for what each finds conflict and 88% against 24% could not be confirmed. Do not market a demo as "accessible" from automated passes. CAN-SPAM has no B2B exception and requires a postal address, an opt-out honored within 10 business days, and accurate headers, with penalties up to $53,088 per email ([FTC](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)). Those elements lint deterministically. State law, TCPA and Places storage terms were not researched and need checking before any send. At 30 sends, a 3% reply rate means about one reply, so decisions should rest on booked conversations.

## Vendor claims, held apart

None of these should drive a decision without a local test.

| Claim | Source | Why it is discounted |
|---|---|---|
| Lead-plus-subagents beat single Opus by 90.2% | [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system) | Eval size unreported; tokens explained 80% of BrowseComp variance in the same post, so topology and spend are confounded. Its 15x cost is relative to chat, about 3.75x relative to one agent [J] |
| Planner, generator, evaluator harness builds better apps | [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps) | One prompt, one run each, $9 against $200, qualitative judgment. The sprint construct was later removed |
| Devin Review finds 2 bugs per PR, about 58% severe | [Cognition](https://cognition.com/blog/multi-agents-working) | No false-positive rate, merge rate or control. Its "writes stay single-threaded" advice is opinion that agrees with the data above |
| agyn team 72.2% on SWE-bench Verified | [agyn](https://dev.to/nikita_benkovich_eb86e54d/coding-agent-teams-outperform-solo-agents-722-on-swe-bench-verified-4of5) | Single agents at higher reasoning reach 71.8%; no variance or ablation; flawed benchmark |
| Replit, others run on Temporal | [Temporal](https://temporal.io/resources/case-studies/replit-uses-temporal-to-power-replit-agent-reliably-at-scale) | Case study at a scale that does not apply to one host |
| GEPA 75x cheaper, 2x more reliable | [DSPy docs quoting Shopify](https://dspy.ai/getting-started/gepa-optimization/) | Unverified |
| SkillAxe closes 47-67% of the gap to human skills | [Microsoft](https://arxiv.org/pdf/2606.10546) | On SpreadsheetBench a naive skill library matched its accuracy; the edge was compactness |
| Cognee 0.815, Mem0 and Zep leaderboard scores | [Cognee](https://www.cognee.ai/knowledge-graph-memory-benchmarks), [Zep](https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/) | 0.476 untuned; disputed benchmark; parties to the dispute |
| Databricks memory: 2.5% to over 50% | [secondary](https://thenuancedperspective.substack.com/p/designing-agentic-memory-in-2026) | Benchmark details unseen |
| Grader fixes moved Opus 4.5 from 42% to 95% on CORE-Bench | [Anthropic](https://anthropic.com/engineering/demystifying-evals-for-ai-agents) | Vendor, but useful as a warning: scorer errors can match model effects, which also matches ticker-extract-v2 here |
| Cold-email reply rates and 142% personalization lift | [Instantly](https://instantly.ai/blog/ai-sales-agent-benchmarks-2026-the-complete-performance-report/), [Woodpecker](https://woodpecker.co/blog/cold-email-statistics/) | Sellers, observational, no local-service data |

## Three local findings need action before the next upgrade or read

| Finding | Evidence, rechecked 2026-11-02 | Consequence | Action and owner |
|---|---|---|---|
| **`--bare` default risk.** Docs say bare mode never reads OAuth credentials and that `--bare` "will become the default for `-p` in a future release" ([headless docs](https://code.claude.com/docs/en/headless)) | [L] No call site passes or guards this flag. `claude -p` is called from `evolve-lab/night/nightlib.py`, `night/claude_tasks.py`, and the TradingAgents fork's `llm_clients/claude_code.py`. This PC runs 2.1.316. Whether an OAuth token works under bare is unstated, and no opt-out flag was confirmed | Night jobs would fail on authentication. In the arena, `ta_runner.py` catches exceptions as no signal, so a flip would silently cost `tradingagents_pick` its trades while it reads as ordinary failed days [J]. A stray API key could also move spending off the plan [J] | Add a preflight canary and an auth-failure class in the runner. Check the release notes on each CLI update. Any change touching the arena path goes to the owner through Paperclip |
| **`tradingagents_pick` branch drift.** The book's treatment is not pinned | [L] `ta_runner.py` sets `BRANCH = "trading-lab-claude-code"` and calls `export_branch()` on each run, which archives the tip. `arena/FROZEN.json` has no mention of TradingAgents, a branch or a commit. The notes record tip e304c42, last commit 2026-10-28, before the freeze, 226 commits behind `origin/main`, with no drift as of 2026-11-02. A fork "hourly upstream sync" commit exists, and its reach was not checked | Any commit to that branch would silently change the book during the Gate v2 window | Do not patch the frozen path. A read-only daily check comparing the tip to e304c42 alerts without changing treatment. Pinning is an owner decision in Paperclip, and any upgrade is a new version |
| **Possible memorization in pulse-stance v59.** Not proven; no holdout score exists | [L] The prompt holds item IDs including F263, F115 and F283, and literal rules such as "waiting for entry" and "R.I.P. SHORTS" as bearish. Train went 0.809 to 0.882 with holdout blank (2026-10-31 evolve pulse-stance-v1 gemma4-12b). Now records 0.815 as the start and "not trusted". DUS-88 fixed the self-scoring. The 0.815 against 0.809 gap is unexplained. "Shorts dying" normally favors longs, so the rule may encode label noise [J] | Using v59 anywhere would carry an inflated score and possibly bad rules | Do not promote. Audit those labels, score seed against v59 and v59 with item rules stripped on fresh items, and add the guard below in evolve-lab |

## Conclusion

The literature moved this design away from the question "which graph?" and toward "which check or independent source justifies this edge?". Most of what looks like graph value here comes from separating authorship from judgment, and code can do much of that at near zero token cost. That matters on a capped plan, and it means the system gets smarter by improving its evals, labels and failure records, with topology changing last. The most useful thing this lab can produce is its own evidence: shrinkage on few-hundred-item prompt tasks, cross-family review on real diffs, and link expansion on a personal vault are all unmeasured, and this box can measure them cheaply.

The main way this could be wrong is the overnight gap. Every controlled result comes from short tasks, and long runs might reward graph structure through context relief in ways nobody has tested. The night runner's ledger makes that testable, so the adopt list starts with instrumentation. Thresholds below are my proposals, to be pre-registered by the `experimenter` agent before use.

## Ranked adopt, trial and skip list

Every recurring item runs under a systemd timer, GPU use takes `~/.night-shift.lock`, approvals stay in Paperclip, and facts stay in the vault. Grade means evidence for the item, including the problem it addresses.

### Night-shift runner

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Subscription-auth preflight canary and failure classes (auth, usage limit, stall, bad output) | Runner: job health | Docs, [L] | A simulated `--bare` run is caught before the first job in 100% of tests; no night loses more than one job to auth |
| 2 | Adopt | `runs`/`steps` SQLite ledger, commit per step, reset on retry, transition table. Audit existing code first | Runner: execution state | [J], gap in all frameworks | 20 of 20 injected `kill -9` crashes resume with no completed step re-run and a clean tree |
| 3 | Adopt | One writer; order is tests and self-report check, mock check, then fresh differently-trained reviewer with no authorship framing; a fix needs a reproducing test | Runner: gates. Reviewer advises only | [A/B] direction, [B] on false alarms | Over 40 PRs against the prior 40, owner rejection or rework falls by at least 15 points; at most 30% of reviewer findings are false on sampled audit |
| 4 | Adopt | Harness stops: loop detection, explicit stop conditions, session timeout | Runner: termination | [A] taxonomy | Loop or timeout burn under 5% of session minutes; every stop gives a reason in the morning report |
| 5 | Trial | Changed-lines rule-based mutation in stages: report, advisory, blocking | `mutation_report` job | [B] problem; no outcome study | Over 30 diffs, at least 1 real test gap per 10 and under 20% false alarms before blocking |
| 6 | Trial | Sandbox on one task class, stop on repeated denial | Claude Code sandbox | [B] | No writes outside the worktree; success drop at most 10 points against the 18.3 worst published |
| 7 | Trial | Workflows or subagents for read-only fan-out in one job, at most 3-4 agents | Claude Code: in-job fan-out | [A] cap, [C] gain | Over 10 paired research jobs, an owner-graded coverage gain at no more than 2x tokens |
| 8 | Trial, conditional | DBOS, then Burr, replacing the ledger if a pipeline reaches several branches and joins, or the ledger keeps breeding bugs | Library: step recording | Docs, [J] | Passes the same 20-crash test; adds no daemon |
| 9 | Skip | Temporal, Restate, Inngest; Agent Framework; CrewAI; AutoGen; LangGraph unless DBOS and Burr fail | Would overlap systemd and Paperclip, or add no durable value | Docs, [M] | Revisit only if a second host appears |
| 10 | Skip | Role teams, debate, depth above 2, multi-writer swarms | None | [A/B] | Revisit if a paired local eval shows a gain |

### Paperclip queue

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Approval state: create issue, exit, later tick resumes | Paperclip: approvals | [J] | 100% of gated transitions in the ledger carry an issue ID; no process waits on approval |
| 2 | Adopt | Findings reach the queue only with a reproducing test or artifact | Paperclip: owner attention | [B] | At least 70% of agent-filed issues are accepted on sampled review |
| 3 | Skip | LLM approval, engine durable waits | Forbidden by the role map | [L] | Zero approvals outside Paperclip and standing `Decisions.md` entries |

### Vault memory

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Harder eval of 100-200 stratified questions, with a reserved split and wrong-answer judge test | `ai-notes`: retrieval eval | [J], [B] on noise floor | All strata populated; BM25 baseline recorded; judge rejects at least 90% of planted wrong answers |
| 2 | Adopt | `FINDINGS.md` rules: cite run, evidence type, retest date | Vault: lessons | [B] | 100% of new lessons cite a run; a paired trial with and without on held-out workflow tasks shows no loss, or the file is pruned |
| 3 | Adopt | `as_of` in `ai-notes find`, labeled superseded results | `ai-notes`: time queries | [B] need | At least 90% on as-of and superseded-trap strata; no significant loss elsewhere |
| 4 | Trial | One-hop `--expand` to best chunk, excluding `project:` and index links, then rerank | `ai-notes`: retrieval | [B, thin] | Paired win on full-evidence recall@k for multi-note questions, no significant single-note loss, latency under 15 s |
| 5 | Trial | Claims file for changeable facts | Vault: a fact store, fed from existing notes | [B] on stale facts | Partial-supersession questions gain at least 10 points; no fact in two places |
| 6 | Trial, later | Personalized PageRank; local entity extraction on 20 notes | Derived index only | [B] indirect | Runs only after #4 wins; must beat it by a paired test |
| 7 | Skip | Neo4j, Graphiti, Mem0, Zep, Cognee, Letta, GraphRAG, LightRAG, RAPTOR | Would duplicate the vault's fact role | Disputed, [V] | Revisit if #4 and #6 still fail on multi-note questions by at least 10 points |

### Evolve-lab

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Three splits, single confirmation, paired tests, shrinkage in every note, look counter | Evolve-lab: selection | [B], [J] | Every run note reports selection and shrinkage; every adoption's CI lower bound clears zero on an unburned holdout |
| 2 | Adopt | Memorization guard: reject item IDs and copied train n-grams of 3+ words; per-class recall floors and majority baseline | Evolve-lab: candidate filter | [L], [J] | Rejects v59 in replay; no candidate with an item ID reaches selection |
| 3 | Adopt | v59 audit as described above | Evolve-lab: pulse-stance | [L] | Verdict recorded with per-item test; label errors corrected in a new task version |
| 4 | Adopt | Scorer outside writable tree, hash-pinned; no agent labels items judging its own prompt | OS permissions | [B] | Hash check passes on all runs; zero harness diffs in candidates |
| 5 | Trial | GEPA ideas: per-item feedback, Pareto archive, local rollouts, Sonnet reflector capped | Evolve-lab: proposer | [SR] | Pre-registered three-arm test on a fresh split; adopt if holdout CI clears zero; report rollouts per hour |
| 6 | Trial | Trace-to-eval: time-routed items plus a random production sample, owner or Sonnet labels | Evolve-lab: eval set | [C], [V] | New items reproduce real failures; failure-only and random sets reported separately; owner labeling stays under a set weekly limit |
| 7 | Trial, later | Error-type niches in the archive; small fixed topology menu | Evolve-lab | [B], [SR] | Beats single best on holdout with disclosed selection accounting |
| 8 | Skip | DGM, SICA, SIFT, open ADAS or AFlow search; MIPROv2 as default | None | [SR], [B] against | Revisit with a scorer-isolated sandbox and a budget for benchmark tasks |

### Finetune-lab

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Keep gates and pre-registration; finish prereg-001 and prereg-002 as planned | Finetune-lab: adapter training | [L] | Each run ends with a recorded gate result |
| 2 | Adopt | Evolve-lab paired statistics for adapter comparisons | Evolve-lab protocol, reused | [B] | Every claimed gain carries a paired CI on a 200+ item holdout |
| 3 | Trial | Interaction test: base plus tuned prompt, adapter plus seed, adapter plus re-tuned prompt | Evolve-lab prompts, finetune-lab adapters | Weak [SR] | Adopt the simplest arm unless another's CI clears zero |
| 4 | Trial | Q4, Q5 and Q8 on the owner's own tasks within VRAM | Finetune-lab: export choice | Gap | Choose the smallest with non-inferiority at a declared margin, and record tokens per second |
| 5 | Skip | Graph orchestration of the pipeline; speculative decoding via a second server | Would create a second inference owner | [C] | Revisit only if Ollama gains it natively and a one-off test shows at least 1.3x with no quality change |

### Paper-trading arena

Nothing here changes a frozen book, and none of it counts toward Gate v2. Builds need the owner's approval.

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Keep Gate v2 unchanged, with no interim peeks | Gate v2: verdicts | [L] | Reads occur only on 2027-01-21 and 2027-04-15; effect size and CI reported |
| 2 | Adopt, owner decides | Read-only branch tip check and count of `tradingagents_pick` failure days | Arena monitoring | [L] | Any tip other than e304c42 raises an alert the same day; failure days are reported beside the verdict |
| 3 | Trial | `ta_flip_probe_v1`: re-run frozen inputs N times offline | New version: stability | [J] | Rating flip rate on at least 30 decisions, with a declared stability threshold |
| 4 | Trial | `single_llm_budget_v1`: same candidate, same token budget | New version: matched control | [A/B] general, none in trading | Tracks at least 50 decisions; report agreement and the graph's incremental filter value, labeled exploratory |
| 5 | Trial | `ta_shadow_v2` validity gate and deterministic veto log, plus pre-trade probabilities | New version: controls and calibration | [J], thin | Blocks audited with under 10% false blocks; Brier score logged per decision, never read as alpha |
| 6 | Skip | Debate tuning, reflective memory, LLM vetoes without counterfactual, Alpha Arena model picking, upgrading the frozen branch, live money from graph output | None | [B] against, [C] | Revisit after Gate v2's final read |

### Site-foundry

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Deterministic matching for DUS-52, with current leads labeled as a regression test | site-foundry: verification | [V] pattern, [L] problem | "No website" precision reaches at least 95% on labeled leads, from about 47% (30 of 64) |
| 2 | Adopt | CAN-SPAM lint on every draft; owner approves in Paperclip and sends | Lint: compliance check. Paperclip: approval | Legal source | 100% of drafts pass before reaching the owner; legal gaps checked before the first send |
| 3 | Adopt | Lighthouse, axe, link and form checks at both widths | site-foundry: QA | [C] | Every demo has a report; zero critical defects at bundle time |
| 4 | Trial | LLM with schema on ambiguous pairs only, three-sample agreement | `local-delegate` | [C] | Beats rules alone on labeled pairs, with disagreement escalated |
| 5 | Trial | Vision review of screenshots, advisory | site-foundry: QA second pass | Conflicting [C] | At least 1 real issue per 5 demos missed by deterministic checks, at under 30% false findings |
| 6 | Skip | Splink, multi-agent site crew, AI sales tools, reply-rate targets | None | [V] | Judge on booked conversations per 30 approved sends; revisit Splink above several thousand leads |

### Ollama local work across projects

| # | Verdict | Item | Role it owns | Grade | Success criterion |
|---|---|---|---|---|---|
| 1 | Adopt | Check-gated cascade: executed test or three-sample agreement, then escalate, with a nightly budget. No local judge | `local-delegate` | [C] with [B] conflict | In a pre-registered trial, accuracy within 2 points of Claude-only at no more than 25% of hosted sessions |
| 2 | Adopt | Schema on the final step only, then value validation | Existing Ollama callers | Docs, [V] | Zero schema-valid range or cross-field errors in sampled output |
| 3 | Trial | Claude Code metrics to console or Prometheus, Phoenix only on demand; raw bodies kept out of the vault | Transcripts remain the record | Docs | Answers a named question about session use; stays off otherwise |
| 4 | Skip | Langfuse self-host, learned or commercial routers, confidence-threshold cascades | Would add services or weak gates | [C], [B] | Revisit if traces become a recurring need |
