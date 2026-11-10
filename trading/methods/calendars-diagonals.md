<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Calendars and diagonals (term-structure and earnings calendars)

> **TL;DR:** Affordable at $100-$400 per position, but there is no direct evidence on calendar P&L and the post-earnings IV collapse hits both legs, so paper-only until term-structure data exists.
> **Source:** trading-lab method card knowledge/methods/calendars-diagonals.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Affordable at $100-$400 per position, but there is no direct evidence on calendar P&L and the post-earnings IV collapse hits both legs, so paper-only until term-structure data exists.

**Thesis:** Selling near-dated rich volatility and owning a longer-dated option profits from steep term-structure kinks (e.g. before earnings), with lower cost and smaller vega than a straight long.

**Fit for AI/semis:** Earnings-heavy AI/semis names have a large front-week IV premium, which is the textbook calendar setup.

**Evidence** (quality label from the card):
- *peer-reviewed*: Vasquez (JFQA 2017): sorting firms by the slope of the implied-volatility term structure predicts straddle returns (positive slope => higher future option returns), significant after traditional and jump factors. [source](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/equity-volatility-term-structures-and-the-cross-section-of-option-returns/F0A40E99FD2458367DD9A56A89783D38)
- *peer-reviewed*: Dubinsky et al.: earnings-date uncertainty is priced in front-month implied volatility and is informative about subsequent volatility, supporting the existence of a front-month event premium. [source](https://ideas.repec.org/a/oup/rfinst/v32y2019i2p646-687..html)
- *practitioner backtest*: iVolatility's large bid/ask study shows long ATM straddles across earnings lose ~18% on average due to the IV crush. [source](https://www.ivolatility.com/news/3147)
- *anecdote*: I did not find a peer-reviewed or well-documented backtest of single-stock earnings calendars with real bid/ask fills; tastylive/OptionAlpha material is explanatory and not cost-adjusted. [source](https://optionalpha.com/learn/poor-mans-covered-call)

**Failure modes:** Back-month IV drops on the print too (term-structure collapse), unlike the textbook assumption | Early assignment on short front leg (dividend or ITM) can break the structure | Large gap in either direction moves price out of the profit tent...

**Costs and feasibility at $1.2k:** $2 to open; allow 3-8% of the debit for spreads across two expiries. Feasible: calendars on $100-$300 stocks cost ~$100-$400 each (ATM, 1-2 weeks apart) and have a defined max loss equal to the debit.

**Test plan:** Forward paper test around earnings: log front/back IV and fills, compare P&L across term-slope terciles. Falsified if mean net return over 40+ events is zero or negative.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 2, evidence 2, feasibility 4. 

**Not in the arena:** No book; needs forward term-structure logging.

See [00 Index](../00-index.md). Card: `knowledge/methods/calendars-diagonals.yaml`.
