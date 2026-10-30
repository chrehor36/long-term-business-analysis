# Check the run file: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment
# placed immediately before an id (within the same sentence) appears verbatim in that row.
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ledger = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open('../2026-10-13 Run - UHS Universal Health Services.md', encoding='utf-8').read()
bad = 0
for m in re.finditer(r'\[E\d+-\d+\]', text):
    print('E-id found:', m.group()); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in ledger: print('MISSING id', i); bad += 1
def norm(s):
    s = s.replace(' ', ' ')
    return re.sub(r'\s+', ' ', s).strip()
# quotes: "...." followed (within 40 chars, no other quote) by **[ID]** possibly several ids
checked = 0
for m in re.finditer(r'“?"([^"]{3,600}?)"[^"\[]{0,60}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    frag, i = m.group(1), m.group(2)
    if i not in ledger: continue
    row = norm(ledger[i])
    parts = [norm(p) for p in re.split(r'\s*\[\.\.\.\]\s*', frag) if p.strip()]
    for p in parts:
        checked += 1
        if p not in row:
            print(f'FRAGMENT NOT IN {i}: "{p[:120]}"'); bad += 1
print('ids:', len(set(ids)), 'fragments checked:', checked, 'problems:', bad)
