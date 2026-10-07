# assemble the run file: template header + fragments + template tail from a marker
import sys
T=open('../_TEMPLATE - Company Run.md',encoding='utf-8').read()
frags=sys.argv[1].split(',')
marker=sys.argv[2] if len(sys.argv)>2 else None
head=T[:T.index('## STEP 0')]
head=head.replace('# Company Run — [COMPANY] ([TICKER]) — [DATE]','# Company Run — Bio-Techne Corporation (TECH) — 2026-09-28')
body=''.join(open(f,encoding='utf-8').read().rstrip('\n')+'\n\n' for f in frags)
tail=T[T.index(marker):] if marker else ''
open('../2026-09-28 Run - TECH Bio-Techne.md','w',encoding='utf-8').write(head+body+tail)
print('ok', len(head+body+tail))
