import csv, sys
import sys; sys.stdout.reconfigure(encoding="utf-8")
rows = {r["\ufeffid"] if "\ufeffid" in r else r["id"]: r for r in csv.DictReader(open(r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv", encoding="utf-8"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print("==", i, "MISSING" if r is None else "")
    if r: print(r["quote_verbatim"])
