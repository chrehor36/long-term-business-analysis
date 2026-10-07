import re,sys
sys.stdout.reconfigure(encoding='utf-8')
labels=['option','Stock','Restricted','Warrant','Net income','Net cash flows provided by operating activities','Net cash provided by operating activities','Deferred compensation plan','Stock compensation expense','Stock-based compensation','ESPP discount','Issuance of common shares as compensation','Depreciation and amortization','Purchases of property, plant','Purchases of property','Accounts payable','Customer prepayments','Acquisition','Issuance of common shares to fund','Treasury shares','Purchase of treasury','Proceeds from stock option','Goodwill impairment','Impairment of goodwill','Goodwill and intangible asset impairment']
for f in sys.argv[1:]:
    L=open(f,encoding='utf-8').read().split('\n')
    idx=[i for i,x in enumerate(L) if re.search(r'STATEMENTS OF CASH FLOWS',x)]
    if not idx: print(f,'no cfs'); continue
    a=idx[-1] if len(idx)<3 else idx[1]
    # pick the occurrence followed by 'Operating Activities' within 20 lines
    for i in idx:
        if any('perating' in L[k] for k in range(i,min(i+25,len(L)))) and any(re.search(r'\d{1,3},\d{3}',L[k]) for k in range(i,min(i+60,len(L)))): a=i
    seg=L[a:a+700]
    out=[];cur=None;vals=[]
    txt=[]
    for x in seg:
        s=x.strip().strip('|').strip()
        if not s or s in ('$','(',')','​'): 
            if s in ('(',): vals.append('(')
            continue
        m=re.fullmatch(r'\(?\s*[\d,]+\s*\)?|-|—|–',s.replace('$','').strip())
        if m and cur is not None:
            vals.append(s.replace('$','').strip())
        else:
            if cur is not None: txt.append((cur,' '.join(vals)))
            cur=s;vals=[]
        if 'end of' in s.lower() and 'period' in s.lower(): break
    print('==',f,'line',a+1)
    for c,v in txt:
        if any(c.startswith(l) or l.lower() in c.lower() for l in labels): print('  ',c[:90],'|',v)
