# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# immediately before an id (within the same sentence) appears in that row's quote. Usage: python -I idcheck.py
import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8')
root='C:/Users/chreh/OneDrive/Documents/BRK/'
run=open(root+'Test Runs/2026-10-13 Run - JCSE JE Cleantech Holdings.md',encoding='utf-8').read()
rows={}
with open(root+'principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.reader(f); h=next(r)
    for row in r: rows[row[0]]=row[2]
bad=0
eids=re.findall(r'\[E\d-\d+\]',run); print('E-ids:',eids); bad+=len(eids)
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run)
print('ids cited:',len(ids),'distinct:',len(set(ids)))
for i in set(ids):
    if i not in rows: print('MISSING',i); bad+=1
def norm(x):
    x=x.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')
    return re.sub(r'\s+',' ',x).strip()
# quoted fragment followed (within 12 chars) by one or more ids
for m in re.finditer(r'"([^"\n]{6,400})"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)',run):
    frag=m.group(1); cited=re.findall(r'([MLR]\d{4}-\d{3})',m.group(2))
    parts=[p.strip() for p in frag.split('[...]') if p.strip()]
    ok=any(all(norm(p) in norm(rows.get(c,'')) for p in parts) for c in cited)
    if not ok: print('FRAGMENT NOT IN ROW',cited,':',frag[:120]); bad+=1
print('RESULT', 'PASS' if bad==0 else 'FAIL', bad)
