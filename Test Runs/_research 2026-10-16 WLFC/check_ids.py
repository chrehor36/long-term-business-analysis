"""Citation check for the WLFC run file.
1. No E-ids.  2. Every M/L/R id exists in principle_ledger_v5.csv.
3. Every quoted fragment that is followed (within the same clause) by one or more bolded ids is found, after splitting on
   [...] and ' ... ', in at least one of those rows' verbatim quote (whitespace normalised; straight and curly quotes
   compared as written, no smoothing).
Usage: python -I check_ids.py <run file> <ledger csv>"""
import csv, io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
run, ledger = sys.argv[1], sys.argv[2]
text = open(run, encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(ledger, encoding='utf-8-sig'))}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
fail = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-ids found:', sorted(set(eids))); fail += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
missing = sorted({i for i in ids if i not in rows})
if missing:
    print('MISSING ids:', missing); fail += 1
print(f'{len(ids)} id citations, {len(set(ids))} distinct, {len(missing)} missing')
flat = norm(text)
# a quote, then up to 60 chars containing no other quote mark, then a run of bolded ids
pat = re.compile(r'"([^"]{3,600}?)"((?:[^"]{0,60}?)\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:\s*,\s*\*\*\[[MLR]\d{4}-\d{3}\]\*\*)*)')
checked = 0
for m in pat.finditer(flat):
    q, tail = m.group(1), m.group(2)
    if '**[' in tail.split('**[')[0] and False: pass
    tids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', tail)
    # only the first id-run after the quote counts
    frags = [f.strip(' .,;:') for f in re.split(r'\[\.\.\.\]| \.\.\. ', q) if f.strip(' .,;:')]
    ok = all(any(norm(f) in norm(rows.get(t, '')) for t in tids) for f in frags)
    checked += 1
    if not ok:
        fail += 1
        print(f'NOT IN ROW {tids}: "{q[:160]}"')
print(f'{checked} quoted fragments beside ids checked')
print('PASS' if not fail else f'FAIL ({fail})')
