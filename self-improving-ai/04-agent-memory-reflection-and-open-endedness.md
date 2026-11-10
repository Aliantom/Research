<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Agent memory, reflection and open-endedness

> **TL;DR:** Reviews memory and reflection methods (Reflexion, ACE, Voyager, Mem0) and favors ACE-style structured playbooks over rewriting one large summary.
> **Source:** Continuation of the 2026-10-24 handoff; memory, context engineering and open-ended learning primary sources  ·  **Project:** evolve-lab  ·  **Updated:** 2026-10-27

## Mechanisms to borrow

| Method | What persists / how the loop works | Practical interpretation |
|---|---|---|
| Reflexion | Evaluate an attempt, write verbal feedback into episodic memory and try again | Store lessons tied to actual outcomes; no weights need change. [Paper](https://arxiv.org/abs/2303.11366) |
| Self-Refine | Generate an answer, critique it, revise, repeat | Bounded within-task refinement; not automatically durable cross-session learning. [Paper](https://arxiv.org/abs/2303.17651) |
| ExpeL | Accumulate experiences, contrast outcomes, extract insights and retrieve relevant examples | Useful for reusable task lessons, with retrieval and curation overhead. [Paper](https://arxiv.org/abs/2308.10144) |
| CLIN | Update textual causal knowledge and use it to adapt to subsequent tasks | Favor actionable conditional lessons over generic “be careful” advice. [Paper](https://arxiv.org/abs/2310.10134) |
| Agent Workflow Memory | Extract reusable workflows from experiences and use them to guide later action | Store successful tool procedures as versioned skills. [Paper](https://arxiv.org/abs/2409.07429) |
| Dynamic Cheatsheet | Maintain an adaptive memory of useful reasoning and facts at test time | Good model for a bounded task playbook; do not mix evaluation answers back into search. [Paper](https://arxiv.org/abs/2504.07952) |
| ACE | Generator, reflector and curator evolve structured context using localized updates and refinement | Better match for the vault than repeatedly rewriting a giant summary. [Paper](https://arxiv.org/abs/2510.04618) |
| Voyager | Automatic curriculum, executable skill library, iterative code improvement with feedback | Borrow the tested skill library; its Minecraft results are not evidence of business autonomy. [Paper](https://arxiv.org/abs/2305.16291) |
| MemGPT / Letta | Manage limited active context by moving information to/from longer-term memory | A memory controller, not unlimited attention. [MemGPT paper](https://arxiv.org/abs/2310.08560) |
| A-MEM | Form and link structured memory notes, updating their relationships | Potential later layer for semantic cross-task retrieval. [Paper](https://arxiv.org/abs/2502.12110) |
| Mem0 | Extract and update useful memories and retrieve them for later conversations | Infrastructure option; compare against simple file/FTS retrieval before adding a service. [Paper](https://arxiv.org/abs/2504.19413) |

## Turn FINDINGS into evidence-backed playbooks

ACE uses itemized entries with identifiers and helpful/harmful metadata, updated through deltas rather than full-context rewrites. It also refines/deduplicates the growing context. Sources: [§3](https://arxiv.org/html/2510.04618v3). My adaptation preserves the existing append-only FINDINGS log as the evidence record, with a separate machine-owned playbook for active guidance.

Proposed entry schema:

```yaml
id: extract-003
scope: ticker-extract-v2
condition: SEC filing input contains an explicit ticker list
action: prefer the audited structured input over guessing an issuer symbol
evidence: [run-id, dataset-version, variant-id]
status: candidate # machine playbook field, not a Human note status
helpful: 0
harmful: 0
last_checked: 2026-10-24
supersedes: null
```

Those zeroes initialize proposed counters, not owner metrics. Never use the playbook to invent or overwrite owner-side properties. Evidence must include the exact context/scorer version: the same tip may be helpful on filings and wrong on ordinary news.

Proposed nightly cycle:

1. **Reflect:** read only new run summaries and a small, balanced set of train failures. Generate at most three candidate lessons with explicit supporting run IDs.
2. **Validate:** reject lessons supported only by the model's own opinion; use an ablation on development cases to test a lesson when possible. Record contradictions and uncertain labels.
3. **Consolidate:** add or amend specific playbook entries by ID. Keep prior revisions, and record why an entry was superseded. Do not rewrite the FINDINGS history or owner prose.
4. **Propose:** select one low-cost next experiment tied to an unresolved failure. Estimate time from measured runs and enforce limits in the controller.
5. **Review:** morning output shows proposed lessons, evidence, failures, actual work completed and unresolved questions. Keep irreversible actions gated separately.

This is a proposed workflow; only the existing four-attempt local prompt run was configured this session. A general reflector/controller was not deployed.

## Storage decision

My recommendation is **Markdown as the readable source of lessons, SQLite as the experiment index, and FTS before embeddings**. Store full trajectories outside active context and retrieve small relevant slices by task/source/version. Only add embeddings if a measured retrieval test shows FTS misses semantically related lessons. A small local embedding model can be loaded after unloading the task model, avoiding simultaneous VRAM pressure. The design fits the existing vault/data-hub architecture; it is not a claim that any one memory framework is inherently best.

Skills should package a tested procedure with instructions, references and optional code. The open Agent Skills format uses a directory with `SKILL.md` front matter including `name` and `description`. Reuse that interface for interoperability, while retaining this vault's required AGENTS/FINDINGS workflow structure. [Specification](https://agentskills.io/specification).

## Debate and judge limits

Mixture-of-Agents combines multiple models' responses in layers, with reported gains on preference/task benchmarks. It adds inference work; multiple agreeing responses are not independent verification. [Paper](https://arxiv.org/abs/2406.04692).

A bull/bear/judge structure is a useful way to ask for conflicting hypotheses, but does not establish financial accuracy. Use concrete evidence IDs and blinded scoring when testing it. LLM judges exhibit position, verbosity and self-enhancement biases; randomize answer order, control length, calibrate against independent labels/tests and keep the grader stable during a search. [Judge study](https://arxiv.org/abs/2306.05685).

## Open-endedness: generate useful tasks

POET jointly evolves challenges and agents and transfers solutions across environments. OMNI-EPIC adds foundation-model judgments of interestingness and learnability to generate coded environments. AI Scientist v2 connects hypothesis generation, experiments, analysis and paper writing through a research agent/search system. Sources: [POET](https://arxiv.org/abs/1901.01753), [OMNI-EPIC](https://arxiv.org/abs/2405.15568), [AI Scientist v2](https://arxiv.org/abs/2504.08066).

My priority heuristic for overnight experiments is:

`priority = expected_usefulness × uncertainty_reduction × chance_of_finishing / measured_cost`

These factors are scheduling estimates, not objective truths. Require every proposed task to name a user goal, an independent success check, a fixed budget and an artifact it will produce. Include a small diversity slot for a new task type, but keep most GPU time on current bottlenecks. Interestingness is not a replacement for the owner's priorities; About me remains blank, so use only the goals already recorded in the handoff.

## Adopt for Alianto's setup

Keep append-only FINDINGS and add a separate compact active playbook. Use trace IDs and task-scoped retrieval instead of reloading the vault. Limit reflection to observed evidence, store hypotheses as hypotheses, and test changes before promoting them. For unattended execution, enforce network/credential isolation for generated code, read-only evaluators, bounded subprocess trees and outputs, a wall-clock stop, a stop file, checkpoints and a morning report. These are proposed engineering controls; a prompt declaring an agent “safe” does not implement them.
