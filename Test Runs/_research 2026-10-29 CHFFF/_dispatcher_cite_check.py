import csv,re,sys
rows={}
for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8')):
    k=list(r.keys()); rows[r[k[0]]]=r
qcol=[c for c in k if 'quote' in c.lower()][0]
t=open(sys.argv[1],encoding='utf-8').read()
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).lower()
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t); bad=[i for i in set(ids) if i not in rows]
print('ids',len(set(ids)),'missing',bad, 'E-ids',re.findall(r'\[E\d+-\d+\]',t))
n=0;slips=0
for m in re.finditer(r'["“]([^"”]{8,400})["”][^"“\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]',t):
    n+=1;frag,i=m.group(1),m.group(2)
    parts=[p.strip(' .,;') for p in re.split(r'\[\.\.\.\]|\.\.\.',frag) if p.strip(' .,;')]
    if not all(norm(p) in norm(rows[i][qcol]) for p in parts): slips+=1;print('SLIP',i,frag[:100])
print('pairs',n,'slips',slips)
