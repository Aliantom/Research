<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Swarm findings (verified only)

> **TL;DR:** 34 Sonnet-verified leads from the overnight local research swarm; top-40 precision 12.5-27.5%, and a blind A/B leaned to rubric v3 (4/20 vs 1/20, p≈0.17).
> **Source:** trading-lab local research swarm (gemma4:12b-cool16k, 2026-10-28 overnight); every lead below was opened and checked by a Sonnet verifier; unverified local-model output is excluded  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

Local models made the leads; a hosted model opened each source and checked it. Only `verified_useful` items appear here. Many are tools or ideas to test, **not evidence of edge**. Licences come from the repo, not the model.

## Data sources
- **GPU rental price indices** (AI-demand alternative data): [gpu-price-index](https://github.com/ewyluda/gpu-price-index), daily index from 11 public sources (MIT, short history), and [compute-screener](https://github.com/renshuBTC/compute-screener), daily GPU rental + AI token prices (data CC BY 4.0, code proprietary). Use both, cross-checked, as a candidate lead indicator for NVDA/CRWV/SMCI. Untested.
- **SEC EDGAR official JSON APIs** ([docs](https://www.sec.gov/edgar/sec-api-documentation)): submissions, companyfacts and frames, no key; plus [edgartools](https://github.com/dgunning/edgartools) (MIT, active) for 8-K/Form 4/13F parsing and [pibou-filings](https://github.com/Pierre-Bouquet/pibou-filings) (13F/N-PORT/Form 3-4-5 into DuckDB; non-commercial licence). Feeds the insider-buying and event-driven cards.
- **[TeraflopAI/SEC-EDGAR](https://huggingface.co/datasets/TeraflopAI/SEC-EDGAR)**: 8M dated filings (Apache-2.0, 590 GB; subset by form type) for text-signal tests.
- **[yfinance-cache](https://github.com/ValueRaider/yfinance-cache)** (MIT, by the yfinance maintainer): a split/dividend-aware cache, to stop hammering Yahoo.

## Methods and screens to test (earnings/IV)
- **Earnings IV30/RV30 + term-structure screens**: [Earnings-Volatility-Calculator](https://github.com/Acelogic/Earnings-Volatility-Calculator) and [volatility-vibes](https://github.com/MattNeto928/volatility-vibes-options-strategy) (IV30/RV30 ≥ 1.25, negative term slope). Both unbacktested; test them on our forward-logged chains around this window's earnings (AMD, ARM, SMCI, ANET, AMAT).
- **Forward factor for calendars**: [TastyFwdFactor](https://github.com/alex-cartwright1/TastyFwdFactor) (MIT; tastytrade data) and [forward-volatility-calculator](https://github.com/olihacuk/forward-volatility-calculator). Candidate signal for the calendars card.
- **Earnings straddle mispricing study** ([repo](https://github.com/unniananya/Earnings-Implied-Move-Mispricing)): ~9.8k straddles 2018–2024; straddles were expensive on average (negative edge for buyers), with some predictable mispricing. Contrary evidence for buying earnings straddles.
- **[volatility-trading-dashboard](https://github.com/larsfjoh/volatility-trading-dashboard)**: vol cone, 5 realized-vol estimators, implied vs realized earnings-move history (MIT; yfinance).

## Honest-evaluation tooling
- **[financial-ml-toolkit](https://github.com/younis-y/financial-ml-toolkit)**: López de Prado toolchain (CPCV, deflated Sharpe), MIT; states plainly it has no strategy edge.
- **[glassbench](https://github.com/davidalmeida90/glassbench)**: runs TradingAgents and AI Hedge Fund with next-open fills, costs and **shuffled-rating placebo** backtests (Apache). A placebo control like our random book, worth copying for the LLM book.
- **[quantarena-clean](https://github.com/Dominic789654/quantarena-clean)**: LLM trading mandates over 226 live days; an equal-weight baseline beat the active mandates. More contrary evidence for LLM stock-picking.
- **[ACE](https://github.com/ace-agent/ace)** (arXiv 2510.04618): generator/reflector/curator "playbook" method; design input for `knowledge/lessons.yaml`.

## Added from batch 3 (rubric v3)
- **[gammagrid](https://github.com/gammagrid/gammagrid)**: collects option-chain snapshots into Postgres; AGPL, so copy the pattern, not the code. Our `tradinglab chains` already forward-logs tastytrade chains.
- **Conformal prediction for trading signals**: [EnbPI](http://arxiv.org/abs/2010.09107) (implemented in the MAPIE library) and [Conformal PID control](http://arxiv.org/abs/2307.16895) (code available): calibrated intervals under drift, a candidate for sizing or no-trade filters.
- **[Pooled ML for intraday realized volatility](http://arxiv.org/abs/2202.08962)** with time-of-day effects: needs intraday bars (partly free).
- **[Share-buyback announcements thesis](http://arxiv.org/abs/2209.12863)**: 57k announcements; ≥1%-of-market-cap buybacks outperformed (unreviewed, data-mined: a seed topic only).
- **Security note:** one lead (`Shannonhomeward768/gammagrid`) was a malware-style copy of gammagrid whose README pushes a Windows installer. The swarm never downloads or runs anything (executables and archives are refused by design), so it was only read; never install from swarm leads without checking the publisher.

## Added from batch 4 (rubric v1 re-run)
- **[Pricing event risk: concave pre-earnings IV curves](https://www.sfi.ch/en/publications/n-21-48-pricing-event-risk-evidence-from-concave-implied-volatility-curves)** (Review of Finance 2025): the IV-curve shape before earnings prices the event; directly testable on our forward-logged chains around AMD/ARM/SMCI/ANET/AMAT reports.
- **[LETF compounding, autocorrelation and regimes](http://arxiv.org/abs/2504.20116)** and **[LETF log-return bounds](http://arxiv.org/abs/2301.03186)**: when 3x ETFs like SOXL decay vs. gain; testable on SOXL vs SOXX daily bars (feeds the `trend_regime_soxl` question).
- **[Structural clustering of volatility regimes](http://arxiv.org/abs/2004.09963)**: regime method candidate.
- **[Foresight learning for SEC risk](http://arxiv.org/abs/2601.19189)** (test set on Hugging Face) and **[rule-following AI trading agents](http://arxiv.org/abs/2610.26324)** (2,627 positions + evaluation toolkit): LLM-evaluation references.
- [BitraAI gex_app](https://github.com/BitraAI/gex_app): GEX visualiser; needs a Schwab API account; personal non-commercial licence; signals untested.

## Added from batch 5 (blind A/B, 06:15–07:18)
- **[Always-valid inference (mSPRT)](https://arxiv.org/abs/1512.04922)**: sequential p-values that stay valid when you check results every day; fits the arena's "peek every evening" reality better than a fixed-horizon test. Method-card candidate.
- **[CUSUM thresholds with familywise false-alarm control](https://arxiv.org/abs/2502.09185)**: calibrates a loss-streak / decay kill switch instead of picking a number by feel.
- **[Kelly with estimation risk, using options](https://arxiv.org/abs/2508.18868)**: theory for haircut sizing when the edge estimate is noisy; seed topic only.
- **[opengreeks](https://github.com/marketcalls/opengreeks)** (MIT, Rust/PyO3): Black-Scholes/Black-76 greeks and IV including vanna/charm; speed claims are self-reported.
- **[pyRMT](https://github.com/GGiecold-zz/pyRMT)** (MIT, stale since 2018): random-matrix cleaning of correlation matrices, to count *effective* independent bets in a correlated semis basket.

## Swarm quality (measured)

| Rubric | Top-40 verified useful | Typical error |
|---|---|---|
| v1 | 11/40 (27.5%) | labelled everything "backtest"; liked toy repos |
| v2 | 6/40 (15%) | quota compressed scores; 9 duplicates (EDGAR wrappers) |
| v3 | 5/40 (12.5%) | topic drift into real but irrelevant papers; 'no code' flags wrong |
| v1 (re-run 05:33–06:10) | 7/40 (17.5%) | judged relevance from the topic label; off-topic papers scored high |
| **A/B, same frontier, randomized by item id (06:15–07:18):** v1 | 1/20 (5%) | keyword matches judged relevant; one wrong claim (FinBERT output range) |
| **A/B:** v3 | 4/20 (20%) | one duplicate; otherwise generic theory papers |

**Reading:** the same rubric scored 27.5% early and 17.5% later, so most of the sequential v1/v2/v3 differences are frontier depth, not prompt quality. The fair test (randomized A/B on the same frontier, verifier blind to the arm) favoured v3, 4/20 vs 1/20, but with n = 20 per arm that is only a lean (one-sided Fisher p ≈ 0.17). Default to v3 and keep running the A/B until one arm reaches ~60 verified items.

The v1/v2 comparison is not perfectly fair: later items come from deeper, more saturated parts of the frontier.
