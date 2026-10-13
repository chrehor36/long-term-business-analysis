"""Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits in the
same sentence-segment just before an id is found in that row (quotes normalised; [...] splits a fragment)."""
import csv, re, sys
RUN = sys.argv[1]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
for m in re.finditer(r'\[E\d', text):
    print('E-id found at', m.start()); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# fragment check: split text into segments ending at each id
pos = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    seg = text[pos:m.start()]
    pos = m.end()
    seg = seg.split('\n\n')[-1]           # same paragraph only
    seg = re.split(r'(?<=[.;:])\s', seg)[-1] if False else seg
    rid = m.group(1)
    if rid not in rows: continue
    row = norm(rows[rid])
    frags = re.findall(r'[“"]([^"“”]{6,}?)[”"]', seg)
    for f in frags[-2:]:
        for piece in norm(f).split('[...]'):
            piece = piece.strip(' .,')
            if len(piece) >= 6 and piece not in row:
                print(f'CHECK {rid}: "{piece[:90]}"')
print('ids:', len(set(ids)), 'bad:', bad)
