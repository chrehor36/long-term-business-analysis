# Check for the CHD run of 2026-10-07: no E-ids; every M/L/R id exists in the v5 ledger;
# every quoted fragment immediately before an id is in that row (quotes ending within 400 chars before the id).
import csv,re,sys
L={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-07 Run - CHD Church & Dwight.md',encoding='utf-8').read()
bad=0
for m in re.finditer(r'\[E\d-\d+\]',t): print('E-id',m.group()); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)
for i in sorted(set(ids)):
    if i not in L: print('MISSING',i); bad+=1
norm=lambda x: re.sub(r'\s+',' ',x.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip()
# fragment check: a "..." quote followed (within 12 chars) by **[id]**
for m in re.finditer(r'"([^"\n]{6,400}?)"[^"\n]{0,14}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2)
    if i in L:
        parts=[p for p in frag.split('[...]')]
        for p in parts:
            p=norm(p).strip(' .,')
            if p and p not in norm(L[i]):
                print('NOT IN ROW',i,'::',frag[:90]); bad+=1
print('ids cited',len(set(ids)),'problems',bad)
sys.exit(1 if bad else 0)
