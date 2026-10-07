import csv,re,sys
rows={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
t=open('Test Runs/2026-10-05 Run - GENC Gencor Industries.md',encoding='utf-8').read()
ids=re.findall(r'\[([A-Z]\d{4}-\d{3})\]',t)
bad=[i for i in ids if i not in rows]; e=[i for i in ids if i.startswith('E')]
print('ids cited',len(ids),'distinct',len(set(ids)),'missing',bad,'E-ids',e)
# every quoted fragment immediately followed (within the same line, before next quote) by **[ID]**
fails=0;checked=0
for line in t.split('\n'):
    for m in re.finditer(r'"([^"]{3,})"\s*((?:\*\*\[[A-Z]\d{4}-\d{3}\]\*\*[,\s]*)+)',line):
        frag=m.group(1); cid=re.findall(r'\[([A-Z]\d{4}-\d{3})\]',m.group(2))
        parts=[p.strip(' .') for p in frag.split('[...]') if p.strip(' .')]
        ok=any(all(p in rows.get(c,'') for p in parts) for c in cid)
        checked+=1
        if not ok: fails+=1; print('FAIL',cid,'|',frag)
print('fragments checked',checked,'fails',fails)
print('em dashes outside headings/labels:',[l[:80] for l in t.split('\n') if '—' in l and not l.startswith('#') and 'COMPUTATION' not in l])
