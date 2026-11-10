<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Earnings straddles vs selling into IV crush

> **TL;DR:** Long straddles are unaffordable and lose on average after bid/ask; only a defined-risk short iron fly is feasible, and that is marginal and exposed to gap years.
> **Source:** trading-lab method card knowledge/methods/earnings-straddle-ivcrush.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Long straddles are unaffordable and lose on average after bid/ask; only a defined-risk short iron fly is feasible, and that is marginal and exposed to gap years.

**Thesis:** Options price an expected earnings move; if actual moves on average differ from implied moves after costs, either buying (if under-priced) or selling (if over-priced) the straddle/strangle earns an edge.

**Fit for AI/semis:** Strong fit: AI/semis names (NVDA, AMD, AVGO, MU, ARM, SMCI, PLTR, CRWV)...

**Evidence** (quality label from the card):
- *peer-reviewed*: Gao/Xing/Zhang (JFQA 2018): straddles on individual stocks generally earn negative returns, but ATM straddles held from 3 days before an announcement to... [source](https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/anticipating-uncertainty-straddles-around-earnings-announcements/7B34877AD5E06304BA3C55FBA3219FDD)
- *practitioner backtest*: Contrary, recent and bid/ask based: iVolatility (vendor) tested buying ATM straddles ~9 DTE before ~9,600 S&P 500 earnings, exit next session at... [source](https://www.ivolatility.com/news/3147)
- *practitioner backtest*: ORATS (data vendor): the historical ratio of actual to implied earnings move has hovered near 85% (straddles usually rich), but its Feb... [source](https://orats.com/blog/earnings-straddles-strong-season-2026)
- *preprint*: de Silva/Smith/So: retail loses about 5-9% on average trading options around earnings (10-14% for high expected-volatility events) because they bid up pre-announcement... [source](https://quantpedia.com/how-retail-losses-money-in-option-trading/)
- *peer-reviewed*: Dubinsky/Johannes/Kaeck/Seeger (RFS 2019): option-implied earnings-date uncertainty is large, time-varying and informative about future volatility, which provides the basis for an implied-move signal. [source](https://ideas.repec.org/a/oup/rfinst/v32y2019i2p646-687..html)

**Failure modes:** Edge reverses by season (2025/2026 regime differences) | Spreads on event expirations widen precisely at entry/exit

**Costs and feasibility at $1.2k:** About $2 to open a straddle; earnings-week spreads run 2-6% of price, up to 20% in thin names. Long straddles on $200+ stocks cost $1,500-$4,000: not feasible on most of the universe.

**Test plan:** Compare realized earnings moves from daily prices with implied moves logged forward, then paper-trade long and short iron fly P&L net of bid/ask each quarter.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 2, evidence 4, feasibility 2. 

**In the arena:** `earnings_ironfly` (defined-risk iron fly into confirmed after-close earnings, exit next 10:00, 6% wings, up to 35% of the book at risk). No long-straddle book.

See [00 Index](../00-index.md). Card: `knowledge/methods/earnings-straddle-ivcrush.yaml`.
