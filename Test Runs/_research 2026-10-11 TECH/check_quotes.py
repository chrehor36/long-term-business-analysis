"""Check the TECH run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every double-quoted fragment that sits directly before a bold id is found in that row
(fragments split at [...]; curly and straight quotes normalised for the comparison only)."""
import csv, re, sys

LEDGER = r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv'
RUN = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-11 Run - TECH Bio-Techne.md'

rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()

def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()

bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-ids found:', eids); bad += 1

ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print('missing ids:', missing); bad += 1
print('ids cited:', len(ids), 'distinct:', len(set(ids)))

# a quoted fragment followed (within a few characters) by one or more bold ids: check against the first id
pat = re.compile(r'["\u201c]([^"\u201c\u201d]{3,}?)["\u201d][\s,.;:)]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
n = 0
for m in pat.finditer(text):
    frag, i = m.group(1), m.group(2)
    if i not in rows:
        continue
    row = norm(rows[i])
    for part in re.split(r'\s*\[\.\.\.\]\s*', frag):
        p = norm(part).strip(' .,;:')
        if not p:
            continue
        n += 1
        if p not in row:
            print(f'NOT IN ROW {i}: "{part}"'); bad += 1
print('fragments checked:', n)
print('RESULT:', 'PASS' if bad == 0 else f'FAIL ({bad})')
