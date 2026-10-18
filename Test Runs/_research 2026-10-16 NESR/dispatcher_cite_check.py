import csv,re,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
qcol=[k for k in next(iter(rows.values())).keys() if 'quote' in k.lower()][0]
norm=lambda s:re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
txt=open(sys.argv[1],encoding='utf-8').read()
ids=set();miss=[];checked=0
for para in re.split(r'\n\s*\n',txt):
    pids=re.findall(r'\b([MLR]\d{4}-\d{3})\b',para)
    if re.search(r'\bE\d-\d{2}\b',para): miss.append(('E-id',para[:80]))
    for i in pids:
        ids.add(i)
        if i not in rows: miss.append(('phantom',i))
    if not pids: continue
    pool=' '.join(norm(rows[i][qcol]) for i in pids if i in rows)
    for q in re.findall(r'["\u201c]([^"\u201d]{12,})["\u201d]',para):
        for frag in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',q):
            f=norm(frag).strip(' .,;:')
            if len(f)<8: continue
            checked+=1
            if f not in pool:
                # filing quotes in same paragraph are expected; report for review
                miss.append(('notin',pids,f[:90]))
print('ids',len(ids),'fragments',checked)
for m in miss: print(m)
# tight check: a quotation immediately followed by a bold id
print('--- tight')
n=0
for m in re.finditer(r'["\u201c]([^"\u201c\u201d\n]{6,400})["\u201d][\s,.;:)]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]\*\*',txt):
    q,i=m.group(1),m.group(2); n+=1
    src=norm(rows[i][qcol]) if i in rows else ''
    for frag in re.split(r'\[\.\.\.\]|\.\.\.|\u2026',q):
        f=norm(frag).strip(' .,;:')
        if len(f)>=4 and f not in src: print('SLIP',i,'|',f[:100])
print('tight pairs',n)
