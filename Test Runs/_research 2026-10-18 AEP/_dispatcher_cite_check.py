import csv,re,sys
csv.field_size_limit(10**8)
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.reader(f);h=next(r)
    qi=[i for i,c in enumerate(h) if 'quote' in c.lower()][0]
    for x in r: rows[x[0]]=x[qi]
def norm(s): return re.sub(r'\s+',' ',s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
t=open(sys.argv[1],encoding='utf-8').read()
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
bad=[i for i in ids if i not in rows];print('ids',len(ids),'unique',len(set(ids)),'missing',bad)
print('E-ids',re.findall(r'\[E\d-\d+\]',t))
n=0;slips=[]
for m in re.finditer(r'"([^"\n]{6,}?)"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]',t.replace('\u201c','"').replace('\u201d','"')):
    q,i=m.group(1),m.group(2);n+=1
    parts=[p for p in re.split(r'\[\.\.\.\]|\.\.\.|…',q) if p.strip()]
    if i in rows and not all(norm(p).strip(' .,;:') in norm(rows[i]) for p in parts): slips.append((i,q))
print('adjacent fragments',n,'slips',len(slips))
for s in slips: print(' SLIP',s)
