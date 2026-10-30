import sys; sys.stdout.reconfigure(encoding="utf-8")
import csv, sys
rows = {}
for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig')):
    rows[r['id']] = r
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r: print(i, 'MISSING'); continue
    print(f"{i} [{r['year']}, {r['speaker']}]: {r['quote_verbatim']}\n")
