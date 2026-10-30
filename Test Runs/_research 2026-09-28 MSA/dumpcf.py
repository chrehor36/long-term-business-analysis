import re,io
out=open('cf_statements.txt','w',encoding='utf-8')
for y in range(1993,2026):
    L=open(f'cache/k{y}.txt',encoding='utf-8',errors='ignore').read().split('\n')
    idx=[i for i,l in enumerate(L) if re.search(r'STATEMENTS? OF CASH FLOWS?',l,re.I) and len(l)<200]
    # choose the heading followed within 15 lines by 'Operating Activities'
    pick=None
    for i in idx:
        if any(re.search(r'operating activities',x,re.I) for x in L[i:i+60]): pick=i
    out.write(f'\n######## FY{y} (heading candidates {len(idx)}, picked {pick})\n')
    if pick is None: continue
    for l in L[pick:pick+420]:
        out.write(l[:260].rstrip()+'\n')
