<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Multi-agent LLM graphs in trading and financial decision-making: evidence as of November 2026

> **TL;DR:** No credible evidence (Nov 2026) that multi-agent LLM graphs add net alpha; results shrink under longer, costed, post-cutoff tests. Forward-only tests on decision quality are the defensible use.
> **Source:** Deep-research assignment, 2026-11-02  ·  **Project:** Trading brain  ·  **Updated:** 2026-11-03

Research notes, not investment advice. Evidence strength is labelled. Most sources are arXiv preprints without peer review. Facts about the owner's setup come from local files and are cited by path.

## Do agent graphs add alpha or decision quality, and what did TradingAgents, FinCon, FINMEM, QuantAgent and AlphaAgents show?

### Takeaway
No credible public evidence shows that a multi-agent graph adds net alpha over simple baselines or over a single LLM with the same budget. The original headline results come from windows of about 3 to 8 months on hand-picked stocks, and the only long-horizon re-test and the only independent post-cutoff reproduction I found both fail to confirm them. Absence of proof is not proof of zero: the null results are themselves low-powered.

### Cited Findings

**Original claims and their weaknesses**

| Study | Claim | Test | Main weaknesses |
|---|---|---|---|
| TradingAgents | CR 23-27%, Sharpe 5.60-8.21, MDD 0.91-2.11% | 1 Jan-29 Mar 2024; results on AAPL, GOOGL, AMZN | About 3 months; costs not stated; no multiple-testing correction; model cutoffs not given |
| FinCon | Single-stock CR up to 82.9%, portfolio Sharpe 3.27 | 5 Oct 2022-10 Jun 2023; 8 stocks and 2 portfolios; GPT-4-Turbo | About 8 months; costs and trade counts not visible in the text read; hand-picked names |
| FinMem | TSLA Sharpe 2.68 | Oct 2022-Apr 2023 window | Fell to 0.40-0.93 on re-run (below) |
| QuantAgent | Beat random baselines on 4-hour intervals | Zero-shot tests on 9 or 10 instruments (versions and summaries disagree) | Baseline is random; audit could recover none of its five protocol fields |
| AlphaAgents | Risk-neutral multi-agent beat benchmark and single agents | 15 tech stocks, Feb-May 2024 (window per secondary summary) | About 4 months in a rally; authors say it is not yet a full portfolio optimization engine |

