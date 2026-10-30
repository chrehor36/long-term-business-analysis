# Peer return-on-equity series from SEC XBRL companyfacts (transcription; FY 10-K values, latest filed for each FY end)
import json,sys,os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'cache')
def series(d,tags,unit='USD',dur=True):
    res={};acc={}
    for t in tags:
        f=d['facts'].get('us-gaap',{}).get(t)
        if not f: continue
        out={}
        for x in f['units'].get(unit,[]):
            if x.get('form') not in ('10-K','10-K/A'): continue
            if dur:
                if 'start' not in x: continue
                from datetime import date
                s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                if not (350<(e-s).days<380): continue
            y=x['end'][:4]
            if x['end'][5:]!='12-31': continue
            out[y]=(x['val'],x['accn'],x['filed']) if y not in out or x['filed']>out[y][2] else out[y]
        if out: res.setdefault('t',[]).append(t); [acc.setdefault(k,v) for k,v in out.items()]
    return ','.join(res.get('t',[])),acc
for cik in sys.argv[1:]:
    d=json.load(open(os.path.join(D,'facts_%s.json'%cik)))
    tn,ni=series(d,['NetIncomeLoss','NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLossAttributableToParent','ProfitLoss'])
    te,eq=series(d,['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],dur=False)
    tr,rev=series(d,['Revenues','RevenueFromContractWithCustomerIncludingAssessedTax','RegulatedAndUnregulatedOperatingRevenue'])
    tc,cx=series(d,['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsToAcquireOtherPropertyPlantAndEquipment','PaymentsToAcquireAndDevelopRealEstate'])
    td,da=series(d,['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet','Depreciation','DepreciationNonproduction'])
    print(d['entityName'],'| tags',tn,te,tr,tc,td)
    print(' FY   NetInc  Equity(end)  ROE(avg eq)  Rev   Capex  D&A  capex/D&A')
    for y in [str(v) for v in range(2015,2026)]:
        n=ni.get(y,(None,))[0]; e=eq.get(y,(None,))[0]; ep=eq.get(str(int(y)-1),(None,))[0]
        roe= n/((e+ep)/2) if n and e and ep else None
        r=rev.get(y,(None,))[0]; c=cx.get(y,(None,))[0]; a=da.get(y,(None,))[0]
        f=lambda v: '%8.0f'%(v/1e6) if v else '       -'
        print(y,f(n),f(e),'   %5.1f%%'%(roe*100) if roe else '     -',f(r),f(c),f(a),' %.2f'%(c/a) if c and a else '')
    print()
