# print v5 ledger rows by id: python row.py ID [ID...]
import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
R={r['id']:r for r in csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=R.get(i); print('==',i, '(MISSING)' if not r else r['year']+' '+r['source_file']); 
    if r: print(r['quote_verbatim']); print()
