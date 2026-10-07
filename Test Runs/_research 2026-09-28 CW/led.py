import sys; sys.stdout.reconfigure(encoding='utf-8')
import csv, sys
rows = {r['id'] if 'id' in r else list(r.values())[0]: r for r in csv.DictReader(open('../../principle_ledger.csv', encoding='utf-8'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print('=====', i, 'MISSING' if r is None else '')
    if r: print({k: (v[:700] if isinstance(v, str) else v) for k, v in r.items()})
