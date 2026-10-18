import json
from datetime import date
def ser(cik,tags,inst=False):
    d=json.load(open(f'cache/cf_{cik}.json')); out={}
    for t in tags:
        u=d['facts']['us-gaap'].get(t)
        if not u: continue
        for unit,vals in u['units'].items():
            for v in vals:
                if not v.get('form','').startswith('10-K'): continue
                if v['end'][5:]!='12-31': continue
                if not inst and not('start' in v and 330<(date.fromisoformat(v['end'])-date.fromisoformat(v['start'])).days<400): continue
                out.setdefault(int(v['end'][:4]),(v['val']/1e6,v['accn']))
    return out
co={'KGS':(1767042,['OperatingIncomeLoss'],None),
    'AROC':(1389050,None,('IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',['InterestExpense','InterestExpenseNonoperating'])),
    'USAC':(1522727,['OperatingIncomeLoss'],None),
    'NGS':(1084991,['OperatingIncomeLoss'],None)}
for k,(cik,op,alt) in co.items():
    A=ser(cik,['Assets'],True)
    if op: E=ser(cik,op)
    else:
        P=ser(cik,[alt[0]]); I={}
        for t in alt[1]:
            for y,v in ser(cik,[t]).items(): I.setdefault(y,v)
        E={y:(P[y][0]+I[y][0],P[y][1]) for y in P if y in I}
    yrs=[y for y in sorted(E) if y>=2014 and y in A]
    vals=[]
    print(k)
    for y in yrs:
        r=E[y][0]/A[y][0]*100; vals.append(r)
        print(f'  {y} EBIT {E[y][0]:8.1f} assets {A[y][0]:8.1f}  {r:5.1f}%  {E[y][1]}')
    sel=[E[y][0]/A[y][0]*100 for y in yrs if y>=2016]
    print(f'  mean 2016+: {sum(sel)/len(sel):.1f}%  over {len(sel)} yrs')
