import json,os,sys,datetime
sys.path.insert(0,'.')
from fetch import get
T=['EPAC','SNA','SWK','KMT','HLIO','IEX','GGG','LECO','ESAB','PH','ITW','NDSN']
tk={v['ticker']:v for v in json.load(open('peers/tickers.json')).values()}
def cf(t):
    p='peers/%s_facts.json'%t
    if t=='EPAC': p='companyfacts.json'
    if not os.path.exists(p):
        c='%010d'%tk[t]['cik_str']; open(p,'wb').write(get('https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json'%c))
    return json.load(open(p))
def ser(j,tag,inst=False):
    out={}
    if tag not in j['facts'].get('us-gaap',{}): return out
    for u,fs in j['facts']['us-gaap'][tag]['units'].items():
        if u!='USD': continue
        for f in fs:
            if f.get('form') not in ('10-K','10-K/A'): continue
            e=f['end']
            if not inst:
                if 'start' not in f: continue
                d=(datetime.date.fromisoformat(e)-datetime.date.fromisoformat(f['start'])).days
                if d<350 or d>380: continue
            if e not in out or f['filed']>out[e][1]: out[e]=(f['val'],f['filed'])
    return {k:v[0] for k,v in out.items()}
def first(j,tags,inst=False):
    res={}
    for tag in tags:
        for k,v in ser(j,tag,inst).items(): res.setdefault(k,v)
    return res
def near(d,s):
    dd=datetime.date.fromisoformat(d)
    c=[k for k in s if abs((datetime.date.fromisoformat(k)-dd).days)<=7]
    return s[c[0]] if c else None
out={}
for t in T:
    try: j=cf(t)
    except Exception as e: print('==',t,'FAILED',e); continue
    R=first(j,['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet','SalesRevenueGoodsNet','RevenueFromContractWithCustomerIncludingAssessedTax'])
    GP=first(j,['GrossProfit']); COGS=first(j,['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold','CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization'])
    OI=first(j,['OperatingIncomeLoss'])
    A=first(j,['Assets'],True); C=first(j,['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],True)
    GW=first(j,['Goodwill'],True); IN=first(j,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],True)
    ends=sorted(e for e in R if e>='2015-06-01')
    rows=[]
    for e in ends:
        r=R[e]; gp=near(e,GP)
        if gp is None:
            cg=near(e,COGS); gp=(r-cg) if cg is not None else None
        oi=near(e,OI); a=near(e,A); c=near(e,C) or 0; g=near(e,GW) or 0; i=near(e,IN) or 0
        tang=(a-c-g-i) if a is not None else None
        rows.append((e,r,gp,oi,tang))
    out[t]=(j.get('entityName',''),rows)
    print('\n==',t,j.get('entityName',''))
    pt=None
    for e,r,gp,oi,tang in rows:
        ret=(oi/((tang+pt)/2)) if (oi is not None and tang and pt) else None
        print('  %s sales %9.1f  GM %s  OM %s  OI/avg tangible non-cash assets %s'%(e,r/1e6,('%5.1f%%'%(100*gp/r)) if gp else '    -',('%5.1f%%'%(100*oi/r)) if oi is not None else '    -',('%6.1f%%'%(100*ret)) if ret is not None else '     -'))
        pt=tang
json.dump(out,open('peers/row_rows.json','w'))
