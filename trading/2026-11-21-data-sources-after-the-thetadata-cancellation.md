<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Data sources after the ThetaData cancellation

> **TL;DR:** Keep the self-logged broker chain archive as the options source, buy no new vendor; add free feeds (IR RSS earnings dates, SEC companyfacts, trial broker news); delete ThetaData data within 30 days.
> **Source:** Scout task 2026-11-21: best free or cheap point-in-time data for the trading research and paper arena once the paid options-history subscription is cancelled (about 2026-12-10)  ·  **Project:** Trading brain  ·  **Updated:** 2026-11-23

All pages fetched 2026-11-21. Nothing was signed up for, no credentials or keys were used, no site was scraped. Only public docs, public feeds and one public read-only database API were read. Local counts come from read-only copies of the arena's own files.

Goal in one sentence: keep the trading research and paper arena improving after the options-history subscription ends, with free or cheap sources that are real, maintained, allowed for personal research, and point-in-time.

## 1. Bottom line

1. **Read the vendor agreement before the cancel date (cost: nothing; most urgent).** VERIFIED (fetched twice, subscriber agreement page): section 8(c) says that on termination the licensee must "delete, destroy, or return all copies of the Data" and certify it in writing; section 8(e) says "All data obtained indirectly or directly from Theta Data must be expunged within 30 days of termination", and that derived works cannot be redistributed and must also be expunged. The page shows no effective date. So "cancel and keep the download" is not clearly allowed. REASONED: if cancelling ends the agreement, the roughly 17 GB on disk (VERIFIED by `du`; the brief says 12 GB) must go about 30 days later. UNKNOWN: whether lapsing a paid tier counts as termination, whether a free-tier account keeps the agreement alive, and whether backtest result tables count as "derived works". First step: send support one question (the owner sends it): "On cancelling Options Value, must we delete previously downloaded data and derived result tables within 30 days under section 8(e), and does keeping a Free account change that?" Until answered, plan as if deletion is required: finish and archive backtest-002 inputs and outputs before 12-10, and store only aggregate result numbers.
2. **Treat the self-logged broker chain archive as the options source from now on, and back it up this week.** It is the only forward options record once the vendor feed ends. VERIFIED (read-only copy, 2026-11-21): 7.24 M rows, 452 runs, 18 sessions 2026-10-28..11-20, 40 underlyings, expirations up to 45 DTE, about 25 snapshots per session; bid, ask, size, last, volume and open interest present; implied vol and delta present on 62% of quoted rows; 1.2% flagged stale. It is a single 0.5 GB file with no second copy found (REASONED from the one location read). **Correction (live session, 2026-11-21): it is backed up. The machine's nightly HDD snapshot includes the archive's folder and ran successfully on 11-19 and 11-20 (after the last daily write), so the remaining risk is only the single-disk HDD, not a missing backup.** First step: a nightly compressed Parquet export to a second disk path plus a row-count check, owned by the trading-lab side (not filed here; it is not a data-hub collector).
3. **Add the free event and fundamentals feeds that data-hub does not have yet.** Company investor-relations RSS for confirmed earnings dates (the January-season need) and the SEC companyfacts API for point-in-time fundamentals. Both are key-free. Issues filed for both (section 6). Broker-API news is a trial after a one-call access check.

**Do not buy another options-history vendor.** Cheapest real alternatives start at a few hundred dollars (section 2) and cannot change what Gate v2 reads, because Gate v2 (2027-01-21) is built on forward arena trades, not on history. REASONED from the pre-registered gate rules in the Trading brain brief.

## 2. Q1: options history after 2026-12-10

### Is the self-logged archive enough?

| Need | Archive covers it? | Evidence |
|---|---|---|
| Forward walk-forward on the arena books (entry quotes, spreads, marks) | Yes, about 60 sessions by 2027-01-21 | VERIFIED 18 sessions so far; REASONED: roughly 42 more trading days to the gate date |
| Realistic fills (bid/ask and size) | Yes, at 15-minute cadence | VERIFIED columns |
| Greeks and IV | Partly: 62% of quoted rows | VERIFIED. The rest can be recomputed from mid and spot (ASSUMED recompute is accurate enough) |
| Expirations beyond 45 DTE | No (LEAPS, long calendars) | VERIFIED max DTE 45; arena books are 0-9 DTE, so low impact (REASONED) |
| Names outside the 40 logged | No | VERIFIED 40 underlyings |
| Anything before 2026-10-28 | No: this is what the vendor data was for | VERIFIED first snapshot |
| Days the PC is off or the logger fails | Gap | VERIFIED: 18 sessions in 18 trading days so far (11-02 onward is clean), but the 10-28 first day is partial |

