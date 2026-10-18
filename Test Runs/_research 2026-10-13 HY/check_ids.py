# Check: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment on a line with an id is in one of
# that line's rows (quote normalised for curly/straight quotes and whitespace).
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = sys.argv[1]; ledger = sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(run, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
# paragraph-level: split into bullet/paragraph blocks
blocks = re.split(r'\n(?=- |\n|\|)', text)
for b in blocks:
    ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', b)
    for i in ids:
        if i not in rows: print('MISSING id', i); bad += 1
    if not ids: continue
    flat = re.sub(r'\s+', ' ', b)
    # each quote immediately followed (within 12 chars) by an id must be in that id's row
    for m in re.finditer(r'"([^"]{6,})"[^"\[]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]', flat):
        q, i = m.group(1), m.group(2)
        if i in rows and norm(q) not in norm(rows[i]):
            print('FRAGMENT NOT IN ROW', i, '::', q); bad += 1
print('ids checked:', len(set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text))), 'problems:', bad)
