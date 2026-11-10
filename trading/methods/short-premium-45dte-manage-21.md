<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Short premium at ~45 DTE, take profits at 50%, exit at 21 DTE

> **TL;DR:** Defined-risk only at this size means 2-3 positions with negative skew, and the supporting research is vendor work on naked SPY/SPX strangles.
> **Source:** trading-lab method card knowledge/methods/short-premium-45dte-manage-21.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Defined-risk only at this size means 2-3 positions with negative skew, and the supporting research is vendor work on naked SPY/SPX strangles.

**Thesis:** Implied volatility on average exceeds realized volatility (variance risk premium), so repeatedly selling defined-risk options near 45 DTE and closing early captures theta while limiting gamma risk.

**Fit for AI/semis:** Semis have high IV (good premium) but also large gap risk from...

**Evidence** (quality label from the card):
- *marketing*: tastylive internal research on SPY 45 DTE 16-delta strangles found managing at 50% of max profit gave the best average P&L per day versus 25% or hold-to-expiry. [source](https://tastylive.com/shows/options-jive/episodes/why-manage-at-50-not-25-for-short-strangles-09-13-2016)
- *marketing*: tastylive: an SPX study found most hold-to-expiry profits came in the first ~25 days. [source](https://www.tastylive.com/shows/market-measures/episodes/duration-to-reach-50-winners-01-17-2017)
- *peer-reviewed*: Academic: selling index puts has historically earned large returns but with crash losses; Broadie/Chernov/Johannes argue the apparent put-selling alpha is statistically insignificant once tail sampling error is considered... [source](https://papers.ssrn.com/abstract=965739)
- *peer-reviewed*: Israelov/Nielsen show option-selling returns decompose into equity beta exposure plus a volatility risk premium; the net 'alpha' is the premium only when implied exceeds realized. [source](https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/FAJ-Covered-Call-Strategies-One-Fact-and-Eight-Myths.pdf)
- *peer-reviewed*: Critique: Coval/Shumway found zero-beta ATM straddles lose ~3% per week on average, i.e. [source](https://scholarsarchive.byu.edu/facpub/9281)

**Failure modes:** Tail event (earnings gap, tariff headline) loses several times the credit | Buying power exhaustion: one $5-wide spread reserves $500

**Costs and feasibility at $1.2k:** About $4 plus clearing per condor; a $5-wide spread reserves $350-$450 of buying power. Defined-risk only. One $5-wide put spread uses ~$350-$450 of buying power, so you can hold at most 2-3 positions, which...

**Test plan:** Snapshot chains daily for 10 tickers and simulate 45 DTE 20-delta put spreads at IV rank over 40, exit at 50% profit or 21 DTE, using bid/ask; compare with holding to expiry.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 2, evidence 2, feasibility 2. 

**Not in the arena:** No 45 DTE book; `earnings_ironfly` is the only premium seller.

See [00 Index](../00-index.md). Card: `knowledge/methods/short-premium-45dte-manage-21.yaml`.
