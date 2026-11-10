<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# GPU rental price indices as a lead indicator for AI-compute names

> **TL;DR:** Untested idea: daily GPU rental price indices as a lead indicator for AI-compute stocks; collect the free indices from now and test after ~60 trading days.
> **Source:** trading-lab method card knowledge/methods/gpu-rental-price-leadlag.yaml (overnight 2026-10-28, from verified swarm leads)  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-28

**Thesis:** Daily GPU rental prices (H100/B200 hourly) measure marginal AI-compute demand before it shows up in reported revenue, so sharp moves may lead NVDA, CRWV and SMCI.

**Fit:** Directly tied to AI-compute demand; most relevant to GPU clouds (CRWV), server makers (SMCI) and NVDA.

**Evidence**
- A free daily GPU rental price index aggregated from 11 public sources exists, with history in git (short history). ([source](https://github.com/ewyluda/gpu-price-index); anecdote)
- A second free index of GPU rental and AI token prices publishes daily CSV/JSON history under CC BY 4.0. ([source](https://github.com/renshuBTC/compute-screener); anecdote)

**Failure modes:** very short history, rental prices may lag rather than lead equity prices, index methodology changes, low liquidity of the rental market itself.

**Costs and feasibility at $1.2k:** Free data; trading via shares or defined-risk spreads; no special frictions beyond normal spreads. Feasible as a filter on existing books; not a standalone strategy at $1.2k until tested.

**Test plan:** Collect both indices daily from now; after >= 60 trading days, test whether 5-day changes in the index predict next 5-20 day excess returns of NVDA/CRWV/SMCI vs SMH, out of sample, with a shuffled-index placebo.

**Scores:** edge 2, evidence 1, feasibility 3 (Evidence is two community repos with short histories; there is no published test of predictive value.)
