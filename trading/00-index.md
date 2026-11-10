<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Trading methods ranked for a $1.2k AI/semis account

> **TL;DR:** No method in the 27-card library has proven edge at $1.2k; best bets are AI/semis rotation and trend/regime overlays (both bias-prone); premium selling, LEAPS, pairs and the wheel fail.
> **Source:** trading-lab method cards knowledge/methods/*.yaml, backtests/summary.md, time_of_day.yaml, arena/registry.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

Library: 29 method cards (27 in the main ranking, 2 in "Added later" below) from trading-lab overnight 2026-10-28 (see 2026-10-28 Overnight trading lab prompt and Trading brain brief). One note per method is in `methods/`.

**Read this first.** Almost every edge here is unproven. The card scores (1-5 each for edge, evidence, feasibility) are one model's judgment from web research, often abstract-level reading and vendor-written sources, not measurements. The only numbers we computed ourselves are the equity/ETF backtests and the 60-day time-of-day study, and those cover a single AI/semis bull-dominated window (2024-07..2026-10). SMH buy-and-hold (39.2% CAGR, Sharpe 1.03 in that window) is a hard bar for anything long. Per the backtest summary, any outperformance vs SMH is "only plausible, not proven".

## How the ranking works

Combined score = edge x evidence x feasibility (max 125), using the card scores except where tonight's results changed them (marked "a to b" in the edge column). Ties are broken by: already in the paper arena, then testable with free data now, then the rest. The "evidence" score measures how much solid evidence exists, in either direction, so strong evidence of a negative edge (0DTE long options, earnings straddles) still scores high there; the low edge score is what pushes those methods down. Treat differences of a few points as noise.

Adjustments made (and why):
- Time-series momentum, regime filter, leveraged-ETF swing: edge 3 to 2. The chosen SMH 200-day plus VIX<20 trend rule returned -2.1% CAGR (Sharpe 0.10, max drawdown -41.7%) in the confirm window against SMH 39.2%, with DSR 0.17 on confirm (trading-lab overnight 2026-10-28).
- Intraday momentum: edge 2 to 1. First 30 minutes did not predict the last 30 minutes in 25 AI/semis stocks plus SMH over 60 days (slopes consistent with zero); the open is about 3x noisier than other half hours.
- Cross-sectional rotation: not adjusted. It is the only backtest that beat SMH (Sharpe 1.43, CAGR 103.6%, DSR 0.85 on confirm) but the universe is today's winners and PBO was 0.81 on the select window, so the score stays at the card's 3.

## Ranking

| Rank | Method | Edge | Evidence | Feasibility | Combined | Status | Rationale |
|---|---|---|---|---|---|---|---|
| 1 | [cross-sectional-momentum-rotation](methods/cross-sectional-momentum-rotation.md) | 3 | 3 | 4 | 36 | in arena (`rotation_top3`); backtested | Only candidate that beat SMH in the confirm window (Sharpe 1.43 vs 1.03), but survivorship-biased and PBO 0.81 on the select window; 2-3 positions at $1.2k. |
| 2 | [regime-filter-markov](methods/regime-filter-markov.md) | 3 to 2 | 3 | 5 | 30 | in arena (via `trend_regime_soxl`); backtested, not supported | Costless overlay, but the tested SMH 200-day plus VIX rule lagged (-2.1% CAGR vs 39.2%) and did not cut drawdown. |
| 3 | [time-series-momentum-semis](methods/time-series-momentum-semis.md) | 3 to 2 | 3 | 5 | 30 | backtested, not supported | Same overnight backtest; DSR on confirm 0.17. One AI bull window is one draw, so not dead, just unproven. |
| 4 | [leveraged-etf-swing](methods/leveraged-etf-swing.md) | 3 to 2 | 3 | 4 | 24 | in arena (`trend_regime_soxl`) | Only dollar-efficient semis exposure at $1.2k, but SOXL buy-and-hold drew down -87.9%; the registry flags the filter as unsupported. |
| 5 | [iv-rank-term-structure-signals](methods/iv-rank-term-structure-signals.md) | 2 | 4 | 3 | 24 | plausible only | Free to compute and a useful filter, but cross-sectional evidence on thousands of stocks does not transfer to 27 names; needs 6-12 months of snapshots. |
| 6 | [social-attention-reddit-stocktwits](methods/social-attention-reddit-stocktwits.md) | 2 | 3 | 3 | 18 | in arena (`pulse_*`) | Cheap forward test; the WallStreetBets signal reportedly died after 2021 and there is no history. |
| 7 | [overnight-vs-intraday-returns](methods/overnight-vs-intraday-returns.md) | 2 | 3 | 3 | 18 | plausible only | Robust descriptively, but daily churn costs eat the premium; a feature (avoid gaps), not a strategy. |
| 8 | [insider-buying-form4](methods/insider-buying-form4.md) | 2 | 3 | 3 | 18 | plausible only | Real academic edge, but mega-cap AI insiders rarely buy, so too few events. |
| 9 | [swing-catalyst-options](methods/swing-catalyst-options.md) | 2 | 2 | 4 | 16 | in arena (`swing_vertical`) | One of the few feasible defined-risk plans, but one correlated AI bet with no historical chains. |
| 10 | [vertical-debit-spreads](methods/vertical-debit-spreads.md) | 2 | 2 | 4 | 16 | in arena (`swing_vertical`) | Feasible; adds friction unless the underlying signal has edge, and it is unproven. |
| 11 | [earnings-straddle-ivcrush](methods/earnings-straddle-ivcrush.md) | 2 | 4 | 2 | 16 | in arena (`earnings_ironfly`, short side only) | Long straddles unaffordable and lose on bid/ask; the feasible short iron fly is marginal and tail-exposed. Evidence is mixed by season. |
| 12 | [calendars-diagonals](methods/calendars-diagonals.md) | 2 | 2 | 4 | 16 | plausible only | Affordable, but no direct evidence on calendar P&L and the print collapses back-month IV too. |
| 13 | [zero-dte-long-options](methods/zero-dte-long-options.md) | 1 | 4 | 3 | 12 | in arena (`mom_0_7dte_*`, `random_0_7dte` control) | Owner style and feasible, but the buyer pays the variance premium plus 5-20% spread; evidence score 4 reflects strong evidence of a negative edge. |
| 14 | [ai-supply-chain-lead-lag](methods/ai-supply-chain-lead-lag.md) | 2 | 2 | 3 | 12 | plausible only | Plausible mechanism, but public data on the most-watched names and decaying customer-momentum edge; cheap free test available. |
| 15 | [event-driven-8k](methods/event-driven-8k.md) | 2 | 2 | 3 | 12 | plausible only | Tradable remainder after the first reaction is small and shrinking. |
| 16 | [index-0dte-spx-xsp](methods/index-0dte-spx-xsp.md) | 1 | 3 | 4 | 12 | plausible only | Only 0DTE vehicle that fits, but the best evidence says net edge near zero. |
| 17 | [seasonality-opex-fomc](methods/seasonality-opex-fomc.md) | 1 | 3 | 4 | 12 | plausible only | Pre-FOMC drift reportedly gone after 2015; effect is a few dollars per event on $1.2k. |
| 18 | [post-earnings-drift](methods/post-earnings-drift.md) | 1 | 3 | 3 | 9 | plausible only | Drift gone in large caps per the main paper; no surprise data. |
| 19 | [butterflies-pinning](methods/butterflies-pinning.md) | 1 | 3 | 3 | 9 | plausible only | Cheap lottery; pinning evidence stops in 2002, fees heavy. |
| 20 | [intraday-momentum-first-last-half-hour](methods/intraday-momentum-first-last-half-hour.md) | 2 to 1 | 4 | 2 | 8 | in arena (related variant, `mom_0_7dte_*`) | Index-ETF literature is strong, but tonight's 60-day AI/semis test found slopes near zero; PDT blocks frequent day trades. |
| 21 | [llm-multi-agent-trading](methods/llm-multi-agent-trading.md) | 1 | 2 | 4 | 8 | in arena (`llm_pick_0_7dte`) | Papers are short-window and leak-prone; the arena twin tests it against its rules-based sibling. |
| 22 | [short-premium-45dte-manage-21](methods/short-premium-45dte-manage-21.md) | 2 | 2 | 2 | 8 | plausible only | Needs many independent positions; $1.2k fits 2-3, with negative skew. |
| 23 | [unusual-options-flow](methods/unusual-options-flow.md) | 1 | 3 | 2 | 6 | plausible only | Needs paid trade-level data; retail flow is noise or contrarian. |
| 24 | [iron-condor-credit-spreads](methods/iron-condor-credit-spreads.md) | 1 | 2 | 2 | 4 | plausible only | Poor fit for gap-prone AI names; XSP/SPY versions add little. |
| 25 | [leaps-pmcc](methods/leaps-pmcc.md) | 2 | 2 | 1 | 4 | not feasible | Deep-ITM LEAPS cost more than the account. |
| 26 | [pairs-relative-value](methods/pairs-relative-value.md) | 1 | 3 | 1 | 3 | not feasible | Shorting, two legs and discrete shares at $1.2k; NVDA-vs-SMH is partly an identity. |
| 27 | [wheel-csp-cc](methods/wheel-csp-cc.md) | 1 | 2 | 1 | 2 | not feasible | A 1-lot cash-secured put needs $10k-$100k+. |

Status key: "in arena" means a pre-registered paper book starts 2026-10-29 (`arena/registry.yaml`, starting cash $1,199.67 per book); "backtested" means tonight's daily-bar tests; "plausible only" means no test yet; "not feasible" means the account size rules it out.

## What we'd need to test the rest

Cost figures come from the pricing research of 2026-10-28 (`paid-data-and-x-pricing.md`); nothing was bought, and the figures are unverified in places. Time estimates are rough guesses.

| Need | Unlocks | Cost | Time |
|---|---|---|---|
| Historical option chains. Candidates: ThetaData Options Value ~$40/month (6 years, 1-minute; whether end-of-day greeks/IV are in this tier is unverified), Massive Developer $79/month (4 years, 15-minute delayed), ORATS Delayed $199 for one month (EOD chains with greeks back to 2007; data-retention licence unchecked) | [iron-condor-credit-spreads](methods/iron-condor-credit-spreads.md), [short-premium-45dte-manage-21](methods/short-premium-45dte-manage-21.md), [calendars-diagonals](methods/calendars-diagonals.md), [vertical-debit-spreads](methods/vertical-debit-spreads.md), [swing-catalyst-options](methods/swing-catalyst-options.md), [earnings-straddle-ivcrush](methods/earnings-straddle-ivcrush.md), [butterflies-pinning](methods/butterflies-pinning.md), [iv-rank-term-structure-signals](methods/iv-rank-term-structure-signals.md), [leaps-pmcc](methods/leaps-pmcc.md) | $40-$200 for a one-off pull | 1-2 days to build a bid/ask-fill backtester |
| Free-data tests, runnable now on daily bars, EDGAR and hourly bars | [overnight-vs-intraday-returns](methods/overnight-vs-intraday-returns.md), [post-earnings-drift](methods/post-earnings-drift.md) (proxy surprise), [insider-buying-form4](methods/insider-buying-form4.md), [ai-supply-chain-lead-lag](methods/ai-supply-chain-lead-lag.md), [event-driven-8k](methods/event-driven-8k.md), [seasonality-opex-fomc](methods/seasonality-opex-fomc.md), [butterflies-pinning](methods/butterflies-pinning.md) (daily-close clustering) | $0 | Hours each |
| A point-in-time universe (what was large in AI/semis each year, plus delisted names) | Honest versions of [cross-sectional-momentum-rotation](methods/cross-sectional-momentum-rotation.md) and [time-series-momentum-semis](methods/time-series-momentum-semis.md) | Not priced; free proxies are imperfect | Days |
| Forward logging only (no history exists) | [iv-rank-term-structure-signals](methods/iv-rank-term-structure-signals.md) (6-12 months of daily chain snapshots), [social-attention-reddit-stocktwits](methods/social-attention-reddit-stocktwits.md) (100+ spike events), [llm-multi-agent-trading](methods/llm-multi-agent-trading.md) (60+ decision days, about 3 months), [unusual-options-flow](methods/unusual-options-flow.md) proxy (about 6 months) | $0, plus inference cost | Months |
| Arena results | Everything marked "in arena"; the brief asks for 1-2 weeks and a minimum trade count before benchmarking against SMH | $0 | 2+ weeks, likely more for 30-60 trade falsification rules |
| Trade-level options flow with open/close labels | [unusual-options-flow](methods/unusual-options-flow.md) properly | $50-$200/month for alerts (card); Unusual Whales API $99-$150 is flow, not chains | Not worth it at this account size |
| A larger account (about $15k+ per the wheel card) | [wheel-csp-cc](methods/wheel-csp-cc.md), [leaps-pmcc](methods/leaps-pmcc.md), and comfortable [pairs-relative-value](methods/pairs-relative-value.md) | n/a | n/a |
| Analyst consensus or tick data around events | Proper [post-earnings-drift](methods/post-earnings-drift.md) and [event-driven-8k](methods/event-driven-8k.md) | Not priced in tonight's research | Unknown |

## Contrary evidence

- The trend/regime idea, which the cards rated as the best fit, lost to buy-and-hold in the one window we tested it on; the select-window winner looked good in-sample (DSR 0.83) and collapsed on confirm (DSR 0.17).
- Rotation looks strong but is flattered by hindsight: the universe is names that won, and one CSCV check on the select window gave PBO 0.81. The select window is about 2.5 years and the 41 trials are highly correlated, so the effective trial count is lower than 41 and a high DSR does not mean the edge is real.
- All long strategies were tested in one AI bull regime. SOXL buy-and-hold made 30.3% CAGR but drew down -87.9%.
- Intraday momentum is a strong index-ETF result (Gao et al., JFE 2018) that tonight's 60-day sample could not reproduce for AI/semis stocks. Sixty days is short, so this is "not supported here", not "refuted".
- Published anomalies lose roughly 58% of their return after publication (McLean and Pontiff), which hits momentum, PEAD, seasonality and customer-momentum cards alike.
- Option buying is on the wrong side of the variance premium: retail loses 5-9% around earnings (de Silva, Smith, So) and long earnings straddles lost ~18.5% per trade in a vendor bid/ask study (iVolatility), while ORATS reports realized moves above implied in the Feb 2026 season. Which side wins flips by season, and these are vendor-authored samples on S&P 500 names, not AI/semis.
- Only the open's noise is solid: the first 30 minutes show about 3.2x the range of other half hours. Whether option spreads follow the same shape is untested until the first chain snapshots arrive.

## Added later the same night (from verified swarm leads)

| Method | Edge | Evidence | Feasibility | Combined | Status | Rationale |
|---|---|---|---|---|---|---|
| [gpu-rental-price-leadlag](methods/gpu-rental-price-leadlag.md) | 2 | 1 | 3 | 6 | needs data (collect daily from now) | Free daily GPU-rental indices exist (two community repos, short history); a plausible lead indicator for CRWV/SMCI/NVDA with no published test. |
| [earnings-iv-rv-screen](methods/earnings-iv-rv-screen.md) | 2 | 2 | 3 | 12 | in arena (`earnings_ironfly`) | Earnings straddles are expensive on average (student study, ~9.8k events); IV30/RV30 and term-slope screens are cheap to log from our chains. |

## Deep pass (06:20): score changes after more primary and contrary evidence

| Method | Edge | Evidence | Feasibility | What changed |
|---|---|---|---|---|
| [cross-sectional-momentum-rotation](methods/cross-sectional-momentum-rotation.md) | 3 → 2 | 3 | 4 | Momentum crashes hit concentrated books hardest; cost studies cover decile books, not 3 names; ~120 months only detects ~9%/yr excess. Still in the arena. |
| [regime-filter-markov](methods/regime-filter-markov.md) | 3 → 2 | 3 | 5 | MA-timing gains inflated by data mining (Zakamulin); trend rules trail buy-and-hold in bull runs; our own confirm-window loss. |
| [iv-rank-term-structure-signals](methods/iv-rank-term-structure-signals.md) | 2 → 1 | 4 → 3 | 3 | Skew signal insignificant in 2023–26 mega caps; ≥ 2/3 of IV-spread predictability is borrow fees (JFE 2025); IV rank needs ~1 year of our own chains. |
| [swing-catalyst-options](methods/swing-catalyst-options.md) | 2 | 2 | 4 → 3 | Long premium has a negative baseline; retail spreads wide; 30 trades is only a futility screen, a pass needs 60+. |
| [earnings-iv-rv-screen](methods/earnings-iv-rv-screen.md) | 2 | 2 | 3 | HV−IV doesn't predict straddle returns, but implied move vs the name's own earnings-move history does (Milian 2023): primary signal switched. |
| [social-attention-reddit-stocktwits](methods/social-attention-reddit-stocktwits.md) | 2 → 1 | 3 | 3 | Attention spikes tend to reverse (JFE 2024, JF 2022); WSB picks showed no alpha; 100 events detect only ~0.5% d+1. |

Read the ranking above with these changes: the top of the list is now "cheap to test, weak expected edge", which is why the arena measures rather than bets.
