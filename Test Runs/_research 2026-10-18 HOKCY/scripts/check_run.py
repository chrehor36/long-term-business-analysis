# Check the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
# that sits immediately before an id (same sentence) is a substring of that row (quotes normalised for curly/straight).
import re, csv, sys
run = sys.argv[1]; ledger = sys.argv[2]
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('�', "'")
    return re.sub(r'\s+', ' ', s).strip()
bad = 0
for m in re.finditer(r'\[E\d', t):
    print('E-id found at', m.start()); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', t)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
# quoted fragment(s) directly followed (within 12 chars) by one or more ids
pat = re.compile(r'"([^"]{6,600})"[^"\[]{0,14}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)')
n = 0
for m in pat.finditer(t):
    frag = m.group(1); idl = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    pieces = [p for p in re.split(r'\s*\.\.\.\s*|\s*\[\.\.\.\]\s*', frag) if p.strip()]
    ok = any(all(norm(p) in norm(rows.get(i, '')) for p in pieces) for i in idl)
    n += 1
    if not ok:
        print('FRAGMENT NOT IN ROW', idl, '::', frag[:120]); bad += 1
print(f'ids {len(set(ids))}, fragments checked {n}, problems {bad}')
sys.exit(1 if bad else 0)
