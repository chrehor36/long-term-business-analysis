"""Competitor row for CSCO. Per fiscal year, from each filer's companyfacts, FIRST-FILED 10-K value per period end:
revenue = largest of the revenue tags; gross margin = GrossProfit / revenue (or revenue - CostOfRevenue);
operating margin = OperatingIncomeLoss / revenue; SBC = ShareBasedCompensation (cash-flow add-back), else AllocatedShareBasedCompensationExpense;
OCF = NetCashProvidedByUsedInOperatingActivities; capex = PaymentsToAcquirePropertyPlantAndEquipment.
Fiscal year labelled by the calendar year in which it ends (Jan/Feb ends count to the prior year)."""
import json, sys, io, datetime
from collections import defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def load(t): return json.load(open(f'{t}_facts.json'))['facts'].get('us-gaap',{})
def series(f, tags):
    out = {}
    for tag in tags:
        if tag not in f: continue
        u = f[tag]['units'].get('USD')
        if not u: continue
        cand = defaultdict(list)
        for x in u:
            if not x['form'].startswith('10-K') or 'start' not in x: continue
            d = (datetime.date.fromisoformat(x['end']) - datetime.date.fromisoformat(x['start'])).days
            if not 340 <= d <= 380: continue
            cand[x['end']].append(x)
        for e, xs in cand.items():
            xs.sort(key=lambda x: x['filed'])
            if e not in out: out[e] = xs[0]['val']
    r = {}
    for e, v in out.items():
        y = int(e[:4]); m = int(e[5:7])
        if m <= 2: y -= 1
        r.setdefault(y, v)
    return r
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
def revmax(f):
    best={}
    for t in REV:
        for y,v in series(f,[t]).items():
            if v>best.get(y,0): best[y]=v
    return best
def run(t):
    f=load(t); rev=revmax(f); gp=series(f,['GrossProfit']); cor=series(f,['CostOfRevenue','CostOfGoodsAndServicesSold'])
    oi=series(f,['OperatingIncomeLoss']); sbc=series(f,['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'])
    ocf=series(f,['NetCashProvidedByUsedInOperatingActivities']); cap=series(f,['PaymentsToAcquirePropertyPlantAndEquipment'])
    rd=series(f,['ResearchAndDevelopmentExpense','ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost'])
    rows={}
    for y in range(2011,2027):
        if y not in rev: continue
        R=rev[y]; G=gp.get(y) if y in gp else (R-cor[y] if y in cor else None)
        rows[y]=dict(rev=R, gm=G/R if G is not None else None, om=oi[y]/R if y in oi else None, sbc=sbc.get(y), ocf=ocf.get(y), cap=cap.get(y), rd=rd[y]/R if y in rd else None)
    return rows
def mean(xs):
    xs=[x for x in xs if x is not None]; return sum(xs)/len(xs) if xs else None
out={}
P=lambda v: '  n/a' if v is None else '%5.1f%%'%(v*100)
for t in sys.argv[1:]:
    r=run(t); out[t]=r
    print('==',t)
    for y,x in r.items(): print(y,'rev %8.0f gm %s om %s rd %s sbc/ocf %s'%(x['rev']/1e6,P(x['gm']),P(x['om']),P(x['rd']),P(x['sbc']/x['ocf'] if x['sbc'] and x['ocf'] and x['ocf']>0 else None)))
    for a,b in ((2016,2025),(2021,2025)):
        ys=[y for y in range(a,b+1) if y in r]
        if not ys: continue
        g=mean([r[y]['gm'] for y in ys]); o=mean([r[y]['om'] for y in ys])
        cagr=(r[ys[-1]]['rev']/r[ys[0]]['rev'])**(1/(ys[-1]-ys[0]))-1 if len(ys)>1 else None
        so=sum(r[y]['sbc'] or 0 for y in ys)/sum(r[y]['ocf'] or 0 for y in ys) if sum(r[y]['ocf'] or 0 for y in ys)>0 else None
        print(f'  {a}-{b} ({ys[0]}-{ys[-1]}, {len(ys)}y): GM {P(g)} OM {P(o)} OM range {P(min(r[y]["om"] for y in ys if r[y]["om"] is not None))}..{P(max(r[y]["om"] for y in ys if r[y]["om"] is not None))} rev CAGR {P(cagr)} SBC/OCF {P(so)}')
json.dump(out,open('row.json','w'),indent=0)
