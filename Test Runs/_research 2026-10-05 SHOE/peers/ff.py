import re,sys,glob
for f in sorted(glob.glob('CAL_FY*.txt')):
    s=open(f,encoding='utf-8').read(); s=re.sub(r'\s*\|\s*',' ',s); s=re.sub(r'\s+',' ',s)
    print('==',f)
    hits=[m.start() for m in re.finditer(r'FAMOUS FOOTWEAR',s)]
    for h in hits:
        seg=s[h:h+1500]
        if re.search(r'(?i)net sales',seg[:300]) and re.search(r'(?i)operating (earnings|income|loss)',seg):
            print(seg[:1400]); print('--'); break
