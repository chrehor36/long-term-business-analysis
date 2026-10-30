import re
for y in range(2014,2026):
    L=open(f'cache/t{y}.txt',encoding='utf-8').read().split('\n')
    idx=[i for i,l in enumerate(L) if re.search(r'(?i)^\s*(CONSOLIDATED|COMBINED AND CONSOLIDATED|CONSOLIDATED AND COMBINED) STATEMENTS? OF OPERATIONS\s*$',l)]
    if not idx: print(y,'NOTFOUND'); continue
    i=idx[0]; print('=====',y)
    for l in L[i:i+40]:
        if '|' in l: print('  ',l[:160])
        if l.startswith('Net income |') or l.startswith('Net income (loss) |'): break
