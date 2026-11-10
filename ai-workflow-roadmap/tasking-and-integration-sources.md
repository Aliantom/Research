<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Tasking and integration sources

> **TL;DR:** Adopt task briefs, cited read-only MCP results and lexical vault retrieval before adding any new interface or agent framework.
> **Source:** 2026-10-24 parallel investigation of practical local AI workflow improvements  ·  **Project:** AI workstation  ·  **Updated:** 2026-10-27

Research checked 2026-10-24. Seven primary documentation pages support the facts below. Rankings, proposed checks, and hardware priorities are recommendations, not measured findings. No software was installed, configuration changed, inference run, or vault material uploaded. System details supplied by the coordinating agent: Ubuntu, RTX 3080 10 GB, 16 GB RAM, 2 TB NVMe, Ollama 0.40.10, existing CLI clients and four read-only STDIO MCP tools. Documentation describes current releases; exact behavior on installed versions remains to be checked locally.

The most useful next layer is a repeatable task contract and small evidence bundle around the existing tools. A new interface or agent framework would add maintenance before establishing whether it improves completed work.

## Ranked roadmap

| Priority | Change and fit | Cost / main risk | Next measurable check |
|---|---|---|---|
| Adopt now | Task brief: objective, allowed inputs, writable paths, completion criteria, time/token budget, output artifact. Use existing workflow folders for recurring jobs. | Small authoring effort; instructions can become too long. | Run three ordinary tasks with the same brief shape; record clarifications, interventions, successful criteria, and elapsed time. |
| Adopt now | Preserve the four read-only MCP tools; add bounded, cited context results before adding capabilities. | Small schema/wrapper work; retrieved notes can contain instructions that should be treated as data. | Every tool result identifies file and excerpt; outside-root and symlink-escape requests fail. |
| Adopt now | Lexical vault retrieval: filenames/front matter, then `rg`, then bounded excerpts. | Existing CLI tools; synonyms may miss relevant notes. | Ten owner-relevant questions, with expected source notes; count source-in-top-five and unsupported claims. |
| Pilot | Native Ollama schema output plus independent validation for machine-consumed results. | Small API wrapper; valid JSON can still contain incorrect answers. | Fixed fixtures including missing evidence and malformed tool results; report schema validity and task correctness separately. |
| Pilot | One worktree per code-changing task, plus actual process permissions. | Extra checkout/dependency storage; a worktree does not enforce access limits. | A disposable task changes only its branch/files; review diff and deliberately test denied writes/network. |
| Pilot, only if chat tasking remains awkward | Local Open WebUI chat against the existing Ollama service. | Another service, account/data backup and updates; extra background requests. | Compare three identical chat tasks with CLI; keep only if navigation/reuse improves without unwanted model loads or memory pressure. |
| Later | SQLite FTS5 index, then optional semantic retrieval over an explicitly chosen subset. | Index invalidation and embedding maintenance; stale or irrelevant snippets. | FTS5 first: compare the same ten retrieval questions. Add embeddings only if lexical misses justify it; include renamed/deleted-note checks. |
| Later | More RAM or VRAM, triggered by the bottleneck on a chosen workload. | Hardware cost and compatibility; capacity alone does not fix task quality. | Record GPU placement, peak memory, swap and latency on the real task before any purchase decision. |
| Skip for now | Whole-vault ingestion, unrestricted shell MCP, autonomous scheduling, multi-agent framework migration, giant context defaults. | Expands permissions, context and maintenance before a reliable task baseline exists. | Reconsider only against a named failed task and a bounded comparison. |

## What the sources establish

