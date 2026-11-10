<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Index 0DTE (SPX/XSP/QQQ-style) incl. XSP minis

> **TL;DR:** XSP is the only 0DTE vehicle that fits $1.2k, but the best evidence says expected net edge is about zero.
> **Source:** trading-lab method card knowledge/methods/index-0dte-spx-xsp.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** XSP is the only 0DTE vehicle that fits $1.2k, but the best evidence says expected net edge is about zero.

**Thesis:** Cash-settled, European-style index options remove assignment/early exercise risk and XSP (1/10th SPX size) lets a small account trade the biggest, tightest 0DTE market with 60/40 tax treatment.

**Fit for AI/semis:** Not the AI-semis universe: this is a market-level instrument.

**Evidence** (quality label from the card):
- *marketing*: Cboe says SPX 0DTE is a very large share of SPX volume, retail is about 50-60% of it, customer flow is balanced so net market-maker gamma hedging is at most... [source](https://www.cboe.com/insights/posts/0-dt-es-decoded-positioning-trends-and-market-impact)
- *preprint*: Vilkov, '0DTE Trading Rules' (Nov 2023): tests straddles, strangles, vertical spreads, ratio spreads and risk reversals held from 10:00/13:00/15:00 to 16:00 on cash-settled 0DTE SPX. [source](https://cxoadvisory.com/equity-options/0dte-strategy-outcomes)
- *preprint*: Bandi/Fusari/Reno estimate 0DTE return and variance risk premia with a new pricing expansion on 2014-2023 intraday data; useful for the existence of a premium, not for net-of-cost trading profits. [source](https://carey.jhu.edu/news/risk-reward-insights-0dte-option-trading)
- *preprint*: Dim/Eraker/Vilkov find high 0DTE open-interest gamma does not amplify past volatility (secondary summary), which undercuts 'dealer gamma squeeze' trading narratives for index 0DTE. [source](https://harbourfrontquant.substack.com/p/impact-of-zero-dte-options-on-the)
- *marketing*: Cboe describes XSP as one-tenth of SPX size, European-style and cash-settled, eligible for 60/40 treatment under Section 1256 (conditions apply; confirm with a tax professional). [source](https://www.cboe.com/tradable_products/sp_500/mini_spx_options/european_style)

**Failure modes:** Short-premium versions have fat left tails (one 2-3% day wipes out weeks of credits) | Overnight/early-morning events not hedgeable inside the session

**Costs and feasibility at $1.2k:** Spreads of 3-10% of premium on XSP; cash-settled, so no assignment risk. XSP is the only 0DTE vehicle that fits $1.2k: an ATM long XSP costs roughly $100-300, and a 1-2 wide...

**Test plan:** Pre-register one XSP rule and paper-trade 100+ sessions with real bid/ask against a random-time null. Falsified if net mean P&L is zero or negative.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 1, evidence 3, feasibility 4. 

**Not in the arena:** Arena books are single-name AI/semis; no XSP book.

See [00 Index](../00-index.md). Card: `knowledge/methods/index-0dte-spx-xsp.yaml`.
