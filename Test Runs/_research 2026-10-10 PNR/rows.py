"""Print v5 ledger rows by id (quote column). Usage: python rows.py ID ..."""
import csv, sys
rows = {r[0]: r for r in csv.reader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, '|', r[2] if r else 'MISSING'); print()
