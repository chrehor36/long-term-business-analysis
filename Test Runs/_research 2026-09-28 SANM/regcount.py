import re,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
L=open('Screens/WATCHLIST RUN QUEUE.md',encoding='utf-8').read().split('\n')
h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']; assert len(h)==1,h
e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]; assert len(e)==1
sl=L[h[0]+1:e[0]]
ent=[l for l in sl if re.match(r'^- \*\*[A-Z0-9.\-]+ \(',l)]
print('heading line',h[0]+1,'entries',len(ent))
print('first 3:',[x[:40] for x in ent[:3]])
print('SANM entries:',sum(1 for x in ent if x.startswith('- **SANM (')))
