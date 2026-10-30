"""Dispatcher's citation check (overnight 2026-10-16, TRN): every quoted fragment directly before a bolded id run is in one of those rows."""
import csv, io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
text = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
n = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')).strip().lower()
flat = re.sub(r'\s+', ' ', text)
pat = re.compile(r'[\"\u201c]([^\"\u201c\u201d]{3,800}?)[\"\u201d]([^\"\u201c\u201d]{0,80}?)((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*[\s,;and]*)+)')
ok = bad = 0
for m in pat.finditer(flat):
    ids = re.findall(r'[MLR]\d{4}-\d{3}', m.group(3))
    if '**[' in m.group(2): continue
    frags = [f for f in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', m.group(1)) if len(f.strip()) > 2]
    hit = all(any(n(f) in n(rows.get(i, '')) for i in ids) for f in frags)
    if hit: ok += 1
    else:
        bad += 1; print('SLIP?', ids, '|', m.group(1)[:160])
eids = re.findall(r'\[E\d+-\d+\]', text); miss = sorted({i for i in re.findall(r'\[([MLR]\d{4}-\d{3})\]', text) if i not in rows})
print('checked', ok+bad, 'ok', ok, 'flagged', bad, 'E-ids', len(eids), 'missing', miss)
