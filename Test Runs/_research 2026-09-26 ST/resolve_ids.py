import re,csv
s=open('Test Runs/2026-09-26 Run - ST Sensata Technologies.md',encoding='utf-8').read()
ids=sorted(set(re.findall(r'E\d-\d+',s)))
led={r[0].lstrip('﻿') for r in csv.reader(open('principle_ledger.csv',encoding='utf-8'))}
miss=[i for i in ids if i not in led]
print(len(ids),'ids; missing:',miss)
