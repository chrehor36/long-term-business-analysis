import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r[0]: r[2] for r in csv.reader(open(sys.argv[2], encoding='utf-8'))}
bad = 0
if re.search(r'\[E\d', run): print('E-id found'); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); bad += 1
# every quoted fragment immediately before an id must be in that row
for m in re.finditer(r'"([^"]{8,}?)"[^"\[]{0,40}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2)
    norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('“', '"').replace('”', '"'))
    parts = [p.strip() for p in norm(frag).split('[...]') if p.strip()]
    if i in rows and not all(p in norm(rows[i]) for p in parts):
        print('FRAGMENT NOT IN ROW', i, '|', frag[:90]); bad += 1
print('ids', len(set(ids)), 'problems', bad)
