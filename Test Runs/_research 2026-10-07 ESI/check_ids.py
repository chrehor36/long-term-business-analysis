# Checks the ESI run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that sits
# immediately before an id (in the same sentence or clause) appears in that row's quote, after normalising quotes/dashes.
import csv, re, sys, unicodedata
RUN = 'Test Runs/2026-10-07 Run - ESI Element Solutions.md'
rows = {}
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        rows[r['id']] = r['quote_verbatim']
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('—', '-'), ('–', '-'), ('�', "'")):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(RUN, encoding='utf-8').read()
problems = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids: print('E-ids found:', eids); problems += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); problems += 1
# fragments: a double-quoted string followed within 40 chars by **[ID]** (no other quote in between)
pat = re.compile(r'["“]([^"“”]{6,}?)["”][^"“”\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for m in pat.finditer(text):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    q = norm(rows[i])
    parts = [p for p in re.split(r'\s*\[\.\.\.\]\s*', norm(frag)) if p]
    checked += 1
    for p in parts:
        p2 = p.strip(' .,;:')
        if p2 and p2 not in q:
            print(f'FRAGMENT NOT IN ROW {i}: "{p2[:120]}"'); problems += 1
print(f'{len(set(ids))} distinct ids, {checked} quoted fragments checked, {problems} problems')
sys.exit(1 if problems else 0)
