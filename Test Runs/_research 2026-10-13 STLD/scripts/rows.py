import csv, sys
sys_ = __import__("sys"); sys_.stdout.reconfigure(encoding="utf-8")
rows = {r["id"]: r for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, "MISSING" if r is None else r["quote_verbatim"])
    print()
