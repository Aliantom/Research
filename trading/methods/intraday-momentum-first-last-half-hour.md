<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Intraday momentum: first half-hour predicts last half-hour

> **TL;DR:** Strong index-ETF literature, but tonight's 60-day test on AI/semis found no link between the first and last half hour, and PDT limits day trades; do not rely on it.
> **Source:** trading-lab method card knowledge/methods/intraday-momentum-first-last-half-hour.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Strong index-ETF literature, but tonight's 60-day test on AI/semis found no link between the first and last half hour, and PDT limits day trades; do not rely on it.

**Thesis:** The return from the prior close through the first 30 minutes predicts the direction of the last 30 minutes, driven by late-informed trading and hedging flows (gamma, leveraged ETF rebalancing).

**Fit for AI/semis:** Leveraged ETFs and options hedging concentrate flows into the close, and semis...

**Evidence** (quality label from the card):
- *peer-reviewed*: Gao, Han, Li and Zhou (JFE 2018). [source](https://profiles.wustl.edu/en/publications/market-intraday-momentum/)
- *peer-reviewed*: Baltussen, Da, Lammers and Martens (JFE 2021). [source](https://pure.eur.nl/en/publications/hedging-demand-and-market-intraday-momentum/)
- *preprint*: Barbon et al. (as summarized): leveraged-ETF rebalancing at the close is economically larger than... [source](https://alphaarchitect.com/hot-topic-does-gamma-hedging-actually-affect-stock-prices/)
- *anecdote*: A newsletter notes replications and contrary results exist for stocks rather than index ETFs... [source](https://harbourfrontquant.substack.com/p/does-intraday-momentum-exist-in-stock)

**Failure modes:** Index-level evidence; single stocks may not show it | Effect strongest in 1993-2013, weaker later (uncertain)

**Costs and feasibility at $1.2k:** SPY/SMH spreads around 1 bp; the constraint is PDT (about 3 day trades per 5 days). Not realistic as a frequent strategy: PDT allows ~3 day trades/week in a margin account under $25k, and a cash...

**Test plan:** Regress the last-30-minute return on the prior-close-to-10:00 return with 2+ years of 5-minute bars. Falsified if the coefficient is zero after 2018 or net per-trade return is negative.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 2, evidence 4, feasibility 2. 

**Adjusted for tonight's evidence:** Edge 2 to 1. trading-lab overnight 2026-10-28 (25 stocks plus SMH, 60 days of 5-minute bars, 2 years hourly): last-30-minute return on first-30-minute return slope 0.011 [-0.014, 0.036] pooled, consistent with zero. The open is about 3x noisier.

**In the arena (related variant):** `mom_0_7dte_1000` and `mom_0_7dte_0945` trade a different rule (strongest AI/semis mover 30 minutes after the open, held 1-7 days via options). The 09:45 twin measures the noisy open's cost.

See [00 Index](../00-index.md). Card: `knowledge/methods/intraday-momentum-first-last-half-hour.yaml`.
