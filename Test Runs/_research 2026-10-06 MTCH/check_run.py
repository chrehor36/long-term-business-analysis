import csv,re,sys
f='Test Runs/2026-10-06 Run - MTCH Match Group.md'
t=open(f,encoding='utf-8').read()
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
bad=0
print('em dashes:',t.count('—'),' en dashes:',t.count('–'))
eids=re.findall(r'\[E\d-\d+\]',t); print('E-ids:',eids)
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)
print('ids cited:',len(ids),'distinct',len(set(ids)))
for i in set(ids):
    if i not in rows: print('MISSING',i); bad+=1
norm=lambda s: re.sub(r'\s+',' ',s.replace('“','"').replace('”','"')).strip()
# each id: the quoted strings between the previous id (or paragraph start) and this id
for para in re.split(r'\n\s*\n|\n(?=[-|0-9])',t):
    pos=0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',para):
        seg=para[pos:m.start()]; pos=m.end()
        qs=re.findall(r'"([^"]+)"',seg)
        if not qs: continue
        # only the quotes in the clause just before the id: take quotes after last ';' or '.' boundary not inside quotes -> simple: last 2
        row=norm(rows[m.group(1)]['quote_verbatim'])
        for q in qs:
            for frag in q.split('[...]'):
                frag=norm(frag).strip(' ,.')
                if frag and frag not in row:
                    print('NOT IN ROW',m.group(1),'|',frag[:90]); bad+=1
print('problems:',bad)