Verdict: enough for the forward walk-forward and the arena; not a history source. Anything that needs pre-October data must use what the vendor data already produced before the cancel date (subject to item 1 above).

### Candidate sources for gaps

| Name | What it is | Evidence | Fit, cost, license | Verdict |
|---|---|---|---|---|
| Self-logged broker chains | 15-min chain snapshots with Greeks | VERIFIED, local read | Free; the broker API terms are not read (the PDF was not opened), personal use ASSUMED | ADOPT (back up) |
| DoltHub `post-no-preference/options` | Free daily EOD option chains, git-versioned database, public SQL API | VERIFIED live: latest commit 2026-11-21 for 2026-11-20 data; 2,199 commits; table has date, symbol, expiration, strike, call/put, bid, ask, implied vol, delta, gamma, theta, vega, rho; repo licence file is CC BY-SA 4.0 | Free. About 120 to 220 rows per name per day: a thin slice, not the full chain. VERIFIED covers AMD MU AVGO MSFT META NVDA PLTR SMCI SNDK LRCX AMAT VRT and SPY; VERIFIED zero rows for SMH, QQQ, CRWV, ARM, TSM, ASML, TEAM, NVDL, SOXL, SOXX that day. History start not verified (query timed out). Upstream provenance of the data is not stated, so the CC licence cannot be checked against whatever the author scraped. A commit date gives a natural known-at time | TRIAL as a daily cross-check and a fill for missed days. Not a backtest source |
| Alpaca historical option bars and trades | Free OHLC of traded prints since Feb 2024 | VERIFIED in Alpaca's OpenAPI file: endpoints are options bars, trades, latest quotes, snapshots and chain; there is no historical quotes endpoint. Docs say historical data starts Feb 2024 and the free feed is "indicative" (quotes are not OPRA); free plan blocks the latest 15 minutes, 200 calls per minute | Free. Prints only, no bid/ask history, so entries and spreads cannot be priced | SKIP for backtests (watch if quotes are added) |
| Massive (formerly Polygon) Options Basic | Free tier: 5 calls per minute, 2 years history, end of day, minute aggregates | VERIFIED on the vendor options page. Paid: Starter $29, Developer $79 (trades), Advanced $199 (quotes, 5+ years) | 5 calls per minute cannot walk a chain (one contract per call, REASONED). Quotes only at $199 per month | SKIP; the free tier is too slow, quotes cost $199 |
| Databento OPRA | Pay-per-GB historical, from 2023-03-28 | Search-result summary only (blog and docs titles); the pricing page excerpt did not show rates or licence; $125 free credit claimed. Not verified | Cost per GB unknown; a full chain for 40 names at tick level is large (REASONED) | WATCH; check the quote before any spend |
| Cboe DataShop end-of-day option quotes | Full OPRA EOD, from 2012, 15:45 snapshot with Greeks | VERIFIED coverage on the product page; price not shown; personal-use terms not shown | Price unknown (commercial) | SKIP unless the owner wants a paid test |
| ORATS | Near-EOD data back to 2007; $99 per month delivery, $599 one-time backfill (search summary, not opened) | Search summary only | Not verified | SKIP (cost) |
| OCC public reports | Volume and open interest reports, batch download | The batch-processing page returned 403 to the fetcher; only a search summary | Open interest by contract is already in the broker chains (VERIFIED column); little gain | SKIP |
| Historical Option Data free samples | One symbol per month sample | VERIFIED page | License not stated; sample only | SKIP |

### Terms that matter, by source

- ThetaData subscriber agreement (VERIFIED, quoted above): personal use for "analysis, and/or research"; copying and derivative works restricted; on termination delete everything and expunge derived works within 30 days; one individual per term. No clause on automated access or rate limits.
- Alpaca: free historical data plan table (200 calls per minute, 15-minute restriction) VERIFIED; the market-data agreement text was not read.
- Massive: individual plans are for "personal, individual, and non-business use" (VERIFIED on its terms page); storage and retention clauses not read.

## 3. Q2: events and fundamentals

