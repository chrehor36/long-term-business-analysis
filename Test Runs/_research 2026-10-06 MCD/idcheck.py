"""Check that every bold [M/L/R id] in the run file exists in principle_ledger_v5.csv. Usage: python idcheck.py RUNFILE LEDGER"""
import csv, re, sys
ids = {r['id'] for r in csv.DictReader(open(sys.argv[2], encoding='utf-8-sig'))}
text = open(sys.argv[1], encoding='utf-8').read()
found = sorted(set(re.findall(r'\[([MLR]\d{4}-\d{3})\]', text)))
missing = [i for i in found if i not in ids]
print(len(found), 'distinct ids cited;', 'missing:', missing or 'none')
