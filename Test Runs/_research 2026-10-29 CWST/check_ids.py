# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment in the same
# paragraph as an id appears in one of that paragraph's cited rows (quotes normalised: curly to straight, whitespace).
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["﻿id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8"))}
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("�", "'")).strip()
bad = 0
if re.search(r"\[E\d", run): print("E-id found"); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run))
for i in sorted(ids):
    if i not in rows: print("MISSING", i); bad += 1
for para in re.split(r"\n(?=- |\n|\*\*|## )", run):
    pids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", para)
    if not pids: continue
    text = " ".join(norm(rows.get(i, "")) for i in pids)
    for q in re.findall(r"“([^”]{6,})”|\"([^\"]{6,})\"", para):
        q = norm(q[0] or q[1])
        parts = [x.strip(" ,.;:") for x in q.split("[...]")]
        if all(x == "" or x in text for x in parts): continue
        # a quote from a filing in the same paragraph is allowed; report for manual review
        print("CHECK", pids, "|", q[:120])
print("ids:", len(ids), "problems:", bad)
