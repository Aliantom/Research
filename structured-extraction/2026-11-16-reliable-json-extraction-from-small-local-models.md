<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Reliable JSON extraction from small local models

> **TL;DR:** Constrained decoding fixes JSON validity but can cost accuracy on small models; best-supported recipe: free-text answer first, then a constrained packaging call, schema in prompt, validator, one retry
> **Source:** research-lane weekly run 2026-11-16; question: best-evidenced way to get reliable JSON extraction from a 4-12B local model (constrained decoding vs retry-with-validation vs verifier)  ·  **Project:** schema-correction  ·  **Updated:** 2026-11-16

**Question.** For a 4-12B model on a single RTX 3080 10 GB / 16 GB RAM workstation, served through Ollama or llama.cpp, what gets reliable structured (JSON) extraction: grammar or schema-constrained decoding, retry-with-validation, or a verifier pass? What does each cost in accuracy and latency?

## Bottom line

1. **Use constrained decoding for validity, but do not make it the only stage, and let the model reason before the constraint bites.** (try, first)
   - Why: hard schema constraints took sub-3B models from 61.5% to 100% schema-valid in a 15,000-generation study, yet answer accuracy did not improve and fell sharply on a tool-call task (91.5% to 48.0% executable accuracy); packaging the same answer in a late, second constrained step restored 91.5%. VERIFIED (Constraint Tax, below). Small models are the regime the question cares about, but the evidence is on sub-3B models and one 3B check, so for 4-12B this is REASONED, not measured.
   - First step: arm (c) in the `next_step`: free-text answer, then a constrained packaging call.
2. **Always put the schema in the prompt as well as in the constraint, and keep temperature low.** (try, cheap) Ollama's own docs recommend passing the schema as text in the prompt "to ground the model's response" and lowering temperature (VERIFIED, docs read 2026-11-16). Separately, the constraint-only arm in the study above lost accuracy, consistent with the constraint carrying no semantic information the model can use.
3. **Validate with a schema validator and allow one repair retry, but measure the retry rate and check repaired values against the source.** (try as a safety net) The only evidence I found for retry-with-error-feedback is practitioner blogs (anecdotal; one claims 60% to over 95% retry success; another warns repair can invent values to satisfy a validator). No peer-reviewed or code-backed evaluation of retry loops turned up. ASSUMED until measured; arm (a) measures it.
4. **A separate verifier or "judge" pass for extraction: no published evidence found** that it beats validator plus source-grounded checks. Skip until a field-level check (does the extracted string occur in the source text?) is shown to be insufficient.

## Candidates table

