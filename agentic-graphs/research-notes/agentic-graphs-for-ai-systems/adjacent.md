<!-- Generated from the Obsidian vault (Machine/Research). Edit the vault note, not this file: mirror_research.py overwrites it. -->

# Adjacent methods for a solo developer's AI workflows (November 2026)

> **TL;DR:** Best-evidenced additions need no new service: check-gated cascades, deterministic and mutation gates, deterministic lead matching, sandboxed workers. Langfuse and speculative decoding rank low.
> **Source:** deep-research assignment on adjacent AI workflow methods, 2026-11-02  ·  **Updated:** 2026-11-03

Scope excludes graph frameworks, graph memory and prompt optimizers. "Local check" means something I observed on this PC on 2026-11-02. Nothing here was benchmarked on this PC; every gain figure comes from someone else's setup.

## Objective: ranked additions with cost and fit

### Takeaway
The best-evidenced additions need no new service: gate cheap work on checks that execute, tighten the gates on night workers, and fix site-foundry's matching with deterministic rules before any LLM. Heavy observability (Langfuse) and speculative decoding rank low on this box.

### Cited Findings
Evidence behind the ranking is cited in the sections below. The table is my judgment, so it sits here as a summary rather than as new facts.

| Rank | Addition | Role owner | New service? | Cost | Evidence |
|---|---|---|---|---|---|
| 1 | Check-gated cascade for local work: run local model, run an executed test or 3-sample agreement, escalate on failure | local-delegate agent / existing scripts | No | Script time; some extra local GPU time | Medium: several papers, one independent-author measurement, conflict noted below |
| 2 | Deterministic gates on night-shift diffs, with mutation testing scoped to changed code | night-shift runner | No | Mutation tool install; CPU time at night | Medium: strong on the problem, thin on agent-level outcome |
| 3 | Fix lead matching with deterministic rules, LLM only on ambiguous pairs (DUS-52) | site-foundry | No | Hours of code | Medium for the pattern; none specific to Google Places or local leads |
| 4 | Sandbox for unattended workers plus stop-on-denied and timeouts | Claude Code / night-shift runner | No (`bwrap`, `socat` installed) | Lower success, more tokens | Medium: one strong preprint on the cost |
| 5 | Schema-constrained local output, with free-form reasoning first and semantic validation after | existing Ollama callers | No | Small code edits | Medium: syntax benefit is firm, semantic risk from a vendor |
| 6 | Deterministic web QA first (axe, Lighthouse), LLM vision as a second pass on screenshots | site-foundry | No (CLI on demand) | npm tools, minutes per site | Weak to medium; figures disagree |
| 7 | Transcript-to-eval mining from existing session logs | evolve-lab | No | A script | Weak: motivated by failure data, no direct efficacy study found |
| 8 | Claude Code telemetry with a console or Prometheus exporter, or short-lived Phoenix | Off until needed | No, or one on-demand process | Low RAM if on demand | Docs are solid; value here is unproven |
| 9 | CAN-SPAM lint and small, personalized batches for owner-approved drafts | site-foundry, Paperclip approves | No | A linter | Legal rules firm; reply data vendor-sourced |
| 10 | Selective spec-first work for new features only | griller/slicer agents already cover it | No | Planning and review time | Mixed |
| Skip for now | Langfuse self-host; speculative decoding through llama-server; learned or commercial routers; Splink | n/a | Would add services or complexity | n/a | See sections below |

### Inferences
- Items 1 to 4 all build on things already here: `local-delegate`, the `mutation_report` night job (local check: `~/code/evolve-lab/night/mutation_report.py`), DUS-52, and installed `bwrap`/`socat` (local check).
- Item 3 has the most direct money link, because Now.md records that the first verification run missed chains and over-matched generic names.
- Paperclip is the approver for items 2 and 9, and systemd timers schedule anything recurring. None of the top items needs a new role.
- Night-shift Claude is capped at 30 sessions until 2026-11-04 (Now.md), so items that spend local CPU or GPU rather than hosted sessions are the better first tests.

### Gaps
- No source measured these additions together, or on a 3080 with 16 GB RAM. Ranking is a judgment call, not a measured result.
- A small pre-registered trial through the `experimenter` agent would be needed before claiming any gain from items 1 or 5 here.

