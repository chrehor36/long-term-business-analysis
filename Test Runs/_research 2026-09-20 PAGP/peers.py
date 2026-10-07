import sys, os, json, urllib.request, gzip
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','tools'))
UA={'User-Agent':'BRK research chrehor36@gmail.com','Accept-Encoding':'gzip'}
D=os.path.dirname(os.path.abspath(__file__))
PEERDIR=os.path.join(D,'peers'); os.makedirs(PEERDIR, exist_ok=True)
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120)
    raw=r.read()
    if r.headers.get('Content-Encoding')=='gzip': raw=gzip.decompress(raw)
    return raw.decode('utf-8','replace')
def facts(cik, tic):
    p=os.path.join(PEERDIR, f'{tic}_companyfacts.json')
    if not os.path.exists(p):
        open(p,'w',encoding='utf-8').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json'))
    return json.load(open(p,encoding='utf-8'))
def annual(f, tags, lo=340, hi=380):
    out={}
    for t in tags:
        u=f.get('facts',{}).get('us-gaap',{}).get(t,{}).get('units',{}).get('USD',[])
        for it in u:
            if it.get('form') not in ('10-K','10-K/A'): continue
            s=it.get('start'); e=it.get('end')
            if not s: continue
            from datetime import date
            sd=date.fromisoformat(s); ed=date.fromisoformat(e)
            if not (lo<=(ed-sd).days<=hi): continue
            y=e[:4]
            if y not in out or it.get('fy',0)>=out[y][1]:
                out[y]=(it['val'], it.get('fy',0))
    return {k:v[0] for k,v in out.items()}
def instant(f, tags):
    out={}
    for t in tags:
        u=f.get('facts',{}).get('us-gaap',{}).get(t,{}).get('units',{}).get('USD',[])
        for it in u:
            if it.get('form') not in ('10-K','10-K/A'): continue
            if it.get('start'): continue
            e=it['end']
            if not e.endswith(('-12-31','-09-30')): continue
            y=e[:4]
            if y not in out or it.get('fy',0)>=out[y][1]:
                out[y]=(it['val'], it.get('fy',0))
    return {k:v[0] for k,v in out.items()}
PEERS=[('PAGP',1581990),('PAA',1070423) ,('EPD',1061219),('ET',1276187),('MPLX',1552000),
       ('OKE',1039684),('KMI',1506307),('TRGP',1389170),('WES',1423902),('GEL',1022321),
       ('HESM',1789832),('DKL',1552797)]
YEARS=['2021','2022','2023','2024','2025']
print(f"{'tic':6s} {'yr':5s} {'OpInc':>9s} {'netPPE':>10s} {'EqMeth':>9s} {'base':>10s} {'ROCE%':>7s} {'Rev':>10s}")
rows={}
for tic,cik in PEERS:
    try:
        f=facts(cik,tic)
    except Exception as ex:
        print(tic,'FAIL',ex); continue
    oi=annual(f,['OperatingIncomeLoss'])
    rev=annual(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax'])
    ppe=instant(f,['PropertyPlantAndEquipmentNet','PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization'])
    eqm=instant(f,['EquityMethodInvestments'])
    intg=instant(f,['FiniteLivedIntangibleAssetsNet','IntangibleAssetsNetExcludingGoodwill'])
    rows[tic]={}
    for y in YEARS:
        o=oi.get(y); p=ppe.get(y); e=eqm.get(y,0) or 0; i=intg.get(y,0) or 0
        if o is None or p is None:
            print(f"{tic:6s} {y:5s} {'-':>9s}"); continue
        base=p+e+i
        r=100.0*o/base if base else float('nan')
        rows[tic][y]=r
        print(f"{tic:6s} {y:5s} {o/1e6:9.0f} {p/1e6:10.0f} {e/1e6:9.0f} {base/1e6:10.0f} {r:7.1f} {(rev.get(y) or 0)/1e6:10.0f}")
print()
print('MEAN ROCE (op income / net PPE + equity method + intangibles), FY2021-25')
for tic,_ in PEERS:
    v=[x for x in rows.get(tic,{}).values()]
    if v: print(f'  {tic:6s} {sum(v)/len(v):6.1f}%   n={len(v)}')
