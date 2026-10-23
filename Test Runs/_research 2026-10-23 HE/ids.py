import sys
import csv,sys
import io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
rows={}
with open(r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv',encoding='utf-8-sig') as f:
    r=csv.DictReader(f)
    for x in r: rows[x[r.fieldnames[0]]]=x
qcol=None
for i in sys.argv[1:]:
    x=rows.get(i)
    if not x: print(i,'MISSING'); continue
    q=[v for k,v in x.items() if k=='quote_verbatim']
    print(i,'|',(q[0] if q else str(x))[:700].replace('\n',' '))
    print()
