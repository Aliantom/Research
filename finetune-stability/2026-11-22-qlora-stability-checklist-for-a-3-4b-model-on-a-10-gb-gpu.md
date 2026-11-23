<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# QLoRA stability checklist for a 3-4B model on a 10 GB GPU

> **TL;DR:** Best-supported QLoRA practice: LoRA on all linear layers, rank 16-64, sweep LR (1e-4 to 2e-4, lower at high rank), small clean data, 3+ seeds with paired tests; early-stopping evidence is thin.
> **Source:** research-lane weekly run 2026-11-22; question: data-quality and training-stability practices for QLoRA on a 3-4B base model on one 10 GB GPU  ·  **Project:** evolve-lab  ·  **Updated:** 2026-11-23

Question: for a 3-4B base model fine-tuned with QLoRA on a single 10 GB GPU, which data-quality and training-stability practices have the strongest published support? Useful here means: it changes a decision in a pre-registered fine-tune ladder, and it costs no more than a few extra short runs on a single RTX 3080 10 GB / 16 GB RAM workstation.

Scope warning: almost all strong evidence is from 7B+ models, or from pretraining. No study I opened tests exactly "3-4B, 4-bit base, QLoRA, small data". Everything below is transfer by analogy unless stated.

## 1. Bottom line

1. **Apply LoRA to all linear layers; do not spend runs on rank.** (VERIFIED, two independent sources.) The QLoRA paper's rank sweep (r from 8 to 256, 3 seeds per configuration) found final performance unrelated to r when LoRA is on all layers, and attention-only/query-value-only did not match full fine-tuning. "LoRA Without Regret" and "LoRA Learns Less and Forgets Less" both find attention-only LoRA underperforms MLP or all-layer LoRA, with most gains coming from MLP modules. First step: fix r at 32 or 64 with all linear layers targeted and treat rank as settled for the first ladder rungs. Caveat: "LoRA Learns Less" saw HumanEval keep rising with rank (r=16: 0.358, r=64: 0.417, r=256: 0.498) on a 7B model with about 100K examples of code, so rank matters for large, hard datasets and not for small ones (REASONED: the Thinking Machines capacity argument says rank only binds when the dataset carries more information than the adapter holds, which small datasets do not).
2. **Treat learning rate as the one knob worth a sweep, and make instability a recorded stop condition.** (VERIFIED.) "LoRA Learns Less" reports LoRA best rates around 1e-4 to 5e-4 (about 10x the full fine-tuning rate), recommends sweeping 1e-5 to 5e-4 and picking the highest value that trains stably, and observed "instabilities/loss spikes" at 2e-4 with r=256 (so it used 1e-4 there). QLoRA used 2e-4 (batch 16) for 7B/13B and 1e-4 for 33B/65B. First step: a three-point grid (about 5e-5, 1e-4, 2e-4) at one fixed rank, one seed each, then the winner with 3 seeds. A grid point counts as unstable if training loss shows a sudden jump or the eval score collapses; log that, do not silently drop it.
3. **Compare runs with paired tests over several seeds, not single scores on a small eval set.** (VERIFIED for seed variance; REASONED for the arithmetic.) A seed study (10 seeds, GLUE/SuperGLUE, Llama3.2-3B with LoRA) found accuracy variance across seeds from 0.09 to 5.17 depending on task, and that two runs with the same accuracy can agree on only a fraction of individual predictions. Arithmetic: on a 100-item set at 50% accuracy the standard error from item sampling alone is 5 points; at 200 items it is about 3.5 points, so a 95% interval is roughly +/-7. Differences under that are noise unless the comparison is paired over the same items. First step: 3 or more seeds for any claimed gain, report per-seed scores, and use a paired test on per-item correctness.
4. **Prefer a small, clean, suitable training set over a large noisy one, but do not filter aggressively.** (VERIFIED, with scope limits.) QLoRA Appendix B.4: going from 50k to 150k examples and 1 to 3 epochs moved 5-shot MMLU by about 0.0-0.5 points, while swapping the dataset moved it 1.5-8.0 points; a 9k-example set beat a 450k subsample on chatbot quality. LIMA (1,000 curated examples on a 65B model) and AlpaGasus (about 9k of 52k Alpaca examples kept by an LLM grader) point the same way. Over-filtering shrinks the pool and is an untested risk here (REASONED, no source opened). None of these use a 3-4B model, and AlpaGasus and LIMA are judged by GPT-4 or humans on chat quality, not on task accuracy.

