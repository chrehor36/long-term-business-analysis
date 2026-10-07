import json
from datetime import date
F={'PFGC':'cache/facts.json','SYY':'../_research 2026-09-26 SYY/companyfacts.json','USFD':'../_research 2026-09-26 SYY/peers/USFD_facts.json',
   'CHEF':'../_research 2026-09-26 SYY/peers/CHEF_facts.json','SPTN':'cache/peers/SPTN_facts.json','UNFI':'cache/peers/UNFI_facts.json',
   'DIT':'cache/peers/DIT_facts.json','COREMARK':'cache/peers/COREMARK_facts.json'}
def mk(fx):
    g=fx['facts']['us-gaap']
    def ann(tag, flow=True):
        if tag not in g: return {}
        out={}
        for u,rows in g[tag]['units'].items():
            if u!='USD': continue
            for r in rows:
                if r.get('form') not in ('10-K','10-K/A'): continue
                if flow:
                    if 'start' not in r: continue
                    d=(date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days
                    if d<340 or d>380: continue
                else:
                    if 'start' in r: continue
                out.setdefault(r['end'],{})[r['filed']]=r['val']
        return {e:v[max(v)] for e,v in out.items()}
    return ann
def first(ann, tags, flow=True):
    res={}
    for t in tags:
        for e,v in ann(t,flow).items(): res.setdefault(e,v)
    return res
out={}
for n,p in F.items():
    ann=mk(json.load(open(p)))
    sales=first(ann,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    gp=first(ann,['GrossProfit']); cogs=first(ann,['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold'])
    for e in set(gp)|set(cogs):
        if e not in sales and e in gp and e in cogs: sales[e]=gp[e]+cogs[e]
    oi=first(ann,['OperatingIncomeLoss']); am=first(ann,['AmortizationOfIntangibleAssets'])
    ar=first(ann,['AccountsReceivableNetCurrent','ReceivablesNetCurrent','AccountsNotesAndLoansReceivableNetCurrent'],False); inv=first(ann,['InventoryNet','InventoryFinishedGoodsNetOfReserves'],False)
    ap=first(ann,['AccountsPayableCurrent','AccountsPayableTradeCurrent'],False); ppe=first(ann,['PropertyPlantAndEquipmentNet'],False)
    rows=[]
    for e in sorted(oi):
        s=sales.get(e); 
        if not s: continue
        # balance at year end (match within 10 days)
        def bal(d):
            for k,v in d.items():
                if abs((date.fromisoformat(k)-date.fromisoformat(e)).days)<=10: return v
        a,i,pay,pp=bal(ar),bal(inv),bal(ap),bal(ppe)
        ntoc=(a+i-pay+pp) if None not in (a,i,pay,pp) else None
        gpm=gp.get(e)/s*100 if gp.get(e) else None
        rows.append((e, round(s/1e6), round(gpm,2) if gpm else None, round(oi[e]/s*100,2), round((oi[e]+am.get(e,0))/ntoc*100,1) if ntoc else None, round(ntoc/1e6) if ntoc else None))
    out[n]=rows
    print('=====',n)
    for r in rows[-14:]: print(r)
json.dump(out,open('peers.json','w'))
