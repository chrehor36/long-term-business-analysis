import json, os, datetime as dt, collections
D=os.path.dirname(os.path.abspath(__file__))
TICKS=['HUBB','VMI','NVT','AZZ','ATKR','THR','WIRE']

def dd(s): return dt.date.fromisoformat(s)

def load(t):
    return json.load(open(os.path.join(D,'companyfacts_%s.json'%t)))

def facts(cf,tag):
    for ns in ('us-gaap','ifrs-full','srt'):
        f=cf.get('facts',{}).get(ns,{}).get(tag)
        if f:
            for unit,rows in f['units'].items():
                if unit in ('USD','usd'):
                    return rows, f.get('label','')
    return None,None

def annual(cf,tag,lo=330,hi=400):
    """return {fyend_date: (value, accn, filed, start)} using 10-K duration facts"""
    rows,_=facts(cf,tag)
    out={}
    if not rows: return out
    for r in rows:
        if 'start' not in r or 'end' not in r: continue
        if not str(r.get('form','')).startswith('10-K'): continue
        n=(dd(r['end'])-dd(r['start'])).days+1
        if not (lo<=n<=hi): continue
        e=r['end']
        cur=out.get(e)
        # prefer ORIGINAL report: earliest filed
        if cur is None or r['filed']<cur[2]:
            out[e]=(r['val'],r.get('accn'),r['filed'],r['start'],n)
    return out

def annual_latest(cf,tag,lo=330,hi=400):
    rows,_=facts(cf,tag); out={}
    if not rows: return out
    for r in rows:
        if 'start' not in r or 'end' not in r: continue
        if not str(r.get('form','')).startswith('10-K'): continue
        n=(dd(r['end'])-dd(r['start'])).days+1
        if not (lo<=n<=hi): continue
        e=r['end']; cur=out.get(e)
        if cur is None or r['filed']>=cur[2]: out[e]=(r['val'],r.get('accn'),r['filed'],r['start'],n)
    return out

def inst(cf,tag):
    rows,_=facts(cf,tag); out={}
    if not rows: return out
    for r in rows:
        if 'start' in r: continue
        if not str(r.get('form','')).startswith('10-K'): continue
        e=r['end']; cur=out.get(e)
        if cur is None or r['filed']<cur[2]: out[e]=(r['val'],r.get('accn'),r['filed'])
    return out

def firstof(fn,cf,tags):
    for t in tags:
        d=fn(cf,t)
        if d: return d,t
    return {},None

REV=['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
COGS=['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold','CostOfSales']
OI=['OperatingIncomeLoss']
NI=['NetIncomeLoss','ProfitLoss']
EQ=['StockholdersEquity']
EQT=['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']
CFO=['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']
CAPEX=['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets']
DA=['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization','DepreciationDepletionAndAmortizationExcludingAmortizationOfDeferredCharges']
GW=['Goodwill']
INT=['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet']

res={}
for t in TICKS:
    cf=load(t)
    d={}
    d['rev'],d['rev_tag']=firstof(annual,cf,REV)
    d['revL'],_=firstof(annual_latest,cf,REV)
    d['gp'],d['gp_tag']=firstof(annual,cf,['GrossProfit'])
    d['cogs'],d['cogs_tag']=firstof(annual,cf,COGS)
    d['oi'],_=firstof(annual,cf,OI)
    d['ni'],_=firstof(annual,cf,NI)
    d['eq'],_=firstof(inst,cf,EQ)
    d['eqt'],_=firstof(inst,cf,EQT)
    d['cfo'],_=firstof(annual,cf,CFO)
    d['capex'],d['capex_tag']=firstof(annual,cf,CAPEX)
    d['da'],d['da_tag']=firstof(annual,cf,DA)
    d['assets'],_=firstof(inst,cf,['Assets'])
    d['liab'],_=firstof(inst,cf,['Liabilities'])
    d['gw'],_=firstof(inst,cf,GW)
    d['int'],d['int_tag']=firstof(inst,cf,INT)
    res[t]=d
    ends=sorted(d['rev'])
    print('==',t,'revtag',d['rev_tag'],'gptag',d['gp_tag'],'cogstag',d['cogs_tag'],'capex',d['capex_tag'],'da',d['da_tag'],'int',d['int_tag'])
    print('  FY ends:',[e for e in ends if e>='2018-01-01'])
json.dump({k:{kk:(vv if not isinstance(vv,dict) else {a:list(b) for a,b in vv.items()}) for kk,vv in v.items()} for k,v in res.items()}, open(os.path.join(D,'peers_raw.json'),'w'), indent=1)
