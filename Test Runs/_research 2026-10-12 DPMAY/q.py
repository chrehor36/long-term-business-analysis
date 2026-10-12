# print v5 ledger rows by id: python q.py ID [ID ...]
import csv, sys
rows = {r['﻿id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, '=>', r['quote_verbatim'] if r else 'MISSING'); print()
