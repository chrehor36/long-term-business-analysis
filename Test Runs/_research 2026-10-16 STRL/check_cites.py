# Citation check for the STRL run: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment beside an id is in that row.
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragments: a "..." immediately followed (within 12 chars) by **[id]** or [id]
for m in re.finditer(r'"([^"]{6,}?)"[^"\n]{0,14}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run.replace('\n', ' ')):
    frag, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ''))
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*', frag) if p.strip()]
    for p in parts:
        if norm(p) not in row:
            print(f'NOT IN ROW {i}: "{p}"'); bad += 1
print('ids cited:', len(set(ids)), '| problems:', bad)
sys.exit(1 if bad else 0)
