import re
L=open(r'C:/Users/chreh/OneDrive/Documents/BRK/Screens/WATCHLIST RUN QUEUE.md',encoding='utf-8').read().split('\n')
h=[i for i,l in enumerate(L) if l=='## COMPLETED FROM THE QUEUE']
e=[i for i,l in enumerate(L) if l.startswith('## THE WRITE-EARLY PROTOCOL')]
assert len(h)==1 and len(e)==1, (h,e)
sl=L[h[0]+1:e[0]]
ent=[l for l in sl if l.startswith('- **')]
print('heading line',h[0]+1,'end',e[0]+1,'entries',len(ent))
print('first:',ent[0][:60]); 
tick=[re.match(r'- \*\*~?~?([A-Z0-9.\-]+)',l).group(1) if re.match(r'- \*\*~?~?([A-Z0-9.\-]+)',l) else '?' for l in ent]
from collections import Counter
print('dups',[k for k,v in Counter(tick).items() if v>1][:20])
print('WSM' in tick)
