# Citation check for the MT run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id (same sentence/clause) appears in that row's quote.
import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')
run=open('Test Runs/2026-10-13 Run - MT ArcelorMittal.md',encoding='utf-8').read()
rows={r[0]:r[2] for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
bad=0
e=re.findall(r'\[E\d+-\d+\]',run)
print('E-ids:',e); bad+=len(e)
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
miss=sorted(set(i for i in ids if i not in rows))
print('ids cited:',len(set(ids)),'missing:',miss); bad+=len(miss)
def norm(x):
    x=x.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','-').replace('–','-')
    return re.sub(r'\s+',' ',x).strip().lower()
# fragment = last "..." before an id, within 60 chars of the id
for m in re.finditer(r'"([^"]{8,600})"\s*(\([^)]*\))?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    frag,i=m.group(1),m.group(3)
    parts=[p.strip() for p in frag.split('[...]')]
    ok=all(norm(p).strip(' .,;') in norm(rows.get(i,'')) for p in parts if p)
    if not ok:
        bad+=1; print('NOT IN ROW',i,':',frag[:120])
print('quoted fragments checked:',len(re.findall(r'"[^"]{8,600}"\s*(?:\([^)]*\))?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*',run)))
print('RESULT:','PASS' if bad==0 else 'FAIL (%d)'%bad)
