import csv, re, sys
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(sys.argv[1], encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('�', '')).strip()
bad = 0
if re.search(r'\[E\d', text): print('E-id found'); bad += 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text))
for i in sorted(ids):
    if i not in rows: print('MISSING id', i); bad += 1
flat = re.sub(r'\n\s*', ' ', text)
pat = re.compile(r'"([^"]{3,}?)"[^"\[]{0,15}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
n = 0
for m in pat.finditer(flat):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    n += 1
    row = norm(rows[i])
    for piece in frag.split('[...]'):
        p = norm(piece).strip(' .,;')
        # inner quotes in the row are rendered as plain double quotes in the run file
        if p and p not in row and p.replace('"', '') not in row.replace('"', ''):
            print(f'NOT IN ROW {i}: "{p[:90]}"'); bad += 1
print(f'ids: {len(ids)}; quoted fragments checked: {n}; problems: {bad}')
