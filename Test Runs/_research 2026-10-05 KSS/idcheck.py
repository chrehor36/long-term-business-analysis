import csv,re,sys
rows={}
for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8')):
    rows[r.get('﻿id') or r['id']]=r['quote_verbatim']
s=open(sys.argv[1],encoding='utf-8').read()
norm=lambda t:re.sub(r'\s+',' ',t).strip()
eids=re.findall(r'\[E\d+-\d+\]',s); print('E-ids:',eids)
bad=0; prev=0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',s):
    i=m.group(1); seg=s[prev:m.start()]; prev=m.end()
    if i not in rows: print('MISSING ID',i); bad+=1; continue
    qs=re.findall(r'"([^"]+)"',seg)
    if not qs: print('NO QUOTE BESIDE',i,'|',norm(seg)[-90:]); bad+=1; continue
    q=qs[-1]; row=norm(rows[i])
    for part in q.split('[...]'):
        part=norm(part)
        if part and part not in row: print('NOT IN ROW',i,'|',part); bad+=1
print('ids checked; problems:',bad)
