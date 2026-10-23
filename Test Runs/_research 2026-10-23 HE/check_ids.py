import csv,re,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
rows={x['id']:x['quote_verbatim'] for x in csv.DictReader(open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open(r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-23 Run - HE Hawaiian Electric Industries.md',encoding='utf-8').read()
bad=0
if re.search(r'\[E\d-\d+\]',t): print('E-id found'); bad+=1
ids=re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
# quoted fragment directly before an id: "...." then up to 3 chars then **[ID]**
for m in re.finditer(r'"([^"]{3,}?)"[\s,.;:)]{0,3}\*\*\[([MLR]\d{4}-\d{3})\]\*\*',t):
    frag,i=m.group(1),m.group(2)
    if i not in rows: continue
    for part in [re.sub(r"\s+"," ",p).strip(" .,;") for p in frag.split("[...]")]:
        if part and part not in re.sub(r"\s+"," ",rows[i]):
            print('NOT IN ROW',i,'|',part[:120]); bad+=1
print('ids',len(set(ids)),'bad',bad)
