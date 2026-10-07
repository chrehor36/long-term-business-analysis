import re,sys,json
sys.stdout.reconfigure(encoding='utf-8')
def doc(y):
    f=f'cache/x13_{y}.txt' if y<=2014 else f'cache/k_{y}.txt'
    return open(f,encoding='utf-8').read()
LAB={'ocf':r'Net cash provided by \(used for\) operating activities',
     'capex':r'Capital expenditures\s*[—–-]+\s*excluding equipment leased to others',
     'lease':r'Expenditures for equipment leased to others',
     'da':r'Depreciation and amortization',
     'disp':r'Proceeds from disposals of (?:leased assets and )?property, plant and equipment',
     'profit':r'Profit(?: \(loss\))? (?:of consolidated and affiliated companies)?',
     'undist':r'Undistributed profit of Financial Products',
     }
def nums(s,n=6):
    s=s.replace('( ','(').replace(' )',')')
    toks=re.findall(r'\(?[\d,]+\)?|—',s)
    out=[]
    for t in toks[:n]:
        if t=='—': out.append(0.0)
        else:
            v=float(t.strip('()').replace(',',''))
            out.append(-v if t.startswith('(') else v)
    return out
res={}
for y in range(2004,2026):
    t=re.sub(r'[\s|$]+',' ',doc(y))
    i=[m.start() for m in re.finditer(r'Supplemental [Dd]ata for (?:Statement of )?[Cc]ash [Ff]low',t)][0]
    blk=t[i:i+25000]
    d={}
    for k,p in LAB.items():
        m=re.search(p,blk)
        if m:
            seg=blk[m.end():m.end()+160]
            seg=re.sub(r'^[^\d(—]*','',seg)
            d[k]=nums(seg)
    res[y]=d
json.dump(res,open('sup_parsed.json','w'),indent=0)
for y in res:
    print(y,{k:v for k,v in res[y].items()})
