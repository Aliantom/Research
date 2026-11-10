<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# tastytrade MCP server vs our SDK path (2026-10-28)

> **TL;DR:** Use tastytrade's official MCP only for interactive read-only chat with a read-scope OAuth grant; skip it for the bot and agents (no greeks/streaming, 36-113k tokens of tools, npm audit issues).
> **Source:** trading-lab overnight 2026-10-28: read-only code review of github.com/tastytrade/tastytrade-mcp at 7f2bb63 (built and tested offline, no credentials) vs the tastyware Python SDK 13.2.3  ·  **Project:** Trading brain  ·  **Updated:** 2026-10-29

**Verdict in three sentences.** The official MCP server is a careful piece of work: its read-only mode really holds (write tools are hidden *and* refused by name, with no passthrough tool), but it defaults to the **production** account and its true safety control is the OAuth grant's scope, not the flag. It is a poor fit for the unattended bot and the overnight research agents: no greeks or streaming, one round trip per call, and 36k–113k tokens of tool definitions per session. Use it, if at all, **read-only for chatting with your account in Claude Code**, with a **new read-scope grant**, never the bot's trade-scoped one.

## What was checked
- Commit `7f2bb63` (2026-09-03), built with `npm ci --ignore-scripts`, run under an empty environment; its own 3,070 tests pass offline. No credentials, no API calls.
- **Tools:** 84 total, 70 read and 14 write (7 order tools, 7 watchlist/alert tools). Five order tools need a 60-second single-use token from a matching dry run, but the agent mints that token itself, so it's not human approval. Cancels and watchlist edits have no dry run.
- **Auth:** OAuth refresh token from environment variables, held in memory; no token files; no body logging.
- **Dependencies:** 2 direct, 113 transitive; `npm audit` shows 1 critical, 5 high (mostly in HTTP-server parts that stdio mode doesn't use). No releases; ~8 weeks without merges; 16 open items.
- **Token cost** (bytes ÷ 4, a proxy): all tools ≈ 113k tokens with output schemas, ≈ 48k without; read-only ≈ 36–89k; the ~9 tools you'd actually use ≈ 5.7k.

## Comparison

| | tastyware SDK (autopilot) | trading-lab read-only adapter | official MCP |
|---|---|---|---|
| Chains, transactions, history, futures, watchlists | yes | what we need | yes |
| Greeks / DXLink streaming | yes | yes (short-lived) | **no** |
| IV rank / market metrics | yes | yes | yes |
| Safety | our code | no write code + write calls blocked at runtime + tests | env flag + name gate; real control = grant scope |
| Efficiency | batched async | batched (40-symbol option batches) | one call per round trip |
| Token cost to Claude | none | none | 36–113k unfiltered |
| Fit: chat with the account | awkward | n/a | **good (read-only)** |
| Fit: unattended bot / research agents | best / good | good / best | poor / poor |

Things it has that our path doesn't yet use: margin/SPAN tools and a risk-free-rate tool. Things our path has that it lacks: greeks/IV per contract via DXLink.

## If you want it for chat (not applied)
Create a separate read-only OAuth grant, export it as `TT_RO_CLIENT_ID`, `TT_RO_CLIENT_SECRET`, `TT_RO_REFRESH_TOKEN`, and add an MCP server entry running `node /mnt/ai-storage/trading-lab/vendor/tastytrade-mcp/dist/index.js` with `TASTYTRADE_READ_ONLY=1` and those variables. Pin the commit, run its `doctor` to confirm no `trade` scope, and allow-list ~9 read tools. Full config snippet and file:line evidence: `/mnt/ai-storage/experiments/trading-lab-20261028-0356/artifacts/mcp-review.md`. Paperclip: DUS-25.
