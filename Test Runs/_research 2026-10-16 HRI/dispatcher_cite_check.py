# dispatcher's citation check: every quoted fragment adjacent to a v5 id must be in that row's quote
import csv, re, sys
run = open(sys.argv[1], encoding='utf8').read()
rows = {}
with open('principle_ledger_v5.csv', encoding='utf8') as f:
    r = csv.reader(f); hdr = next(r)
    for row in r: rows[row[0]] = ' '.join(row)
norm = lambda s: re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u201c','"').replace('\u201d','"')).lower()
ids = set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', run)); bad = [i for i in ids if i not in rows]
print('ids', len(ids), 'missing', bad, 'E-ids', re.findall(r'\bE\d-\d+\b', run))
n = slips = 0
for m in re.finditer(r'["\u201c]([^"\u201d]{8,400})["\u201d][^"\u201c\n]{0,40}?\*\*\[?([MLR]\d{4}-\d{3})', run):
    n += 1
    for frag in norm(m.group(1)).split('[...]'):
        frag = frag.strip(' .,;:')
        if frag and frag not in norm(rows.get(m.group(2), '')):
            slips += 1; print('SLIP', m.group(2), frag[:100])
print('fragments', n, 'slips', slips)
