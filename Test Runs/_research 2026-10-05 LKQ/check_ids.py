import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-05 Run - LKQ LKQ Corporation.md',encoding='utf-8').read()
bad=0
eids=re.findall(r'\[E\d+-\d+\]',t); print('E-ids:',eids)
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
missing=sorted({i for i in ids if i not in rows}); print('ids cited:',len(set(ids)),'missing:',missing)
norm=lambda s: re.sub(r'\s+',' ',s)
pos=[(m.start(),m.group(1)) for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)]
prev=0; checked=0
for p,i in pos:
    seg=t[prev:p]; prev=p+len(i)+6
    qs=re.findall(r'"([^"]+)"',seg)
    if not qs: continue
    q=qs[-1]
    for frag in [x.strip(' .,;') for x in q.split('[...]')]:
        if not frag: continue
        checked+=1
        if norm(frag) not in norm(rows.get(i,'')):
            bad+=1; print('NOT IN ROW',i,'::',frag[:120])
print('fragments checked',checked,'bad',bad)
