# Check the VUOC run file: no E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted fragment that
# immediately precedes an id (the last "..." ending within 12 characters before the id's bold marker, after joining
# lines) is in that row, split on [...] elisions, whitespace normalised.
import csv, re, sys
run = sys.argv[1]; led = sys.argv[2]
t = open(run, encoding='utf-8').read()
flat = re.sub(r'\s*\n\s*', ' ', t)
R = {r['id']: re.sub(r'\s+', ' ', r['quote_verbatim']) for r in csv.DictReader(open(led, encoding='utf-8-sig'))}
bad = 0
for e in re.findall(r'\[E\d-\d+\]', t):
    print('E-id found', e); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
for i in sorted(set(ids)):
    if i not in R: print('MISSING id', i); bad += 1
QUOTE = r'(?:"([^"]+)"|“([^”]+)”)'
checked = 0
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    i = m.group(1); pre = flat[max(0, m.start()-900):m.start()]
    qs = list(re.finditer(QUOTE, pre))
    if not qs: continue
    q = qs[-1]
    if len(pre) - q.end() > 12: continue
    frag = q.group(1) or q.group(2)
    for part in frag.split('[...]'):
        p = part.strip(' .,;:').strip()
        if len(p) < 4: continue
        checked += 1
        if p not in R.get(i, ''):
            print(f'NOT IN ROW {i}: {p[:100]}'); bad += 1
print(f'ids: {len(set(ids))} distinct, {len(ids)} uses; fragments checked: {checked}; problems: {bad}')
