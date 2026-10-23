"""Check the EIX run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every straight-quoted fragment
placed between the previous id (or paragraph start) and an id is in that id's row (elisions [...] split)."""
import csv, re, sys, os
root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.stdout.reconfigure(encoding='utf-8')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(root, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
text = open(os.path.join(root, 'Test Runs', '2026-10-22 Run - EIX Edison International.md'), encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
problems = 0
for m in re.finditer(r'\[(E\d-\d+)\]', text):
    print('E-id found:', m.group(1)); problems += 1
paras = re.split(r'\n\s*\n|\n- |\n\d+\. ', text)
for para in paras:
    flat = norm(para)
    prev = 0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
        rid = m.group(1)
        if rid not in rows:
            print('MISSING id', rid); problems += 1; prev = m.end(); continue
        seg = flat[prev:m.start()]
        # keep only the text after the last sentence or attribution boundary that lies outside a quotation
        inq = False; cut = 0
        for i, ch in enumerate(seg):
            if ch == '"': inq = not inq
            elif not inq and seg[i:i+2] in ('. ', '; ', '): ', ').', '),'):
                cut = i + 2
        seg = seg[cut:]
        # only the quotes in the last sentence-ish chunk before the id (after the last id or semicolon-free run)
        for q in re.findall(r'"([^"]+)"', seg):
            parts = [p.strip(' .,;') for p in q.split('[...]') if p.strip(' .,;')]
            row = norm(rows[rid])
            for p in parts:
                if p not in row:
                    print(f'NOT IN ROW {rid}: "{p[:90]}"'); problems += 1
        prev = m.end()
ids = sorted(set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)))
print(len(ids), 'distinct ids;', problems, 'problems')
