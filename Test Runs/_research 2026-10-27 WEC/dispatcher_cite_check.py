# Dispatcher check, tight adjacency: a quote ending within 15 characters before an id, or starting within 15 after it.
import csv, re, sys
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(sys.argv[1], encoding='utf-8').read()
ids = list(re.finditer(r'\*\*\[?([MLR]\d{4}-\d{3})\]?\*\*', text))
quotes = list(re.finditer(r'[“"]([^“”"]{4,}?)[”"]', text, re.S))
checked = miss = 0
for m in ids:
    near = [q for q in quotes if 0 <= m.start() - q.end() <= 15 or 0 <= q.start() - m.end() <= 15]
    for q in near:
        frags = [norm(x).strip(' .,;:') for x in re.split(r'\[\.\.\.\]|\.\.\.|\[…\]|…', q.group(1))]
        ok = all(fr in norm(rows.get(m.group(1), '')) for fr in frags if len(fr) > 3)
        checked += 1
        if not ok:
            miss += 1; print('MISS', m.group(1), '|', re.sub(r'\s+',' ',q.group(1))[:160])
print('adjacent pairs', checked, 'unmatched', miss, 'ids', len(ids), 'missing ids', [m.group(1) for m in ids if m.group(1) not in rows])
