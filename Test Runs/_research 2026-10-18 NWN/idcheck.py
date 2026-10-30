import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8'))}
probs = 0
if re.search(r'\[E\d', run): print('E-id found'); probs += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING', i); probs += 1
def norm(s): return re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
nq = 0
for m in re.finditer(r'"([^"]{6,600}?)"((?:[^"\n]{0,40}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*)', run.replace('\n', ' ')):
    q, i = m.group(1), m.group(3)
    if i not in rows: continue
    nq += 1
    src = norm(rows[i])
    for frag in q.split('[...]'):
        f = norm(frag).strip(' .,')
        if f and f not in src:
            print('NOT IN ROW', i, '|', frag[:90]); probs += 1
print(f'{len(set(ids))} ids, {nq} quotes checked, {probs} problems')
