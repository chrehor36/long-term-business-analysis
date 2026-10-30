import json,urllib.request,os
UA={"User-Agent":"Chris Hrehor chrehor36@gmail.com"}
C={'CHD':313927,'PG':80424,'CLX':21076,'CL':21665,'KMB':55785,'KVUE':1944048,'EPC':1096752}
def facts(t):
    p=f'cache/{t}_facts.json'
    if not os.path.exists(p):
        u=f'https://data.sec.gov/api/xbrl/companyfacts/CIK{C[t]:010d}.json'
        open(p,'wb').write(urllib.request.urlopen(urllib.request.Request(u,headers=UA)).read())
    return json.load(open(p))
def annual(f,tags):
    out={}
    for tag in tags:
        d=f['facts']['us-gaap'].get(tag)
        if not d: continue
        for u in d['units'].values():
            for x in u:
                if x.get('form') in ('10-K','10-K/A') and x.get('fp')=='FY' and 'start' in x:
                    from datetime import date
                    s=date.fromisoformat(x['start']); e=date.fromisoformat(x['end'])
                    if 350<(e-s).days<380:
                        out.setdefault(e.isoformat()[:7],(x['val'],x['accn'],tag))
        # keep first tag priority only for missing years
    return out
if __name__=='__main__':
 for t in C:
     f=facts(t)
     rev=annual(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'])
     cogs=annual(f,['CostOfGoodsAndServicesSold','CostOfRevenue','CostOfGoodsSold'])
     gp=annual(f,['GrossProfit'])
     oi=annual(f,['OperatingIncomeLoss'])
     print('=====',t)
     for k in sorted(rev):
         if k<'2015': continue
         r=rev[k][0]; g=gp.get(k,(None,))[0]
         if g is None and k in cogs: g=r-cogs[k][0]
         o=oi.get(k,(None,))[0]
         print(k, f"rev {r/1e6:9.0f}", f"gm {g/r*100:5.1f}%" if g else "gm   n/a", f"om {o/r*100:5.1f}%" if o else "om n/a", rev[k][1])
