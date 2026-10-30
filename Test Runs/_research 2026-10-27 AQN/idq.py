import csv, sys
r={x[0].lstrip('﻿'):x for x in csv.reader(open('C:/Projects/BRK/principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    x=r.get(i); print(i, x[3] if x else 'MISSING', '|', (x[2][:400] if x else ''))
