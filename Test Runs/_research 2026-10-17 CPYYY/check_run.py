# Citation check for the CPYYY run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every double-quoted fragment that sits immediately before an id is found in that row (after light normalisation).
import csv, re, sys
RUN = "Test Runs/2026-10-17 Run - CPYYY Centrica.md"
rows = {}
for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8")):
    k = r.get("﻿id") or r.get("id")
    rows[k] = r["quote_verbatim"]
text = open(RUN, encoding="utf-8").read()
def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", t).strip().lower()
problems = 0
eids = re.findall(r"\[E\d+-\d+\]", text)
if eids:
    print("E-ids found:", sorted(set(eids))); problems += len(eids)
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("MISSING id", i); problems += 1
# quoted fragment directly followed (within 12 chars) by an id
for m in re.finditer(r"\"([^\"]{3,400})\"\s*(?:\*\*)?\s*\[([MLR]\d{4}-\d{3})\]", text):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    parts = [p.strip() for p in frag.split("[...]") if p.strip()]
    for p in parts:
        if norm(p) not in norm(rows[i]):
            print("FRAGMENT NOT IN ROW", i, "::", p[:120]); problems += 1
print("ids cited:", len(set(ids)), "| problems:", problems)
sys.exit(1 if problems else 0)
