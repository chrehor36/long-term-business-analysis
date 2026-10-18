"""Check the run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
immediately before an id (within the same sentence) is a substring of that row's quote."""
import csv, re, sys
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(sys.argv[2], encoding="utf-8-sig"))}
norm = lambda s: re.sub(r"\s+", " ", s.replace("�", "'").replace("’", "'").replace("‘", "'")
                        .replace("“", '"').replace("”", '"')).strip()
bad = 0
if re.search(r"\[E\d-\d+\]", run): print("E-id found"); bad += 1
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING", i); bad += 1
# quoted fragments followed by an id within 40 chars
for m in re.finditer(r'"([^"]{3,400})"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    if i in rows:
        parts = [p for p in re.split(r"\s*\[\.\.\.\]\s*", frag) if p]
        for p in parts:
            if norm(p) not in norm(rows[i]):
                print("NOT IN ROW", i, "::", p[:90]); bad += 1
print("ids:", len(set(ids)), "problems:", bad)
