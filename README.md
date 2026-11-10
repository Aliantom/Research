<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Research

Research notes, one folder per topic. Each line below is a note and its one-line conclusion.

## Agentic graphs

- [Spend on checks before adding agents](agentic-graphs/reports/agentic-graphs-for-ai-systems.md): No default multi-agent graphs: keep one writer, the Python runner, hybrid search and Gate v2; add deterministic gates, differently-trained review and GEPA-style evolution on a three-way split.
- [Adjacent methods for a solo developer's AI workflows (November 2026)](agentic-graphs/research-notes/agentic-graphs-for-ai-systems/adjacent.md): Best-evidenced additions need no new service: check-gated cascades, deterministic and mutation gates, deterministic lead matching, sandboxed workers. Langfuse and speculative decoding rank low.
- [Agent graph orchestration frameworks and durable engines (as of 2026-11-02)](agentic-graphs/research-notes/agentic-graphs-for-ai-systems/frameworks.md): Single-host solo setup: keep the Python runner, SQLite, worktrees and Paperclip; Claude workflows only for fan-out in a job; DBOS or Burr only for a real branching pipeline; skip CrewAI, AutoGen.
- [Graph-based memory and retrieval for a personal agent (November 2026)](agentic-graphs/research-notes/agentic-graphs-for-ai-systems/graph-memory.md): Graph memory helps mainly on multi-hop questions and fact updates, untested against BM25 + embeddings + rerank; keep hybrid search, add link expansion and a harder eval before any extraction graph.
- [Self-improving agents and prompt/graph optimization (November 2026)](agentic-graphs/research-notes/agentic-graphs-for-ai-systems/self-improvement.md): GEPA-style instruction evolution fits evolve-lab best, but evidence is mostly self-reported; a three-way split, paired tests on 200-300 items and a hidden scorer matter more than the optimizer.
- [Empirical evidence on multi-agent graph topologies versus single agents (as of November 2026)](agentic-graphs/research-notes/agentic-graphs-for-ai-systems/topology-evidence.md): Topology gains are conditional: decomposable tasks gain, sequential planning loses 39-70%, one agent usually ties on equal budgets; verify with deterministic oracles first, then a different reviewer.
- [Multi-agent LLM graphs in trading and financial decision-making: evidence as of November 2026](agentic-graphs/research-notes/agentic-graphs-for-ai-systems/trading.md): No credible evidence (Nov 2026) that multi-agent LLM graphs add net alpha; results shrink under longer, costed, post-cutoff tests. Forward-only tests on decision quality are the defensible use.

## AI diagramming and reasoning maps

- [AI diagramming and reasoning maps: overview](ai-diagramming-and-reasoning-maps/ai-diagramming-overview.md): Start page: diagrams help AI when they are structured text (Mermaid plus legend table, DAG reasoning records, repo maps); gains are largest for small quantized local models; first experiments listed.
- [AI diagramming research log](ai-diagramming-and-reasoning-maps/ai-diagramming-research-log.md): Log: the 2026-11-04 pass found text diagrams with legend tables and small-model scaffolds are evidence-backed, no study tests them on quantized models, and queued five local experiments.
- [AI diagramming sources](ai-diagramming-and-reasoning-maps/ai-diagramming-sources.md): Every source behind the diagramming notes with URL, date and evidence label (FETCHED, SUMMARY, TITLE, SECONDARY, MEMORY, LOCAL); D-ids are what the notes cite.
- [Applying diagrams and maps to this system](ai-diagramming-and-reasoning-maps/applying-diagrams-and-maps-to-this-system.md): Five cheap moves ranked: Mermaid map of the AI stack, repo map for the local coder, blueprints for 4-bit workers, DAG reasoning records, quant sensitivity map; each has a test and stop rule.
- [Graph memory and knowledge graphs for agents](ai-diagramming-and-reasoning-maps/graph-memory-and-knowledge-graphs-for-agents.md): Typed, temporal graph memory shows gains on agent benchmarks (self-reported), but simple retrieval often matches it and it can be poisoned; build a typed experience graph on top of hybrid search.
- [Ingestible diagram formats](ai-diagramming-and-reasoning-maps/ingestible-diagram-formats.md): Mermaid plus a legend table is the default AI-readable diagram format; Structurizr for C4, JSON Canvas for Obsidian, repo maps for code; validate-and-repair lifts Mermaid from ~70% to ~100% valid.
- [Reasoning maps and thought structures](ai-diagramming-and-reasoning-maps/reasoning-maps-and-thought-structures.md): GoT sorts 62% better at 31% lower cost than ToT, but for small models the wins come from handing them the plan (blueprints, templates), not more search; DAG-shaped records make reasoning checkable.

## AI workflow roadmap

- [Observability and evaluation sources](ai-workflow-roadmap/observability-and-evaluation-sources.md): Keep JSONL traces and add GPU CSV sampling now; pilot Promptfoo or Phoenix; skip Prometheus/Grafana, hosted tracing and LLM judges.
- [Tasking and integration sources](ai-workflow-roadmap/tasking-and-integration-sources.md): Adopt task briefs, cited read-only MCP results and lexical vault retrieval before adding any new interface or agent framework.

## AI workstation multi agent research

- [Recursive Self-Improvement for AI Agents Without Retraining (Prompting/Scaffolding/Orchestration-Based)](ai-workstation-multi-agent-research/01-self-improvement-harnesses.md): Harness² is a real 2026 Google-affiliated paper and repo on recursive harness self-improvement, with up to +11.5 points on WorkBuddy-Bench.
- [Multi-Agent Communication Architectures, Agentic RAG, and AI Agent Evaluation Frameworks](ai-workstation-multi-agent-research/02-multiagent-eval.md): Named multi-agent patterns exist (debate, supervisor-worker, blackboard); AutoGen is archived while CrewAI and LangGraph remain active.
- [Coding CLIs and Claude Code Features/Plugins](ai-workstation-multi-agent-research/03-coding-clis-and-features.md): Claude Code, Codex CLI and OpenCode are all viable in 2026, but only OpenCode is built for provider-agnostic use with local models.
- [MCP Server Integration Patterns, Obsidian-as-Memory, and Repo Structure for LLM Agents](ai-workstation-multi-agent-research/04-mcp-obsidian-repo-structure.md): Only seven reference MCP servers remain maintained in the official repo; most others were archived in favor of vendor-maintained servers.
- [Cloud Compute Supplementation and 2019 Intel MacBook Pro as Supplemental AI Compute](ai-workstation-multi-agent-research/05-cloud-compute-and-macbook.md): RunPod Community Cloud and Vast.ai are the cheapest on-demand GPU options, Lambda targets data-center GPUs, and pricing sources disagree.
- [Small/Efficient Local LLMs (10GB GPU) and Token-Efficient Self-Improving Process Mapping for Agents](ai-workstation-multi-agent-research/06-models-and-process-mapping.md): Qwen 3.8 2.7b does not exist; Qwen3.8 models are all 27B or larger, so the user likely means Qwen3-4B or Qwen3-1.7B.

## Boris Cherny YC 2026

- [Transcript: Boris Cherny at YC Startup School 2026](boris-cherny-yc-2026/transcript-yc-2026.md): Transcript of Boris Cherny at YC Startup School (2026-07-27): deleting prompts per model, verification, harder tasks, dynamic workflows, self-maintaining routines. Whisper turbo, names fixed.

## data-hub

- [Honest backfill audit (2026-10-29)](data-hub/2026-10-29-honest-backfill-audit.md): Only raw prices with a splits/dividends table, SEC EDGAR by acceptance time and FRED ALFRED vintages can be backfilled honestly; news, social and options history cannot.

## Google ADK harness and loop courses

- [Video 1 transcript (harness + self-evolving agents)](google-adk-harness-and-loop-courses/video-1-transcript-harness-self-evolving-agents.md): Raw Whisper transcript of the 97-minute compilation: Google's AI harness crash course, then the Agent 102 self-evolving agent livestream.
- [Video 2 transcript (agents, memory, long-running, MCP)](google-adk-harness-and-loop-courses/video-2-transcript-agents-memory-long-running-mcp.md): Raw Whisper transcript of the 72-minute compilation: ADK first agent, three memory layers, long-running agents, MCP and multi-agent basics.

## Kimi K3.1

- [Kimi K3.1 weights detected 2026-11-04](kimi-k3.1/weights-2026-11-04.md): Kimi K3.1 weights watcher, 2026-11-04: only the official 1,561 GB MXFP4 repo exists; it fits neither RAM+VRAM nor disk, and no third-party quants were listed yet.

## Local agent evaluation

- [Sources](local-agent-evaluation/sources.md): Sources for local agent evaluation: Anthropic evals guidance, a holdout reuse paper, and a 2026-10-24 Gemma and Qwen sampler audit.

## Mastering Claude Code talk

- [Transcript: Mastering Claude Code in 30 minutes](mastering-claude-code-talk/transcript.md): Transcript of Boris Cherny's talk Mastering Claude Code in 30 minutes (Anthropic, uploaded 2025-05-22): Whisper turbo, with the mis-heard product name corrected by regex.

## Quantization

- [Ollama mechanics for custom quants](quantization/ollama-mechanics-for-custom-quants.md): Ollama 0.40.10 never quantizes GGUF on import and keeps the KV cache at f16; a custom quant goes in via a Modelfile (FROM weights, DRAFT, vision projector, RENDERER/PARSER gemma4).
- [Quantization and reasoning models](quantization/quantization-and-reasoning-models.md): For reasoning models W8A8 or W4A16 is near-lossless and 3-bit is risky; harder tasks degrade most, small models lose more (Qwen3 0.6B -10% MMLU vs 14B -1%), 4-bit KV is fine.
- [Calibration deep dive](quantization/quantization-calibration-deep-dive.md): PTQ calibration saturates near 128 samples of 2048 tokens; domain match beats volume, Wikipedia-only flatters perplexity, and an imatrix should use use-case text and be evaluated elsewhere.
- [Distillation and low-bit QAT deep dive](quantization/quantization-distillation-and-low-bit-qat-deep-dive.md): Below 3 bits a model must re-learn; self-distillation from the full-precision teacher makes sub-4-bit QAT work, and heavily over-trained models like a 12B lose more per bit.
- [Evaluation methods for this PC's jobs](quantization/quantization-evaluation-methods-for-this-pc.md): evolve-lab already scores any Ollama tag on JSON tasks, KL divergence is the fidelity layer under it, and a deterministic tool-call set is missing; lm-eval and BFCL cover generative tasks only.
- [Fine-tuning with quantized bases](quantization/quantization-fine-tuning-with-quantized-bases.md): QLoRA loses quality when merged weights are re-quantized; LoftQ and QA-LoRA avoid this, so finetune-lab should measure its own merge loss by KL divergence.
- [Formats, GGUF types and the KV cache](quantization/quantization-formats-gguf-and-kv-cache.md): Ampere runs INT4/INT8 only (no FP8/FP4); GGUF Q4_K_M is ~4.85 bpw with median KL 0.0075 on Mistral-7B; an 8B KV cache costs 128 KB/token at FP16 and half at q8_0.
- [Quantization glossary](quantization/quantization-glossary.md): Every quantization term with what it is, why it exists and its modern descendant; about half the classic list is CNN-era, replaced by group quantization, GPTQ rounding and rotation.
- [Quantization KL experiment 001: gemma-4-12b-it on the RTX 3080](quantization/quantization-kl-experiment-001-gemma4-12b.md): Pre-registration of the first measured quant test here: eleven gemma-4-12b-it quants and two KV settings scored by KL against Q8_0 on wiki, chat and code text; thresholds fixed in advance.
- [Mixed precision and sensitivity](quantization/quantization-mixed-precision-and-sensitivity.md): Layers differ ~10x in sensitivity; output-error measures rank them better than Hessian proxies; keep early layers and attention V / FFN-down high; llama.cpp --tensor-type applies it.
- [Quantization of MoE and multimodal models](quantization/quantization-of-moe-and-multimodal-models.md): MoE quantizes per expert (rare experts to 2 bits, hot ones 4-8), which could fit qwen3:30b-a3b on this card; multimodal models need the vision tower kept at higher precision.
- [Outliers and rotation deep dive](quantization/quantization-outliers-and-rotation-deep-dive.md): Outliers cause quantization damage; fixes went from channel equalizing to range migration (SmoothQuant, AWQ) to rotation (QuaRot, SpinQuant), and 2026 work shows rotation does nearly all the work.
- [Quantization: overview](quantization/quantization-overview.md): Start page for the quantization research folder: the one idea, a map of the notes, the bottom line for the RTX 3080, and how this folder is mirrored to Aliantom/AITools.
- [Quantization playbook for the RTX 3080 (10 GB)](quantization/quantization-playbook-for-the-rtx-3080.md): On the 3080: imatrix or Unsloth UD GGUF at Q4_K_M-Q6_K, Q8_0 under 4B, flash attention plus q8_0 KV, no CPU offload, QLoRA via Unsloth, and KL against Q8_0 as the acceptance test.
- [Primary paper reads](quantization/quantization-primary-paper-reads.md): Full reads confirmed the headline claims but fixed details: ParetoQ split is from one 125M model, GPTQ beats AWQ at 4-bit on Qwen3, 4-bit KV loses under 1%, blueprints lift small models 20 points.
- [Post-training quantization (PTQ) methods](quantization/quantization-ptq-methods.md): PTQ in 2026: GPTQ and AWQ are the 4-bit workhorses, rotation (QuaRot, SpinQuant) handles activations and sub-4-bit, codebooks and trellises (QuIP#, AQLM, EXL3) win at 2-3 bits.
- [Quantization-aware training (QAT) methods](quantization/quantization-qat-methods.md): QAT recovers most 4-bit-and-below loss (torchao: up to 96% of the PTQ gap) and vendors ship QAT checkpoints (Gemma 3/4, gpt-oss); on this PC the practical form is QLoRA fine-tuning.
- [Quantization research log](quantization/quantization-research-log.md): Dated log of each quantization research pass: asked, found, changed, and open questions (Unsloth claims unverified, EXL3 numbers missing, q8_0 KV quality unmeasured).
- [Rounding methods deep dive](quantization/quantization-rounding-methods-deep-dive.md): Round-to-nearest is provably suboptimal; AdaRound to GPTQ to SignRoundV2 learn rounding to cut output error, GPTQ is Babai nearest-plane, and the frontier is better init and extreme-low-bit rounding.
- [Serving kernels and speculative decoding](quantization/quantization-serving-kernels-and-speculative-decoding.md): On Ampere use llama.cpp CUDA, Marlin or EXL3; EXL3 at 4.0 bpw beats GGUF Q4_K_M on KL, GGUF wins above 5 bits; gemma4 ships an MTP draft that Ollama uses for speculative decoding.
- [Quantization sources](quantization/quantization-sources.md): Every source behind the quantization notes with URL, date and evidence label: 50 read via search or fetch, plus from-memory papers whose IDs need checking before citing.
- [Quantization tools and repos](quantization/quantization-tools-and-repos.md): Toolchain for this PC: llama.cpp for GGUF, GPTQModel/llm-compressor for vLLM, exllamav3 for EXL3, torchao for QAT, bitsandbytes/Unsloth for QLoRA; AIMET and TensorRT-LLM matter for other hardware.

## self-improving-ai

- [Blueprint: make the suite improve through measured local work](self-improving-ai/00-blueprint.md): Recommends building on evolve-lab with a DGM, GEPA and ACE splice and a frozen scorer, defaulting to a 4-bit 8-12B local model on the 3080.
- [DGM family deep dive](self-improving-ai/01-dgm-family-deep-dive.md): Compares Gödel Machine, DGM, HGM, SICA and related self-improving agent methods using authors' reported results, none reproduced locally.
- [Prompt and program evolution](self-improving-ai/02-prompt-and-program-evolution.md): Surveys prompt and program evolution methods (FunSearch, AlphaEvolve, OpenEvolve, OPRO) that work around a frozen local model, with no common leaderboard.
- [Weight-based self-improvement on a 3080](self-improving-ai/03-weight-based-self-improvement-on-a-3080.md): Ranks weight-update methods from rejection-sampling SFT to GRPO by cost on a 3080, recommending verified-success SFT as the first experiment.
- [Agent memory, reflection and open-endedness](self-improving-ai/04-agent-memory-reflection-and-open-endedness.md): Reviews memory and reflection methods (Reflexion, ACE, Voyager, Mem0) and favors ACE-style structured playbooks over rewriting one large summary.
- [Applying it: trading, coding, money](self-improving-ai/05-applying-it-trading-coding-money.md): Finds no verified evidence that agent trading systems beat simple baselines after costs, and warns headline prediction scores are not tradable profit.
- [Primary source register](self-improving-ai/sources/2026-10-24-primary-source-register.md): Register of bibliographic links for the self-improving AI research notes, showing which note cites each paper; citation does not mean reproduced.

## site-foundry

- [Reaching site-foundry leads with no phone and no email](site-foundry/2026-10-29-reaching-leads-without-phone-or-email.md): For leads with no phone or email: walk-ins first, then a manual Facebook/Instagram message, then a hand-mailed postcard with a QR code; skip texts, scraped emails and contact-finder tools.
- [Outreach compliance for site-foundry (DC, Maryland, Virginia)](site-foundry/2026-11-02-outreach-compliance.md): Manual cold email works with CAN-SPAM fixes and a suppression list; cold calls need DNC scrubbing and Virginia rules; skip cold SMS; Google Places terms bar storing its data. Not legal advice.
- [Reaching no-website, no-email leads without phone calls](site-foundry/2026-11-03-reaching-no-website-leads-without-phone.md): Best no-phone route for the 13 phone-only Annapolis leads: a personalized first-class postcard with a per-lead QR link (about $12 for 13) plus a walk-in; no channel has solid response-rate data.

## trading

- [Trading methods ranked for a $1.2k AI/semis account](trading/00-index.md): No method in the 27-card library has proven edge at $1.2k; best bets are AI/semis rotation and trend/regime overlays (both bias-prone); premium selling, LEAPS, pairs and the wheel fail.
- [ThetaData Options Value: does it give 1-minute bid/ask on expired contracts?](trading/2026-11-03-thetadata-value-tier-expired-1-minute-quotes-check.md): ThetaData docs list 1-minute NBBO option quotes under Value, but none says Value serves expired contracts back to 2020; email support once, then buy one month and test SPY 2020-03-20 250C.
- [AI supply-chain lead-lag (TSMC revenue, hyperscaler capex, DRAM pricing, Asian session)](trading/methods/ai-supply-chain-lead-lag.md): Plausible but unproven, and likely priced in on the most-watched stocks; a free Asian-session test is cheap, but this is not a tradable edge yet.
- [Butterflies, OPEX pinning and dealer gamma (GEX)](trading/methods/butterflies-pinning.md): Cheap lottery at best: the pinning evidence ends in 2002, fees take a big bite of a $20-60 debit, and nothing supports single-name AI stocks.
- [Calendars and diagonals (term-structure and earnings calendars)](trading/methods/calendars-diagonals.md): Affordable at $100-$400 per position, but there is no direct evidence on calendar P&L and the post-earnings IV collapse hits both legs, so paper-only until term-structure data exists.
- [Cross-sectional momentum / industry rotation among AI-semi names](trading/methods/cross-sectional-momentum-rotation.md): Momentum is a real but decayed anomaly proven on broad long-short books; a top-3-of-27 AI-semis rotation can't be told from owning the beta, so edge is rated 2 and needs a random-pick placebo.
- [Earnings IV/RV and term-structure screen (sell rich, avoid buying rich)](trading/methods/earnings-iv-rv-screen.md): Implied earnings moves beat realized ones in most events, but the average edge is near zero after fat tails and flips by regime, and IV-minus-RV does not predict straddle returns: forward test only.
- [Earnings straddles vs selling into IV crush](trading/methods/earnings-straddle-ivcrush.md): Long straddles are unaffordable and lose on average after bid/ask; only a defined-risk short iron fly is feasible, and that is marginal and exposed to gap years.
- [Event-driven trading on 8-K items and headlines (guidance, contracts, offerings)](trading/methods/event-driven-8k.md): The tradable part after the first reaction is small and shrinking; worth only a cheap next-day-open event study, not a live method.
- [GPU rental price indices as a lead indicator for AI-compute names](trading/methods/gpu-rental-price-leadlag.md): Untested idea: daily GPU rental price indices as a lead indicator for AI-compute stocks; collect the free indices from now and test after ~60 trading days.
- [Index 0DTE (SPX/XSP/QQQ-style) incl. XSP minis](trading/methods/index-0dte-spx-xsp.md): XSP is the only 0DTE vehicle that fits $1.2k, but the best evidence says expected net edge is about zero.
- [Insider open-market purchases (SEC Form 4)](trading/methods/insider-buying-form4.md): Opportunistic insider buying has a real academic edge, but mega-cap AI insiders almost never buy, so there will be too few events to trade or even test.
- [Intraday momentum: first half-hour predicts last half-hour](trading/methods/intraday-momentum-first-last-half-hour.md): Strong index-ETF literature, but tonight's 60-day test on AI/semis found no link between the first and last half hour, and PDT limits day trades; do not rely on it.
- [Iron condors and credit spreads (defined-risk premium selling)](trading/methods/iron-condor-credit-spreads.md): Poor fit for gap-prone AI names and a thin edge after four-leg costs; only XSP/SPY versions fit, and they add little.
- [IV rank, term-structure and skew/spread signals as return predictors](trading/methods/iv-rank-term-structure-signals.md): Option-implied signals predicted returns in broad cross-sections, but the effect fades after 2008, partly reflects borrow fees and is insignificant in 2023-26 mega-caps: filters at best, edge 1.
- [LEAPS and poor-man's covered calls](trading/methods/leaps-pmcc.md): Not tradable at $1.2k: a deep in-the-money LEAPS on any universe name costs more than the account.
- [Leveraged ETF swing trading with trend filter (SOXL, NVDL, TQQQ)](trading/methods/leveraged-etf-swing.md): The only way to get real dollar exposure to semis without options, but the tail is near-total loss and tonight's backtest did not support the trend filter; tiny size and forward test only.
- [LLM multi-agent trading frameworks (TradingAgents, FinMem, FinAgent, FinCon)](trading/methods/llm-multi-agent-trading.md): No credible evidence of edge: the papers are short-window and leak-prone, so treat it as a research hypothesis tested only forward on post-cutoff headlines.
- [Overnight vs intraday return premium (tug of war)](trading/methods/overnight-vs-intraday-returns.md): Descriptively robust, but costs eat the premium for daily churn; use it as a feature (avoid holding earnings gaps), not a strategy.
- [Pairs / relative-value (NVDA vs SMH, AMD vs NVDA)](trading/methods/pairs-relative-value.md): Not feasible: two legs, short margin and discrete share sizes at $1.2k, and NVDA-vs-SMH is partly an identity.
- [Post-earnings-announcement drift (PEAD) in mega-cap tech](trading/methods/post-earnings-drift.md): The literature says drift is gone in large caps, and we lack surprise data; low odds.
- [Regime filter (200-day MA, VIX bands, HMM/Markov bull-bear-sideways)](trading/methods/regime-filter-markov.md): A risk overlay, not a return source: trend/regime rules mostly cut volatility and give up bull-run upside; our SMH 200d + VIX rule lagged badly in 2024-26; evidence rests on about four drawdowns.
- [Calendar effects: pre-FOMC drift, OPEX week, turn-of-month](trading/methods/seasonality-opex-fomc.md): Pre-FOMC drift reportedly vanished after 2015 and expected profit per event on $1.2k is a few dollars; a research curiosity only.
- [Short premium at ~45 DTE, take profits at 50%, exit at 21 DTE](trading/methods/short-premium-45dte-manage-21.md): Defined-risk only at this size means 2-3 positions with negative skew, and the supporting research is vendor work on naked SPY/SPX strangles.
- [Social attention / sentiment (Reddit, StockTwits, search volume)](trading/methods/social-attention-reddit-stocktwits.md): Mention counts predict next-day and 20-day reversal in several studies, but WSB picks show no alpha, effects sit in small retail stocks, and our history starts 2026-10-28: forward test only, edge 1.
- [2-8 week options around catalysts (earnings, launches, AI capex news)](trading/methods/swing-catalyst-options.md): Mixed evidence: straddles gain in the 3 days before earnings, but long premium has a negative baseline and wide spreads, and nothing tests 5-10 day pre-catalyst debit spreads: paper only, 2-year test.
- [Time-series momentum / trend following on SMH and AI-semi names](trading/methods/time-series-momentum-semis.md): Sensible and feasible, but tonight's SMH 200-day plus VIX backtest lost badly to buy-and-hold in the confirm window, with high overfit risk.
- [Unusual options activity and put-call ratio signals](trading/methods/unusual-options-flow.md): Cannot be tested properly without paid trade-level data, and retail-flow signals are noise or contrarian; do not pay for alerts out of this account.
- [Vertical debit spreads (defined-risk directional)](trading/methods/vertical-debit-spreads.md): Feasible and a sensible way to express a directional view, but the spread only adds friction unless the underlying signal has an edge, which is unproven.
- [The wheel: cash-secured puts then covered calls](trading/methods/wheel-csp-cc.md): Not feasible: one cash-secured put on a universe name needs $10,000 to $100,000+.
- [0-7 DTE directional long calls/puts on single names](trading/methods/zero-dte-long-options.md): Feasible and closest to the owner's style, but the lowest-expectancy approach here: the buyer pays the variance premium plus spread, so it is a lottery sleeve measured against a random control.
- [Swarm findings (verified only)](trading/swarm-findings.md): 34 Sonnet-verified leads from the overnight local research swarm; top-40 precision 12.5-27.5%, and a blind A/B leaned to rubric v3 (4/20 vs 1/20, p≈0.17).
- [tastytrade MCP server vs our SDK path (2026-10-28)](trading/tastytrade-mcp-vs-sdk.md): Use tastytrade's official MCP only for interactive read-only chat with a read-scope OAuth grant; skip it for the bot and agents (no greeks/streaming, 36-113k tokens of tools, npm audit issues).