- TradingAgents numbers, window, tickers, absence of stated costs and of model cutoff dates; authors footnote that the top Sharpe "exceeds our expected empirical range" and attribute it to few pullbacks — [TradingAgents paper](https://arxiv.org/html/2412.20138)
- Each TradingAgents prediction takes about 11 LLM calls and 20+ tool calls — [TradingAgents paper](https://arxiv.org/html/2412.20138)
- FinCon window, tickers, model and table values — [FinCon v3](https://arxiv.org/html/2407.06567v3)
- QuantAgent's design is price-only with four agents; the v2 abstract reports 10 instruments and 4-hour intervals, another summary says 9 instruments at 1 and 4 hours, and a third-party review reports weaker results at 1-15 minutes — [arXiv v2](https://arxiv.org/abs/2509.09995v2); [papers.cool](https://papers.cool/arxiv/2509.09995); [Liner review](https://liner.com/review/quantagent-pricedriven-multiagent-llms-for-highfrequency-trading)
- AlphaAgents setup and risk-neutral result; risk-averse portfolios lagged the benchmark in the rally but had lower volatility and drawdowns (secondary summary) — [AlphaAgents](https://arxiv.org/pdf/2508.11152); [NCFA summary](https://ncfacanada.org/blackrock-tests-multi-agent-ai-in-equity-portfolios/)

**Re-tests**

- **FINSABER (strongest long-horizon evidence; authors independent of FinMem and FinAgent as far as I could tell, not verified).** Tested FinMem and FinAgent, which are LLM agents rather than full debate graphs, on historical S&P 500 constituents 2004-2024, long-only, with delisted names included and commissions at $0.0049/share — [FINSABER v5](https://arxiv.org/html/2505.07078v5)
  - On the original window FinMem's TSLA Sharpe was reported as 2.679 and reproduced at 0.927 (GPT-4o-mini) or 0.404 (GPT-4o); FinAgent made no TSLA trades — [FINSABER v5](https://arxiv.org/html/2505.07078v5)
  - No LLM agent had significant alpha (all p > 0.34); paired t-tests favour buy and hold in the composite setup — [FINSABER v5](https://arxiv.org/html/2505.07078v5)
  - Regime behaviour: "too cautious when risk is rewarded and too aggressive when it is penalised" (FinMem Sharpe -0.19 bull, -0.97 bear) — [FINSABER v5](https://arxiv.org/html/2505.07078v5)
  - Its own limits: pretrained models may have seen test data, rule baselines were not tuned per window, public data only. The abstract says "100+ symbols" while the composite tables show 63-91 per selector — [FINSABER v5](https://arxiv.org/html/2505.07078v5)
- **The Alpha Illusion (only post-cutoff TradingAgents reproduction found; position paper).** Equal-weight TSLA/NVDA/KO/XOM/MSTR, Jan 2025-Jan 2026, $100K — [Alpha Illusion](https://arxiv.org/html/2605.16895v1)
  - TradingAgents Sharpe 0.43 gross, 0.22 net; ending $106.4K gross, $102.3K net, against buy and hold $104.8K — [Alpha Illusion](https://arxiv.org/html/2605.16895v1)
  - QuantAgent Sharpe -0.96 gross, -1.15 net; ending $81.4K gross, $77.9K net — [Alpha Illusion](https://arxiv.org/html/2605.16895v1)
  - About 252 daily observations give a net Sharpe CI wide enough to span the whole gap between agent and buy and hold, so this does not prove the agents are worse — [Alpha Illusion](https://arxiv.org/html/2605.16895v1)
  - Reliability flags: the HTML rendering of Sharpe values was garbled; bps cost values and LLM models were not visible; one appendix says buy and hold beat both agents on "44 of 55 tickers", unexplained against the 5-ticker portfolio, while a summary says TradingAgents lost to buy and hold on 4 of 5 — [Alpha Illusion](https://arxiv.org/html/2605.16895v1); [alphaXiv summary](https://www.alphaxiv.org/abs/2605.16895)
- **Protocol audits.** One audit of 30 studies found costs or turnover recoverable (including partially) in 14/30, against point-in-time basis in 25/30 and artifacts in 18/30; TradingAgents' costs were not recovered and QuantAgent's fields were all not recoverable — [Execution Assumptions audit](https://arxiv.org/html/2606.08285v1)
- A second evidence map of 19 primary studies found 2/19 with extractable time-consistent splits, 1/19 with an explicit cost model, 1/19 documenting universe or survivorship handling, and 0/19 reaching its top reproducibility tier — [Agentic Trading survey](https://arxiv.org/html/2605.19337v1)
- The two audits count different samples with different coding, so their 25/30 and 2/19 are not contradictory measures of the same thing — [audit](https://arxiv.org/html/2606.08285v1); [survey](https://arxiv.org/html/2605.19337v1)
- The TradingAgents maintainers themselves call it a research scaffold rather than a strategy with a fixed, replicable return, and say two runs of the same ticker and date can differ — [TradingAgents README](https://github.com/tauricresearch/tradingagents)

**Graph versus single agent**

- General (non-finance) evidence: under matched reasoning-token budgets, single agents "consistently match or outperform" multi-agent systems on multi-hop reasoning, and budget control problems can inflate apparent multi-agent gains. Authors predict multi-agent becomes competitive when single-agent context use degrades — [Tran & Kiela](https://arxiv.org/abs/2604.02460)
- The Alpha Illusion asks that multi-agent claims report a single-agent ablation, role similarity, disagreement rate, debate-round cost and net-return delta. Its own reproduction did not report these — [Alpha Illusion](https://arxiv.org/html/2605.16895v1)

**Positive evidence worth taking seriously, none of it about graphs**

- A real-time agentic nowcasting study on the Russell 1000 from April 2025: long top 20, daily six-factor alpha 18.4 bps, annualized Sharpe 2.43, costs under 10% of gross alpha; edge only at the extreme top, and the authors note the setup cannot be reproduced. This is a single LLM doing search, not a role graph, with a short sample and no independent confirmation — [Agentic nowcasting](https://arxiv.org/abs/2601.11958)

### Inferences
- Honest verdict on alpha: **unproven and more likely small or absent net of costs for retail-size daily decisions** (moderate confidence on "unproven", low on magnitude).
- Honest verdict on decision quality: **no finance study I found tests it properly with matched budgets.** FinCon's ablations are in-sample to one short window and authored by the system's own team.
- The evidence on graphs is mostly about stock trading. **I found nothing testing LLM graphs on short-dated long options**, so its relevance to `tradingagents_pick` is by analogy, and option spreads make the hurdle harder than the costs modelled in these equity papers.
- Designs that hold up best are those separating the LLM from the final decision: LLM extracts or labels, deterministic code handles sizing, risk and execution. The Alpha Illusion recommends this, but as a position, not a proven result.
- Benchmark choice repeatedly drives claims: TSLA buy and hold had a negative Sharpe in FinMem's window, which flatters any cautious agent. Random-baseline comparisons, as in QuantAgent, set a low bar.

### Gaps
- No independent, peer-reviewed replication of TradingAgents, FinCon or AlphaAgents with a pre-registered protocol was found.
- No direct matched-compute graph-versus-single-LLM trading experiment was found.
- FinCon's cost and trade-count treatment was not visible in the portion read (about 100k of 126k characters).
- FinAgent is not a debate graph, so FINSABER tests graphs only indirectly.

## Are there independent replications or live or paper results, and is there evidence that LLM stance or news signals decay?

### Takeaway
Live evidence exists but is short, mostly single-model and uninformative about graphs; contests show dispersion, not skill. Decay evidence is suggestive: the best-known paper links falling returns to rising LLM adoption, but I found no independent measurement with a clean design.

### Cited Findings
- **Alpha Arena Season 1** (crypto perpetuals, $10K each, identical prompts, about 18 Oct-3 Nov 2025): Qwen3 Max about +22.3%, DeepSeek about +4.9%, four others negative, GPT-5 about -60%. Sources are secondary and disagree on end date — [iWeaver](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/); [Flat Circle](https://blog.flatcircle.ai/p/ai-trading-arenas)
- Alpha Arena Season 1.5 moved to US stocks; a secondary source says all models eventually lost money. I would not rely on this account, and did not find official results — [Buildix](https://www.buildix.trade/blog/nof1-alpha-arena-lessons-ai-trading-byok-strategy-advisor-2026)
- **LiveTradeBench**: 50-day live evaluation of 21 LLMs on US stocks and Polymarket, with live prices and news to prevent leakage; high LMArena scores did not imply better trading. Abstract only read — [LiveTradeBench](https://www.arxiv.org/pdf/2511.03628)
- **Lopez-Lira & Tang v6 (Oct 2025):** GPT-4 hits about 90% portfolio-day on the non-tradable initial reaction; drift is predictable mainly in small stocks and negative news; "strategy returns fall as LLM adoption grows" — [arXiv v6](https://arxiv.org/abs/2304.07619v6)
- In 2023, Lopez-Lira guessed zero predictability "by year five"; that is a forecast, not a result, and an earlier version's model implied predictability persists in equilibrium — [CNBC](https://www.cnbc.com/2023/04/12/chatgpt-may-be-able-to-predict-stock-movements-finance-professor-says.html); [arXiv v3](https://arxiv.org/pdf/2304.07619v3)
- A modelling paper puts signal half-life at about 18 months versus 5-7 years pre-AI. That is a model output from assumed parameters, not a measurement — [Meng & Chen](https://arxiv.org/abs/2605.23905)
- Valid features can still fail in a policy: an LLM news feature with held-out IC above 0.15 made an RL agent worse than a price-only baseline during a macro shock, recovering in calmer conditions; macro state variables were the most robust driver. One independent researcher; the prompt was tuned against IC, an overfitting risk — [Yang 2026](https://arxiv.org/pdf/2604.10996)
- Short-dated options costs are a large part of retail loss: more than $50M of $70M in losses over about two years on S&P 0DTE (secondary summary), though an SEC staff paper finds low costs with non-marketable limit orders, and corrects an OPRA sequencing issue, so the two are not directly comparable. A 2026 study finds large 0DTE risk premia, but costs make vol-arb Sharpe economically insignificant — [paper summary](https://medium.com/@y125789/retail-traders-love-0dte-options-paper-summary-6da4a7ff7d72); [SEC DERA](https://www.sec.gov/files/dera-hope-reasonable-prc-2503.pdf); [HKUST](https://bm.hkust.edu.hk/bizinsight/2026/04/are-0dte-options-mispriced)

### Inferences
- A tournament's winner with a two-week crypto leverage record tells you about variance. Do not use Alpha Arena rankings to choose a graph model.
- For the arena: the Lopez-Lira pattern (edge in small stocks and negative news) sits awkwardly with long options on heavily covered AI/semis names, where news is likely absorbed quickly. Plausible, not tested.
- Published-edge haircuts should be applied to anything LLM-based. The audit's one-third haircut already in the power audit may be generous for LLM stance signals (low confidence).

### Gaps
- No clean event study of LLM news signals before versus after adoption, with fixed models, was read in full. I did not extract Lopez-Lira's adoption test details or sample years.
- No audited, multi-month, real-money results from a multi-agent graph were found. Vendor and social-media claims were excluded.
- LiveTradeBench's numeric results were not extracted.

## Which graph elements could help without claiming alpha: risk veto, data-validity checks, adversarial reviewer, pre-mortem, journaling?

### Takeaway
Treat these as controls judged on errors avoided and calibration. The evidence is best for deterministic checks by reasoning (with almost no trading-specific measurement), modest for pre-mortems outside trading, mixed for LLM debate, and absent for journaling in the searches run. None justifies an alpha claim.

### Cited Findings
- **Risk control:** FinCon's within-episode CVaR control ablation is the most cited result: GOOG CR 25.1% versus -1.5%; NIO 17.5% versus -52.9%; portfolio 113.8% versus 14.7%. It is author-run on one short window and the magnitudes are implausible as a generalizable estimate — [FinCon v3](https://arxiv.org/html/2407.06567v3)
- **LLM extraction plus separate quant risk modules** is the design the Alpha Illusion recommends — [Alpha Illusion](https://arxiv.org/html/2605.16895v1)
- **Reasoning traces** add observability but are not guaranteed faithful, so should be checked against grounded inputs and realized outcomes. Memory is rarely reported with update rules, retention or deletion policies. Search methods such as MCTS raise multiple-testing risk — [Agentic Trading survey](https://arxiv.org/html/2605.19337v1)
- **Data validity:** TradingAgents' own changelog shows repeated look-ahead defects across dated paths: Alpha Vantage, FRED macro, social, decision-log memory, then filings after the run date as late as v0.7.1 (Oct 2026). It also says company identity and price grounding were fixed after reports of mismatched companies and fabricated price levels — [TradingAgents README](https://github.com/tauricresearch/tradingagents)
- **Debate:** gains appear in some benchmarks (87.91% versus 85.68% single inference in one extraction task), but one controlled study suggests part of the gain comes from aggregation, and a single persuasive adversarial agent can disrupt debate — [MADIAVE](https://arxiv.org/pdf/2510.05611); [Controlled study](https://arxiv.org/pdf/2511.07784); [Nature Sci Rep](https://www.nature.com/articles/s41598-026-42705-7)
- **Consensus gating** in one crypto paper prevents execution when debate quality is low; the search summary reports a zero-trade result rather than head-to-head performance. I could not open the paper (HTTP 403), so this is snippet-level only — [MDPI](https://www.mdpi.com/2079-9292/15/15/3453)
- **Pre-mortem:** prospective hindsight gives about 30% more reasons, but that measures quantity, not correctness. Veinott et al. found about twice the confidence reduction of pros/cons or cons-only (178 participants). A review calls the literature thin. All non-trading, and via secondary review — [Jason Collins review](https://corporate.jasoncollins.blog/premortem)

### Inferences

Evidence labels below are mine.

| Element | Plausible benefit | Evidence | How to judge without claiming alpha |
|---|---|---|---|
| Deterministic data-validity gate (timestamp <= decision time, price within quote, ticker identity, stale feed) | Stops plumbing errors reaching a decision | Strong reasoning, documented defects, no effect-size study | Count blocks; sample and audit for false blocks |
| Deterministic risk veto (max premium, event windows, spread cap) | Limits ruin at $1.2k, where one option can be a large share of the account | Reasoning; FinCon only weakly | Log would-be P&L on vetoed trades; report tail loss avoided descriptively |
| Adversarial reviewer (LLM) | May catch missed risks; could also just add noise or veto randomly | Mixed, none in trading | Veto rate, calibration, flip rate across repeated runs |
| Pre-mortem step | More risks named, lower overconfidence | Thin, non-trading | Do confidence and Brier score improve on its subset? |
| Journaling with structured forecasts | Makes calibration measurable and supports post-mortems | No study found; value is mostly measurement | Probability logged before the outcome, then Brier and calibration |

- A veto must be deterministic or at least logged shadow-style. An LLM veto cannot be judged unless the vetoed trade's counterfactual is recorded.
- Run a single-LLM control with the same token budget before crediting the graph with anything.
- **Local finding on the existing book:** `tradingagents_pick` runs analysts, bull/bear debate, trader, risk and PM on one candidate at 09:00, with Qwen quick tier and Sonnet deep tier, and trades at 10:30 with "the same execution and caps as its rules twin". Any failure means no trade (`~/code/trading-lab/docs/ARENA.md`, `~/code/trading-lab/src/tradinglab/learn/ta_runner.py`). So the graph's incremental value is really a filter on a rules candidate. Failure-to-no-trade is a safe default, but failure days should be counted because they could correlate with market stress.
- **New-version ideas (none touch frozen books, none count toward Gate v2; all exploratory, and owner approval is needed before any build):**
  - `ta_shadow_v2`: read-only sidecar logging validity-gate results and deterministic veto outcomes per `tradingagents_pick` decision, with no change to the book's orders.
  - `single_llm_budget_v1`: one LLM with the same token budget and the same candidate, as the matched control.
  - `ta_flip_probe_v1`: re-run the same frozen input N times offline to measure rating stability. A rating that flips under resampling is noise and is cheap to detect without waiting for trades. GPU runs take `~/.night-shift.lock`.
  - Log a pre-trade probability to allow Brier scoring. This gives one observation per decision, including no-trade decisions, so it accumulates faster than closed trades.

### Gaps
- No rigorous ablation showing an adversarial reviewer improves risk-adjusted trading results over a matched single agent was found.
- No trading-journal efficacy evidence was found; only one combined search touched it, and it returned nothing, so this is under-searched rather than disproven.
- Primary pre-mortem papers were not opened.

## How does point-in-time leakage in LLMs (model knowledge cutoff lookahead) work and how can it be controlled?

### Takeaway
Model weights can contain the future relative to a backtest date, and prompt-level filtering does not remove that. Forward-only runs on a model trained before the test are the cleanest control, and the frozen arena already has this property for new trades. Vintage models and logit methods are research tools with thin independent validation, and the size of the bias is contested.

### Cited Findings
- **Evidence for a large effect:** Look-Ahead-Bench reports alpha decay of -15 to -22pp for Llama 3.1 and DeepSeek 3.2 from an in-window period (Apr-Sep 2021) to a post-cutoff one (Jul-Dec 2024), while Pitinf point-in-time models were stable (+0.3 to +1.3pp) — [Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770)
- The same benchmark's limits: five large tech stocks, two 6-month windows, labelled a proof of concept, using the `ai-hedge-fund` agent framework. It evaluates proprietary Pitinf models. Its baselines also decayed: Mean Reversion -10.78pp, Random Noise -10.30pp — [Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770)
- **Profit Mirage:** "dazzling back-tested returns evaporate once the model's knowledge window ends"; proposes counterfactual perturbations (FactFin), reporting out-of-sample Sharpe 1.4x the best baseline per its own summary, no independent replication found — [Profit Mirage](https://arxiv.org/abs/2510.07920v1); [Profit Mirage PDF](https://arxiv.org/pdf/2510.07920)
- **Memorization:** reported recall of S&P 500 closes with under 1% error inside the training window and "exploding" error after it (Lopez-Lira et al., as cited; not read directly) — [Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770)
- **Evidence for a modest effect:** ChronoBERT's real-time Sharpe is comparable to state-of-the-art models, "indicating that lookahead bias is modest"; Glasserman & Lin found the distraction effect exceeded look-ahead bias in GPT-3.5 headline sentiment — [ChronoGPT](https://arxiv.org/pdf/2502.21206); [Glasserman & Lin](https://arxiv.org/html/2309.17322v1)
- These conflict in part because they test different tasks: sentiment on supplied news versus free portfolio selection on memorable tickers.
- **Anonymization has a cost:** in earnings-call sentiment with GPT-4o-mini, information loss was more severe than look-ahead effects — [Anonymization and Information Loss](https://arxiv.org/pdf/2511.15364)
- **Controls available:**
  - Vintage-trained models (ChronoBERT and ChronoGPT, with cutoffs from 1999; ChronoGPT-Instruct as a "conservative lower bound") — [ChronoGPT](https://arxiv.org/pdf/2502.21206); [ChronoGPT-Instruct](https://arxiv.org/html/2510.11677v1)
  - DatedGPT, time-aware pretraining — [DatedGPT](https://arxiv.org/abs/2603.11838)
  - Logit adjustment using two small models to forget without retraining — [Merchant & Levy](https://neurips.cc/virtual/2025/132478)
  - Lookahead Propensity, a test correlating model familiarity with forecast accuracy (Gao et al., as cited) — [Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770)
  - Real-time collection "at the edge of time", at the cost of being unreproducible — [Agentic nowcasting](https://arxiv.org/abs/2601.11958)
- **Data-layer leakage is separate from weights.** TradingAgents v0.5.0-v0.7.1 added "point-in-time integrity across every dated path" and backtests that use only data published by each analysis date, score from the first close after each decision, and fix model dates that could read later filings — [TradingAgents README](https://github.com/tauricresearch/tradingagents)

### Inferences
- Look-Ahead-Bench's headline is weaker than it reads: its random control decayed by about 10pp, so its -15 to -22pp decays are only moderately above noise in that design, with no significance test seen. The "scaling paradox" rests on 3+3 models. Pitinf is a commercial product; I did not establish whether the author has ties to it, so treat as a possible conflict until checked.
- **For the arena:** forward trades from 2026-10-29 use models trained before those dates, so weight leakage is not an issue for Gate v2 verdicts. Weight leakage bites only if anyone replays history. Any pre-2026-10-24 replay also lacks `hub.db` point-in-time guarantees, and Claude or Qwen weights may know those dates. Label such replays as exploratory.
- **Local finding on versions:** the branch this book runs (`trading-lab-claude-code`, commit e304c42) has `pyproject` version 0.4.0 and is 226 commits behind `origin/main` (0.7.1) in the owner's fork (checked 2026-11-02). Most later fixes target past-dated runs, so they should matter much less to same-day forward runs, but I did not audit them line by line. Do **not** patch the frozen book's code path; any upgrade should be a new version. **Treatment-drift risk, confirmed in code:** `ta_runner.py` calls `export_branch()` on every run, archiving the branch tip rather than a fixed commit, and a text search of `arena/FROZEN.json` found no mention of TradingAgents or a branch (23 lines). So a commit to that branch would silently change the book during the Gate v2 window. The branch's last commit is 2026-10-28, before the freeze, so no drift has occurred as of 2026-11-02. The fork also has an "hourly upstream sync" commit; I did not check whether it can touch this branch. The owner should know; any guard is a decision for them, since it touches the frozen setup.
- Practical control list for any new replay version:
  1. Prefer forward runs; pin model IDs, prompts and code hash per decision.
  2. Split results by each model's cutoff, and treat in-window results as contaminated.
  3. Probe memorization: ask the model for dated closes in the window.
  4. Run a date-shifted placebo (same structure, shuffled dates or outcomes).
  5. Use anonymized tickers as a sensitivity test, not a default, given the information loss.
  6. Enforce timestamps in code, and keep the journal or memory layer to outcomes resolved before the decision.
- Provider-hosted model silent updates are a further risk for pinned-treatment claims; log returned model IDs. This is reasoning, not a sourced finding.

### Gaps
- No independent validation of Pitinf models was found, and their training is not publicly verifiable as far as I saw.
- `From Knowing to Doing` (a memory-controlled benchmark, [arXiv 2605.28359](https://arxiv.org/pdf/2605.28359)) could not be read as fetched and may be directly relevant.
- Exact training cutoffs for GPT-4o and GPT-4-Turbo were not checked against the TradingAgents and FinCon test windows. FINSABER's general caveat stands, but whether each specific window falls inside the model's training data is unverified.

## What is best practice for testing with very small trade counts?

### Takeaway
Pre-register, test few hypotheses, read only on set dates, and compare against a randomised control. Gate v2 already does this well. Accept that `tradingagents_pick` probably cannot be judged at the first read, and gather faster non-P&L measures alongside it without treating those as alpha evidence.

### Cited Findings
- Permutation tests break the signal-return link and avoid normality and independence assumptions of t-tests, which is useful with few trades (library documentation, not primary) — [fynance guards](https://fynance.readthedocs.io/en/master/_modules/fynance/research/guards.html)
- Deflated Sharpe compares the observed Sharpe to the expected maximum across trials tried; minimum track record length gives the observations needed, and skew and kurtosis raise it, but those moments are noisy in small samples — [Wikipedia DSR](https://en.wikipedia.org/wiki/Deflated_Sharpe_ratio); [Trading Strategy glossary](https://tradingstrategy.ai/glossary/probabilistic-sharpe-ratio)
- CPCV paths overlap, so the fold count is not an effective sample size — [MinervaScore paper](https://arxiv.org/pdf/2608.23808)
- Over about 252 daily observations, a net Sharpe CI can span the whole agent versus buy-and-hold gap; the same paper uses Lo (2002) standard errors — [Alpha Illusion](https://arxiv.org/html/2605.16895v1)
- **Local:** Gate v2 pre-registers four books with a fallback graph (Bretz et al. 2009), reads on 2027-01-21 and 2027-04-15 at alpha 0.05 each, one-sided permutation p against `random_0_7dte`, a bootstrap CI, an SMH comparison, a 40% drawdown cap and 20 minimum trades. Below 20 trades a book enters with p = 1 (`~/code/trading-lab/docs/EVAL_GATE_v2.md`)
- **Local:** `tradingagents_pick` closes about 1.1 trades a week (0.6-1.5), and a +50% edge needs 21 weeks in the main model and over 24 in the harsher ones; a skill-free book loses about 13% per trade, like the random control. Weighted by plausible edges, the audit's chance of confirming any real edge by week 24 was about 11% under v1, and the Decisions row says 7% for the chosen v2 — (2026-10-28 Arena power audit; `Machine/Context/Decisions.md`)

### Inferences
- **Arithmetic for this book (mine, from the audit's rates):** 12 weeks at 0.6-1.5 trades a week gives about 7-18 closed trades, so **`tradingagents_pick` will very likely read "insufficient evidence" on 2027-01-21**. Twenty-four weeks gives about 14-36 trades, so even reaching 20 by 2027-04-15 is not assured. Its starting alpha is 13.3% of 0.05, about 0.0067, unless weights pass along the graph. An "insufficient" result would not count against the graph.
- **Illustrative size:** if per-trade return SD is about 1x premium (an assumption, not measured) and n = 26, SE is about 0.20, and 80% power at one-sided alpha 0.0067 needs an edge near +65% of premium. That is consistent in order of magnitude with the audit, and well above anything credible in the literature.
- Best-practice checklist for new versions:
  - Keep Gate v2 as is. Do not add interim peeks, and do not read the provisional table as signal.
  - Report the effect size and CI along with the verdict, and never read non-significance as "no edge".
  - Use the randomised control and SMH together; report P&L per premium with fees, at natural fills, as the gate already does.
  - Count all trials ever run, including retired prompts and books, to allow deflation later. Search-style tuning increases the number.
  - Exploit decisions as the unit where possible: logged probabilities and no-trade decisions give more observations than closed trades, for calibration only. They are not independent of market regime, and Brier skill on direction does not imply option P&L after spread and theta.
  - Use bootstrap CIs cautiously at n under about 30: percentile bootstraps tend to understate tails with lottery-like payoffs (general statistical point, not from a cited source here).
  - Use sequential, anytime-valid methods only as a separately pre-registered new version; they cost power, and would not replace Gate v2.
  - Do not start with live money at $1.2k on graph output. The evidence does not support it, and the gate's output is only a recommendation for the owner.

### Gaps
- No trading-specific evidence on e-values or anytime-valid testing was found in the single search run on it.
- Primary papers for deflated Sharpe, MinTRL and Lo (2002) were not opened; the descriptions are from secondary or library sources.
- Actual per-trade SD for `tradingagents_pick` was not measured because too few trades exist yet (the v2 window opened 2026-10-29).
