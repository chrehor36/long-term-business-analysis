import csv, re, sys
p = "Test Runs/2026-10-06 Run - NX Quanex Building Products.md"
s = open(p, encoding="utf-8").read()
rows = {r["id"]: r["quote_verbatim"] for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
ok = True
eids = re.findall(r"\[E\d+-\d+\]", s)
if eids: print("E-ids found:", eids); ok = False
ids = re.findall(r"\*\*\[([MLR]\d{4}-\d{3})\]\*\*", s)
print("id citations:", len(ids), "distinct:", len(set(ids)))
for i in set(ids):
    if i not in rows: print("MISSING id", i); ok = False
# every id must be preceded by a quoted fragment in that row
flat = re.sub(r"\s*\n\s*", " ", s)
for m in re.finditer(r'"([^"]{3,400})"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    q = rows.get(i, "")
    norm = lambda t: re.sub(r"\s+", " ", t)
    parts = [x.strip() for x in frag.split("[...]") if x.strip()]
    if not all(norm(x) in norm(q) for x in parts):
        print("FRAGMENT NOT IN ROW", i, "::", frag); ok = False
# ids with no immediately preceding quote
for m in re.finditer(r'(.{0,3})\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    if not m.group(1).rstrip().endswith('"'):
        print("id without adjacent quote:", m.group(2), "::", flat[max(0,m.start()-80):m.start()+20])
print("PASS" if ok else "FAIL")
