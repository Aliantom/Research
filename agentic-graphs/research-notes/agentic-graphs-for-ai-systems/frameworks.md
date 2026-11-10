<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Agent graph orchestration frameworks and durable engines (as of 2026-11-02)

> **TL;DR:** Single-host solo setup: keep the Python runner, SQLite, worktrees and Paperclip; Claude workflows only for fan-out in a job; DBOS or Burr only for a real branching pipeline; skip CrewAI, AutoGen.
> **Source:** deep-research assignment on agent graph orchestration, 2026-11-02  ·  **Updated:** 2026-11-03

Evidence labels used throughout:
- **[Vendor]** is a claim from the party selling or maintaining the thing.
- **[Competitor]** is a vendor writing about a rival. Diagrid sells a competing product.
- **[Measured]** is my own measurement on this PC on 2026-11-02 (Python 3.14.4, clean venv, `import` only, no LLM call, so a floor and not a runtime figure).
- **[Local]** is read from the owner's machine or repos.

## How do the options differ on state, checkpoints, retries, human approval and parallelism?

### Takeaway
They fall into four kinds: graph libraries that checkpoint between nodes (LangGraph, Agent Framework, Burr, Pydantic graph, CrewAI Flows), durable engines that journal steps and replay code (Temporal, Restate, Inngest, DBOS), Claude-native orchestration (subagents, dynamic workflows, Agent SDK), and DSPy, which optimizes prompts and is not an orchestrator. The engines, LangGraph and Agent Framework document a pause for human input stored with their durable state. Dynamic workflows explicitly have no mid-run human input.

### Cited Findings

**Comparison table.** "nv" means not verified this session (see Gaps), not "absent".

