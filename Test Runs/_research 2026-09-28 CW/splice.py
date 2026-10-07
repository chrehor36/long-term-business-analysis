# usage: python splice.py FRAG START_MARKER END_MARKER  (replaces [start, end) in the run file)
import sys
F = '../2026-09-28 Run - CW Curtiss-Wright.md'
frag, a, b = sys.argv[1:4]
t = open(F, encoding='utf-8').read()
i = t.index(a); j = t.index(b, i + len(a)) if b != 'EOF' else len(t)
assert t.count(a) == 1, ('start marker not unique', t.count(a))
new = open(frag, encoding='utf-8').read()
t = t[:i] + new + t[j:]
open(F, 'w', encoding='utf-8').write(t)
print('spliced', frag, len(new))
