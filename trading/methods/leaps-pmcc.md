<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# LEAPS and poor-man's covered calls

> **TL;DR:** Not tradable at $1.2k: a deep in-the-money LEAPS on any universe name costs more than the account.
> **Source:** trading-lab method card knowledge/methods/leaps-pmcc.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Not tradable at $1.2k: a deep in-the-money LEAPS on any universe name costs more than the account.

**Thesis:** A deep in-the-money long-dated call replicates stock exposure with less capital and defined loss, and selling short-dated OTM calls against it can add income (PMCC).

**Fit for AI/semis:** Good thesis fit for a long AI-capex view, but the per-share prices ($100-$1000) make deep ITM LEAPS very expensive.

**Evidence** (quality label from the card):
- *peer-reviewed*: Israelov/Nielsen: covered-call-type structures give equity beta plus a short-volatility exposure; the extra return versus the stock is the volatility risk premium only when implied exceeds realized, and they dispel the... [source](https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/FAJ-Covered-Call-Strategies-One-Fact-and-Eight-Myths.pdf)
- *peer-reviewed*: Coval/Shumway: call returns rise with strike and exceed the underlying; deep ITM calls have lower leverage and dollar-vega, so a LEAPS substitute carries the stock's expected return with extra option... [source](https://scholarsarchive.byu.edu/facpub/9281)
- *marketing*: Practitioner guidance: LEAPS leg delta >= 0.75-0.80, short call 30-45 DTE at 0.20-0.40 delta; Option Alpha implements PMCC as a call diagonal with a ~150 DTE long call. [source](https://optionalpha.com/learn/poor-mans-covered-call)
- *marketing*: A worked example puts the net debit at about one-fifth of the stock purchase cost with max loss equal to the debit (illustrative, not historical). [source](https://www.optionsplaybook.com/blogs/poor-mans-covered-call-how-to-run-a-covered-call-strategy-for-less-capital)

**Failure modes:** Short-call early assignment before ex-dividend; must roll or exercise | Wide spreads on LEAPS for mid-liquidity names | Stock falls: LEAPS loses time value and delta, short call profit is...

**Costs and feasibility at $1.2k:** LEAPS bid/ask is the real cost, 1-5% of premium per side. Mostly not feasible. A 0.80-delta 12-month call on a $150 stock costs ~$4,500 and on NVDA/AVGO/ASML far more.

**Test plan:** Do not trade at $1.2k. Simulate 0.75-delta LEAPS plus short calls against the stock with Black-Scholes, then forward chain snapshots; compare return per unit of max loss.

**Status:** researched; implementability: needs money. **Scores (1-5, judgment):** edge 2, evidence 2, feasibility 1. If a handful of lower-priced universe names exist, a single tiny LEAPS could be possible.

**Not in the arena:** Not feasible at this size.

See [00 Index](../00-index.md). Card: `knowledge/methods/leaps-pmcc.yaml`.
