import re
for y in range(2019,2025):
    L=open(f'tenk_{y}.txt',encoding='utf-8').read().split('\n')
    idx=[k for k,l in enumerate(L) if re.search(r'Revenues from customers',l)]
    for i in idx[:2]:
        s=' '.join(x.strip() for x in L[i-40:i+60] if x.strip() not in ('','|','$','%'))
        s=re.sub(r'\s+',' ',s)
        a=s.find('Year Ended'); 
        print('=====',y); print(s[max(0,a):a+900])
