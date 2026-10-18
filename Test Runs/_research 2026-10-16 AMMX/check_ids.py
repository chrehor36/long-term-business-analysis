import csv,re,sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={x['id']:x['quote_verbatim'] for x in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
norm=lambda s: re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
bad=0
if re.search(r'\[E\d-\d+\]',run): print('E-id found'); bad+=1
ids=list(re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run))
print('ids cited:',len(ids),'distinct:',len({m.group(1) for m in ids}))
for m in ids:
    if m.group(1) not in rows: print('MISSING',m.group(1)); bad+=1
prev=0
for m in ids:
    seg=run[max(prev,m.start()-260):m.start()]
    prev=m.end()
    q=re.findall(r'"([^"]{3,})"',seg)
    if not q: continue
    frag=q[-1]
    # only check the fragment if it ends within 40 chars of the id (i.e. it is beside it)
    tail=seg[seg.rfind('"')+1:]
    if len(tail)>40: continue
    f=norm(frag)
    parts=[p.strip(' .') for p in f.split('...') if p.strip(' .')]
    r=norm(rows.get(m.group(1),''))
    for p in parts:
        if p not in r: print('NOT IN ROW',m.group(1),'|',frag[:90]); bad+=1
print('problems:',bad)
