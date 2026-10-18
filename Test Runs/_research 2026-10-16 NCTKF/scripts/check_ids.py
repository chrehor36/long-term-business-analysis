# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment written
# directly before an id is verbatim in that row ([...] splits a fragment into pieces, each checked).
import csv,re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
run=open('Test Runs/2026-10-16 Run - NCTKF Nabtesco.md',encoding='utf-8').read()
rows={}
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    for r in csv.DictReader(f): rows[r['﻿id'] if '﻿id' in r else r['id']]=r['quote_verbatim']
bad=0
eids=re.findall(r'\[E\d+-\d+\]',run)
if eids: print('E-ids found:',eids); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
norm=lambda s:' '.join(s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').split())
for m in re.finditer(r'"([^"\n]{3,400})"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    frag,i=m.group(1),m.group(2)
    row=norm(rows.get(i,''))
    for piece in frag.split('[...]'):
        p=norm(piece.strip())
        if p and p not in row:
            # tolerate curly vs straight quotes only through norm; report otherwise
            print('NOT IN ROW',i,'|',p); bad+=1
print('ids cited:',len(set(ids)),'| quote-before-id checks:',len(re.findall(r'"([^"\n]{3,400})"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run)),'| problems:',bad)
