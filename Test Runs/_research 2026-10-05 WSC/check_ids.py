import csv,re,sys
R={r['﻿id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
t=open(r'Test Runs/2026-10-05 Run - WSC WillScot.md',encoding='utf-8').read()
bad=0
if re.search(r'\[E\d-\d+\]',t): print('E-ID FOUND'); bad+=1
norm=lambda s: re.sub(r'\s+',' ',s)
ids=list(re.finditer(r'\*\*\[([A-Z]\d{4}-\d{3})\]\*\*',t))
print('id occurrences',len(ids),'distinct',len({m.group(1) for m in ids}))
prev=0
for m in ids:
    i=m.group(1)
    if i not in R: print('MISSING',i); bad+=1; prev=m.end(); continue
    span=t[prev:m.start()]
    # quoted fragments in double quotes (straight or curly) within the span since previous id
    frs=re.findall(r'"([^"]{3,}?)"',span)+re.findall(r'“([^”]{3,}?)”',span)
    for fr in frs:
        parts=[p.strip() for p in fr.split('[...]')]
        for p in parts:
            if p and norm(p) not in norm(R[i]):
                print('NOT IN ROW',i,'::',p[:120]); bad+=1
    prev=m.end()
print('problems',bad)
