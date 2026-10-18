"""Check a run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment immediately before an id
(within the same sentence span) is a substring of that row, after normalising quotes and splitting on [...].
Usage: check_ids.py runfile"""
import csv, re, sys, unicodedata
rows = {}
for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig')):
    rows[r['id']] = r['quote_verbatim']
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(sys.argv[1], encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
print('E-ids:', eids or 'none')
bad += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
missing = sorted({i for i in ids if i not in rows})
print(f'ids cited: {len(ids)} ({len(set(ids))} distinct); missing: {missing or "none"}')
bad += len(missing)
# quoted fragment(s) directly preceding an id: take text between previous id/bullet and this id
flat = ' '.join(text.split())
checked = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    i = m.group(1)
    start = max(flat.rfind('**[', 0, m.start() - 1), flat.rfind('. ', 0, m.start() - 200) if False else -1)
    seg = flat[max(0, m.start() - 400):m.start()]
    # only the closest quotation that ends within 40 chars before the id
    q = list(re.finditer(r'"([^"]{6,})"', seg))
    if not q:
        continue
    last = q[-1]
    if len(seg) - last.end() > 40:
        continue
    frag = last.group(1)
    if i not in rows:
        continue
    row = norm(rows[i])
    parts = [p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.', frag)]
    ok = all(norm(p) in row for p in parts if len(p) > 3)
    checked += 1
    if not ok:
        bad += 1
        print(f'NOT IN ROW {i}: "{frag[:120]}"')
print(f'quoted fragments checked: {checked}')
print('RESULT:', 'PASS' if bad == 0 else f'FAIL ({bad})')
