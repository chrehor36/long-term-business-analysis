import sys,json
sys.path.insert(0,'tools'); import sources as s
tags_rev=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
tags_oi=['OperatingIncomeLoss']
tags_ni=['NetIncomeLoss','ProfitLoss']
tags_eq=['StockholdersEquity']
def fy(facts,tag):
    out={}
    u=facts['facts'].get('us-gaap',{}).get(tag,{}).get('units',{}).get('USD',[])
    for r in u:
        if r.get('form')!='10-K' or r.get('fp')!='FY': continue
        if 'start' in r:
            from datetime import date
            d0=date.fromisoformat(r['start']); d1=date.fromisoformat(r['end'])
            if not 340<= (d1-d0).days <=380: continue
        y=int(r['end'][:4])
        # keep earliest-filed value for the period (as first reported)
        if y not in out or r['filed']<out[y][1]: out[y]=(r['val'],r['filed'],r['accn'])
    return out
for tk in sys.argv[1:]:
    cik=s.cik_for(tk)[0]; f=s.sec_facts(cik)
    print('==',tk,cik,f.get('entityName'))
    def pick(tags):
        m={}
        for t in tags:
            for y,v in fy(f,t).items():
                m.setdefault(y,v)
        return m
    R=pick(tags_rev); O=pick(tags_oi); N=pick(tags_ni); E=pick(tags_eq)
    for y in sorted(set(R)|set(O)):
        if y<2013: continue
        r=R.get(y,(None,))[0]; o=O.get(y,(None,))[0]; n=N.get(y,(None,))[0]; e=E.get(y,(None,))[0]
        m = f"{o/r*100:6.1f}%" if r and o is not None else '   n/a'
        roe = f"{n/e*100:6.1f}%" if n is not None and e else '   n/a'
        acc = (O.get(y) or R.get(y))[2]
        print(y, f"rev {r/1e6 if r else float('nan'):9.0f}", f"opinc {o/1e6 if o is not None else float('nan'):8.0f}", 'opm',m, f"ni {n/1e6 if n is not None else float('nan'):8.0f}", 'roe',roe, acc)
