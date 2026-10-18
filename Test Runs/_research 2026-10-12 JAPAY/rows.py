# print v5 ledger rows by id: python -I rows.py LEDGER ID [ID...]
import csv, sys
rows = {r['id']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8-sig'))}
for i in sys.argv[2:]:
    r = rows.get(i)
    if not r:
        print(i, 'MISSING'); continue
    print(i, '|', r['quote_verbatim'][:1200]); print()
