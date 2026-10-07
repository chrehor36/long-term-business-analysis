import sys, os, json, urllib.request, gzip, time
from datetime import date
UA={'User-Agent':'BRK research chrehor36@gmail.com','Accept-Encoding':'gzip'}
D=os.path.dirname(os.path.abspath(__file__))
PEERDIR=os.path.join(D,'cache','peers'); os.makedirs(PEERDIR, exist_ok=True)
def get(url):
    r=urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120)
    raw=r.read()
    if r.headers.get('Content-Encoding')=='gzip': raw=gzip.decompress(raw)
    return raw.decode('utf-8','replace')
def facts(cik, tic):
    p=os.path.join(PEERDIR, f'{tic}_companyfacts.json')
    if not os.path.exists(p):
        open(p,'w',encoding='utf-8').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json')); time.sleep(0.3)
    return json.load(open(p,encoding='utf-8'))
def annual(f, tags, lo=340, hi=380):
    out={}
    for t in tags:
        u=f.get('facts',{}).get('us-gaap',{}).get(t,{}).get('units',{}).get('USD',[])
        for it in u:
            if it.get('form') not in ('10-K','10-K/A'): continue
            s=it.get('start'); e=it.get('end')
            if not s: continue
            if not (lo<=(date.fromisoformat(e)-date.fromisoformat(s)).days<=hi): continue
            y=e[:4]
            if y in out and out[y][2]!=t: continue   # first tag in list wins for a year
            if y not in out or it.get('fy',0)>=out[y][1]:
                out[y]=(it['val'], it.get('fy',0), t)
    return {k:v[0] for k,v in out.items()}
def instant(f, tags):
    out={}
    for t in tags:
        u=f.get('facts',{}).get('us-gaap',{}).get(t,{}).get('units',{}).get('USD',[])
        for it in u:
            if it.get('form') not in ('10-K','10-K/A'): continue
            if it.get('start'): continue
            e=it['end']
            if not e.endswith(('-12-31',)): continue
            y=e[:4]
            if y in out and out[y][2]!=t: continue
            if y not in out or it.get('fy',0)>=out[y][1]:
                out[y]=(it['val'], it.get('fy',0), t)
    return {k:v[0] for k,v in out.items()}
PEERS=[('DTM',1842022),('WMB',107263),('KMI',1506307),('AM',1623925),('OKE',1039684),('TRGP',1389170),
       ('ET',1276187),('WES',1423902),('KNTK',1692787),('HESM',1789832),('MPLX',1552000),('EPD',1061219),
       ('BWP',1336047),('ETRN',1747009)]
YEARS=['2021','2022','2023','2024','2025']
rowsA={}; rowsB={}
print(f"{'tic':5s} {'yr':4s} {'OpInc':>7s} {'EqEarn':>7s} {'netPPE':>8s} {'EqInv':>7s} {'Intang':>7s} {'A%':>6s} {'B%':>6s}")
for tic,cik in PEERS:
    try: f=facts(cik,tic)
    except Exception as ex: print(tic,'FAIL',ex); continue
    oi=annual(f,['OperatingIncomeLoss'])
    ee=annual(f,['IncomeLossFromEquityMethodInvestments','IncomeLossFromEquityMethodInvestmentsNetOfDividendsOrDistributions'])
    ppe=instant(f,['PropertyPlantAndEquipmentNet','PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization','PublicUtilitiesPropertyPlantAndEquipmentNet'])
    eqm=instant(f,['EquityMethodInvestments','LongTermInvestments'])
    intg=instant(f,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'])
    rowsA[tic]={}; rowsB[tic]={}
    for y in YEARS:
        o=oi.get(y); p=ppe.get(y); e=eqm.get(y,0) or 0; i=intg.get(y,0) or 0; q=ee.get(y,0) or 0
        if o is None or p is None:
            print(f"{tic:5s} {y:4s} missing oi={o} ppe={p}"); continue
        base=p+e+i
        a=100*o/base; b=100*(o+q)/base
        rowsA[tic][y]=(o,base); rowsB[tic][y]=(o+q,base)
        print(f"{tic:5s} {y:4s} {o/1e6:7.0f} {q/1e6:7.0f} {p/1e6:8.0f} {e/1e6:7.0f} {i/1e6:7.0f} {a:6.1f} {b:6.1f}")
print('\nFIVE-YEAR, ratio of means (sum numerator / sum denominator), years available within FY2021-2025')
print(f"{'tic':5s} {'n':>2s} {'A: opinc/base':>14s} {'B: (opinc+eq)/base':>19s}")
res=[]
for tic,_ in PEERS:
    ra=rowsA.get(tic,{}); rb=rowsB.get(tic,{})
    if not ra: continue
    A=100*sum(v[0] for v in ra.values())/sum(v[1] for v in ra.values())
    B=100*sum(v[0] for v in rb.values())/sum(v[1] for v in rb.values())
    res.append((tic,len(ra),A,B))
for tic,n,A,B in sorted(res,key=lambda r:-r[3]):
    print(f"{tic:5s} {n:2d} {A:14.1f} {B:19.1f}")
