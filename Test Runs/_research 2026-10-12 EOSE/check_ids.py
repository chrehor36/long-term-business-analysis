import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
run = open('../2026-10-12 Run - EOSE Eos Energy Enterprises.md', encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv', encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', '')).strip()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragment immediately before an id: "...." **[ID]**  (allow a closing punctuation between)
pat = re.compile(r'"([^"\n]{3,})"[^"\n]{0,3}\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
nfrag = 0
for q, i in pat.findall(run.replace('“', '"').replace('”', '"')):
    nfrag += 1
    src = norm(rows.get(i, ''))
    for part in norm(q).split('[...]'):
        part = part.strip(' .,;')
        if part and part not in src:
            print(f'FRAGMENT NOT IN ROW {i}: {part!r}'); bad += 1
print(f'ids cited: {len(set(ids))} distinct; fragments checked: {nfrag}; problems: {bad}')