## 2. Practices by topic, with evidence strength

| Practice | Evidence | Strength | Notes for this box |
|---|---|---|---|
| LoRA on all linear layers | QLoRA ablation; Learns-Less Fig. 7; Thinking Machines | VERIFIED, peer-reviewed (TMLR) plus a lab blog with experiments | Adapter memory at r=32-64 is small next to a 4-bit 3-4B base; exact peak VRAM is ASSUMED, check with a smoke run |
| Rank barely matters on small data | QLoRA Fig. 4 (3 seeds); Thinking Machines capacity argument | VERIFIED for 7B+; REASONED for 3-4B | Rank only matters when data is large and hard |
| LR about 10x full fine-tuning; sweep 1e-5 to 5e-4 | Learns-Less Sec. 4.7; Thinking Machines (fitted multiplier about 9.8, about 15x for runs under 100 steps, anecdotal) | VERIFIED | Short runs (tens of steps) may want a higher LR; unverified beyond the blog's anecdote |
| Lower LR when rank is high | Learns-Less: 2e-4 spiked at r=256, 1e-4 stable | VERIFIED, one setup | Thinking Machines says the optimal LR is within 2x from r=4 to r=512 with the 1/r scaling; the two disagree in emphasis, see section 3 |
| LoRA alpha convention | Learns-Less: alpha = 2r, important at high rank; QLoRA: fixed alpha=16 with r=64 | VERIFIED but conventions differ | Record the alpha convention in the pre-registration; comparing LRs across conventions is meaningless |
| Large batches hurt LoRA more than full fine-tuning | Thinking Machines | VERIFIED (blog, experiments) | Favors small effective batch on this box anyway |
| LoRA dropout 0.05-0.1 | QLoRA: 0.1 up to 13B, 0.05 for larger; dropout helped 7B/13B, not 33B/65B | VERIFIED | Default 0.05-0.1 is defensible for a 3-4B model (REASONED by size trend) |
| Gradient clipping and warmup against spikes | Search-snippet reports (pretraining papers on clipping and warmup; not opened by me) | The one stability paper I opened studies an 830M model with layer-norm fixes and does not test warmup or clipping | ASSUMED | Treat clipping at 1.0 and a short warmup as cheap defaults, ASSUMED to transfer to LoRA fine-tuning; no verified source |
| Stop on downstream metric, not only validation loss | Search snippets only; the one agent-tuning paper I opened did not state the claim on its abstract page | ASSUMED | See open questions; do not cite as established |
| Several seeds, paired tests | Seed-variance study (arXiv 2503.07329); benchmark-variance study (arXiv 2406.10229) | VERIFIED (preprints) | Authors call 5-10 seeds sufficient for variance estimates; 3 is the practical floor here |

## 3. Where sources disagree or are thin

- **Rank and learning rate.** Learns-Less lowered the LR at r=256 after loss spikes; Thinking Machines says the 1/r scaling makes the optimal LR nearly rank-independent. These need not conflict (different alpha conventions, a 100K-example code set versus tens of thousands), but nobody has shown which holds for a 3-4B QLoRA run. A 2026 preprint reportedly finds the relationship depends on initialization and scaling choices (seen only in a search snippet; not opened, so not relied on).
- **Early stopping.** I found no controlled study of validation-loss early stopping versus a downstream metric for small-model SFT. The NER fine-tuning paper I opened only describes an early-stopping scheme; the agent-tuning paper I opened does not discuss it in its abstract. Treat the stop rule as a pre-registered design choice, not a published best practice.
- **Spikes in fine-tuning.** Spike-mitigation literature is pretraining-centric. The one fine-tuning data point I verified is the Learns-Less LR 2e-4 spike at r=256.

## 4. Adjacent ideas

