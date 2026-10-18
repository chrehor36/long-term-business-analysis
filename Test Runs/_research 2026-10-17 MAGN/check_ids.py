# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment immediately before an id is in that row's quote (ellipses [...] split the fragment).
import csv,re,sys,unicodedata
root='C:/Users/chreh/OneDrive/Documents/BRK/'
run=open(root+'Test Runs/2026-10-17 Run - MAGN Magnera.md',encoding='utf-8').read()
rows={r['\ufeffid']:r['quote_verbatim'] for r in csv.DictReader(open(root+'principle_ledger_v5.csv',encoding='utf-8'))}
norm=lambda t: re.sub(r'\s+',' ',t.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
bad=0
e=re.findall(r'\[E\d-\d+\]',run)
if e: print('E-ids found',e); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# quoted fragments: "..." followed within 6 chars by **[ID]
for m in re.finditer(r'"([^"]{6,600})"\s*(?:\(?[^"\[]{0,8})?\*\*\[([MLR]\d{4}-\d{3})\]\*\*',run):
    frag,i=m.group(1),m.group(2)
    if i not in rows: continue
    q=norm(rows[i])
    for part in frag.split('[...]'):
        part=norm(part).strip(' .,')
        if part and part not in q:
            print('NOT IN ROW',i,'::',part[:120]); bad+=1
print('ids cited:',len(set(ids)),' problems:',bad)
