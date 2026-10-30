import re
names = ['Flow Control','Motion Control','Metal Treatment','Commercial/Industrial','Defense','Power','Aerospace & Industrial','Defense Electronics','Naval & Power','Energy','Controls','Surface Technologies','Total segments','Total segment','Corporate and eliminations','Corporate and other','Total operating income','Total net sales','Total sales']
for yr in range(2010, 2026):
    t = open(f'cache/k{yr}.txt', encoding='utf-8').read().splitlines()
    print('#' * 10, yr)
    # the MD&A summary table: first block containing 'Sales:' followed by segment lines and 'Operating income:'
    for i, l in enumerate(t):
        if re.match(r'^\s*Sales:?\s*$', l) and any(re.match(r'^\s*Operating income:?', x) for x in t[i:i+12]):
            for x in t[i-3:i+22]: print('  ', x[:170])
            break
