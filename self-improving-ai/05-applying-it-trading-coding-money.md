<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Applying it: trading, coding, money

> **TL;DR:** Finds no verified evidence that agent trading systems beat simple baselines after costs, and warns headline prediction scores are not tradable profit.
> **Source:** Continuation of the 2026-10-24 handoff; application papers, benchmark documentation and platform policies  ·  **Project:** evolve-lab  ·  **Updated:** 2026-10-27

## A. Trading: separate information quality from investable advantage

| System | What it contributes | What its result does not establish |
|---|---|---|
| TradingAgents | Specialized analysts, bull/bear researchers, trader and risk debate; reports improvements over its chosen baselines | Robust net advantage for our universe, current models or short-dated options. [Paper](https://arxiv.org/abs/2412.20138) |
| FinMem | Profiling, layered memory and a decision module; tests how memory/character choices affect stock-trading results | That a longer memory or trader persona creates a durable edge. [Paper](https://arxiv.org/abs/2311.13743) |
| FinAgent | Multimodal market intelligence, tools, memory and dual-level reflection; reports gains across its stock/crypto datasets | That headline return statistics survive leakage, costs and a new deployment period. [Paper](https://arxiv.org/abs/2402.18485) |
| FinCon | Manager/analyst hierarchy and risk-triggered revision of textual investment beliefs | That self-critique supplies an independent reward signal. [Paper](https://arxiv.org/abs/2407.06567) |
| RD-Agent factor research | Automates hypothesis/code/evaluation cycles for data/model research, including quantitative factors | That searching more factors avoids multiple-testing bias. [Microsoft repository](https://github.com/microsoft/RD-Agent) |

Do these beat simple baselines out of sample? The papers report favorable comparisons in their experimental settings. **No verified evidence here establishes that adopting them will beat a simple baseline after costs in Alianto's future trading.** This assessment does not reject all LLM signals; it says the proposed application has not been demonstrated. A current news-headline study distinguishes a highly predictable **non-tradable initial reaction** from later drift, and reports declining strategy returns with wider adoption. This is a useful warning against treating a headline prediction score as executable profit. [Lopez-Lira and Tang](https://arxiv.org/abs/2304.07619).

Social sentiment is a candidate input, not a reward. For Reddit/X-derived features, compare the added signal against price/volume/news-only baselines, timestamp every capture, dedupe reposts and distinguish attention from directional information. Incremental profitability for this setup is **unverified**; the headline result above is not evidence that a social-media bot has the same advantage.

### Honest evaluation design

My proposed trading evaluation has these layers:

1. **Availability:** store publication time, collection time, revision time and model version. Replay only information captured before the decision. Use point-in-time constituents and include delisted securities where the strategy's universe requires them.
2. **Temporal integrity:** train/develop on earlier periods, select on later development periods, and use untouched future periods for confirmation. Embargo boundaries where labels overlap across positions. Fit normalizers and thresholds only inside each training window.
3. **Pretraining leakage:** a modern model can remember historical outcomes even if the prompt only contains old news. Do not treat “pretend it is 2023” or entity masking as a complete solution. Point-in-time models address training chronology directly; live forward logging is the strongest practical check available here. [Point-in-time LM research](https://www.nber.org/papers/w35247), [real-time benchmark rationale](https://arxiv.org/abs/2505.11065).
4. **Execution:** include commissions, bid/ask spread, slippage, latency, rejected/partial orders, contract multiplier, assignment and settlement behavior. Enter using a defensible later executable price rather than the same price that generated the signal.
5. **Multiple searches:** record every attempted prompt, factor, universe and threshold. Deflated Sharpe addresses selection effects and non-normal returns; Probability of Backtest Overfitting studies selection instability using combinations of samples. Neither substitutes for chronological forward validation or repairs poor market data. [DSR](https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf), [PBO](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf).
6. **Baselines and uncertainty:** compare against cash, buy-and-hold or a simple risk-matched strategy appropriate to the mandate. Report drawdown, turnover, exposure, net return and uncertainty, not a single Sharpe. Count inactivity as a legitimate decision. The gate is a documented procedure; a short lucky period is not proof.

The handoff's 4–6 weeks of paper trading remains a minimum operational check before any live consideration, not enough evidence by itself to establish a stable Sharpe ratio. The options bot stays on hold as requested in the handoff.

### 0–7 DTE options

Very short-dated options require contract-level execution data and settlement rules, not just stock direction. FINRA describes rapid price changes, possible total loss for buyers, greater risk for uncovered sellers and possible broker liquidation around expiration. Cash-settled index options and physically settled equity options behave differently. [FINRA](https://syndication.finra.org/content/zeroing-options-trading-strategy-0dte).

My conclusion: the current daily-price/RSS data-hub is suitable for research and extraction tasks; it does **not** supply a validated options fill simulator. A bullish news classifier with high label agreement is not a scored 0DTE trading system. Build event extraction, evidence retrieval and risk-invariant tests as independent tasks first. Keep any trade execution in the deterministic guarded executor, outside an evolutionary candidate's authority.

## B. Coding: measurable agents on small tasks

SWE-agent demonstrates that the interface for file navigation/editing/execution affects agent performance. OpenHands provides agent/runtime and benchmark infrastructure. Aider evaluates code-editing behavior against executable tests, including its Polyglot benchmark. These are useful harness references, not quality guarantees for a model on our repos. Sources: [SWE-agent](https://arxiv.org/abs/2405.15793), [OpenHands](https://arxiv.org/abs/2407.16741), [Aider benchmarks](https://aider.chat/docs/benchmarks.html).

My proposed coding loop:

- A task snapshot contains a small broken repo, issue description and fixed dependencies. The candidate gets source plus public feedback; the independent scorer keeps hidden regression tests elsewhere.
- Allow a small patch budget and two test-feedback retries. Score independently verified task success first, then regression rate, wall time, tool-call validity and patch size. Do not reward changing a test to match the buggy behavior.
- Run generated code in a disposable environment without credentials, the vault, network access or the Docker socket; mount only the task checkout and controlled scratch space. Use a separate supervisor to impose CPU/RAM/disk/process-tree limits.
- Save the diff, command trace and exact failures. Restart a candidate from a clean snapshot rather than letting unrelated failed attempts accumulate changes.
- Evolve tool format, retrieval/context packing and retry policy before allowing changes to an entire harness. Keep the supervisor, scorer and access policy outside self-editable code.

Headless Claude/Codex are already proposal routes in evolve-lab; they are bounded subscription work, not an unlimited backend. This session added an explicit `ollama:MODEL` proposal route and a train-only run flag. These prompt-only proposals have no execution tools. A general unattended code-editing agent is **not** enabled by that change.

## C. Content and realistic income experiments

MoneyPrinterTurbo connects script generation, footage selection, speech, subtitles and rendering. Its current README lists Ollama, local footage, stock providers such as Pexels and Edge TTS. This establishes integration options, not earnings. Compatibility/performance on this exact installation remains untested. Stock footage and network TTS can require external services even when the LLM is local. [Project README](https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README-en.md).

| Platform | Verified policy boundary as checked 2026-10-24 |
|---|---|
| YouTube | Its July 15, 2025 policy clarification covers repetitive/mass-produced material under “inauthentic content.” Originality and substantive value matter; an AI label does not make repetitive work monetizable. [Monetization policy](https://support.google.com/youtube/answer/1311392?hl=en) |
| YouTube disclosure | Realistic generated/meaningfully altered content must be disclosed; requirements are separate from monetization eligibility. [Current disclosure guidance](https://support.google.com/youtube/answer/14328491?hl=en) |
| TikTok | Indexed official help describes Creator Rewards eligibility in terms of original, high-quality content at least a minute long and separate AI labels. Full-page access was blocked/redirected; exact current labeling exceptions and account/program eligibility remain **unverified**. Recheck before building around payouts. [Creator Fund replacement guidance](https://support.tiktok.com/en/business-and-creator/tiktok-creator-fund-us/who-is-eligible-us), [AI guidance](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content) |
| Instagram | Current exact monetization/disclosure rules **unverified** in this pass: official help returned HTTP 429. Do not copy YouTube or TikTok eligibility assumptions. [Official policy entry](https://help.instagram.com/2635536099905516) |

My proposed content scorer checks factual sourcing, original contribution, rights/provenance, subtitle accuracy, speech intelligibility and render validity. Use real retention/watch feedback only after approved publishing; an LLM's predicted virality is not ground truth. Start with a niche where Alianto can add firsthand knowledge, such as documented Linux/AI setup experiments, rather than generating generic stock-footage advice at volume. The first useful output is one reviewable pilot, with its factual claims and asset sources attached.

### Four other home-server income hypotheses

These are proposals, not surveyed market rates or guaranteed revenue. The handoff supports Annapolis/DMV as the relevant location; demand and willingness to pay still require direct validation.

| Experiment | Small deliverable to test | Main cost/risk | How to evaluate |
|---|---|---|---|
| Local-business website repair/build packages | A verified business record and a tailored local demo | Finding customers, verifying facts and revision/support time | Paid acceptance and contribution margin per owner-hour |
| Caption/transcript cleanup for local organizations | One corrected, timestamped transcript using the existing transcription tool | Human review and handling client material | Error audit, turnaround and repeat purchase |
| Small reporting/CSV automation for businesses | One repeatable report from an example export | Integration and long-term maintenance | Verified time saved and willingness to pay |
| Tested templates/guides | A reproducible setup guide, checklist or small tool based on actual work | Distribution and support, even if generation is cheap | Qualified interest, sales, refunds and support hours |

Illustrative arithmetic, not a forecast: if a job sells for $300, has $20 direct costs and takes eight owner-hours, contribution is $35/hour before taxes and acquisition time. If 20 hours of outreach precedes that one sale, the same contribution is $10/hour across 28 hours. Expected revenue cannot be estimated honestly until conversion, price and labor are measured. GPU availability does not create demand.

## Adopt for Alianto's setup

Prioritize an audited coding/extraction task and a small site-foundry validation experiment. Let the server prepare evidence, drafts, local demos and candidate improvements. Keep publishing, outreach and live orders behind the owner's existing approval boundary. Treat financial signals and content performance as separately measurable hypotheses; do not let a convenient judge score stand in for profit, audience response or customer acceptance.
