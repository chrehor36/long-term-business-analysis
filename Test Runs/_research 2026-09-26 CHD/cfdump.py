import re,glob
out=open('cf_blocks.txt','w',encoding='utf-8')
for f in sorted(glob.glob('tenk_20*.txt')):
    raw=open(f,encoding='utf-8').read().split('\n')
    idx=[i for i,x in enumerate(raw) if re.search(r'STATEMENTS? OF CASH FLOWS?',x,re.I) and 'continued' not in x.lower()]
    # pick the first occurrence followed within 60 lines by 'Net Income' or 'Net income'
    best=None
    for i in idx:
        win=' '.join(raw[i:i+80])
        if re.search(r'Net (I|i)ncome',win) and re.search(r'Depreciation',' '.join(raw[i:i+200])):
            best=i;break
    if best is None: out.write(f'#### {f} NOT FOUND\n'); continue
    L=[re.sub(r'\s*\|\s*$','',x.strip()) for x in raw[best:best+900]]
    L=[x for x in L if x not in ('','|','$')]
    txt=' '.join(L); txt=re.sub(r'\s*\|\s*',' ',txt)
    txt=re.sub(r'\(\s*([\d,.]+)\s*\)',r'(\1)',txt)
    k=txt.find('Cash and cash equivalents at end'); 
    if k<0: k=txt.lower().find('cash and cash equivalents at end')
    out.write(f'#### {f} line {best}\n'+txt[:(k+300 if k>0 else 9000)]+'\n')
out.close()
