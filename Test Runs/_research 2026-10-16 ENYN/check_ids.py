# Check: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment directly before an id is in that row.
# Usage: python -I check_ids.py <run file> <principle_ledger_v5.csv>
import csv, re, sys

run = open(sys.argv[1], encoding='utf-8').read()
led = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
bad = 0
if re.search(r'\[E\d-\d+\]', run):
    print('E-id found'); bad = 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', run))
for i in sorted(ids):
    if i not in led:
        print('MISSING', i); bad = 1


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('’', "'").replace('“', '"').replace('”', '"')).strip()


checked = 0
for m in re.finditer(r'"([^"]{8,}?)"[^"\[]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]', run):
    frag, i = m.group(1), m.group(2)
    for p in [p for p in frag.split('[...]') if p.strip()]:
        checked += 1
        if norm(p) not in norm(led.get(i, '')):
            print('NOT IN ROW', i, '|', p); bad = 1
print('ids:', len(ids), 'fragments checked:', checked, 'RESULT', 'FAIL' if bad else 'PASS')
