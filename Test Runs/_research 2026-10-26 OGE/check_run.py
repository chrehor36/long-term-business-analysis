# Check for the OGE run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment set directly before an id (same line, nothing but space, punctuation or
# a closing parenthesis between the closing quote and the id) is a substring of that row's quote.
# Run from the repository root: python -I "Test Runs/_research 2026-10-26 OGE/check_run.py"
import csv, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = 'Test Runs/2026-10-26 Run - OGE OGE Energy.md'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
text = open(RUN, encoding='utf-8').read()
bad = 0
if re.search(r'\[E\d', text):
    print('E-id found'); bad += 1
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING id', i); bad += 1
def norm(s):
    return re.sub(r'\s+', ' ', s.replace('“', '"').replace('”', '"')).strip()
pat = re.compile(r'"((?:[^"\n]|"[^"\n]*?"(?=[^\s.,;:)]))+?)"\s*[.,;:)]*\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*')
checked = 0
for line in text.splitlines():
    for m in re.finditer(r'"([^"\n]{3,}?)"[\s.,;:)]{0,4}\*\*\[([MLR]\d{4}-\d{3})\]\*\*', line):
        frag, i = m.group(1), m.group(2)
        checked += 1
        row = norm(rows.get(i, ''))
        f = norm(frag)
        if f not in row:
            # allow a fragment that itself contains nested straight quotes: test each piece
            pieces = [p for p in re.split(r'"', f) if p.strip()]
            if not all(norm(p) in row for p in pieces):
                print('NOT IN ROW', i, '|', frag[:120]); bad += 1
print(f'ids cited: {len(set(ids))} distinct; fragments checked: {checked}; problems: {bad}')
print('PASS' if bad == 0 else 'FAIL')
