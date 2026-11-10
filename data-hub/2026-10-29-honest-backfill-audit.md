<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Honest backfill audit (2026-10-29)

> **TL;DR:** Only raw prices with a splits/dividends table, SEC EDGAR by acceptance time and FRED ALFRED vintages can be backfilled honestly; news, social and options history cannot.
> **Source:** quant-skeptic audit (Sonnet, read-only) in a live Claude Code session, 2026-10-29; owner approved a ~2-year point-in-time backfill for data-hub  ·  **Project:** data-hub  ·  **Updated:** 2026-10-31

Labels: VERIFIED = read in code or hub.db; REASONED = follows from verified facts; ASSUMED = vendor knowledge, a worker
must confirm before relying on it. Spec for the backfill slices on Paperclip (Night shift project).

## 0. Findings in the repo and db

- **hub.db already holds unlabelled backfill (VERIFIED):** 2,985 `items` rows have `fetched_at` 2026-10-24 08:xx and an
  earlier `published_at`; prices start 2026-07-24 (3-month pull on 10-24); Form 4 starts 2026-08-05 (90-day lookback).
  The hub MCP treats them as known at `published_at`. Tag them `origin='backfill_implicit'` first.
- **`hn` is not a time series (VERIFIED):** Algolia `/search` ranks by popularity, so old rows exist only because they
  became popular (survivorship).
- **`prices` is probably not unadjusted (REASONED/ASSUMED):** `auto_adjust=False`, but Yahoo's raw Close/Volume are
  believed to be retroactively split-adjusted. Check NVDA across its June 2024 10:1 split. No Adj Close, no splits
  table, no `fetched_at`; `upsert_prices` overwrites on conflict.
- **Other overwrite paths:** `upsert_insider_tx` INSERT OR REPLACE; `upsert_items` UPDATEs title/meta on re-sight;
  `replace_sec_tickers` rebuilds the ticker->CIK map from today's file (delisted names vanish).
- **Form 4 coverage is tiny (VERIFIED):** 60 filings, 4 tickers, 2 signals (both large_sale). All `accepted_at` fall
  in UTC hours 00/20/21/23: plausible after-close filing, or an ET/UTC mislabel. Needs test A1.
- **Mixed timestamp formats (VERIFIED):** `Z` and `+00:00` both appear. Normalize at write time.
- **Universe (VERIFIED):** 31 symbols, several young (CRWV 2025 IPO, SNDK 2025 spin, ARM 2023, CEG 2022) plus ETFs
  without Form 4. Ranked on today's `ai_exposure`/`liquidity`/`affordability`: hindsight selection by construction.

## 1. Source verdicts

| Source | Verdict | Known-at rule | Main trap |
|---|---|---|---|
| EDGAR Form 4 | OK with conditions | `acceptanceDateTime` (UTC) of the accession; never filingDate/transaction_date | Walk older `filings.files[]` pages (else only recent 1,000); verify UTC (A1); sparse events |
| EDGAR 8-K | OK with conditions | `acceptanceDateTime`; Item 2.02 = actual earnings release time | Never use the actual date as "known beforehand"; after-hours acceptance not tradable same session |
| Amendments (4/A, 8-K/A) | OK with conditions | New event, own accession and acceptance time | Never overwrite the original; 4/A skipped in v1 (document) |
| XBRL companyfacts | OK with conditions (v2) | filed date + 1 day 00:00 UTC | Restatements: select by `filed <= as_of`, never "latest value" |
| 13F / 13D/G / 144 | OK, low value | acceptanceDateTime | 13F lags up to 45 days; skip |
| Daily prices (raw OHLCV + splits/dividends) | OK with conditions | Bar D: D 16:00 America/New_York + 30 min (zone-aware); volume D+1 00:00 ET; open only after 09:30 ET on D | Yahoo is unofficial, restates, drops delisted; adjusted series never as-of, adjust at query time |
| Intraday bars | Not available free / v2 | - | yfinance 7 days of 1m, 60 of 5m; Polygon free maybe 2 y with key (ASSUMED) |
| Options chains / IV / IV rank | Not honest | - | No free historical chains; use HV from raw prices as a labelled proxy |
| FRED / ALFRED macro | OK with conditions | `realtime_start` of the ALFRED vintage, end of that day (23:59 ET) | Plain `observations` returns revised values (lookahead); needs vintage params; key from env |
| FRED market series (DGS10, VIXCLS) | OK | same rule | lag only |
| RSS news | Not honest | - | newest-N survivors, edited entries |
| GDELT DOC API | Not honest | - | ~3 months, re-ranked |
| GDELT GKG/Events raw files | OK with conditions (v2, heavy) | DATEADDED (15-min) | metadata only, noisy org->ticker, ~70k files, large download |
| Vendor news APIs | Not honest by default | provider timestamp | unknown selection, recomputed sentiment (ASSUMED) |
| Hacker News `search_by_date` | OK with conditions | created_at | points/comments are today's values; deleted stories gone |
| arXiv | OK with conditions, low value | submitted + 48 h | API returns latest version text |
| GitHub search / Reddit / StockTwits | Not honest | - | current stars only / deletions and score drift / no history |
| Earnings calendars | Not honest | - | show the final date, not the expectation at the time |

