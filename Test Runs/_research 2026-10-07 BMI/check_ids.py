"""Check the run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment beside an id is in that row."""
import csv, re, sys, unicodedata
RUN = "Test Runs/2026-10-07 Run - BMI Badger Meter.md"
rows = {r['﻿id'] if '﻿id' in r else r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
t = open(RUN, encoding='utf-8').read()
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
problems = 0
for e in re.findall(r'\[E\d+-\d+\]', t):
    print('E-id found:', e); problems += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); problems += 1
# quoted fragment immediately before an id (allowing a closing parenthesis or punctuation between)
flat = re.sub(r'\s+', ' ', t)
for m in re.finditer(r'"([^"]{6,600})"\s*[.,;:]?\s*(?:\([^)]*\)\s*)?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    q = norm(rows[i])
    parts = [norm(x) for x in re.split(r'\[\.\.\.\]', frag) if norm(x)]
    ok = all(pt.strip(' .,;') in q for pt in parts)
    if not ok:
        print('FRAGMENT NOT IN ROW', i, '|', frag[:120]); problems += 1
print('ids cited:', len(set(ids)), '| problems:', problems)
