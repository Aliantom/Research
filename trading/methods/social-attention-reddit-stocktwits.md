<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Social attention / sentiment (Reddit, StockTwits, search volume)

> **TL;DR:** Mention counts predict next-day and 20-day reversal in several studies, but WSB picks show no alpha, effects sit in small retail stocks, and our history starts 2026-10-28: forward test only, edge 1.
> **Source:** trading-lab method card knowledge/methods/social-attention-reddit-stocktwits.yaml (deep pass 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict:** Use, if at all, as an avoid/trim filter after attention spikes. Edge 2 to 1; evidence 3 and feasibility 3 unchanged.

**New evidence (deep pass):**
- Cookson, Lu, Mullins and Niessner (JFE 2024): attention predicts lower next-day returns, sentiment higher; mention counts are an attention measure.
- Barber, Huang, Odean and Schwarz (JF 2022): heavy Robinhood buying precedes negative returns, about -4.7% over 20 days for the top-bought stocks.
- *Contrary:* Chacon, Morillon and Wang (2023): 221k WallStreetBets recommendations, 2012-2021, show no risk-adjusted alpha at any holding period from 1 day to 1 year.
- *Contrary, preprint:* Otsubo, Poon and Wei: WSB attention cascades gave about +5% abnormal return with no reversal, so a fade can be squeezed.
- Still in the card: Bradley et al. (WSB due-diligence predictability died after GameStop) and Da, Engelberg and Gao (about two-week price pressure, then reversal).

**Test plan (frozen):** pulse daily mention counts for 25 single names, day cut at 16:00 ET. Spike = robust z at least 3 (30-day median and MAD), count at least 5, first spike after 5 quiet days, earnings +/-1 day reported separately. Outcomes: next-open excess return vs SMH (60d beta) at +1, +5 and +10 days, 10 bps round trip (25 for SMCI, CRWV, PLTR). Regress on the spike plus same-day return, absolute return, volume ratio, earnings dummy and ticker effects, clustered by date, and compare with matched non-spike days.

**Power:** 100 events can only detect about 0.5% at d+1 and 1.2% at d+5; Bonferroni across three horizons (|t| above 2.4).

**Decision:** long-after-spike is falsified if no horizon is significantly positive. Adopt the avoid/trim filter only if excess return is below -0.5% after costs with t below -2.4 and the same sign in both halves. If the sign is positive, drop the fade. Fewer than 100 spikes by 2027-06 means stop.

**Status:** researched-deep; implementability: needs data.

See [00 Index](../00-index.md). Card: `knowledge/methods/social-attention-reddit-stocktwits.yaml`.
