import glob,re,sys
sys.stdout.reconfigure(encoding='utf-8')
def table(s):
    idx=[m.start() for m in re.finditer(r'SEGMENT REPORTING|Segment Reporting|SEGMENT INFORMATION',s)]
    best=None
    for i in idx:
        seg=s[i:i+9000]
        if re.search(r'Technology',seg) and re.search(r'Financing',seg): best=i
    if best is None: return None
    t=s[best:best+8000]; t=re.sub(r'\s*\|\s*',' ',t); t=re.sub(r'\s+',' ',t)
    t=re.sub(r'\(\s*([\d,]+)\s*\)',r'-\1',t)
    return t
num=r'(-?[\d,]+|-)'
def row(t,label):
    m=re.search(re.escape(label)+r'\s*\$?\s*((?:\$?\s*-?[\d,]+\s*|\$?\s*-\s+){3,9})',t)
    if not m: return None
    vals=re.findall(r'-?[\d,]+|(?<=\s)-(?=\s)',' '+m.group(1)+' ')
    out=[]
    for v in vals:
        v=v.replace(',','')
        out.append(0 if v in('-','') else int(v))
    return out
labels=['Net sales','Total revenues','Sales of product and services','Cost of sales, products and services','Cost of sales, product and services','Operating income','Segment earnings','Earnings before provision for income taxes','Earnings before taxes','Total assets']
for p in sorted(glob.glob('cache/k_20*.txt')):
    s=open(p,encoding='utf-8').read(); t=table(s)
    if not t: print(p[8:18],'no table'); continue
    for l in labels:
        r=row(t,l)
        if r: print(p[8:18], l, r[:9])
