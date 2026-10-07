import re,sys
for y in sys.argv[1:]:
    s=open(f'cache/k{y}.txt',encoding='utf-8').read()
    s=re.sub(r'[\s|$]+',' ',s)
    m=re.search(r'Days available \d',s,re.I)
    if m:
        p=m.start(); st=s.rfind('Revenue',0,p-60); st=s.rfind('Revenue',0,st-5) if p-st<120 else st
        print('===',y,s[p-420:p+170]); print()
