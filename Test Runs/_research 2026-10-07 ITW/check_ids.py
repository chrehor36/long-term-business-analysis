# Citation check for the ITW run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (within the same sentence) is in that row's quote, elisions as [...].
import csv, re, sys, os, unicodedata
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUN = os.path.join(ROOT, "Test Runs", "2026-10-07 Run - ITW Illinois Tool Works.md")
rows = {r["﻿id"] if "﻿id" in r else r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8"))}
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
txt = open(RUN, encoding="utf-8").read()
bad = 0
if re.search(r"\[E\d-\d+\]", txt): print("E-id found"); bad += 1
ids = re.findall(r"\[((?:M|L|R)\d{4}-\d{3})\]", txt)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
# quoted fragment followed by an id: "...." **[ID]** or "....", **[ID]** ; also chains "..." **[A]**, **[B]** check against first
for m in re.finditer(r'"([^"\n]{3,600})"[\s,.;:)]*(?:\*\*)?\[((?:M|L|R)\d{4}-\d{3})\]', txt):
    q, i = m.group(1), m.group(2)
    if i not in rows: continue
    src = norm(rows[i]["quote_verbatim"])
    for part in re.split(r"\[\.\.\.\]|\.\.\.", q):
        p = norm(part).strip(" .,;:")
        if len(p) < 3: continue
        if p not in src:
            print(f"NOT IN ROW {i}: {part[:120]!r}"); bad += 1
print(f"ids cited: {len(set(ids))}; problems: {bad}")
sys.exit(1 if bad else 0)
