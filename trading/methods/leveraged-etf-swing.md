<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Leveraged ETF swing trading with trend filter (SOXL, NVDL, TQQQ)

> **TL;DR:** The only way to get real dollar exposure to semis without options, but the tail is near-total loss and tonight's backtest did not support the trend filter; tiny size and forward test only.
> **Source:** trading-lab method card knowledge/methods/leveraged-etf-swing.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** The only way to get real dollar exposure to semis without options, but the tail is near-total loss and tonight's backtest did not support the trend filter; tiny size and forward test only.

**Thesis:** A 2-3x daily-reset fund beats its index only in smooth trends and bleeds in choppy markets, so it should be held only when a trend/volatility filter says conditions are favorable.

**Fit for AI/semis:** SOXL/NVDL are the only way a $1.2k account can get meaningful dollar...

**Evidence** (quality label from the card):
- *peer-reviewed*: Avellaneda and Zhang: leveraged ETF return over a horizon depends on the... [source](https://math.nyu.edu/~avellane/LeveragedETF20090515.pdf)
- *peer-reviewed*: Cheng and Madhavan: leveraged/inverse ETFs embed a path-dependent option that can destroy... [source](https://joim.com/dynamics-leveraged-inverse-exchange-traded-funds)
- *anecdote*: Commentary reports SOXL fell about 90% in 2022 while the underlying semiconductor... [source](https://247wallst.com/investing/2026/05/26/soxl-lost-90-percent-in-2022-while-semiconductors-themselves-fell-35-percent-and-the-daily-reset-math-hasnt-changed/?.tsrc=rss)
- *anecdote*: Public SOXL trend-filter scripts exist; one TradingView script reports ~84% max drawdown... [source](https://id.tradingview.com/scripts/trend-following/)

**Failure modes:** Volatility decay in chop (loses even if underlying flat) | Gap/overnight risk at 3x; single-day -15% in semis is -45% in fund

**Costs and feasibility at $1.2k:** 1-5 bps spreads, ~1% expense ratio already in the price, $0 commission. Mechanically the most feasible aggressive vehicle at $1.2k (low share price, whole shares fine). Blunt.

**Test plan:** Build a synthetic 3x series from SOXX back to 2001, long above the 200-day average with low realized vol, test through 2002, 2008 and 2022. Falsified if filtered drawdown tops 60% in any episode.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 3, evidence 3, feasibility 4. 

**Adjusted for tonight's evidence:** Edge 3 to 2. trading-lab overnight 2026-10-28: the trend rule returned -2.1% CAGR in the confirm window versus SMH 39.2% (DSR 0.17). SOXL buy-and-hold drew down -87.9%.

**In the arena:** `trend_regime_soxl` (hold SOXL only when SMH is above its 50-day average and VIX is under 25; all-in by design, so max loss is the full notional). The registry itself calls it unsupported by the backtest and keeps it as a cheap forward test.

See [00 Index](../00-index.md). Card: `knowledge/methods/leveraged-etf-swing.yaml`.
