import sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read()
old = "**POSITION NOTE, declared before any verdict:** blind run: not checked, by the brief's blind rule."
assert t.count(old) == 1
t = t.replace(old, old + " Filled by the dispatching session at the fold (overnight 2026-10-16), after the run was committed: **not held** (`PORTFOLIO.md` carries no line for R or Ryder).")
open(p, 'w', encoding='utf-8').write(t)
