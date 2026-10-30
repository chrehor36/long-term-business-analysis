import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = sys.argv[1]
run = open(sys.argv[2], encoding="utf-8").read()
rows = {}
with open(ROOT + "/principle_ledger_v5.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f): rows[r["id"]] = r["quote_verbatim"]
bad = 0
if re.search(r"\[E\d", run): print("E-id found"); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in set(ids):
    if i not in rows: print("MISSING", i); bad += 1
def norm(t): return re.sub(r"\s+", " ", t.replace("�","")).strip()
# a quoted fragment immediately before an id: "...." **[ID]**  (fragments may contain [...] elisions)
for m in re.finditer(r'"([^"]{6,600}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    row = norm(rows[i])
    parts = [norm(p) for p in frag.split("[...]") if norm(p)]
    for p in parts:
        if p not in row:
            print("NOT IN ROW", i, "::", p[:120]); bad += 1
print("ids cited:", len(set(ids)), "problems:", bad)
