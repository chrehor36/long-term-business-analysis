import re,glob
num=r'\(?\s*[\d,]+\s*\|?\s*\)?'
def grab(t,label,seg):
    # find "label ... seg | $ | a | $ | b | $ | c"
    i=t.find(label)
    if i<0: return None
    w=t[i:i+1500]
    m=re.search(re.escape(seg)+r'\s*\|\s*\$?\s*\|?\s*([\(\d,]+)[\s|)]*\$?\s*\|?\s*([\(\d,]+)[\s|)]*\$?\s*\|?\s*([\(\d,]+)',w)
    if not m: return None
    f=lambda x: -float(x.strip('(').replace(',','')) if x.startswith('(') else float(x.replace(',',''))
    return [f(x) for x in m.groups()]
for fn in sorted(glob.glob('k/*_10-K_*.txt')):
    t=open(fn,encoding='utf-8').read().replace('\n',' | ')
    fy=fn.split('/')[-1][:4]
    r={}
    for lab in ['Operating Income:','Assets:','Capital Expenditures:','Depreciation and Amortization:']:
        r[lab]={s:grab(t,lab,s) for s in ['Food Service','Retail Supermarket','Frozen Beverages']}
    print(fy, {k:{s:v for s,v in d.items()} for k,d in r.items()})
