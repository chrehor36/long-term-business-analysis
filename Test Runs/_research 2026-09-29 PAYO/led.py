import csv, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
rows = {r['﻿id'] if '﻿id' in r else r['id']: r for r in csv.DictReader(open('principle_ledger.csv', encoding='utf-8'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    if not r: print(i, 'MISSING'); continue
    print(i, r['year'], r['source_file'], '|', r['quote_verbatim'][:900], '|| concept:', r['concept'][:200]); print()
