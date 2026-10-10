# Run-file citation check (the brief's own check): no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment that stands immediately before an id (the quote, optional words in brackets or parentheses, then the id)
# is found in that row, each [...]-separated piece separately, after normalising quotes, dashes and spaces.
import csv, re, sys
RUN = "Test Runs/2026-10-07 Run - CMG Chipotle.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-').replace('�', '')
    s = s.replace('"', '').replace("'", '')
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# the quoted fragment immediately before an id: the last "..." span in the 400 characters before the id, with no more
# than 60 characters (and no other id) between its closing quote and the id; a nested inner quote is rejoined.
flat = re.sub(r'\s*\n\s*', ' ', text)
PAIRS = [(q.start(), q.end(), q.group(1)) for q in re.finditer(r'"([^"]*)"', flat)]  # paired over the whole text
n = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    rid = m.group(1)
    if rid not in rows: continue
    qs = [q for q in PAIRS if q[1] <= m.start() and q[1] >= m.start() - 400]
    if not qs: continue
    a, b, frag = qs[-1]
    gap = flat[b:m.start()]
    if len(gap) > 60 or '**[' in gap: continue
    if len(qs) >= 2 and (frag.strip() == '' or len(frag) < 3):   # nested inner quote: rejoin
        frag = qs[-2][2] + frag
    n += 1
    row = norm(rows[rid])
    for piece in re.split(r'\[\.\.\.\]', frag):
        p2 = norm(piece)
        if p2 and p2 not in row:
            print(f'NOT IN ROW {rid}: "{piece.strip()[:120]}"'); bad += 1
print(f'ids cited: {len(ids)} ({len(set(ids))} distinct); quoted fragments checked: {n}; problems: {bad}')
sys.exit(1 if bad else 0)
