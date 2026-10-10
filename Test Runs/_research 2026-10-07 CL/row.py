# print v5 ledger rows by id (quote and source) for the CL run
import csv, sys
rows = {r["id"]: r for r in csv.DictReader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(f"== {i}: " + ("MISSING" if not r else f"{r['year']} {r['source_file']}\n{r['quote_verbatim']}\n"))
