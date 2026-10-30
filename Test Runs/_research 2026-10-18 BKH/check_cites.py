# Checks a run file: no E-ids; every M/L/R id exists in the v5 ledger; every quoted fragment
# immediately before an id (within the same sentence) is in that row (quotes/apostrophes normalized).
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
run, ledger = sys.argv[1], sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('�', '').replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(run, encoding='utf-8').read()
problems = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids: print('E-ids found:', set(eids)); problems += len(eids)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); problems += 1
# quoted fragment then optional punctuation/space then **[ID]**
for m in re.finditer(r'"([^"\n]{3,600})"[^"\n]{0,40}?\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text):
    frag, i = m.group(1), m.group(2)
    between = text[m.end(1)+1:m.start(0)+len(m.group(0))-len(i)-6]
    if '"' in between: continue
    if i not in rows: continue
    row = norm(rows[i])
    for part in frag.split('[...]'):
        p = norm(part).strip(' .,;:')
        if p and p not in row:
            print(f'NOT IN ROW {i}: "{part.strip()}"'); problems += 1
print('ids cited:', len(set(ids)), 'problems:', problems)
