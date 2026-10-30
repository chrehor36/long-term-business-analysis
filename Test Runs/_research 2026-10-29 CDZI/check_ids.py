# Check for the CDZI run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that
# stands immediately before (or immediately after, as "id (quote)") an id is in that row's verbatim text.
# Usage: python -I check_ids.py <repo root>
import csv, re, sys, os
root = sys.argv[1]
run = os.path.join(root, 'Test Runs', '2026-10-29 Run - CDZI Cadiz.md')
rows = {}
with open(os.path.join(root, 'principle_ledger_v5.csv'), encoding='utf-8-sig') as f:
    r = csv.reader(f); next(r)
    for row in r:
        rows[row[0]] = row[2]
text = open(run, encoding='utf-8').read()
bad = 0
for m in re.finditer(r'\[(E\d?-\d+)\]', text):
    print('E-ID FOUND', m.group(1)); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING ID', i); bad += 1
print('ids cited:', len(set(ids)))
QUOTE = r'"([^"]{6,})"|“([^”]{6,})”'
checked = 0
for para in re.split(r'\n\s*\n', text):
    flat = ' '.join(para.split())
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
        rid = m.group(1)
        before = flat[:m.start()]
        # the quote that ends within 12 characters before the id
        qs = [q for q in re.finditer(QUOTE, before)]
        frag = None
        if qs and len(before) - qs[-1].end() <= 12:
            frag = qs[-1].group(1) or qs[-1].group(2)
        else:
            after = flat[m.end():m.end() + 6]
            qa = re.match(r'\s*\(\s*' + QUOTE, flat[m.end():])
            if qa: frag = qa.group(1) or qa.group(2)
        if frag is None or rid not in rows:
            continue
        checked += 1
        src = ' '.join(rows[rid].split())
        parts = [p.strip(' .,;:') for p in frag.split('[...]') if p.strip(' .,;:')]
        for p in parts:
            p = ' '.join(p.split())
            if p not in src:
                print('FRAGMENT NOT IN ROW', rid, '::', p[:120]); bad += 1
print('quoted fragments checked:', checked)
print('RESULT:', 'PASS' if bad == 0 else 'FAIL (%d)' % bad)
