# Check: no E-ids; every M/L/R id in the run file is in principle_ledger_v5.csv; every quoted fragment
# in the same sentence span just before an id is found in that id's row (normalised for whitespace only).
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
bad = 0
if re.search(r'\[E\d-\d+\]', run): print('E-id found'); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
norm = lambda t: re.sub(r'\s+', ' ', t).strip()
# fragment: a "..." quotation immediately followed (within 3 chars) by a bold id, or a group of ids
checked = 0
for m in re.finditer(r'"([^"]{3,})"\s*((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[,\s]*)+)', run):
    frag = m.group(1); cited = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [norm(p) for p in frag.split('[...]') if norm(p)]
    ok = any(all(p in norm(rows.get(c, '')) for p in parts) for c in cited)
    checked += 1
    if not ok: print('FRAGMENT NOT IN ROW', cited, '|', frag[:120]); bad += 1
print('ids', len(set(ids)), 'fragments checked', checked, 'problems', bad)
