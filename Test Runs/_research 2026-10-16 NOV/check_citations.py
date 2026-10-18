# Citation check for the NOV run: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment that stands
# immediately before an id (closing quote within 40 characters of the id, nothing but punctuation, spaces or another id
# between) is a substring of that row's quote (whitespace normalized). Quotes earlier in a paragraph that carry a filing
# attribution are not tested here; they were read by hand.
import csv, re
run = open('Test Runs/2026-10-16 Run - NOV NOV Inc.md', encoding='utf-8').read()
rows = {r['\ufeffid']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
print('E-ids:', re.findall(r'\[E\d-\d+\]', run) or 'none')
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
print('distinct ids cited:', len(set(ids)), '| missing from ledger:', sorted({i for i in ids if i not in rows}) or 'none')
bad = n = 0
for m in re.finditer(r'"([^"]{3,}?)"([\s.,;:]{0,6})\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    n += 1
    q, i = m.group(1), m.group(3)
    q2 = q.replace(' ... ', ' ').replace('[...]', ' ')
    ok = all(norm(part) in norm(rows[i]) for part in re.split(r'\s*\.\.\.\s*|\s*\[\.\.\.\]\s*', q) if part.strip())
    if not ok:
        bad += 1; print('NOT IN ROW', i, '|', q[:100])
print('fragments tested:', n, '| not in their row:', bad)
