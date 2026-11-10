<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Observability and evaluation sources

> **TL;DR:** Keep JSONL traces and add GPU CSV sampling now; pilot Promptfoo or Phoenix; skip Prometheus/Grafana, hosted tracing and LLM judges.
> **Source:** Owner request: parallel local AI workflow research  ·  **Project:** AI workstation  ·  **Updated:** 2026-10-27

Reviewed 2026-10-24. Primary-source review only; no installation, uploads, inference, or resource benchmarks. Hardware and current workflow below come from the task brief, not a fresh inventory: RTX 3080 10 GB, 16 GB RAM, 2 TB AI NVMe; Ollama, local CLI wrappers, read-only STDIO MCP, JSONL traces, restricted Docker graders, Glances/tmux/GNOME Resources. Existing 128 CLI trials found wrong keys/source rows and no clear prompt gain. That is evidence for better failure attribution and confirmation testing, not evidence that a tracing platform improves accuracy.

## Ranked decisions

| Rank | Decision | Why / integration work |
|---|---|---|
| 1 — adopt now | Keep JSONL as the durable record; join call, tool, grader, and resource records by run/case/call IDs. | Smallest addition. Preserve raw model output separately from parsed output; record exact-key/schema pass, correct source-row pass, semantic pass, timeout, and tool errors independently. These are proposed engineering choices, not vendor capabilities. |
| 2 — adopt now | Add short-lived NVIDIA CSV sampling around measured runs; keep existing monitors. | Correlates latency/errors with VRAM, utilization, temperature, and power. No new service or dashboard required. |
| 3 — pilot | Promptfoo only if its comparison matrix/reporting saves review time. | Ollama support and deterministic assertions fit. CLI wrappers need a provider adapter; do not replace the existing Docker execution boundary with unrestricted assertion code. |
| 4 — pilot | Phoenix on demand, SQLite, for a difficult multi-step trace. | UI plus OTLP collector without a separate database service is attractive. JSONL-to-span conversion/manual instrumentation is still required. |
| 5 — later | OpenTelemetry SDK spans first; standalone Collector only for multiple destinations or processing needs. | Collector routes/processes data; it does not supply the durable analysis UI. Avoid another daemon until routing is actually needed. |
| 6 — later | Langfuse on a separate host or after a measured RAM budget proves fit. | Useful broader platform, but its documented VM recommendation alone equals this workstation's entire installed RAM. |
| 7 — skip for this iteration | Full Prometheus/Grafana/DCGM stack; hosted tracing; LLM judges for exact keys/row IDs; autonomous prompt search. | Additional operations, egress, or inference do not address the known deterministic failure classes. Revisit only against a concrete unmet question. |

These rankings are inferences for this workstation. No tool's actual idle/peak RAM, disk growth, or latency overhead was measured. NVMe capacity does not establish enough RAM headroom for more services.

## Official source findings

