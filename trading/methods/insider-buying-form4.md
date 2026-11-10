<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Insider open-market purchases (SEC Form 4)

> **TL;DR:** Opportunistic insider buying has a real academic edge, but mega-cap AI insiders almost never buy, so there will be too few events to trade or even test.
> **Source:** trading-lab method card knowledge/methods/insider-buying-form4.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Opportunistic insider buying has a real academic edge, but mega-cap AI insiders almost never buy, so there will be too few events to trade or even test.

**Thesis:** Open-market purchases by officers and directors, especially opportunistic and clustered ones, predict positive abnormal returns over the following months.

**Fit for AI/semis:** Poor fit: executives at NVDA, MSFT, GOOGL, META, AMZN, AVGO overwhelmingly sell via scheduled 10b5-1 plans and almost never make open-market purchases....

**Evidence** (quality label from the card):
- *peer-reviewed*: Cohen, Malloy and Pomorski: splitting insiders into routine (same-month pattern) and opportunistic trades, opportunistic portfolios earn about 82 bps/month value-weighted abnormal return (1986-2007) while routine trades earn about zero. [source](https://www.nber.org/papers/w16454)
- *peer-reviewed*: Lakonishok and Lee (RFS 2001): studied insider trades 1975-1995; insider purchases carry more information than sales and information is stronger in small stocks (specific figures not verified here). [source](https://www.nber.org/papers/w6656)
- *practitioner backtest*: Practitioner summaries say clustered buys and CFO/CEO buys are stronger; I found no 2020s peer-reviewed confirmation and the figures come from blogs. [source](https://www.interactivebrokers.com/campus/traders-insight/securities/stocks/what-corporate-insider-buying-can-tell-investors-evidence-from-academic-research/)

**Failure modes:** Event scarcity in mega-cap AI names | Filing lag up to 2 business days; the price may already have moved | Distinguishing routine vs opportunistic needs a 3+ year history per insider

**Costs and feasibility at $1.2k:** Normal stock costs; entry at the next open after the filing. Feasible if events exist, but you would be waiting for rare events; 1-2 positions of ~$600 each. Not a daily-activity system.

**Test plan:** Pull Form 4 code-P purchases 2010-2026 for the universe plus wider semis, enter at the next open, hold 63 days vs SMH. First count events; falsified at once if there are too few.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 2, evidence 3, feasibility 3. Likely too few qualifying events in the owner's universe to ever be statistically testable.

**Not in the arena:** Events too rare for a forward book.

See [00 Index](../00-index.md). Card: `knowledge/methods/insider-buying-form4.yaml`.
