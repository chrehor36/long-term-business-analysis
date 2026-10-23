# Checks for the IDA run file: no E-ids; every M/L/R id exists in the v5 ledger;
# every quoted fragment immediately followed by an id (quote ... **[ID]** within 40 chars) is found in that row.
import csv, re, sys, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-23 Run - IDA IDACORP.md'
LED = r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LED, encoding='utf-8-sig'))}
t = open(RUN, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', t)
if eids: print('E-ids found:', eids); bad += 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', t))
for i in sorted(ids):
    if i not in rows: print('MISSING id', i); bad += 1
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).strip()
n = 0
for m in re.finditer(r'"([^"]{6,}?)"((?:[^"\n]{0,40}?\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)', t):
    q = m.group(1); idl = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    parts = [p.strip() for p in q.split('[...]') if p.strip()]
    for i in idl[:1]:
        row = norm(rows.get(i, ''))
        for p in parts:
            p2 = norm(p).strip(' .,;')
            # allow bracketed insertions like include[s]
            if p2 not in row:
                print('NOT IN ROW', i, '::', p2[:120]); bad += 1
        n += 1
print('ids:', len(ids), 'quote-id pairs checked:', n, 'problems:', bad)
