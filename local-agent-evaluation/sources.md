<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Sources

> **TL;DR:** Sources for local agent evaluation: Anthropic evals guidance, a holdout reuse paper, and a 2026-10-24 Gemma and Qwen sampler audit.
> **Source:** Primary research consulted for local agent workflow experiments  ·  **Project:** AI workstation  ·  **Updated:** 2026-10-27

- [Anthropic: Demystifying evals for AI agents, January 9, 2026](https://www.anthropic.com/research/demystifying-evals-for-ai-agents). Distinguishes tasks, repeated trials, transcripts and real outcomes; recommends checking graders and inspecting traces. Application to this lab: deterministic outcome checks and successful tool retrieval, rather than self-reported success.
- [Dwork et al.: Generalization in Adaptive Data Analysis and Holdout Reuse, 2015](https://arxiv.org/abs/1506.02629). Explains how adaptive reuse can overfit a holdout. This lab uses one-shot reservations and fresh banks; it does not implement the paper's formal differential-privacy algorithm or claim its guarantees.

Interpretation and run evidence belong in the dated output and FINDINGS, not in the original papers. Research improves the measurement process; it does not establish unlimited model gains.

## 2026-10-24 — sampler audit

- [Official Gemma best practices](https://gemma.ai/get-started/best-practices/): temperature 1.0, top-p .95, top-k 64. Existing Gemma workbench matches these sampling defaults; temperature .2 is an experimental challenger, not an upstream recommendation.
- [Qwen3.5 9B author model card](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/README.md): mode/task-dependent settings; precise thinking-mode coding uses temperature .6 and presence penalty 0, unlike our .1/1.5 workbench. Non-thinking general guidance uses .7/.8/20/1.5. The page has inconsistent non-thinking reasoning values between sections; avoid silently choosing one.
- Interpretation: compare full presets across models, and isolate one factor within a model. Current 2K generation cap intentionally measures bounded interactive work, not maximum reasoning capability; upstream Qwen suggests much larger outputs. Future longer-budget tests must be a separate declared condition. Do not promote untested manufacturer settings automatically.