**1. NVIDIA: use the installed driver interface.** `nvidia-smi` supports selected GPU queries and CSV output; unsupported fields can be `N/A`, and output compatibility is not guaranteed across versions. Start with `timestamp,uuid,memory.used,memory.total,utilization.gpu,temperature.gpu,power.draw` at a modest sampling interval. Check field support locally; retain units/header or record them explicitly. This measures GPU state, not task accuracy, host RAM, or per-call attribution by itself. [NVIDIA System Management Interface](https://docs.nvidia.com/deploy/nvidia-smi/)

**2. Promptfoo: useful optional evaluation UI.** YAML connects prompts, providers, test inputs, and assertions; assertions include JSON structure and custom deterministic code. Ollama is supported; `-j 1` serializes target calls, but models can remain resident during Ollama's keep-alive period. Some model-grader paths have separate concurrency behavior. Use deterministic checks here, explicit local providers, and intentional cache policy; cached output replay tests a grader, not fresh inference. [Configuration](https://www.promptfoo.dev/docs/configuration/guide/), [Ollama provider](https://www.promptfoo.dev/docs/providers/ollama/)

Promptfoo usage telemetry is on by default. Set `PROMPTFOO_DISABLE_TELEMETRY=1` and `PROMPTFOO_DISABLE_UPDATE=1` for a pilot. These controls are not a network-isolation guarantee: provider choices, sharing, and red-team generation can create separate network paths. Prefer ordinary evals and avoid cloud sync/sharing. The reviewed pages do not establish an authenticated local viewer boundary; explicitly check the installed release's bind/listener behavior before using the UI. [Telemetry](https://www.promptfoo.dev/docs/configuration/telemetry/), [Data handling](https://www.promptfoo.dev/docs/red-team/troubleshooting/data-handling/)

**3. Phoenix: the smaller tracing-server candidate.** It combines UI and OTLP HTTP/gRPC ingestion and supports SQLite. Explicitly persist its working directory/database: official pages differ on whether default SQLite resides under the working directory or a temporary directory. Defaults include `PHOENIX_HOST=0.0.0.0`, telemetry enabled, infinite retention, and built-in remote MCP enabled. For a tracing-only pilot, explicitly bind loopback, set retention, disable built-in MCP (`PHOENIX_ENABLE_MCP_SERVER=false`), and set `PHOENIX_ALLOW_EXTERNAL_RESOURCES=false` plus `PHOENIX_TELEMETRY_ENABLED=false`. This does not override separately configured model/sandbox providers. [Configuration](https://arize.com/docs/phoenix/self-hosting/configuration), [Self-hosting](https://arize.com/docs/phoenix/self-hosting/deploying-phoenix)

Authentication is disabled by default in the reviewed auth documentation; enabling it requires secret configuration and API-key changes for clients. Verify the pinned release. Keep the pilot private and separate from the existing read-only MCP server. No reliable workstation-sized RAM floor was established by these pages. [Authentication](https://arize.com/docs/phoenix/deployment/authentication)

**4. Langfuse: larger operational commitment.** Compose documentation recommends at least four cores and 16 GiB RAM for its VM deployment; this is guidance, not measured idle consumption or proof that a small pilot cannot run. Current configuration requires Postgres, ClickHouse, Redis, and event blob storage; Compose uses MinIO. UI signup creates the first user—there is no shipped default login. SDK integration, secret management, volumes, backups, retention, and upgrades remain local work. [Docker Compose deployment](https://langfuse.com/self-hosting/deployment/docker-compose), [Environment configuration](https://langfuse.com/self-hosting/configuration)

Self-hosted OSS sends deployment telemetry by default; `TELEMETRY_ENABLED=false` must reach all application containers. That does not eliminate every outbound request: update checks and browser resources have separate paths. Enterprise telemetry cannot be disabled according to current docs. [Telemetry and outbound hosts](https://langfuse.com/self-hosting/security/telemetry)

**5. OpenTelemetry: portability, not automatic visibility.** The Collector requires configured receivers/processors/exporters and enabled pipelines; SDK instrumentation or an adapter must emit spans. Localhost is the documented Collector default, though examples use `0.0.0.0`; authentication/TLS require configuration. For this stack, instrument the CLI wrapper parent span, tool/MCP children, local model call, and grader execution. A separate Collector is unnecessary for a direct SDK-to-local-Phoenix pilot. STDIO MCP stdout must remain protocol-only; diagnostics belong on stderr or separate files. The integration recommendation is inference. [Collector configuration](https://opentelemetry.io/docs/collector/configuration/)

## Measurement gate before adoption

Proposed protocol: replay existing sanitized traces into an optional UI without inference first. Measure process/container RSS, host available RAM and swap, service CPU, bytes per imported call, and manual diagnosis time. Then, only within the owner's authorized local test budget, compare a fixed baseline with one candidate change on development cases; freeze the candidate before opening the fresh one-shot confirmation bank. Compare identical cases/settings and distinguish cold model loads from warm calls. Record model digest, prompt hash, input/source hash, wrapper version, seed where supported, output limit, elapsed time, and grader version. Unknown token counts stay unknown.

Use paired outcome counts and uncertainty; do not treat repeated runs of the same case as independent new tasks. Report format compliance and correct-row selection separately so an easier JSON format cannot conceal incorrect evidence selection. A tracing UI earns adoption only if it materially reduces diagnosis/review effort at acceptable measured resource overhead; it does not earn adoption merely by showing attractive traces.
