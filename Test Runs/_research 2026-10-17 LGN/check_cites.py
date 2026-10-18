# Citation check for the LGN run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that sits immediately before a bold id (the quote, then the id) is in that row.
import csv, re, sys
RUN = "Test Runs/2026-10-17 Run - LGN Legence.md"
rows = {}
for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8")):
    rows[r.get("﻿id") or r.get("id")] = r["quote_verbatim"]
text = open(RUN, encoding="utf-8").read()
bad = 0
e_ids = re.findall(r"\[E\d+-\d+\]", text)
if e_ids:
    print("E-ids found:", e_ids); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", text))
for i in sorted(ids):
    if i not in rows:
        print("MISSING id", i); bad += 1
def norm(s):
    return (s.replace("’", "'").replace("‘", "'").replace("�", "'")
             .replace("“", '"').replace("”", '"'))
flat = re.sub(r"\n\s*", " ", text)
pat = re.compile(r'"([^"]{4,600})"[\s,.;:)]{0,6}\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for m in pat.finditer(flat):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    parts = [p.strip() for p in frag.split("[...]") if p.strip()]
    for p in parts:
        checked += 1
        if p not in rows[i]:
            if norm(p) in norm(rows[i]):
                print("QUOTE-MARK ONLY mismatch (fix to the row's own character)", i, "::", p[:80]); bad += 1
            else:
                print("NOT IN ROW", i, "::", p[:120]); bad += 1
print("ids:", len(ids), "fragments checked:", checked, "failures:", bad)
sys.exit(1 if bad else 0)
