import csv,sys
rows={r[list(r.keys())[0]]:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
k=list(next(iter(rows.values())).keys())
for i in sys.argv[1:]:
    r=rows.get(i)
    if not r: print(i,'MISSING'); continue
    q=[v for kk,v in r.items() if 'quote' in kk.lower() or 'text' in kk.lower()]
    print(i,'|',(q[0] if q else r)[:600].replace('\n',' '));print()
