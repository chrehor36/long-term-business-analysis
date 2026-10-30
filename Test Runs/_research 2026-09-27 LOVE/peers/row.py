import json,os,sys,datetime
sys.path.insert(0,'..'); sys.path.insert(0,'.')
from fetch import get
T=['LOVE','RH','WSM','ARHS','ETD','LZB','HVT','BSET','HOFT','SNBR','PRPL','W','FLXS','KIRK']
if not os.path.exists('peers/tickers.json'):
    open('peers/tickers.json','wb').write(get('https://www.sec.gov/files/company_tickers.json'))
tk={v['ticker']:v for v in json.load(open('peers/tickers.json')).values()}
def cf(t):
    p='peers/%s_facts.json'%t
    if t=='LOVE': p='companyfacts.json'
    if not os.path.exists(p):
        c='%010d'%tk[t]['cik_str']; open(p,'wb').write(get('https://data.sec.gov/api/xbrl/companyfacts/CIK%s.json'%c))
    return json.load(open(p))
def ser(j,tags,inst=False):
    out={}
    for tag in tags:
        for ns in ('us-gaap',):
            if tag not in j['facts'].get(ns,{}): continue
            for u,fs in j['facts'][ns][tag]['units'].items():
                if u!='USD': continue
                for f in fs:
                    if f.get('form') not in ('10-K','10-K/A'): continue
                    e=f['end']
                    if not inst:
                        if 'start' not in f: continue
                        d=(datetime.date.fromisoformat(e)-datetime.date.fromisoformat(f['start'])).days
                        if d<350 or d>380: continue
                    if e not in out or f['filed']>out[e][1]: out[e]=(f['val'],f['filed'])
        if out and not inst: pass
    return {k:v[0] for k,v in out.items()}
def first(j,taglist,inst=False):
    res={}
    for tag in taglist:
        s=ser(j,[tag],inst)
        for k,v in s.items(): res.setdefault(k,v)
    return res
out=[]
for t in T:
    try: j=cf(t)
    except (SystemExit,KeyError) as e: print('== '+t+' NOT IN company_tickers.json or fetch failed: '+repr(e)); continue
    R=first(j,['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueGoodsNet'])
    GP=first(j,['GrossProfit']); OI=first(j,['OperatingIncomeLoss','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']); A=first(j,['Assets'],True)
    C=first(j,['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],True)
    ends=sorted(e for e in R if e>='2016-06-01')
    # month-match balance dates to fiscal year ends (within 7 days)
    def near(d,s):
        dd=datetime.date.fromisoformat(d)
        c=[k for k in s if abs((datetime.date.fromisoformat(k)-dd).days)<=7]
        return s[c[0]] if c else None
    line=[t,j.get('entityName','')]
    rows=[]
    for i,e in enumerate(ends):
        r=R[e]; gp=near(e,GP); oi=near(e,OI); a=near(e,A); c=near(e,C)
        nca=(a-c) if (a is not None and c is not None) else None
        if gp is None and oi is None: continue
        rows.append((e,r,gp,oi,nca))
    out.append((t,j.get('entityName',''),rows))
    print('\n==',t,j.get('entityName',''))
    pn=None
    for e,r,gp,oi,nca in rows:
        ret=(oi/((nca+pn)/2)) if (oi is not None and nca and pn) else None
        print('  %s sales %9.1f  GM %s  OM %s  OI/avg(assets-cash) %s'%(e,r/1e6,('%5.1f%%'%(100*gp/r)) if gp else '    -',('%5.1f%%'%(100*oi/r)) if oi is not None else '    -',('%6.1f%%'%(100*ret)) if ret is not None else '     -'))
        pn=nca
json.dump(out,open('peers/row_rows.json','w'))
