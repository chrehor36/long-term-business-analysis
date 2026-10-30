import re, csv, sys, glob
led = set()
with open('principle_ledger.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        for c in row[:2]:
            if re.fullmatch(r'E\d-\d+', c.strip()): led.add(c.strip())
txt = ''
for fn in sys.argv[1:]:
    txt += open(fn, encoding='utf-8').read()
ids = set(re.findall(r'E\d-\d+', txt))
print('cited', len(ids), 'missing from ledger:', sorted(ids - led))
