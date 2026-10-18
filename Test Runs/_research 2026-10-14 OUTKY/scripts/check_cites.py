# Citation check for the run file: no E-ids; every M/L/R id in the v5 ledger; every quoted fragment
# that sits immediately before an id (same sentence) is found in one of the ids that follow it.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# fragments: "..." followed (within 40 chars, no other quote) by one or more bold ids
flat = re.sub(r'\s+', ' ', run)
n = 0
for m in re.finditer(r'"([^"]{6,400})"((?:[^"\[]{0,40}?\*\*\[[MLR]\d{4}-\d{3}\]\*\*,?)+)', flat):
    frag, tail = m.group(1), m.group(2)
    cited = re.findall(r'([MLR]\d{4}-\d{3})', tail)
    parts = [p.strip() for p in norm(frag).split('[...]') if p.strip()]
    ok = all(any(norm(p) in norm(rows.get(c, '')) for c in cited) for p in parts)
    n += 1
    if not ok: print('FRAGMENT NOT IN ROW', cited, '|', frag[:120]); bad += 1
print(f'ids: {len(set(ids))} distinct; fragments checked: {n}; problems: {bad}')
