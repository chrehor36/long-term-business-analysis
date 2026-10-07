import json
from datetime import date
def annual(d,tags):
    best={}
    for t in tags:
        if t not in d: continue
        for unit,arr in d[t]['units'].items():
            for f in arr:
                if 'start' not in f or not f['form'].startswith(('10-K','40-F','20-F','6-K')): continue
                s=date.fromisoformat(f['start']); e=date.fromisoformat(f['end'])
                if not 350<(e-s).days<380: continue
                y=e.year
                # newest filed wins
                if y not in best or f['filed']>best[y][1]: best[y]=(f['val'],f['filed'],unit,t)
        if best: pass
    return best
def inst(d,tags):
    best={}
    for t in tags:
        if t not in d: continue
        for unit,arr in d[t]['units'].items():
            for f in arr:
                if 'start' in f or not f['form'].startswith(('10-K','40-F','20-F','6-K')): continue
                e=f['end']
                if e[5:]!='12-31': continue
                y=int(e[:4])
                if y not in best or f['filed']>best[y][1]: best[y]=(f['val'],f['filed'],unit,t)
    return best
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','OperatingRevenue','RevenueFromContractWithCustomerIncludingAssessedTax']
OPI=['OperatingIncomeLoss']
OPX=['CostsAndExpenses','OperatingExpenses','OperatingCostsAndExpenses']
PPE=['PropertyPlantAndEquipmentNet']
NI=['NetIncomeLoss','ProfitLoss']
EQ=['StockholdersEquity','MembersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']
out={}
for t in ('UNP','BNSF','CSX','NSC','CP','CNI'):
    d=json.load(open(f'peers/{t}_facts.json'))['facts']['us-gaap']
    def first(tags,f=annual):
        for tg in tags:
            r=f(d,[tg])
            if r: yield tg,r
    rv={};oi={};pp={};ni={};eq={}
    for tg,r in first(REV):
        for y,v in r.items():
            if y not in rv or v[0]>rv[y][0]: rv[y]=v
    for tg,r in first(OPI):
        for y,v in r.items(): oi.setdefault(y,v)
    for tg,r in first(PPE,inst):
        for y,v in r.items(): pp.setdefault(y,v)
    for tg,r in first(NI):
        for y,v in r.items(): ni.setdefault(y,v)
    for tg,r in first(EQ,inst):
        for y,v in r.items(): eq.setdefault(y,v)
    print('==',t, 'units', set(v[2] for v in rv.values()))
    row={}
    for y in range(2009,2026):
        if y in rv and y in oi:
            orr=100*(1-oi[y][0]/rv[y][0])
            rop=None
            if y in pp and (y-1) in pp: rop=100*oi[y][0]/((pp[y][0]+pp[y-1][0])/2)
            roe=None
            if y in ni and y in eq and (y-1) in eq: roe=100*ni[y][0]/((eq[y][0]+eq[y-1][0])/2)
            row[y]=(round(orr,1), round(rop,1) if rop else None, round(roe,1) if roe else None, round(rv[y][0]/1e6))
            print(y, row[y], rv[y][3], oi[y][1])
    out[t]=row
json.dump(out,open('peerrow.json','w'),indent=0)
