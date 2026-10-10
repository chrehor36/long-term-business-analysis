import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
L={r['id']:r for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=L.get(i); print('##',i, '' if r else 'MISSING'); 
    if r: print(r['quote_verbatim'][:900])
