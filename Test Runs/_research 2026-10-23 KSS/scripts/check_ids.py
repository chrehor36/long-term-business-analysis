# Check: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment just before an id is in that row.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open(sys.argv[2], encoding="utf-8"))}
norm = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0
eids = re.findall(r"\[E\d-\d+\]", run)
if eids: print("E-ids found:", eids); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
# fragments: a "..." quote followed (within 60 chars, no other id or quote) by **[ID]**
for m in re.finditer(r'"([^"]{6,600}?)"([^"\[]{0,60}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, gap, i = m.group(1), m.group(2), m.group(3)
    if "**[" in gap: continue
    row = norm(rows.get(i, ""))
    parts = [norm(x) for x in frag.split("[...]") if norm(x)]
    miss = [x for x in parts if x not in row]
    if miss: print("NOT IN ROW", i, "|", miss); bad += 1
print("ids:", len(set(ids)), "checked fragments OK" if not bad else f"PROBLEMS: {bad}")
