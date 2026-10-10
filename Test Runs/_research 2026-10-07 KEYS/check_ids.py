# Checks the KEYS run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment that sits
# immediately before an id (same sentence group) is found in that id's row. Apostrophes and quote marks normalized.
import csv, re, sys
RUN = 'Test Runs/2026-10-07 Run - KEYS Keysight.md'
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', '')
    return re.sub(r'\s+', ' ', s).strip()
t = open(RUN, encoding='utf-8').read()
flat = re.sub(r'\s+', ' ', t)
bad = 0
if re.search(r'\[E\d', t): print('E-id found'); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
# fragment immediately before an id: "..." then optional punctuation/space then **[ID]**
for m in re.finditer(r'"([^"]{8,}?)"[^"\[]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*', norm(frag)) if p]
    row = norm(rows.get(i, ''))
    for p in parts:
        if p.rstrip('.,;:') not in row:
            print('NOT IN ROW', i, '|', p[:120]); bad += 1
print('ids', len(set(ids)), 'FAIL' if bad else 'PASS')
sys.exit(1 if bad else 0)
