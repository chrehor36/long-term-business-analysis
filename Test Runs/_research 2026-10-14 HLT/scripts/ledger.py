import csv, sys, re
rows = {r['\ufeffid'] if '\ufeffid' in r else r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
mode = sys.argv[1]
if mode == 'id':
    for i in sys.argv[2:]:
        r = rows.get(i); print(i, '::', r['quote_verbatim'] if r else 'MISSING'); print()
else:
    pat = re.compile(sys.argv[2], re.I)
    for i, r in rows.items():
        if pat.search(r['quote_verbatim']): print(i, '::', r['quote_verbatim'][:400].replace('\n',' ')); print()
