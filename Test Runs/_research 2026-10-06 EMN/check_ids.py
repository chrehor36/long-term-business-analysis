# Checks the EMN run file: no v4 E-ids; no em dashes; every M/L/R id exists in principle_ledger_v5.csv and is in bold;
# every double-quoted fragment that sits between the previous id (or the paragraph start) and an id appears verbatim in
# that id's row (fragments split on [...]; curly quotes normalised; whitespace collapsed).
import csv, re, sys, bisect
RUN = 'Test Runs/2026-10-06 Run - EMN Eastman Chemical.md'
rows = {r['﻿id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8'))}

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip()

txt = open(RUN, encoding='utf-8').read()
bad = 0
e = re.findall(r'\[E\d+-\d+\]', txt)
if e:
    print('V4 E-IDS FOUND:', set(e)); bad += 1
if '—' in txt:
    print('EM DASHES FOUND:', txt.count('—'))
    for m in re.finditer('—', txt):
        print('   ...', txt[max(0, m.start() - 60):m.start() + 20].replace('\n', ' '))
    bad += 1
idre = re.compile(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
ids = idre.findall(txt)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print('MISSING IDS:', missing); bad += 1
loose = re.findall(r'(?<!\*\*)\[([MLR]\d{4}-\d{3})\](?!\*\*)', txt)
if loose:
    print('IDS NOT IN BOLD:', set(loose)); bad += 1
breaks = [m.start() for m in re.finditer(r'\n\s*\n|\n\s*- |\n\s*\d+\. |\n\|', txt)]
nfr = 0
last = 0
for m in idre.finditer(txt):
    k = bisect.bisect_right(breaks, m.start())
    b = breaks[k - 1] if k > 0 else 0
    start = max(last, b)
    last = m.end()
    span = norm(txt[start:m.start()])
    rid = m.group(1)
    if rid not in rows:
        continue
    q = norm(rows[rid])
    for frag in re.findall(r'"([^"]{3,})"', span):
        for piece in [p.strip(' .,;:') for p in frag.split('[...]')]:
            if len(piece) < 3:
                continue
            nfr += 1
            if piece not in q:
                print(f'NOT IN ROW {rid}: "{piece[:140]}"'); bad += 1
print(f'{len(ids)} id citations, {len(set(ids))} distinct, {nfr} fragments checked; problems: {bad}')
sys.exit(1 if bad else 0)
