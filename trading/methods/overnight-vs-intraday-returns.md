<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Overnight vs intraday return premium (tug of war)

> **TL;DR:** Descriptively robust, but costs eat the premium for daily churn; use it as a feature (avoid holding earnings gaps), not a strategy.
> **Source:** trading-lab method card knowledge/methods/overnight-vs-intraday-returns.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Descriptively robust, but costs eat the premium for daily churn; use it as a feature (avoid holding earnings gaps), not a strategy.

**Thesis:** A large share of equity returns accrue overnight, and the overnight/intraday split is persistent for stocks and strategies, so holding only overnight or only intraday can change risk-adjusted returns.

**Fit for AI/semis:** AI/semis names have big overnight gaps from earnings, Asian-session news and index futures, so the overnight leg carries most of the variance...

**Evidence** (quality label from the card):
- *peer-reviewed*: Lou, Polk and Skouras (JFE 2019): abnormal returns of momentum strategies accrue overnight while profits of other anomalies accrue intraday. [source](https://researchonline.lse.ac.uk/id/eprint/87481)
- *peer-reviewed*: McLean and Pontiff-type decay applies: an old, widely cited split should be expected to weaken; I found no clean cost-adjusted test of overnight-only SPY/semis in this session. [source](https://academicnewsletter.sufe.edu.cn/info/359722)
- *practitioner backtest*: Alpha Architect summary links overnight returns to momentum strategies and says intraday profits fall for other anomalies, with return gaps useful for forecasting. [source](https://alphaarchitect.com/2015/02/overnight-momentum-vs-intraday-momentum/)

**Failure modes:** Cost drag: daily round trip pays two spreads and open/close auction slippage | Overnight premium may just be compensation for gap risk | Opening-print prices from yfinance differ from what a retail order gets

**Costs and feasibility at $1.2k:** Two spreads per day plus auction slippage of 2-5 bps; a 0.5 bp/day edge disappears. Easy to place (whole shares, fits $1.2k) but a daily churn strategy that is nearly cost-negative; I would not run it live. Useful as a feature (e.g., avoid holding earnings gaps) rather than a strategy.

**Test plan:** Split daily returns into close-to-open and open-to-close for SPY, QQQ, SMH and the universe 2005-2026, 3 bps per leg. Falsified if overnight-only net Sharpe does not beat buy-and-hold.

**Status:** researched; implementability: now. **Scores (1-5, judgment):** edge 2, evidence 3, feasibility 3. The split is robust descriptively but I could not verify a post-2015, post-cost tradable premium.

**Not in the arena:** No book.

See [00 Index](../00-index.md). Card: `knowledge/methods/overnight-vs-intraday-returns.yaml`.
