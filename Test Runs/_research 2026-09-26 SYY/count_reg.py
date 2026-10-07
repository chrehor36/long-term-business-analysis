import re
L=open('../../Screens/WATCHLIST RUN QUEUE.md',encoding='utf-8').read().split('\n')
h=[i for i,l in enumerate(L) if l.rstrip()=='## COMPLETED FROM THE QUEUE']
e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(h)==1 and len(e)==1, (h,e)
s=L[h[0]+1:e[0]]
ent=[l for l in s if re.match(r'^- \*\*',l)]
print('heading line',h[0]+1,'end line',e[0]+1,'entries',len(ent))
print('first:',ent[0][:90]); print('second:',ent[1][:90])
import collections
names=[re.match(r'^- \*\*([A-Z.\-]+)',l).group(1) if re.match(r'^- \*\*([A-Z.\-]+)',l) else '?' for l in ent]
print('SYY entries:',names.count('SYY'))