| Name | What it is | Real? (docs) | Maintained | Terms and rate limits | Fit in data-hub | Verdict |
|---|---|---|---|---|---|---|
| Company IR press-release and event RSS | The company's own feed; earnings date announcements arrive here first | VERIFIED: a live NVIDIA press-release feed returned items today; its event feed lists scheduled events; 3 of 10 guessed IR hosts returned a valid feed, 1 returned 403, the rest were not feeds or not found (hosts were guessed, so real coverage needs per-company discovery) | Live (last build date 2026-11-20 on the NVIDIA feed) | The NVIDIA page offers the feeds for subscription and states no terms; each site's own terms still need a read; one request per feed per hour is polite | New collector `ir:feeds` with a per-ticker feed list; store title, link, published and first-seen time; parse earnings-date announcements | ADOPT (issue filed) |
| SEC EDGAR companyfacts and submissions APIs | XBRL fundamentals by filing; filing history | VERIFIED on the SEC API documentation page: submissions updated in under a second, XBRL under a minute; bulk zips rebuilt nightly about 3:00 a.m. ET | Active | VERIFIED: 10 requests per second per user across machines; declare a User-Agent with contact; "Download only what you need"; no crawling by automated tools. data-hub already sends a compliant User-Agent | Extends the existing EDGAR source: facts keyed by filing date, so quarter figures are known only from the day they were filed (the `filed` field is ASSUMED present; the docs page did not define it, so the acceptance check samples one response) | ADOPT (issue filed) |
| FINRA short interest and short volume | Flat files | Already live in data-hub (code reviewed) | Yes | cdn.finra.org public files | Exists | Already adopted; nothing to add |
| SEC Form 4 insiders | Insider trades by acceptance time | Already live in data-hub | Yes | Same SEC rules | Exists | Already adopted |
| SEC Form 13F data sets | Quarterly ZIPs of institutional holdings | VERIFIED: page titled July 2013 to August 2026, quarterly since March 2024 in three-month sets, "as-filed", no licence or reuse text, accuracy disclaimer | Current | Static files; filings arrive up to 45 days after quarter end (REASONED from the 13F rule, not on the page) | Slow signal; low value for 0-9 DTE books | TRIAL later, low priority |
| FRED and ALFRED | Macro series with vintage (as-first-published) history | VERIFIED: the API supports realtime_start and realtime_end and a vintage_dates parameter; the terms page was read | Active | Terms VERIFIED: no specific request figure on the page; third-party sources say 120 requests per minute (not confirmed officially); on termination you must destroy API copies; apps must show a notice; copyrighted series need owner permission for non-personal use | Collector already built in data-hub (backfill); needs the owner's free key, which is pending | ADOPT; blocked on the key (owner action) |
| Finnhub earnings calendar and company news | Free-key REST API | VERIFIED in Finnhub's own swagger file: earnings calendar free tier is "1 month of historical earnings and new updates"; company news free tier is "1 year of historical news"; news sentiment and press releases are premium; free plan 60 calls per minute (third-party sources; pricing page did not show it) | Active | VERIFIED terms: personal use only; do not share "data or derived results" with any third party without written approval. That rules out putting Finnhub data in the public research mirror | Poll the calendar daily and store each snapshot as seen, so the first-seen time is real. It carries no "confirmed" flag, so it is a cross-check, not the source of truth | TRIAL (needs the owner's free sign-up) |
| Alexandria/Firecrawl data providers | Hosted structured data | Not opened beyond the tool description | n/a | Billed per call | Adds a metered dependency | SKIP |

Semiconductor industry data: data-hub already collects TSMC monthly revenue, SIA global sales and Korea chip exports (code reviewed). Cheap additions through FRED once the key exists (REASONED, series ids not verified this session): Federal Reserve industrial production for semiconductors and a semiconductor producer price index. Paid industry trackers (DRAM contract prices) were not opened and are assumed to forbid scraping.

## 4. Q3: news and sentiment with point-in-time stamps (free tiers)

