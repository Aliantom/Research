<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Cross-sectional momentum / industry rotation among AI-semi names

> **TL;DR:** Momentum is a real but decayed anomaly proven on broad long-short books; a top-3-of-27 AI-semis rotation can't be told from owning the beta, so edge is rated 2 and needs a random-pick placebo.
> **Source:** trading-lab method card knowledge/methods/cross-sectional-momentum-rotation.yaml (deep pass 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict:** The anomaly is real but weaker now, and the evidence is for thousands of stocks, not 3 of 27 correlated ones. Edge 3 to 2.

**New evidence (deep pass):**
- *Contrary, peer-reviewed:* Grundy and Martin (RFS 2001) find industry effects are not the main source of momentum, which weakens the Moskowitz-Grinblatt rotation story.
- McLean and Pontiff: published predictors lose about 58% of return after publication.
- Daniel and Moskowitz (JFE 2016): momentum crashes in panic rebounds; a 2-3 name book cannot hedge that.
- Novy-Marx and Velikov (RFS 2016): momentum is mid-turnover and costs erase many high-turnover anomalies unless a buy/hold band is used (decile books only).

**Failure modes:** hindsight-picked universe, names with short history (ARM, CRWV, SNDK), one AI-capex factor, and low power: with ~4% monthly tracking error, 120 months only detect ~9%/yr excess.

**Test plan (frozen):** 12-1 momentum at month-end, trade next open, top 3 (and top 2) equal weight, 3 bps/side (10 for SMCI, CRWV, ARM, SNDK). A name is eligible only after 273 days of its own history. Nulls: equal-weight universe, SMH, and 10,000 random 3-name picks per month. Hold out 2024-26.

**Decision:** adopt (2 names, small) only if net excess over equal weight is positive with a bootstrap CI above zero, the strategy ranks at or above the 95th percentile of the placebo, and it holds in both halves (split 2015) and the hold-out. Placebo percentile under 90 or loss of the edge after the eligibility rule means falsified. Anything between is inconclusive and means no capital.

**Costs and fit at $1.2k:** costs are minor (monthly, 1-3 names); the real issue is concentration, since one bad pick is about -50% of the account.

**Status:** researched-deep; implementability: now. **Scores:** edge 2, evidence 3, feasibility 4.

See [00 Index](../00-index.md). Card: `knowledge/methods/cross-sectional-momentum-rotation.yaml`.
