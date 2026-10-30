# Dispatcher's check at the fold (overnight 2026-10-13): every quoted fragment within 40 chars before an id is in a nearby id's row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u201c','"').replace('\u201d','"')).strip().lower()
bad = checked = 0
print('E-ids:', re.findall(r'\[E\d+-\d+\]', run))
for i in sorted(set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', run))):
    if i not in rows: print('MISSING', i); bad += 1
for m in re.finditer(r'"([^"\n]{4,}?)"([^"\n]{0,40}?)((?:\*{0,2}\[[MLR]\d{4}-\d{3}\]\*{0,2}[\s,;and]*)+)', run):
    ids = re.findall(r'[MLR]\d{4}-\d{3}', m.group(3))
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*|\s*\.\.\.\s*', m.group(1)) if p.strip()]
    checked += 1
    if not any(all(norm(p) in norm(rows.get(i, '')) for p in parts) for i in ids):
        bad += 1; print('NOT IN ROW', ids, '::', m.group(1)[:150])
print('checked', checked, 'problems', bad)
