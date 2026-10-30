import re,sys
def norm(s):
    s=s.replace('\n',' ')
    s=re.sub(r'\(\s*([\d,\.]+)\s*\|?\s*\)',r'(\1)',s)
    s=re.sub(r'[|\s]+',' ',s)
    return s
labels=[r'Net cash provided by operating activities',r'Share-based compensation',r'Additions to property, plant and equipment and capitalized software',r'Depreciation',r'Amortization of intangible assets',r'Acquisition[s]? of [^()]{0,80}?net of cash[^()0-9]{0,20}',r'Payments on capitali[sz]ed lease[^0-9(]*|Payments (on|of) finance lease[^0-9(]*|Payments on capital lease[^0-9(]*',r'Proceeds from (the )?sale of business[^0-9(]*|Proceeds from the sale of [^0-9(]{0,60}',r'Cash paid for interest',r'Cash paid for income taxes',r'Purchase of noncontrolling interest[^0-9(]*',r'Payments to repurchase ordinary shares',r'Excess tax benefit[^0-9(]*',r'Payments of employee restricted stock tax withholdings']
for fy in range(2010,2026):
    s=norm(open(f'10-K_FY{fy}.txt',encoding='utf-8').read())
    i=[m.start() for m in re.finditer(r'Consolidated Statements of Cash Flows \(',s)]
    if not i: i=[m.start() for m in re.finditer(r'Consolidated Statements of Cash Flows',s)]
    # choose the occurrence followed by 'Cash flows from operating activities' within 800 chars
    st=None
    for k in i:
        if 'Cash flows from operating activities' in s[k:k+800]: st=k
    seg=s[st:st+9000] if st else ''
    print('=====',fy, 'found' if st else 'NOTFOUND')
    for L in labels:
        m=re.search(L,seg)
        if m: print('  ',m.group(0)[:70].strip(),'=>',seg[m.end():m.end()+60])
