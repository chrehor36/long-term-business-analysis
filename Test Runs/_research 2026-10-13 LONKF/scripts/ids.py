import csv,sys
R={r['\ufeffid'] if '\ufeffid' in r else r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8'))}
for i in sys.argv[1:]:
    r=R.get(i); print('###',i, '' if r else 'MISSING'); 
    if r: print(r['quote_verbatim'][:900]); print()