| Name | Evidence | Terms and limits | Point-in-time? | Verdict |
|---|---|---|---|---|
| Alpaca news API | VERIFIED in its OpenAPI file: `/v1beta1/news`, fields headline, summary, content, `created_at`, `updated_at`, symbols, source, URL | Free market-data plan: 200 historical calls per minute (VERIFIED). Whether news is included on the free plan is not stated in the plan table (ASSUMED yes; one authenticated GET settles it) | `created_at` is the publisher time; first-seen time from our own polling is the honest known-at; `updated_at` shows edits. A history backfill is not point-in-time | TRIAL (an Alpaca key already exists for the bars downloader) |
| GDELT 2.0 events, mentions and GKG files | VERIFIED: the update index returned a file set stamped 2026-11-21 13:00 today; the site says files update every 15 minutes and calls the data "100% free and open"; the DOC API answered with a "one request every 5 seconds" notice | Free; bulk files, no key. A formal terms page was not read | File timestamps are 15-minute and give a real ingest time | WATCH: broad, noisy, hard to map to tickers; high storage cost for little gain next to the existing RSS feeds |
| Finnhub company news | VERIFIED free tier: 1 year of history | Personal use; no sharing of derived results | Polling gives a real first-seen time | TRIAL together with the earnings calendar |
| Local sentiment scoring | A small finance-tuned classifier on the 3080 for bulk headlines (REASONED: fits in 10 GB; no model was checked this session) | Local, free | Inherits the headline's known-at | WATCH; the existing extraction task already scores ticker and sentiment |
| Business Wire / GlobeNewswire RSS | Business Wire terms page returned 403; a search summary says its terms list retrieving RSS as permitted (not verified); GlobeNewswire says it offers RSS, rules on automated retrieval not found | Unverified | Published time plus first-seen | WATCH until the terms are read |

## 5. Adjacent ideas

- **Archive health as a data source.** A daily check that the chain logger got its expected run count and that stale flags stay under a threshold gives early warning of silent gaps (REASONED; it matches the gap risk in section 2).
- **Dated earnings snapshots.** Storing each calendar as seen (Finnhub or IR) lets the arena measure how often an estimated date later moved, which is the evidence for keeping alternate-date rows. REASONED.
- **EOD cross-check from the public database** (DoltHub above) to detect a bad logger day without paying anyone.

## 6. Issues filed

Filed in the data-hub backlog (titles in the final report): IR RSS earnings-date collector, and EDGAR companyfacts point-in-time fundamentals. The Alpaca news trial and the Finnhub calendar were not filed: the first needs one access check and the second needs a sign-up the owner must do.

## 7. Rejected, with reasons

- Massive free options tier: 5 calls per minute cannot read a chain.
- Alpaca historical option data for backtests: prints only, no historical quotes, indicative feed on the free plan.
- Cboe DataShop, ORATS: paid, price or terms not confirmed; no change to what Gate v2 can read.
- OCC batch reports: duplicate what the broker chains already carry; page blocked the fetcher.
- Historical Option Data samples: one symbol a month, licence not stated.
- Nasdaq and Yahoo earnings pages: unofficial endpoints whose terms were not read; the company-feed route avoids the question. ASSUMED terms forbid automated collection.
- Firecrawl/Alexandria providers: metered spend for data that free official feeds already give.

## 8. Sources (all retrieved 2026-11-21)

- ThetaData subscriber agreement: https://www.thetadata.net/subscriber-agreement
- SEC accessing EDGAR data (fair access): https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data
- SEC API documentation: https://www.sec.gov/edgar/sec-api-documentation
- SEC developer resources: https://www.sec.gov/about/developer-resources
- SEC Form 13F data sets: https://www.sec.gov/dera/data/form-13f
- FRED API terms: https://fred.stlouisfed.org/docs/api/terms_of_use.html
- FRED series observations: https://fred.stlouisfed.org/docs/api/fred/series_observations.html
- Finnhub swagger file: https://finnhub.io/static/swagger.json and terms: https://finnhub.io/terms-of-service
- Alpaca market data OpenAPI: https://docs.alpaca.markets/us/v1.1/openapi/market-data-api.json
- Alpaca about market data: https://docs.alpaca.markets/us/docs/about-market-data-api
- Alpaca historical option data: https://docs.alpaca.markets/docs/historical-option-data
- Massive options pricing: https://massive.com/options
- Cboe DataShop EOD option quotes: https://datashop.cboe.com/option-quotes-end-of-day-with-calcs
- DoltHub options database (via its public read API): https://www.dolthub.com/repositories/post-no-preference/options
- Databento usage pricing FAQ: https://databento.com/docs/faqs/usage-pricing-and-data-credits
- NVIDIA investor RSS page: https://investor.nvidia.com/investor-resources/rss/default.aspx
- GDELT data page: https://www.gdeltproject.org/data.html and update index: http://data.gdeltproject.org/gdeltv2/lastupdate.txt
- Historical Option Data free page: https://historicaloptiondata.com/free-data/
- Local: read-only copies of the arena chain file and the data-hub source code (no paths recorded here).
