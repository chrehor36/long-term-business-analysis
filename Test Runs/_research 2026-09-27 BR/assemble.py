# Assemble the run file: header + template verdict box + bodies + remaining template (from the first heading not yet written)
import sys,io,os
T=open('../_TEMPLATE - Company Run.md',encoding='utf-8').read().split('\n')
hdr=['# Company Run — Broadridge Financial Solutions, Inc. (BR) — 2026-09-27',
'**WAVE 7 (the first name in the order file not in the done file; the done file held 63 lines, last NGVC). Claimed at dispatch 2026-09-27 by an unattended run agent (the template copied before any fetch, commit `3750b010`).**']
# template lines index: find markers
def idx(s):
    for i,l in enumerate(T):
        if l.startswith(s): return i
    raise SystemExit(s)
box=T[1:idx('## STEP 0')-1]   # lines after title through the verdict box, excluding '---' before step0
bodies=[open(b,encoding='utf-8').read().rstrip('\n') for b in sys.argv[2:]]
rest=T[idx(sys.argv[1]):] if sys.argv[1]!='NONE' else []
out='\n'.join(hdr+box)+'\n'+'\n'.join(bodies)+'\n'+('\n'.join(rest) if rest else '')
open('../2026-09-27 Run - BR Broadridge.md','w',encoding='utf-8').write(out)
print(len(out.split('\n')),'lines')
