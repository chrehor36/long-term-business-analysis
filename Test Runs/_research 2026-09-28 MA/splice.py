# usage: python splice.py FRAG START_HEADING END_HEADING  (replace [start, end) in the run file)
import sys
p='../2026-09-28 Run - MA Mastercard.md'
t=open(p,encoding='utf-8').read()
frag=open(sys.argv[1],encoding='utf-8').read()
s,e=sys.argv[2],sys.argv[3]
i=t.index(s); j=len(t) if e=='EOF' else t.index(e,i+1)
assert t.count(s)==1, s
t=t[:i]+frag+t[j:]
open(p,'w',encoding='utf-8',newline='\n').write(t); print('ok', i, j, len(t))
