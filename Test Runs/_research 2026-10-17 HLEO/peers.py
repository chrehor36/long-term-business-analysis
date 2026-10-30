import json, urllib.request, sys
UA={'User-Agent':'Chris Hrehor chrehor36@gmail.com'}
def facts(cik):
    p=f"cache/cf_{cik}.json"
    try: return json.load(open(p))
    except Exception:
        raw=urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json",headers=UA)).read()
        open(p,'wb').write(raw); return json.loads(raw)
def annual(f,tags):
    for t in tags:
        u=f['facts'].get('us-gaap',{}).get(t)
        if not u: continue
        out={}
        for x in u['units'].get('USD',[]):
            if x.get('form')=='10-K' and x.get('fp')=='FY' and x.get('frame') and len(x['frame'])==6:
                out[x['frame']]=(x['val'],x['accn'])
        if out: return t,out
    return None,{}
for name,cik in [('Redwire',1819810),('Sidus Space',1879726)]:
    f=facts(cik)
    t1,rev=annual(f,['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'])
    t2,oi=annual(f,['OperatingIncomeLoss'])
    t3,ocf=annual(f,['NetCashProvidedByUsedInOperatingActivities'])
    print(name,t1,t2,t3)
    for y in sorted(set(rev)|set(oi)):
        r=rev.get(y,(None,''));o=oi.get(y,(None,''));c=ocf.get(y,(None,''))
        m=(o[0]/r[0]*100) if r[0] and o[0] is not None else None
        print(' ',y,r[0],o[0],c[0], f"{m:.1f}%" if m is not None else '', r[1] or o[1])
