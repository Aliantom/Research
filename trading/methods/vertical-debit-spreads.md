<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Vertical debit spreads (defined-risk directional)

> **TL;DR:** Feasible and a sensible way to express a directional view, but the spread only adds friction unless the underlying signal has an edge, which is unproven.
> **Source:** trading-lab method card knowledge/methods/vertical-debit-spreads.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Feasible and a sensible way to express a directional view, but the spread only adds friction unless the underlying signal has an edge, which is unproven.

**Thesis:** Buying a call/put spread cuts premium and vega versus a naked long option, letting you express a directional view with a known max loss and less IV-crush exposure.

**Fit for AI/semis:** Good fit: high-priced AI/semis stocks (NVDA, AVGO, ASML, ANET, ETN) make single long options expensive.

**Evidence** (quality label from the card):
- *peer-reviewed*: Coval/Shumway: call returns exceed the underlying and rise with strike, while ATM straddles lose about 3% per week; i.e. [source](https://scholarsarchive.byu.edu/facpub/9281)
- *peer-reviewed*: Retail multi-leg strategies earned negative returns on average and losses grew with complexity (secondary summary of retail option studies), a caution that defined-risk structure alone does not create edge. [source](https://quantpedia.com/how-retail-losses-money-in-option-trading/)
- *peer-reviewed*: Muravyev/Pearson: effective spreads are lower than quoted for traders who time execution, so working limit orders on spreads (paying near mid) can reduce frictions materially. [source](https://ideas.repec.org/a/oup/rfinst/v33y2020i11p4973-5014..html)

**Failure modes:** Wide bid-ask on both legs doubles friction vs a single option | Buying spreads after the move into elevated IV overpays | Directional call must be right and large enough to exceed the break-even...

**Costs and feasibility at $1.2k:** $2 to open; combined bid/ask on two legs is the main cost. Feasible. A $5-wide spread on a $100-300 stock costs ~$150-$350, so 2-4 positions fit. $10-wide spreads on NVDA/AVGO-class names would cost $400-$600 and are too concentrated. Max loss is known at entry.

**Test plan:** Paper-trade 45 DTE 0.60/0.30 delta call spreads on trending names (debit under 45% of width), exit at 60% profit or 14 DTE, against equal capital-at-risk in shares.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 2, evidence 2, feasibility 4. Value depends wholly on the underlying signal; if the signal has no edge the spread only adds frictions.

**In the arena:** `swing_vertical`, the same book as the swing-catalyst card.

See [00 Index](../00-index.md). Card: `knowledge/methods/vertical-debit-spreads.yaml`.
