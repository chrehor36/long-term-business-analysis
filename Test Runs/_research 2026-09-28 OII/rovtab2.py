import re,sys
for y in sys.argv[1:]:
    s=open(f'cache/k{y}.txt',encoding='utf-8').read()
    s=re.sub(r'[\s|]+',' ',s)
    m=[x.start() for x in re.finditer(r'Days available',s,re.I)]
    # choose the occurrence followed by 'Utilization'
    for p in m:
        seg=s[p:p+400]
        if re.search('utiliz',seg,re.I):
            st=s.rfind('Revenue',0,p-50)
            st=s.rfind('ROV',0,p-600)
            print('===',y,s[p-700:p+330]); print(); break
