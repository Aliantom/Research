<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# The wheel: cash-secured puts then covered calls

> **TL;DR:** Not feasible: one cash-secured put on a universe name needs $10,000 to $100,000+.
> **Source:** trading-lab method card knowledge/methods/wheel-csp-cc.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Not feasible: one cash-secured put on a universe name needs $10,000 to $100,000+.

**Thesis:** Selling cash-secured puts on stocks you would own earns premium, then assignment turns into a covered-call phase that keeps collecting premium.

**Fit for AI/semis:** Not feasible on most of the AI/semis universe. NVDA, AVGO, TSM, ASML, MU, AMAT, LRCX, MSFT, META, etc.

**Evidence** (quality label from the card):
- *marketing*: A cash-secured put on a $100 strike requires $10,000 in a tastytrade cash account (strike x 100). [source](https://tastytrade.com/learn/accounts/margin-vs-cash-accounts/)
- *peer-reviewed*: Israelov/Nielsen: covered calls (the second wheel leg) are equivalent to being long stock plus short volatility. [source](https://www.aqr.com/-/media/AQR/Documents/Insights/Journal-Article/FAJ-Covered-Call-Strategies-One-Fact-and-Eight-Myths.pdf)
- *peer-reviewed*: Put-writing historically earned strong index returns with crash-linked losses (Bondarenko summary), but Broadie/Chernov/Johannes show the put alpha is statistically insignificant after accounting for tail sampling error. [source](https://www.cxoadvisory.com/equity-options/is-40-per-month-shorting-index-puts-a-fair-return)
- *anecdote*: I found no independent post-cost backtest of the single-stock 'wheel' on high-volatility growth stocks; popular material is anecdotal or promotional. [source](https://www.cxoadvisory.com/equity-options/is-40-per-month-shorting-index-puts-a-fair-return)

**Failure modes:** Growth/semis drawdowns of 30-50% are common; premium collected is small versus these | Capital lock-up: one contract ties the whole account | Early assignment of puts at dividends or deep ITM

**Costs and feasibility at $1.2k:** Commissions are trivial; thin-option spreads are the economic cost. Basically not feasible: the universe's shares cost $100-$1000+, so a 1-lot CSP needs $10,000-$100,000+.

**Test plan:** No trading test at $1.2k. Paper-only once the account passes about $15k: simulate 0.25-delta puts on one name for 12 months against buy-and-hold.

**Status:** researched; implementability: not feasible. **Scores (1-5, judgment):** edge 1, evidence 2, feasibility 1. Feasibility could change for a rare sub-$12 name; edge in a rising AI-capex market could look better than the long-run premium evidence...

**Not in the arena:** Not feasible.

See [00 Index](../00-index.md). Card: `knowledge/methods/wheel-csp-cc.yaml`.
