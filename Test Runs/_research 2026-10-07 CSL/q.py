import csv, sys, re
L = r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv'
rows = {r['id']: r for r in csv.DictReader(open(L, encoding='utf-8-sig'))}
if sys.argv[1] == '-s':
    pat = re.compile(sys.argv[2], re.I)
    for k, r in rows.items():
        if pat.search(r['quote_verbatim']):
            print(k, '|', r['quote_verbatim'][:300].replace('\n', ' '))
else:
    for i in sys.argv[1:]:
        r = rows.get(i)
        print(i, '::', r['quote_verbatim'] if r else 'MISSING')
        print()
