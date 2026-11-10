import re, sys, collections, pathlib
root = pathlib.Path(sys.argv[1])
notes = [p for p in root.rglob("*.md") if ".git" not in p.parts and ".obsidian" not in p.parts]
names = collections.defaultdict(list)
for p in notes: names[p.stem].append(p)
by_folder = collections.Counter(); tok = collections.Counter()
no_fm = []; no_type = []; types = collections.Counter(); props = collections.Counter()
links_out = {}; inbound = collections.Counter(); dead = collections.Counter()
big = []
for p in notes:
    t = p.read_text(errors="replace"); rel = p.relative_to(root)
    top = "/".join(rel.parts[:2]) if len(rel.parts) > 2 else rel.parts[0]
    by_folder[top] += 1; tk = len(t) // 4; tok[top] += tk; big.append((tk, str(rel)))
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m: no_fm.append(str(rel))
    else:
        keys = re.findall(r"^([A-Za-z_][\w-]*):", m.group(1), re.M); props.update(keys)
        ty = re.search(r"^type:\s*(.+)$", m.group(1), re.M)
        if ty: types[ty.group(1).strip().strip('"')] += 1
        else: no_type.append(str(rel))
    ls = [l.split("|")[0].split("#")[0].strip() for l in re.findall(r"\[\[([^\]]+)\]\]", t)]
    links_out[str(rel)] = ls
    for l in ls:
        stem = pathlib.Path(l).stem if l else ""
        if stem in names: inbound[stem] += 1
        elif l: dead[l] += 1
arch = lambda s: s.startswith("Machine/Claude Archive")
orph = [str(p.relative_to(root)) for p in notes if inbound[p.stem] == 0 and not arch(str(p.relative_to(root)))]
print("notes", len(notes), "est tokens", sum(tok.values()))
for k, v in sorted(by_folder.items(), key=lambda x: -tok[x[0]]): print(f"  {k:45} {v:4} notes {tok[k]:8} tok")
print("no front matter:", len(no_fm), no_fm[:8]); print("front matter w/o type:", len(no_type), no_type[:5])
print("types:", dict(types)); print("top props:", props.most_common(25))
print("dead links:", len(dead), dead.most_common(10))
print("orphans (no inbound, excl archive):", len(orph)); [print("   ", o) for o in orph[:25]]
print("dup names:", {k: len(v) for k, v in names.items() if len(v) > 1})
print("largest:"); [print(f"   {a:7} {b}") for a, b in sorted(big, reverse=True)[:12]]
