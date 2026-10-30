import re,sys,glob
for f in sorted(glob.glob('tenk_20*.txt')):
    L=open(f,encoding='utf-8').read().split('\n')
    idx=[i for i,l in enumerate(L) if re.search(r'(?i)statements? of cash flows',l) and 'for the years' not in l.lower()[:0]]
    # take the occurrence followed within 15 lines by 'OPERATING ACTIVITIES'
    start=None
    for i in idx:
        if any('OPERATING ACTIVITIES' in x.upper() for x in L[i:i+15]): start=i
    if start is None: print(f,'NOTFOUND'); continue
    chunk=[x.strip() for x in L[start:start+400] if x.strip() not in ('','|')]
    s=' '.join(chunk); s=re.sub(r'\s+',' ',s)
    end=s.upper().find('NOTES TO CONSOLIDATED')
    s=s[:end if end>0 else 6000]
    s=re.sub(r'\( ?([\d,]+) ?\|? ?\)',r'(\1)',s)
    open('cfs_'+f[5:9]+'.txt','w',encoding='utf-8').write(s)
    print(f, len(s))
