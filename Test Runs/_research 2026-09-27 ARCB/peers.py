import json,sys,os,time,datetime
sys.path.insert(0,'.')
from fetch import get
P={'ARCB':894405,'ODFL':878927,'SAIA':1177702,'XPO':1166003,'YELL':716006,'CHRW':1043277,'LSTR':853816,'RXO':1929561,'KNX':1492691}
for t,c in P.items():
    fn='cache/peers/%s_facts.json'%t
    if not os.path.exists(fn):
        try: open(fn,'wb').write(get('https://data.sec.gov/api/xbrl/companyfacts/CIK%010d.json'%c)); time.sleep(0.3)
        except SystemExit as e: print('FAIL',t); continue
def annual(f,tag):
    out={}
    for ns in ('us-gaap',):
        if tag not in f['facts'].get(ns,{}): continue
        for unit,vals in f['facts'][ns][tag]['units'].items():
            if unit!='USD': continue
            for v in vals:
                if v.get('form') not in ('10-K','10-K/A'): continue
                if v.get('start'):
                    s=datetime.date.fromisoformat(v['start']);e=datetime.date.fromisoformat(v['end'])
                    if (e-s).days<340: continue
                out.setdefault(v['end'][:4],(v['filed'],v['val']))
                if v['filed']>out[v['end'][:4]][0]: out[v['end'][:4]]=(v['filed'],v['val'])
    return {k:v[1]/1e6 for k,v in out.items()}
def first(f,tags,mx=False):
    d={}
    for t in tags:
        a=annual(f,t)
        for k,v in a.items():
            if mx: d[k]=max(d.get(k,0),v)
            else: d.setdefault(k,v)
    return d
rows=[]
for t in P:
    fn='cache/peers/%s_facts.json'%t
    if not os.path.exists(fn): continue
    f=json.load(open(fn))
    rev=first(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueServicesNet','OperatingRevenue','RevenuesNetOfInterestExpense','RevenueFromContractWithCustomerIncludingAssessedTax'],mx=True)
    oi=first(f,['OperatingIncomeLoss'])
    eq=first(f,['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'])
    debt=first(f,['LongTermDebt','LongTermDebtNoncurrent','DebtLongtermAndShorttermCombinedAmount'])
    ltn=first(f,['LongTermDebtNoncurrent']); cur=first(f,['LongTermDebtCurrent','DebtCurrent'])
    cash=first(f,['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'])
    sti=first(f,['ShortTermInvestments'])
    gw=first(f,['Goodwill']); ia=first(f,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'])
    print('=====',t)
    for y in sorted(oi):
        if y<'2005': continue
        r=rev.get(y); o=oi[y]
        d=debt.get(y) if debt.get(y) is not None else (ltn.get(y,0)+cur.get(y,0))
        cap=None
        if eq.get(y) is not None: cap=eq[y]+(d or 0)-cash.get(y,0)-sti.get(y,0)
        tcap=cap-gw.get(y,0)-ia.get(y,0) if cap is not None else None
        print(y,'rev',r and round(r,1),'oi',round(o,1),'om',r and '%.1f%%'%(100*o/r),'opcap',cap and round(cap,1),'oi/opcap',cap and '%.1f%%'%(100*o/cap),'oi/tangcap',tcap and tcap>0 and '%.1f%%'%(100*o/tcap))
