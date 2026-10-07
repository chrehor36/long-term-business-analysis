import re,sys
labels=[r'^Net sales',r'^Cost of products sold',r'^Gross profit',r'^Selling and administrative',r'^Advertising costs',r'^Research and development',r'^Interest expense',r'^Earnings (from continuing operations )?before income taxes',r'^Net earnings',r'^Depreciation and amortization',r'^Stock-based compensation',r'^Net cash provided by (continuing )?operations',r'^Capital expenditures',r'^Businesses acquired',r'^Business(es)? acquired',r'^Proceeds from',r'^Treasury stock purchased',r'^Cash dividends paid',r'^Income taxes paid',r'^Goodwill, trademark and other asset impairments',r'^Loss on divestiture',r'^Pension settlement',r'^Venture agreement']
f=sys.argv[1]
L=[re.sub(r'\s+',' ',l).strip() for l in open(f,encoding='utf-8').read().split('\n')]
# find statement pages
for key in ['CONSOLIDATED STATEMENTS OF EARNINGS','CONSOLIDATED STATEMENTS OF CASH FLOWS']:
    idx=[i for i,l in enumerate(L) if l.upper().startswith(key) or l.upper()==key]
    if not idx: idx=[i for i,l in enumerate(L) if key in l.upper()]
    i0=idx[-1] if key.endswith('FLOWS') else idx[0]
    # prefer the one followed by 'The Clorox Company' within 3 lines
    for i in idx:
        if any('Clorox' in L[k] for k in range(i,min(i+4,len(L)))): i0=i;break
    print('##',key,i0)
    buf=L[i0:i0+160]
    j=0
    while j<len(buf):
        l=buf[j]
        for lab in labels:
            if re.match(lab,l):
                # join following lines if values on next lines
                s=l
                k=j+1
                while k<len(buf) and len(s)<400 and (re.match(r'^[\|\$\(\)\d,\.\s—-]*$',buf[k]) ):
                    s+=' '+buf[k];k+=1
                print('   ',s[:300])
                break
        j+=1
