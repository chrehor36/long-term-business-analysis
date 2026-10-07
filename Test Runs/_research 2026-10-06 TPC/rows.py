"""Print the verbatim ledger row for each id given (transcription from principle_ledger_v5.csv)."""
import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r["id"]: r for r in csv.DictReader(open("../../principle_ledger_v5.csv", encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print("=== ", i, "MISSING" if not r else f'{r["year"]} {r["source_file"]}')
    if r: print(r["quote_verbatim"])
