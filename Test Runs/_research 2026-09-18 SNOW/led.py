import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r["id"]: r for r in csv.DictReader(open("principle_ledger.csv", encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, "MISSING" if not r else (r["year"] + " | " + r["concept"] + " | " + r["quote_verbatim"][:260]))
