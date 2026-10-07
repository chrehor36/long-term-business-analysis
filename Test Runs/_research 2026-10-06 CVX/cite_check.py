"""Check the run file's citations against principle_ledger_v5.csv: every **[ID]** must exist, no v4 E-id may appear, and
every double-quoted fragment that stands immediately before an id (or before a run of ids) must be found in one of those
rows (fragments split on [...] are checked piecewise). Usage: python -I cite_check.py"""
import csv, re, pathlib

root = pathlib.Path(__file__).resolve().parents[2]
run = root / 'Test Runs' / '2026-10-06 Run - CVX Chevron.md'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(root / 'principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = run.read_text(encoding='utf-8')


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return re.sub(r'\s+', ' ', s).strip().lower()


ids = re.findall(r'\*\*\[([A-Z]+\d{4}-\d{3})\]\*\*', text)
eids = re.findall(r'\[E\d+-\d+\]', text)
problems = []
for i in sorted(set(ids)):
    if i not in rows:
        problems.append(f'missing id {i}')
if eids:
    problems.append(f'v4 ids present: {sorted(set(eids))}')

# quote immediately followed (allowing punctuation/space) by one or more ids
pat = re.compile(r'"([^"]{4,}?)"[\s.,;:)]*((?:\*\*\[[A-Z]+\d{4}-\d{3}\]\*\*[\s,]*)+)')
checked = 0
for m in pat.finditer(text):
    frag, idblock = m.group(1), m.group(2)
    cands = re.findall(r'\[([A-Z]+\d{4}-\d{3})\]', idblock)
    pieces = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip(' .')]
    ok = any(all(norm(p).strip(' .') in norm(rows.get(c, '')) for p in pieces) for c in cands)
    checked += 1
    if not ok:
        problems.append(f'fragment not found in {cands}: "{frag[:90]}"')
print(f'{len(set(ids))} distinct ids cited; {checked} quoted fragments checked; {len(problems)} problems')
for p in problems:
    print('  ', p)
