"""Check the SWX run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
standing in the same sentence-chunk immediately before an id is a substring of that row (or of one of the ids that
follow it in the same group). Usage: python -I idcheck.py"""
import csv, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
run = os.path.join(root, 'Test Runs', '2026-10-18 Run - SWX Southwest Gas Holdings.md')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(root, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
t = open(run, encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
problems = []
eids = re.findall(r'\[E\d-\d+\]', t)
if eids: problems.append(f'E-ids present: {eids}')
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', t)
for i in sorted(set(ids)):
    if i not in rows: problems.append(f'missing id {i}')
# fragments: a double-quoted string followed (within 12 chars, allowing punctuation) by one or more bold ids
pat = re.compile(r'"([^"\n]{6,}?)"[^"\n]{0,12}?((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)')
nfrag = 0
for m in pat.finditer(t.replace('\n', ' ')):
    frag = m.group(1)
    cited = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    nfrag += 1
    nf = norm(frag.replace('[...]', ''))
    parts = [p.strip() for p in norm(frag).split('[...]') if p.strip()]
    if not any(all(p in norm(rows.get(c, '')) for p in parts) for c in cited):
        problems.append(f'fragment not in cited row(s) {cited}: "{frag[:90]}"')
print(f'ids cited: {len(set(ids))} distinct, {len(ids)} citations; fragments checked: {nfrag}; problems: {len(problems)}')
for p in problems: print('  ', p)
