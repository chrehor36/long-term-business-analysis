import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
R={r['﻿id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    r=R.get(i); print(f"[{i}] {r['year'] if r else 'MISSING'}: {r['quote_verbatim'] if r else ''}\n")
