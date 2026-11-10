<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Iron condors and credit spreads (defined-risk premium selling)

> **TL;DR:** Poor fit for gap-prone AI names and a thin edge after four-leg costs; only XSP/SPY versions fit, and they add little.
> **Source:** trading-lab method card knowledge/methods/iron-condor-credit-spreads.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Poor fit for gap-prone AI names and a thin edge after four-leg costs; only XSP/SPY versions fit, and they add little.

**Thesis:** Selling out-of-the-money put and call spreads collects the variance risk premium with a hard cap on loss, profiting when the stock stays inside a range.

**Fit for AI/semis:** Poor fit for AI/semis: realized volatility and event gaps are exactly what...

**Evidence** (quality label from the card):
- *marketing*: Option Alpha (retail education, not cost-adjusted) reports 0DTE SPX iron condors opened after the first two hours averaged +37% return on premium across 759 positions with 67% expiring worthless. [source](https://optionalpha.com/blog/0dte)
- *practitioner backtest*: Contrary: Hull Tactical and secondary summaries of Vilkov argue 0DTE strategies show median profits but wide return distributions and mostly statistically insignificant mean returns after costs and tail events. [source](https://hulltactical.com/2026/07/08/0dte-options-tiny-edge-huge-distribution/)
- *peer-reviewed*: Broadie/Chernov/Johannes: large put-selling returns are statistically insignificant relative to model-implied outcomes given crash sampling noise; delta-hedged or market-neutral option portfolios are explained by jump risk premia. [source](https://papers.ssrn.com/abstract=965739)
- *marketing*: Per third-party margin documentation, iron condor buying power reserves the wider side only (spread width x 100 x contracts), and tastytrade requires margin privileges ($2,000 equity) for spreads. [source](https://tastytrade.com/learn/accounts/margin-vs-cash-accounts/)

**Failure modes:** Gap through short strike on news (earnings, guidance, export controls) | Win rate 70-85% with losses 2-5x the average win: one loss erases several wins | Both sides can lose in whipsaw (one side tested, then the other)

**Costs and feasibility at $1.2k:** About $4 plus clearing to open, with 10-40 cents of total bid/ask on four legs. Only on index/ETF products with narrow strikes. A $5-wide condor on SPY/QQQ reserves ~$400 BP (about one third of the...

**Test plan:** Paper-trade 30-45 DTE 10-delta condors on XSP/SPY/QQQ at IV rank above 30, closing at 50% profit or 21 DTE. Falsified if net mean P&L over 60 trades is zero or negative.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 1, evidence 2, feasibility 2. 

**Not in the arena:** The only premium-selling book is `earnings_ironfly`.

See [00 Index](../00-index.md). Card: `knowledge/methods/iron-condor-credit-spreads.yaml`.
