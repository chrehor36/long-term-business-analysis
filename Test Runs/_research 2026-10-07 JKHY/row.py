"""Print v5 ledger rows by id. Usage: row.py ID [ID...]"""
import csv, sys, os
sys.stdout.reconfigure(encoding="utf-8")
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'principle_ledger_v5.csv')
rows = {r['﻿id'] if '﻿id' in r else r['id']: r for r in csv.DictReader(open(p, encoding='utf-8'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(f"== {i}: " + (r['quote_verbatim'] if r else 'MISSING'))
