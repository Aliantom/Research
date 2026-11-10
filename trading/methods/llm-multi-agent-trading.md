<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# LLM multi-agent trading frameworks (TradingAgents, FinMem, FinAgent, FinCon)

> **TL;DR:** No credible evidence of edge: the papers are short-window and leak-prone, so treat it as a research hypothesis tested only forward on post-cutoff headlines.
> **Source:** trading-lab method card knowledge/methods/llm-multi-agent-trading.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** No credible evidence of edge: the papers are short-window and leak-prone, so treat it as a research hypothesis tested only forward on post-cutoff headlines.

**Thesis:** Teams of LLM agents (analysts, bull/bear debaters, traders, risk managers) with memory can read news, filings and prices and generate profitable trades.

**Fit for AI/semis:** AI/mega-cap names are what these papers test on (AAPL, NVDA, MSFT, etc.)...

**Evidence** (quality label from the card):
- *preprint*: TradingAgents (arXiv 2412.20138, AAAI workshop): simulates a trading firm with analyst, bull/bear researcher, trader and risk-manager LLM agents. [source](https://arxiv.org/abs/2412.20138)
- *preprint*: FINSABER: over ~20 years and 100+ symbols, earlier reported LLM advantages deteriorate. [source](https://arxiv.org/abs/2505.07078)
- *preprint*: LiveTradeBench (arXiv 2511.03628): 50-day live evaluation of 21 LLMs shows high general-benchmark scores do not imply better trading; models show distinct risk styles. [source](https://arxiv.org/abs/2511.03628)
- *peer-reviewed*: Look-ahead: Glasserman and Lin show GPT sentiment backtests can be affected by memorization (anonymizing names helps). [source](https://arxiv.org/abs/2309.17322)
- *preprint*: FinMem (layered memory, arXiv 2311.13743) and FinCon (manager-analyst hierarchy with verbal reinforcement, NeurIPS 2024, arXiv 2407.06567) report better returns and Sharpe vs RL and LLM baselines on short... [source](https://arxiv.org/abs/2407.06567)

**Failure modes:** Look-ahead/memorization in backtests on famous tickers | Short evaluation windows (months) and few tickers inflate results

**Costs and feasibility at $1.2k:** Inference cost plus ordinary trading costs; account size is not the limit. Account size is not the issue (paper trading is free).

**Test plan:** Run the agent pipeline daily at 15:00 ET on as-of headlines for 60+ decision days and two models; compare with SMH and a 200-day trend rule. Replay only post-cutoff, name-stripped events.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 1, evidence 2, feasibility 4. 

**In the arena:** `llm_pick_0_7dte` (Sonnet via claude -p picks among the top 3 movers or NONE; execution identical to the rules twin). The full TradingAgents pipeline is built but not wired in.

See [00 Index](../00-index.md). Card: `knowledge/methods/llm-multi-agent-trading.yaml`.
