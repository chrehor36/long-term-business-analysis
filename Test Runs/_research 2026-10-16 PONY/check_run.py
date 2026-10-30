# Checks the run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment directly before an id is in that row.
import csv, re, sys
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
def norm(s):
    for a, b in (('“', '"'), ('”', '"'), ('‘', "'"), ('’', "'"), (' ', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
missing = sorted({i for i in ids if i not in rows})
if missing: print('MISSING ids:', missing); bad += 1
# fragment check: for each id occurrence, take text since the previous id occurrence; the last straight-quoted span ("...") in it
flat = norm(t)
pos = 0; checked = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    seg = flat[pos:m.start()]; pos = m.end()
    q = re.findall(r'"([^"]{6,}?)"(?=[^"]*$)', seg)
    if not q: continue
    tail = seg[seg.rfind('"')+1:]
    if len(tail) > 60: continue   # the quote is not beside the id
    frag = q[-1].strip().rstrip('.,;:')
    rid = m.group(1)
    if rid not in rows: continue
    checked += 1
    parts = [p.strip(' .,;') for p in frag.split('[...]')]
    row = norm(rows[rid])
    if not all(p in row for p in parts if p):
        print(f'FRAGMENT NOT IN ROW {rid}: "{frag[:120]}"'); bad += 1
print(f'ids cited: {len(ids)} ({len(set(ids))} distinct); fragments checked: {checked}; problems: {bad}')
sys.exit(1 if bad else 0)
