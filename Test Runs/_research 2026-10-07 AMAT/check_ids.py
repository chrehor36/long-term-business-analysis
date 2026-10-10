# Check for the AMAT run file: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv; (3) the quoted
# fragment immediately before each id (inside the same paragraph) is in that row's quote_verbatim, [...] splitting it.
import csv, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RUN = os.path.join(ROOT, 'Test Runs', '2026-10-07 Run - AMAT Applied Materials.md')
rows = {r[0].lstrip('﻿'): r[2] for r in csv.reader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8'))}
text = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    return re.sub(r'\s+', ' ', s).strip()
fail = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids: print('E-ids found:', eids); fail += 1
ids = list(re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text))
paras = [(m.start(), m.end()) for m in re.finditer(r'(?s).+?(?:\n\s*\n|\Z)', text)]
noquote = []
for k, m in enumerate(ids):
    i = m.group(1)
    if i not in rows: print('MISSING id', i); fail += 1; continue
    pstart = max(s for s, e in paras if s <= m.start())
    prev_end = ids[k-1].end() if k and ids[k-1].end() > pstart else pstart
    seg = text[prev_end:m.start()]
    quotes = re.findall(r'"([^"]+)"', seg)
    if not quotes:
        noquote.append(i); continue
    q = quotes[-1]
    row = norm(rows[i])
    for frag in re.split(r'\s*\[\.\.\.\]\s*', q):
        f = norm(frag).rstrip('.,;:')
        if f and f not in row:
            print(f'FRAGMENT NOT IN ROW {i}: "{f[:90]}"'); fail += 1
print(f'{len(ids)} id citations, {len(set(m.group(1) for m in ids))} distinct; without an adjacent quote: {noquote}')
print('PASS' if fail == 0 and not noquote else 'FAIL')
sys.exit(1 if fail or noquote else 0)
