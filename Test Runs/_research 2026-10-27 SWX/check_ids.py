import csv, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
L = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(r'C:\Projects\BRK\principle_ledger_v5.csv', encoding='utf-8-sig'))}
txt = open(r'C:\Projects\BRK\Test Runs\2026-10-27 Run - SWX Southwest Gas Holdings.md', encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = s.replace('\u2014', '-').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
probs = 0
eids = re.findall(r'\[E\d-\d+\]', txt)
if eids: print('E-ids found:', eids); probs += 1
ids = re.findall(r'\[((?:M|L|R)\d{4}-\d{3})\]', txt)
for i in sorted(set(ids)):
    if i not in L: print('MISSING id', i); probs += 1
# quoted fragment immediately followed by an id: "..." **[ID]**  (also "..." **[A]**, **[B]**: check first id only)
n = 0
for m in re.finditer(r'"([^"]{3,600})"\s*(?:\([^)]{0,80}\)\s*)?\*\*\[((?:M|L|R)\d{4}-\d{3})\]\*\*', txt):
    frag, i = m.group(1), m.group(2)
    n += 1
    if i not in L: continue
    row = norm(L[i])
    for part in re.split(r'\[\.\.\.\]', frag):
        p = norm(part).strip(' .,;:')
        if p and p not in row:
            print(f'FRAGMENT NOT IN {i}: "{part.strip()}"'); probs += 1
print(f'{len(set(ids))} ids, {n} fragments, {probs} problems')