## 2. v1 scope (ranked)

1. **Raw prices + splits + dividends** for the universe plus SPY, QQQ, SMH, SOXX, IWM, ^VIX, TLT, GLD. Include a name
   only with at least 250 trading days.
2. **EDGAR 8-K + Form 4 acceptance-timed events** (about 200 earnings events across the universe in 2 years: enough for
   event studies, not for tuning dozens of parameters).
3. **FRED/ALFRED short list** (15-30 series: CPI, payrolls, fed funds, DGS2/DGS10, claims, VIXCLS) for regime flags.
4. Defer GDELT GKG, HN/arXiv, companyfacts, intraday. Never backfill RSS, Reddit, StockTwits, GitHub.
5. **Survivorship:** ETF/benchmark and SEC series are the primary bias-free evidence; tag universe rows
   `selected_with_hindsight=1`; add non-winner control peers (candidates to evaluate: INTC, ON, MCHP, TXN, QCOM, some
   weaker small AI plays) and a delisted name if any free source serves one; report with and without the top 3
   winners; drop the first 60 trading days after an IPO/spin; claims are "this basket, this regime" until peers agree.

## 3. Acceptance tests (pytest, fixtures, no network)

- **A1** accepted_at equals the EDGAR header time in UTC on known fixtures; no Form 4 outside 06:00-22:00 ET.
- **A2** no backfilled row has known_at earlier than its source publication time.
- **A3** backfill rows: collected_at > known_at; live rows: collected_at - known_at within a few hours.
- **A4** as-of fence never returns known_at > T (edges T and T+1 s).
- **A5** bar D not visible before D 16:30 ET; volume not before D+1 00:00 ET.
- **B1** no as-of path reads adjusted prices (fails if a query touches adj_close).
- **B2** raw close shows the jump across a known split (e.g. SMCI 10:1 2024-10-01, verify); as-of adjustment uses only
  actions with ex_date <= T.
- **B3** cumulative split factor from the splits table matches the source's adjusted close within 0.1% on a few dates.
- **B4** no NaN/zero prices, trading days only, gaps > 5 trading days fail unless pre-IPO; row counts reported.
- **B5** collected_at column; re-runs don't change old rows (idempotent) or log a diff.
- **C1** amendments are new rows, never overwrite. **C2** submissions paging reaches back at least 2 years.
  **C3** 8-K Item 2.02 flagged as an actual event time, never a schedule.
- **D1** as-of returns the vintage in force at T for a revised series. **D2** lint fails on plain `observations`.
- **E1** every row has origin in {live, backfill, backfill_implicit}; the 10-24 08:xx rows become backfill_implicit.
- **E2** as-of API has an origin filter; a live-only query excludes all backfill.
- **E3** the backfill never updates live rows in place. **E4** one timestamp format (+00:00), `Z` rejected.
- **E5** one manifest row per backfill run (source, requests, range, code version, rows).

## 4. Cost

Prices: one batched call, under 2 min. EDGAR submissions: ~125 requests, under 1 min at 4/s. Form 4 XML over 2 years:
8k-25k filings (ASSUMED, wide), 35-105 min at 4/s, 100-300 MB cache. 8-K bodies optional (~200 requests). FRED/ALFRED
~75 requests, ~1 min. **v1 total about 1-2 hours**, dominated by Form 4. Safe overnight.

## 5. Storage

A **separate `hub_backfill.db`** written only by a dedicated backfill tool, both files exposed through one read-only
as-of layer that returns `origin` and defaults to a pre-registered mode. Every backfill row carries `known_at`,
`collected_at`, `origin='backfill'` and a manifest run id. A live row proves "we had this then"; a backfill row only
proves "the source claims this timestamp". **The live period from 2026-10-24 is the only clean holdout: develop and
tune on backfill, confirm once on live, pre-registered via `experimenter`.**

## 6. What would change the verdict

Raw prices: B1-B3 pass on at least 3 real splits and stored Close is shown unadjusted. Acceptance times: A1 passes on at
least 20 real Form 4/8-K filings spread across market hours. Any signal claim: at least 100 independent events, holds
without the top 3 winners, beats SMH buy-and-hold and a random control after realistic option costs (which this data
cannot supply), and holds on the live holdout. **Options P&L cannot be backtested honestly with this data:** v1 tests
are stock-direction or event-return tests, and reports must say so.
