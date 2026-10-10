"""Run-file citation check: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment adjacent to an id is in that row."""
import csv,re,sys
RUN='C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-07 Run - ATR AptarGroup.md'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(RUN,encoding='utf-8').read()
def norm(s):
    s=s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2014','-').replace('\u2013','-')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
for m in re.finditer(r'\[E\d-\d+\]',t): print('E-id',m.group()); bad+=1
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',t))
for i in sorted(ids):
    if i not in rows: print('PHANTOM',i); bad+=1
# quoted fragment immediately before an id (within the same sentence chunk)
for m in re.finditer(r'"([^"]{3,400})"\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2)
    if i not in rows: continue
    parts=[p for p in frag.split('[...]') if p.strip()]
    for p in parts:
        if norm(p) not in norm(rows[i]):
            print('NOT IN ROW',i,'|',p[:120]); bad+=1
print('ids',len(ids),'problems',bad)
