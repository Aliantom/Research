"""Compare retrieval variants on the same 20 questions (experiment only; no repo changes)."""
import re, sys, importlib.util
sys.path.insert(0, "/home/sol-badguy/code/evolve-lab/src")
import evolve.semantic_retrieval as sr
from evolve.retrieval import corpus, rank_corpus
spec = importlib.util.spec_from_file_location("ev", sys.argv[1].rsplit("/",1)[0] + "/retrieval_eval_qs.py")
ev = importlib.util.module_from_spec(spec); spec.loader.exec_module(ev)
QS, hit = ev.QS, ev.hit
sr.MAX_CHUNKS = 10**6; sr.MAX_TEXT = 10**9
orig_chunks = sr._chunks
def headed_chunks(docs):
    chunks, reasons = orig_chunks(docs)
    text = {d["source"]: d["text"].splitlines() for d in docs}
    for c in chunks:
        lines = text[c["source"]][:c["start_line"]]
        head = next((l.lstrip("# ").strip() for l in reversed(lines) if l.startswith("#")), "")
        title = c["source"].rsplit("/", 1)[-1][:-3]
        c["content"] = f"Note: {title}\nSection: {head}\n\n" + c["content"]
    return chunks, reasons
def run(name, docs, stats, headed, fuse, cache):
    sr._chunks = headed_chunks if headed else orig_chunks
    n = 0; misses = []
    for q, wants in QS:
        s = [m["source"] for m in sr.semantic_rank(q, docs, stats, limit=5, cache_path=cache)["matches"]]
        if fuse:
            l = [m["source"] for m in rank_corpus(q, docs, stats, limit=5)["matches"]]
            score = {}
            for lst in (s, l):
                for r, src in enumerate(lst): score[src] = score.get(src, 0) + 1 / (60 + r)
            s = sorted(score, key=score.get, reverse=True)[:5]
        ok = hit(s, wants); n += ok
        if not ok: misses.append(q)
    print(f"{name:42} recall@5 {n}/{len(QS)}  misses: {misses}")
docs, stats = corpus()
noindex = [d for d in docs if not d["source"].endswith("Context/Index.md")]
run("semantic, uncapped", docs, stats, False, False, sr.FIXED)
run("semantic + note/heading prefix", docs, stats, True, False, sys.argv[1])
run("hybrid RRF (semantic+BM25)", docs, stats, False, True, sr.FIXED)
run("hybrid RRF + prefix", docs, stats, True, True, sys.argv[1])
run("hybrid RRF + prefix, Index.md excluded", noindex, stats, True, True, sys.argv[1])
