import json,sys,os
B=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'cache')
def series(facts,tags,fy_end_month=None):
    out={}
    for t in tags:
        u=facts['facts'].get('us-gaap',{}).get(t)
        if not u: continue
        for unit,vals in u['units'].items():
            for v in vals:
                if v.get('form')!='10-K': continue
                fp=v.get('fp'); 
                if 'start' in v:
                    from datetime import date
                    s=date.fromisoformat(v['start']); e=date.fromisoformat(v['end'])
                    if not (350<= (e-s).days <=380): continue
                key=v['end']
                # first filed vintage
                if key not in out or v['filed']<out[key][1]:
                    out[key]=(v['val'],v['filed'],t,v['accn'])
        if out: pass
    return out
def pick(facts,tags):
    res={}
    for t in tags:
        s=series(facts,[t])
        for k,v in s.items():
            if k not in res: res[k]=v
    return res
names={'0000356309':'NJR','0000731802':'ATO','0001587732':'OGS','0001733998':'NWN'}
for cik,n in names.items():
    f=json.load(open(os.path.join(B,f'facts_{cik}.json')))
    ni=pick(f,['NetIncomeLoss','ProfitLoss'])
    eq=pick(f,['StockholdersEquity'])
    ocf=pick(f,['NetCashProvidedByUsedInOperatingActivities'])
    cap=pick(f,['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsForCapitalImprovements'])
    da=pick(f,['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'])
    rev=pick(f,['Revenues','RevenueFromContractWithCustomerIncludingAssessedTax'])
    print('=====',n)
    ends=sorted(set(k for k in ni if k>='2015-06-01'))
    for e in ends:
        g=lambda d: d.get(e,(None,))[0]
        def fm(x): return f'{x/1e6:9.1f}' if x is not None else '        -'
        print(e, 'NI',fm(g(ni)),'EQ',fm(g(eq)),'OCF',fm(g(ocf)),'CAPEX',fm(g(cap)),'DA',fm(g(da)),'REV',fm(g(rev)), ni[e][3])
