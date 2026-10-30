# Check: no E-ids; every M/L/R id in the run file exists in principle_ledger_v5.csv; every quoted fragment sitting
# beside an id (in the same bullet/sentence, before the id) is found in that row (whitespace and quote styles normalized).
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run = open(sys.argv[1], encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open(sys.argv[2], encoding="utf-8-sig"))}
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip().lower()
eids = re.findall(r"\[E\d-\d+\]", run)
print("E-ids:", eids or "none")
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", run)
missing = sorted(set(i for i in ids if i not in rows))
print("ids cited:", len(set(ids)), "missing:", missing or "none")
# quoted fragments immediately followed (within 12 chars) by a bold id
bad = 0; checked = 0
for m in re.finditer(r'"([^"\n]{6,}(?:\n[^"\n]*)*?)"[^"\n]{0,14}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    checked += 1
    parts = [p for p in re.split(r"\[\.\.\.\]", frag)]
    ok = all(norm(p).strip(" .,;:") in norm(rows[i]) for p in parts if norm(p).strip(" .,;:"))
    if not ok:
        bad += 1; print("NOT IN ROW", i, "|", frag[:160].replace("\n", " "))
print("quoted fragments checked:", checked, "failing:", bad)
