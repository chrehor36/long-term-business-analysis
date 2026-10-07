import json,datetime,sys
sys.stdout.reconfigure(encoding='utf-8')
def load(t):
    return json.load(open(f'{t}_facts.json'))['facts']['us-gaap']
def ann(F,tags,inst=False,month=None):
    out={}
    for tag in tags:
        if tag not in F: continue
        for unit,vals in F[tag]['units'].items():
            if unit!='USD': continue
            for v in vals:
                if v.get('form') not in ('10-K','10-K/A'): continue
                e=datetime.date.fromisoformat(v['end'])
                if inst:
                    if v.get('start'): continue
                else:
                    if not v.get('start'): continue
                    s=datetime.date.fromisoformat(v['start'])
                    if not 340<(e-s).days<380: continue
                fy=e.year
                if month and abs(e.month-month)>1 and not (month==12 and e.month==1): continue
                k=fy
                if k not in out or (tag==tags[0] and out[k][2]!=tags[0]) or (v['filed']>out[k][1] and out[k][2]==tag):
                    if k in out and out[k][2]==tags[0] and tag!=tags[0]: continue
                    out[k]=(v['val'],v['filed'],tag)
    return {k:v[0] for k,v in out.items()}
T=sys.argv[1]; month=int(sys.argv[2])
F=load(T)
rev=ann(F,['RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','Revenues','SalesRevenueNet','SalesRevenueGoodsNet'],month=month)
oi=ann(F,['OperatingIncomeLoss'],month=month)
A=ann(F,['Assets'],True,month); CA=ann(F,['AssetsCurrent'],True,month); CL=ann(F,['LiabilitiesCurrent'],True,month)
cash=ann(F,['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents'],True,month)
gw=ann(F,['Goodwill'],True,month); ia=ann(F,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],True,month)
std=ann(F,['LongTermDebtCurrent','DebtCurrent','LineOfCredit'],True,month)
print(T,'fiscal year keyed by the calendar year in which it ends; fiscal year-end month',month)
print('fy  sales  opinc  opmargin%  capital_incl_gw  pretax_return_incl_gw%  ntoa  return_on_ntoa%')
prevc=None;prevn=None
for y in sorted(rev):
    if y<2015: continue
    r=rev[y]; o=oi.get(y)
    cap=None;nt=None
    if y in A and y in CL:
        cap=A[y]-cash.get(y,0)-(CL[y]-std.get(y,0))
        nt=cap-gw.get(y,0)-ia.get(y,0)
    s=f'{y} {r/1e6:9.1f} '
    s+=(f'{o/1e6:8.1f} {100*o/r:6.1f}' if o is not None else '      --      --')
    if cap:
        avgc=(cap+prevc)/2 if prevc else cap; avgn=(nt+prevn)/2 if prevn else nt
        s+=f' {cap/1e6:9.1f} '+(f'{100*o/avgc:6.1f}' if o is not None else '--')
        s+=f' {nt/1e6:8.1f} '+(f'{100*o/avgn:6.1f}' if o is not None and avgn>0 else '--')
        prevc=cap;prevn=nt
    print(s)
