import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["﻿id"]: r["quote_verbatim"] for r in csv.DictReader(open(sys.argv[2], encoding="utf-8"))}
bad = 0
if re.search(r"\bE\d-\d+\b", run): print("E-id found"); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
# quoted fragment immediately before an id: "..." **[ID]** or "..." [ID] (allow comma/space)
norm = lambda t: re.sub(r"\s+", " ", t.replace("[...]", "\x00"))
for m in re.finditer(r'"([^"]{3,400})"\s*(?:\*\*)?\[([MLR]\d{4}-\d{3})\]', run):
    frag, i = m.group(1), m.group(2)
    q = norm(rows.get(i, ""))
    parts = [p.strip() for p in norm(frag).split("\x00") if p.strip()]
    for p in parts:
        if p not in q:
            print("NOT IN ROW", i, "::", p[:120]); bad += 1
print("ids:", len(set(ids)), "problems:", bad)
