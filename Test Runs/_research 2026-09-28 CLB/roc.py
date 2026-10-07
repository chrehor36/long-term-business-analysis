# consolidated operating income (filed MD&A table, latest vintage) and pre-tax return on net tangible capital
import json, re, statistics as S
def num(s): s=s.strip().replace(',','').replace('$','').strip(); neg=s.startswith('('); s=s.strip('( )'); return -float(s) if neg else float(s)
oi={}; rev={}
for y in range(2007,2026):
    try: t=open(f'cache/t{y}.txt',encoding='utf-8').read().split('\n')
    except: continue
    for l in t:
        if re.match(r'^OPERATING INCOME( \(LOSS\))? \|', l):
            c=[x for x in l.split('|')[1:]]
            vals=[num(x) for x in c if re.search(r'\d{2},\d{3}',x)]
            # first three thousands-sized values are years y, y-1, y-2
            for k,v in enumerate(vals[:3]): oi[y-k]=v/1000   # years ascending: the latest filing's figure wins
            break
# revenue from tags (latest vintage, both CIKs)
def dur(f,t):
    from datetime import date
    o={}
    if t not in f: return o
    for u,a in f[t]['units'].items():
        for x in a:
            if x.get('form') in ('10-K','10-K/A') and 'start' in x and 350<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=380: o[int(x['end'][:4])]=x['val']/1e6
    return o
def inst(f,t):
    o={}
    if t not in f: return o
    for u,a in f[t]['units'].items():
        for x in a:
            if x.get('form') in ('10-K','10-K/A') and 'start' not in x: o[int(x['end'][:4])]=x['val']/1e6
    return o
F=[json.load(open(f'cache/facts_{k}.json'))['facts']['us-gaap'] for k in ('nv','new')]
def merge(fn,tags):
    o={}
    for f in F:
        for t in tags:
            for k,v in fn(f,t).items(): o.setdefault(k,v)
    return o
rev=merge(dur,['RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','Revenues'])
for f in F:  # newest vintage for revenue where both exist
    for k,v in dur(f,'RevenueFromContractWithCustomerExcludingAssessedTax').items(): rev[k]=v
eq=merge(inst,['StockholdersEquity']); debt=merge(inst,['LongTermDebt','LongTermDebtNoncurrent'])
cash=merge(inst,['CashAndCashEquivalentsAtCarryingValue']); gw=merge(inst,['Goodwill']); ia=merge(inst,['IntangibleAssetsNetExcludingGoodwill'])
for f in F:
    for d,t in ((eq,'StockholdersEquity'),(debt,'LongTermDebt'),(cash,'CashAndCashEquivalentsAtCarryingValue'),(gw,'Goodwill'),(ia,'IntangibleAssetsNetExcludingGoodwill')):
        for k,v in inst(f,t).items(): d[k]=v
print('FY | revenue | op inc | op margin | equity | debt | cash | goodwill | intangibles | net tangible capital | pre-tax return')
rs=[]
for y in range(2007,2026):
    o=oi.get(y); r=rev.get(y)
    line=f"{y} | {r:,.1f} | " if r else f"{y} | n/a | "
    line+= f"{o:,.1f} | {100*o/r:.1f}%" if (o is not None and r) else 'n/a | n/a'
    if all(y in d for d in (eq,debt,cash,gw)):
        ntc=eq[y]+debt[y]-cash[y]-gw[y]-ia.get(y,0)
        line+=f" | {eq[y]:,.1f} | {debt[y]:,.1f} | {cash[y]:,.1f} | {gw[y]:,.1f} | {ia.get(y,float('nan')):,.1f} | {ntc:,.1f}"
        if o is not None: line+=f" | {100*o/ntc:.1f}%"; rs.append((y,o/ntc))
    print(line)
print('mean return 2009-2015', round(100*S.mean(r for y,r in rs if y<=2015),1), '| 2016-2025', round(100*S.mean(r for y,r in rs if y>=2016),1), '| 2021-2025', round(100*S.mean(r for y,r in rs if y>=2021),1))
