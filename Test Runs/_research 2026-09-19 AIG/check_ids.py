import csv, re, sys
run = open('Test Runs/2026-09-19 Run - AIG American International Group.md', encoding='utf-8').read()
ids = set(re.findall(r'E[1-5]-\d+', run))
led = set()
with open('principle_ledger.csv', encoding='utf-8-sig') as f:
    for row in csv.reader(f):
        if row and re.match(r'E[1-5]-\d+$', row[0].strip()): led.add(row[0].strip())
print('ledger rows', len(led), '| cited', len(ids), '| MISSING:', sorted(ids - led))
