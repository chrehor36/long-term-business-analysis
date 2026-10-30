import re
S={'2009':3528,'2010':3752,'2011':3784,'2012':8039,'2013':10287}
for y,st in S.items():
    L=open('tenk_'+y+'.txt',encoding='utf-8').read().split('\n')
    chunk=[x.strip() for x in L[st-12:st+420] if x.strip() not in ('','|')]
    s=re.sub(r'\s+',' ',' '.join(chunk))
    end=s.upper().find('NOTES TO CONSOLIDATED')
    s=s[:end if end>0 else 7000]
    s=re.sub(r'\( ?([\d,]+) ?\|? ?\)',r'(\1)',s)
    open('cfs_'+y+'.txt','w',encoding='utf-8').write(s); print(y,len(s))