## Agent observability and tracing that works locally: what's light enough for 16 GB RAM?

### Takeaway
Claude Code already exports metrics, events and beta traces with no server if you use the console or Prometheus exporter, and its transcripts are on disk. Phoenix is light enough to run on demand; Langfuse's multi-service stack is a poor fit for this box.

### Cited Findings
- Claude Code telemetry is off until `CLAUDE_CODE_ENABLE_TELEMETRY=1`; metrics exporters are otlp, prometheus, console, none, and logs exporters are otlp, console, none. Prometheus metrics are scraped from `localhost:9464/metrics` — [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage)
- Traces are beta and need `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` plus `OTEL_TRACES_EXPORTER`. Span hierarchy: `claude_code.interaction` to `claude_code.llm_request` and `claude_code.tool`. Detailed hook spans require organization allowlisting in interactive sessions — [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage)
- Metrics include sessions, lines of code, commits, cost (USD), tokens by type, edit decisions and active time. Events include prompts, tool results and decisions, API errors and refusals — [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage)
- Content is redacted by default: prompts, responses, tool details and tool content each need their own opt-in variable. `OTEL_LOG_RAW_API_BODIES=file:<dir>` writes full request and response JSON to disk with an `index.jsonl` — [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage)
- Third-party guide: metrics export every 60 seconds and events every 5 seconds by default, and the cost metric is approximate, so billing data is the authority — [Better Stack guide](https://betterstack.com/docs/logs/claude-code/) (search summary; defaults not re-checked against the official page)
- Langfuse self-host runs web and worker containers plus Postgres, ClickHouse, Redis/Valkey and S3. One hosting guide reports about 1.0 to 1.6 GB idle per container and advises capping the Node heap at 3 GB — [Railway Langfuse template](https://railway.com/deploy/langfuse-observability.md) (hosting vendor, single source, not an official spec)
- Phoenix: one hosting guide lists a 512 MB minimum, 1 GB recommended and 2 GB+ for heavy volume. It queues up to 20,000 spans at about 50 KiB each, which works out to roughly 1 GB if the queue fills — [Railway Phoenix template](https://railway.com/deploy/phoenix.md) (hosting vendor, not an official spec)
- Phoenix runs as one container on SQLite, with UI and OTLP/HTTP on 6006 and gRPC on 4317. SQLite data is lost if a container has no volume — [Railway Phoenix guide](https://railway.com/deploy/arize-phoenix-observability)
- Phoenix licensing conflict: described as source-available under Elastic License 2.0, while another source calls it open source — [Langfuse comparison](https://langfuse.com/compare/arize-phoenix) (a competitor's page)
- Local check: 83 session transcripts directly under the home project and 351 MB under `~/.claude/projects`. 10 GB RAM was available at the time of checking, with no large job evident from that snapshot alone.

### Inferences
- Rough Langfuse sizing: six services, even at conservative figures, would likely take several GB, competing with Ollama and night jobs. My estimate; I did not run it.
- For one user, start with what exists: transcripts plus the `claude_code.*` metrics if a question needs them. Use Phoenix only as a process started for a debugging session. A permanent backend would need a named role, and "looking at traces" is not yet a recurring need here.
- `claude_code.cost.usage` will show API-equivalent estimates on a subscription, so treat it as a relative usage signal, not spending. Tokens are the cleaner number for tracking the session cap.
- Turning on raw bodies or tool content writes prompts and tool output to disk. Owner rules forbid secrets in notes, and these logs could capture them, so keep them outside the vault.

### Gaps
- OTel GenAI semantic convention stability: the [OpenTelemetry page](https://opentelemetry.io/docs/specs/semconv/gen-ai/) now only says they moved to a separate repository. I did not confirm current status or which conventions Claude Code follows.
- The portion of the Claude Code page I read does not say whether telemetry behaves differently on Max subscriptions. I read 100,000 of about 172,000 characters.
- No official RAM spec for Langfuse or Phoenix, and no independent side-by-side on low-memory hardware.
- Single-binary viewers (otel-tui, otel-desktop-viewer) returned no results, so they are unverified.
- Codex CLI telemetry was not researched.

## Model routing, cascades, structured outputs, speculative decoding and quantization on 10 GB VRAM: measured gains?

### Takeaway
Gate on something that can see the answer, especially executed tests. Learned or prompt-based routers have weak independent benchmark support, and speculative decoding is not worth a new service on current models here. I found no usable quantization evidence for this hardware.

### Cited Findings
Routing and cascades:
- Measurements on 404 task-model cells: executed tests correlated 0.85 with correctness; requiring 3 samples to agree correlated 0.78 to 0.98 at about 3% of one top-model call; a same-tier LLM judge correlated negatively; 2 samples gave 0.00 because a split has no majority — [Rung review, Stanford-hosted blog](https://web.stanford.edu/~shuhuiq/blog/review-routing-cascades.html) (one author reporting on their own system)
- Same source: prompt-based routing never beat a predict-nothing policy across 6,891 task-configuration cells, and the ladder beat every single model in 37 of 39 matched-spend comparisons on HumanEval+ (164 tasks) — [Rung review](https://web.stanford.edu/~shuhuiq/blog/review-routing-cascades.html)
- Secondary figures reported there: Model Cascading for Code, gated by self-generated tests, 26% average cost cut and up to 70%; EcoAssistant, gated by code execution, 10 points more success than GPT-4 at under half its cost; LLMRouterBench (400,000+ instances, 33 models) found recent methods and OpenRouter do not beat the best single model; RouterArena ranked Not Diamond 12th; CodeJudgeBench found LLM judges significantly random — [Rung review](https://web.stanford.edu/~shuhuiq/blog/review-routing-cascades.html) (I did not read these papers directly)
- Conflict: across five benchmarks and eight models, a lightweight pre-generation router beat the best threshold cascade on four of five datasets, full chains did worse than pairs, and tuned subsequences added little on held-out data. The authors point to the cost of running the cheap model first — [Is Escalation Worth It?, ICML 2026](https://icml.cc/virtual/2026/75267)
- Cascades with quality estimation retained 97 to 99% of the strongest model's accuracy while lowering time per output token — [Cluster, Route, Escalate](https://arxiv.org/abs/2606.27457) (search summary; dollar cost not confirmed)
- SWE-Router reads a weak model's first turns: AUC 0.780 on SWE-bench Verified, 15.3 points over prompt-only — [Rung review](https://web.stanford.edu/~shuhuiq/blog/review-routing-cascades.html)

Structured outputs:
- Ollama takes a JSON Schema in `format`, and `format: "json"` alone does not enforce structure. Docs advise temperature 0, including the schema in the prompt, and validating with Pydantic or Zod — [Ollama docs](https://docs.ollama.com/capabilities/structured-outputs)
- Constraints can trade correctness for validity: BAML's receipt benchmark reports 91.37% with constrained decoding against 93.63% with free-form parsing — [article summarizing BAML](https://tianpan.co/blog/2026-04-16-grammar-constrained-generation-output-reliability); [BAML post](https://boundaryml.com/blog/structured-outputs-create-false-confidence) (BAML sells a parsing product; model and test set not described in the summary, and the example used OpenAI Structured Outputs, not local grammar)
- Reported compile times: Outlines seconds per schema, XGrammar 0.12 to 0.30 s, Guidance under 60 ms; the common "5 to 15% overhead" figure is called outdated. Figures not tied to a specific test. Same article suggests a free-form scratchpad, then constrained final output — [Tian Pan](https://tianpan.co/blog/2026-04-16-grammar-constrained-generation-output-reliability)

Speculative decoding:
- Consumer GPU tests on llama.cpp: RTX 5060 Ti CUDA, 7B target 0.27x (slower) and 14B target 1.40x overall (code 1.57x, chat 0.92x); GTX 1080 Ti 7B 1.16x on math; CPU 3B 1.72x. Output is unchanged, and n-gram modes need no draft model — [InventiveHQ](https://inventivehq.com/blog/llama-cpp-speculative-decoding-consumer-gpu) (single blog, Windows, no RTX 3080)
- DraftBench: slow 72B Q8_0 target (about 6 tok/s) gained about 80%, faster 72B Q4_K_M (about 9.5 tok/s) about 12% — [DraftBench](https://github.com/alexziskind1/draftbench)
- Draft latency matters more than draft quality — [Decoding Speculative Decoding](https://arxiv.org/pdf/2402.01528)
- Ollama's native support is claimed only by a secondary post (MTP-based, v0.32.6) — [tech-insider tutorial](https://tech-insider.org/speculative-decoding-setup-2026/) (unverified). Local check: Ollama here is 0.40.10.

### Inferences
- The conflict above likely comes down to the gate. The ICML result studies deferral on model confidence; Rung and Model Cascading for Code gate on tests or sample agreement. So I would not build a confidence threshold cascade. That reconciliation is my reading, not tested by either source.
- Fit: local runs are free in money but not in time, which weakens the ICML objection (cheap-model cost) when the night GPU is idle. It still applies when local output delays a queue.
- Practical rule: three-sample agreement for classification and extraction, executed tests for code, escalation to Claude only on disagreement or failure, and a per-night escalation budget. Do not use a local LLM as the judge of another local LLM. That matters here because local judge habits would be the cheap default. Sampling three times triples local time.
- Apply the schema to the final step only, then validate values (ranges, cross-field rules). A schema-valid wrong answer otherwise passes silently.
- Do not add llama-server for speculation: it would be a second inference owner beside Ollama. The 7B regression shows that a fast small model can get slower. An n-gram test could be tried inside a one-off experiment, for code-heavy work only.
- Quantization: keep treating model-plus-context fit as the constraint. Here `gemma4:12b` tags are 8.0 GB and `qwen3:30b-a3b` is 18 GB (local check), so the larger one cannot fit fully in VRAM.

### Gaps
- No Q4 versus Q5 versus Q8 quality comparison found for Qwen or Gemma on 10 GB. Best source would be evolve-lab's own tasks. finetune-lab's Q8_0 work is the only local data point I noticed, and I did not read its results.
- No measurement of grammar constraints combined with speculative decoding.
- No Ollama-specific structured-output benchmark. Ollama's docs do not say what its enforcement mechanism is, or what happens if a response does not match.
- Whether Ollama 0.40.10 exposes speculative decoding: unconfirmed. Check its release notes or test it.

## Unattended coding agent safeguards and evaluation: sandboxes, mutation testing, spec-driven and test-first, trace-to-eval, deterministic gates: evidence?

### Takeaway
Passing tests is a weak acceptance signal, which is the strongest reason to add mutation checks and fresh review. The evidence shows the problem better than it shows the fix. Sandboxes cost real success and tokens, and blocked agents tend to burn time, so timeouts and stop rules belong with them.

### Cited Findings
Why tests alone are not enough:
- METR: 296 AI PRs (five models, newest Claude Sonnet 4.5) reviewed by 4 maintainers across scikit-learn, Sphinx and pytest. Grader pass rate was about 24.2 points above maintainer merges after baseline adjustment (SE 2.7), 34.9 points unadjusted. Golden patches merged about 68% of the time. Authors say this is not a fundamental capability limit, since models get one attempt, and reviewers lacked CI — [METR](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)
- 36% of coding-agent commits add mocks to tests versus 26% for non-agents, and 23% touch test files versus 13% — [Hora, MSR 2026](https://arxiv.org/pdf/2602.00409)
- 20,574 sessions across 1,639 repos: 90.50% of misalignment episodes cost effort and trust rather than irreversible damage, and 91.49% of visible resolutions needed explicit user correction. Rates are declining, but constraint violations and inaccurate self-reporting are a growing share — [Tang et al.](https://arxiv.org/abs/2605.29442)
- Of 8,106 agent fix PRs, 65.0% were merged and 26.1% closed unmerged — [arXiv 2602.00164](https://arxiv.org/html/2602.00164) (search summary)

Mutation testing:
- Meta's ACH combines LLMs and mutation testing to generate regression tests in its CI workflow — [Meta, arXiv 2501.12862](https://alphaxiv.org/abs/2501.12862)
- Mutation score directly measures whether tests separate correct code from subtle bugs, unlike coverage. On HumanEval+ the top 25% of generated tests gave over 85% of total mutation score — [MIST-RL](https://arxiv.org/html/2603.01409v1) (preprint, pilot, not agent workflows)
- Adversarial setup with a test agent and a mutant agent — [AdverTest](https://arxiv.org/html/2602.08146v2) (preprint)
- Mutation analysis is useful "only when scoped correctly" — [University of Twente thesis](https://essay.utwente.nl/fileshare/file/111098/Final%20Project%20Everard%20de%20Vree.pdf)
- LLM mutants showed lower compilability and more useless mutations than rule-based ones, though they imitated real bugs better — [literature summary](https://themoonlight.io/review/an-exploratory-study-on-using-large-language-models-for-mutation-testing) (secondary)

Sandboxes and permissions:
- 12 agents on Terminal-Bench 2.1 under nested policies: under the strictest, success fell by up to 18.3 points and cost rose by up to 167.3%. Blocked agents tend to run until timeout or produce wrong answers instead of stopping early. Boundary-Bench was released as a plugin — [Permission Denied](https://arxiv.org/abs/2608.02670)
- Claude Code's sandbox has auto-allow and regular permission modes, and needs bubblewrap and socat on Linux — [Claude Code sandboxing docs](https://code.claude.com/docs/en/sandboxing?via=sale) (search summary)
- CVE-2026-25725 is described as a CVSS 10.0 escape in the bubblewrap sandbox of Claude Code, tied to a missing `settings.json`, fixed in 2.1.2 — [stack.watch](https://stack.watch/vuln/CVE-2026-25725) (database summary)
- Auto mode is classifier-based. Willison questions relying on it against prompt injection and reports it blocked a cleanup command in his runs — [Simon Willison](https://feeds.simonwillison.net/tags/claude-code/)
- Codex on Linux runs Bubblewrap, with Landlock as a legacy fallback; SKILL.md appears in 9 of 11 systems and MCP in 8 of 11 — [Harness Engineering](https://arxiv.org/pdf/2609.00006); partly contradicted by [a practitioner blog](https://codex.danielvaughan.com/2026/07/08/balkanised-execution-security-coding-agents-codex-cli-sandbox-approval-toctou-gaps/) describing Bubblewrap plus Landlock

Spec-driven and test-first:
- 21 interviews plus 470,795 public spec files: specs are used selectively, mainly for new features; practitioners report more reliable agents along with higher planning and review costs; implementation detail may help agents but makes specs decay — [Spec-Driven Development as Prescribed and as Practiced](https://arxiv.org/abs/2608.25202)

### Inferences
- Promote `mutation_report` in stages: report only, then advisory on Paperclip, then a blocking gate if false alarms stay low. Scope it to changed lines with a time limit. `mutmut` is not installed (local check), so tool choice would go through `tool-gatekeeper`.
- Rule-based mutants fit better than LLM mutants here, since they cost no quota and compile more often.
- Add a cheap mock check to gates, flagging diffs that only add mocks to make tests pass, given the 36% versus 26% result. This is plausible but has no direct evidence.
- METR's result means gates should include what maintainers look for: repo conventions and whether the fix addresses the issue. That supports the existing `reviewer` fan-out, though its accuracy was not measured here.
- Night workers should also compare self-reports to artifacts (did tests really run, does the branch exist), since inaccurate self-reporting is a growing failure share. A deterministic check handles this at near zero cost.
- For sandboxing, add a hard session timeout and treat a repeated permission denial as a stop-and-report event in the morning queue. Expect some night tasks to fail more often, and measure this by trialing one task class first. Keep Claude Code updated given the CVE.
- Note that passwordless sudo is on by owner choice. A sandbox is the layer that limits an unattended worker's reach to it, but this is a fit point for the owner to weigh, not a suggestion to change that setting.
- Spec-first fits new features through `griller` and `slicer`. It does not justify a spec framework tool or specs for small fixes. A spec's tests only show that software matches the spec.

### Gaps
- No study found measuring mutation gates inside Claude Code or Codex workflows with agent-level outcomes.
- No controlled comparison of test-first versus test-after coding agents found. Consort ([arXiv 2609.09671](https://arxiv.org/pdf/2609.09671)) appeared but is a framework introduction that I did not read.
- No direct evidence for trace-to-eval pipelines improving outcomes. Using sessions where the owner pushed back as eval seeds is my extrapolation from Tang et al., and it should use evolve-lab holdouts.
- No primary postmortem of an unattended-agent incident retrieved. The Replit case was searched but returned nothing usable.
- METR's newest model is Sonnet 4.5, so the gap for current models is unknown.

## Local-business website lead pipeline: lead verification, entity resolution, visual QA, and cold outreach within CAN-SPAM

### Takeaway
Use cheap deterministic candidates and LLMs only for ambiguous pairs. Run axe and Lighthouse on every demo, with vision as an extra check for what they cannot judge. CAN-SPAM's rules are clear and cover B2B; reply-rate data is vendor-sourced and only directional.

### Cited Findings
Entity resolution and verification:
- Cheap retrieval first, then an LLM judging only returned candidates, because LLM-only matching is costly in time and money — [Elastic](https://www.elastic.co/search-labs/blog/elasticsearch-entity-resolution-llm-semantic-search) (vendor)
- BOOSTER sends a limited set of matching questions to LLMs because pair counts can reach n-squared — [BOOSTER](https://research.polyu.edu.hk/en/publications/booster-leveraging-large-language-models-for-enhancing-entity-res/)
- LLM entity resolution is described as promising for individuals or small companies without extensive training — [arXiv 2401.03426](https://arxiv.org/html/2401.03426v1)
- LLMs reliably replicated expert decisions compared with rule-based matching, in a sanctions-list domain — [arXiv 2603.11051](https://arxiv.org/pdf/2603.11051) (search summary, different domain)
- Business matching works best with name plus website — [Explorium docs](https://developers.explorium.ai/v2/businesses/match_businesses.md) (vendor)
- Splink runs unlabeled with a match threshold; oversized clusters signal unrelated records chained together — [Kestra blueprint](https://kestra.io/blueprints/splink-entity-resolution-golden-records)
- Local fact: 34 of 64 "no website" leads had a site, the first verifier missed chains and over-matched generic names, and few leads have phones — Now in the vault.

Visual QA and accessibility:
- Deque reports automated tests found 57.38% of issues by volume, and argues the common 20 to 30% counts success criteria instead — [Deque](https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues) (vendor, 2021); practitioner sources say 30 to 40% — [feedbagel](https://feedbagel.com/post/playwright-accessibility-testing-what-axe-and-lighthouse-miss)
- Lighthouse runs on axe-core rules, so the two overlap — [webability](https://www.webability.io/blog/automated-accessibility-scanners) (vendor)
- A W4A '25 study is reported to find the best of GPT-4o, Gemini and Llama 3 detected just 38% of what a scanner found, on mobile apps — [8th Light](https://8thlight.com/insights/llms-proving-impossible-automate-away-human-experience) (secondary, different platform)
- Conflict: one snippet reports GPT-4o with tailored prompts finding 88% of induced violations against 24% for Lighthouse (Hinderks et al. 2025, cited by van de Hoef et al.). I could not open the source to confirm it (see Gaps).

Outreach:
- CAN-SPAM has no B2B exception. It bans deceptive headers and subject lines, and requires ad disclosure, a valid postal address (including a registered PO box or private mailbox) and a working opt-out. Opt-outs must work for at least 30 days and be honored within 10 business days. Penalties reach $53,088 per email. Promoter and sender can both be liable — [FTC guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)
- Reply rates: 3.43% average, top 10% at 10.7%+ — [Instantly](https://instantly.ai/blog/ai-sales-agent-benchmarks-2026-the-complete-performance-report/) (vendor); 2.1% median, down from 4.7% in 2022 — [Visionary Marketing](https://visionary-marketing.co.uk/blog/b2b-cold-email-statistics-2026); 1.4% — [Boomerang](https://www.getboomerang.ai/glossaries/cold-email-reply-rate-benchmarks-2026) (vendor, unclear method)
- 142% reply lift from personalized first lines — [Visionary Marketing](https://visionary-marketing.co.uk/blog/b2b-cold-email-statistics-2026); under-50-recipient campaigns averaged 5.8% versus 2.1% at 500+ — [Woodpecker citing Belkins](https://woodpecker.co/blog/cold-email-statistics/) (vendor)
- 3% can be excellent in enterprise SaaS but mediocre for local services — [Mailshake](https://mailshake.com/blog/cold-email-benchmarks-2026/) (vendor, no local data shown)

### Inferences
- For DUS-52 a scale of dozens of leads does not need Splink. Normalize name, phone, domain and address; keep a chain list; require two independent matching fields for generic names; and send only ambiguous pairs to an LLM with a schema. Label the current leads as a small regression test. Precision matters more than recall here, because pitching a business that has a site wastes a send and damages credibility.
- Visual QA order: Lighthouse/axe, broken links and form checks at mobile and desktop widths, then a vision review of screenshots for layout and looks. Findings by a vision model should be advisory. Do not run Lighthouse via a daemon; `npx` is available (local check).
- Do not market demos as "accessible" based on automated passes, given how much tools miss.
- Outreach: treat CAN-SPAM's elements as a deterministic lint on each draft (postal address present, opt-out present, subject matches body, ad disclosure). The owner approves and sends through Paperclip. Small batches suit 6 to 30 leads anyway, and a real demo link or real site fact is the natural personalization.
- With so few leads, a benchmark reply rate cannot be judged: at 30 sends and 3%, expect about one reply. Owner decisions should rest on booked conversations rather than reply percentages.

### Gaps
- No benchmark for Google Places matching, per-pair LLM cost or Splink with an LLM on lead data.
- Could not open the [University of Maribor proceedings](https://press.um.si/index.php/ump/en/catalog/view/1128/1757/6429) (redirect error), so 88% versus 24% remains unconfirmed and I could not determine that this is its source.
- No independent cold-email data for local service businesses, and no controlled study of AI personalization. All lift figures are observational and vendor-adjacent.
- Not researched: state laws (DMV-area) beyond federal CAN-SPAM, phone outreach rules (TCPA), deliverability setup, and Google Places terms for storing data. Have these checked before sending; these notes are not legal advice.
- No evidence on LLM vision versus deterministic checks for desktop or mobile web layout defects specifically.

## New tools from 2026 worth a look; flag hype

### Takeaway
Few new tools earn a place; the useful 2026 items are features of tools already installed plus a benchmark plugin. The clearest hype is in commercial routers, vendor AI-sales figures and any claim that a sandbox or classifier makes unattended agents safe.

### Cited Findings
Worth a look:
- Claude Code traces (beta) and `OTEL_LOG_RAW_API_BODIES=file:<dir>` — [Claude Code docs](https://code.claude.com/docs/en/monitoring-usage)
- Claude Code sandbox — [docs](https://code.claude.com/docs/en/sandboxing?via=sale)
- Boundary-Bench, only if testing night-worker policies — [Permission Denied](https://arxiv.org/abs/2608.02670)
- SWE-Router's idea of judging from a weak model's early turns, as a research idea for tasks without tests. It needs a trained 7B head — [Rung review](https://web.stanford.edu/~shuhuiq/blog/review-routing-cascades.html)

Hype or caution:
- Commercial and learned routers: independent benchmarks do not show them beating the best single model — [Rung review](https://web.stanford.edu/~shuhuiq/blog/review-routing-cascades.html)
- Datacenter speculative decoding claims such as 15x do not carry to consumer GPUs, where gains run tens of percent to about 2x — [InventiveHQ](https://inventivehq.com/blog/llama-cpp-speculative-decoding-consumer-gpu)
- Sandbox marketing: a Medium headline style of "makes YOLO mode look amateurish" oversells it, as a CVSS 10.0 escape was reported — [Medium](https://medium.com/@joe.njenga/how-to-use-new-claude-code-sandbox-to-autonomously-code-without-security-disasters-c6efc5e8e652); [stack.watch](https://stack.watch/vuln/CVE-2026-25725)
- Cold-email "AI agent" stats come from sellers of those tools — [Instantly](https://instantly.ai/blog/ai-sales-agent-benchmarks-2026-the-complete-performance-report/)
- Observability comparison pages are written by interested parties — [FutureAGI](https://futureagi.com/blog/arize-phoenix-vs-langfuse-2026/); [Langfuse](https://langfuse.com/compare/arize-phoenix)

### Inferences
- Under the one-owner rule, each worth-a-look item is a setting or one-off experiment, so none creates a new role. Any install should still pass `tool-gatekeeper`.
- LLM-judge products deserve the same skepticism as routers, given the judge correlation results.

### Gaps
- My search for trending 2026 tools found no independent roundup, so this list is not exhaustive and new tools may have been missed.
- The Grok Build harness result (a 34.6-point drop) comes from a [blog summary](https://codex.danielvaughan.com/2026/08/07/permission-denied-policy-graded-coding-agents-hardened-environments-codex-cli-enterprise-sandbox-profiles/) I did not verify in the paper, so I do not rely on it.
