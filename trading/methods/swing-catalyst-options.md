<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# 2-8 week options around catalysts (earnings, launches, AI capex news)

> **TL;DR:** Mixed evidence: straddles gain in the 3 days before earnings, but long premium has a negative baseline and wide spreads, and nothing tests 5-10 day pre-catalyst debit spreads: paper only, 2-year test.
> **Source:** trading-lab method card knowledge/methods/swing-catalyst-options.yaml (deep pass 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict:** Paper trade only, with a pre-registered rule and a kill switch. Scores: edge 2, evidence 2, feasibility 4 to 3.

**New evidence (deep pass):**
- Gao, Xing and Zhang (JFQA 2018): average stock straddles lose, but 3 days before earnings to the print they earn about 3.3%, stronger in small, costly names and weakest in liquid ones.
- *Contrary:* Coval and Shumway (JF 2001): ATM straddles lose about 3% a week on average; far-OTM calls lose heavily.
- *Contrary:* Bryzgalova, Pavlova and Sikorskaya (JF 2023): retail option traders lose on average; quoted spreads on weeklies average about 12.6%.
- Lei, Wang and Yan (JBF 2020): the call-put IV spread rises into earnings and predicts the announcement return (useful direction signal, but IV itself gets bid up).
- Still in the card: de Silva, Smith and So (retail loses 5-9% around earnings) and iVolatility (-18% on straddles held through the print).

**Test plan (frozen):** earnings dates for MSFT, GOOGL, META, AMZN, NVDA, AVGO, ORCL, MU, AMD. Bull call spread (0.60 long, 0.30 short delta), 35-45 DTE, on the basket member with the lowest IV30/RV20 and spread under 8% of mid. Enter 7 trading days before, exit the day before the print or at +50%/-50% of debit. Fills at mid plus or minus half the half-spread, plus tastytrade fees. Controls: equal-dollar SMH shares, 5 random-date spreads per trade outside +/-10 days of catalysts, and the same spread held through the print.

**Power:** per-trade SD is about 60-80% of debit and trades cluster into 4 seasons a year, so use a cluster bootstrap; 30 trades is a futility screen only.

**Decision:** drop after 30 trades if mean net return does not beat SMH shares or the 90% upper bound on excess vs the placebo is below +5% of debit. Go to small real money only after 60+ trades with a positive lower bound, worst season no worse than -35%, and measured spread cost at or under 8% of debit.

**Status:** researched-deep; implementability: now.

See [00 Index](../00-index.md). Card: `knowledge/methods/swing-catalyst-options.yaml`.
