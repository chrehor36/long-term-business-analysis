"""Check the run file's citations: no E-ids; every M/L/R id exists in principle_ledger_v5.csv;
every quoted fragment immediately preceding an id (same segment, after the previous id) is in that row."""
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = "Test Runs/2026-10-18 Run - BESS Bimergen Energy.md"
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open('principle_ledger_v5.csv', encoding='utf-8-sig'))}
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(RUN, encoding='utf-8').read()
problems = 0
for m in re.finditer(r'\[E\d', text):
    print('E-id found at', m.start()); problems += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in set(ids):
    if i not in rows:
        print('MISSING id', i); problems += 1
paras = [' '.join(b.split('\n')) for b in re.split(r'\n\s*\n|\n(?=- |\| |## )', text)]
for line in paras:
    pos = 0
    for m in re.finditer(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', line):
        seg = line[pos:m.start()]
        pos = m.end()
        rid = m.group(1)
        if rid not in rows: continue
        rq = norm(rows[rid])
        for q in re.findall(r'"([^"]+)"', seg):
            for part in q.split('[...]'):
                p = norm(part).strip(' .,;:')
                if len(p) < 4: continue
                if p not in rq:
                    print(f'FRAGMENT NOT IN {rid}: "{part.strip()}"'); problems += 1
print('ids cited:', len(set(ids)), 'problems:', problems)
