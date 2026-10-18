# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that stands
# immediately before an id is found in that row (apostrophes and quote marks normalised, [...] elisions split).
import csv, re, os, sys
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, '..', '..', '..'))
RUN = os.path.join(ROOT, 'Test Runs', '2026-10-18 Run - XNGSY ENN Energy Holdings.md')
rows = {}
for r in csv.DictReader(open(os.path.join(ROOT, 'principle_ledger_v5.csv'), encoding='utf-8')):
    rows[r.get('﻿id') or r['id']] = r['quote_verbatim']
t = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
missing = sorted(set(i for i in ids if i not in rows))
if missing: print('MISSING ids:', missing); bad += 1
print(f'{len(ids)} id citations, {len(set(ids))} distinct, missing {len(missing)}')
checked = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    i = m.group(1); pre = t[max(0, m.start() - 600):m.start()]
    q = re.search(r'["“]([^"“”]{3,500})["”][^"“”\[\]]{0,14}$', pre)
    if not q: continue
    frag = q.group(1); checked += 1
    rt = norm(rows.get(i, ''))
    for piece in frag.split('[...]'):
        p = norm(piece).strip(' .,;:')
        if p and p not in rt:
            print(f'NOT IN ROW {i}: "{piece.strip()}"'); bad += 1
print(f'{checked} quoted fragments checked beside ids (strict: the quote ends within 14 characters of the id)')
# wider window, listed for review by hand only (filing quotes followed by prose and then an id are expected here)
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    i = m.group(1); pre = t[max(0, m.start() - 600):m.start()]
    q = re.search(r'["“]([^"“”]{3,500})["”][^"“”\[\]]{15,90}$', pre)
    if q and not all(norm(x).strip(' .,;:') in norm(rows.get(i, '')) for x in q.group(1).split('[...]')):
        print(f'  review (not counted): quote before {i}: "{q.group(1)[:60]}"')
print('RESULT:', 'PASS' if bad == 0 else f'FAIL ({bad})')
