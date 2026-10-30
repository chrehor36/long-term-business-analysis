import re,sys,io,json
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
LAB={'ni':r'Net earnings\b','da':r'Depreciation and amortization\b','acqam':r'Amortization of acquired intangibles[^|]*','otham':r'Amortization of other assets','sbc':r'Stock-based compensation expense',
'onca':r'Increase in Other non-current assets|Other non-current assets','ocf':r'Net cash flows? provided by operating activities(?! from discontinued)[^|]*','capex':r'Capital expenditures','soft':r'Software purchases[^|]*|Purchases of intangibles',
'acq':r'Acquisitions, net of cash acquired|Acquisitions of businesses[^|]*','ipp':r'Purchase of intellectual property','div':r'Dividends paid','buy':r'Purchases? of Treasury stock','opt':r'Proceeds from exercise of stock options'}
NUM=r'\(?\s*[\d,]+\.\d\s*(?:\|\s*)?\)?|—|�|–'
res=json.load(open('cfs.json'))
for fy in range(2007,2020):
    t=open(f'tenk_{fy}.txt',encoding='utf-8',errors='replace').read()
    t=re.sub(r'\s+',' ',t)
    # locate statement: 'Cash Flows From Operating Activities' followed within 300 chars by 'Net earnings'
    cands=[m.start() for m in re.finditer(r'Cash Flows? (From|from) Operating Activities',t) if re.search(r'Net earnings',t[m.start():m.start()+400])]
    if not cands: print(fy,'none'); continue
    s=t[cands[0]:cands[0]+9000]
    got={}
    for k,p in LAB.items():
        m=re.search(r'(?:'+p+r')[\s|$]*((?:(?:'+NUM+r')[\s|$]*){3})',s)
        if not m: continue
        vals=[]
        for x in re.findall(NUM,m.group(1)):
            if x in ('—','�','–'): vals.append(0.0)
            else:
                v=float(re.sub(r'[^\d.]','',x)); vals.append(-v if '(' in x else v)
        got[k]=vals[:3]
    res[str(fy)]=got
    print(fy,got)
json.dump(res,open('cfs.json','w'),indent=0)
