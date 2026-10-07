import json
f=json.load(open('cache/facts.json'))['facts']['us-gaap']
def inst(t):
    o={}
    if t not in f: return o
    for u,a in f[t]['units'].items():
        for x in a:
            if x.get('form')=='10-K' and 'start' not in x: o[int(x['end'][:4])]=x['val']
    return o
def dur(t):
    from datetime import date
    o={}
    for u,a in f[t]['units'].items():
        for x in a:
            if x.get('form')=='10-K' and 'start' in x and 350<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=380: o[int(x['end'][:4])]=x['val']
    return o
eq=inst('StockholdersEquity'); cash=inst('CashAndCashEquivalentsAtCarryingValue')
d1=inst('LongTermDebt'); d2=inst('LongTermDebtNoncurrent'); d3=inst('SeniorNotes')
oi=dur('OperatingIncomeLoss'); rev=dur('Revenues')
print('tags LongTermDebtNoncurrent', sorted(d2.items())[-12:] if d2 else None)
print('FY | op inc | equity | debt | cash | net capital | pre-tax return on net capital')
rs=[]
for y in range(2008,2026):
    d=d1.get(y, d2.get(y, d3.get(y)))
    if d is None: print(y,'debt n/a'); continue
    nc=eq[y]+d-cash[y]; r=oi[y]/nc; rs.append((y,r))
    print(f'{y} | {oi[y]/1e6:,.1f} | {eq[y]/1e6:,.1f} | {d/1e6:,.1f} | {cash[y]/1e6:,.1f} | {nc/1e6:,.1f} | {100*r:.1f}%')
import statistics as S
print('mean all', round(100*S.mean(r for y,r in rs),1), 'n',len(rs))
print('mean 2016-2025', round(100*S.mean(r for y,r in rs if y>=2016),1))
print('mean 2008-2015', round(100*S.mean(r for y,r in rs if y<=2015),1))
