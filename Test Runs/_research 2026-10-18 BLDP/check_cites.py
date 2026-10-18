# Check the run file's citations: no E-ids; every M/L/R id in principle_ledger_v5.csv;
# every quoted fragment immediately before an id is in that row (quotes normalised, [...] splits).
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
probs = 0
for m in re.finditer(r'\[(E\d+-\d+)\]', t):
    print('E-id found', m.group(1)); probs += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); probs += 1
# quoted fragment(s) between the previous id (or paragraph start) and this id
flat = t.replace('\n', ' ')
prev = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    seg = flat[prev:m.start()]
    prev = m.end()
    # only the last sentence-ish chunk: quotes ending within 40 chars before the id
    qs = list(re.finditer(r'"([^"]{3,})"', seg))
    if not qs: continue
    q = qs[-1]
    if len(seg) - q.end() > 40: continue
    rid = m.group(1)
    row = norm(rows.get(rid, ''))
    for frag in q.group(1).split('[...]'):
        f = norm(frag).strip(' .,;')
        if f and f not in row:
            print(f'NOT IN ROW {rid}: "{f[:120]}"'); probs += 1
print('ids', len(set(ids)), 'problems', probs)
