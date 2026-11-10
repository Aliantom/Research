<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# ThetaData Options Value: does it give 1-minute bid/ask on expired contracts?

> **TL;DR:** ThetaData docs list 1-minute NBBO option quotes under Value, but none says Value serves expired contracts back to 2020; email support once, then buy one month and test SPY 2020-03-20 250C.
> **Source:** Claude scout task 2026-11-03, follow-up to 2026-11-02 ThetaData purchase decision: confirm historical 1-minute bid/ask on expired contracts before buying  ·  **Project:** Trading brain  ·  **Updated:** 2026-11-03

All pages fetched 2026-11-03. Nothing was signed up for, no account used, terminal not downloaded.

## 1. Bottom line

**Answer to Q1: very likely yes, not proven in words.**
- VERIFIED: `GET /v3/option/history/quote` "returns every NBBO quote reported by OPRA", takes `interval=1m` (also tick, 10ms ... 1h), and carries the **Value, Standard, Pro** badges. Response has bid, ask, bid_size, ask_size, exchanges, conditions. (https://thetadata.net/docs/operations/option_history_quote.html)
- VERIFIED: the Value tier is listed at "1 Minute" granularity, first access 2020-01-01, 2 concurrent requests, real-time (https://thetadata.net/docs/Articles/Getting-Started/Subscriptions.html). Value is capped at 1-minute, so `interval=tick` and sub-minute intervals likely need Standard (REASONED from the granularity column; the quote page itself says it does not state the minimum tier for sub-minute intervals).
- AMBIGUOUS: no page says "expired contracts are available". The quote page and the list-expirations page are both silent. Circumstantial support: the endpoint takes any `expiration` and `date`; the docs' own IV example queries AAPL expiration 20241108 on date 20241104 (so already expired today); the Data Issues page discusses contracts that stop quoting "1-2 months before expiration" as normal and speaks of 2018 and 2022 historical quirks (https://thetadata.net/docs/Articles/Data-And-Requests/Data-Issues.html). Also, a historical-data vendor that dropped expired contracts would have almost no use for its own history. REASONED, probability high.
- AMBIGUOUS: the exact tier mapping in the subscriptions table (checkmarks lost alignment in extraction on both v2 and v3 pages). Quote = 3 checkmarks, so Free does not get it; with 4 tiers, 3 checkmarks means Value, Standard, Pro. REASONED, matches the endpoint badges.

**Recommendation: TRY FIRST.** Send the one-line support email below today (free). If it confirms or the reply is slow, buy one month of Value and run the test in section 7. Cost of being wrong is $40, not a lock-in (but see terms: no refunds).

## 2. Data by tier

| Need | Endpoint (v3, local terminal port 25503) | Tier | Evidence |
|---|---|---|---|
| 1-min NBBO bid/ask | `/v3/option/history/quote?interval=1m` | Value+ (badges Value, Standard, Pro) | VERIFIED page badges |
| 1-min OHLC of trades | `/v3/option/history/ohlc` | not determinable (3 checkmarks, so likely Value+) | page not opened; ASSUMED |
| EOD chain (OHLC, volume, last NBBO bid/ask at 17:15 ET, no Greeks) | `/v3/option/history/eod`, `expiration=*` allowed | all four badges shown, EOD has 4 checkmarks = Free+ | VERIFIED page; Free is limited to 2023-06-01 on |
| Open interest history | `/v3/option/history/open_interest` | Value, Standard, Pro badges; 3 checkmarks | VERIFIED. Value inferred |
| Implied volatility history | `/v3/option/history/greeks/implied_volatility` | **Standard and Pro only** | VERIFIED page text |
| First-order Greeks history | `/v3/option/history/greeks/...` | 2 checkmarks, so Standard+ | REASONED; second/third order 1 checkmark (Pro only likely) |

Consequence for the strategy: Value gives bid/ask and OI but no ThetaData-computed IV or Greeks. You can compute IV yourself from mid price, underlying price and a rate (needs a 1-minute underlying series; ThetaData stock data on Value starts 2021-01-01 and is 15 minutes delayed per the table, though that delay is irrelevant for history). Earlier note says the strategy does not use Greeks.

Useful request shape on the quote endpoint: `expiration=*`, `max_dte=14`, `strike_range=n`, `interval=1m`, single `date`. The page says multi-day requests are limited to 1 month and must name one expiration, so the efficient pull is one request per symbol per day with `expiration=*`. Whether Value accepts `expiration=*` plus `max_dte` for quotes is not stated (only the IV page says `*` is limited to one day and interval at least 1m). ASSUMED to work; the section 7 test checks it.

## 3. Access model, limits, volume estimate

- VERIFIED: Theta Terminal v3 is `ThetaTerminalv3.jar`, run with `java -jar`, needs Java 21+, serves HTTP on localhost only; REST calls go to the local server. Auth by API key or creds.txt. (https://thetadata.net/docs/Articles/Getting-Started/Getting-Started.html) RAM need is not documented.
- VERIFIED: concurrency Free 1, Value 2, Standard 4, Pro 8, account-wide. Extra requests queue (default 16, max 128, then possible 429). "Requests are not rate-limited, but concurrent requests are capped." (https://thetadata.net/docs/Articles/Data-And-Requests/Concurrent-Requests.html). Note the older v2 page said Value had 1 thread, and the free tier rate limit is stated as 20, 30 or 1 concurrent in different pages. Docs disagree on small details, so trust the terminal's startup printout of access level per data type (v2 docs say it displays this).
- The docs lack any throughput number. Pricing page says "3 request types" for Value vs 7 and 12 above.

Estimate (REASONED, my arithmetic; assumptions flagged):
- 30 underlyings x ~500 trading days (2 years) = 15,000 symbol-days = 15,000 requests if one request per symbol-day.
- Contracts per symbol-day: ASSUMED `strike_range=10` (21 strikes) x 2 rights x ~3 expirations within 14 DTE (more for SPY/QQQ with daily expirations, fewer for thin names) ~ 126 contracts.
- Rows: 126 x 390 minutes ~ 49k rows per symbol-day, ~737M rows total (upper bound; illiquid strikes may return fewer rows).
- Size: ~100 bytes/row CSV ~ 70 GB raw, roughly 8-15 GB as Parquet with zstd (ASSUMED compression). Fits easily on /mnt/ai-storage (1.4 TB free VERIFIED with df today).
- Time: with 2 concurrent requests and an ASSUMED 10-60 s per request (large CSV responses, nothing published), 15,000 / 2 x (10 to 60 s) = about 21 to 125 hours of wall time. The only real number comes from timing one request in the test. Plan on running it in chunks over several nights, resumable per symbol-day, and shrink to `strike_range=5` or 10-15 underlyings first. This pull conflicts with nothing on the GPU (network and disk bound), so it can run during night-shift but must not exceed the 16 GB RAM budget.

## 4. Terms

- VERIFIED (https://www.thetadata.net/subscriber-agreement): license is "solely for Licensee's internal personal use"; one individual; use for "trading on Licensee's behalf, analysis, and/or research" is permitted in Exhibit A; backtesting is not mentioned by name. No redistribution of data or derived works, "before or after the time of termination". Pricing page nav: Individual plan is "Personal use only, no redistribution or business use".
- Storing locally: no clause forbids caching. Section 1(b) bars "copy, modify, or create derivative works of the Data" which, read literally, is in tension with saving it to disk or computing features. AMBIGUOUS; every backtest does this, so this is a question for support. Also: do not publish the dataset or sell signals/results derived from it.
- Professional vs non-professional: the agreement does not define either. The OPRA terms mention Professional Subscribers. Standard OPRA rule (generic, not ThetaData's text): a person registered with or employed by a financial firm in a professional capacity may be Professional. The owner is a self-taught developer trading own account, probably non-professional. ASSUMED; confirm in the account sign-up questionnaire. Using it for a business (local-business websites, selling trading signals) would exceed "personal".
- Cancellation: pricing page says "Cancel Anytime" (from 2026-11-02 note). The agreement says term is "indefinitely", OPRA terms say 30 days notice, and "no refund" on termination (Section 8(c)); fees "variable and by no means will remain the same". So: cancel before the renewal date, expect no refund, and ask support whether cancel in portal takes effect at period end. No free trial found.

## 5. Alternatives (official pages, 2026-11-03)

| Vendor | Price | Coverage for "1-min option quotes, expired contracts" | Verdict |
|---|---|---|---|
| Massive (formerly Polygon) options (https://massive.com/options) | Starter $29, Developer $79, Advanced $199/mo | Quotes listed only on Advanced ($199), 5+ years, individual non-pro. Developer has trades and minute aggregates, 4 years. | skip (5x cost for quotes) |
| Databento OPRA (https://databento.com/catalog/opra/OPRA.PILLAR, https://databento.com/pricing) | pay-per-GB, no OPRA rate shown on pages; Standard $199/mo is for live data | schemas include CBBO-1m, TCBBO, OHLCV-1m, definition; "13+ years"; historical needs no license. Per-GB cost cannot be computed from the pages; the batch download tool quotes an exact price before purchase. | watch: get a free quote for the exact 30-symbol pull in the batch tool, best way to price a one-off |
| ORATS (https://orats.com/data-api, https://orats.com/one-minute-data) | Search snippet: Individual one-time historical $599 (not opened on official page) | 1-minute data from Aug 2020 (search snippet) | watch; ASSUMED, open page before using |
| IVolatility (https://www.ivolatility.com/news/493, search result only; official data-products page returned 404) | quote-based, contact sales; no individual price found | one-minute US options history claimed from 2011 (search snippet, unverified) | skip (no published price) |
| CBOE DataShop Option Quotes (https://datashop.cboe.com/option-quotes) | No price shown; monthly/annual and pick symbols | 1-minute or n-minute interval summaries; history start not stated | watch; ask price for a pick-symbols order |

Caution: the table above relies on a few lines of fetched text that mixed vendors; the ORATS $599 and IVolatility lines come from search snippets, and the orats.com data-api page I fetched listed API plans ($199 to $899/mo, one-minute history from Aug or Oct 2020) rather than that one-time price, so treat both as unverified. Only Massive and ThetaData prices are cleanly VERIFIED. ThetaData at $40 is the cheapest confirmed path to 1-minute quotes from 2020.

## 6. Fit with this machine

- REASONED: the terminal is a Java 21 app, the work is network and disk bound, no GPU. Java heap typically a few hundred MB to a couple GB (ThetaData publishes no figure; ASSUMED). With Ollama holding ~6-9 GB and 5.7 GB used now (free -h shows 15 GiB total, 9.3 GiB available), run it when no model is loaded or cap with `-Xmx2g`. Run it as a systemd user service for the overnight pull, only one at a time, not during GPU night-shift loads that fill RAM.
- It listens on localhost:25503 (v3), which should not collide with Ollama (11434), Guacamole (8080) or the VS Code tunnel. VERIFIED port from docs; collision not checked on the machine.
- Check Java is installed: `java -version` (not run here). Do not download the jar until buying.
- Use the owner's own API-key route (env var), never write the key into notes.

## 7. First test if they buy

Run this the same day, before anything else (needs the terminal running and Value tier showing "1 minute" access for options):

```
curl "http://127.0.0.1:25503/v3/option/history/quote?symbol=SPY&expiration=20200320&strike=250.00&right=call&date=20200316&interval=1m&start_time=09:30:00&end_time=16:00:00&format=csv" | head -5
```

Pass: about 390 rows, non-null bid and ask with ask >= bid, timestamps 09:30 to 16:00, for a contract that expired 2020-03-20 (an early date near the 2020-01-01 limit). Then repeat with `date=20200102&expiration=20200103` (earliest edge) and one wildcard day for timing: `symbol=AAPL&expiration=*&date=20240604&max_dte=14&strike_range=10&interval=1m`, time it, and count rows. If the first returns an error, 404 or 472 "no data", the answer to Q1 is no for that date: ask for refund and cancel. Record seconds-per-request to replace my 10-60 s guess.

Email to send first (support@thetadata.net, owner sends it): "On the Options Value plan, does /v3/option/history/quote with interval=1m return historical NBBO bid/ask for already-expired contracts back to 2020-01-01, and does expiration=* with max_dte work for historical dates? Also: is saving the results to local disk for personal backtesting permitted, and is cancellation effective at period end with no refund?"

## Final recommendation: TRY FIRST

Email the question, then buy one month of Options Value and run the SPY 2020-03-20 test above on day one. Do not buy a second month until the backtest rules are written and `quant-skeptic` has reviewed.

## Sources (all retrieved 2026-11-03)

- https://www.thetadata.net/pricing
- https://thetadata.net/docs/Articles/Getting-Started/Subscriptions.html (v3 tier table; checkmarks misaligned in extraction)
- https://http-docs.thetadata.us/Articles/Getting-Started/Subscriptions.html (v2, marked no longer maintained)
- https://thetadata.net/docs/operations/option_history_quote.html
- https://http-docs.thetadata.us/operations/get-hist-option-quote.html (v2)
- https://http-docs.thetadata.us/operations/get-bulk_hist-option-quote.html (v2)
- https://thetadata.net/docs/operations/option_history_greeks_implied_volatility.html
- https://thetadata.net/docs/operations/option_history_eod.html
- https://thetadata.net/docs/operations/option_history_open_interest.html
- https://thetadata.net/docs/operations/option_list_expirations.html
- https://thetadata.net/docs/Articles/Data-And-Requests/Data-Issues.html
- https://thetadata.net/docs/Articles/Data-And-Requests/Concurrent-Requests.html
- https://thetadata.net/docs/Articles/Getting-Started/Getting-Started.html
- https://www.thetadata.net/subscriber-agreement
- https://massive.com/options, https://databento.com/pricing, https://databento.com/catalog/opra/OPRA.PILLAR, https://orats.com/data-api, https://datashop.cboe.com/option-quotes, https://www.ivolatility.com/news/493 (search result only)
