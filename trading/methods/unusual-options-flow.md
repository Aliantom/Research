<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Unusual options activity and put-call ratio signals

> **TL;DR:** Cannot be tested properly without paid trade-level data, and retail-flow signals are noise or contrarian; do not pay for alerts out of this account.
> **Source:** trading-lab method card knowledge/methods/unusual-options-flow.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Cannot be tested properly without paid trade-level data, and retail-flow signals are noise or contrarian; do not pay for alerts out of this account.

**Thesis:** Informed traders place leveraged directional bets in options before news, so abnormal call or put buying (open-buy volume, option-to-stock volume) predicts short-run stock returns.

**Fit for AI/semis:** Large caps like NVDA see enormous option volume dominated by retail and market-maker flow, which dilutes information.

**Evidence** (quality label from the card):
- *peer-reviewed*: Pan/Poteshman (RFS 2006): put-call ratios built from open-buy volume predict next-day returns of >40 bp and next-week returns of >1% (low-minus-high), using CBOE data with trade-initiator labels from 1990-2001. [source](https://www.nber.org/papers/w10925)
- *peer-reviewed*: Johnson/So (JFE 2012): the lowest decile of option-to-stock volume beat the highest by ~0.34% per week; follow-up work finds P/C ratios may predict only temporarily. [source](https://academicnewsletter.sufe.edu.cn/info/356813)
- *preprint*: Contrary: Cremers/Weinbaum show information content declining over their sample; and de Silva/Smith/So show retail option flow loses 5-9% around earnings, i.e. following retail-heavy flow is counterproductive. [source](https://quantpedia.com/how-retail-losses-money-in-option-trading/)
- *anecdote*: My searches found no peer-reviewed evidence that public retail flow-tracker alerts (sweeps, block tags) predict returns net of costs. [source](https://arxiv.org/pdf/2201.09319)

**Failure modes:** Signal requires opening-trade buy/sell classification that free data lacks | Retail-dominated flow is noise or contrarian | Publication decay and widespread data vendors

**Costs and feasibility at $1.2k:** Flow-alert subscriptions of $50-$200 a month are large relative to $1.2k. Trading itself is feasible (it reduces to buying a cheap option or stock), but the data needed to measure the signal properly are not free and are not in our data set, so this cannot...

**Test plan:** Only a proxy is testable: log chain volume and open interest daily, compute option-to-stock and put-call ratios, test rank IC against returns after 6 months. A null would not fully falsify the idea.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 1, evidence 3, feasibility 2. Proxy volume without trade classification may miss the signal that...

**Not in the arena:** The needed data is not free.

See [00 Index](../00-index.md). Card: `knowledge/methods/unusual-options-flow.yaml`.
