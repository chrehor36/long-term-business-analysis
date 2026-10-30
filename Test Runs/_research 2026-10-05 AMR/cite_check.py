# Citation check for the AMR run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment adjacent to an id (same line, preceding the id) appears in that row's quote.
import csv,re,sys
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
t=open('Test Runs/2026-10-05 Run - AMR Alpha Metallurgical.md',encoding='utf-8').read()
bad=0
e=re.findall(r'\[E\d+-\d+\]',t)
if e: print('E-ids:',e); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
norm=lambda x: re.sub(r'\s+',' ',x.replace('’',"'").replace('“','"').replace('”','"'))
# fragments: "..." immediately before **[ID]** (allowing up to a few words between)
text=t.replace('\n',' ')
for m in re.finditer(r'"([^"]{8,}?)"((?:(?!\*\*\[)[^"]){0,40})\*\*\[([MLR]\d{4}-\d{3})\]\*\*',text):
    frag,idd=m.group(1),m.group(3)
    q=norm(rows.get(idd,''))
    for part in frag.split('[...]'):
        part=norm(part).strip(' .,')
        if part and part not in q:
            print('NOT IN ROW',idd,'|',part[:90]); bad+=1
print('ids cited:',len(set(ids)),'| problems:',bad)
sys.exit(1 if bad else 0)
