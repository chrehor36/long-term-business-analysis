import csv, sys
rows = {r['﻿id'] if '﻿id' in r else r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, '|', (r['quote_verbatim'][:600] if r else 'MISSING'), '\n')
