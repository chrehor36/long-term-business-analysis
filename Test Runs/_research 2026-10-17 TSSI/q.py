import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
r = {x["\ufeffid"]: x for x in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8"))}
for i in sys.argv[1:]:
    x = r.get(i)
    print(i, "MISSING" if not x else x["quote_verbatim"]); print()
