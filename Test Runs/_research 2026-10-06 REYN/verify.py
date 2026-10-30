import csv,re,sys,unicodedata
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-06 Run - REYN Reynolds Consumer Products.md',encoding='utf-8').read()
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','')
    return re.sub(r'\s+',' ',s).strip().lower()
eids=re.findall(r'\[E\d-\d+\]',t); print('E-ids:',eids)
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t); allids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
missing=[i for i in allids if i not in rows]; print('ids cited:',len(allids),'missing:',missing)
# every quoted fragment immediately preceding an id (within same paragraph, nearest quote before id)
bad=0; checked=0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    i=m.group(1); pre=t[max(0,m.start()-700):m.start()]
    # take text after the previous id marker
    k=max(pre.rfind(']**'),pre.rfind('\n\n'))
    seg=pre[k+3:] if k>=0 else pre
    for q in re.findall(r'"([^"]{6,})"|“([^”]{6,})”',seg):
        q=q[0] or q[1]
        # quotes that are filing text: skip if not in row and contains filing markers? check all, report misses
        for frag in q.split('[...]'):
            f=norm(frag).strip(' .,;:')
            if len(f)<5: continue
            checked+=1
            if f not in norm(rows[i]):
                bad+=1; print('NOT IN ROW',i,'|',frag.strip()[:120])
print('fragments checked',checked,'misses',bad)
