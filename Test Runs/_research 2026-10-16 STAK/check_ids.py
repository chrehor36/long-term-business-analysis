# Check: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment beside an id is in that row.
import csv, re, sys, unicodedata
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
# quoted fragments immediately before an id: "...." **[ID]**  (allowing up to 3 ids chained)
for m in re.finditer(r'"([^"]{6,400})"\s*(?:\*\*\[([MLR]\d{4}-\d{3})\]\*\*)', run.replace('“', '"').replace('”', '"')):
    frag, i = m.group(1), m.group(2)
    parts = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip()]
    for p in parts:
        if norm(p) not in norm(rows.get(i, '')):
            print('FRAGMENT NOT IN ROW', i, '|', p[:90]); bad += 1
print('ids cited:', len(set(ids)), '| problems:', bad)
sys.exit(1 if bad else 0)
