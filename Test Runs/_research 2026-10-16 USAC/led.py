import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
hdr=next(csv.reader(open('principle_ledger_v5.csv',encoding='utf-8')))
qi=[i for i,h in enumerate(hdr) if 'quote' in h.lower() or 'text' in h.lower()]
for i in sys.argv[1:]:
    r=rows.get(i)
    if not r: print(i,'MISSING'); continue
    q=r[qi[0]] if qi else r[2]
    print(f"{i}: {q[:900]}\n")