| Option | State and checkpoint | Retries and crash recovery | Human approval | Parallelism | Source |
|---|---|---|---|---|---|
| LangGraph 1.2 | Checkpoint per super-step; durability modes `exit`, `async`, `sync`; SQLite saver for local use, Postgres for production | Finished sibling outputs kept as pending writes; replay re-runs nodes after the checkpoint, including LLM calls; retries nv | `interrupt()` plus `Command(resume=...)`; the node restarts from its beginning on resume | Parallel branches; parallel interrupts resumed by ID map | [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers), [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) |
| Pydantic AI graph | `pydantic_graph`; older API still carries an early-beta note; beta builder API is the newer one. Agent `StepPersistence` snapshots steps without an engine | Durable only through a plugged-in engine, which journals model and wrapped tool calls | Page says durable workflows can wait hours or days; no mechanism detail on that page | Beta API advertises parallel execution | [Durable overview](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/index.md), [Beta graph](https://pydantic.dev/docs/ai/api/pydantic_graph/beta) |
| Apache Burr | State written after each action; SQLite persister; can fork from any app, partition and sequence ID; state must be JSON-serializable | Resume with `resume_at_next_action`; retries nv | Modelled as a state that waits for input (chatbot example); no named feature | Separate concept page, nv | [Burr persistence](https://burr.apache.org/docs/concepts/state-persistence/) |
| Microsoft Agent Framework (Python 1.24) | Checkpoint at each superstep end; memory, file or Azure Cosmos stores; pickle with a restricted unpickler | Resume or rehydrate from a checkpoint; topology and executor IDs must match | Pending requests and responses are part of the checkpoint | Superstep model; concurrent orchestration builder | [MS Learn checkpoints](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints) |
| AutoGen | Maintenance mode, README advises against production use | n/a | n/a | n/a | [AutoGen repo](https://github.com/microsoft/autogen) |
| CrewAI Flows | Pydantic state; `@persist` saves to a database; `id` input resumes; `restore_from_state_id` forks | Docs mention resume after a crash | Docs say persistence lets a Flow "wait for human input"; no feature detail on that page | `kickoff_async` for long work | [CrewAI production docs](https://docs.crewai.com/en/concepts/production-architecture.md) [Vendor] |
| Claude subagents | Results live in Claude's context window | Interruption restarts the turn | Normal permission prompts | A few delegated tasks per turn | [Workflows doc table](https://code.claude.com/docs/en/workflows) |
| Claude dynamic workflows | JS script; results in script variables; saved per run under `~/.claude/projects/` | Replays saved results by agent start order; stalled agents restart up to 5 times; failed agent reruns itself and everything started after it | None mid-run. Docs: run each stage as its own workflow for sign-off | 16 concurrent by default, 1,000 agents per run, 4,096 items per `pipeline()`/`parallel()` | [Workflows doc](https://code.claude.com/docs/en/workflows) |
| Claude Agent SDK / `claude -p` | Sessions resume and fork; `--resume <id>` | API retry events; SIGTERM leaves the turn unfinished, resume does not continue it unless `CLAUDE_CODE_RESUME_INTERRUPTED_TURN=1` | `canUseTool`, `--permission-prompt-tool`, hooks | Subagents | [Headless doc](https://code.claude.com/docs/en/headless), [SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) |
| DSPy 3.4 | Compiled program saved and reloaded; GEPA `log_dir` resumes from last checkpoint | Optimizer-level only | None found | nv | [GEPA docs](https://dspy.ai/api/optimizers/GEPA), [Optimizer guide](https://dspy.ai/diving-deeper/choosing-an-optimizer/) |
| Temporal | Replay engine; event history capped at 51,200 events or 50 MB, warning at 10,240 or 10 MB; 2 MB per payload | Retry details nv; workflow code must be deterministic | Signals and timers in the journal survive redeploys | Yes | [Beri comparison](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost) (secondary, cites vendor docs) |
| DBOS | Library; steps recorded in SQLite (default) or Postgres | Completed step never re-executed; uncaught exception ends as `ERROR` and is not recovered; `DBOSStepNondeterminismError` on divergence | `DBOS.recv(topic, timeout_seconds)` with `DBOS.send`; `None` on timeout; docs use this as a payment approval example | Queues with concurrency control; child workflows; `asyncio.gather` in deterministic order | [Workflow tutorial](https://docs.dbos.dev/python/tutorials/workflow-tutorial), [Communication](https://docs.dbos.dev/python/tutorials/workflow-communication), [DB connection](https://docs.dbos.dev/python/tutorials/database-connection) |
| Inngest | Single binary; in-memory Redis with SQLite snapshots by default; reported 1,000 steps per run, 4 MiB per step, 32 MiB run state | Executor handles retries | `waitForEvent` | Flow-controlled queue | [Self-hosting](https://www.inngest.com/docs/self-hosting); limits via [Beri](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost) (single source) |
| Restate | Single binary server; replay journal | Durable timers and promises survive crashes [Vendor] | Awakeable: durable promise with a callback ID, agent suspends, resolved by HTTP (curl works locally) | nv | [Restate HITL](https://docs.restate.dev/ai/patterns/human-in-the-loop) |

**Details that change decisions**
- LangGraph under `exit` durability leaves "no record of the thread" after a mid-run crash. Before the first durable checkpoint a thread looks never-invoked, so the docs advise recording admission in your own store first — [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers).
- LangGraph code before `interrupt()` re-runs on every resume, so side effects there must be idempotent — [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts).
- Dynamic workflows run on replay order. If B fails in A, B, C, D, a relaunch returns A from cache and reruns B, C and D even if C and D finished — [Workflows doc](https://code.claude.com/docs/en/workflows).
- A stalled workflow agent's restart loses its transcript, and "Files the stalled attempt already changed stay changed" — [Workflows doc](https://code.claude.com/docs/en/workflows).
- A fresh Claude session cannot relaunch a workflow run; it starts over. `claude --resume` of the same session is required — [Workflows doc](https://code.claude.com/docs/en/workflows).
- The Temporal integration in Pydantic AI re-runs approval listeners on replay, so their external effects must be idempotent — [Pydantic docs, via search summary](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/).
- Pydantic AI supports Temporal, DBOS, Prefect, Restate, Lambda, Absurd, pgtask and Airflow as durability backends, one per agent — [Durable overview](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/index.md).
- Replay engines require model calls inside steps and no clock, random, network or file reads outside them — [Beri](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost). DBOS states the same determinism rule — [DBOS tutorial](https://docs.dbos.dev/python/tutorials/workflow-tutorial).
- Trigger.dev's co-founder argues against replay for coding agents with working directories, preferring append-only logs and machine snapshots. He is a competing vendor, and this is reported second-hand — [Beri](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost).
- A critique says Agent Framework checkpointing is not durable execution, and long runs should pair with the Azure Durable Task extension. This is a secondary blog summary — [search result set](https://www.developersdigest.tech/blog/microsoft-agent-framework-developer-guide-2026).

**Production evidence**
- Replit says each Agent is its own Temporal Workflow, and that migrating the control plane took a couple of weeks [Vendor case study] — [Temporal/Replit](https://temporal.io/resources/case-studies/replit-uses-temporal-to-power-replit-agent-reliably-at-scale).
- Temporal lists OpenAI, Lovable, Replit, Cursor and Retool as builders on its platform [Vendor] — [Temporal AI page](https://temporal.io/ai). A claim that Codex specifically runs on Temporal did not verify.
- A Sept 2026 LangChain forum post reports per-node Postgres checkpoints did allow crash resume, but live runs surfaced problems tests missed — [LangChain forum](https://forum.langchain.com/t/fixed-graph-vs-llm-supervisor-lessons-from-building-a-7-step-paper-writer-in-langgraph/4582.md).

### Inferences
- The graph libraries' checkpoint and the engines' journal solve different problems. A checkpoint saves state and needs something else to notice the run died and restart it. On this PC, systemd plus the existing runner already do that part.
- None of these journals capture filesystem state. For agents editing a git worktree, a replayed step acts on a tree already changed by the failed attempt. A git commit or reset at each node boundary has to be written regardless of framework. This is the gap Claude's docs admit for stalled agents and the argument Trigger.dev makes.
- Dynamic workflows fit a fan-out inside one job. They do not fit a pipeline with an approval stop, since sign-off forces separate runs, which matches the existing Paperclip gate between stages.

### Gaps
- Retry policy details for LangGraph, Burr and Agent Framework, parallelism in Burr and Restate, and Pydantic graph's persistence API were not read directly.
- No named-company incident report for LangGraph was found. The one titled postmortem ([Towards AI](https://pub.towardsai.net/langgraph-checkpointing-is-not-free-a-production-postmortem-398bc86861f4)) returned HTTP 403, so only its search snippet was seen: checkpoint schema changes need explicit migration, and old threads can silently break.
- No independent benchmark comparing these frameworks was found.

## What do they actually add over a plain Python runner with SQLite and git worktrees?

### Takeaway
For a single-host solo setup whose nodes are long CLI subprocesses, mostly small things: replay-safe step recording, a durable wait primitive, a graph visualizer and time travel. The runner already owns scheduling, locking and allowlisting. The most credible add-on is a library such as DBOS or Burr, adopted only for a pipeline that really has branches and approvals. Any server engine duplicates roles held by systemd and Paperclip.

### Cited Findings
- The existing runner is a systemd timer running `night/night.py` in `~/code/evolve-lab`. `night/` is about 4,250 lines of Python with allowlisted job types, a `claude_tasks` job with concurrency options, SQLite reads and `~/.night-shift.lock` [Local].
- DBOS gives exactly-once `send` from workflows, and step records so completed steps never re-run — [Communication](https://docs.dbos.dev/python/tutorials/workflow-communication), [Tutorial](https://docs.dbos.dev/python/tutorials/workflow-tutorial).
- Durable sleep persists the wakeup time, so long waits survive restarts — [DBOS tutorial](https://docs.dbos.dev/python/tutorials/workflow-tutorial).
- LangGraph adds time travel (replay from a prior `checkpoint_id`) and parallel interrupt handling — [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers), [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts).
- Dynamic workflows add concurrency caps, cached prefix sharing across a fan-out, schema-validated agent output with 5 attempts, stall restarts and a `/workflows` view — [Workflows doc](https://code.claude.com/docs/en/workflows).
- Saving state does not by itself resume anything: "nothing will notice if the workflow has stopped" [Competitor] — [Diagrid checklist](https://www.diagrid.io/blog/langgraph-agent-production-checklist).
- Plain-loop opinion: a 2026 comparison says most production teams start on a framework and later move to custom Python, and frames it as setup speed versus control. This is one blog's unsourced generalization, not data — [bswen](https://docs.bswen.com/blog/2026-03-18-raw-python-vs-langgraph-for-ai-agents).
- A dependency-free graph runtime of about 400 lines exists, which shows how small the core concept is [author's claim] — [simple-graph-agents](https://pypi.org/project/simple-graph-agents/).
- Costs of adoption seen in the docs: LangGraph checkpoints accumulate and need pruning — [Durable execution page](https://docs.langchain.com/oss/python/langgraph/durable-execution). Agent Framework rehydration fails if executor identities change — [MS Learn](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints). Temporal self-hosting is a multi-service cluster, with one third-party estimate of 0.25 to 1.0 FTE for a small production cluster — [Beri](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost).

### Inferences
What a plain runner needs to write itself, in rough order of value:
1. A `runs`/`steps` SQLite ledger with a unique key per step, written before and after each step.
2. A commit in the worktree at each successful step, and `git reset --hard` plus a clean to the last commit on retry. This handles the filesystem gap no framework covers.
3. An explicit transition table, which is the "graph" itself. A dict of state to next state is enough for under about 10 states.
4. An approval state that creates a Paperclip issue and exits. A later timer tick checks the issue and continues. The process does not sit waiting, so there is no durable-wait problem to solve.
5. A retry budget per step, plus classification of failures (usage limit, stall, bad output).

Likely what a framework would really earn on this setup: replay correctness that is already tested, parallel join handling, and a trace UI. That is worth adopting only once a pipeline has several branches and joins, or when the hand-written ledger starts to accumulate bugs. These are my judgments, not sourced findings.

Role rule check:
- **Temporal, Restate, Inngest** each add an always-on scheduler and queue that overlaps systemd timers and Paperclip.
- **DBOS** as a library overlaps only the hand-written ledger, so it can replace it cleanly.
- **Dynamic workflows** own fan-out inside one Claude job and need no overlap with the runner.
- **DSPy** owns prompt optimization, offline, and overlaps nothing here.

### Gaps
- No controlled study compares frameworks with hand-written runners on reliability. The evidence is opinion and first-person accounts.
- I did not audit the night runner's retry or step-resume code, so which of the above it already has should be checked before any decision.

## Which work well with local Ollama models and subscription CLIs rather than API keys?

### Takeaway
All the graph libraries can call a CLI, since a node is just a function; the engines can too, since a step is too. So the CLI question really concerns their model abstractions, which go unused, and subscription terms. Claude subscription use of `claude -p` and the SDK is currently allowed and draws on plan limits, but there is a trap: `--bare` ignores subscription login and is slated to become the `-p` default. Ollama is natively supported by LangGraph's ecosystem, Pydantic AI, Agent Framework and DSPy; the one-model-at-a-time limit has to be enforced by the orchestrator.

### Cited Findings

**Claude subscription terms and mechanics**
- Current policy per Anthropic support: signed in with a plan, "the Claude Agent SDK and `claude -p` still draw from your subscription limits". The June 15, 2026 plan to change this was paused. Oct 7, 2026 added monthly API credits for Max, Ultra and Team, which apply when using a linked Console API key — [Anthropic support](https://support.claude.com/en/articles/15036540).
- The docs page in some locales may still state the old planned credit system, so sources conflict. The support article's dated updates are the most recent official wording — [Korean docs copy](https://code.claude.com/docs/ko/agent-sdk/overview) versus [support](https://support.claude.com/en/articles/15036540).
- The SDK overview says third-party developers may not offer claude.ai login or rate limits in their products, and points to API keys — [SDK overview](https://code.claude.com/docs/en/agent-sdk/overview).
- Anthropic's Legal page, as quoted by a third party, says subscription login is "designed to support ordinary use", and that it doesn't prevent "an end user from signing in to the unmodified Claude Code binary with their own Claude subscription" — [autonomee](https://autonomee.ai/blog/claude-code-terms-of-service-explained/). Not checked against the original.
- **Trap:** "In bare mode, Claude Code never reads OAuth credentials or the system keychain", and "`--bare` ... will become the default for `-p` in a future release" — [Headless doc](https://code.claude.com/docs/en/headless).
- `claude -p` starts in Manual mode from v2.1.302, so calls needing approval are denied unless allowed; `--permission-prompts none` exists for unattended runs — [Headless doc](https://code.claude.com/docs/en/headless). This PC runs 2.1.316 [Local].
- Workflows in `-p` show no prompt; they need a `Workflow` or `Workflow(<name>)` allow rule, auto mode, bypass or a hook. The `ultracode` keyword does not trigger from a `-p` prompt — [Workflows doc](https://code.claude.com/docs/en/workflows).
- A workflow pauses for a usage-limit reset only in an interactive subscription session. Under `claude -p` or the SDK the affected agent fails instead — [Workflows doc](https://code.claude.com/docs/en/workflows).
- `--output-format json` with `--json-schema` gives structured output, but check that `structured_output` exists before using it. `total_cost_usd` is a client-side estimate — [Headless doc](https://code.claude.com/docs/en/headless).
- Usage limits have no scriptable query, per a GitHub issue — [claude-code #44328](https://github.com/anthropics/claude-code/issues/44328) (seen in search summary only).

**Codex**
- `codex exec` reuses saved CLI auth. OpenAI's docs call API keys "the right default for automation" and ChatGPT-managed auth an advanced option for trusted runners: "Use this path only if you specifically need to run as your Codex account" — [Codex non-interactive](https://learn.chatgpt.com/docs/non-interactive-mode).
- It offers `--json` JSONL events, `--output-schema`, `codex exec resume <id>`, read-only sandbox by default and `--sandbox workspace-write` — [Codex non-interactive](https://learn.chatgpt.com/docs/non-interactive-mode).
- `codex` was not on the login shell PATH here during the check, though a binary exists under an nvm-style path [Local]. A systemd unit needs an explicit path.

**Framework CLI bridges**
- Community LangChain wrappers (`claude-code-langchain`, `langchain-claude-agent-sdk`, `langchain-claude-cli`) wrap the CLI as a chat model. All are third-party; one warns that built-in tools plus bypass permissions turn prompt injection into code execution — [PyPI: claude-code-langchain](https://pypi.org/project/claude-code-langchain/), [langchain-claude-cli](https://pypi.org/project/langchain-claude-cli/1.0.0/), [langchain-claude-agent-sdk](https://pypi.org/project/langchain-claude-agent-sdk/).
- Agent Framework ships packages named `claude`, `ollama`, `github_copilot` and others in its repo; their auth behaviour was not read [Local read of [repo tree](https://github.com/microsoft/agent-framework/tree/main/python/packages)].

**Ollama**
- Pydantic AI has an Ollama model doc in its repo [Local read of [repo docs](https://github.com/pydantic/pydantic-ai/tree/main/docs/models)]. A tutorial says Ollama 0.5+ gets schema-valid `NativeOutput`, unverified against official docs — [localaimaster](https://localaimaster.com/blog/pydantic-ai-ollama-agents).
- DSPy's docs reference `ollama_chat` in its language model guide — [DSPy LM docs](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/learn/programming/language_models.md). GEPA and MIPROv2 can spend "hundreds of dollars" of hosted calls per compile, so local reflection models are community practice, not official guidance — [Optimizer guide](https://dspy.ai/diving-deeper/choosing-an-optimizer/).
- CrewAI: the community forum has many Ollama threads, including "CrewAI not Working with Ollama" (Jan 2026) and LiteLLM issues, with resolutions not seen — [forum](https://community.crewai.com/c/community-support/7?page=1). A practitioner write-up reports 2 to 4x local latency — [Enterprise DNA](https://enterprisedna.co/resources/blog/practitioner-crewai-production).

### Inferences
- The clean pattern is a node or step that runs `subprocess.run(["claude","-p",...,"--output-format","json","--json-schema",...])` and writes results to the ledger. Wrapping the CLI as a chat model discards the CLI's own tools and session handling, and adds a third-party dependency for little gain.
- The runner should set the auth path explicitly and test it after each Claude Code update, given the bare-default warning. A default flip would surface as authentication failures in overnight runs.
- `claude -p` usage-limit behaviour means the runner must classify rate-limit failures itself and reschedule. Workflow auto-pause does not help unattended.
- Codex subscription automation is permitted but discouraged in OpenAI's wording. Treat it as less stable ground than Claude's.
- GPU exclusivity: a concurrency setting of 1 on an Ollama queue plus `~/.night-shift.lock` is enough. No framework reviewed advertises model-swap awareness, though I did not check exhaustively.

### Gaps
- Whether `CLAUDE_CODE_OAUTH_TOKEN` or a `claude setup-token` token works under `--bare` is not stated on the page read. The docs say only the API key or `apiKeyHelper`. Needs a local test.
- Quantitative plan-limit behaviour under automated use is not published in anything found.
- Whether `codex --oss` or Ollama works with `codex exec` is not on the page read.
- Official Ollama limits for tool calling in each framework were not found. Local-model tool-call quality is likely model-specific.

## Maintenance health, license, footprint on 16 GB RAM, known failure modes and criticism

### Takeaway
Nearly everything is actively maintained; AutoGen is the exception and should be excluded. Python library memory is trivial on 16 GB (under 80 MB each at import), so RAM does not decide this. Server daemons add more, but no reliable figures were found. License matters only mildly for internal use (Inngest SSPL, Restate BSL). CrewAI failed to install on this PC's Python 3.14.

### Cited Findings

**Health snapshot from the GitHub API, 2026-11-02.** Each repo name links to its source. Commits are for the last 12 weeks where the stats API returned data.

| Repo | Stars | Open issues + PRs | License | Latest release | 12-week commits |
|---|---|---|---|---|---|
| [langgraph](https://github.com/langchain-ai/langgraph) | 44.3k | 442 | MIT | 1.2.19, Oct 30 | 223 |
| [pydantic-ai](https://github.com/pydantic/pydantic-ai) | 21.0k | 1,772 | MIT | v2.64.0, Oct 30 | 100+ since Oct 1 (API page cap) |
| [burr](https://github.com/apache/burr) | 2.6k | 110 | Apache-2.0 | 0.43.0-incubating, Aug 29 | n/a, pushed Nov 2 |
| [agent-framework](https://github.com/microsoft/agent-framework) | 14.5k | 885 | MIT | python-1.24.0, Oct 30 | 1,013 |
| [autogen](https://github.com/microsoft/autogen) | 61.7k | 1,130 | Detector reports CC-BY-4.0 (repo also holds docs; code license not checked) | python-v0.7.5, Sept 2025 | 2 |
| [crewAI](https://github.com/crewAIInc/crewAI) | 60.4k | 994 | MIT | 1.15.34, Nov 1 | 373 |
| [dspy](https://github.com/stanfordnlp/dspy) | 38.9k | 751 | MIT | 3.4.1, Oct 12 | 183 |
| [temporal](https://github.com/temporalio/temporal) | 24.1k | 1,127 | MIT | v1.32.1, Oct 8 | 629 |
| [dbos-transact-py](https://github.com/dbos-inc/dbos-transact-py) | 1.7k | 10 | MIT | 3.4.0, Oct 28 | 67 |
| [inngest](https://github.com/inngest/inngest) | 6.0k | 276 | SSPL with Apache 2.0 future license | v1.49.0, Oct 23 | 100+ since Aug 10 (cap) |
| [restate](https://github.com/restatedev/restate) | 4.6k | 475 | BSL 1.1 | v1.8.1-hotfix.2, Nov 2 | 100+ since Aug 10 (cap) |
| [claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 8.4k | 610 | MIT (usage under Commercial Terms) | v0.2.176, Oct 31 | 169 |

- Claude dynamic workflows are described in [search results citing the docs](https://code.claude.com/docs/en/workflows) as research preview. The page fetched in this pass carried no such label, so the current status is unclear. Docs list frequent behaviour changes by version (v2.1.271, v2.1.305 and others).
- AutoGen's README: "AutoGen is now in maintenance mode", contributions limited to fixes, "as it transitions to archived, we continue to advise against production use" — [AutoGen README](https://github.com/microsoft/autogen). GitHub does not yet mark it archived.
- Agent Framework 1.0 GA dates to April 3, 2026 per secondary sources — [AgenticWire](https://www.agenticwire.news/article/microsoft-agent-framework-1-0-workflows-mcp).
- Restate's use grant reportedly permits internal production use but forbids a public platform service; Inngest's SSPL is reportedly fine for internal use — [Beri](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost). This is a blogger's reading, not legal advice.

**Footprint [Measured]** (venv size, import RSS; no agent actually run)

| Package | Import | Venv | RSS |
|---|---|---|---|
| langgraph | `langgraph.graph` | 86 MB | 79 MB |
| pydantic-graph | `pydantic_graph` | 27 MB | 25 MB |
| pydantic-ai-slim | `pydantic_ai` | 55 MB | 66 MB |
| burr | `burr.core` | 35 MB | 27 MB |
| dspy | `dspy` | 325 MB | 68 MB |
| agent-framework-core | `agent_framework` | 39 MB | 19 MB |
| dbos | `dbos` | 77 MB | 74 MB |
| crewai | failed | n/a | n/a |

- CrewAI failed to build on this PC: `tiktoken` wheel build failed on Python 3.14.4. Its pyproject declares `requires-python = ">=3.10, <3.14"` [Measured] — [crewAI repo](https://github.com/crewAIInc/crewAI).
- The Temporal server: one forum post from roughly three years ago reports about 112 to 150 MB idle, deployment type unclear — [Temporal forum](https://community.temporal.io/t/reduce-memory-footprint-of-temporal-process/9083). An open issue reports frontend goroutine and memory growth under `start-dev` — [temporal #6323](https://github.com/temporalio/temporal/issues/6323).
- Machine context: 16 GB total with about 10 GB available during this check, before an Ollama model loads or a Claude fan-out starts [Local].

**Known failure modes and criticism**
- LangGraph: the in-memory saver loses state on restart, and docs mark it non-production — [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers). Postgres `thread_id` must stay under 255 characters — [Durable execution page](https://docs.langchain.com/oss/python/langgraph/durable-execution). Default serialization can't handle all objects; `pickle_fallback=True` is the opt-in — [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers).
- LangGraph security: SQLite checkpoint SQL injection CVE-2025-67644 (CVSS 7.3) and msgpack deserialization CVE-2026-28277 (CVSS 6.8), with upgrade to `langgraph-checkpoint` 3.0+ advised; maintainers treat the latter as post-exploitation — [SecNews](https://www.secnews.gr/?p=714913). Seen via search summary; verify against the advisories.
- A LangGraph "write amplification" and runaway loop cost warning appears in a Chinese-language guide — [Shareuhack](https://www.shareuhack.com/posts/langgraph-production-agent-guide-2026).
- Agent Framework: pickle-based stores are a trust boundary; "Never load checkpoints from untrusted" sources. Cosmos is the store labelled for production — [MS Learn](https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints). v1.13.0 changed checkpoint ordering, with minor breaking changes — same source.
- CrewAI: `@persist` works at workflow boundaries and saves no internal agent reasoning, and saving state does not resume execution [Competitor] — [Diagrid](https://www.diagrid.io/learn/crewai-durable-execution). A community thread reports `@persist` not working as expected — [CrewAI forum](https://community.crewai.com/t/issue-with-persist-decorator-not-working-as-expected/5479). Verbose stdout logging by default hurts production performance, per a secondary write-up — [Enterprise DNA](https://enterprisedna.co/resources/blog/practitioner-crewai-production).
- DBOS: uncaught exceptions are not recovered, and code changes to in-flight workflows need its upgrade procedure — [Tutorial](https://docs.dbos.dev/python/tutorials/workflow-tutorial). Docs recommend Postgres for production, on the stated grounds that a SQLite file cannot serve multiple servers — [DB connection](https://docs.dbos.dev/python/tutorials/database-connection).
- Temporal: Quo documented moving self-hosted Temporal to Cassandra, and cost estimates of $2,500 to $4,500 a month appear for small production clusters; both reported second-hand — [Beri](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost).
- Inngest: self-hosted support is not guaranteed — [Self-hosting](https://www.inngest.com/docs/self-hosting). The 1,000-step cap would limit long agent loops, per one source — [Beri](https://www.beri.net/article/temporal-vs-inngest-vs-restate-vs-dbos-durable-execution-agent-cost).
- Claude dynamic workflows: a mid-fan-out failure reruns finished work, runs are tied to their session, the script cannot touch files or import modules, and a run over 25 agents gets only an advisory warning — [Workflows doc](https://code.claude.com/docs/en/workflows). `pipeline()` silently gives `null` for an agent that failed, so scripts must check — same source.
- `claude -p` runs repo hooks and `.mcp.json` servers in untrusted folders without a prompt unless `--bare` is used — [Headless doc](https://code.claude.com/docs/en/headless). This matters when worktrees contain code from elsewhere.

### Inferences
Suggested shortlist for this PC. This is my judgment for the report writer, not a sourced finding.

| Decision | Option | Why |
|---|---|---|
| Keep | Runner + SQLite ledger + worktrees + Paperclip | Already owns the roles, and subprocess nodes need no model abstraction |
| Use inside jobs | Claude subagents and saved workflows | Fan-out and cross-checking within one job, drawing on plan limits. Avoid depending on resume |
| Add only for prompt tuning | DSPy | Owns a separate offline role; run on local models to avoid a compile eating the plan |
| Trial if a real branching pipeline appears | DBOS on SQLite, or Burr | No server. Postgres advice rests on multi-server use, which doesn't apply on one host. Run a `kill -9` test first, as Beri recommends. DBOS has a small community and one vendor; Burr has infrequent releases |
| Trial second | LangGraph with `SqliteSaver` and `durability="sync"` | Largest ecosystem, time travel, but brings the most concepts and a checkpoint security history |
| Skip | Temporal, Restate, Inngest | Add a daemon and overlap systemd and Paperclip. Their scale benefits don't apply to one host |
| Skip | Agent Framework | Active, but production path leans to Azure; no SQLite store listed for Python checkpoints |
| Skip | CrewAI | Install failed on this Python, role-play abstractions add no durable guarantees here |
| Exclude | AutoGen | Maintainer advises against production use |

Star counts are a poor signal here: AutoGen has the most stars and the least maintenance. Also, 16 GB constrains parallel `claude -p` processes and Ollama far more than it constrains any orchestration library. The RSS of concurrent Claude Code processes was not measured.

### Gaps
- No reliable idle RAM numbers for Restate or Inngest, and none current for Temporal. None were run here, since installing daemons was out of scope. A 30-minute measurement would settle it.
- Runtime memory for each library during real graph runs is not measured. The numbers above are import floors, and lazy imports likely understate some (dspy, agent-framework).
- `Pydantic AI` and `Burr` issue trends and criticism were not specifically investigated. No substantial independent criticism surfaced in the searches run, which is not evidence of absence.
- No independent benchmark or engineering postmortem with numbers was found for any of the 14 options. Comparison content online is dominated by vendors, notably Diagrid, and SEO blogs.
- The Beri comparison is by an individual with no stated vendor tie, though its Restate pricing came from a third-party mirror.
