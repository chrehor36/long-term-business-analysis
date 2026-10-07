import json, sys, os
from fetch import get
from tables import flat
for t,cik in [('TMO','0000097745'),('DHR','0000313616'),('BIO','0000012208'),('RVTY','0000031791')]:
    p=f'cache/peers/{t}_sub.json'
    if not os.path.exists(p): open(p,'wb').write(get(f'https://data.sec.gov/submissions/CIK{cik}.json'))
    r=json.load(open(p))['filings']['recent']
    i=[k for k in range(len(r['form'])) if r['form'][k]=='10-K'][0]
    acc=r['accessionNumber'][i]; doc=r['primaryDocument'][i]
    out=f'cache/peers/{t}_10k_{r["reportDate"][i][:4]}.txt'
    if not os.path.exists(out):
        open(out,'w',encoding='utf-8').write(flat(get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-","")}/{doc}')))
    print(t, r['filingDate'][i], acc, doc, out)
