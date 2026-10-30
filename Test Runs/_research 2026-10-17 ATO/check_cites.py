import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = "../2026-10-17 Run - ATO Atmos Energy.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('../../principle_ledger_v5.csv', encoding='utf-8-sig'))}
txt = open(RUN, encoding='utf-8').read()
def norm(s):
    s = s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
    return re.sub(r'\s+', ' ', s).strip()
problems = 0
eids = re.findall(r'\[E\d+-\d+\]', txt)
if eids: print("E-ids found:", eids); problems += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', txt)
for i in sorted(set(ids)):
    if i not in rows: print("MISSING id:", i); problems += 1
# quoted fragment immediately before an id (allow up to 3 chars of punctuation/space between close-quote and the id)
pat = re.compile(r'(["\u201c])([^"\u201c\u201d]{3,700}?)(["\u201d])([\s,.;:]{0,3})\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for m in pat.finditer(txt):
    frag, rid = m.group(2), m.group(5)
    if rid not in rows: continue
    row = norm(rows[rid])
    for piece in re.split(r'\[\.\.\.\]', frag):
        p = norm(piece).strip(' .,;:')
        if len(p) < 4: continue
        checked += 1
        if p not in row and p.replace('""', '"') not in row:
            print(f"NOT IN ROW {rid}: «{p[:160]}»"); problems += 1
print(f"ids cited: {len(set(ids))} distinct, {len(ids)} total; quoted fragments checked: {checked}; problems: {problems}")
