# Dispatcher's check (overnight 2026-10-13, ANIOY): every M/L/R id exists; every quoted fragment within 60 chars before an id is in that row.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
rows = {}
for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig')):
    rows[r['id']] = r['quote_verbatim']
txt = open(sys.argv[1], encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = re.sub(r'[^\w\s\']', ' ', s)
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', txt))
for i in sorted(ids):
    if i not in rows: print('MISSING', i); bad += 1
if re.search(r'\[E\d-\d+\]', txt): print('E-id present'); bad += 1
n = 0
for m in re.finditer(r'[\"\u201c]([^\"\u201c\u201d]{6,}?)[\"\u201d]((?:[^\"\u201c\u201d\n]{0,60}?)(?:\*\*)?\[([MLR]\d{4}-\d{3})\])', txt):
    q, i = m.group(1), m.group(3)
    if i not in rows: continue
    n += 1
    src = norm(rows[i])
    for part in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', q):
        p = norm(part)
        if p and p not in src:
            print('SLIP', i, '::', part[:140]); bad += 1
print('ids', len(ids), 'fragments', n, 'problems', bad)
