"""Run check: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment in the same sentence-clause as an id
is in that row (fragments of 12+ characters, matched exactly after collapsing whitespace). Usage: python check_quotes.py RUNFILE"""
import csv, re, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'principle_ledger_v5.csv')
rows = {r['id']: re.sub(r'\s+', ' ', r['quote_verbatim']) for r in csv.DictReader(open(p, encoding='utf-8-sig'))}
t = open(sys.argv[1], encoding='utf-8').read()
flat = re.sub(r'\s+', ' ', t)
eids = re.findall(r'\[E\d-\d+\]', t)
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', t))
missing = sorted(i for i in ids if i not in rows)
print('E-ids:', eids or 'none'); print('ids:', len(ids), 'missing:', missing or 'none')
problems = 0
# for each id occurrence, take the quoted fragments between the previous id (or 400 chars back) and it
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    i = m.group(1); start = max(0, m.start() - 400)
    prev = list(re.finditer(r'\*\*\[[MLR]\d{4}-\d{3}\]\*\*', flat[start:m.start()]))
    if prev: start = start + prev[-1].end()
    seg = flat[start:m.start()]
    near = re.search(r'"([^"]{8,})"[^"]{0,12}$', seg)  # the fragment that stands directly before the id
    for q in ([near.group(1)] if near else []):
        parts = [x.strip(' .,;') for x in q.split('[...]')]
        for part in parts:
            if len(part) >= 8 and part not in rows.get(i, ''):
                problems += 1; print(f'NOT IN ROW {i}: "{part}"')
print('fragment problems:', problems)
