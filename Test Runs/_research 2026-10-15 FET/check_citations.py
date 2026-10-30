"""Citation check for the FET run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment immediately beside an id (the last quotation ending within a few characters before it) is in that row."""
import csv, re, sys, os, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.join(here,'..','..')
rows={r[0]:r[2] for r in csv.reader(open(os.path.join(root,'principle_ledger_v5.csv'),encoding='utf-8'))}
run=open(os.path.join(root,'Test Runs','2026-10-15 Run - FET Forum Energy Technologies.md'),encoding='utf-8').read()
def norm(t): 
    t=unicodedata.normalize('NFC',t); t=re.sub(r'\s+',' ',t); return t
bad=0
eids=re.findall(r'\[E\d+-\d+\]',run); print('E-ids:',eids); bad+=len(eids)
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
print('distinct ids',len(set(ids)),'uses',len(ids))
flat=norm(run)
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',flat):
    pre=flat[max(0,m.start()-8):m.start()]
    if '"' not in pre and '”' not in pre: continue
    # find the quotation that ends right before the id
    end=flat.rfind('"',0,m.start())
    start=flat.rfind('"',0,end)
    frag=flat[start+1:end]; print("checked",m.group(1),"|",frag[:70])
    for part in frag.split('[...]'):
        part=part.strip(' .,;:')
        if part and part not in norm(rows[m.group(1)]):
            print('NOT IN ROW',m.group(1),'|',part[:120]); bad+=1
print('RESULT', 'PASS' if bad==0 else f'FAIL ({bad})')
