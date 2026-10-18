import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-13 Run - FSTR L.B. Foster.md'
LEDGER = r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
text = re.sub(r'\s*\n\s*', ' ', open(RUN, encoding='utf-8').read())
text = text.replace('“', '"').replace('”', '"')
def norm(s):
    s = s.replace('\ufffd', "'").replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# every "quote" immediately followed (optionally by a comma) by one or more bold ids must be in the first id's row
for m in re.finditer(r'"([^"\n]{3,400})",?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    row = norm(rows[i])
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*', frag) if p.strip()]
    for p in parts:
        if norm(p) not in row:
            print(f'NOT IN ROW {i}: {p!r}'); bad += 1
print('ids cited:', len(set(ids)), '| quote-id pairs checked:', len(re.findall(r'"([^"\n]{3,400})",?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)))
print('PASS' if not bad else f'FAIL ({bad})')
