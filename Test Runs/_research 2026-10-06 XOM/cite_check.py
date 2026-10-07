"""Every [M|L|R yyyy-nnn] id in the run file must exist in principle_ledger_v5.csv. Usage: cite_check.py RUNFILE"""
import csv, re, sys
ids = set()
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for x in csv.DictReader(f):
        ids.add(x['id'])
txt = open(sys.argv[1], encoding='utf-8').read()
found = sorted(set(re.findall(r'\b([MLR]\d{4}-\d{3})\b', txt)))
missing = [i for i in found if i not in ids]
print(f'{len(found)} distinct ids cited; missing: {missing or "none"}')
