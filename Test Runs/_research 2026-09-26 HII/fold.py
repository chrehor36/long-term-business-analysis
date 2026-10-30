import re,io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
Q='../../Screens/WATCHLIST RUN QUEUE.md'
raw=open(Q,'rb').read(); crlf=b'\r\n' in raw[:5000]
t=raw.decode('utf-8'); nl='\r\n' if crlf else '\n'
L=t.split(nl)
H=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']; assert len(H)==1,H
W=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]; assert len(W)==1
h,w=H[0],W[0]
def count(L,h,w): return sum(1 for l in L[h+1:w] if l.startswith('- **'))
before=count(L,h,w)
dup=[l for l in L[h+1:w] if l.startswith('- **HII ')]; assert not dup
e=open('_reg_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
e=[x.replace('@@COUNT@@',str(before+1)).replace('@@BEFORE@@',str(before)).replace('@@LINE@@',str(h+1)) for x in e]
L2=L[:h+1]+e+L[h+1:]
H2=[i for i,l in enumerate(L2) if l=='## COMPLETED FROM THE QUEUE']; W2=[i for i,l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
after=count(L2,H2[0],W2[0])
first=L2[H2[0]+1][:40]
print('heading line',h+1,'before',before,'after',after,'first',first,'crlf',crlf)
assert after==before+1 and first.startswith('- **HII ')
open(Q,'wb').write(nl.join(L2).encode('utf-8'))
