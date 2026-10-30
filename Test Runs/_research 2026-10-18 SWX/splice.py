"""Replace the run file's text from START marker up to (not including) END marker with draft.md. Usage: python -I splice.py START END"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, '..', '2026-10-18 Run - SWX Southwest Gas Holdings.md')
t = open(p, encoding='utf-8').read()
s, e = sys.argv[1], sys.argv[2]
i = t.index(s); j = t.index(e, i + 1) if e != 'EOF' else len(t)
d = open(os.path.join(here, 'draft.md'), encoding='utf-8').read()
open(p, 'w', encoding='utf-8', newline='\n').write(t[:i] + d + t[j:])
os.remove(os.path.join(here, 'draft.md'))
print('spliced', i, j)
