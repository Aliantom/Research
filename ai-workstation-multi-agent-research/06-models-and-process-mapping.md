<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Small/Efficient Local LLMs (10GB GPU) and Token-Efficient Self-Improving Process Mapping for Agents

> **TL;DR:** Qwen 3.8 2.7b does not exist; Qwen3.8 models are all 27B or larger, so the user likely means Qwen3-4B or Qwen3-1.7B.
> **Project:** AI workstation  ·  **Updated:** 2026-10-27

## Part A.1 — "Qwen 3.8 2.7b": what's real vs. what the user likely meant

### Takeaway
"Qwen 3.8 2.7b" as a specific named model does not exist. The Qwen organization has moved on to a "Qwen3.8" branding tier by late 2026, but every Qwen3.8 model found is large (27B+); there is no ~2.7B-ish Qwen3.8 variant. The small model the user is almost certainly thinking of is from the original **Qwen3** dense lineup (0.6B / 1.7B / 4B / 8B / 14B / 32B), most likely **Qwen3-4B** or **Qwen3-1.7B**, not anything called "3.8" or "2.7b".

### Cited Findings
- NVIDIA's NeMo docs list the Qwen3 dense model family as 0.6B, 1.7B, 4B, 8B, 14B, 32B parameters; a Hugging Face card gives 8.2B total / 6.95B non-embedding params for the 8B variant — [docs.nvidia.com](https://docs.nvidia.com/nemo/automodel/latest/model-coverage/llm/qwen/qwen3.html)
- A separate Qwen embedding-model family (not the chat/agent LLMs) also ships in 0.6B/4B/8B sizes, which is a likely source of size confusion — [Simon Willison](https://feeds.simonwillison.net/2025/Jun/8/qwen3-embedding/)
- Direct fetch of the official `huggingface.co/Qwen` org page (Oct 2026) shows the current front-page lineup is branded **Qwen3.8**: `Qwen3.8-27B` (~28B), `Qwen3.8-Flash-Next` (~180B), and `Qwen3.8-2.4T-A95B` (2.4T MoE) — no Qwen3.8 model near 2.7B or 3.8B parameters exists on that page. The only sub-5B models shown on the org page at all are the safety-classifier `Qwen3Guard-Stream` series (0.6B/4B/8B), which are not general chat/coding models — [huggingface.co/Qwen](https://huggingface.co/Qwen) (direct fetch)
- A third-party guide lists intermediate releases between Qwen3 and Qwen3.8: Qwen3.5 (Feb 2026: 397B-A17B, 122B-A10B, 35B-A3B, 27B dense, plus hosted Flash/Plus tiers) and Qwen3.6 (open-weight 35B-A3B MoE and a 27B dense model). A RunPod guide claims Qwen3.7 was API-only with no open weights, and that a "Qwen3.8-Max" preview had promised-but-unreleased weights — these specific claims come from a single blog and are unverified — [runpod.io](https://www.runpod.io/articles/guides/run-qwen-3-on-runpod)
- A blog review claims Qwen3-4B "rivals Qwen2.5-72B-Instruct" on some tasks, but cites no specific benchmark and is a secondhand claim — [kunalganglani.com](https://www.kunalganglani.com/blog/qwen3-agent-capabilities-review.md)

### Inferences
- The "3.8" in the user's query is a real current Qwen branding tier, but every model under that tier is tens-to-trillions of billions of parameters — it has no small variant. The "2.7b" figure doesn't match any documented Qwen3 or Qwen3.x size (nearest real sizes are 1.7B and 4B). This strongly suggests the user is conflating the newest branding number ("3.8") they'd seen in passing with an older, smaller model size they actually want.
- Given the target hardware (10GB VRAM, local agentic coding), the practical "what they probably meant" is **Qwen3-4B** (or Qwen3-4B-Instruct-2507-style variants) — small enough for comfortable headroom on 10GB even at higher precision, or **Qwen3-1.7B** for an even lighter footprint.

### Gaps
- Could not find an official Qwen3-4B-Instruct benchmark table (LiveCodeBench, BFCL, TAU-Bench, etc.) in search results — only secondhand/anecdotal claims. Recommend pulling the actual Hugging Face model card for Qwen3-4B-Instruct-2507 directly before finalizing a choice.
- Could not fully confirm whether Qwen3.7/Qwen3.8-Max-preview open-weight release claims are accurate (single-blog source only).

---

## Part A.2 — "Kimi k3.1 pro": what's real vs. what the user likely meant

### Takeaway
No model called "Kimi K3.1" (Pro or otherwise) was found anywhere — it appears to not exist. The real, verifiable Moonshot AI Kimi lineage as of late 2026 is: **Kimi K2** (July 2025, 1T-parameter MoE, 32B active) → **Kimi K2.5** (Jan 2026, multimodal upgrade with a 400M-param vision encoder "MoonViT") → **Kimi K2.7 Code** (June 2026, per Wikipedia, a coding-focused stable release) → **Kimi K3** (July 2026, 2.8T-parameter MoE, reportedly ~104B active, 1M-token context, native vision, built on new "Kimi Delta Attention"/"Attention Residuals" architecture). The user likely meant **Kimi K2** (the well-known, widely-deployed open-weight release) or **Kimi K3** (the current flagship), not a "K3.1" variant.

### Cited Findings
- Kimi K2 launched July 11, 2025 as a 1-trillion-parameter open-weight MoE model with 32B active parameters, released as `Kimi-K2-Base` and `Kimi-K2-Instruct`; API model name `kimi-k2-0711-preview` — [Simon Willison](https://feeds.simonwillison.net/2025/Jul/11/kimi-k2/)
- Kimi K2.5 (Jan 2026) added native vision via a 400M-parameter vision encoder called MoonViT, per Wikipedia's Kimi chatbot article — [Wikipedia: Kimi (chatbot)](https://en.wikipedia.org/wiki/Kimi_(chatbot))
- Wikipedia's Kimi article lists "Kimi K2.7 Code" as the latest stable release, dated 16 June 2026 — [Wikipedia: Kimi (chatbot)](https://en.wikipedia.org/wiki/Kimi_(chatbot))
- Kimi K3 launched July 16–17, 2026 across the Kimi app, Kimi Work, Kimi Code, and Kimi API; described as a 2.8T-parameter MoE with a 1M-token context window and native vision, built on "Kimi Delta Attention (KDA)" and "Attention Residuals (AttnRes)" — [ithome.com.tw](https://www.ithome.com.tw/news/177376), [nexos.ai](https://nexos.ai/blog/kimi-k3/), [forklog.com](https://forklog.com/en/news/moonshot-ai-unveils-kimi-k3-first-open-3t-class-ai-model)
- Sources disagree on active-parameter count (104B per token in one source vs. unspecified in another) and on whether open weights were actually released on the promised July 27, 2026 date — one source says yes with an accompanying technical report, a launch-day page says not yet, and no independent post-launch confirmation was found either way — [handyai.substack.com](https://handyai.substack.com/p/model-drop-kimi-k3), [news.smol.ai](https://news.smol.ai/issues/26-07-16-kimi-k30)
- API pricing reported at $3/million input tokens, $15/million output tokens, $0.30 for cache hits — [nexos.ai](https://nexos.ai/blog/kimi-k3/)
- A direct search for `"Kimi K3.1" Moonshot AI` returned zero results referencing any K3.1 model — every result was about K3 itself.

### Inferences
- "k3.1 pro" is very likely the user misremembering either (a) the version-number style of other vendors (e.g., minor ".1" point releases common elsewhere) applied incorrectly to Kimi, or (b) a tier/plan name ("Pro") from the Kimi consumer app conflated with the model's technical version number. There is no evidence of a real "K3.1" model or a "Pro" model variant distinct from the K3 instruct release.
- For local/on-prem use, none of the real Kimi K2/K2.5/K2.7/K3 models are remotely usable on a 10GB consumer GPU — they are trillion-parameter-class MoE models designed for API/cloud serving or multi-GPU datacenter inference, not single-GPU local hosting.

### Gaps
- Could not independently confirm whether Kimi K3 open weights were actually published by July 27, 2026 as promised — sources conflict.
- Could not confirm the existence of any smaller distilled/mini Kimi variant that might be locally runnable; no evidence of one was found in this search pass.

---

## Part A.3 — "CLM-8B": verification

### Takeaway
No reliable, primary-source confirmation of a specific, well-known model named "CLM-8B" was found. One secondary aggregator (Digg) describes an unnamed-lab "Contrastive Language Model" with self-reported benchmark claims, but there is no lab paper, official release page, or independent verification behind it. This should be treated as **unverified** — likely either a very obscure/niche release, a confusion with a different acronym, or a possible misremembering by the user.

### Cited Findings
- A Digg aggregator post describes a "Contrastive Language Model" (matching the CLM-8B initialism) claiming up to 9× faster inference than a model called "Jev," with self-reported scores of 81.6% on DeepSWE and 87.6% on Terminal-Bench 2.1 after lightweight fine-tuning, and an architecture that caches situation/action representations separately — [digg.com](https://digg.com/ai/i50dwfno)
- Two "BenchLM" comparison pages (CLM-8B vs. BERT-MNLI-YN, CLM-8B vs. BoolQ) exist but contain no actual shared benchmark scores or usable comparison data — [benchlm.ai](https://benchlm.ai/compare/clm-8b-vs-native-circa-bert-mnli-yn)
- All other search hits for "CLM-8B" are unrelated products sharing the acronym (Danfoss hydraulic motors, a WWI-era Crawford CLM aircraft, Canadian Line Materials sirens, Samtec PCB sockets) — none are AI models.

### Inferences
- Given the complete absence of a primary source (no lab name, no paper, no official model card, no Hugging Face page found), "CLM-8B" cannot be confidently described as a real, specific, named model in current circulation. The Digg-sourced claims may describe a real but very new/obscure release that hasn't yet been indexed by mainstream sources, or the name itself may be slightly garbled.

### Gaps
- Could not identify the lab/developer behind the Digg-described "Contrastive Language Model," nor find its Hugging Face/GitHub page, so the benchmark claims (DeepSWE 81.6%, Terminal-Bench 2.1 87.6%) could not be verified against a primary source.
- Flagging clearly per instructions: **do not treat CLM-8B as a confirmed real model** without further direct verification (e.g., searching GitHub/Hugging Face directly for "CLM-8B" or asking the user where they encountered the name).

---

## Part A.4 — Recommended real, current small/efficient open-weight models for local agentic coding on a 10GB GPU (RTX 3080)

### Takeaway
For a single 10GB consumer GPU running local agentic coding, the best-supported, verifiable picks are **Qwen2.5-Coder-7B-Instruct** (mature, well-benchmarked, ~4.7GB at Q4) and **Qwen3-4B** or **Qwen3-8B** (newer architecture, native tool-use/agentic training, comfortable fit at Q4/Q5 with room for long context). MoE options like **Qwen3-Coder-30B-A3B** (only ~3B active params) are a plausible stretch pick if quantized aggressively, but multiple sources put its practical VRAM floor at 16–24GB, so it's a reach rather than a safe fit on 10GB.

### Cited Findings
- Qwen2.5-Coder 7B is repeatedly named the standout 7B/8B-tier local coding model, running at roughly 4.7GB at Q4 quantization — [tembo.io](https://www.tembo.io/blog/best-local-llm-for-coding), general consensus across multiple guides
- A benchmark comparison (single site, not independently verified) lists "Qwen 3 7B" at HumanEval 76.0 (Q4_K_M), ahead of Llama 3.3 8B (72.6) and Mistral Small 3 7B (68.2) — [orcarouter.ai](https://www.orcarouter.ai/blog/best-local-llm-for-coding)
- A dedicated 8GB/12GB/16GB/24GB VRAM coding-model guide names Qwen3.5-9B at Q4 as a practical starting point for 8GB cards, implying comfortable headroom at 10GB — [zimaspace.com](https://shop.zimaspace.com/blogs/tech-ai-hub/best-local-coding-models-8gb-12gb-16gb-24gb-vram)
- Qwen3-Coder-30B-A3B is called an agentic-coding favorite, but one guide lists it at Q3_K_M even in the 16GB tier, and another puts its VRAM floor around 18–24GB; its MoE design (~3B active) might allow CPU/RAM offload of inactive experts, but this is untested in the sources found — [zimaspace.com](https://shop.zimaspace.com/blogs/tech-ai-hub/best-local-coding-models-8gb-12gb-16gb-24gb-vram)
- Devstral Small 2 (24B) reports 68.0% on SWE-bench Verified per Mistral, but an IQ4_XS quantized build is ~12.8GB — too large for a reliable 10GB fit — [zimaspace.com](https://shop.zimaspace.com/blogs/tech-ai-hub/best-local-coding-models-8gb-12gb-16gb-24gb-vram)
- gpt-oss-20b (MoE, 3.61B active/token) runs at roughly 14–16GB, which is also too large for a comfortable 10GB fit — [zimaspace.com](https://shop.zimaspace.com/blogs/tech-ai-hub/best-local-coding-models-8gb-12gb-16gb-24gb-vram)
- Caveat flagged by a general-purpose source: OpenAI reportedly stopped reporting SWE-bench Verified scores for frontier models after confirming training-data contamination on that benchmark, and different guides disagree on scores for the same model (e.g., GLM-5 reported as 72.8% in one source and 77.8% in another) — treat any single-source SWE-bench number with caution — [sitepoint.com](https://www.sitepoint.com/best-local-llm-models-2026/)

### Inferences
- The safest, most defensible 10GB picks are dense models in the 4B–8B range at Q4/Q5 quantization: **Qwen2.5-Coder-7B-Instruct** for a mature, widely-tested coding specialist, and **Qwen3-4B** (or Qwen3-8B if VRAM headroom allows after accounting for context length and KV cache) for more modern agentic/tool-use behavior.
- MoE models with small active-parameter counts (Qwen3-Coder-30B-A3B, gpt-oss-20b) are architecturally attractive for a 10GB card in theory (low active compute) but their total-parameter memory footprint at usable quantization still exceeds 10GB in most guides reviewed — they should be considered experimental/stretch options requiring careful quantization (and ideally RAM-offload tooling) rather than default recommendations.

### Gaps
- No single source tested exactly "10GB" as a tier — all guides bucket by 8GB/12GB/16GB/24GB, so exact fit at 10GB (vs. 8GB or 12GB) required interpolation rather than a direct citation.
- Could not verify current (Oct 2026) official benchmark numbers directly from Qwen's own model cards within the tool-call budget; recommend the user pull the live Hugging Face model cards for Qwen2.5-Coder-7B-Instruct and Qwen3-4B-Instruct before final selection.

---

## Part B.1 — Token-efficient structured decision maps (decision trees, routing graphs, state machines) for LLM agents

### Takeaway
There is active research on making agent routing/decision logic token-efficient by representing it as structured artifacts (trees, skill libraries, reusable workflows, compressed memory) rather than re-deriving reasoning from scratch each call, but no paper found frames this explicitly as a "decision tree for LLM agents" in those exact terms — the closest matches are trajectory-reuse routing frameworks and workflow/skill compression methods.

### Cited Findings
- **TRIAGE** (arXiv 2609.01428) proposes a three-level routing framework that cuts token use for ReAct-style agents by reusing historical execution trajectories instead of rerunning a full reasoning loop for similar queries — [arxiv.org/pdf/2609.01428](https://arxiv.org/pdf/2609.01428)
- **SkillReducer** (arXiv 2603.29919) treats agent routing as matching requests against a library of skill descriptions, and finds that descriptions which are too short cause routing failures while verbose ones waste tokens — it compresses descriptions to the minimum needed to disambiguate skills — [arxiv.org/pdf/2603.29919](https://arxiv.org/pdf/2603.29919)
- **RCR-Router** (arXiv 2508.04903) performs role-aware context routing in multi-agent systems, selecting memory subsets per agent under an explicit token budget, reporting up to 30% token reduction on multi-hop QA benchmarks — [arxiv.org/html/2508.04903v1](https://arxiv.org/html/2508.04903v1)
- **AlphaRouter** (ICML 2026 poster) uses reinforcement learning plus tree search to route individual tokens between a small and a large model — a model-level (not agent-decision-level) routing method — [icml.cc/virtual/2026/poster/63811](https://icml.cc/virtual/2026/poster/63811)
- **R2R** (arXiv 2505.21600) and **CITER** (arXiv 2502.01976) are token-level small/large model routing methods for divergent reasoning paths — relevant to the general concept of structured routing but not agent-level decision trees specifically — [arxiv.org/pdf/2505.21600](https://arxiv.org/pdf/2505.21600), [arxiv.org/pdf/2502.01976](https://arxiv.org/pdf/2502.01976)
- **Agent Workflow Memory (AWM)**, per a survey of agentic reasoning (arXiv 2601.12538), induces reusable workflows from successful trajectories and retrieves them to guide future tasks — effectively a compact, reusable structured-decision artifact rather than raw chain-of-thought — [arxiv.org/pdf/2601.12538](https://arxiv.org/pdf/2601.12538)

### Inferences
- The literature converges on a pattern: instead of a literal visual flowchart, token-efficient "process maps" for agents tend to take the form of (a) a compressed library of named skills/workflows with short disambiguating descriptions, (b) cached/reusable trajectory records keyed by situation similarity, or (c) a lightweight router (bandit/RL-trained) that picks among these without re-running full reasoning. A human-readable decision tree or flowchart specifically designed for cheap LLM parsing at inference time was not found as a named, benchmarked research artifact in this search pass — it may be more of an engineering/product pattern (seen in agent-framework blogs) than a published, benchmarked research method.

### Gaps
- Could not find a paper that explicitly benchmarks "decision tree reasoning" or a visual flowchart format against free-text chain-of-thought for token efficiency in agent routing. A follow-up search for terms like "structured prompt compression tree format LLM" or examining AFlow/EvoAgentX's workflow representations directly (see Part B.2) may close this gap.
- Did not verify whether any of these methods publish the actual token-count savings vs. baseline free-text reasoning in a head-to-head comparison beyond RCR-Router's reported 30% figure.

---

## Part B.2 — Self-improving process maps: do agents fix their own decision trees/routing graphs from reflection on failures?

### Takeaway
Yes — this is a documented and active research area. Several systems (AFlow, EvoAgentX, Reflexion, Agent Workflow Memory, IBM's trajectory-informed memory) have agents or search procedures that explicitly revise their own workflow/decision structure based on execution feedback or failure analysis, though a 2026 paper also documents a real failure mode: self-generated reflections can lock in confidently wrong diagnoses unless grounded in evidence.

### Cited Findings
- **AFlow** (arXiv 2410.10762, ICLR 2025) uses Monte Carlo Tree Search to explore and refine agentic workflows through code edits, tree-structured experience, and execution feedback, reporting a 5.7% average improvement over state-of-the-art baselines across six benchmarks, and finding smaller models can beat GPT-4o on specific tasks at 4.55% of its inference cost — [arxiv.org/pdf/2410.10762](https://arxiv.org/pdf/2410.10762); code referenced at the FoundationAgents/AFlow GitHub repo (location unverified — may have moved)
- **EvoAgentX** (arXiv 2507.03616) is described as "An Automated Framework for Evolving Agentic Workflows" — a direct hit on self-improving workflow structures — [arxiv.org/pdf/2507.03616](https://arxiv.org/pdf/2507.03616)
- **Reflexion** (the foundational verbal self-reflection method): an agent writes a verbal post-mortem after a failed attempt and reuses it on the next try, reporting 91% pass@1 on HumanEval vs. 80% for GPT-4 without reflection — [promptlayer.com/glossary/reflexion](https://www.promptlayer.com/glossary/reflexion)
- **ReAP** (arXiv 2506.02158), a web-navigation method, uses reflections on both successful and failed past runs, improving baseline results by 11 points overall and 29 points specifically on previously-failed tasks — [arxiv.org/html/2506.02158v1](https://arxiv.org/html/2506.02158v1)
- IBM's **trajectory-informed memory** framework (arXiv 2603.10600) extracts learnings — including recovery tips — from execution traces, reporting up to 14.3 percentage-point gains in scenario goal completion on held-out AppWorld tasks — [arxiv.org/pdf/2603.10600](https://arxiv.org/pdf/2603.10600)
- A 2026 paper, informally titled **"Honest Lying: Understanding Memory Confabulation in Reflexive Agents"** (arXiv 2605.29463), finds Reflexion-style agents can store confident-but-wrong self-diagnoses and keep acting on them; it proposes replacing open-ended self-diagnosis with programmatic extraction of failure signals, raising correct object mention from 0% to 86% in their tests — found only via an aggregator summary, not the primary arXiv page, so verify directly — [opentrain.ai summary](https://www.opentrain.ai/papers/honest-lying-understanding-memory-confabulation-in-reflexive-agents--arxiv-2605.29463/)
- A memory survey (arXiv 2603.07670) explicitly flags the risk that a wrong reflection persisting in a long-running agent can cause serious harm, and recommends requiring the agent to cite specific episodic evidence for each reflection it generates as a mitigation — [arxiv.org/pdf/2603.07670](https://arxiv.org/pdf/2603.07670)

### Inferences
- Self-improving process maps are real and demonstrated (AFlow, EvoAgentX for workflow structure; Reflexion/AWM/ReAP/IBM's framework for memory-level self-correction), but the strongest, most directly relevant method for "an agent identifying where a decision tree led it astray and proposing a fix to the tree itself" is **AFlow's** MCTS-based workflow search over tree-structured experience with execution feedback — it operationalizes exactly this loop (propose a workflow edit → test it → keep or discard based on results).
- The "Honest Lying" / confabulation finding is an important caveat for the user's goal: a naive reflection-and-edit loop risks the agent convincing itself of a wrong fix. The mitigation pattern across multiple 2026 papers is to require **programmatic/evidence-grounded** failure signals (not open-ended LLM self-narration) before updating the map.

### Gaps
- Could not verify the current location/activity of the AFlow GitHub repo (listed variously under MetaGPT and FoundationAgents orgs across sources).
- Did not fetch full text of "Honest Lying" (arXiv 2605.29463) directly — only an aggregator summary — so its exact methodology and dataset weren't independently confirmed.

---

## Part C — Mathematical/statistical methods for agent workflow robustness, token efficiency, and accuracy over time

### Takeaway
Three distinct, research-backed statistical toolkits apply here: **(1) contextual-bandit / dueling-bandit methods for model and route selection** (strong, multiple 2025–2026 papers with reported results), **(2) Bayesian uncertainty quantification** for calibrating agent confidence and triggering clarification/retrieval (active but more exploratory/survey-stage), and **(3) statistical process control (SPC) / control-chart methods adapted to agent-pipeline monitoring** (currently mostly vendor/practitioner-level work, not yet peer-reviewed in the sources found).

### Cited Findings
- **LLM Bandit** (arXiv 2502.02743) frames model selection as a multi-armed bandit problem with preference-conditioned routing, letting users set a cost-vs-performance tradeoff at inference time, and is designed to generalize to models it hasn't seen before — [arxiv.org/abs/2502.02743](https://www.arxiv.org/abs/2502.02743?context=cs)
- **PILOT** (Preference-prior Informed LinUCB for adaptive rouTing) extends LinUCB: it learns a shared query/LLM embedding space from offline human-preference data, refines it online via bandit feedback, and uses a multi-choice knapsack formulation to respect budget constraints — [aclanthology.org/people/sho-takemori](https://aclanthology.org/people/sho-takemori)
- **OrcaRouter** (arXiv 2605.30736, May 2026) is a production technical report applying contextual bandits (LinUCB) to live routing with an evolving model pool, offline warm-up, and online adaptation — [alphaxiv.org/abs/2605.30736](https://www.alphaxiv.org/abs/2605.30736)
- **LLM Routing with Dueling Feedback** (arXiv 2510.00841) frames routing as contextual dueling bandits learning from pairwise preferences, using Feel-Good Thompson Sampling for selection; its survey passage groups prior online-routing work into multi-armed bandits, contextual bandits, and RL — [arxiv.org/pdf/2510.00841](https://www.arxiv.org/pdf/2510.00841)
- **AgentPRM** (two distinct papers sharing the name: arXiv 2502.10325 and arXiv 2511.08325) train step-level process reward models for agents via Monte Carlo rollouts / step-wise promise-and-progress scoring; the earlier paper reports small 3B models trained this way beating GPT-4o baselines on ALFWorld — [arxiv.org/html/2502.10325v1](https://arxiv.org/html/2502.10325v1), [arxiv.org/html/2511.08325v1](https://arxiv.org/html/2511.08325v1)
- **Online Process Reward Learning (OPRL)** (arXiv 2509.19199) trains an implicit PRM alongside the agent's policy via alternating optimization, turning trajectory-preference DPO into implicit step rewards combined with episode-level advantages — evaluated on WebShop, VisualSokoban, SOTOPIA — [arxiv.org](https://arxiv.org/pdf/2509.19199v2)
- **Textual Bayes** (arXiv 2506.10060) treats prompts as textual Bayesian parameters, using a new MCMC variant (Metropolis-Hastings through LLM Proposals) to get predictive accuracy and uncertainty estimates, and works with closed-source models — [arxiv.org/abs/2506.10060v1](https://arxiv.org/abs/2506.10060v1)
- A UQ/calibration survey (arXiv 2503.15850) proposes a taxonomy covering input, reasoning, parameter, and prediction uncertainty, and notes classic Bayesian methods like MC dropout are computationally expensive to apply to large LLMs — [arxiv.org/pdf/2503.15850](https://arxiv.org/pdf/2503.15850)
- A Bayesian position paper (arXiv 2506.07448) argues for separating reducible from irreducible uncertainty so agent systems can act differently on each (e.g., ask for clarification vs. retrieve more information) — [arxiv.org/pdf/2506.07448](https://www.arxiv.org/pdf/2506.07448)
- An agent-specific UQ paper, "Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol, and an Empirical Study" (arXiv 2609.07395), exists but only its reference list was retrievable in this search pass — its actual findings could not be confirmed — [arxiv.org/pdf/2609.07395](https://arxiv.org/pdf/2609.07395)
- Practitioner/vendor sources describe applying statistical process control to LLM pipelines: treating causes as "assignable" (traceable to a specific change) vs. "common" (background variance), using I-MR charts for continuous metrics (latency, token spend) and c/u or p charts for attribute counts (error events, blocked prompts), and using rolling-window divergence measures like Jensen–Shannon divergence for discrete distributions (tool IDs, status codes) — [gravitee.io](https://gravitee.io/corpus/gen-939/management-science/statistical-process-control-for-prompt-drift.html)
- A practitioner case study describes a support bot whose responses became shorter and vaguer over time without any single-sample test catching it — motivating sequence/trend monitoring (not single-point checks) for agent quality — [kernel-crush Notion post, July 2026](https://kernel-crush.notion.site/I-Applied-Statistical-Process-Control-to-LLM-Quality-Monitoring-Here-s-What-I-Learned-3914df040c1481abad4bf77ddfc60c8e)

### Inferences
- Of the three toolkits, **contextual/dueling bandits for routing** has the most mature, peer-reviewed-style research backing with concrete reported gains (LLM Bandit, PILOT, OrcaRouter, dueling-feedback routing) and is the most directly applicable, well-trodden method for "which model/route to use when" decisions that also conserves tokens by avoiding unnecessary escalation to larger/pricier models.
- **Process reward models (AgentPRM, OPRL)** are the most relevant math/stats tool specifically for improving *accuracy* over time via fine-grained, step-level credit assignment rather than sparse outcome-only rewards — directly useful if the user wants to train/fine-tune a local small model to get better at multi-step agentic tasks over time.
- **SPC for agent pipelines** is a promising applied-engineering idea with real recommended chart types (I-MR, c/u/p charts, JS-divergence for categorical drift) but is currently backed mainly by vendor blogs and one practitioner case study, not academic papers — treat it as a credible engineering pattern to adopt, not yet an established, peer-reviewed research result.
- **Bayesian UQ for agents** is real and growing but less concretely "production-ready" than the bandit-routing literature — most sources are surveys, position papers, or methods not yet validated specifically on agentic workflows (the one agent-specific UQ paper found, arXiv 2609.07395, couldn't be read beyond its reference list).

### Gaps
- Could not read the full text/findings of the agent-specific UQ taxonomy paper (arXiv 2609.07395) — only its reference list loaded.
- No peer-reviewed (as opposed to vendor/blog) source was found specifically validating SPC control charts for LLM/agent pipeline monitoring; this is a gap the user should be aware of if they want to cite rigorous backing for that approach specifically.
- Did not find a single paper combining all three toolkits (bandit routing + PRM-based training + SPC monitoring) into one unified framework — these currently appear to be three separate, non-integrated research threads that the user would need to combine themselves.
