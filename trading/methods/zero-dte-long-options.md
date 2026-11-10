<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# 0-7 DTE directional long calls/puts on single names

> **TL;DR:** Feasible and closest to the owner's style, but the lowest-expectancy approach here: the buyer pays the variance premium plus spread, so it is a lottery sleeve measured against a random control.
> **Source:** trading-lab method card knowledge/methods/zero-dte-long-options.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict:** Feasible and closest to the owner's own style, but the lowest-expectancy approach in the file: the buyer pays the variance premium plus spread, so it is a lottery sleeve measured against a random control.

**Thesis:** Very short-dated long options give maximum convexity per dollar, so a correct call on a catalyst day can return several multiples of a ~$100 premium.

**Fit for AI/semis:** High-beta AI/semis names move 3-8% on news, which suits convexity.

**Evidence** (quality label from the card):
- *preprint*: Retail traders in S&P 500 0DTE options lost money on average in Jan 2021-Feb 2023 (about $358k/day after daily expiries... [source](https://www.bnnbloomberg.ca/day-traders-lose-358-000-per-day-gambling-on-zero-day-options-1.1910634)
- *preprint*: Beckmeyer/Branger/Gayda paper (SSRN 4404704) is the primary source; I could only read abstract-level summaries, not the full text. [source](https://cxoadvisory.com/individual-investing/retail-0dte-option-trader-performance)
- *preprint*: Retail investors lose roughly 5-9% around earnings announcements, 10-14% for high expected-volatility events, with average bid-ask spreads near 20% of... [source](https://quantpedia.com/how-retail-losses-money-in-option-trading/)
- *preprint*: Almeida/Freire/Hizmeri find a large variance risk premium in 0DTEs (long-option buyers pay it) and that a strategy exploiting pricing-bound violations... [source](https://tinbergen.nl/event/2025/11/06/13089/0dte-asset-pricing)
- *preprint*: Contrary: a HKUST summary says 0DTEs are expensive but not mispriced. [source](https://bm.hkust.edu.hk/bizinsight/2026/04/are-0dte-options-mispriced)

**Failure modes:** Wide bid-ask on weeklies; round trip can cost 5-20% of premium | IV crush after the catalyst even if direction is right

**Costs and feasibility at $1.2k:** Spread dominates: 5-20% of premium round trip; $1.12 per contract to open. Mechanically feasible: a $60-$300 premium per contract fits a $1.2k account, and you can have 3-5 open at once.

**Test plan:** Forward paper test: 0.30-0.40 delta, 2-5 DTE, on tagged catalyst days, exit at +100% or end of next session. Falsified if the mean over 60 trades net of ask-in/bid-out fills is zero or negative.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 1, evidence 4, feasibility 3. 

**In the arena:** The `mom_0_7dte_*`, `pulse_*` and `llm_pick_0_7dte` books all buy 1-7 DTE long options (about 2% OTM, max premium $250), and `random_0_7dte` is the luck control. Registry minimum is 1 DTE, so no true 0DTE.

See [00 Index](../00-index.md). Card: `knowledge/methods/zero-dte-long-options.yaml`.
