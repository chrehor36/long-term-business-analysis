import re,json,io
w=io.open('cfs_blocks.txt','w',encoding='utf-8')
for y in range(2003,2026):
    s=open(f'tenk_{y}.txt',encoding='utf-8').read()
    fs=re.sub(r'[|$\s]+',' ',s)
    fs=re.sub(r'\(\s*([\d,]+)\s*\)',r'(\1)',fs)
    best=None
    for m in re.finditer(r'Cash provided by operating activities (\(?[\d,]{4,}\)?) ',fs):
        pre=fs[max(0,m.start()-2500):m.start()]
        if re.search(r'Depreciation (\(?[\d,]+\)?) ',pre) and re.search(r'(?i)operating activities',pre):
            st=pre.rfind('Net income')
            end=fs.find('Cash and cash equivalents at end of year',m.start())
            if end<0: end=fs.find('at end of year',m.start())
            best=fs[max(0,m.start()-2500)+st:end+80]; break
    w.write(f'== {y}\n{best}\n\n')
w.close()
