# Citation check for the ENIC run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that stands in the same sentence as an id (before it) is found in that id's row.
import csv, re, sys, unicodedata

RUN = "Test Runs/2026-10-23 Run - ENIC Enel Chile.md"
LEDGER = "principle_ledger_v5.csv"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()

rows = {}
with open(LEDGER, encoding="utf-8") as f:
    for r in csv.reader(f):
        rows[r[0].lstrip("﻿")] = r[2]

text = open(RUN, encoding="utf-8").read()
problems = 0
for m in re.finditer(r"\[(E\d+-\d+)\]", text):
    print("E-id found:", m.group(1)); problems += 1

ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", text)
for i in sorted(set(ids)):
    if i not in rows:
        print("missing id:", i); problems += 1

# quotes before an id in the same paragraph line-joined text
flat = re.sub(r"\s*\n\s*", " ", text)
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", flat):
    i = m.group(1)
    prev = flat.rfind("]**", 0, m.start())
    start = max(flat.rfind(". ", 0, m.start()), flat.rfind("; ", 0, m.start()), prev + 3 if prev >= 0 else 0, 0)
    seg = flat[start:m.start()]
    # skip quotes that are themselves filing quotes cited with a filing reference inside the segment
    for q in re.findall(r'"([^"]{6,})"', seg):
        if i in rows and norm(q) not in norm(rows[i]):
            # allow the [...] elision: every piece must be in the row, in order
            parts = [p.strip() for p in q.split("[...]") if p.strip()]
            pos, ok = 0, True
            nr = norm(rows[i])
            for p in parts:
                k = nr.find(norm(p), pos)
                if k < 0: ok = False; break
                pos = k + len(norm(p))
            if not ok:
                print(f"fragment not in {i}: {q[:90]}"); problems += 1

print(f"ids cited: {len(set(ids))}; problems: {problems}")
sys.exit(1 if problems else 0)
