import re,json,sys
LABELS={'ocf':r'Net cash provided by operating activities','sbc':r'Share-based compensation expense','da':r'Depreciation and amortization',
 'capex':r'Additions to plant and equipment','proc':r'Proceeds from sales of plant and equipment','acq':r'Acquisition[s]? of businesses, net of cash acquired',
 'rec':r'(?:\(Increase\) decrease|Decrease \(increase\)|Increase|Decrease|\(Increase\)) in receivables','inv':r'(?:\(Increase\) decrease|Decrease \([Ii]ncrease\)|\(Increase\)|Increase|Decrease) in inventories',
 'pre':r'(?:\(Increase\) decrease|Decrease \(increase\)|Increase|Decrease)[^|]{0,15} in prepaid expenses and other current assets','ap':r'(?:Increase \(decrease\)|\(Decrease\) increase|Increase|Decrease)[^|]{0,5} in accounts payable',
 'acc':r'(?:Increase \(decrease\)|\(Decrease\) increase|Increase|Decrease)[^|]{0,5} in accrued expenses','ni':r'Net earnings'}
def nums(s,k=3):
    s=s.replace('—',' 0 ')
    toks=re.findall(r'\(\s*[\d,]+\s*\)?|[\d,]{1,}(?:\.\d+)?',s)
    out=[]
    for t in toks:
        neg='(' in t
        v=t.replace('(','').replace(')','').replace(',','').strip()
        if not v or not re.match(r'^\d+(\.\d+)?$',v): continue
        out.append(-float(v) if neg else float(v))
        if len(out)==k: break
    return out
def parse(fy):
    t=open(f'tenk_FY{fy}.txt',encoding='utf-8').read()
    idx=[m.start() for m in re.finditer(r'(?i)cash flows from operating activities:',t)]
    best=None
    for i in idx:
        w=t[i-800:i+30000]
        if re.search(LABELS['ocf'],w) and re.search(LABELS['capex'],w) and re.search(r'Share-based compensation',w): best=i-800
    w=t[best:best+30000]; w=re.sub(r'\s*\|\s*',' ',w); w=re.sub(r'\$',' ',w); w=re.sub(r'\s+',' ',w)
    thousands='thousands' in w[:900]
    res={}
    for k,lab in LABELS.items():
        m=re.search(lab,w)
        if not m: res[k]=None; continue
        v=nums(w[m.end():m.end()+200])
        res[k]=[x/1000 if thousands else x for x in v]
    return res
if __name__=='__main__':
    out={}
    for fy in sys.argv[1:]:
        r=parse(int(fy)); out[fy]=r; print(fy, json.dumps(r))
    json.dump(out,open('cf_parsed.json','w'),indent=1)
