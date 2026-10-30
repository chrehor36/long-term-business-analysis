import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
rows={}
for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8')):
    k=r.get('﻿id') or r.get('id'); rows[k]=r['quote_verbatim']
txt=open(sys.argv[1],encoding='utf-8').read()
norm=lambda s: re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip().lower()
bad=0
if re.search(r'\[E\d-\d+\]',txt): print('E-id found'); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
# quoted fragment immediately before an id: "..." **[ID]** (allow up to 40 chars between)
for m in re.finditer(r'"([^"]{6,}?)"[^"]{0,45}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt):
    q,i=m.group(1),m.group(2)
    if i not in rows: continue
    src=norm(rows[i])
    for part in q.split('[...]'):
        p=norm(part).strip(' .,;:')
        if p and p not in src:
            print('FRAGMENT NOT IN ROW',i,'::',part[:120]); bad+=1
print('ids checked',len(set(ids)),'problems',bad)
