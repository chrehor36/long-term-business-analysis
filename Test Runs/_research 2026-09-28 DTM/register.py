import re,sys
p='Screens/WATCHLIST RUN QUEUE.md'
L=open(p,encoding='utf-8').read().split('\n')
H='## COMPLETED FROM THE QUEUE'; W='## THE WRITE-EARLY PROTOCOL'
hi=[i for i,l in enumerate(L) if l.rstrip()==H]
wi=[i for i,l in enumerate(L) if l.startswith(W)]
assert len(hi)==1 and len(wi)==1, (hi,wi)
h,w=hi[0],wi[0]
def count(L,h,w): return sum(1 for l in L[h+1:w] if l.startswith('- **'))
def tick(L,h,w): return [l for l in L[h+1:w] if l.startswith('- **DTM ')]
before=count(L,h,w)
print('heading line',h+1,'write-early line',w+1,'entries before',before,'DTM already',len(tick(L,h,w)))
if sys.argv[1:]==['write']:
    assert not tick(L,h,w)
    e=open('Test Runs/_research 2026-09-28 DTM/register_entry.md',encoding='utf-8').read().rstrip('\n')
    e=e.replace('__N__',str(before+1)).replace('__B__',str(before)).replace('__L__',str(h+1))
    L=L[:h+1]+e.split('\n')+L[h+1:]
    open(p,'w',encoding='utf-8').write('\n'.join(L))
    L2=open(p,encoding='utf-8').read().split('\n')
    h2=[i for i,l in enumerate(L2) if l.rstrip()==H][0]; w2=[i for i,l in enumerate(L2) if l.startswith(W)][0]
    first=[l for l in L2[h2+1:w2] if l.startswith('- **')][0]
    print('after',count(L2,h2,w2),'first:',first[:60],'DTM count',len(tick(L2,h2,w2)))
