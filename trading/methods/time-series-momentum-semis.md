<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Time-series momentum / trend following on SMH and AI-semi names

> **TL;DR:** Sensible and feasible, but tonight's SMH 200-day plus VIX backtest lost badly to buy-and-hold in the confirm window, with high overfit risk.
> **Source:** trading-lab method card knowledge/methods/time-series-momentum-semis.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Sensible and feasible, but tonight's SMH 200-day plus VIX backtest lost badly to buy-and-hold in the confirm window, with high overfit risk.

**Thesis:** An asset whose own past 1-12 month excess return is positive tends to keep rising, so holding it only while its trend is up should cut drawdowns and capture persistent runs.

**Fit for AI/semis:** Semis have strong multi-year trends (2023-2025 AI run) and deep drawdowns (2022...

**Evidence** (quality label from the card):
- *peer-reviewed*: Moskowitz, Ooi and Pedersen found time-series momentum across 58 liquid futures (equity indices, FX, commodities, bonds). [source](https://www.aqr.com/library/journal-articles/time-series-momentum)
- *peer-reviewed*: Critiques: Kim, Tse and Wald argue the reported profits come mostly from volatility scaling rather than trend itself... [source](https://quantpedia.com/?p=637)
- *peer-reviewed*: McLean and Pontiff: across 97 published predictors, returns fall ~26% out of sample and ~58% after publication, so... [source](https://academicnewsletter.sufe.edu.cn/info/359722)
- *practitioner backtest*: Faber-style 10-month moving average rule is widely replicated as reducing drawdown on asset-class baskets. [source](https://freefincal.com/market-timing-with-ten-month-moving-average-tactical-asset-allocation-backtest-part-2/)

**Failure modes:** Momentum crashes at sharp market reversals (Daniel and Moskowitz; not verified in this session) | Backtest dominated by one AI bull run; very few independent trend episodes

**Costs and feasibility at $1.2k:** 1-2 bps ETF spread, negligible at monthly frequency; whipsaw is the real cost. Yes. One or two positions (SMH or SOXX, whole shares) fit in $1.2k. Fractional shares: verify availability on tastytrade.

**Test plan:** SMH daily closes, long above the 200-day average (and separately 12-month return above zero), next-open fills, 3 bps all-in, cash earns T-bills; compare with buy-and-hold over 2001-2026 and rolling 5-year windows.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 3, evidence 3, feasibility 5. 

**Adjusted for tonight's evidence:** Edge 3 to 2. trading-lab overnight 2026-10-28: -2.1% CAGR, Sharpe 0.10 versus SMH 39.2% and 1.03; DSR on confirm 0.17. The confirm window is one AI bull regime, so this is one draw, not proof the idea fails.

**Not in the arena as its own book:** `trend_regime_soxl` uses a 50-day version of the same idea on SOXL.

See [00 Index](../00-index.md). Card: `knowledge/methods/time-series-momentum-semis.yaml`.
