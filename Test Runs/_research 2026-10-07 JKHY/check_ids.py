"""Citation check for the JKHY run file: no E-ids; every M/L/R id exists in principle_ledger_v5.csv; every quoted fragment
standing beside an id (the quote immediately before the bolded id or id chain) appears in one of those rows."""
import csv, re, os, sys
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, '..', '..')
run = os.path.join(root, 'Test Runs', '2026-10-07 Run - JKHY Jack Henry.md')
rows = {}
for r in csv.DictReader(open(os.path.join(root, 'principle_ledger_v5.csv'), encoding='utf-8')):
    rows[r.get('﻿id') or r.get('id')] = r['quote_verbatim']
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-').replace('�', '')
    return re.sub(r'\s+', ' ', s).strip().lower()
text = open(run, encoding='utf-8').read()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids: print('E-ids found:', eids); bad += 1
ids = re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text)
for i in sorted(set(ids)):
    if i not in rows: print('MISSING id', i); bad += 1
flat = re.sub(r'\s+', ' ', text)
pat = re.compile(r'"([^"]{4,400})"((?:[^"*]{0,60}?)(?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)')
checked = 0
for m in pat.finditer(flat):
    quote = m.group(1)
    chain = re.findall(r'\[([MLR]\d{4}-\d{3})\]', m.group(2))
    parts = [p for p in re.split(r'\[\.\.\.\]', quote) if len(p.strip()) > 3]
    ok = any(all(norm(p) in norm(rows.get(c, '')) for p in parts) for c in chain)
    checked += 1
    if not ok:
        print('FRAGMENT NOT IN ROW', chain, '|', quote[:120]); bad += 1
print(f'ids cited: {len(set(ids))}; quote fragments checked: {checked}; problems: {bad}')
print('check_ids PASS' if bad == 0 else 'check_ids FAIL')
