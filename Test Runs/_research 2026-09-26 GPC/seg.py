import re,sys
for y in sys.argv[1:]:
    s=open(f'tenk_{y}-12-31.txt',encoding='utf-8').read()
    s=re.sub(r'[\s|]+',' ',s)
    for key in ['Net sales:','Operating profit:','Identifiable assets:','Assets:']:
        idx=[m.start() for m in re.finditer(re.escape(key),s)]
        for i in idx[-2:]:
            print(y,key,'::',s[i:i+700]); print()
