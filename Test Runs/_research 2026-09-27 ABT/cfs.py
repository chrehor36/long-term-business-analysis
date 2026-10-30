import re,sys
sys.stdout.reconfigure(encoding='utf-8')
for y in map(int,sys.argv[1:]):
    t=open(f'cache/tenk_{y}.txt',encoding='utf-8').read()
    t=re.sub(r'[​\xa0]',' ',t)
    t=re.sub(r'\n\s*(\||\$|\)|\()',r' \1',t)   # rejoin broken cells
    lines=[re.sub(r'[\s|]+',' ',l).strip() for l in t.split('\n')]
    # locate operating section
    idx=[i for i,l in enumerate(lines) if l.startswith('Cash Flow From (Used in) Operating Activities')]
    if not idx: print(y,'not found'); continue
    i=idx[0]
    print('=====',y)
    for l in lines[i:i+80]:
        if re.search(r'Net earnings|Depreciation|Amortization|Share-based|Stock|Net Cash From|Acquisitions of property|Acquisitions of businesses|contingent|Contingent|Dividends paid|Purchases of common|Other|pension|Pension|Proceeds from business|Income taxes paid|Interest paid|Trade|Inventories|Income taxes',l):
            print('  ',l[:230])
        if l.startswith('Supplemental') : pass
