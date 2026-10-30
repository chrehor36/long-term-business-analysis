# Dispatcher check (overnight 2026-10-13): every quoted fragment beside a v5 id is in that row's quote.
import csv, re, sys, unicodedata
run = sys.argv[1]
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        rows[r[list(r.keys())[0]]] = ' '.join(r.values())
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
txt = open(run, encoding='utf-8').read()
bad = ids = 0
for para in re.split(r'\n\s*\n', txt):
    found = re.findall(r'\b([MLR]\d{4}-\d{3}[a-z]?)\b', para)
    if not found: continue
    for i in found:
        ids += 1
        if i not in rows: print('PHANTOM', i); bad += 1
    quotes = re.findall(r'"([^"]{12,})"|\u201c([^\u201d]{12,})\u201d', para)
    for q in quotes:
        q = q[0] or q[1]
        parts = [p for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q) if len(p.strip()) > 6]
        for p in parts:
            if not any(norm(p) in norm(rows.get(i, '')) for i in found):
                print('NOT IN ROW', found, '|', p.strip()[:120]); bad += 1
print('ids', ids, 'problems', bad)
