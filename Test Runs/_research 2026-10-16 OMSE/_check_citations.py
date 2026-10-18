# Citation check for the OMSE run: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment
# that sits in the same sentence-chunk immediately before an id is a substring of that row's quote (quotes normalised).
import csv,re,sys
run=open(sys.argv[1],encoding='utf-8').read()
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('�','')
    return re.sub(r'\s+',' ',s).strip().lower()
bad=0
eids=re.findall(r'\[E\d-\d+\]',run)
if eids: print('E-ids found',eids); bad+=1
ids=re.findall(r'\[([MLR]\d{4}-\d{3})\]',run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id',i); bad+=1
# fragments: a "..." quote followed (within 12 chars, allowing ** and spaces/commas) by **[ID]**
for m in re.finditer(r'"([^"\n]{6,400})"\s*(?:\*\*)?\s*\[([MLR]\d{4}-\d{3})\]',run.replace('\n',' ')):
    frag,i=m.group(1),m.group(2)
    if i in rows:
        parts=[p for p in re.split(r'\[\.\.\.\]',frag) if p.strip()]
        for p in parts:
            if norm(p).strip(' .,') not in norm(rows[i]):
                print('NOT IN ROW',i,'|',p[:120]); bad+=1
print('ids cited:',len(set(ids)),'quote-id pairs checked:',len(re.findall(r'"([^"\n]{6,400})"\s*(?:\*\*)?\s*\[([MLR]\d{4}-\d{3})\]',run.replace('\n',' '))))
print('PASS' if not bad else f'FAIL ({bad})')
