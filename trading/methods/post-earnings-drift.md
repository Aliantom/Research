<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Post-earnings-announcement drift (PEAD) in mega-cap tech

> **TL;DR:** The literature says drift is gone in large caps, and we lack surprise data; low odds.
> **Source:** trading-lab method card knowledge/methods/post-earnings-drift.yaml (overnight 2026-10-28)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Verdict:** The literature says drift is gone in large caps, and we lack surprise data; low odds.

**Thesis:** Stocks with large positive earnings surprises keep drifting up (negative ones down) for weeks after the report because investors under-react.

**Fit for AI/semis:** AI names have big, frequent earnings surprises and guidance moves, but they are the most-watched, most-covered stocks on earth, where evidence says...

**Evidence** (quality label from the card):
- *peer-reviewed*: Martineau (2021/22): PEAD disappeared for non-microcap stocks by ~2006 and only recently for microcaps; announcement-day reaction now captures the information. [source](https://cfr.ivo-welch.info/published/papers/martineau2021rest.pdf)
- *practitioner backtest*: Two papers accepted in 2025 claim PEAD is alive; a UCLA Anderson brief says the disagreement is largely research-design choices (return window, benchmark). [source](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again/)
- *peer-reviewed*: Quantpedia summarizes Milian: in the most liquid stocks the 2-day post-earnings pattern has reversed, so short-window and quarterly-window drift can differ. [source](https://quantpedia.com/Screener/Details/238)
- *preprint*: Lopez-Lira and Tang: GPT-4 news scores predict subsequent drift mainly for small stocks and negative news, and strategy returns fall as LLM adoption rises, i.e. little left in large caps. [source](https://arxiv.org/abs/2304.07619)

**Failure modes:** Drift not present in large caps (the core contrary result) | Surprise measures need analyst consensus data we do not have for free | Tiny sample: 27 names x 4 reports/yr

**Costs and feasibility at $1.2k:** Normal costs after day 1; the post-print day can have wide spreads. Mechanically feasible (holds are days to weeks), but with 27 names there are only ~100 events a year and we lack surprise data, so a robust test is hard.

**Test plan:** Proxy surprise by the earnings-day return vs SMH, enter at the day t+2 open, exit day t+21, 5 bps. Falsified if the top-minus-bottom tercile spread is not positive.

**Status:** researched; implementability: needs data. **Scores (1-5, judgment):** edge 1, evidence 3, feasibility 3. The 2025 papers conflict with Martineau and I could not read them to see which window/sample matters for mega caps.

**Not in the arena:** No book.

See [00 Index](../00-index.md). Card: `knowledge/methods/post-earnings-drift.yaml`.
