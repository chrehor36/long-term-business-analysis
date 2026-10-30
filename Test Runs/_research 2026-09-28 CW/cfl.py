import re
for yr in range(2010,2026):
    t=open(f'cache/k{yr}.txt',encoding='utf-8').read().splitlines()
    idx=[i for i,l in enumerate(t) if re.search(r'CONSOLIDATED STATEMENTS? OF CASH FLOWS',l,re.I)]
    # choose the index whose following lines contain 'operating activities'
    s=None
    for i in idx:
        if any("perating activities" in x for x in t[i:i+8]) and any(re.search("^Net (earnings|income)",x) for x in t[i:i+8]): s=i; break
    print('#'*20, yr, idx[:5], s)
    if s is None: continue
    for l in t[s:s+70]:
        print(l[:200])
        if re.search(r'end of (the )?(year|period)',l,re.I): break
