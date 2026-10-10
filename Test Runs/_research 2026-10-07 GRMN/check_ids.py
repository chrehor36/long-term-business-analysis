"""Check for the GRMN run: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment beside an id is in that row."""
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
L = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
t = open('Test Runs/2026-10-07 Run - GRMN Garmin.md', encoding='utf-8').read()
probs = []
if re.search(r'\[E\d', t): probs.append('E-id present')
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in set(ids):
    if i not in L: probs.append('missing ' + i)
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('“', '"').replace('”', '"')).strip()
# quoted fragments immediately before an id: "....." **[ID]** (optionally with a few words between)
for m in re.finditer(r'"([^"\n]{12,}?)"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t):
    frag, i = m.group(1), m.group(2)
    row = norm(L.get(i, ''))
    for piece in norm(frag).split('[...]'):
        p = piece.strip(' .,;')
        if p and p not in row:
            probs.append(f'{i}: fragment not in row: {p[:90]}')
print(f'{len(set(ids))} distinct ids, {len(probs)} problems')
for p in probs: print(' ', p)
