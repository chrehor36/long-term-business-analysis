# Dispatcher's check at the fold: every quoted fragment immediately followed by a v5 id is in that row's quote.
import csv, re, sys
rows = {r['id']: r for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
txt = open(sys.argv[1], encoding='utf-8').read()
n = bad = 0
for m in re.finditer(r'["\u201c]([^"\u201d]{4,600}?)["\u201d][\s,.;:)]{0,4}\*\*\[((?:[MLR]\d{4}-\d{3}(?:,\s*)?)+)\]\*\*', txt):
    frag, ids = m.group(1), re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*|\s*\.\.\.\s*|\s*\[[^\]]{1,20}\]\s*', frag) if len(p.strip()) > 2]
    n += 1
    if not any(i in rows and all(norm(p) in norm(rows[i]['quote_verbatim']) for p in parts) for i in ids):
        bad += 1; print('SLIP?', ids, '|', frag[:160].replace('\n', ' '))
missing = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', txt)) - set(rows)
print('fragments checked', n, 'unmatched', bad, 'ids', len(set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', txt))), 'missing', missing, 'E-ids', re.findall(r'\bE\d-\d+\b', txt))
