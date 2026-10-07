import sys
RUN='../2026-09-27 Run - BUKS Butler National.md'
T=open('../_TEMPLATE - Company Run.md',encoding='utf-8').read().split('\n')
head=T[:T.index('## STEP 0 — THE RATE, AND THE FILING')]
head[0]='# Company Run — Butler National Corporation (BUKS) — 2026-09-27'
head.insert(1,'**WAVE 7, name 65 of 218 (the first name in the order file not in the done file; the done file held 64 lines, last BR). Claimed at dispatch 2026-09-27 by an unattended run agent (the template copied before any fetch, commit `bcef6137`).**')
bodies=[open(b,encoding='utf-8').read().rstrip('\n') for b in sys.argv[2:]]
nxt=sys.argv[1]  # heading of the first template section not yet written
rest=T[T.index(nxt):] if nxt!='-' else []
open(RUN,'w',encoding='utf-8').write('\n'.join(head)+'\n'+'\n\n'.join(bodies)+'\n'+('\n'.join(rest)+'\n' if rest else ''))
print('ok')
