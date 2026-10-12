# splice.py DRAFT START_MARKER END_MARKER : replace run-file text from START (or file start if '^') up to END with DRAFT
import sys
p="../2026-10-12 Run - ABG Asbury Automotive.md"
s=open(p,encoding='utf-8').read(); d=open(sys.argv[1],encoding='utf-8').read()
a=0 if sys.argv[2]=='^' else s.index(sys.argv[2]); b=s.index(sys.argv[3])
open(p,'w',encoding='utf-8').write(s[:a]+d+s[b:]); print('ok',a,b)
