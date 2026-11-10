<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Weight-based self-improvement on a 3080

> **TL;DR:** Ranks weight-update methods from rejection-sampling SFT to GRPO by cost on a 3080, recommending verified-success SFT as the first experiment.
> **Source:** Continuation of the 2026-10-24 handoff; self-training papers and current trainer documentation  ·  **Project:** evolve-lab  ·  **Updated:** 2026-10-27

## Choose the lowest-cost learning signal first

| Method | Exact learning cycle in brief | Main constraint for this machine |
|---|---|---|
| Rejection-sampling SFT | Generate multiple completions, retain externally verified successes, supervise the model on those completions | Straightforward first experiment; correctness filtering and diversity determine what is learned. This is the simple self-training baseline underlying the next rows |
| STaR | Generate reasoning, keep correct examples; for failures, condition on the correct answer to obtain a rationale, then train on successful rationales and repeat | Requires trustworthy answers; a plausible rationale is not independent verification. [Paper](https://arxiv.org/abs/2203.14465) |
| ReST-EM | Alternate sampling from the current model and fitting to reward-selected samples | Useful when many local samples are cheap and reward is reliable. [Paper](https://arxiv.org/abs/2312.06585) |
| Teacher distillation | Generate examples/answers with a stronger teacher, filter, train the student; evaluate against a frozen baseline | My proposed practical variant: use locally verifiable tasks and only a small explicitly budgeted hosted correction set. Matching a teacher's errors is not improvement |
| Self-Rewarding LMs | Generate preference pairs, judge with the model and perform iterative preference training | The judge must improve too; a self-confirming preference loop is a weak first target. [Paper](https://arxiv.org/abs/2401.10020) |
| SPIN | Treat human SFT answers as the target and the current model's generated answers as the opposing distribution; iteratively update | Still depends on a human data anchor, despite the self-play name. [Paper](https://arxiv.org/abs/2401.01335) |
| SEAL | Generate a self-edit containing training data/update instructions, perform adaptation, use downstream success as the outer-loop reward | Nested training/adaptation costs and contamination control make this a later experiment. [Paper](https://arxiv.org/abs/2506.10943) |
| Absolute Zero | Propose executable reasoning tasks, solve them, verify with execution, reinforce useful proposal/solution behavior | Zero external task data is not zero compute or zero verification. [Paper](https://arxiv.org/abs/2505.03335) |
| GRPO | Sample groups of completions per prompt, compute relative advantages from reward, update the policy | Multiple rollouts and training activations consume memory/time; start with a small model and short outputs. [TRL guide](https://huggingface.co/docs/trl/grpo_trainer) |

## LoRA, QLoRA and DoRA

LoRA trains low-rank updates while keeping the base weights fixed. QLoRA keeps the base in low precision while training adapters; it reduces weight memory but does not remove activations, gradients or optimizer state. DoRA separates magnitude and direction of weight updates, rather than being a way to make arbitrary large models fit. Sources: [PEFT LoRA reference](https://huggingface.co/docs/peft/package_reference/lora), [QLoRA](https://arxiv.org/abs/2305.14314), [DoRA](https://arxiv.org/abs/2402.09353).

An inference GGUF's size is not a training memory requirement. Use the original supported training checkpoint and compatible 4-bit loader, not an arbitrary Ollama model blob. Preserve the exact tokenizer, chat template and base revision.

| Target | Evidence / my fit assessment on 10 GB |
|---|---|
| Qwen 3.5 2B | Unsloth reports 5 GB for bf16 LoRA; best conservative first training target |
| Qwen 3.5 4B | Its guide reports about 10 GB for bf16 LoRA. I would attempt **4-bit QLoRA**, short text-only sequences and rank 8; exact peak on this GPU remains unverified |
| Conventional 7–8B | Short-sequence low-rank QLoRA may fit, architecture dependent; do not promise long context, full projection coverage or GRPO fits |
| Gemma 4 E4B | Unsloth lists a 10 GB training requirement; very tight once display/runtime buffers are included. “Effective 4B” is not a memory calculation |
| Qwen 3.5 9B | Guide lists 22 GB for bf16 LoRA. QLoRA needs measurement; defer until a smaller run works |
| Gemma 4 12B | Training support exists, but 10 GB fit for our recipe is **unverified**. Do not start with it just because its inference fits |

Published figures are configuration-dependent vendor guidance, not measurements on Alianto's box. Sources: [Qwen fine-tuning guide](https://unsloth.ai/docs/models/qwen3.5/fine-tune), [Gemma fine-tuning guide](https://unsloth.ai/docs/models/gemma-4/train).

The handoff warns about Python 3.14. Current Unsloth installation instructions now explicitly support 3.13, so the older blanket warning that even 3.13 is unsupported is stale. Use a fresh Python **3.12 or documented 3.13** environment, resolve versions together and record a lockfile; do not alter `~/ai-lab` or the pinned NVIDIA driver. Source: [current Core installation](https://unsloth.ai/docs/get-started/install/pip-install).

## A proposed finetune-lab recipe

These are proposed initial hyperparameters and gates, not a tested training run or a new repo created this session.

1. **Data before weights.** Choose a narrow task: code repairs with independent tests, or schema extraction with audited labels. Put related documents, duplicate headlines and events in the same split. Reserve final confirmation data and timestamps before generating variants. Collect 500–1,000 deduplicated verified training pairs initially; keep the original training set in the mix each round.
2. **Record provenance.** Each JSONL record carries input, target, task/scorer version, source document IDs, generator model/digest, generation date and verification result. Never train on holdout answers, critic comments about holdout, or post-event market facts presented as earlier evidence.
3. **Generate cheaply.** Sample 2–4 local answers per training input. Keep independently verified passes, cap near-duplicates, and preserve hard cases rather than retaining only easy successes. Use at most a small fixed hosted batch during the day if the owner chooses; no automatic quota fallback. The current local models can generate this dataset without a subscription.
4. **Environment.** Create `~/code/finetune-lab` only when the dataset passes audit. Isolate training dependencies in `.venv`, pin versions and the base revision, and keep weights/datasets outside the vault. Start with a supported 2B model for an environment smoke test, then a 4B model if there is headroom. Stop Ollama's loaded models before training so inference and training do not compete for VRAM.
5. **Initial SFT configuration.** 4-bit base, text only; maximum sequence length **512** initially, then 1024 if justified; microbatch **1**; gradient accumulation **16**; LoRA **rank 8 / alpha 16 / dropout 0** on attention projections first; gradient checkpointing; learning rate **1e-4**; warmup **5%**; one epoch; FP16 compute as the conservative starting setting. Record all defaults inherited from the chosen trainer. Add MLP projections or rank 16 only after observing memory and validation gains.
6. **Calibrate rather than invent a duration.** Run 20–50 optimizer steps with the exact sequence/batch configuration, measure median post-warmup seconds/step and peak VRAM. Estimate remaining time from the number of steps, including evaluation/export. Example arithmetic only: 1,000 examples × one epoch / effective batch 16 gives about 63 steps without packing. At an assumed 20 s/step that is about 21 minutes of training; at 120 s/step, about two hours. **Neither speed is a 3080 measurement.** Long sequences and larger models can change these numbers substantially.
7. **Confirmation.** Compare frozen base, evolved prompt on base, adapter with the same prompt, and quantized exported model. Score on development data first. Select once and check unseen confirmation data, including unrelated-task regressions and malformed-input behavior. Inspect error types, not only the mean. Reject if improvement disappears after quantization or if speed/memory harms the intended workload.
8. **Export and rollback.** Save the adapter and its base revision; create merged weights outside GPU memory if needed; convert and quantize using a compatible GGUF tool. Ollama imports a prepared GGUF through `FROM /path/model.gguf` and `ollama create`. Recheck architecture/template support in the installed runtime; current import support does not mean every third-party multimodal GGUF works. Source: [Ollama import documentation](https://docs.ollama.com/import).

## GRPO and overnight use

After SFT is reproducible, test GRPO on a **1–2B** model, short prompts/completions, two generations per prompt, low-rank adapters and an execution-based reward. Set the effective batch to be divisible by the number of generations, per the trainer's constraints. Keep generation/training memory from overlapping unnecessarily; exact trainer/offload settings require a live memory smoke test. Source: [TRL GRPO](https://huggingface.co/docs/trl/grpo_trainer).

Do not start unattended GRPO or SEAL on 8–12B here. The first overnight learning cycle should generate verified data or evolve prompts; the first training night should resume a configuration already run interactively, with a fixed step/time limit and a saved baseline. An NVMe gives room for datasets and checkpoints and faster I/O, but does not reduce the GPU memory needed for backpropagation.

## Adopt for Alianto's setup

Start with verified self-training SFT on a small model, using a measured calibration run. Keep a base checkpoint, a bounded replay dataset and a final untouched confirmation set. Prefer prompt, tool and data improvements until their gains plateau. Fine-tuning is useful when it improves a repeated skill or reduces prompt length/latency; it is not yet justified simply to make a locally running model sound more like Claude. DoRA, self-rewarding, SEAL and Absolute Zero remain research branches until the simpler loop demonstrates a repeatable benefit.
