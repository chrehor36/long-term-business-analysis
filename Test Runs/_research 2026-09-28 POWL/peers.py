import json, sys, os
sys.path.insert(0, r'../../tools')
import sources as S
from fetch import get
from datetime import date
PEERS=['POWL','ETN','HUBB','NVT','VRT','GEV','AZZ','THR','IESC','PLPC','ABBNY','AYI','ATKR','GE','EMR','ROK','SIEGY']
out={}
for t in PEERS:
    try:
        c=S.cik_for(t)
    except Exception as e:
        c=None
    print(t, c)
    if not c: continue
    cik=c[0] if isinstance(c,tuple) else c
    fn=f'cache/facts_{t}.json'
    if not os.path.exists(fn):
        try: open(fn,'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{str(cik).zfill(10)}.json'))
        except SystemExit as e: print('  fail', e); continue
    F=json.load(open(fn))['facts']
    out[t]={'cik':cik,'name':c[1] if isinstance(c,tuple) else ''}
    for ns in F:
        for tag in F[ns]:
            pass
    def ann(tag):
        for ns in ('us-gaap','ifrs-full'):
            if ns in F and tag in F[ns]:
                res={}
                for u,rows in F[ns][tag]['units'].items():
                    for r in rows:
                        if r.get('fp')!='FY' or r.get('form') not in ('10-K','20-F','10-K/A','20-F/A'): continue
                        if 'start' in r:
                            d=(date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days
                            if d<340 or d>380: continue
                        res.setdefault(r['end'][:4],{})[r['filed']]=(r['val'],u)
                return {e:v[max(v)] for e,v in res.items()}
        return {}
    def first(*tags):
        m={}
        for tg in tags:
            for k,v in ann(tg).items(): m.setdefault(k,v)
        return m
    rev=first('Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet','Revenue')
    oi=first('OperatingIncomeLoss','ProfitLossFromOperatingActivities')
    ar=first('AccountsReceivableNetCurrent','ReceivablesNetCurrent','TradeAndOtherCurrentReceivables','CurrentTradeReceivables')
    inv=first('InventoryNet','Inventories')
    ap=first('AccountsPayableCurrent','TradeAndOtherCurrentPayables','AccountsPayableTradeCurrent')
    ppe=first('PropertyPlantAndEquipmentNet','PropertyPlantAndEquipment')
    ca=first('ContractWithCustomerAssetNetCurrent','CostsInExcessOfBillingsCurrent')
    cl=first('ContractWithCustomerLiabilityCurrent','BillingsInExcessOfCostCurrent')
    am=first('AmortizationOfIntangibleAssets')
    rows=[]
    for y in sorted(set(rev)&set(oi)):
        if int(y)<2005: continue
        r=rev[y][0]; o=oi[y][0]; a=am.get(y,(0,))[0]
        if not r: continue
        cap=None
        if y in ar and y in inv and y in ap and y in ppe:
            cap=ar[y][0]+inv[y][0]-ap[y][0]+ppe[y][0]
        cap2=None
        if cap is not None: cap2=cap+ca.get(y,(0,))[0]-cl.get(y,(0,))[0]
        rows.append((y, round(r/1e6,1), round(o/1e6,1), round(o/r*100,2), round((o+a)/cap*100,1) if cap else None, round((o+a)/cap2*100,1) if cap2 and cap2>0 else (None if cap2 is None else 'neg'), rev[y][1]))
    out[t]['rows']=rows
    for rr in rows: print('  ', rr)
json.dump(out,open('peers.json','w'),indent=0)
