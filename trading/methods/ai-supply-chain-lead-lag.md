<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# AI supply-chain lead-lag (TSMC revenue, hyperscaler capex, DRAM pricing, Asian session)

> **TL;DR:** Plausible but unproven, and likely priced in on the most-watched stocks; a free Asian-session test is cheap, but this is not a tradable edge yet.
> **Source:** trading-lab method card knowledge/methods/ai-supply-chain-lead-lag.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Plausible but unproven, and likely priced in on the most-watched stocks; a free Asian-session test is cheap, but this is not a tradable edge yet.

**Thesis:** Upstream data (TSMC monthly sales, hyperscaler capex guidance, DRAM/NAND prices, Asian-session moves in TSM/SK Hynix/Tokyo Electron) leads US-listed suppliers because investors are slow to propagate links.

**Fit for AI/semis:** The theme is a tightly linked supply chain: hyperscaler capex drives NVDA/AVGO/ANET orders and DRAM/HBM pricing drives MU/SNDK.

**Evidence** (quality label from the card):
- *peer-reviewed*: Cohen and Frazzini (JF 2008): shocks to a firm's major customers predict supplier returns, consistent with limited investor attention; long-short returns survived factor and momentum controls in the original sample. [source](https://www.aqr.com/Insights/Research/Journal-Article/Economic-Links-and-Predictable-Returns)
- *preprint*: A later replication (arXiv 2301.11394) finds customer momentum significant overall but smaller and statistically insignificant in the post-discovery sample, consistent with exploitation. [source](https://ar5iv.labs.arxiv.org/html/2301.11394)
- *anecdote*: For DRAM, trade press says spot prices lead contract prices with a lag and TrendForce revises contract forecasts quarterly. [source](https://seekingalpha.com/article/4285514-micron-nows-time-buy)
- *anecdote*: Press relay of a TrendForce forecast raising Q3/Q4 2026 DRAM contract prices and calling it a Micron benefit shows the information is public, widely distributed and probably priced by the... [source](https://www.kucoin.com/news/flash/trendforce-raises-q3-q4-dram-contract-price-forecasts-benefits-micron)

**Failure modes:** Information is public and instantly priced in the most-followed stocks | Memory stocks often lead (not lag) the price cycle: stock peaks before prices peak | TrendForce/DRAMeXchange paid data, not free history

**Costs and feasibility at $1.2k:** Normal single-stock costs, $0 commission, wide spreads at the 09:30 open. Feasible for daily-frequency use with free data (Asian close to US open gap, monthly TSMC revenue). Paid price indices are not. Whole-share MU/SNDK positions fit.

**Test plan:** Regress US open-to-close return on the prior Asian-session return (000660.KS, 8035.T) for MU, AMAT, LRCX; event-study TSMC monthly revenue. Falsified if next-day net t-stat is under 2.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 2, evidence 2, feasibility 3. 

**Not in the arena:** No book of its own; a free test on existing data comes first.

See [00 Index](../00-index.md). Card: `knowledge/methods/ai-supply-chain-lead-lag.yaml`.
