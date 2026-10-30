# Citation check for the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment standing between the previous id and an id is found in that id's row
# (fragments split on [...]; curly and straight quotes and whitespace normalised).
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
run = open("Test Runs/2026-10-12 Run - MTSUY Mitsubishi Corporation.md", encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-ids found:', eids); bad += 1
ids = list(re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', run))
prev = 0
for m in ids:
    i = m.group(1)
    if i not in rows: print('MISSING', i); bad += 1; prev = m.end(); continue
    seg = run[prev:m.start()]
    # only the text since the last paragraph break or id
    seg = re.split(r'\n\n|\n- |\n  - ', seg)[-1]   # a paragraph or a list item is the unit
    qs = re.findall(r'["“]([^"”]{6,}?)["”]', seg)
    for k, q in enumerate(qs):
        last = (k == len(qs) - 1)
        for frag in re.split(r'\s*\[\.\.\.\]\s*', q):
            f = norm(frag).strip(' ,.;:')
            if len(f) < 6: continue
            if f not in norm(rows[i]):
                if last: print(f'NOT IN {i} (quote next to the id): "{f}"'); bad += 1
                else: print(f'review {i} (earlier quote in segment, attributed elsewhere?): "{f}"')
    prev = m.end()
print(f'{len(ids)} id citations, {len(set(x.group(1) for x in ids))} distinct; problems: {bad}')
