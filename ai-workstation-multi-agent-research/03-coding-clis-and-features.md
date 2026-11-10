<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Coding CLIs and Claude Code Features/Plugins

> **TL;DR:** Claude Code, Codex CLI and OpenCode are all viable in 2026, but only OpenCode is built for provider-agnostic use with local models.
> **Project:** AI workstation  ·  **Updated:** 2026-10-27

## Part A, Key Question 1: How do Claude Code, OpenAI Codex CLI, and OpenCode compare on feature depth, extensibility/plugins, local vs. cloud model support, and robustness/maturity (as of 2026)?

### Takeaway
All three are viable in 2026 and roughly tier-1, but they trade off differently: Claude Code is the most mature/polished with the deepest built-in plugin system but is Claude-model-centric; Codex CLI is bundled into ChatGPT plans and supports local models via an `--oss` flag or OpenAI-compatible endpoints but has more usage-limit complaints; OpenCode is fully open-source and model-agnostic (75+ providers via Models.dev, native Ollama support) with a real plugin system, and has very high adoption, but benchmarks are mixed and one source flags an access-risk incident with Anthropic. For a user mixing paid Claude/OpenAI subscriptions with local models, OpenCode (or the Kilo CLI fork of it) is the only one of the three built around provider-agnosticism; Claude Code and Codex CLI are each best used against their own vendor's subscription, with local-model support as a secondary/bolted-on capability.

