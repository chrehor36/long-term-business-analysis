# Dispatcher's check, narrowed: a quote whose closing mark is followed within 40 characters by a bold v5 id.
import csv, re, sys, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8') as f:
    r = csv.reader(f); hdr = next(r)
    qi = [i for i, h in enumerate(hdr) if 'quote' in h.lower()][0]
    for row in r: rows[row[0]] = norm(row[qi])
text = open(sys.argv[1], encoding='utf-8').read().replace('\u201c', '"').replace('\u201d', '"')
n = bad = 0
for m in re.finditer(r'"([^"]{6,600})"([^"]{0,40}?)\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    q, rid = m.group(1), m.group(3)
    parts = [norm(p).strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q)]
    parts = [p for p in parts if len(p) >= 5]
    n += 1
    if not all(p in rows[rid] for p in parts):
        bad += 1; print('SLIP', rid, '|', ' '.join(q.split())[:160], '| row:', rows[rid][:160])
print('quote-beside-id pairs', n, 'slips', bad)
