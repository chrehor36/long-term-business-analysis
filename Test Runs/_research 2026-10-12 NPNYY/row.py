import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
rows={r[0]:r for r in csv.reader(open('principle_ledger_v5.csv',encoding='utf-8'))}
hdr=rows.get('id') or next(iter(rows.values()))
for i in sys.argv[1:]:
    r=rows.get(i)
    print(i, '->', 'MISSING' if r is None else r[2][:900] if len(r)>1 else r)
    print()
