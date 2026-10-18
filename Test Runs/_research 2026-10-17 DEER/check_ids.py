# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# immediately before an id (within the same sentence run) is found in that row. Usage: python -I check_ids.py RUNFILE LEDGER
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
t = open(run, encoding='utf-8').read()
rows = {}
for r in csv.DictReader(open(ledger, encoding='utf-8')):
    rows[r['﻿id'] if '﻿id' in r else r['id']] = r['quote_verbatim']
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-').replace('�', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
problems = 0
nfrag = 0
eids = re.findall(r'\[E\d-\d+\]', t)
if eids: print('E-ids found:', eids); problems += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); problems += 1
# fragments: quoted text in the 400 characters before each id occurrence, back to the previous id
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    i = m.group(1)
    start = max(0, m.start() - 600)
    prev = [x.end() for x in re.finditer(r'\*\*\[[MLR]\d{4}-\d{3}\]\*\*', t[start:m.start()])]
    seg = t[start + (prev[-1] if prev else 0): m.start()]
    seg = seg.replace('\n', ' ')
    qs = [(mm.group(1), len(seg) - mm.end()) for mm in re.finditer(r'["“]([^"“”]{6,}?)["”]', seg)]
    for q, gap in qs:
        if gap > 40: continue   # only the quotation that stands beside the id
        if i not in rows: continue
        row = norm(rows[i]); nfrag += 1
        for part in q.split('[...]'):
            p = norm(part).strip(' .,;:')
            if p and p not in row:
                print(f'FRAGMENT not in {i}: "{part.strip()[:90]}"'); problems += 1
print('ids checked:', len(set(ids)), 'fragments checked:', nfrag, 'problems:', problems)
