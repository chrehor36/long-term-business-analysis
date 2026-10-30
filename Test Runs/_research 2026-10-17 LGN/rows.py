import csv, sys
rows = {}
for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8")):
    rows[r.get("﻿id") or r.get("id")] = r
out = sys.stdout.buffer
for i in sys.argv[1:]:
    r = rows.get(i)
    out.write(("===== %s %s\n" % (i, "MISSING" if r is None else r["year"])).encode("utf-8"))
    if r:
        out.write((r["quote_verbatim"] + "\n").encode("utf-8"))
