import re,sys
sys.path.insert(0,'.')
from cond import condense
sys.stdout.reconfigure(encoding='utf-8')
fn=sys.argv[1]
L=open(fn,encoding='utf-8').read().split('\n')
hits=[i for i,l in enumerate(L) if re.search(r'(?i)cash flows? from operating activities',l)]
for i in hits:
    if any(re.search(r'(?i)depreciation',x) for x in L[i:i+15]):
        j=i
        while j<len(L) and not re.search(r'(?i)see accompanying notes|the accompanying notes',L[j]): j+=1
        for x in condense(L[i-6:j]): print(x)
        break
