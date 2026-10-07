import csv,sys
ids=sys.argv[1:]
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
out=open('Test Runs/_research 2026-10-05 KTB/rows_out.txt','w',encoding='utf-8')
for i in ids:
    r=rows.get(i)
    out.write(i+' | '+('MISSING' if r is None else r['year']+' | '+r['quote_verbatim'][:900].replace('\n',' '))+'\n\n')
