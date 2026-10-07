# Citation check for the MBC run of 2026-10-05: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment standing just before a bold id is found verbatim (whitespace-normalised) in that id's row.
# Run from the repository root.
import csv, re, sys
run = open('Test Runs/2026-10-05 Run - MBC MasterBrand.md', encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
bad = 0
if re.search(r'\[E\d+-\d+\]', run):
    print('E-id found'); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING', i); bad += 1
def norm(x):
    return re.sub(r'\s+', ' ', x)
pat = re.compile(r'"([^"]{6,400})"[^"\[]{0,14}\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
n = 0
for m in pat.finditer(run):
    n += 1
    frag, i = m.group(1), m.group(2)
    for p in [q.strip() for q in frag.split('[...]') if q.strip()]:
        if norm(p) not in norm(rows.get(i, '')):
            print('NOT IN ROW', i, '|', p); bad += 1
print('ids', len(set(ids)), 'fragments', n, 'problems', bad)
sys.exit(1 if bad else 0)
