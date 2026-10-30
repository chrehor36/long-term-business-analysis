import csv, sys
rows = {r["\ufeffid"]: r["quote_verbatim"] for r in csv.DictReader(open(r"C:\Projects\BRK\principle_ledger_v5.csv", encoding="utf-8"))}
for i in sys.argv[1:]:
    print(i, "::", rows.get(i, "MISSING")[:700]); print()
