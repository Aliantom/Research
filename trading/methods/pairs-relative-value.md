<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Pairs / relative-value (NVDA vs SMH, AMD vs NVDA)

> **TL;DR:** Not feasible: two legs, short margin and discrete share sizes at $1.2k, and NVDA-vs-SMH is partly an identity.
> **Source:** trading-lab method card knowledge/methods/pairs-relative-value.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Not feasible: two legs, short margin and discrete share sizes at $1.2k, and NVDA-vs-SMH is partly an identity.

**Thesis:** Prices of closely related stocks revert to their historical spread, so buy the laggard and short the leader when the spread widens.

**Fit for AI/semis:** Semis are highly correlated, but NVDA is a large weight in SMH (so NVDA-vs-SMH is partly an identity), and AI names diverge...

**Evidence** (quality label from the card):
- *peer-reviewed*: Gatev, Goetzmann and Rouwenhorst (1962-2002 US data): pairs portfolios earned up to ~11% annual excess return, above conservative cost estimates. [source](https://alphaarchitect.com/2013/06/pairs-trading-kicks-butt/)
- *peer-reviewed*: Do and Faff (FAJ 2010): pairs trading profitability has trended down, but it does better in turbulent periods and can be improved with alternative algorithms. [source](https://research.bond.edu.au/en/publications/does-simple-pairs-trading-still-work/)
- *practitioner backtest*: A 2024 Yale replication summarized by a newsletter reports ~6.2% annual excess return after costs for its best pairs variant (secondary summary, not verified). [source](https://harbourfrontquant.substack.com/p/rethinking-pairs-trading-can-traditional)

**Failure modes:** Declining profits after publication and crowding | Structural divergence (one name re-rates for good) means the spread never reverts | Short leg requires margin, borrow availability and recall risk

**Costs and feasibility at $1.2k:** Double spreads, short borrow fees and margin interest. Poor. With $1.2k, a dollar-neutral pair means two positions of ~$300-500 each with short margin; one pair can consume most buying power; discrete shares make hedge ratios sloppy. Share-price granularity makes it nearly unworkable.

**Test plan:** Rolling 60-day spread z-score on AMD/NVDA, NVDA/SMH, AVGO/MRVL, enter at 2 sigma with walk-forward hedge ratios. Falsified if net Sharpe is under 0.5 or post-2015 profit is zero.

**Status:** researched; implementability: not feasible. **Scores (1-5, judgment):** edge 1, evidence 3, feasibility 1. Even if the statistical edge exists for large universes, the owner's account size and short-selling constraints make it impractical.

**Not in the arena:** Not feasible.

See [00 Index](../00-index.md). Card: `knowledge/methods/pairs-relative-value.yaml`.