**Instructions, skills, and MCP solve different parts of tasking.** OpenAI describes `AGENTS.md` as durable project guidance, skills as reusable workflows with instructions and optional scripts/references, and MCP as access to tools or context providers. Skills use progressive disclosure instead of loading all their content initially. [Official OpenAI customization documentation](https://learn.chatgpt.com/docs/customization/overview).

Recommendation: retain the vault's Human/Machine rules as the local authority. Keep one canonical workflow body, with small client-specific discovery wrappers only where needed; verify discovery separately in Claude, OpenCode and Codex. Do not assume those clients load the same file names, precedence, or skill locations. An MCP tool should expose a small operation, while the skill explains when to use it and how to verify its result. A plain local script needs no MCP wrapper unless cross-client discovery or a strict interface materially helps.

**Permissions require enforcement beyond prose.** Codex documentation separates OS sandboxing, network controls, and approval policies; Linux enforcement uses `bwrap` and `seccomp` in current documentation. These are documented capabilities, not a claim about the active session or other clients. [Official OpenAI agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security).

Recommendation: audit each launcher rather than copying settings between clients. Test a temporary denied write and denied network operation. Give tools explicit roots, result-size limits, timeout/error behavior and a narrow operation schema. Treat “read-only” metadata as a description until server behavior is checked. Retrieved text must not authorize shell actions or change vault instructions. Keep provenance fields small: tool name/version, canonical path, source hash or modification time, excerpt location and truncation flag. Avoid logging secrets or complete note bodies by default. Publishing, sending and other external side effects still follow the owner's approval rule.

**Worktrees separate edits and branches.** Git supports multiple working trees attached to the same repository, including detached worktrees for experiments. [Git worktree manual](https://git-scm.com/docs/git-worktree).

Recommendation: use them for real code repositories, with a task branch and reviewable diff; they share repository administration and are not a security boundary. They also do not capture uncommitted changes from the original checkout automatically. Do not make the Obsidian vault a repository or reorganize its notes merely to adopt this pattern. For a file-only trial, use a bounded staging directory and produce a patch before applying changes.

**Local structured outputs already have a direct route.** Ollama documents JSON schema in the native API's `format` field, and validation with Pydantic. It recommends grounding the prompt with the schema and lowering temperature for consistency. [Ollama structured outputs](https://docs.ollama.com/capabilities/structured-outputs).

Recommendation: use a native API adapter where the client's compatibility layer does not forward the schema. Validate required keys, types, extra fields, tool allowlists and arguments before execution. Separate syntactic compliance from correct tool selection, faithful evidence, and successful completion. Report unsupported/refused/timed-out output distinctly instead of silently repairing it. Keep one bounded repair attempt and preserve both attempts for evaluation. No claim is made here that the installed version or every CLI path forwards the schema correctly.

**Retrieval can start without embeddings.** SQLite FTS5 provides full-text queries, ranking through BM25, and highlighted excerpts/snippets. [SQLite FTS5 documentation](https://www.sqlite.org/fts5.html).

Recommendation: first try direct filename and exact-text search. An optional FTS5 index can store canonical path, front matter, headings, text, hash and modification time outside the vault; return the top few short excerpts and then read their originals. Update changed files and remove deleted/renamed entries. A later semantic index should use a local embedding model over an allowlisted subset, keep per-chunk provenance, and demonstrate better retrieval on the same questions. Search accuracy and answer accuracy are separate checks. Indexing is not permission to edit Human notes.

**Open WebUI is an interface option with deployment tradeoffs.** Its quick start supports Linux, Docker and Python deployment, persistent chat/settings storage, and connecting the container to an existing host inference service. Its slim variant reduces the download but requires external providers for features such as embeddings and document processing; current slim RAG also requires PostgreSQL/pgvector. [Open WebUI quick start](https://docs.openwebui.com/getting-started/quick-start/).

Recommendation: pilot chat only, locally bound, using existing Ollama rather than a second bundled inference server. Do not select slim assuming that full RAG comes with no extra services. Pin a release and plan data backup if adopted. Add no terminal integration or vault upload in the initial comparison. Treat this as optional convenience for reusable conversations, not a prerequisite for agent work or an automatic improvement to correctness.

**Memory demand grows with context and concurrency.** Ollama documents GPU/CPU placement via `ollama ps`, request queuing when memory is insufficient, memory growth from parallel contexts, and explicit model unload/keep-alive control. [Ollama FAQ](https://docs.ollama.com/faq).

Inference/recommendation: the 10 GB GPU and 16 GB system RAM favor one active inference job and a tested context size; 16K presets should remain measured choices. Extra RAM may reduce host pressure but is not equivalent to extra VRAM. More VRAM is relevant when the required model/context spills from GPU; more NVMe capacity mainly helps storage headroom rather than token generation. Quantization can trade quality for fit, so compare task correctness as well as speed. No specific hardware purchase is justified by this documentation-only review.

## Suggested first trial

Use one small, repeatable existing task, one model, the current four tools, a compact task brief and a bounded evidence output. Measure successful completion, unsupported claims, intervention count and total elapsed time. Change one layer at a time: schema enforcement, retrieval, then interface. Retain failed examples alongside successful ones. This determines which missing piece is real before selecting a product project or replacing the current stack.
