# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
# immediately before an id (within 40 characters) is found in that row (whitespace and quote marks normalized; [...] splits).
import csv, re, sys
run = open("Test Runs/2026-10-17 Run - CNIG Corning Natural Gas Holding.md", encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open("principle_ledger_v5.csv", encoding="utf-8"))}
def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip().lower()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id", i); bad += 1
flat = re.sub(r"\s+", " ", run)
n = 0
for m in re.finditer(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", flat):
    pre = flat[max(0, m.start() - 600):m.start()]
    q = re.search(r'"([^"]{3,})"([^"]{0,40})$', pre)
    if not q: continue
    frag = q.group(1); n += 1
    row = norm(rows.get(m.group(1), ""))
    for part in frag.split("[...]"):
        part = norm(part).strip(" .,;:")
        if part and part not in row:
            print(f"NOT IN ROW {m.group(1)}: {part[:120]}"); bad += 1
print(f"ids cited: {len(set(ids))} distinct, {len(ids)} total; quoted fragments checked: {n}; problems: {bad}")
sys.exit(1 if bad else 0)
