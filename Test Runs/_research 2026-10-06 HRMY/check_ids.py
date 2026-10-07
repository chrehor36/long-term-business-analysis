# Checks the HRMY run file: no E-ids, every M/L/R id in the v5 ledger, every quoted fragment beside an id in that row.
import csv,re
rows={r['id']:re.sub(r'\s+',' ',r['quote_verbatim']) for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=re.sub(r'\s+',' ',open('Test Runs/2026-10-06 Run - HRMY Harmony Biosciences.md',encoding='utf-8').read())
bad=0
if re.search(r'\[E\d',t): print('E-id found'); bad+=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
for i in sorted(ids):
    if i not in rows: print('MISSING',i); bad+=1
n=0
for m in re.finditer(r'"([^"]{3,600}?)"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2); n+=1
    for p in frag.split('[...]'):
        p=p.strip(' .,;')
        if p and p not in rows.get(i,''): print('NOT IN ROW',i,'|',p); bad+=1
print('distinct ids',len(ids),'| quote-id pairs',n,'| em dashes',t.count('—'),'|','FAIL' if bad else 'PASS')
