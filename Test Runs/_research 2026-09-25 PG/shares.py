import re,sys
for y in [2016,2017,2018,2019,2020,2026]:
    t=open(f'tenk_FY{y}.txt',encoding='utf-8').read()
    t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    seg=sorted(set(re.findall(r'Global market share of the [A-Za-z,& ]{3,40} segment [^.]{0,60}\.',t)))
    print('== FY',y,'segment share sentences:',len(seg))
    for s in seg: print('  ',s)
    if y in (2017,2020,2026):
        for s in re.findall(r'[^.]{0,200}(?:global market share|market share position|global market leader)[^.]{0,200}\.',t)[:14]:
            print('   *',s.strip()[:330])
