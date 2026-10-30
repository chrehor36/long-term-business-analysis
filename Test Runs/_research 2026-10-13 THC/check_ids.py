# check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment directly before an id is in that row
import csv, re, sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2],encoding='utf-8-sig'))}
norm=lambda t: re.sub(r'\s+',' ',t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
bad=0
eids=re.findall(r'\[E\d+-\d+\]',run)
if eids: print('E-ids found',eids); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING',i); bad+=1
# fragments: "..." followed (within 12 chars) by **[ID]**
for m in re.finditer(r'"([^"]{6,400})"\s*(?:\*\*)?\[([MLR]\d{4}-\d{3})\]',run):
    frag,i=m.group(1),m.group(2)
    if i in rows and norm(frag) not in norm(rows[i]):
        # allow elision marks
        parts=[x.strip() for x in norm(frag).split('[...]')]
        if not all(x in norm(rows[i]) for x in parts if x):
            print('FRAGMENT NOT IN ROW',i,'|',frag[:120]); bad+=1
print('ids',len(set(ids)),'checked; problems',bad); print('PASS' if not bad else 'FAIL')
