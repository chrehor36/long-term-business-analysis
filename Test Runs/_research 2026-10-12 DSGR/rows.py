# print ledger rows by id: rows.py ID [ID ...]
import csv, sys
r = {x['﻿id'] if '﻿id' in x else x['id']: x for x in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
out = []
for i in sys.argv[1:]:
    x = r.get(i)
    out.append('%s | %s\n   %s\n' % (i, x['year'] if x else '-', x['quote_verbatim'] if x else 'MISSING'))
sys.stdout.buffer.write('\n'.join(out).encode('utf-8'))
