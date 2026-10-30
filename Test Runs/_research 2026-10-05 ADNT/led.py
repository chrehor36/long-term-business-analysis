import csv,re,sys
rows=list(csv.DictReader(open('../../principle_ledger_v5.csv',encoding='utf-8-sig')))
byid={r['id']:r for r in rows}
if sys.argv[1]=='id':
    for i in sys.argv[2:]:
        r=byid.get(i); print('==',i, '' if r else 'MISSING')
        if r: print(r['quote_verbatim']); print('  [',r['source_file'],']')
else:
    pat=re.compile(sys.argv[2],re.I)
    for r in rows:
        if pat.search(r['quote_verbatim']):
            print(r['id'],'|',r['quote_verbatim'][:int(sys.argv[3]) if len(sys.argv)>3 else 300].replace('\n',' '));print()
