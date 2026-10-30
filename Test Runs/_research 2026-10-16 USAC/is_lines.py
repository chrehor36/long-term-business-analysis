import re,sys
pats=[r'Total revenues',r'Impairment of goodwill',r'Impairment of compression equipment',r'Impairment of assets',r'Operating income \(loss\)',r'Operating income',r'Interest expense, net']
for y in sys.argv[1:]:
    s=re.sub(r'\s+',' ',open(f'cache/k{y}.txt',encoding='utf-8').read())
    i=s.find('Consolidated Statements of Operations',s.find('REGISTERED PUBLIC ACCOUNTING FIRM'))
    seg=s[i:i+9000]
    print('==',y)
    for p in pats:
        m=re.search(p+r' ?\|?([ |$()0-9,.-]{5,90})',seg)
        if m: print('  ',p, re.sub(r'[ |$]+',' ',m.group(1))[:80])
