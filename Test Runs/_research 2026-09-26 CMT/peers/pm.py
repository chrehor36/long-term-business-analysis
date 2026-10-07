import json,datetime,sys
def ann(cf,tags):
    out={}
    for t in tags:
        if t not in cf: continue
        for u,v in cf[t]['units'].items():
            for x in v:
                if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
                a=datetime.date.fromisoformat(x['start']);b=datetime.date.fromisoformat(x['end'])
                if 350<(b-a).days<380:
                    out.setdefault(int(x['end'][:4]),x['val'])
    return out
for fn in ['cvgi.json','mye.json']:
    j=json.load(open(fn)); cf=j['facts']['us-gaap']
    s=ann(cf,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'])
    o=ann(cf,['OperatingIncomeLoss'])
    print(j['entityName'])
    print(' '.join(f"{y}:{o[y]/s[y]*100:.1f}%" for y in sorted(o) if y in s and y>=2008))
