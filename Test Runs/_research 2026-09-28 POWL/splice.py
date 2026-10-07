# usage: python splice.py FRAG START_MARKER END_MARKER  (replaces [start, end) in the run file)
import sys
run='../2026-09-28 Run - POWL Powell Industries.md'
frag, a, b = sys.argv[1:4]
s=open(run,encoding='utf-8').read(); f=open(frag,encoding='utf-8').read().rstrip('\n')+'\n\n'
i=s.index(a); j=s.index(b, i+1)
assert s.count(a)==1, a
s=s[:i]+f+s[j:]
open(run,'w',encoding='utf-8').write(s); print('ok', i, j, len(s))
