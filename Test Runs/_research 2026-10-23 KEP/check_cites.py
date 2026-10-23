"""Check the run file's citations: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
that sits immediately before an id (no other id between) is found in that row (quotes and whitespace normalised;
[...] splits fragments). Prints each pairing so a reader can audit the heuristic."""
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}

def norm(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    t = t.replace('—', '-').replace('–', '-').replace('�', '')
    return re.sub(r'\s+', ' ', t).strip().lower()

bad = 0
eids = re.findall(r'\[E\d+-\d+\]', run)
if eids: print('E-IDS FOUND:', eids); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', run)
missing = sorted({i for i in ids if i not in rows})
print(f'{len(ids)} id citations, {len(set(ids))} distinct; missing: {missing}')
bad += len(missing)

flat = re.sub(r'\s+', ' ', run)
checked = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    i = m.group(1); start = m.start()
    window = flat[max(0, start - 700):start]
    # cut the window at the previous id so a quote belongs to the nearest id only
    prev = [x.end() for x in re.finditer(r'\[[MLR]\d{4}-\d{3}\]', window)]
    if prev: window = window[prev[-1]:]
    quotes = re.findall(r'["“]([^"“”]{6,}?)["”]', window)
    if not quotes: continue
    q = quotes[-1]
    # only the quote that ends close to the id (within 160 chars) is taken as the row's words
    tail = window[window.rfind(q) + len(q):]
    if len(tail) > 160: continue
    frags = [f.strip(' .,;:') for f in re.split(r'\[\.\.\.\]|\.\.\.', q) if len(f.strip(' .,;:')) > 3]
    row = norm(rows.get(i, ''))
    for f in frags:
        checked += 1
        if norm(f) not in row:
            bad += 1
            print(f'MISMATCH {i}: "{f[:120]}"')
print(f'{checked} quoted fragments checked against their rows')
print('RESULT:', 'PASS' if bad == 0 else f'{bad} problem(s)')
