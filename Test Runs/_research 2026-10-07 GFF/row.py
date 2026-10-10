"""Print ledger rows by id: python row.py M1995-051 L2007-004 ..."""
import csv, sys
rows = {r[0]: r for r in csv.reader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8"))}
hdr = rows.get("id")
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r: print(i, "MISSING"); continue
    print("==", i, "|", " | ".join(r[1:4]))
    print([c for c in r if len(c) > 80][0][:1500] if any(len(c) > 80 for c in r) else r)
