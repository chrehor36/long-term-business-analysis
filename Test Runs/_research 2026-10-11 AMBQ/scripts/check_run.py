"""Check the AMBQ run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment that
stands immediately before an id is in that row (elisions [...] split the fragment). Also lists ids with no quote
immediately before them, for a reader's eye."""
import csv, re, sys
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
norm = lambda t: re.sub(r'\s+', ' ', t).strip()
bad = 0
for e in re.findall(r'\[(E\d+-\d+)\]', run):
    print('E-ID FOUND', e); bad += 1
flat = norm(run)
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat)
for i in sorted(set(ids)):
    if i not in rows:
        print('MISSING ID', i); bad += 1
# quote immediately before an id: "...." [optional punctuation/words up to 3 chars] **[ID]**
checked = 0
for m in re.finditer(r'"([^"]{3,}?)"[.,;:)]?\s*\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    frag, i = m.group(1), m.group(2)
    row = norm(rows.get(i, ''))
    for part in frag.split('[...]'):
        part = norm(part).strip(' .,;')
        if part and part not in row:
            print(f'NOT IN ROW {i}: {part!r}'); bad += 1
    checked += 1
# ids not preceded by a closing quote within 4 characters
for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', flat):
    pre = flat[max(0, m.start()-6):m.start()]
    if '"' not in pre and ']**' not in pre:
        print('id without a quote just before it:', m.group(1), '...', flat[max(0, m.start()-90):m.start()])
print(f'{len(ids)} id uses, {len(set(ids))} distinct, {checked} quoted fragments checked, problems: {bad}')
sys.exit(1 if bad else 0)
