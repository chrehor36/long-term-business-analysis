import re,sys
for y in sys.argv[1:]:
    L=open(f'cache/k{y}.txt',encoding='utf-8').read().split('\n')
    idx=[i for i,l in enumerate(L) if re.search(r'^\s*(ROV )?Days available',l,re.I)]
    if not idx: print(y,'none'); continue
    i=idx[0]
    s=' '.join(L[i-40:i+14]); s=re.sub(r'\s+',' ',s)
    print('===',y, s[-2200:]); print()
