import re
P='Screens/WATCHLIST RUN QUEUE.md'
raw=open(P,'rb').read()
crlf=b'\r\n' in raw
txt=raw.decode('utf-8')
L=txt.split('\r\n' if crlf else '\n')
h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']
assert len(h)==1, h
entry=open('Test Runs/_research 2026-09-28 OPXS/register_entry.md',encoding='utf-8').read().rstrip('\n').split('\n')
# insert first under the heading (the existing layout has the first entry on the next line)
L=L[:h[0]+1]+entry+L[h[0]+1:]
out=('\r\n' if crlf else '\n').join(L)
open(P,'wb').write(out.encode('utf-8'))
L2=out.split('\r\n' if crlf else '\n')
h2=[i for i,l in enumerate(L2) if l=='## COMPLETED FROM THE QUEUE']; w=[i for i,l in enumerate(L2) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
sl=L2[h2[0]+1:w[0]]
e=[l for l in sl if re.match(r'^- \*\*[A-Z0-9.\-]+ \(',l)]
print('crlf',crlf,'heading',h2[0]+1,'entries',len(e),'first',e[0][:40],'OPXS count',sum(1 for l in e if l.startswith('- **OPXS ')),'second',e[1][:30])
