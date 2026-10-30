# Checks the WKC run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment adjacent to an id is in that row.
import csv,re
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
s=open('Test Runs/2026-10-06 Run - WKC World Kinect.md',encoding='utf-8').read()
norm=lambda x:re.sub(r'\s+',' ',x).strip()
ids=re.findall(r'\[([A-Z]+\d{4}-\d{3}[A-Za-z-]*)\]',s)
bad=[i for i in ids if i.startswith('E') or i not in rows]
print('ids cited',len(ids),'distinct',len(set(ids)),'| E-ids or missing:',bad)
n=f=0
def ok(q,i): return all(norm(p).strip(' .') in norm(rows[i]) for p in q.replace('...','[...]').split('[...]') if p.strip(' .'))
for m in re.finditer(r'"([^"]{3,700})"[\s.,;:)]{0,4}\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*',s,flags=re.S):
    n+=1; f+= not ok(norm(m.group(1)),m.group(2))
for m in re.finditer(r'\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*:? *\(?"([^"]{3,700})"',s,flags=re.S):
    n+=1; f+= not ok(norm(m.group(2)),m.group(1))
print('quote-id pairs checked',n,'| failures',f,'| em dashes',s.count('—'))
