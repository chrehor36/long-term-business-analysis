import json, os, datetime as dt
D=os.path.dirname(os.path.abspath(__file__))
TICKS=['HUBB','VMI','NVT','AZZ','ATKR','THR','WIRE']
M=1e6
def dd(s): return dt.date.fromisoformat(s)
CF={t:json.load(open(os.path.join(D,'companyfacts_%s.json'%t))) for t in TICKS}

def rows(cf,tag):
    for ns in ('us-gaap',):
        f=cf.get('facts',{}).get(ns,{}).get(tag)
        if f:
            for unit,rs in f['units'].items():
                if unit=='USD': return rs
    return []

def dur(cf,tags,lo=330,hi=400):
    out={}
    for tag in tags:
        for r in rows(cf,tag):
            if 'start' not in r or not str(r.get('form','')).startswith('10-K'): continue
            n=(dd(r['end'])-dd(r['start'])).days+1
            if not (lo<=n<=hi): continue
            e=r['end']; cur=out.get(e)
            if cur is None or (r['filed'],)<(cur['filed'],):
                out[e]={'val':r['val'],'accn':r['accn'],'filed':r['filed'],'start':r['start'],'days':n,'tag':tag}
        if out: break   # tag priority: use first tag that yields data, then fill gaps below
    for tag in tags:
        for r in rows(cf,tag):
            if 'start' not in r or not str(r.get('form','')).startswith('10-K'): continue
            n=(dd(r['end'])-dd(r['start'])).days+1
            if not (lo<=n<=hi): continue
            e=r['end']
            if e in out: continue
            out[e]={'val':r['val'],'accn':r['accn'],'filed':r['filed'],'start':r['start'],'days':n,'tag':tag}
    return out

def ins(cf,tags):
    out={}
    for tag in tags:
        for r in rows(cf,tag):
            if 'start' in r or not str(r.get('form','')).startswith('10-K'): continue
            e=r['end']
            if e in out: continue
            cur=out.get(e)
            out[e]={'val':r['val'],'accn':r['accn'],'filed':r['filed'],'tag':tag}
        # keep earliest-filed within a tag
    # redo with earliest-filed preference per tag priority
    out={}
    for tag in tags:
        tmp={}
        for r in rows(cf,tag):
            if 'start' in r or not str(r.get('form','')).startswith('10-K'): continue
            e=r['end']; c=tmp.get(e)
            if c is None or r['filed']<c['filed']:
                tmp[e]={'val':r['val'],'accn':r['accn'],'filed':r['filed'],'tag':tag}
        for e,v in tmp.items():
            out.setdefault(e,v)
    return out

SPEC={
 'rev':(dur,['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet']),
 'gp':(dur,['GrossProfit']),
 'cogs':(dur,['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold','CostOfGoodsSoldExcludingDepreciationDepletionAndAmortization']),
 'oi':(dur,['OperatingIncomeLoss']),
 'ni':(dur,['NetIncomeLoss','ProfitLoss']),
 'cfo':(dur,['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations']),
 'capex':(dur,['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipmentAndIntangibleAssets']),
 'da':(dur,['DepreciationDepletionAndAmortization','DepreciationAmortizationAndAccretionNet','DepreciationAndAmortization']),
 'dep':(dur,['Depreciation']),
 'amort':(dur,['AmortizationOfIntangibleAssets']),
 'eq':(ins,['StockholdersEquity']),
 'eqt':(ins,['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']),
 'assets':(ins,['Assets']),
 'liab':(ins,['Liabilities']),
 'gw':(ins,['Goodwill']),
 'int':(ins,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet']),
}
DATA={}
for t in TICKS:
    cf=CF[t]
    DATA[t]={k:fn(cf,tags) for k,(fn,tags) in SPEC.items()}

# fiscal-year label = calendar year of period end date
def fy(e):
    d=dd(e)
    return d.year

# canonical FY end dates per ticker (from revenue series), 2019+
FYENDS={}
for t in TICKS:
    es=sorted(DATA[t]['rev'])
    keep={}
    for e in es:
        y=fy(e)
        if y<2018: continue
        # for VMI drop the anomalous 364-day 2022-12-24 duplicate; prefer the one with a gp value
        if y in keep:
            a=keep[y]; b=e
            ga=DATA[t]['gp'].get(a); gb=DATA[t]['gp'].get(b)
            if gb is not None and ga is None: keep[y]=b
        else: keep[y]=e
    FYENDS[t]=keep
json.dump({'FYENDS':FYENDS},open(os.path.join(D,'fyends.json'),'w'),indent=1)

def V(t,k,e):
    x=DATA[t][k].get(e)
    return None if x is None else x['val']

out={}
for t in TICKS:
    out[t]={}
    for y,e in sorted(FYENDS[t].items()):
        rec={'fyend':e,'start':DATA[t]['rev'][e]['start'],'days':DATA[t]['rev'][e]['days'],
             'accn':DATA[t]['rev'][e]['accn'],'revtag':DATA[t]['rev'][e]['tag']}
        for k in ['rev','gp','cogs','oi','ni','cfo','capex','da','dep','amort','eq','eqt','assets','liab','gw','int']:
            rec[k]=V(t,k,e)
        if rec['gp'] is None and rec['rev'] is not None and rec['cogs'] is not None:
            rec['gp']=rec['rev']-rec['cogs']; rec['gp_src']='rev-cogs'
        else: rec['gp_src']='GrossProfit' if rec['gp'] is not None else None
        if rec['da'] is None and (rec['dep'] is not None or rec['amort'] is not None):
            rec['da']=(rec['dep'] or 0)+(rec['amort'] or 0); rec['da_src']='Depreciation+AmortizationOfIntangibleAssets'
        else: rec['da_src']='DDA' if rec['da'] is not None else None
        eqtot = rec['eqt'] if rec['eqt'] is not None else rec['eq']
        rec['eqtot']=eqtot
        if rec['liab'] is None and rec['assets'] is not None and eqtot is not None:
            rec['liab']=rec['assets']-eqtot; rec['liab_src']='Assets-Equity'
        else: rec['liab_src']='Liabilities' if rec['liab'] is not None else None
        eqp = rec['eq'] if rec['eq'] is not None else eqtot
        rec['eq_used']=eqp
        rec['tang']= None if eqp is None else eqp-(rec['gw'] or 0)-(rec['int'] or 0)
        out[t][y]=rec
json.dump(out,open(os.path.join(D,'peers_clean.json'),'w'),indent=1)

def f(x,d=1):
    return '   n/a  ' if x is None else ('%8.1f'%(x/M) if abs(x)>1000 else '%8.1f'%(x/M))
def p(x):
    return '  n/a ' if x is None else '%5.1f%%'%(100*x)

for t in TICKS:
    print('\n===== %s ====='%t)
    print('%-4s %-11s %4s %9s %9s %9s %9s %9s %9s %9s %9s %9s %9s %9s %9s'%('FY','end','days','rev','gp','oi','ni','eq(par)','eq(tot)','gw','intang','tang eq','cfo','capex','d&a'))
    for y,r in sorted(out[t].items()):
        print('%-4d %-11s %4d %s %s %s %s %s %s %s %s %s %s %s %s'%(y,r['fyend'],r['days'],
          f(r['rev']),f(r['gp']),f(r['oi']),f(r['ni']),f(r['eq']),f(r['eqtot']),f(r['gw']),f(r['int']),f(r['tang']),f(r['cfo']),f(r['capex']),f(r['da'])))
