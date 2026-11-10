<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Graph-based memory and retrieval for a personal agent (November 2026)

> **TL;DR:** Graph memory helps mainly on multi-hop questions and fact updates, untested against BM25 + embeddings + rerank; keep hybrid search, add link expansion and a harder eval before any extraction graph.
> **Source:** Deep research assignment: graph-based memory and retrieval for agents, November 2026  ·  **Project:** AI workstation  ·  **Updated:** 2026-11-03

Evidence labels used below: **[independent]** = authors have no product among those compared, as far as affiliations show. **[vendor]** = authors sell or built a compared system. **[secondary]** = I read a write-up, not the primary data. "Inference" items are mine.

## What do independent evaluations show for GraphRAG, LightRAG, HippoRAG, RAPTOR, Graphiti/Zep, Mem0, Letta and Cognee versus BM25 plus embeddings plus reranking? Which benchmark claims are disputed?

### Takeaway
Graphs win clearly on multi-hop questions over large unfamiliar corpora (often 10 to 30 points against plain dense retrieval, in single-shot mode) and roughly tie or lose on single-hop lookups. Memory-product leaderboards are too contaminated to rank systems: the same system's score moves by more than 30 points with who ran it. I found no study that pits these systems against hybrid BM25 + embeddings + reranking, the owner's actual baseline, so the size of the gain over `ai-notes find` is unknown and has to be measured locally.

### Cited Findings

