# Citation check: no E-ids; every M/L/R id exists; every quoted fragment just before an id is in that row.
import csv, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')
root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
rows = {r['id']: r['quote_verbatim'] for r in csv.DictReader(open(os.path.join(root, 'principle_ledger_v5.csv'), encoding='utf-8-sig'))}
run = open(os.path.join(root, 'Test Runs', '2026-10-17 Run - HWDJY Howden Joinery Group.md'), encoding='utf-8').read()
flat = re.sub(r'\s+', ' ', run)
problems = 0
eids = re.findall(r'\[(E\d+-\d+)\]', flat)
if eids: print('E-ids found:', eids); problems += len(eids)
ids = re.findall(r'\[([MLR]\d{4}-\d{3})\]', flat)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); problems += 1
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
# fragment immediately before an id: "...." **[ID]** or "...." [ID]
for m in re.finditer(r'"([^"]{6,600})"\s*(?:\*\*)?\[([MLR]\d{4}-\d{3})\]', flat):
    frag, i = m.group(1), m.group(2)
    if i not in rows: continue
    parts = [p for p in re.split(r'\[\.\.\.\]', frag) if p.strip()]
    for p in parts:
        if norm(p) not in norm(rows[i]):
            print(f'NOT IN ROW {i}: "{p[:90]}"'); problems += 1
print('fragments checked:', len(re.findall(r'"([^"]{6,600})"\s*(?:\*\*)?\[([MLR]\d{4}-\d{3})\]', flat)))
print('ids cited:', len(set(ids)), '| problems:', problems)
