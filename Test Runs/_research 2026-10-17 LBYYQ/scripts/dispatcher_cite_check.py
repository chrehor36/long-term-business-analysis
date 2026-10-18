import csv,re,sys
rows={r['id'] if 'id' in r else list(r.values())[0]:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
t=open(sys.argv[1],encoding='utf-8').read()
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip().lower()
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t); bad=[i for i in set(ids) if i not in rows]; print('ids',len(set(ids)),'missing',bad, 'E-ids', re.findall(r'\[E\d-\d+\]',t))
n=0;slip=0
for m in re.finditer(r'"([^"]{8,})"\s*\**\s*\[([MLR]\d{4}-\d{3})\]',t.replace('“','"').replace('”','"')):
    q,i=m.group(1),m.group(2); n+=1
    txt=norm(' '.join(rows[i].values()))
    parts=[p for p in norm(q).split('[...]') if p.strip()]
    if not all(p.strip(' .,') in txt for p in parts): slip+=1; print('SLIP',i,q[:90])
print('fragments',n,'slips',slip)
