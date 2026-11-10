"""Recall@5 of the vault's two retrievers on questions with a known answer note.
Run: evolve-lab/.venv/bin/python -I retrieval_eval.py [--uncapped]"""
import json, sys
sys.path.insert(0, "/home/sol-badguy/code/evolve-lab/src")
import evolve.semantic_retrieval as sr
from evolve.retrieval import corpus, rank_corpus

QS = [  # (question, any of these note-name substrings counts as a hit)
 ("Which local model should be the default worker and why?", ["Local model analysis", "Local model recommendations"]),
 ("What happens if the routing proxy goes down?", ["caveman proxy down"]),
 ("How do I reach the home PC from my work laptop?", ["Remote access from work"]),
 ("Why can't Kimi K3.1 run on this computer?", ["Kimi K3.1 Pro feasibility"]),
 ("Is the network exposed? Which ports are listening?", ["Security and network exposure audit"]),
 ("How was Paperclip installed and what are its gotchas?", ["Paperclip AI agent dashboard setup"]),
 ("What should we build first to make money with AI?", ["AI money strategy"]),
 ("Can I fine-tune a model on a 10GB card with LoRA?", ["03 Weight-based self-improvement", "VRAM headroom"]),
 ("What is the plan for self-improving agents built on evolve-lab?", ["00 Blueprint", "AI build-out plan"]),
 ("What does the night-shift workflow do each night?", ["night-shift/", "Morning report"]),
 ("How does the daily review workflow work?", ["daily-review/"]),
 ("Why did the keyboard keep repeating keys?", ["Keyboard runaway repeats"]),
 ("Which GNOME extension tiles windows?", ["Window layout picker"]),
 ("Why were the models moved to the NVMe drive?", ["NVMe model migration", "Independent local model and NVMe"]),
 ("What did the VRAM temperature tests at different power caps show?", ["GPU unlock validation queue"]),
 ("How do I run Claude Code against a local Ollama model?", ["Local models in Claude Code and Codex", "Local AI terminal handbook"]),
 ("What memory and reflection techniques could agents use?", ["04 Agent memory"]),
 ("What is the answer key spot-check for headline labels?", ["answer key spot-check"]),
 ("How do I set up n8n?", ["n8n setup"]),
 ("Which tools for evaluating agents and tracing were reviewed?", ["Observability and evaluation sources", "02_multiagent_eval"]),
]

def hit(sources, wants): return any(w in s for s in sources for w in wants)

def main():
    if "--uncapped" in sys.argv: sr.MAX_CHUNKS = 10**6; sr.MAX_TEXT = 10**9
    docs, stats = corpus()
    sem = lex = 0; rows = []
    for q, wants in QS:
        s = [m["source"] for m in sr.semantic_rank(q, docs, stats, limit=5)["matches"]]
        l = [m["source"] for m in rank_corpus(q, docs, stats, limit=5)["matches"]]
        a, b = hit(s, wants), hit(l, wants); sem += a; lex += b
        rows.append((a, b, q, len(set(s))))
    for a, b, q, u in rows: print(f"sem {'Y' if a else '-'}  bm25 {'Y' if b else '-'}  uniq-notes-in-top5={u}  {q}")
    print(f"recall@5  semantic {sem}/{len(QS)}  bm25 {lex}/{len(QS)}  either {sum(a or b for a,b,_,_ in rows)}/{len(QS)}")

main()
