# Dispatcher's citation check (overnight 2026-10-17, AMTM): every quoted fragment beside a v5 id is in that row.
import csv, re, sys, unicodedata
run = open(sys.argv[1], encoding='utf-8').read()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    r = csv.reader(f); hdr = next(r)
    for row in r: rows[row[0]] = ' '.join(row)
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).lower()
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', run))
print('ids', len(ids), 'missing', sorted(i for i in ids if i not in rows))
print('E-ids', re.findall(r'\bE\d-\d+\b', run))
bad = 0; n = 0
for m in re.finditer(r'\*\*\[?([MLR]\d{4}-\d{3})', run):
    i = m.group(1); seg = run[max(0, m.start()-400):m.start()]
    qs = re.findall(r'"([^"]{6,})"', seg.split('**')[-1] if seg.count('**') else seg)
    qs = re.findall(r'"([^"]{6,})"', seg)[-1:] if not qs else qs[-1:]
    for q in qs:
        n += 1
        parts = [p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q) if len(p.strip(' .,;:')) > 3]
        if i in rows and not all(norm(p) in norm(rows[i]) for p in parts):
            bad += 1; print('SLIP?', i, '|', q[:140])
print('fragments checked', n, 'flags', bad)