### Cited Findings
- Claude Code is closed-source and tied to Claude models; OpenCode is open-source and connects to 75+ providers through the Models.dev registry, including local models run through Ollama — [SSOJet: Claude Code Alternatives](https://ssojet.com/blog/claude-code-alternatives), [AgenticWire: OpenCode vs Claude Code](https://www.agenticwire.news/article/opencode-vs-claude-code)
- Benchmark claims conflict: one source puts Codex ahead of Claude Code on SWE-bench Verified (88.7% vs 87.6%); another says Claude Code leads SWE-bench Pro (64.3%); an older figure (72.7% vs 69.1%) is likely outdated — [Dupple: Codex vs Claude Code 2026](https://dupple.com/learn/codex-vs-claude-code), [InventiveHQ: codex cli vs claude code 2026](https://inventivehq.com/blog/codex-cli-vs-claude-code-2026)
- In one same-model, same-task benchmark, Claude Code finished 4 tasks in 9m09s vs. OpenCode's 16m20s, though OpenCode wrote more tests; config differs — Claude Code reads `CLAUDE.md`, OpenCode reads `AGENTS.md` + `opencode.json` — [Morph LLM: OpenCode vs Claude Code](https://www.morphllm.com/comparisons/opencode-vs-claude-code)
- Claude Code plugins can bundle skills, agents, hooks, MCP servers, LSP servers, background monitors, themes, and default settings; they are namespaced, versioned, and distributed via marketplaces (default marketplace `claude-plugins-official`, custom ones added via `/plugin marketplace add`) — per the official reference at `code.claude.com/docs/en/plugins-reference`, relayed via [Fast.io plugin guide](https://fast.io/resources/claude-code-plugins-development-guide/) and [Novita: Claude Code Plugins](https://blogs.novita.ai/claude-code-plugins-docs/)
- Codex CLI can run inference locally through Ollama, LM Studio, or MLX using the `--oss` flag or a configured profile; by default it checks for `gpt-oss-20b` via Ollama; it can also point at any OpenAI-compatible endpoint via `config.toml` — [Shashikant86 Substack: Codex CLI Running GPT-OSS and Local Coding Models](https://shashikant86.substack.com/p/codex-cli-running-gpt-oss-and-local), [DEV Community mirror](https://dev.to/shashikant86/codex-cli-running-gpt-oss-and-local-coding-models-with-ollama-lm-studio-and-mlx-403g)
- Codex CLI usage-limit complaints are the most visible criticism: one analysis counted over 100 forum/Reddit complaints about fast quota depletion, and an independent quota tracker drew on 500+ Codex users — [community.openai.com thread](https://community.openai.com/t/codex-limits-spark-frustration-among-subscribers/1390408?page=11)
- One 2026 review: Codex CLI is "already good enough to pilot seriously" but "not my daily driver yet"; a competitive analysis places Codex in the same top tier as Claude Code but says Claude Code dominates developer sentiment with a 46% "most loved" rating — [Daniel Vaughan: Codex CLI for the Sceptic](https://codex.danielvaughan.com/2026/04/19/codex-cli-for-the-sceptic-honest-answers/), [Daniel Vaughan: Codex CLI Competitive Position April 2026](https://codex.danielvaughan.com/2026/04/07/codex-cli-competitive-position-april-2026)
- OpenCode star counts and adoption are large but contested across sources: one puts it at ~112K stars (Feb 2026); another cites live GitHub API data of 191,904 stars vs. Claude Code's 139,886 (early Aug 2026); OpenCode's own homepage claims a rounder 160,000 stars, 900 contributors, 13,000+ commits, 7.5M monthly developers — figures described as trailing the live GitHub count — [LetsDataScience: OpenCode Records Rapid Adoption](https://letsdatascience.com/news/opencode-records-rapid-adoption-as-vendor-dependence-concern-2f2ff6de), [Abhs.in: OpenCode Reaches 7.5M Developers](https://abhs.in/blog/opencode-vs-cursor-github-copilot-ai-coding-agent-war-june-2026)
- Despite high stars, OpenCode's npm downloads (8,245,142/month) trail Claude Code's (44,264,901/month) by more than 5x, and OpenCode had ~4,900 open GitHub issues as of August 2026 — [Abhs.in: OpenCode vs Cursor/Copilot](https://abhs.in/blog/opencode-vs-cursor-github-copilot-ai-coding-agent-war-june-2026)
- One source mentions "an Anthropic OAuth block of OpenCode on January 9, 2026" as a dependency risk for anyone relying on Claude access through OpenCode — single-source claim, not independently corroborated in this research pass — [Abhs.in: OpenCode vs Cursor/Copilot](https://abhs.in/blog/opencode-vs-cursor-github-copilot-ai-coding-agent-war-june-2026)
- OpenCode has a plugin system; a third-party plugin, `opencode-local-provider`, adds a unified local-model provider with runtime detection across Ollama, LM Studio, llama.cpp server, and vLLM, but does not currently support API-key auth and uses OpenCode's global config rather than project-local config — [GitHub: goniz/opencode-local-provider](https://github.com/goniz/opencode-local-provider), via [theaiops Substack](https://theaiops.substack.com/p/setting-up-opencode-with-local-models)
- Claude Code has 40–80 built-in slash commands depending on the source/date counted (one 2026 cheat sheet says ~80), plus bundled "skills" that ship as slash commands (`/batch`, `/loop`, `/simplify`, `/debug`, `/fewer-permission-prompts`, `/claude-api`); `/pr-comments` was reportedly removed in v2.1.91 and `/vim` in v2.1.92 — [heyuan110: Claude Code Slash Commands 2026](https://www.heyuan110.com/posts/ai/2026-03-05-claude-code-slash-commands/)

### Inferences
- The "feature depth" and "extensibility" gap between the three is narrowing; the bigger practical differentiator for a mixed-subscription + local-model user is model-agnosticism (OpenCode/Kilo CLI) vs. vendor-bundled convenience and polish (Claude Code, Codex CLI).
- Benchmark and star-count figures across these blogs are too inconsistent (differing by date, methodology, and clear vendor-adjacency) to treat any single number as authoritative; relative ordering should be treated as roughly tied/contested rather than a clear winner.
- The single-source "Anthropic OAuth block" claim about OpenCode, if true, would be a meaningful risk factor for anyone building a stack around OpenCode talking to Claude models — this warrants direct verification (e.g., checking OpenCode's GitHub issues/changelog) before relying on OpenCode as a Claude access path.

### Gaps
- No independent security/reliability audit of OpenCode or Codex CLI was found in this pass — only vendor-adjacent blogs and marketing-driven comparisons.
- Could not corroborate the "Anthropic OAuth block of OpenCode" claim beyond one blog source.
- No official Anthropic/OpenAI head-to-head benchmark page was found; all benchmark figures come from third-party blogs with conflicting methodology.

## Part A, Key Question 2: Does a coding-agent CLI called "Kilo" (or "Kilo Code") exist?

### Takeaway
Yes — Kilo Code is a real, currently-documented agentic coding CLI (`kilo` command, npm package `@kilocode/cli`), and it is specifically built as a fork of OpenCode, making it model-agnostic and well-suited to a mixed-subscription + local-model setup.

### Cited Findings
- Kilo Code's CLI is described in official docs as orchestrating agents from the terminal, using "the same underlying technology that powers the IDE extensions" — [kilo.ai/docs/cli](https://kilo.ai/docs/cli), [kilocode.ai/docs/cli](https://kilocode.ai/docs/cli)
- Install options include `npm install -g @kilocode/cli`, curl, pnpm, bun, Homebrew, and AUR; after install you run `kilo` in a project directory — [kilocode.ai/docs/cli](https://kilocode.ai/docs/cli)
- The CLI includes two built-in agent modes switchable via Tab (a default "build" agent and a read-only "plan" agent); docs also list Architect, Ask, Debug, and Orchestrator modes; common commands include `/mode`, `/model`, `/new`, `/help` — [kilo.ai/docs/cli](https://kilo.ai/docs/cli)
- Kilo lets users pick from 500+ models and switch mid-task, paying "the model provider's rate with zero markup" — [kilo.ai/docs/cli](https://kilo.ai/docs/cli)
- Kilo CLI is explicitly stated to be "a fork of OpenCode, enhanced to work within the Kilo agentic engineering platform" — [kilo.ai/articles/best-cli-coding-agents](https://kilo.ai/articles/best-cli-coding-agents)
- Repo exists at GitHub (`Kilo-Org/kilocode`) with version info varying by mirror (pkg.go.dev shows versions from v1.0.x up to v7.3.42, published June 10, 2026) — [GitHub: Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode/), [pkg.go.dev](https://pkg.go.dev/github.com/Kilo-Org/kilocode@v1.0.21)
- Kilo CLI is explicitly grouped with OpenCode, Cline, and Aider as a "model-agnostic" AI CLI that emphasizes provider choice, BYOK, custom endpoints, and local models — [Pinggy: Top 5 CLI coding agents in 2026](https://pinggy.io/amp/blog/top_cli_based_ai_coding_agents/)

### Inferences
- Because Kilo CLI is a fork of OpenCode with a no-markup, 500+ model marketplace, it is arguably a stronger fit than vanilla OpenCode for someone who wants to pay providers directly (including local-model setups) while keeping a single CLI UX.

### Gaps
- Version numbers conflict across mirrors (v1.0.x vs v7.3.42) — could not determine which is authoritative without checking the live npm/GitHub release page directly.

## Part A, Key Question 3: Does a coding-agent CLI called "Jam" exist, or is "Jam" something else?

### Takeaway
"Jam" is not an agentic coding CLI. Jam (jam.dev) is a bug-report / screen-recording / debugging tool for web and mobile apps; it has a CLI, but that CLI scripts Jam's own recording/bug-report workflow (and ships "skills" for AI coding agents to consume Jam's debug data), it does not write code autonomously. A separate, unrelated open-source "Jam" project is an agent-manager desktop app (not a CLI, not itself a coding agent).

### Cited Findings
- Jam (jam.dev) is fundamentally a screen recorder for bugs that auto-captures console logs, network requests, repro steps, session/user details, device/OS info, and backend logs; its developers describe it as "basically a screen recorder" — [DEV Community: Jam team post](https://dev.to/jamdotdev/our-ex-cloudflare-team-built-a-tool-that-extracts-debug-data-from-screen-recordings-44ld)
- Jam's CLI is built for shell scripts, CI jobs, and AI coding agents; it reads/writes Jam data and includes a recording command; `jam skills install` writes bundled `jam-cli` and `jam-proof` skills for an agent to read — [jam.dev/docs/cli-reference](https://jam.dev/docs/cli-reference), [jam.dev/docs/cli](https://jam.dev/docs/cli)
- A separate Jam MCP plugin connects to a Jam MCP server and works with Cursor, Claude Code, GitHub Copilot CLI, and Gemini CLI — aimed at letting an agent read a Jam recording's console logs/network requests for debugging, not at autonomous coding — [mcpmarket.com: Jam Plugin](https://mcpmarket.com/server/jam-plugin)
- Jam reports "Instant Replay" (saves the last two minutes of browser activity after a bug) and integrations with Jira, GitHub, Linear, Notion, Slack; a mobile (iOS) version also exists — [jam.dev](https://www.jam.dev), [Jam blog: Launching Jam for iOS](https://jam.dev/blog/launching-today-jam-for-ios/)
- A separate, unrelated open-source "Jam" desktop app (via an Indie Hackers post) is described as a tool for managing multiple AI coding agents (Claude Code, Codex CLI, OpenCode, Cursor runtimes) from one interface — it is a desktop agent-manager/launcher, not a CLI and not itself a coding agent — [Indie Hackers: Show IH — open source AI agent manager](https://www.indiehackers.com/post/show-ih-i-built-an-open-source-ai-agent-manager-and-an-ai-agent-is-running-the-marketing-20641321b9)

### Inferences
- The user's instinct was correct: "Jam" is best known as a bug-report/screen-recording tool, not a coding-agent CLI. If the user encountered "Jam" in a coding-agent context, it was most likely either Jam's MCP integration (used by Claude Code/Cursor/etc. for debugging context) or the separate, same-named open-source agent-manager desktop app — neither of which is itself a coding agent.

### Gaps
- Could not find independent (non-vendor) reviews of Jam.dev to corroborate its own marketing usage numbers (13.7M "Jams", 200,000+ users).

## Part A, Key Question 4: What other well-regarded agentic coding CLIs turned up that the user didn't name?

### Takeaway
Aider, Google's Gemini CLI, and Sourcegraph Amp ("Deep mode") were the most consistently mentioned additional CLIs; Cursor and Cline were explicitly excluded from some "CLI" roundups as IDE-extension-first tools rather than CLI-first tools.

### Cited Findings
- Aider is repeatedly described as git-first, open-source, BYOK AI pair programming; one source reports "15B/week tokens processed through Aider" — [Pinggy: Top 5 CLI coding agents in 2026](https://pinggy.io/amp/blog/top_cli_based_ai_coding_agents/)
- Gemini CLI (Google) is named in most 2026 roundups alongside Claude Code, Codex CLI, OpenCode, and Aider as a leading tool, noted for having a free tier — [search synthesis across multiple 2026 roundups, e.g. AnalyticsVidhya](https://www.analyticsvidhya.com/blog/2026/09/top-agentic-coding-cli-tools/)
- Sourcegraph Amp ("Deep mode") is named as an honorable mention in at least one list, without a detailed review in the sources found — [Pinggy: Top 5 CLI coding agents in 2026](https://pinggy.io/amp/blog/top_cli_based_ai_coding_agents/)
- One roundup explicitly excludes Cursor and Cline from its CLI comparison, reasoning they are "IDE extensions first, CLI second" — [Pinggy: Top 5 CLI coding agents in 2026](https://pinggy.io/amp/blog/top_cli_based_ai_coding_agents/)
- Model-agnostic/BYOK CLIs are grouped together across sources as OpenCode, Kilo CLI, Cline, and Aider, contrasted with vendor-bundled subscription agents (Codex CLI, Cursor, Windsurf) — [SSOJet: Claude Code Alternatives](https://ssojet.com/blog/claude-code-alternatives), [Pinggy](https://pinggy.io/amp/blog/top_cli_based_ai_coding_agents/)

### Inferences
- For the user's stated mix (paid Claude/OpenAI subscriptions + local models), Aider is probably the next CLI worth a side-by-side trial beyond Claude Code/Codex CLI/OpenCode/Kilo, given its maturity and BYOK/local-model flexibility.

### Gaps
- No deep feature/maturity breakdown of Amp or Gemini CLI was pulled — they appeared only as list entries in roundups, not in a dedicated comparison fetch.

---

## Part B: Verification of specific terms

## Verification 1: "savvy progress"

### Takeaway
Not verified. No tool, plugin, feature, or documentation using the phrase "savvy progress" was found anywhere, in connection with Claude Code or otherwise.

### Cited Findings
- A search for the exact phrase returned no matching results tied to Claude Code; results were generic Claude Code tutorials/courses with no feature by that name — [search pass, no single citable source for the term itself]
- The two closest conceptual matches found are unrelated-by-name: "Claude HUD," a community plugin by Jarrod Watts that shows a persistent status display (context window health, active tool usage, running subagents, task progress) below the input line — [Emelia: Claude HUD Review](https://emelia.io/hub/claude-hud-plugin-review), [Mintlify: Claude HUD docs](https://www.mintlify.com/jarrodwatts/claude-hud/introduction)
- "plan-progress," a separate mod that displays live progress bars above the Claude Code prompt as a task is split into stages/steps — [search result title/snippet only; no stable primary URL captured]

### Inferences
- "Savvy progress" is likely a garbled half-memory of one of these progress/status-display tools (most plausibly Claude HUD or plan-progress), but there is no basis to assert a direct match.

### Gaps
- Could not find any source using "savvy" in connection with Claude Code, coding CLIs, or progress tracking at all. This may require the user's original source (a specific article, video, or screenshot) to resolve.

## Verification 2: "claude skins"

### Takeaway
Not an exact match, but a real, close feature exists: Claude Code added built-in custom **theme** support (not called "skins") around v2.1.118 (April 2026) — JSON theme files, built-in presets, and plugin-distributed themes that show up in a `/theme` picker. Separately, at least one community plugin does literally re-skin Claude Code's mascot graphic.

### Cited Findings
- A custom theme is a JSON file in `~/.claude/themes/<slug>.json` with a name, a base preset (dark/light/other built-in), and token overrides; edits apply live without a restart — [wmedia.es: Claude Code custom themes](https://wmedia.es/en/tips/claude-code-custom-themes)
- Users can highlight a custom theme and press Ctrl+E to open a token-by-token editor with live preview; six built-in presets are listed, including daltonized (colorblind) variants — [per search synthesis of theme guide, no single stable primary URL captured beyond the wmedia.es piece above]
- Plugins can ship themes by placing JSON files in a `themes/` directory inside the plugin package; those themes then appear in the `/theme` picker on install — [claudeissues.com #52190: docs gap re: plugin theme directories](https://claudeissues.com/issue/52190-docs-theme-customization-docs-missing-named-custom-themes-and-plugin-themes-dire)
- A GitHub issue (filed April 2026, closed May 2026) noted the official docs did not yet cover named custom themes or plugin `themes/` directories — meaning the feature existed before docs caught up — [claudeissues.com #52190](https://claudeissues.com/issue/52190-docs-theme-customization-docs-missing-named-custom-themes-and-plugin-themes-dire)
- A community plugin literally swaps Claude Code's "Clawd" mascot for seasonal/holiday looks — cosmetic only, closer to the literal word "skin" than the color themes are — [skillselion.com: clawd-theme plugin listing](https://skillselion.com/plugin/TaylorWatson/clawd-theme)
- A community repo, `Piebald-AI/claude-code-themes`, is described as a ready-to-use starting point for themes — [referenced in search synthesis; no separate primary fetch performed]

### Inferences
- "Claude skins" almost certainly refers to this theme system (terminal color palettes), or possibly to the mascot-swapping "skin" plugin specifically. Both are real; "skins" is not Anthropic's own terminology (they call it "themes"), which likely explains the mismatch in the user's memory.

### Gaps
- Did not independently confirm the exact version number (v2.1.118) or ship date against Anthropic's own changelog — this came from a third-party blog, not `code.claude.com` directly.

## Verification 3: "filetree"

### Takeaway
Real, with an exact-name match: a third-party Claude Code plugin/skill literally named **filetree** (by "nekocode") exists and maintains a `FILETREE.md` context file. It is not a built-in Claude Code feature — official docs show no native file-tree context display — but the community plugin name matches exactly.

### Cited Findings
- The `filetree` plugin (nekocode/filetree-skill) maintains `FILETREE.md` — a one-line description per file plus content hashes for staleness detection — with commands `/filetree:init`, `/filetree:update`, `/filetree:lint`; installed via `/plugin marketplace add nekocode/filetree-skill` — [claudepluginhub.com: nekocode-filetree](https://claudepluginhub.com/plugins/nekocode-filetree)
- A matching skill listing on a separate registry describes "Filetree" as shared rules loaded by the `/filetree:init`/`/filetree:update` commands, not invoked directly — [claudskills.com/skills/filetree](https://claudskills.com/skills/filetree/)
- No official Anthropic documentation for a built-in file-tree context display was found; related items found were only feature *requests* (e.g., a GitHub issue asking for a Cursor-style multi-file picker, another asking for a read-only Markdown context sidebar, another asking for a visual file explorer in the Claude Desktop Code tab) — [claudeissues.com #6271](https://claudeissues.com/issue/6271-feature-request-multi-file-context-selection-ui-similar-to-cursors-add-to-chat), [claudeissues.com #48297](https://claudeissues.com/issue/48297-feature-request-markdown-context-sidebar), [claudeissues.com #93669](https://claudeissues.com/issue/93669-feature-add-visual-file-explorer-code-browser-to-claude-desktop-code-tab)
- Third-party tools provide adjacent but separate functionality: "Smart Tree" is an MCP server giving Claude directory-tree overviews; "cltree" is a split-pane terminal tool showing a read-only file tree beside Claude Code — neither is built into Claude Code — [docs.rs: cltree 0.2.2](https://docs.rs/crate/cltree/0.2.2), [glama.ai: Smart Tree MCP server](https://glama.ai/mcp/servers/@8b-is/smart-tree/inspect)
- One (single, unofficial, partly-promotional) blog claims the Claude Code desktop app has a sidebar showing the live project directory tree — flagged as unverified/single-source — [MindStudio: Claude Code desktop app features](https://www.mindstudio.ai/blog/claude-code-desktop-app-features)

### Inferences
- "Filetree" most likely refers to the community `filetree` plugin/skill specifically (exact name match), rather than any built-in Claude Code capability.

### Gaps
- Could not verify the nekocode/filetree-skill plugin against its actual source repository (only third-party directory listings were checked) — recommend checking the repo directly before installing.
- Could not confirm or deny the single-source claim of a built-in desktop-app directory-tree sidebar.

## Verification 4: "cache tax"

### Takeaway
Partially real: "Cache Tax" is attested as the name of a community-built Claude Code mod concerned with prompt-caching costs, per one source (MindStudio blog) — but this is thin, single-source verification, not an official or widely-corroborated tool name. The underlying concept it's built on (Anthropic's prompt caching pricing — a write premium and a cheaper read, with a short TTL) is real and official.

### Cited Findings
- "Cache Tax" is described as "a mod for Claude Code built around prompt caching," whose pitch is that keeping a session warm avoids reprocessing the system prompt/history at full price, but the article stresses that warming a cache "isn't free either" and the mod does not invent the underlying caching mechanic (that's Anthropic-side) — [MindStudio: claude-code-cache-tax-cost](https://www.mindstudio.ai/blog/claude-code-cache-tax-cost) (fetched directly and confirmed)
- General prompt-cache pricing structure (not "Cache Tax" specifically): a write premium (estimates ranged ~1.25x to ~1.5x base input price depending on source) and a read discount (estimates ranged ~75% to ~90% cheaper than standard input tokens); default cache TTL reported as 5 minutes — sources here were inconsistent with each other and largely from one low-quality site (tkmxai.it.com) that republishes near-identical pages with conflicting numbers, so these figures should be checked against Anthropic's own pricing docs rather than relied on — [tkmxai.it.com cluster, multiple near-duplicate pages, treat as low-confidence]

### Inferences
- The term/tool "Cache Tax" appears to be real but niche/thinly documented (one blog, no GitHub repo or install instructions surfaced). The underlying cost dynamic it describes (cache-warming has its own token cost, so naive warming can be a net loss depending on usage pattern) is a sound and verifiable concept independent of whether "Cache Tax" the named mod is widely used.

### Gaps
- Could not find the mod's actual repository, author, or install method — only a secondary blog description.
- Could not get reliable, consistent numbers for Anthropic's actual current cache write/read pricing from this research pass; the pricing-specific sources found were low-quality and contradictory. This should be checked directly against Anthropic's official pricing page.

## Verification 5: "keepwarm"

### Takeaway
No tool is literally named "keepwarm," but the concept matches real, documented tools closely: **claude-thermos** (a Python wrapper/proxy for Claude Code that periodically replays a minimal request to keep the prompt cache from expiring) is the closest real match, and a separate tool, **pi-cachew**, explicitly offers a "keep warm" feature (for a different agent, "pi," not Claude Code).

### Cited Findings
- `claude-thermos` is an open-source Python wrapper that runs Claude Code behind a local proxy and, while a subagent is running, replays the main agent's last request with `max_tokens: 1` roughly every 270 seconds, to refresh the cached prefix before its 5-minute TTL expires; install/run via `uvx claude-thermos` — [zeli.app: Claude-thermos](https://zeli.app/en/story/49024882), [everydev.ai: claude-thermos](https://www.everydev.ai/tools/claude-thermos)
- The tool's rationale: when a main agent waits on a subagent for more than 5 minutes, its prompt cache silently expires, forcing a full re-encode at the write rate; the README reportedly attributes about 22% of total API spend across ~185 local sessions to these cache rebuilds — [everydev.ai: claude-thermos](https://www.everydev.ai/tools/claude-thermos)
- Hacker News commenters disputed the tool's universal value: one said Pro/Max plans reportedly had 1-hour cache expiries "as of today," reducing the tool's relevance for those plans — anecdotal, not independently confirmed — [referenced via search synthesis of HN comments, no stable primary URL captured]
- `pi-cachew` is a separate extension for the "pi" agent (not Claude Code) that explicitly offers "keep warm" functionality, by default only warming models that advertise caching support — [GitHub: aaalexliu/pi-cachew](https://github.com/aaalexliu/pi-cachew)

### Inferences
- "Keepwarm" is most likely the user's generic/half-remembered label for this cache-warming technique/category of tool, with claude-thermos being the most relevant real, Claude-Code-specific implementation found.

### Gaps
- Could not confirm current Claude subscription-tier cache TTLs (5 minutes vs. 1 hour) from an official source — only from a disputed HN comment thread.

## Verification 6: "blastradius"

### Takeaway
Partially real: at least two different, unrelated community skills on third-party Claude skill registries use "blast radius" in their name (one explicitly as "blast-radius" in a hyphenated slug), aimed at assessing what a code change could break beyond its diff. Neither could be verified against a primary/canonical repository, and there is no single, official "BlastRadius" plugin.

### Cited Findings
- "Cursor Plugin Pstack Blast Radius" — described as finding what a change could break elsewhere before it ships, triggered by requests like "blast radius of X"; installs as a SKILL.md auto-discovered under `~/.claude/skills/cursor-plugin-pstack-blast-radius/` — [claudskills.com: cursor-plugin-pstack-blast-radius](https://claudskills.com/skills/cursor-plugin-pstack-blast-radius/)
- "Map Blast Radius" — a separate listing with the same install pattern under `~/.claude/skills/map-blast-radius/`; description of its specific behavior was not available in the search result — [claudskills.com: map-blast-radius](https://claudskills.com/skills/map-blast-radius/)

### Inferences
- "Blastradius" is a real concept/name in the Claude Code skills ecosystem, but exists as (at least) two separate, unverified third-party listings rather than one canonical, well-known tool — the user is likely thinking of one of these two, or a similarly-named one not surfaced in this search.

### Gaps
- Neither listing's author/repository could be verified in this pass (claudskills.com is a third-party aggregator, not a primary source) — recommend checking the linked install source directly before trusting or installing.

## Verification 7: "reflect"

### Takeaway
Real: "reflect" is a fairly common name among multiple, unrelated community Claude Code skills/plugins (not an official Anthropic feature), including at least five distinct implementations found across different registries and authors.

### Cited Findings
- `cursor/plugins` "reflect" — spawns three parallel reviewers (judgment, tooling, divergent) to mine the session transcript for durable patterns, asks for approval before applying edits; installs via `npx -y skills add cursor/plugins --skill reflect --agent claude-code` — [claudemarketplaces.com: cursor/plugins/reflect](https://claudemarketplaces.com/skills/cursor/plugins/reflect)
- `alirezarezvani/claude-skills` "reflect-skill" — a lighter-weight journaling skill, described as "a light-prompt reflection skill with a single forcing question and structured journal capture"; installs via `/plugin marketplace add alirezarezvani/claude-skills && /plugin install reflect-skill@claude-code-skills` — [vibeindex.ai: alirezarezvani/claude-skills/reflect](https://www.vibeindex.ai/skills/alirezarezvani/claude-skills/reflect)
- `CodeAlive-AI/claude-code-reflection-skills` — a plugin with its own marketplace, installed via `/plugin marketplace add https://github.com/CodeAlive-AI/claude-code-reflection-skills.git`; only a Russian-language blog post was found describing it, contents not independently confirmed — [habr.com post](https://habr.com/ru/posts/986194)
- `spences10/claude-code-toolkit` "reflect" and a separate `neolabhq` "reflect" — standalone SKILL.md files; the neolabhq one "reflects on the previous response and output, based on a self-refinement framework" — [vibeindex.ai: spences10/claude-code-toolkit/reflect](https://www.vibeindex.ai/skills/spences10/claude-code-toolkit/reflect), [claudskills.com: neolabhq-context-engineering-kit-reflect](https://claudskills.com/skills/neolabhq-context-engineering-kit-reflect/)

### Inferences
- There is no single canonical "Reflect" plugin — the name is a common, descriptive choice across the community ecosystem for self-review/self-correction skills. Whichever one the user encountered, "reflect" as a category of Claude Code skill (self-review/correction-capture) is real and reasonably common.

### Gaps
- None of these five were cross-checked against their primary GitHub repos; all information comes from third-party directory/listing sites, so exact behavior should be verified against the actual repo before use.

## Verification 8: "/browser"

### Takeaway
Not verified as a real Claude Code slash command. No official or third-party slash-command reference found a `/browser` command. The real, closely-related things are Claude's browser-automation *capabilities* (Claude in Chrome, and the built-in browser pane), which are driven by dedicated MCP tool namespaces, not a `/browser` slash command.

### Cited Findings
- A search specifically for `Claude Code "/browser" slash command` returned no source documenting such a command; general slash-command references (which list 40+ to ~80 built-in commands depending on source/date) did not include `/browser` — [heyuan110: Claude Code Slash Commands 2026](https://www.heyuan110.com/posts/ai/2026-03-05-claude-code-slash-commands/), and the broader set of guides checked in the same pass
- One guide explicitly lists bundled-skill slash commands (`/batch`, `/simplify`, `/loop`, `/debug`, `/claude-api`) with no browser-related command among them — [per same search synthesis]
- `/help` is cited as the authoritative, version-specific source for what commands actually exist in an installed version — [per same search synthesis]
- Separately (not from web search, but from this session's own environment/skill listing): Claude's actual browser-control capabilities are "Claude in Chrome" (tools named `mcp__claude-in-chrome__*`, a Chrome extension acting in the user's real browser) and the "built-in browser" pane inside the desktop app (tools named `mcp__Claude_Browser__*` or `mcp__remote-devices__Claude_Browser__*` for linked cloud sessions) — these are accessed via dedicated skills/tool namespaces, not a `/browser` slash command.

### Inferences
- If the user saw something called "/browser," it most plausibly refers loosely to one of these two real browser-automation features (Claude in Chrome or the built-in browser pane) rather than an actual slash command of that exact name — but this is an inference, not a confirmed match.

### Gaps
- Could not run `/help` in a live Claude Code session to give a fully authoritative, current answer — the verdict rests on the absence of this command across multiple third-party references, which is strong but not perfectly conclusive evidence of absence.

## Verification 9: "replay theater"

### Takeaway
Not found as an exact name. No tool, feature, or plugin called "Replay Theater" turned up. Several real, differently-named tools exist for replaying/visualizing Claude Code session logs, any of which could be what the user is half-remembering.

### Cited Findings
- Apache SkyWalking's "AI Sessionizer" — a pre-alpha project offering a local, browser-based replay view that reads Claude Code's own session records to browse conversations, tool calls, and child-agent activity, without a plugin or config change; it does not re-run the model or re-execute tools — [Apache SkyWalking blog: Replay Claude Code Sessions](https://skywalking.apache.org/blog/2026-09-03-ai-sessionizer-first-look/)
- `claude-replay` (npm package, GitHub handle "es617") — converts Claude Code, Cursor, Codex CLI, and other agent session logs into interactive, shareable HTML replays; running with no arguments opens a browser editor that finds local sessions; supports `--serve --watch` to monitor sessions live — [npm/jsdelivr: claude-replay README](https://cdn.jsdelivr.net/npm/claude-replay@0.10.0/README.md), [Hacker News mirror via hn.svelte.dev](https://hn.svelte.dev/item/47276604)
- "Claude Replay" (GitHub handle "constripacity") — a different tool that passively hooks into every session, records to a local SQLite store, and adds search, metrics, and a dashboard — [glama.ai: Claude-Replay](https://glama.ai/mcp/servers/constripacity/Claude-Replay)

### Inferences
- "Replay theater" is most likely a garbled/generic description of one of these session-replay/visualization tools (most plausibly `claude-replay`'s "video-like player," given the "theater" framing), but no source uses that name.

### Gaps
- No source anywhere used the exact phrase "replay theater" — this verification rests entirely on absence-of-evidence plus plausible analogues; could not do better without the user's original source for the term.
