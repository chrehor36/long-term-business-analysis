"""CHFFF run: check the run file's citations. No E-ids; every M/L/R id in principle_ledger_v5.csv; every quoted
fragment placed immediately before one or more bold ids is found in at least one of those rows (quotes and
apostrophes normalised; [...] splits a quote into parts, each of which must be found).
Run: python -I check_run.py"""
import csv, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
run = os.path.join(root, 'Test Runs', '2026-10-29 Run - CHFFF China Everbright Environment Group.md')
rows = {r[0].lstrip('﻿'): r[2] for r in csv.reader(open(os.path.join(root, 'principle_ledger_v5.csv'), encoding='utf-8'))}
text = open(run, encoding='utf-8').read()
def norm(s):
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('�', '?')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()
bad = 0
eids = re.findall(r'\[E\d+-\d+\]', text)
if eids:
    print('E-ids found:', eids); bad += 1
ids = set(re.findall(r'\*\*\[([MLR]\d{4}-\d{3})\]\*\*', text))
for i in sorted(ids):
    if i not in rows:
        print('MISSING id', i); bad += 1
flat = re.sub(r'\s+', ' ', text)
# a quote "..." followed (after optional punctuation/words up to 12 chars) by one or more **[ID]**
for m in re.finditer(r'"([^"]{3,600})"[^"*]{0,12}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', flat):
    q, idl = m.group(1), re.findall(r'[MLR]\d{4}-\d{3}', m.group(2))
    parts = [p for p in re.split(r'\[\.\.\.\]', q) if p.strip()]
    ok = any(all(norm(p).strip(' .,;:') in norm(rows.get(i, '')) for p in parts) for i in idl)
    if not ok:
        print('NOT IN ROW', idl, '|', q[:120]); bad += 1
pairs = list(re.finditer(r'"([^"]{3,600})"[^"*]{0,12}((?:\*\*\[[MLR]\d{4}-\d{3}\]\*\*(?:,\s*)?)+)', flat))
print(f'{len(pairs)} quote-id pairs checked')
print(f'{len(ids)} distinct ids checked; result:', 'PASS' if not bad else f'FAIL ({bad})')
sys.exit(1 if bad else 0)
