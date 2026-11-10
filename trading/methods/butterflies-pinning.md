<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Butterflies, OPEX pinning and dealer gamma (GEX)

> **TL;DR:** Cheap lottery at best: the pinning evidence ends in 2002, fees take a big bite of a $20-60 debit, and nothing supports single-name AI stocks.
> **Source:** trading-lab method card knowledge/methods/butterflies-pinning.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** Cheap lottery at best: the pinning evidence ends in 2002, fees take a big bite of a $20-60 debit, and nothing supports single-name AI stocks.

**Thesis:** Stock prices cluster near large open-interest strikes at expiration because of hedging flows, so a cheap butterfly centered there could pay 5-20x if the pin is predictable.

**Fit for AI/semis:** Pinning is documented for optionable stocks in general, and strongest where open interest is concentrated.

**Evidence** (quality label from the card):
- *peer-reviewed*: Ni/Pearson/Poteshman (JFE 2005): closing prices of optionable stocks cluster at strikes on expiration dates, shifting returns by >=16.5 bp per expiry on average, attributed to market-maker delta hedging and trader... [source](https://ideas.repec.org/a/eee/jfinec/v78y2005i1p49-87.html)
- *marketing*: Cboe states net market-maker 0DTE gamma hedging is at most ~0.2% of SPX daily liquidity, arguing the hedging channel is small for index 0DTE. [source](https://www.cboe.com/insights/posts/0-dt-es-decoded-positioning-trends-and-market-impact)
- *preprint*: Dim/Eraker/Vilkov: high 0DTE open-interest gamma does not propagate past volatility (secondary summary), challenging the simple GEX narrative. [source](https://harbourfrontquant.substack.com/p/impact-of-zero-dte-options-on-the)
- *practitioner backtest*: An independent 8-year SPY backtest (FlashAlpha, vendor blog) concludes GEX mostly tracks VIX and adds little once VIX is controlled. [source](https://flashalpha.com/articles/gex-dex-vex-chex-8-year-backtest-spy-vix-control)
- *marketing*: SqueezeMetrics GEX white paper (practitioner origin of the signal). [source](https://slopeofhope.com/wp-content/uploads/2020/11/GEX-white_paper.pdf)

**Failure modes:** Assignment/exercise on expiring in-the-money short legs creates stock positions you cannot fund | Pin effect is small (basis points) and the 2005 sample predates 0DTE... | GEX is a model estimate (assumes dealers are long customers' puts and...

**Costs and feasibility at $1.2k:** About $4 to open a 1-2-1 butterfly, over 10% of a $30 debit before spreads. Feasible mechanically (debit $20-$100 each), but pinning on single-name AI stocks has no modern evidence of tradable size.

**Test plan:** From daily closes, check whether expiry-day closes cluster near strikes more than other days for 2023-2026; if no excess clustering, kill it. Otherwise paper-trade Friday 1-wide butterflies.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 1, evidence 3, feasibility 3. 

**Not in the arena:** No book and no usable open-interest history.

See [00 Index](../00-index.md). Card: `knowledge/methods/butterflies-pinning.yaml`.
