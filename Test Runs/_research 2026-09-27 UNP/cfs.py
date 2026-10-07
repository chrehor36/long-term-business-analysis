import re,json
LABELS={'ocf':r'Cash provided by operating activities','dep':r'Depreciation','capex':r'Capital investments','sbc':r'(?:Stock|Share)-based compensation(?: expense)?','ni':r'Net income','assets':r'Proceeds from asset sales','other_inv':r'Other investing activities, net','acq':r'Acquisitions?(?: of [A-Za-z ,.]{0,40})?(?:, net of cash acquired)?','buyback':r'Share repurchase programs?|Common shares repurchased|Common share repurchase programs?','pension':r'Cash paid to fund pension plan|Pension and postretirement contributions?'}
num=r'\(?\s*-?[\d,]+\s*\)?'
out={}
for y in range(2003,2026):
    s=open(f'tenk_{y}.txt',encoding='utf-8').read()
    idx=[m.start() for m in re.finditer(r'(?i)CONSOLIDATED STATEMENTS? OF CASH FLOWS',s)]
    blk=None
    for i in idx:
        seg=s[i:i+14000]
        fs=re.sub(r'[|$\s]+',' ',seg)
        if re.search(r'Cash provided by operating activities [\d,]{4,}',fs) and re.search(r'(?i)investing activities',fs):
            blk=seg; break
    if blk is None: print(y,'no block'); continue
    f=re.sub(r'[|$\s]+',' ',blk)
    f=re.sub(r'\(\s*([\d,]+)\s*\)',r'(\1)',f)
    rec={}
    for k,lab in LABELS.items():
        m=re.search(r'(?:'+lab+r')\s*(?:\[\w\])?\s*((?:'+num+r'|-)\s+(?:'+num+r'|-)\s+(?:'+num+r'|-))',f)
        if m:
            vals=[]
            for t in m.group(1).split():
                if t=='-': vals.append(0); continue
                neg=t.startswith('('); v=int(t.strip('()').replace(',',''))
                vals.append(-v if neg else v)
            rec[k]=vals
    out[y]=rec
    print(y,rec)
json.dump(out,open('cfs_raw.json','w'),indent=0)
