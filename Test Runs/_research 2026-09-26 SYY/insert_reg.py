p='../../Screens/WATCHLIST RUN QUEUE.md'
raw=open(p,'rb').read()
crlf=b'\r\n' in raw[:5000]
t=raw.decode('utf-8')
nl='\r\n' if crlf else '\n'
L=t.split(nl)
h=[i for i,l in enumerate(L) if l.rstrip()=='## COMPLETED FROM THE QUEUE']
assert len(h)==1, h
new=open('register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
L[h[0]+1:h[0]+1]=new
# wave progress line is inside the entry itself; nothing else to change
open(p,'wb').write(nl.join(L).encode('utf-8'))
print('inserted after line',h[0]+1,'crlf',crlf)
