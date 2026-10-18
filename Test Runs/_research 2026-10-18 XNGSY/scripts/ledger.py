# Print v5 ledger rows by id, or search quotes: python -I ledger.py ID [ID...] | python -I ledger.py -s "phrase"
import csv, sys, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'principle_ledger_v5.csv')
rows = {r['﻿id'] if '﻿id' in r else r['id']: r for r in csv.DictReader(open(P, encoding='utf-8'))}
a = sys.argv[1:]
if a and a[0] == '-s':
    for k, r in rows.items():
        if all(x.lower() in r['quote_verbatim'].lower() for x in a[1:]): print(k, '|', r['quote_verbatim'][:300])
else:
    for k in a: print(k, '|', rows[k]['quote_verbatim'] if k in rows else 'MISSING'); print()
