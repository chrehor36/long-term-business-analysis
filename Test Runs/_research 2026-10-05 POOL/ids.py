import csv,sys
r={x['﻿id']:x for x in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    x=r.get(i)
    print(i, '::', x['quote_verbatim'] if x else 'MISSING')
    print()
