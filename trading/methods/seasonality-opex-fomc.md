<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Calendar effects: pre-FOMC drift, OPEX week, turn-of-month

> **TL;DR:** Pre-FOMC drift reportedly vanished after 2015 and expected profit per event on $1.2k is a few dollars; a research curiosity only.
> **Source:** trading-lab method card knowledge/methods/seasonality-opex-fomc.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Pre-FOMC drift reportedly vanished after 2015 and expected profit per event on $1.2k is a few dollars; a research curiosity only.

**Thesis:** Equity returns are unusually high in the 24 hours before scheduled FOMC announcements and in options-expiration weeks, and around the turn of the month, because of risk-premium and hedging flows.

**Fit for AI/semis:** Semis have high beta to Fed-driven rate moves and large options open interest, so calendar effects could be amplified.

**Evidence** (quality label from the card):
- *peer-reviewed*: Lucca and Moench (JF 2015) documented large average equity excess returns in the 24 hours before scheduled FOMC announcements, with no corresponding effect in Treasuries or money-market futures. [source](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr512.pdf)
- *practitioner backtest*: Lucca and Moench themselves noted the drift had weakened in more recent data (consistent with arbitrage). [source](https://libertystreeteconomics.newyorkfed.org/2018/11/the-pre-fomc-announcement-drift-more-recent-evidence.html)
- *practitioner backtest*: Quantpedia summarizes a study of S&P 100 stocks finding high returns in option-expiration weeks (third-Friday week), concentrated in large caps with active options and linked to delta-hedge rebalancing (author attribution... [source](https://quantpedia.com/screener/details/102)
- *peer-reviewed*: McLean and Pontiff: published anomalies decay about 58% post-publication; calendar anomalies are especially visible and tradable at scale. [source](https://academicnewsletter.sufe.edu.cn/info/359722)

**Failure modes:** Drift disappeared after ~2015 | Only ~8 FOMC meetings/year: tiny sample and huge statistical noise | Turn-of-month and election-day effects not verified in this session

**Costs and feasibility at $1.2k:** 1-2 bps ETF spread against tens of bps of effect. Feasible with SPY/QQQ/SMH whole shares, but the expected profit per event on ~$1.2k is a few dollars; it is for research, not income.

**Test plan:** Event study of pre-FOMC and OPEX-week returns on SPY, QQQ, SMH, split 2000-2014 vs 2015-2026. Expect the later half to show little.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 1, evidence 3, feasibility 4. Pre-FOMC evidence suggests the effect has...

**Adjusted for tonight's evidence:** No score change. Tonight's hourly check found no OPEX-week volatility effect (range ratio 1.01 [0.90, 1.13], n=24), and FOMC had too few days to say.

**Not in the arena:** No book.

See [00 Index](../00-index.md). Card: `knowledge/methods/seasonality-opex-fomc.yaml`.
