p='Screens/WATCHLIST RUN QUEUE.md'
L=open(p,encoding='utf-8').read().split('\n')
h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']; assert len(h)==1
e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]; assert len(e)==1
before=sum(1 for l in L[h[0]+1:e[0]] if l.startswith('- **'))
entry=open('Test Runs/_research 2026-09-26 ST/_reg_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L=L[:h[0]+1]+entry+L[h[0]+1:]
e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')][0]
sl=L[h[0]+1:e]
after=sum(1 for l in sl if l.startswith('- **'))
st=[l for l in sl if l.startswith('- **ST ')]
print('heading line',h[0]+1,'before',before,'after',after,'first',sl[0][:30],'ST entries',len(st))
assert after==before+1 and len(st)==1 and sl[0].startswith('- **ST ')
open(p,'w',encoding='utf-8').write('\n'.join(L))
