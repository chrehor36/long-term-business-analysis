import sys, re, os

D = 'Test Runs/_research 2026-09-19 OTTR/peers'

pats = sys.argv[2:]
f = os.path.join(D, sys.argv[1])
lines = open(f, encoding='utf-8').read().split('\n')
for i, ln in enumerate(lines):
    if len(ln) > 900:
        continue
    for p in pats:
        if re.search(p, ln, re.I):
            print('%d: %s' % (i + 1, ln[:400]))
            break
