# Check: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment beside an id is in that row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {}
for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig')):
    rows[r['id']] = r['quote_verbatim']
norm = lambda t: re.sub(r'\s+', ' ', t.replace('’', "'").replace('“', '"').replace('”', '"')).strip()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragment immediately before an id: "..." **[ID]** (allow one intervening short phrase)
for m in re.finditer(r'"([^"]{6,400})"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*', frag) if p.strip()]
    for p in parts:
        if norm(p) not in norm(rows[i]):
            print('NOT IN ROW', i, '|', p[:90]); bad += 1
print('ids cited:', len(set(ids)), '| problems:', bad)
sys.exit(1 if bad else 0)
