# Dispatcher check (overnight cycle 2026-10-26): every quoted fragment adjacent to a v5 ledger id is in that row.
import csv, re, sys
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        rows[r[list(r.keys())[0]]] = r
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
qcol = [k for k in next(iter(rows.values())).keys() if 'quote' in k.lower()][0]
text = open(sys.argv[1], encoding='utf-8').read()
paras = re.split(r'\n\s*\n', text)
checked = miss = 0
for p in paras:
    ids = list(re.finditer(r'\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*', p))
    if not ids: continue
    quotes = list(re.finditer(r'[“"]([^“”"]{6,}?)[”"]', p))
    for q in quotes:
        # nearest id after the quote, else before
        after = [m for m in ids if m.start() >= q.end()]
        m = after[0] if after else ids[-1]
        if after and m.start() - q.end() > 120:
            before = [x for x in ids if x.end() <= q.start()]
            if before and q.start() - before[-1].end() < m.start() - q.end(): m = before[-1]
        row = norm(rows.get(m.group(1), {}).get(qcol, ''))
        frags = [norm(x).strip(' .,;:') for x in re.split(r'\[\.\.\.\]|\.\.\.', q.group(1))]
        ok = all(fr in row for fr in frags if len(fr) > 3)
        checked += 1
        if not ok:
            miss += 1
            print('CHECK', m.group(1), '|', q.group(1)[:150])
print('pairs checked', checked, 'unmatched', miss)
