import re,sys
for y in range(2012,2025):
    L=open(f'tenk_{y}.txt',encoding='utf-8').read().split('\n')
    i=[k for k,l in enumerate(L) if re.search(r'(?i)professional services operating income',l)][0]
    j=[k for k,l in enumerate(L) if re.search(r'(?i)aerospace products operating income',l)][0]
    def J(a,b): 
        s=' '.join(x.strip() for x in L[a:b] if x.strip() not in ('','|','$','%'))
        return re.sub(r'\s+',' ',s)
    print('=====',y); print(J(i-60,i+12)[-900:]); print('--'); print(J(j-50,j+12)[-700:])
