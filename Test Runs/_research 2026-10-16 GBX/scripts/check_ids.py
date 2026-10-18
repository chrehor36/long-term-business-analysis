# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
# immediately before an id (the pattern "..." **[ID]**) is found in that row (elisions [...] split the fragment).
import csv, re, sys, unicodedata
BASE = r'C:\Users\chreh\OneDrive\Documents\BRK'
rows = {r[0]: r[2] for r in csv.reader(open(BASE + r'\principle_ledger_v5.csv', encoding='utf-8'))}
run = open(BASE + r'\Test Runs\2026-10-16 Run - GBX Greenbrier.md', encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-').replace('\ufffd', '?')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
allids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
missing = sorted(set(i for i in allids if i not in rows))
if missing: print('MISSING ids:', missing); bad += 1
print('ids cited:', len(set(allids)))
flat = re.sub(r'\s+', ' ', run)
# quote immediately followed by an id (optionally after a comma/space)
for m in re.finditer(r'"([^"]{3,400})"\s*,?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    q, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ''))
    parts = [p.strip(' .,') for p in norm(q).split('[...]')]
    ok = all(p in row for p in parts if p)
    if not ok:
        bad += 1; print('NOT IN ROW', i, '::', q[:120])
print('quote-id pairs checked:', len(re.findall(r'"([^"]{3,400})"\s*,?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat)))
print('RESULT:', 'PASS' if not bad else 'FAIL')
