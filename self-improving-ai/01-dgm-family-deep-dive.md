<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# DGM family deep dive

> **TL;DR:** Compares Gödel Machine, DGM, HGM, SICA and related self-improving agent methods using authors' reported results, none reproduced locally.
> **Source:** Continuation of the 2026-10-24 handoff; primary papers and repositories checked by Codex  ·  **Project:** evolve-lab  ·  **Updated:** 2026-10-27

Scope: methods and numbers below are authors' reported results, not reproductions. Recommendations are my proposed design for Alianto. Unchecked implementation details and dollar costs are marked explicitly rather than inferred from benchmark scores.

## What each method actually changes

| Method | Loop, selection and evaluation | Evidence and limitation |
|---|---|---|
| Gödel Machine | Proof search over self-rewrites; execute when a proof establishes greater expected utility than continuing proof search, relative to the encoded axioms | A theoretical construction, not an implementable guarantee for our noisy market/news benchmark. [Paper](https://arxiv.org/abs/cs/0309048) |
| DGM | Diagnose failures, let a parent agent edit its own code, test the child, retain functioning self-editors in an archive, sample parents using performance plus a child-count bonus | Reports SWE-bench 20→50% and Polyglot 14.2→30.7%; not evidence that a small local model attains these numbers. [Paper](https://arxiv.org/abs/2505.22954) |
| HGM | Use evidence from a parent's whole descendant clade; separately decide whether to evaluate or expand; choose nodes using Thompson sampling | Reports 56.7% on SWE-Verified-60 vs DGM 53.3%, with 517 vs 1231 allocated CPU-hours in its controlled comparison. Those are allocated hours, not desktop wall time. [Method and Table 2](https://arxiv.org/html/2510.21614v3) |
| DGM-H / Hyperagents | An editable program contains both task-solving and improvement procedures; archive and evaluate changes to either | Extends beyond coding; reports cross-domain accumulation of improvements to the improvement process. This does not establish unlimited or accelerating recursive improvement. [Paper](https://arxiv.org/abs/2603.19461) |
| SICA | Evaluate an agent, archive its results, have it edit its own code, repeat; favor a strong current agent rather than DGM's exploratory tree selection | Reports 17→53% on a random SWE-bench Verified subset; distinct benchmark setup from DGM. [Paper](https://arxiv.org/abs/2504.15228), [implementation loop](https://github.com/MaximeRobeyns/self_improving_coding_agent) |
| Gödel Agent | Give an LLM introspection/editing tools and a high-level objective; let it revise running agent logic | The empirical work reports gains on reasoning/agent tasks; it supplies no universal proof of improvement. Exact run cost for our intended setup: **unverified**. [Paper](https://arxiv.org/abs/2410.04444) |
| STOP | An improver samples program changes and selects by utility; invoke that improver on its own implementation | Demonstrates improving a scaffold around a frozen LM, not weight-level improvement; also investigates sandbox bypasses. [Paper](https://arxiv.org/abs/2310.02304) |
| ADAS | A meta-agent writes agent programs informed by an archive, executes evaluations, adds discoveries and repeats | Searches agent designs; reported transfers across tasks/models do not imply every discovered design generalizes. [Paper](https://arxiv.org/abs/2408.08435) |

## Selection formulas worth distinguishing

**DGM:** among eligible nonperfect agents, let accuracy be `a_i`, functioning-child count `n_i`. Its published sampling rule is

`w_i = sigmoid(10(a_i − 0.5)) / (1 + n_i)`, then `p_i = w_i / Σ_j w_j`.

Children must retain code-editing functionality; a lower-performing child can remain a stepping stone. A SWE-bench run was estimated at about **$22,000**, not a subscription-sized nightly job. [Appendices C.2 and E.1](https://arxiv.org/html/2505.22954v3).

**HGM:** with clade success/failure totals `S_C,F_C`, its estimator is `CMP_hat = S_C/(S_C+F_C)`. Expansion samples each node's Beta belief with parameters `τ(1+S_C), τ(1+F_C)` and chooses the largest draw. Evaluation uses the individual node's counts instead. Expand when `N^α ≥ |tree|`; experiments use `α=.6`, `τ=B/b`. Final selection uses a specified Beta posterior quantile. True CMP concerns expected *future* best clade utility; the pooled estimator is not simply the best existing descendant. [§3.2–3.3](https://arxiv.org/html/2510.21614v3).

**Current local code:** `pick_parent` exploits the best train score with probability .7, otherwise softmax-samples the maximum observed score in each clade. This is an inspectable heuristic, not HGM's posterior/scheduling algorithm. It uses graded scores, whereas the paper's success/failure formulation uses test outcomes. Calling it faithful HGM would be inaccurate. Source: local `src/evolve/loop.py` and `archive.py` inspected this session.

**My proposed small implementation:** keep this heuristic as a baseline, add HGM as an optional strategy only on binary code-test tasks, count distinct test outcomes and repeats separately, and compare the strategies under the same evaluation budget. Do not interpret highly correlated repeated executions of the same deterministic cases as independent evidence. For graded extraction, either define a meaningful pass threshold before searching or use a graded-outcome model and label it an adaptation.

## Evaluator-first and meta-improvement

VeriEvolve constructs challenge states and executable evaluators, freezes the evaluator within a search round, and refines it between rounds with counterfactual cases. It reports 113/122 agreement on held-out states and an external-success gain from 6/30 to 18/30 for one executor. This is evidence for calibrating the scorer independently, not permission to let a candidate rewrite its grading rules. [Paper](https://arxiv.org/abs/2610.29005).

The RSI survey separates deployment adaptation, policy training, evaluator work and automated research, and emphasizes how signal reliability constrains demonstrated gains. It is a taxonomy, not a recipe proving inevitable improvement. [Survey](https://arxiv.org/abs/2607.07663).

Hyperagents' appendix reports roughly 33M modification tokens over 100 iterations, excluding evaluation. Its displayed `33M + .506M × 100 ≈ 88.6M` contains an arithmetic inconsistency: those terms sum to **83.6M**. Budget using measured calls and task costs rather than copying the total. [Appendix D.2](https://arxiv.org/html/2603.19461v1).

## Code, licenses and cost boundaries

| Implementation | Checked repository license / reuse boundary |
|---|---|
| [DGM](https://github.com/jennyzzt/dgm) | Apache-2.0 |
| [HGM](https://github.com/metauto-ai/HGM) | Apache-2.0 |
| [SICA](https://github.com/MaximeRobeyns/self_improving_coding_agent) | MIT |
| [Gödel Agent](https://github.com/Arvid-pku/Godel_Agent) | MIT |
| [STOP](https://github.com/microsoft/stop) | MIT code; repository states separate documentation/data terms |
| [ADAS](https://github.com/ShengranHu/ADAS) | Apache-2.0 |
| [HyperAgents](https://github.com/facebookresearch/HyperAgents) | Has `LICENSE.md`; exact terms **unverified** in this pass; read it before copying code |

Comparable cost per useful improvement for HGM, SICA, Gödel Agent, STOP and ADAS on our local setup is **unverified**. Paper results use different models, evaluation workloads and budgets. Reusing an algorithmic idea in a small measured loop is more practical than reproducing their headline experiment.

## Adopt for Alianto's setup

1. Freeze and hash task inputs, scorer and independent test harness before a search. Fix mislabeled examples in an explicit new dataset version and re-score comparable variants. Never count a scorer change as an agent gain.
2. Store candidate prompt, scaffold configuration, tool definitions, code diff, parent, model digest, evaluator hash, per-case result, token count and wall time. Existing SQLite lineage is the foundation.
3. First expand beyond prompts into **retrieval settings, context packing, retry limits, patch format and small parsing functions**. Keep the nightly controller, quotas, mounts and credential handling outside the editable candidate.
4. For extraction, start with four proposals × the existing 150-case train split. For code, begin with 20 inexpensive test cases and promote survivors to the full development suite. These are proposed limits, not measured GPU capacity. Use actual timings to adjust; do not run a full SWE-bench search overnight.
5. Require compile/import smoke checks, independent tests and a valid self-edit operation before a code variant becomes an expandable parent. Keep failed artifacts for diagnosis, but do not execute them as parents.
6. Evaluate gains per total GPU-minute and hosted token, not per generation. Use an untouched confirmation set after selecting on development results; refresh future-facing market tests chronologically.
7. Protect against objective hacking with a separately mounted read-only evaluator, no answer-key files in candidate containers, no credentials/network in generated-code execution, and externally enforced time/output limits. Prompt instructions alone are insufficient isolation.

My selection: DGM-style archive first, GEPA-style feedback second, HGM as a measured optional selector, and editable meta-code only after these basics are reliable. This is a staged engineering recommendation, not a demonstrated result of the papers.
