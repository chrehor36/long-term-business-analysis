import csv, sys, re
ledger = sys.argv[1]
ids = sys.argv[2:]
if len(ids) == 1 and ids[0].endswith(".md"):
    ids = sorted(set(re.findall(r"\[([MLR]\d{4}-\d{3})\]", open(ids[0], encoding="utf-8").read())))
rows = {}
with open(ledger, encoding="utf-8") as f:
    rd = csv.reader(f)
    hdr = next(rd)
    for r in rd:
        rows[r[0]] = r
print(hdr)
for i in ids:
    r = rows.get(i)
    if not r:
        print(i, "MISSING")
    else:
        print(i, "|", " || ".join(x[:300] for x in r[1:4]))
