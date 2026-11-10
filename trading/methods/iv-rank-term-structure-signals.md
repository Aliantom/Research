<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# IV rank, term-structure and skew/spread signals as return predictors

> **TL;DR:** Option-implied signals predicted returns in broad cross-sections, but the effect fades after 2008, partly reflects borrow fees and is insignificant in 2023-26 mega-caps: filters at best, edge 1.
> **Source:** trading-lab method card knowledge/methods/iv-rank-term-structure-signals.yaml (deep pass 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict:** Real in the academic cross-section, weakest where we trade (liquid mega-caps). Edge 2 to 1, evidence 4 to 3.

**New evidence (deep pass):**
- *Contrary, 2026 re-test (arXiv 2608.26115):* 10,026 underlyings, 2015-2026. The skew coefficient falls from t=-5.5 to t=-1.5 in the AI/mega-cap period, but the Cremers-Weinbaum call-put IV spread stays significant.
- Honarvar and Howard (summary via OptionMetrics): signals worked 1996-2008, declined afterwards, and a non-synchronous-data look-ahead bias inflated early results.
- Muravyev, Pearson and Pollet (JFE 2025): predictability falls by at least two-thirds once stock borrow fees are removed; megacaps have cheap borrow.
- Still in the card: Cremers-Weinbaum, Vasquez, Goyal-Saretto. No peer-reviewed test exists for IV rank as a timing filter.

**Test plan (frozen):** from 2026-10-29, one sample per day at the last snapshot before 15:45 ET for 25 single names. Signals: IV30/RV20 (IV rank only after 252 days, so not before 2027-10), call-put IV spread, 25-delta skew, 60d-30d slope; earnings-contaminated expiries masked. Targets: next 5-day and 21-day excess return vs SMH, and net straddle P&L (buy at ask, sell at bid a week later). Statistic: weekly mean of the daily cross-sectional Spearman IC with a week-block bootstrap, 8 tests so Benjamini-Hochberg at 10%.

**Power:** with 25 names, an IC of 0.05 needs about 60 independent weeks, so a 26-week read can only reject large effects. Earliest real verdict is around November 2027.

**Decision:** promote a signal to a filter only if its IC has the pre-stated sign, the corrected CI excludes zero, |IC| is at least 0.05, it holds in both halves, and the top-minus-bottom tercile difference is positive after costs. Never trade standalone at $1.2k.

**Status:** researched-deep; implementability: needs data. **Scores:** edge 1, evidence 3, feasibility 3.

See [00 Index](../00-index.md). Card: `knowledge/methods/iv-rank-term-structure-signals.yaml`.