| Name | What it is | Evidence (label, source, date) | Fit on this box | Verdict |
|---|---|---|---|---|
| Schema/grammar-constrained decoding via Ollama `format` or llama.cpp grammar | Token mask forces output to match a JSON schema | Benchmark with code: JSONSchemaBench (preprint, 2025; benchmark repo pushed 2026-09-28). VERIFIED | Free; already in the stack. Per-token cost depends on engine (see below) | try (as the packaging stage) |
| llguidance backend for llama.cpp | Rust constrained-decoding engine, optional build flag in llama.cpp | llama.cpp docs: about 50 microseconds average CPU time per token mask on JSON Schema Bench with a 128k-token vocabulary; engine repo pushed 2026-11-11, MIT, 85 open issues. VERIFIED (docs read; the speed figure is the maintainers' own) | Needs a Rust toolchain at build time; existing GBNF grammars need conversion; whether Ollama uses it was NOT verified | watch (try only if grammar sampling shows a latency problem) |
| Constrain late: reason free, package constrained | Model answers in free text first; second call only formats | Constraint Tax (single-author preprint, 2026-05, no code link stated). VERIFIED numbers, small synthetic tasks | Two calls per item; roughly doubles calls but the packaging call is short | try |
| Schema in prompt plus validator plus one repair retry | Parse, validate, feed the error back once | Blogs only (anecdotal) | Free; adds latency only on failures | try, measure retry rate |
| Grammar-aligned decoding (ASAp) | Sampling that corrects the distribution distortion that plain grammar masking causes | NeurIPS 2024; evaluated on a 7B model, but on code-synthesis and parsing tasks, not extraction; authors call slow convergence the key limitation; code repo last pushed 2025-02-10, 29 stars. VERIFIED | Research code; not a practical serving path | skip for now |
| SLOT: small fine-tuned model converts free text to schema | Post-processing model, LoRA-trained | Preprint 2025-05, also reported at EMNLP 2025 Industry (only the abstract page listing was read). Reports 99.5% schema accuracy and 94.0% content similarity with a fine-tuned 7B plus constrained decoding; benchmark release pending, no code or data stated. VERIFIED abstract only | Would need a training run | watch (idea behind arm (c), but needs data and a training run) |

## What each approach costs

- **Accuracy.** JSONSchemaBench Table 8 (Llama-3.1-8B-Instruct, quality experiments): constrained decoding was about level with or a little above unconstrained on three reasoning tasks, for example GSM8K 80.1% unconstrained vs 82.4% (llama.cpp grammar) and 83.7% (XGrammar); Last Letters 50.7% vs 52.0% and 51.2%. VERIFIED. This is the opposite direction to the Constraint Tax result, so the effect depends on the task, the prompt, and whether the model gets room to reason; do not treat either as general.
- **Validity.** Without constraints, schema compliance on harder real-world schemas was poor: for the "GitHub Hard" set, a 1B model's unconstrained compliance was 0.13, against 0.63-0.69 for the best constrained engines (JSONSchemaBench Table 4, Llama-3.2-1B-Instruct). Coverage varies widely by engine; some engines produced very little valid output on hard schemas (Outlines 0.06). Pick the engine on your own schemas, not on a leaderboard. VERIFIED, 1B model, so treat as a lower bound on difficulty.
- **Latency.** On the same benchmark's efficiency study (8B at Q8, llama.cpp backend), per-token time was 15.40 ms unconstrained vs 29.98 ms with llama.cpp grammar sampling, plus 0.05 s grammar compile time; Guidance was 6.37 ms. The paper's own total-time table shows constrained generation can be faster overall when it stops sooner. VERIFIED, hardware not stated in the text I read. An older llama.cpp issue (Llama-3-8B, closed 2024-05-30, no resolution described) reported grammar sampling at 85 ms per token vs 1.66 ms; I could not tell what changed. On the Constraint Tax calendar task, a hard schema cost only +0.06 s per item on average (1.63 s vs 1.69 s). The overhead therefore depends heavily on engine, grammar and version; measure it on the box.
- **Reasoning-before-answer.** The "Let Me Speak Freely" preprint (2024) reports reasoning declines under format restriction. A rebuttal from a constrained-decoding vendor (not neutral) says the paper compared mismatched prompts and used a weak parser, and reports structured at or above unstructured on the same tasks with Llama-3-8B-Instruct (GSM8K 0.77 vs 0.78, Last Letter 0.73 vs 0.77, Shuffle Object 0.41 vs 0.44). The two sources disagree and I could not check the original paper's per-model numbers (the abstract page had none). Practical reading: compare arms under identical prompts on your own tasks.

## Adjacent ideas

- **Field order is a prompt.** In a constrained schema the model writes fields in declared order, so a rationale or "evidence" field placed before the answer field acts as a scratchpad; an answer-first order cannot. The Constraint Tax expanded study supports this direction (rationale-then-answer schema 36.5% vs answer-only 26.8% executable accuracy, 20 examples per family, so design evidence only). One practitioner source also reported a drop from 0.804 to 0.650 when field order was changed against a fine-tune; I could not trace it to a primary source, so ASSUMED.
- **Extraction-specific cheap check:** require each extracted string field to appear in (or be derivable from) the source text; fail otherwise. This catches repair-pass fabrication without an LLM judge. REASONED, not measured.
- **Wrong-but-valid outputs rise with constraints.** In the main study the share of outputs that were valid but wrong rose from 49.5% to 88.9% under a hard schema, so schema validity must never be reported as accuracy.
- Report validity, accuracy and latency separately, and keep the item as the unit for paired tests.

## Rejected

- **Trusting blog overhead figures** (for example "10-15% throughput loss for GBNF"): no benchmark or code behind them, and they conflict with the primary numbers above.
- **XGrammar as an Ollama or llama.cpp option**: search results suggested it, but I found no evidence either uses it; the JSONSchemaBench XGrammar rows were produced on other serving setups. Do not plan around it.
- **A GenSIE 2026 workshop paper** on structured extraction surfaced in search; the PDF could not be read through the fetch tool, so it is not cited.
- **Treating Ollama's cloud endpoint as an option:** its docs say structured outputs are not supported there, and it is outside the local-only constraint anyway.

## Sources (all opened 2026-11-16 unless noted)

- JSONSchemaBench (Geng et al., arXiv 2501.10868, v3 HTML; read to about 100k of 111k characters): https://arxiv.org/html/2501.10868v3
- JSONSchemaBench repo, GitHub API: https://api.github.com/repos/guidance-ai/jsonschemabench (pushed 2026-09-28, not archived, no license listed, 3 open issues)
- The Constraint Tax (arXiv 2605.26128, HTML v1; single-author preprint): https://arxiv.org/html/2605.26128v1
- Let Me Speak Freely? (arXiv 2408.02442, abstract page only): https://arxiv.org/abs/2408.02442
- Say What You Mean (rebuttal, constrained-decoding vendor): https://blog.dottxt.ai/say-what-you-mean.html
- Grammar-Aligned Decoding (NeurIPS 2024, arXiv 2405.21047): https://arxiv.org/html/2405.21047 and abstract https://arxiv.org/abs/2405.21047
- GAD code repo, GitHub API: https://api.github.com/repos/ebmoon/transformers-GAD (pushed 2025-02-10, MIT, 29 stars)
- SLOT (arXiv 2505.04016, abstract page): https://arxiv.org/abs/2505.04016
- Ollama structured outputs docs: https://docs.ollama.com/capabilities/structured-outputs
- llama.cpp llguidance doc: https://raw.githubusercontent.com/ggml-org/llama.cpp/master/docs/llguidance.md
- llama.cpp repo, GitHub API: https://api.github.com/repos/ggml-org/llama.cpp (pushed 2026-11-17 UTC, MIT, not archived, 2,622 open issues)
- llama.cpp grammar slowdown issue 7554 (2024): https://api.github.com/repos/ggml-org/llama.cpp/issues/7554
- llguidance repo, GitHub API: https://api.github.com/repos/guidance-ai/llguidance (pushed 2026-11-11, MIT, 85 open issues)
