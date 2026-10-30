# Checks: no E-ids; every M/L/R id in the run file exists in the v5 ledger; every quoted fragment beside an id is in that row.
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r[0]: r[2] for r in csv.reader(open(sys.argv[2], encoding="utf-8-sig")) if r and r[0] != "id"}
bad = 0
if re.search(r"\[E\d+-\d+\]", run): print("E-id found"); bad += 1
ids = set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", run))
for i in sorted(ids):
    if i not in rows: print("MISSING", i); bad += 1
norm = lambda s: re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()
# quoted fragment immediately followed (within the same sentence) by one or more ids
for m in re.finditer(r"\"([^\"]{12,}?)\"[^\"\n]{0,80}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)", run.replace("\n", " ")):
    frag = m.group(1); cited = re.findall(r"[MLR]\d{4}-\d{3}", m.group(2))
    parts = [p.strip(" .,;:") for p in re.split(r"\.\.\.|\[\.\.\.\]", frag) if len(p.strip(" .,;:")) > 5]
    ok = any(all(norm(p) in norm(rows.get(c, "")) for p in parts) for c in cited)
    if not ok:
        print("FRAGMENT NOT IN ROW", cited, "::", frag[:120]); bad += 1
print("ids checked:", len(ids), "problems:", bad)
