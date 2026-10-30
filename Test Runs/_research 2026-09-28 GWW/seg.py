import glob,re
for y in range(2008,2021):
    fs=[f for f in glob.glob(f'cache/k{y}_*.txt') if ('10k' in f or 'gww-20' in f) and 'xex' not in f]
    if not fs: continue
    t=open(fs[0],encoding='utf-8').read()
    t=re.sub(r'[\s|$]+',' ',t)
    print('==',y)
    for lab in ['Total net sales','Net sales to external customers','Segment operating earnings \(losses\)','Segment operating earnings']:
        for m in list(re.finditer(lab+r'((?: \(?[\d,.]+\)?){2,5})',t))[-2:]:
            print('  ',lab,':',m.group(1)[:120])
