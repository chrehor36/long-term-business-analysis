# Checks the PRKS run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id is in that row (split on [...]).
import csv,re,sys
root='C:/Users/chreh/OneDrive/Documents/BRK/'
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(root+'principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(root+'Test Runs/2026-10-05 Run - PRKS United Parks and Resorts.md',encoding='utf-8').read()
bad=0
eids=re.findall(r'\[E\d+-\d+\]',t)
if eids: print('E-ids found',eids); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
norm=lambda s: re.sub(r'\s+',' ',s)
# quoted fragment(s) followed (within 40 chars, no other quote) by **[ID]**
for m in re.finditer(r'"([^"]+)"([^"]{0,40}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,mid,i=m.group(1),m.group(2),m.group(3)
    if i not in rows: continue
    row=norm(rows[i])
    for part in frag.split('[...]'):
        part=norm(part).strip().strip('.,;: ')
        if not part: continue
        if part not in row:
            print('NOT IN ROW',i,'|',part[:90]); bad+=1
print('ids cited:',len(set(ids)),'checked fragments OK' if not bad else 'FAILURES %d'%bad)
