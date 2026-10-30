import sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read()
old = "**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule.\n"
assert t.count(old) == 1
t = t.replace(old, "**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule. *Filled at the fold by the dispatching session, 2026-10-22, after the run was committed (eac4982f): `PORTFOLIO.md` read for this one ticker; **not held**.*\n")
open(p, 'w', encoding='utf-8', newline='').write(t)
print('filled')
