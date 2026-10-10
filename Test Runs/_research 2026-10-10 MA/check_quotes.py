# Check the MA run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# beside an id (in the same bullet/sentence before the id) appears in that row (elisions [...] split the quote).
import csv, re, sys, unicodedata
ROOT = r'C:\Users\chreh\OneDrive\Documents\BRK'
run = open(ROOT + r'\Test Runs\2026-10-10 Run - MA Mastercard.md', encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ROOT + r'\principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
if re.search(r'\[E\d-\d+\]', run): print('E-id found'); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragments immediately preceding an id: "....." **[ID]** or "...." ... **[ID]** within 160 chars
flat = re.sub(r'\s+', ' ', run)
for m in re.finditer(r'"([^"]{6,400})"([^"]{0,160}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    q, gap, i = m.group(1), m.group(2), m.group(3)
    if re.search(r'\((10-K|10-Q|proxy|8-K|COF|DFS|V 10-K|AXP|PYPL)', gap) or ' - **' in gap or '## ' in gap or '| ' in gap: continue
    if i not in rows: continue
    row = norm(rows[i])
    parts = [p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]', q)]
    pos = 0; ok = True
    for p in parts:
        pn = norm(p)
        if not pn: continue
        k = row.find(pn, pos)
        if k < 0: ok = False; break
        pos = k + len(pn)
    if not ok:
        print('NOT IN ROW', i, '::', q[:120]); bad += 1
print('ids checked', len(set(ids)), 'FAIL' if bad else 'PASS')
