<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Prompt and program evolution

> **TL;DR:** Surveys prompt and program evolution methods (FunSearch, AlphaEvolve, OpenEvolve, OPRO) that work around a frozen local model, with no common leaderboard.
> **Source:** Continuation of the 2026-10-24 handoff; prompt/program optimization primary sources  ·  **Project:** evolve-lab  ·  **Updated:** 2026-10-27

## Methods and what they buy

These mechanisms can operate around a frozen local model. Results from different papers are not a common leaderboard.

| Method | Proposal and selection mechanism | Fit / evidence |
|---|---|---|
| FunSearch | Sample program variants, execute a scoring function, retain good programs in island populations and sample them as future context | Best when validity and quality are executable. [Reference implementation](https://github.com/google-deepmind/funsearch) |
| AlphaEvolve | LLM-generated code modifications, automated evaluators and a population database | Scientific/algorithmic discovery evidence, not a general guarantee for business or trading rewards. [Paper](https://arxiv.org/abs/2506.13131) |
| OpenEvolve | Open implementation with diff-based program evolution, islands and archive policies | OpenAI-compatible model endpoints and configurable selection; Apache-2.0. Existing integration is preferable to duplicating a whole code-search engine. [Repository](https://github.com/algorithmicsuperintelligence/openevolve), [configuration](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/configs/default_config.yaml) |
| ShinkaEvolve | Parent sampling, novelty rejection and bandit selection across proposing LMs | Reports 150 samples for a circle-packing result; that efficiency is specific to its problem and setup. Apache-2.0. [Paper](https://arxiv.org/abs/2509.19349), [authors' writeup](https://sakana.ai/shinka-evolve/) |
| ELM / OpenELM | Use a code LM as the mutation operator in evolutionary search | Useful precursor for semantic rather than character-level mutations. [Paper](https://arxiv.org/abs/2206.08896), [code](https://github.com/CarperAI/OpenELM) |
| Promptbreeder | Co-evolve task prompts and the mutation prompts that generate them | Attractive later for meta-search; creates another editable layer and search budget. [Paper](https://arxiv.org/abs/2309.16797) |
| OPRO | Put previous candidate solutions and their scores in a meta-prompt; ask the LM for better candidates | Simple baseline, but scalar score history can hide which behavior broke. [Paper](https://arxiv.org/abs/2309.03409) |
| APE | Infer candidate instructions from examples, evaluate, select and refine | Good initialization baseline. [Paper](https://arxiv.org/abs/2211.01910) |
| EvoPrompt | Use LLMs to implement evolutionary prompt operators such as mutation/crossover and select by task fitness | A straightforward population baseline. [Paper](https://arxiv.org/abs/2309.08532) |
| DSPy MIPROv2 | Bootstrap demonstrations, propose instructions, search instruction/demo combinations with Bayesian optimization | Best candidate when few-shot examples are a large part of the task. [DSPy optimizer guide](https://dspy.ai/3.4.1/diving-deeper/choosing-an-optimizer/) |
| GEPA | Reflect on trajectories and feedback; mutate prompts, retain complementary candidates using per-instance performance and merge useful lessons | Reports fewer rollouts than GRPO on its tested tasks; the comparison is not a hardware-independent claim. MIT standalone implementation. [Paper](https://arxiv.org/abs/2507.19457), [code](https://github.com/gepa-ai/gepa) |
| TextGrad | Propagate natural-language feedback through a computation graph to update text parameters | Useful for attributing failures across pipeline stages; feedback quality remains the bottleneck. [Paper](https://arxiv.org/abs/2406.07496) |
| Trace / OptoPrime | Capture execution dependencies and optimize marked program nodes using rich feedback | Useful after the pipeline has multiple mutable stages. [Authors' project](https://microsoft.github.io/Trace/), [paper](https://arxiv.org/abs/2406.16218) |
| PromptWizard | Task-aware feedback-driven prompt and example refinement | Another packaged prompt optimizer; benchmark it before adding a second framework. [Microsoft repository](https://github.com/microsoft/PromptWizard) |

## Per-example selection: adopt the useful part of GEPA

Proposed `evolve-lab` design: represent candidate `v` by development score vector `s(v)=(s_1,…,s_n)` and measured cost. Candidate `u` dominates `v` if it is at least as good on every objective and strictly better on one. Preserve complementary specialists rather than retaining only the largest mean. This is my proposed adaptation of GEPA's complementary-candidate idea, not a claim that every nondominated candidate is useful. [GEPA](https://arxiv.org/abs/2507.19457).

With many noisy objectives, almost everything can become nondominated. Bound the archive, group examples into stable source/event slices, track mean score as well, and require a minimum number of useful wins. Compare this policy against the existing mean-score baseline using the **same number of metric calls**. Keep latency and invalid output rate as additional promotion gates. Do not let an extraction sentiment gain hide ticker losses.

The archive already stores per-example scores, so the first implementation can avoid an external optimizer dependency. Add an ablation: existing selection versus complementary selection, fixed seeds, equal evaluation budgets and an untouched confirmation set. A full DSPy migration is justified only if modular pipelines and joint demo optimization save more work than migration costs.

DSPy has local-model support through provider interfaces; verify its versioned LM configuration and chat template against the installed Ollama model before comparison. A local reflection model has no hosted token bill but still has inference cost and may propose weaker edits. [DSPy documentation entry](https://dspy.ai/), [optimizer interfaces](https://dspy.ai/3.4.1/diving-deeper/choosing-an-optimizer/).

## Demos, edit control and diversity

My proposed genotype is `{instruction, demo_ids, retrieval_config, tool_policy}`. Evolve one component at a time initially. Demonstrations come only from the optimization split; store IDs rather than repeatedly copying text. Dedupe related news/filings across splits before creating demo sets. Reserve separate search/development/final data as the corpus grows. Joint instruction/demo search follows the MIPROv2 design motivation. [DSPy optimizer guide](https://dspy.ai/3.4.1/diving-deeper/choosing-an-optimizer/).

Use two small logical islands on one GPU: one for concise rules, another for a tiny demo set. Alternate them sequentially; migration means sharing a useful candidate, not loading multiple models simultaneously. OpenEvolve implements island populations and migration; its defaults are reference configuration, not an appropriate starting budget for this PC. [Configuration](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/configs/default_config.yaml).

For quality-diversity/MAP-Elites, bins could describe prompt length and tool-call count, keeping the best valid candidate per bin. These descriptors are my design choice. Diversity should expose useful accuracy/cost tradeoffs; arbitrary novelty without independent task success is not a product improvement.

Minimal-edit proposal brief now asks for changes to at most two failure-related rules while preserving structure. That is a request to the proposer, not a hard mathematical guarantee. Next enforce patches mechanically: return bounded SEARCH/REPLACE blocks, verify exact old-text matches, cap changed tokens, and reject wholesale replacement. Record both rejected and accepted changes to compare proposal efficiency. Retain an occasional separately labeled broad rewrite experiment so minimal edits do not permanently restrict search.

## Evolving code

Use OpenEvolve or ShinkaEvolve for an isolated **pure function** first: ticker normalization, deduplication or business-lead scoring with audited labels. Candidate code receives only its inputs; a separate runner executes it with fixed resources. Score correctness before runtime. Parsing speed is only valuable after correctness. Trading-rule search must use chronological development folds and account for every attempted variant, as detailed in [05 Applying it - trading, coding, money](05-applying-it-trading-coding-money.md).

My suggested first code task is a parser with adversarial symbols, malformed payloads and known normalization requirements. Do not let the mutable function rewrite the tests, import credentials or contact services. After this works, evolve a patch application/tool-retry scaffold on small code-repair tasks.

## Adopt for Alianto's setup

Keep `evolve-lab` as the experiment ledger and controller. Add per-component feedback and bounded edits before adding new frameworks. Run local proposals at night and use hosted review on a small number of informative failures. Adopt demo evolution next, then compare two small islands against the existing single population. Evaluate OpenEvolve/ShinkaEvolve in a separate code-task adapter only after the independent code scorer exists. The useful snowball is an expanding library of measured tasks and retained improvements; extra population complexity alone is not evidence of progress.
