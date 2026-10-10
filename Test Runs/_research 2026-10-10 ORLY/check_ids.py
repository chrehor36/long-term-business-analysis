# Check for the ORLY run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment written
# beside an id (same paragraph, within the quote marks just before the id) appears in that row (whitespace normalised,
# [...] elisions split into pieces).
import csv,re,sys
root=r"C:\Users\chreh\OneDrive\Documents\BRK"
rows={r['id']:r['quote_verbatim'] for r in csv.DictReader(open(root+r"\principle_ledger_v5.csv",encoding='utf-8-sig'))}
run=open(root+r"\Test Runs\2026-10-10 Run - ORLY O'Reilly Automotive.md",encoding='utf-8').read()
norm=lambda t: re.sub(r'\s+',' ',t.replace('\u201c','"').replace('\u201d','"')).strip()
bad=0
e=re.findall(r'\[E\d-\d+\]',run)
print('E-ids:',e); bad+=len(e)
ids=set(re.findall(r'\[([MLR]\d{4}-\d{3})\]',run))
miss=[i for i in ids if i not in rows]; print('ids used:',len(ids),'missing:',miss); bad+=len(miss)
# quotes: "...." immediately followed (within 12 chars) by **[ID]** or [ID]
flat=norm(run)
for m in re.finditer(r'"([^"]{8,600})"\s*(?:\*\*)?\s*\[([MLR]\d{4}-\d{3})\]',flat):
    q,i=m.group(1),m.group(2)
    row=norm(rows.get(i,''))
    for piece in [x.strip(' .,;') for x in q.split('[...]')]:
        if piece and norm(piece) not in row:
            print('NOT IN ROW',i,'|',piece[:120]); bad+=1
print('FAIL' if bad else 'PASS')
