"""Parse the filed cash-flow statement of every BR 10-K (fiscal 2007-2026). Newest filed vintage per fiscal year kept, all vintages printed."""
import re,sys,io,json
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
LAB={'ocf':r'Net cash flows? (provided by|from) operating activities|Net cash provided by operating activities|Net cash flows from operating activities',
'da':r'^Depreciation and amortization\b','acqam':r'^Amortization of acquired intangibles','otham':r'^Amortization of other assets','sbc':r'^Stock-based compensation',
'capex':r'^Capital expenditures','soft':r'^Software purchases','acq':r'^Acquisitions, net of cash acquired|^Acquisitions of businesses|^Acquisition',
'ipp':r'^Purchase of intellectual property','onca':r'Other non-current assets|Increase in Other non-current assets','ni':r'^Net earnings\b','div':r'^Dividends paid','buy':r'^Purchases of Treasury stock','opt':r'^Proceeds from exercise of stock options','cfo_cont':r'Net cash flows provided by operating activities from continuing'}
def nums(s):
    s=s.replace('�','—')
    out=[]
    for m in re.finditer(r'\(\s*([\d,]+\.?\d*)\s*\)|([\d,]+\.\d+|\d{1,3}(?:,\d{3})+|\d+)|—|–',s):
        if m.group(1): out.append(-float(m.group(1).replace(',','')))
        elif m.group(2): out.append(float(m.group(2).replace(',','')))
        else: out.append(0.0)
    return out
res={}
for fy in range(2007,2027):
    txt=open(f'tenk_{fy}.txt',encoding='utf-8',errors='replace').read()
    txt=txt.replace('\n|','|')
    L=[re.sub(r'\s+',' ',l).strip() for l in txt.split('\n')]
    starts=[k for k,l in enumerate(L) if re.search(r'Statements? of Cash Flows',l,re.I)]
    blk=None
    for k in starts:
        seg=L[k:k+120]
        if any(re.match(r'Net earnings',x) for x in seg[:25]) and any(re.search(LAB['capex'],x) for x in seg): blk=seg; break
    if not blk: print(fy,'NO BLOCK'); continue
    got={}
    for l in blk:
        for key,pat in LAB.items():
            if key in got: continue
            if re.search(pat,l):
                n=[x for x in nums(re.sub(r'^[^|]*?(\||$)','',l,1)) ]
                n=[x for x in n if not (x in (1.0,2.0,3.0) )] if False else n
                if len(n)>=3: got[key]=n[-3:]
    res[fy]=got
    print(fy, {k:v for k,v in got.items()})
json.dump(res,open('cfs.json','w'),indent=0)
