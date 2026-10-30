# Check the run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment that sits
# immediately before an id (same clause, no other id between) is found verbatim in that row (elisions [...] split).
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
R={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('../2026-10-07 Run - ACLS Axcelis.md',encoding='utf-8').read()
bad=0
for m in re.finditer(r'\[E\d-\d+\]',t): print('E-id found',m.group()); bad+=1
ids=list(re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t))
print('id occurrences',len(ids),'distinct',len(set(m.group(1) for m in ids)))
norm=lambda s:re.sub(r'\s+',' ',s).strip()
prev_end=0
for m in ids:
    i=m.group(1)
    if i not in R: print('MISSING',i); bad+=1; prev_end=m.end(); continue
    # walk back from the id over quotes chained with short gaps (the quotes that belong to this id)
    pos=m.start(); lo=max(prev_end,0); qs=[]
    while True:
        seg=t[lo:pos]
        mm=re.search(r'"([^"]+)"([^"]{0,60})$',seg)
        if not mm or re.search(r'\.\s',mm.group(2)) or '**[' in mm.group(2): break
        qs.append(mm.group(1)); pos=lo+mm.start()
    for q in qs:
        for frag in [f for f in re.split(r'\[\.\.\.\]',q) if len(f.strip())>3]:
            if norm(frag) not in norm(R[i]):
                print(f'NOT IN ROW {i}: "{frag.strip()[:120]}"'); bad+=1
    prev_end=m.end()
print('problems',bad)
