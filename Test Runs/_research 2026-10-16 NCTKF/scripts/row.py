import csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
ids=set(sys.argv[1:])
with open('principle_ledger_v5.csv',encoding='utf-8') as f:
    r=csv.DictReader(f)
    for row in r:
        if row[r.fieldnames[0]] in ids:
            q=[v for k,v in row.items() if 'quote' in k.lower()]
            print(row[r.fieldnames[0]],'|',(q[0] if q else '')[:900]); print()
