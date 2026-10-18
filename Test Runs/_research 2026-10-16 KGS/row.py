import csv,sys
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
hdr=next(csv.reader(open('principle_ledger_v5.csv',encoding='utf-8')))
qi=[i for i,h in enumerate(hdr) if 'quote' in h.lower()][0]
for i in sys.argv[1:]:
    r=rows.get(i); print(i, '::', r[qi] if r else 'MISSING'); print()
