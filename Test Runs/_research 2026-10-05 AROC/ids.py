import csv,sys
rows={r['id']:r for r in csv.DictReader(open('principle_ledger_v5.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=rows.get(i)
    print('##',i, '' if r else 'MISSING')
    if r: print(r['quote_verbatim'][:1500]); print('   [',r['source_file'],'|',r['concept'][:150],']')
