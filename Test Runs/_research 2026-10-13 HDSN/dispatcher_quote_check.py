# Dispatcher check (overnight 2026-10-13): each quoted fragment that closes just before a bold v5 id is in that row.
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r[0]: ' '.join(r[1:3]) for r in csv.reader(open('principle_ledger_v5.csv', encoding='utf-8'))}
def norm(s):
    s = s.replace('\ufffd', "'").replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
print('E-ids:', re.findall(r'\[E\d-\d+\]', run))
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)); print('ids', len(ids), 'missing', sorted(i for i in ids if i not in rows))
checked = slips = 0
for m in re.finditer(r'"([^"\n]{4,}(?:\n[^"\n]*){0,4})"[\s.,;:)]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run):
    frag, i = m.group(1), m.group(2); checked += 1
    for part in re.split(r'\[\.\.\.\]|\.\.\.', frag):
        p = norm(part).strip(' .,;:')
        if p and p not in norm(rows.get(i, '')):
            slips += 1; print('SLIP', i, '|', part.strip()[:140])
print('checked', checked, 'slips', slips)