**Corpus RAG versus GraphRAG**
- RAG vs GraphRAG, Llama 3.1-8B **[independent]**: single-hop NQ F1 was RAG 64.78, Community-GraphRAG Local 63.01, HippoRAG2 61.03, KG-GraphRAG triplets+text 50.27. Multi-hop HotpotQA F1 was HippoRAG2 63.01, Community Local 61.66, RAG 60.04. MultiHop-RAG accuracy was HippoRAG2 70.27, Community Local 69.01, RAG 67.02 — [Han et al., RAG vs. GraphRAG](https://arxiv.org/html/2502.11371v3)
- Same study: 13.6% of MultiHop-RAG queries were answered only by GraphRAG and 11.6% only by RAG; integrating both improved the best baseline by 6.4% but runs both pipelines per query. Only about 65.8% (HotpotQA) and 65.5% (NQ) of answer entities existed in the extracted KG — [Han et al.](https://arxiv.org/html/2502.11371v3)
- RAGSearch (NYU Shanghai) reports a much larger single-shot gap using Qwen-2.5-7B and Contain-EM: HotpotQA dense 19.00 vs best graph variant 46.70, 2Wiki 35.53 vs 62.56, while NQ was 46.62 vs 48.31 and TriviaQA 58.60 vs 57.65. "Graph" here is the best of five variants per dataset, which flatters it — [Fan et al., Do We Still Need GraphRAG?](https://arxiv.org/pdf/2604.09666)
- RAGSearch: agentic multi-round search helps dense unevenly. Under GraphSearch dense rose on HotpotQA from 19.00 to 38.22, but the graph variant still reached 58.64. A larger model cut the average GraphRAG-Dense gap from 14.70 to 9.75 going from 7B up. HippoRAG2 was the strongest graph method on HotpotQA, PopQA and 2Wiki. Authors conclude dense stays competitive for general QA, graphs for multi-hop — [Fan et al.](https://arxiv.org/pdf/2604.09666)
- GraphRAG-Bench (ICLR 2026) opens by noting that recent studies find GraphRAG often does worse than vanilla RAG on real tasks, and asks when graphs help. I could read only the abstract; the PDF exceeded the fetch limit — [Xiang et al.](https://arxiv.org/abs/2506.05690)
- On GraphRAG-Bench Novel, a vendor reports HippoRAG2 56.48, LightRAG 45.09, HippoRAG 44.75 **[vendor, secondary]** — [FalkorDB](https://www.falkordb.com/blog/graphrag-sdk-knowledge-graph/)
- RAPTOR had the slowest online retrieval in RAGSearch's cost table (8.4 s vs about 1 s) — [Fan et al.](https://arxiv.org/pdf/2604.09666)

**Memory products**
- MemoryAgentBench: Mem0 21.1, Zep 24.0, long-context gpt-4o-mini 42.2, plain BM25 41.5. MemoryArena: Mem0 0.13, BM25 0.17, all systems at or below 0.20. LongMemEval-V2: file-based 72.5 vs strongest RAG 48.5 **[secondary; not checked against the source papers]** — [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)
- Re-evaluation of eight memory systems across five scenarios: an agentic harness managing flat text files through tool calls had the best cross-task ranking. The authors go on to propose their own harness, AutoMEM, so they are not neutral on the follow-up claim. Abstract only; no scores read — [Chen et al.](https://arxiv.org/abs/2606.04315)
- MemoryArena: agents near the ceiling on LoCoMo-style benchmarks perform poorly on interdependent multi-session tasks — [He et al.](https://arxiv.org/abs/2602.16313)
- Letta put LoCoMo history in a file with grep, semantic search, open and close tools and got 74.0% with GPT-4o mini, above Mem0's reported graph variant at 68.5%. Letta is a vendor, and it is not a grep-only result **[vendor]** — [Letta](https://www.letta.com/blog/benchmarking-ai-agent-memory)
- Mem0 graph vs base on LoCoMo, as tabulated by Zep: 68.44 vs 66.88, while full context scored 72.90 **[vendor]** — [Zep](https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/)
- Retrieval-channel ablation on LongMemEval with a strong model: embedding + lexical 95.20, embedding 94.00, grep 93.60, lexical 93.40 **[vendor]** — [Agent Zero Memory](https://arxiv.org/pdf/2608.29606)
- MemPalace audit: its 96.6% Recall@5 is attributed mainly to verbatim storage plus ChromaDB's default all-MiniLM embeddings; the palace hierarchy is flat metadata filtering; its compressed mode fell to 84.2%. Its 100% LoCoMo claim used top_k=50, effectively the whole conversation — [Dey & Viradecha](https://arxiv.org/pdf/2604.21284)
- EvalMem across seven systems: retrieval is the most common failure layer on default LoCoMo (22.1% defects vs 7.7% encoding, 6.5% generation), and a search-friendly wiki built from the memory export added 2.5 and 2.3 points on LoCoMo and LongMemEval-S — [Liu et al.](https://arxiv.org/pdf/2609.22231)
- Cognee: 0.476 correctness untuned vs 0.815 tuned on HotPotQA, and its head-to-head used 24 questions. Cognee itself says it is not an independent study; I found no third-party replication **[vendor]** — [Cognee benchmarks](https://www.cognee.ai/knowledge-graph-memory-benchmarks); [Cognee paper](https://www.arxiv.org/pdf/2505.24478)

**The disputes**
- Zep scores on LoCoMo by who ran it: Mem0 58.44 and 65.99; Zep 75.14 and 94.7; third parties 59.22, 79.09, 81.06, 85.22 **[secondary]** — [braindetox](https://braindetox.kr/posts/memory_benchmark_scores_reliability_2026.html)
- The same write-up says Zep's first claim of about 84% dropped to 75.14 after Mem0's CTO challenged category 5 being removed from the denominator but kept in the numerator. I could not confirm this from a primary record — [braindetox](https://braindetox.kr/posts/memory_benchmark_scores_reliability_2026.html)
- Zep says Mem0 ran Zep wrongly (user role on both speakers, timestamps appended rather than `created_at`, sequential searches), and that LoCoMo is too short (16K to 26K tokens per conversation) and has no knowledge-update tests **[party to the dispute]** — [Zep](https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/)
- Answer key: 99 of 1,540 errors (6.4%), so a perfect system tops out near 93.6%; the judge accepted 62.81% of deliberately wrong but topical answers. Penfield sells agent memory, undisclosed in the post — [Penfield audit](https://dev.to/penfieldlabs/we-audited-locomo-64-of-the-answer-key-is-wrong-and-the-judge-accepts-up-to-63-of-intentionally-33lg). A second audit found 7.0% wrong or ambiguous and overlapped on 40 of its 52 "wrong" flags — [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)
- Judge sensitivity on identical answers: 55.8% to 81.4% from the judge prompt alone, 12 points from the judge model alone. The Mem0 2026 prompt passed 100% of hedged multi-candidate answers. Single runs by a company selling AI products, but methods are disclosed — [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)
- Noise floor: minimum detectable difference is about 4.5 points on LoCoMo and 4 to 6 on LongMemEval, so many "state of the art" gaps of 0.3 to 1.6 points are noise. Full context with a 2026 cheap model scored 80.7% on LoCoMo and 81.6% on LongMemEval-S, about $2.51 and $14.95 — [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)
- Mem0 on LongMemEval: about 49% earlier, then 93.4% in April 2026 per one paper, 94.4 per another source — [Dey & Viradecha](https://arxiv.org/pdf/2604.21284); [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026). Zep on LongMemEval: 71.2 in its paper, 90.2 in newer claims. The dataset was also cleaned (454 of 500 haystacks replaced), so old and new scores are not comparable — [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)
- Newest state-of-the-art claims (95.60 LongMemEval, 93.60 LoCoMo) are self-reported, and 93.60 sits at the 93.6% answer-key ceiling estimated by Penfield — [Agent Zero Memory](https://arxiv.org/pdf/2608.29606); [Penfield audit](https://dev.to/penfieldlabs/we-audited-locomo-64-of-the-answer-key-is-wrong-and-the-judge-accepts-up-to-63-of-intentionally-33lg)

### Inferences
- Verdict on the objective: for this vault, an extraction-based graph is unlikely to pay back on ordinary lookup. It could pay on multi-note connection questions, on the order of single to low double digits in those categories, not overall. That range is extrapolated from dense-baseline studies on Wikipedia-style data, and the owner's baseline is stronger, so the real gain is likely smaller.
- Benchmarks that favor graphs (HotpotQA, 2Wiki) ask about strangers' facts over huge corpora. A 600K-token personal vault with curated descriptions and a generated index is a different problem. Its notes are already distilled, which removes part of what entity graphs add.
- The memory products mostly solve what the vault already solves by hand: deciding what to store and how to distill it. Mem0's and Zep's scores do not transfer to a curated note store.
- Any eval here must beat the noise floor. With 20 questions, one question is 5 points, so only large differences can show. Roughly 100 to 200 questions are needed to detect about 10 point differences by paired test (my estimate, not sourced).
- A harder eval should stop being a source-identity check. Suggested strata: multi-note questions needing 2 to 3 linked notes; paraphrases with no shared vocabulary; "what was true on date X"; superseded-note traps, where the old note is the tempting answer; aggregation ("all decisions about X"); and unanswerable questions, scored for abstention. Score recall@k of the full evidence set plus answer correctness, include a BM25-only and a full-context-of-candidates baseline, write questions without looking at retriever output, keep a reserved split (as the lab's holdout practice already does), and test the judge with deliberately wrong answers.

### Gaps
- No head-to-head of any named system against BM25 + embeddings + cross-encoder rerank was found. Most "RAG" baselines are dense-only, which likely overstates the graph gain.
- No neutral third-party rerun settling LoCoMo. No study on a personal Markdown vault.
- No reliable independent data for LightRAG in memory use or for RAPTOR reproducibility. Letta is evaluated mainly through its own filesystem experiment. GraphRAG-Bench numbers were not read.
- MemoryAgentBench, MemoryArena and LongMemEval-V2 scores come via one blog and should be checked before being quoted as primary.

## What are extraction and indexing cost, and quality with local models on a 10 GB GPU?

### Takeaway
A 600K-token vault costs a few dollars once on a hosted model, or hours to a couple of days locally, plus upkeep on every edit. The local floor is about 7B parameters; smaller models fail on structured output, and more extracted entities did not mean better answers. A 10 GB GPU can do it as an overnight batch, but quality was mediocre in the only consumer-hardware study found.

### Cited Findings
- Construction per 1M tokens on NQ: HippoRAG2 1.19 h and $2.85; HypergraphRAG 1.37 h and $3.93; RAPTOR 1.70 h and $6.38; GraphRAG 1.72 h and $13.19; LinearRAG 0.68 h and $0. Retrieval about 1 s except RAPTOR at 8.4 s. Context size: RAPTOR 814 tokens, HippoRAG2 3,229, LinearRAG 4,600, GraphRAG 22,160 — [Fan et al.](https://arxiv.org/pdf/2604.09666)
- MultiHop-RAG build time with an 8B model: RAG 135 s, Community-GraphRAG 5,560 s, KG-GraphRAG 7,702 s. Total retrieval time: RAG 1,724 s, KG-GraphRAG 14,434 s. Storage roughly equal, 117 to 165 MB — [Han et al.](https://arxiv.org/html/2502.11371v3)
- Microsoft GraphRAG via Ollama on an 8 GB GTX 1070 Ti with 32 GB RAM, on 141 text units (512-token chunks with 256 overlap): Qwen 2.5 7B took 88 min for 330 entities; Llama 3.1 took about 2.4× longer for 1,172 entities; Mistral had 649 entities and 926 relations — [Fernandes & Kanjilal](https://arxiv.org/pdf/2605.20815)
- Same study: answer quality by manual score was Qwen 3.3/5 (local search), Llama 2.7/5, despite Llama's far larger graph. Phi-4-mini (3.8B) crashed on invalid JSON after 16 entities; Mistral got stuck in repetition for 21 minutes on one case. Authors put the threshold near 7B. Local search was about 3× faster than global (about 52 s vs 156 s) with fewer hallucinations. Small corpus, manually scored, no plain-RAG baseline read — [Fernandes & Kanjilal](https://arxiv.org/pdf/2605.20815)
- Graph quality limits results: triplets-only KG retrieval held the answer string in just 39.20% of HotpotQA cases and 32.18% of NQ, vs RAG at 88.60% and 86.70% — [Han et al.](https://arxiv.org/html/2502.11371v3)
- Graphiti docs warn smaller models produce wrong schemas and ingestion failures; its Ollama guide suggests 7B+ with structured output support via `OpenAIGenericClient` — [Graphiti LLM configuration](https://help.getzep.com/v4/graphiti/configuration/llm-configuration); [Graphiti Ollama guide](https://mintlify.com/getzep/graphiti/integrations/ollama)
- Graphiti write amplification: a per-message cascade of LLM calls, reported at over 600K tokens to ingest a single LoCoMo unit (attributed by a competitor to an "independent evaluation"; I did not trace it or confirm the unit) — [Agent Zero Memory](https://arxiv.org/pdf/2608.29606)
- Graphiti backends: Kuzu is deprecated upstream; FalkorDB Lite and the LadybugDB fork allow embedded use with single-writer limits. One practitioner's write-up — [Rene Zander](https://dev.to/reneza/kuzu-is-deprecated-heres-how-i-run-graphiti-on-one-file-with-ollama-4bfk)
- LinearRAG skips relation extraction, using only entity extraction and semantic linking, with PPR over an entity-passage graph; it claims over 77% lower indexing time **[authors' claim]** — [Zhuang et al., ICLR 2026](https://arxiv.org/pdf/2510.10114)
- EHRAG also uses lightweight NER (GLiNER or spaCy) with PPR refinement **[authors' method; results not read]** — [EHRAG](https://www.alphaxiv.org/abs/2604.17458)

### Inferences
- Hosted one-time cost for 600K tokens by linear scaling of Fan et al.: HippoRAG2 about $1.71 and 0.7 h; RAPTOR about $3.83 and 1 h; GraphRAG about $7.91 and 1 h; LinearRAG about $0 and 0.4 h. The model and pricing behind those numbers apply to their setup, so treat these as order of magnitude.
- Local time by scaling Fernandes: 37 s per 512-token unit with 50% overlap gives about 2,340 units and roughly 24 h (Qwen 2.5) to 58 h (Llama 3.1) on a 1070 Ti with every stage included. A 3080 is faster, and larger chunks with less overlap cut calls, so expect about one to two nights. It would hold `~/.night-shift.lock` for that time and compete with other GPU jobs. These are extrapolations, not measurements.
- Incremental cost matters more than the first build. Dated research notes and outputs arrive daily, and global community summaries are hard to update cheaply. Per-note entity extraction with a content hash cache would be the affordable form.
- Non-LLM extraction (GLiNER, spaCy, or simply note titles and wikilinks) fits the no-heavy-services constraint best. A 7B-class local model at about 5 GB leaves little of 10 GB for a reranker at the same time, so extraction belongs in a batch.
- Always-on Neo4j is not justified. Everything needed for a small graph fits in SQLite or an in-memory matrix: this vault has only about 1,500 links.

### Gaps
- No measured Graphiti tokens per episode, or success rates with a 7B to 9B local model on a 10 GB card.
- No evaluation found of current local models (Qwen 3.x, Gemma 3/4) as extractors for this task, and no RTX 3080 data. A small trial on 20 notes would settle it.

## Which approaches handle "what was true when" and superseded notes?

### Takeaway
Bi-temporal designs that invalidate rather than delete are the right idea and the evidence supports the need: append-only stores keep serving stale facts. But the benefit comes from the time model, not the graph, and the vault can get most of it with front-matter dates and filters. Extracted facts must supplement the text rather than replace it.

### Cited Findings
- Graphiti/Zep tracks `created_at`, `valid_at`, `invalid_at` and `expired_at`; contradictions set `invalid_at` on old edges rather than deleting them, and dates are extracted by an LLM using an episode reference timestamp — [Zep key concepts](https://help.getzep.com/v2/concepts); [Graphiti package](https://pypi.org/project/graphiti-core/0.5.0/)
- Engram (single independent researcher, own system, AGPL): lossless episodes with async fact extraction, invalidate-never-delete, and as-of filtering. On full LongMemEval-S, 83.6% vs 73.2% full context at 9.6K vs 79K tokens (McNemar p < 10^-6); knowledge-update 87.5%, temporal 81.1%. Single run with no ablation, so the temporal model's own contribution is unproven — [Wang, Engram](https://arxiv.org/pdf/2606.09900)
- Engram reports that a facts-only read path loses recall because extraction drops detail; adding raw chunks restores it. Stated as a design observation, not a controlled test — [Wang, Engram](https://arxiv.org/pdf/2606.09900)
- Full context with a cheap 2026 model on cleaned LongMemEval-S: knowledge-update 75.6%, temporal 80.5%. Models and judges differ from Engram, so this is not a direct comparison — [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)
- EvalMem's dynamic benchmark: mean accuracy falls from 63.0% before a fact changes to 51.5% after (-11.5 points). Append-only retrieval systems (EverMemOS, GAM) drop most because stale records are still retrieved; recency-weighted systems (TiMem, MemoryOS) drop less — [Liu et al.](https://arxiv.org/pdf/2609.22231)
- Temporal comparison queries on MultiHop-RAG: RAG 30.70, Community-GraphRAG Local 50.60, Global 53.34. One of the few big graph wins in that study; these are about ordering across documents — [Han et al.](https://arxiv.org/html/2502.11371v3)
- Mem0's update and delete are destructive, losing the superseded value; Agent Zero treats a correction as updating belief while keeping history **[competitor's characterization]** — [Agent Zero Memory](https://arxiv.org/pdf/2608.29606)
- BEAM contradiction resolution scored at or below 0.053 for a 1M-token context model, so full context does not solve this **[secondary]** — [Coredot Today](https://core.today/blog/agent-memory-benchmarks-locomo-longmemeval-2026)
- LoCoMo has no knowledge-update tests, per Zep, so LoCoMo scores say nothing here — [Zep](https://www.getzep.com/blog/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/)
- Vault today: replaced notes get `status: superseded` and `superseded_by`; `supersede_series.py` retires dated series; the Index lists them separately and `ai-notes` skips them — vault `AGENTS.md` (local file, read 2026-11-02)

### Inferences
- The vault already has note-level invalidation, which is the coarse form of what Graphiti does at edge level. Git history adds a transaction-time record for free.
- Current behavior has a gap for "what was true when": skipping superseded notes is right for "what is true now" and wrong for historical questions. A cheap fix is an `as_of` option in `ai-notes find` that includes superseded notes, filtered by `date` and the successor's date, and labels them.
- A second gap is partial supersession: a note can be right except for one claim. Finer granularity helps most there. A small append-only claims file for the changeable facts (paths, versions, decisions, each with `valid_from`, `valid_to` and source note) would cover it without a graph database, and `Decisions.md` is already most of this for decisions.
- Point-in-time correctness is also a data leakage matter for the trading work; the `hub` tool's `as_of` already follows this pattern, so the vault would be consistent with it.

### Gaps
- No ablation found that isolates the temporal model from the rest of a system, and no independent Graphiti result on temporal questions that I could verify. A figure of 63.8% circulates via secondary pages, unconfirmed, so I left it out as a finding.
- No evidence on date extraction accuracy from local models on notes.

## Do already-linked notes (wikilinks) give a cheap graph via personalized PageRank or link expansion? What is the evidence?

### Takeaway
Plausibly yes and it is by far the cheapest experiment, but direct evidence is thin: one 20-query study of link expansion, indirect PPR results, and nothing on personal vaults. It needs no LLM and can be built in a day; measure it on the harder eval and keep it only if it wins.

### Cited Findings
- LARAG follows author-written HTML links in technical documentation, stored as chunk metadata with no graph database. Vs top-10 dense: highest macro F1, about 8 chunks and 1,527 tokens vs 10 chunks and 1,853 tokens, with latency 11.37 s vs lower for top-5 at 8.22 s. More robust on long or multi-step queries. Twenty expert queries on one product's docs, with some authors from that vendor (Rulex) — [Bolognesi et al., LARAG](https://arxiv.org/pdf/2605.07517)
- PPR on Wikipedia's hyperlink graph (pre-RAG, relatedness and disambiguation): walking the full graph beat using direct links alone, and non-reciprocal links hurt performance **[via search summary, full text not read]** — [Agirre et al.](https://www.arxiv.org/pdf/1503.01655)
- HippoRAG and successors do PPR for multi-hop, but over an LLM-extracted entity graph, seeded from the query. HippoRAG2 is the best graph method in several tests above — [LinearRAG background](https://arxiv.org/html/2510.10114v4); [Fan et al.](https://arxiv.org/pdf/2604.09666)
- LinearRAG shows relation extraction can be dropped while keeping PPR over entity-passage links, which reduces the cost of graph construction **[authors' claim]** — [Zhuang et al.](https://arxiv.org/pdf/2510.10114)
- EvalMem's search-friendly wiki built over memory exports added only about 2.3 to 2.5 points, a modest gain from auxiliary structure that also falls within common noise floors — [Liu et al.](https://arxiv.org/pdf/2609.22231)
- Measured on this vault on 2026-11-02 (my script, filename-level resolution, all `.md` outside hidden folders): 337 notes, 528,534 words, 1,494 wikilinks, 1,463 resolving (98%), 248 notes with outgoing links, 12 fully orphaned, about 4.3 resolved links per note. Top in-links: evolve-lab 81, trading brain 66, AI workstation 62, 00 Index 33. Some links are front-matter `project:` properties.

### Inferences
- Coverage is good enough to try, and link quality is probably higher than LLM triples since an author or agent chose each link deliberately. The vault's graph also has none of the 34% entity miss found by Han et al., though it has only note-level granularity.
- Hubs are the main risk. Plain PPR on this graph will drift to evolve-lab, trading brain and index pages. Countermeasures: exclude `project:` links and generated index pages from walks, or dampen by degree, and keep walks small (2 hops at most).
- Note-level links mean expansion pulls whole notes (research notes can be long). Expand to the best chunk in the linked note, scored against the query, then rerank everything together.
- Suggested design, in order: (1) take top hybrid results as seeds; (2) add the one-hop neighbors' best chunks, then feed the existing reranker; (3) only if that helps on multi-note questions, try PPR with seed weights from retrieval scores, computed in memory with scipy from a file parsed at query time or cached. Cost is effectively zero with no always-on service. Run it as an agent-callable option too (`ai-notes find --expand`), matching evidence that agent control over retrieval matters.
- Expect no effect on the current 20/20 test by construction, and possible precision loss. Ship only on a paired win on multi-note questions with no loss on single-note ones.

### Gaps
- I found no paper on PPR over authored note links for RAG without an entity step. No Obsidian or Zettelkasten retrieval evaluation with a baseline.
- No comparison of authored links vs LLM-extracted graphs on the same corpus.
- LARAG's comparison lacks a statistical test I could confirm and has no reranker in the baseline.

## Does episodic memory and lessons learned from past failures measurably improve later agent runs?

### Takeaway
Sometimes, and mostly when feedback is precise and the lesson is tied to evidence. Classic gains come from retrying the same task; cross-task gains are weakly supported, and controlled context-file studies show zero to small effects with added cost. FINDINGS.md is worth keeping only if short, evidence-linked and tested.

### Cited Findings
- Reflexion: 91% pass@1 vs 80% for GPT-4 on HumanEval, cited in later work. It is a same-task trial setting — [Dixit et al.](https://arxiv.org/pdf/2605.29463); [RPMS on trial-level methods](https://arxiv.org/pdf/2603.17831)
- Memory confabulation: agents store and repeat false self-diagnoses. Frozen environments: ALFWorld 32% (16/50), HumanEval 17% (4/23), and 46% and 82% in two other domains. In the 16 frozen ALFWorld environments, 0 of 121 reflections mentioned the correct object — [Dixit et al.](https://arxiv.org/pdf/2605.29463)
- Replacing free self-diagnosis with programmatic failure signals raised correct object mention from 0% to 86% and cut repetition rate from 0.64 to 0.10, yet solved only 3 of 16 frozen environments. Precise unit-test feedback gave the lowest frozen rate (17%) — [Dixit et al.](https://arxiv.org/pdf/2605.29463)
- Survey warning: a false "this always fails" lesson stops the agent from retesting; requiring reflections to cite failure instances gives an audit trail but does not fully fix it — [Memory for Autonomous LLM Agents survey](https://arxiv.org/html/2603.07670v1)
- AGENTS.md study (ETH Zurich / LogicStar): context files tended to lower success compared with no context and raised cost by over 20%. LLM-generated files lost about 0.5% on SWE-bench Lite and 2% on AGENTbench **[those two figures via secondary summary]**; developer-written files helped a few points but added steps and cost; files mostly compensate for missing docs — [Gloaguen et al.](https://arxiv.org/html/2602.11988v1); [summary](https://todatabeyond.substack.com/p/do-agentsmdclaudemd-files-help-coding)
- 288 runs on 17 tasks in 3 repos with Claude Code and Codex: context strategy made no measurable change to correctness, with equivalence bounds of 10 to 15 points, so moderate effects are not excluded. Failures came mostly from implementation skill, and a real AGENTS.md never turned a near miss into a pass — [Khatri](https://arxiv.org/abs/2607.27250)
- MemoryArena's 766 multi-session tasks: all methods had low success, and external memory returned compressed or reordered information that fit poorly with the agent's in-context learning **[via summaries, success numbers not read]** — [He et al.](https://arxiv.org/abs/2602.16313); [summary](https://www.emergentmind.com/topics/memoryarena)
- A matched backend study on MemoryArena says its evidence does not establish statistical significance or a causal effect of any single mechanism — [MemoryLake](https://arxiv.org/pdf/2608.13883)
- Databricks reports accuracy rising from 2.5% to over 50% after 62 log records on enterprise data tasks **[vendor, secondary, benchmark details unseen]** — [Designing Agentic Memory in 2026](https://thenuancedperspective.substack.com/p/designing-agentic-memory-in-2026)

### Inferences
- Likely useful: lessons from deterministic checks (scorer output, test failures, ledger facts), which match the low-confabulation condition. Risky: free-text "why it failed" written by the agent that failed, which is what a FINDINGS.md can easily become.
- Rules for FINDINGS.md and Ledger use: each lesson cites a run or ledger line; records the evidence type; gets a date and a re-test or expiry trigger; negative "never do X" lessons get periodic retesting; keep the file short, because context files carry a cost even when correct.
- Retrieve episodes on demand instead of loading them all. The Ledger is a searchable trace; it should not be injected wholesale.
- This is measurable here. Evolve-lab can run a paired test: the same held-out workflow tasks with and without FINDINGS.md, or with old vs pruned versions, scored on task outcome, tokens and steps. Expect a small effect, so repeated trials are needed; the `experimenter` agent's pre-registration fits this.

### Gaps
- I found no rigorous controlled study of lessons memory across different tasks in real agent workflows, and none measuring harm from stale lessons directly.
- No study of Markdown findings files specifically; the context-file studies are the nearest analog, and those are repo instructions rather than failure lessons.
