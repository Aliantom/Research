<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Event-driven trading on 8-K items and headlines (guidance, contracts, offerings)

> **TL;DR:** The tradable part after the first reaction is small and shrinking; worth only a cheap next-day-open event study, not a live method.
> **Source:** trading-lab method card knowledge/methods/event-driven-8k.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** The tradable part after the first reaction is small and shrinking; worth only a cheap next-day-open event study, not a live method.

**Thesis:** Material 8-K items and news (guidance changes, big customer contracts, offerings) cause price moves; a model that reads them could capture the continuation after the first reaction.

**Fit for AI/semis:** AI names live on news flow (capex announcements, customer wins, export-control rules), so event density is high.

**Evidence** (quality label from the card):
- *preprint*: Lopez-Lira and Tang: GPT-4 news-headline scores capture the initial market response (~90% portfolio-day hit rate) but that initial reaction is non-tradable. [source](https://arxiv.org/abs/2304.07619)
- *peer-reviewed*: Glasserman and Lin: GPT sentiment backtests can be flattered by look-ahead from training data; anonymizing company names reduced the bias in-sample, and out-of-sample the look-ahead was not a concern. [source](https://arxiv.org/abs/2309.17322)
- *preprint*: Look-Ahead-Bench: standard LLMs show significant look-ahead (alpha decay when moving to unseen periods) while point-in-time models do not. [source](https://arxiv.org/abs/2601.13770v1)

**Failure modes:** The reaction is over before a retail order lands (non-tradable) | LLM labels memorize known events in backtests (look-ahead) | 8-K timestamps vs price timestamps misaligned; after-hours spreads wide

**Costs and feasibility at $1.2k:** Zero commission, but after-news spreads can be 10-50 bps on small caps. Feasible only as slow (next-day-open or later) trades; anything fast is not realistic with $1.2k, a retail broker and a PDT limit.

**Test plan:** Event study on 8-K items 2.02/7.01/8.01/1.01 for the universe, measured from the first full session after filing, 10 bps cost, with text labelled name-stripped. Falsified if post-day-1 drift is null.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 2, evidence 2, feasibility 3. The tradable portion after the initial reaction appears small and shrinking; sample and look-ahead risk dominate.

**Not in the arena:** No book of its own.

See [00 Index](../00-index.md). Card: `knowledge/methods/event-driven-8k.yaml`.
