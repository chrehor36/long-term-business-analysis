# Dispatcher check (overnight cycle 2026-10-11): every quoted fragment immediately before a bold v5 id is in that row.
import csv, re, sys
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows[r['id']] = ' '.join(r['quote_verbatim'].split()).replace('\u2019', "'").replace('\u201c','"').replace('\u201d','"')
txt = open(sys.argv[1], encoding='utf-8').read()
txt = ' '.join(txt.split()).replace('\u2019', "'")
n = bad = 0
for m in re.finditer(r'\*\*\[([MLR][0-9]{4}-[0-9]{3}[a-z]?)(?:[,;] ?[MLR][0-9-]+)*\]\*\*', txt):
    ids = re.findall(r'[MLR][0-9]{4}-[0-9]{3}[a-z]?', m.group(0))
    pre = txt[max(0, m.start()-400):m.start()]
    pre = pre.split('**[')[-1] if '**[' in pre else pre
    frags = re.findall(r'["\u201c]([^"\u201c\u201d]{6,})["\u201d]', pre)
    for fr in frags[-2:]:
        n += 1
        parts = [p.strip(' .,;:') for p in re.split(r'\[\.\.\.\]|\.\.\.|\u2026', fr.replace('\u201c','"').replace('\u201d','"')) if p.strip(' .,;:')]
        hit = any(all(p in rows.get(i, '') for p in parts) for i in ids)
        if not hit:
            bad += 1; print('NOT IN ROW', ids, '|', fr[:160])
print('fragments', n, 'not in row', bad)
