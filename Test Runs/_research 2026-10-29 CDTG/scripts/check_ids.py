# Checks for the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# that sits in the same sentence-chunk as an id (before it, up to the previous id or paragraph start) is in that row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
bad = 0
if re.search(r'\[E\d', run): print('E-id found'); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
# fragment check: a quote immediately followed by an id in bold
norm = lambda t: re.sub(r'\s+', ' ', t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"'))
for m in re.finditer(r'"([^"\n]{6,400}(?:\n[^"\n]{0,400}){0,4})"[^"\[\n]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    q = norm(rows.get(i, ''))
    parts = [norm(p).strip(' .,;') for p in frag.split('[...]')]
    for p in parts:
        if p and p not in q:
            print('FRAGMENT NOT IN ROW', i, '::', p[:90]); bad += 1
print('ids:', len(set(ids)), 'distinct;', 'problems:', bad)
sys.exit(1 if bad else 0)
