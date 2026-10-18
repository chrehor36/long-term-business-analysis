"""Citation check for the APEMY run file: (1) no E-ids; (2) every M/L/R id exists in principle_ledger_v5.csv;
(3) every double-quoted fragment immediately followed by one or more bold ids is found in at least one of those rows
(elisions '[...]' split the fragment; curly/straight quotes normalised)."""
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = sys.argv[1]; LEDGER = sys.argv[2]
t = open(RUN, encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', t)
print('E-ids:', eids or 'none'); bad += len(eids)
ids = sorted(set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)))
missing = [i for i in ids if i not in rows]
print(f'ids cited: {len(ids)}; missing: {missing or "none"}'); bad += len(missing)
# quoted fragment followed (within a short gap) by bold ids
pat = re.compile(r'"([^"]{6,}?)"[^"\n]{0,40}?((?:\s*,?\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)+)')
n = 0
for m in pat.finditer(t):
    frag = m.group(1); cited = re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [norm(p) for p in frag.split('[...]') if norm(p)]
    ok = any(all(p in norm(rows.get(c, '')) for p in parts) for c in cited)
    n += 1
    if not ok:
        bad += 1; print('FAIL', cited, '|', frag[:120])
print(f'quoted fragments checked: {n}; failures: {bad}')
print('RESULT:', 'PASS' if bad == 0 else 'FAIL')
