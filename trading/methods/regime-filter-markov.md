<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Regime filter (200-day MA, VIX bands, HMM/Markov bull-bear-sideways)

> **TL;DR:** A risk overlay, not a return source: trend/regime rules mostly cut volatility and give up bull-run upside; our SMH 200d + VIX rule lagged badly in 2024-26; evidence rests on about four drawdowns.
> **Source:** trading-lab method card knowledge/methods/regime-filter-markov.yaml (deep pass 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict:** Fully feasible as a daily rule but unproven for semis. Edge 3 to 2.

**New evidence (deep pass):**
- *Contrary:* Zakamulin (J. Asset Management 2014): published moving-average timing results are inflated by data mining and ignore costs; bootstrapped out-of-sample tests 1930-2012 show much smaller gains, mostly lower volatility.
- Takada and Kitajima (PLOS ONE 2022): on four stock indices out of sample, trend rules avoid big downside but trail buy-and-hold when uptrends dominate.
- Shu, Yu and Mulvey (arXiv 2024): a persistence-penalised jump model beats an HMM and buy-and-hold on drawdown and Sharpe for US/DE/JP indices, 1990-2023, with costs and delay (author claim; no semis).
- Still in the card: FINSABER (LLM strategies fail across regimes) and the Quantpedia warning that in-sample HMM results are upper bounds.

**Own backtest (2026-10-28):** SMH 200d plus VIX under 20 returned -2.1% CAGR against 39.2% for buy-and-hold in the 2024-26 confirm window, and drawdown was not lower (-41.7% vs -35.7%).

**Test plan (frozen):** three rules only (SMH over 200d; same with a 3% band; plus VIX under 20 as a known-weak control) and a walk-forward 2-state HMM refit each Dec 31 on filtered probabilities with a 1-day lag. Next-open trades, 2 bps. Placebo: 10,000 random on/off schedules with the same time out and number of switches.

**Decision:** keep a rule only if max drawdown falls by a third or more, CAGR loss is at most 20%, it beats the placebo at 95%, and it works pre-2012, post-2012 and in the hold-out (not losing more than 10 CAGR points in 2024-26). The HMM must beat the best simple rule on Calmar out of sample or be dropped. If all fail, use a position-size cap instead.

**Status:** researched-deep; implementability: now. **Scores:** edge 2, evidence 3, feasibility 5.

**In the arena indirectly:** `trend_regime_soxl` uses the SMA plus VIX filter.

See [00 Index](../00-index.md). Card: `knowledge/methods/regime-filter-markov.yaml`.