- **Forgetting as a side metric.** LoRA forgets less than full fine-tuning (Learns-Less, TMLR), and forgetting concentrates in "intruder dimensions" that grow with high rank and learning rate (arXiv 2410.21228, abstract opened; the learning-rate claim came from a search summary and is not verified). Cheap guard: score a small unrelated held-out set before and after each run and flag drops.
- **Pairwise judging order bias.** QLoRA reports that GPT-4 judging favors whichever answer appears first; average both orders if any model judge scores outputs.
- **Report prediction-level agreement** between seeds, not only accuracy.
- **Checkpoint selection costs eval time.** Evaluating every checkpoint on a downstream task costs generation time on a 10 GB card; a cheap proxy (a 30-50 item subset every N steps, full set at the end) is a design choice worth pre-registering. ASSUMED useful; no source.

## 5. Candidates and verdicts

| Name | What it is | Evidence | Fit | Verdict |
|---|---|---|---|---|
| peft (Hugging Face) | LoRA/QLoRA adapters | Apache-2.0, last push 2026-11-20, not archived, 109 open issues | Standard library for this | try (already the default) |
| trl (Hugging Face) | SFT/GRPO trainers | Apache-2.0, last push 2026-11-21, not archived, 310 open issues | Standard | try |
| unsloth | Memory-lean LoRA training | Apache-2.0, last push 2026-11-22, not archived, 568 open issues | Fits small VRAM; speed and memory claims not checked here | watch (verify claims with a smoke run) |
| GradientStabilizer | Drop-in gradient-magnitude stabilizer | Preprint, ICML 2026; code "will be released soon" per abstract | Pretraining-focused; no code seen | skip for now |
| GradES | Gradient-based early stopping per component | Single 2025 preprint, seen only in search results | Unchecked | skip (not opened) |
| Superfiltering | Weak model selects instruction data | ACL 2024 main; no code link on the abstract page | A small local model could score data | watch |
| AlpaGasus-style grader filtering | LLM grader keeps top-scored examples | Preprint v5 (2024); about 9k of 52k kept | Needs a grader; judge bias applies | watch |

## 6. Rejected

- Memory-only claims about QLoRA double quantization or paged optimizers: they address memory, not stability or accuracy, so they do not answer the question.
- Pretraining spike remedies (layer-norm placement, softmax capping, QK-norm): they change the architecture, which a fine-tune cannot do.
- Blog claims about retry and early-stopping gains seen only in search snippets: not opened, no controlled numbers.

## 7. Sources (read 2026-11-22)

- QLoRA, Dettmers et al., arXiv 2305.14314, May 2023, read via the ar5iv HTML copy: https://ar5iv.labs.arxiv.org/html/2305.14314 (abstract page also opened: https://arxiv.org/abs/2305.14314)
- LoRA Learns Less and Forgets Less, TMLR Aug 2024 (arXiv v2 Sep 2024), HTML read up to about 100k characters: https://arxiv.org/html/2405.09673v2 and https://arxiv.org/abs/2405.09673
- LoRA Without Regret, Thinking Machines Lab blog, 2025-09-29: https://thinkingmachines.ai/blog/lora/
- LoRA vs Full Fine-tuning: An Illusion of Equivalence, arXiv 2410.21228 (v3 Oct 2025, abstract page only): https://arxiv.org/abs/2410.21228
- Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning LLMs, arXiv 2503.07329 (v2 Nov 2025): https://arxiv.org/html/2503.07329v2
- Quantifying Variance in Evaluation Benchmarks, arXiv 2406.10229 (Jun 2024, abstract page): https://arxiv.org/abs/2406.10229
- LIMA, arXiv 2305.11206 (May 2023): https://arxiv.org/abs/2305.11206
- AlpaGasus, arXiv 2307.08701 (v5 Feb 2024): https://arxiv.org/abs/2307.08701
- Superfiltering, ACL 2024, arXiv 2402.00530: https://arxiv.org/abs/2402.00530
- Methods of improving LLM training stability, arXiv 2410.16682 (Oct 2024, 830M model): https://arxiv.org/abs/2410.16682
- GradientStabilizer, arXiv 2502.17055 (ICML 2026): https://arxiv.org/abs/2502.17055
- Adaptive Fine-Tuning for NER, arXiv 2202.02617: https://arxiv.org/abs/2202.02617
- Retrieval-Augmented LLM Agents, arXiv 2603.18272 (opened, did not contain the early-stopping claim): https://arxiv.org/abs/2603.18272
- Repository checks (GitHub API): https://api.github.com/repos/huggingface/peft, https://api.github.com/repos/huggingface/trl, https://api.github.com/repos/unslothai/unsloth
