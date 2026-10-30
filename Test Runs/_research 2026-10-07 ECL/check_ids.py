# Citation check for the ECL run: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
# every quoted fragment written immediately before an id is in that row (case, quotes, dashes, bold normalized).
import csv, re, sys, unicodedata
run = open(sys.argv[1], encoding='utf-8').read()
rows = {r[0]: r[2] for r in csv.reader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = unicodedata.normalize('NFKC', s).replace('�', "'")
    s = re.sub(r"[‘’`´]", "'", s); s = re.sub(r'[“”]', '"', s); s = re.sub(r'[–—]', '-', s)
    s = s.replace('**', '').replace('"', '').lower()
    return re.sub(r'[^a-z0-9$%]+', ' ', s).strip()
bad = 0
if re.search(r'\[E\d', run): print('E-id found'); bad += 1
for m in re.finditer(r'\[([MLR]\d{4}-\d{3})\]', run):
    i = m.group(1)
    if i not in rows: print('MISSING', i); bad += 1; continue
    before = run[max(0, m.start() - 700):m.start()]
    q = re.search(r'["“]([^"“”]{6,600})["”][\s\*,;:.\)\(]*$', before)
    if not q: continue
    for frag in re.split(r'\[\.\.\.\]', q.group(1)):
        f = norm(frag)
        if f and f not in norm(rows[i]): print('NOT IN ROW', i, '|', frag[:90]); bad += 1
ids = set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', run))
print(f'{len(ids)} distinct ids; problems: {bad}')
sys.exit(1 if bad else 0)
