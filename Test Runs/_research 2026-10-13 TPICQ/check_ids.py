# Check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# on the same line as (or the line before) an id is a substring of that id's row.
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
root = sys.argv[1]; run = sys.argv[2]
rows = {r["﻿id"]: r["quote_verbatim"] for r in csv.DictReader(open(root + "/principle_ledger_v5.csv", encoding="utf-8"))}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()
txt = open(run, encoding="utf-8").read()
bad = 0
for m in re.finditer(r"\[(E\d-\d+)\]", txt):
    print("E-ID FOUND", m.group(1)); bad += 1
paras = re.split(r"\n(?=- |\n|\|)", txt)
for p in paras:
    ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", p)
    for i in ids:
        if i not in rows: print("MISSING ID", i); bad += 1
    if not ids: continue
    # quotes immediately followed (within 12 chars) by an id
    for m in re.finditer(r"\"([^\"]{4,}?)\"\s*(?:\*\*\[([MLR]\d{4}-\d{3})\]\*\*)?", p):
        q, i = m.group(1), m.group(2)
        if not i: continue
        parts = [x.strip() for x in q.split("[...]") if x.strip()]
        for part in parts:
            if norm(part.rstrip(".,;:")) not in norm(rows.get(i, "")):
                print("NOT IN ROW", i, "|", part[:90]); bad += 1
print("ids used:", len(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", txt))), "problems:", bad)
