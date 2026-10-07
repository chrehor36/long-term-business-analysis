import csv,sys
sys.stdout.reconfigure(encoding='utf-8')
rows={r['id']:r for r in csv.DictReader(open('principle_ledger.csv',encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r=rows.get(i)
    if not r: print('\n## MISSING',i); continue
    print('\n##',i, r['year'], r['source_file'], '|', r['concept'][:120]); print(r['quote_verbatim'][:int(900)])
