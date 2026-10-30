# Check the run file: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment
# immediately before an id (within the same sentence span) appears in that row's quote.
import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-16 Run - GATX GATX Corporation.md"
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8-sig"))}
s = open(RUN, encoding="utf-8").read()
bad = 0
for m in re.finditer(r"\[(E\d+-\d+)\]", s):
    print("E-id found:", m.group(1)); bad += 1
ids = re.findall(r"\[([MLR]\d{4}-\d{3})\]", s)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id:", i); bad += 1
norm = lambda t: re.sub(r"\s+", " ", t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
# quoted fragment followed (within 6 chars) by **[ID]**
for m in re.finditer(r"\"([^\"]{4,}?)\"\s*\**\s*\[([MLR]\d{4}-\d{3})\]", s):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    parts = [p.strip() for p in frag.split("[...]") if p.strip()]
    q = norm(rows[i])
    for p in parts:
        if norm(p) not in q:
            print("FRAGMENT NOT IN ROW", i, ":", p[:120]); bad += 1
print("ids cited:", len(set(ids)), "| problems:", bad)
sys.exit(1 if bad else 0)
