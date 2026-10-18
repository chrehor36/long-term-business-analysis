import csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8",errors="replace")
R={r['﻿id']:r for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    r=R.get(i); print('==',i, '(MISSING)' if not r else r['year']); 
    if r: print(r['quote_verbatim'][:900])
