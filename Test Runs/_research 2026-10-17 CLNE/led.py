import csv,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
P='C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv'
ids=sys.argv[1:]
rows={r['id']:r for r in csv.DictReader(open(P,encoding='utf-8-sig'))}
for i in ids:
    r=rows.get(i)
    print(i,'|',r['quote_verbatim'] if r else 'MISSING','\n')
