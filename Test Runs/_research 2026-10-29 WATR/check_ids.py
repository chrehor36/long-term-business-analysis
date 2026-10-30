# Checks: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment immediately before an id is in that row.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8'))}
bad = 0
if re.search(r'\[E\d-\d+\]', run):
    print('E-id found'); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING', i); bad += 1
def norm(s):
    s = s.replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
pat = r'"([^"]{8,})"\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*'
n = 0
for m in re.finditer(pat, run):
    n += 1
    frag, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ''))
    for p in frag.split('[...]'):
        if norm(p) not in row:
            print('NOT IN ROW', i, '|', p.strip()[:100]); bad += 1
print('distinct ids', len(set(ids)), '| quotes checked', n, '| problems', bad)
