# Checks the run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every "double-quoted fragment"
# lying between the previous id and an id (the whole file read as one line) is found verbatim in that id's row
# ([...] splits a fragment). Filing text in the run file is quoted in single typographic quotes and is not checked.
import csv, re, sys
RUN = r'C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-10-16 Run - TRN Trinity Industries.md'
LEDGER = r'C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv'
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(LEDGER, encoding='utf-8-sig'))}
txt = open(RUN, encoding='utf-8').read()
bad = 0
if re.search(r'\[E\d-\d+\]', txt):
    print('E-id found'); bad += 1
idre = re.compile(r'\[([MLR]\d{4}-\d{3})\]')
flat = re.sub(r'\s*\n\s*', ' ', txt)
last = 0
for m in idre.finditer(flat):
    i = m.group(1)
    seg = flat[last:m.start()]
    last = m.end()
    if i not in rows:
        print('MISSING', i); bad += 1; continue
    for q in re.findall(r'"([^"]{6,})"', seg):
        for part in [p.strip(' .,;') for p in q.split('[...]')]:
            if part and part not in rows[i]:
                print(i, 'NOT IN ROW:', part[:100]); bad += 1
print('ids checked:', len(set(idre.findall(txt))), 'problems:', bad)
sys.exit(1 if bad else 0)
