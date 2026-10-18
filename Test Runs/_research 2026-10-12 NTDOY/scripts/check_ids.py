# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# in the same sentence-chunk just before an id is found in that id's row (quotes and apostrophes normalised).
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', re.sub(r"[‘’“”'\"�`]", "'", s)).strip().lower()
text = open(run, encoding='utf-8').read()
bad = 0
for e in re.findall(r'\[E\d-\d+\]', text):
    print('E-id found', e); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# fragment check: for each "quote" immediately followed (within 12 chars) by **[ID]
for m in re.finditer(r'"([^"]{6,400})"[^"\[]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]', text):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    parts = [p.strip(' .,;') for p in frag.split('[...]') if p.strip(' .,;')]
    for p in parts:
        if norm(p) not in norm(rows[i]):
            print('FRAGMENT NOT IN ROW', i, '|', p[:120]); bad += 1
print('ids', len(set(ids)), 'problems', bad)
