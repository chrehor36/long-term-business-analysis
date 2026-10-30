import csv,sys
r={x['﻿id']:x for x in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    x=r.get(i)
    print(f"[{i}]", "MISSING" if not x else x['quote_verbatim'][:700].replace("\n"," "))
