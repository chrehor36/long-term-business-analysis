"""Check the SBUX run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment placed
immediately before an id (pattern: "fragment" **[ID]** or "fragment" ([...]) **[ID]**) is in that row's quote.
Elisions [...] split a fragment into parts, each checked. Curly and straight quotes/apostrophes and dashes normalised."""
import csv, re, sys
RUN = r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/2026-10-10 Run - SBUX Starbucks.md'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(r'C:/Users/chreh/OneDrive/Documents/BRK/principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-').replace('\ufffd', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
ids = set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text))
for i in sorted(ids):
    if i not in rows: print('MISSING id', i); bad += 1
n = 0
qpos = [m.start() for m in re.finditer('"', text)]
if len(qpos) % 2: print('odd number of straight double quotes; pairing may be off'); bad += 1
for k in range(0, len(qpos) - 1, 2):
    a, b = qpos[k], qpos[k + 1]
    frag = text[a + 1:b]
    after = text[b + 1:b + 60]
    m = re.match(r'[^"]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', after)
    if not m: continue
    i = m.group(1)
    if i not in rows: continue
    q = norm(rows[i]); n += 1
    for part in frag.split('[...]'):
        pp = norm(part).strip(' .,;:')
        if pp and pp not in q:
            print(f'NOT IN ROW {i}: "{part.strip()}"'); bad += 1
print(f'{len(ids)} distinct ids, {n} quoted fragments checked, {bad} problems')
sys.exit(1 if bad else 0)
