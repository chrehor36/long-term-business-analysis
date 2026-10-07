import json,datetime,sys
def annual(d,tag):
    if tag not in d: return {}
    out={}
    for u,vals in d[tag]['units'].items():
        for v in vals:
            if v.get('fp')=='FY' and v.get('form','').startswith('10-K') and 'start' in v:
                s=datetime.date.fromisoformat(v['start']); e=datetime.date.fromisoformat(v['end'])
                if (e-s).days<350: continue
                out[e.year]=v['val']   # latest filed wins
    return out
for t in sys.argv[1:]:
    d=json.load(open(t+'_facts.json'))['facts']['us-gaap']
    S={}
    for tag in ['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax']:
        for k,v in annual(d,tag).items(): S.setdefault(k,v)
    GP=annual(d,'GrossProfit'); OI=annual(d,'OperatingIncomeLoss'); NI=annual(d,'NetIncomeLoss')
    print(t)
    for y in sorted(S):
        if y<2008: continue
        g=GP.get(y); o=OI.get(y)
        print(f"  {y} sales {S[y]/1e6:9.1f}  GM {g/S[y]*100 if g else float('nan'):5.1f}  OM {o/S[y]*100 if o else float('nan'):5.1f}  NI {NI.get(y,0)/1e6:8.1f}")
