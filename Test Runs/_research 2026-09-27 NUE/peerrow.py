"""Competitor row, arithmetic only. Same metrics, same windows, each filer's own 10-K/20-F facts (companyfacts, newest filed vintage).
Metric A: net income attributable to the parent / average parent equity (year-end pair). Metric B: pre-tax income / revenue.
Fiscal year labelled by the calendar year of its end date."""
import json,sys,io
from datetime import date
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def facts(p): return json.load(open(p))['facts']
def ann(F,tags,inst=False,forms=('10-K','20-F','40-F')):
    out={}
    for ns,tag in tags:
        try: u=F[ns][tag]['units']
        except KeyError: continue
        for unit,L in u.items():
            if unit not in ('USD',): continue
            for x in L:
                if not x.get('form','').startswith(forms): continue
                if not inst:
                    if 'start' not in x: continue
                    d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                    if d<350 or d>380: continue
                y=int(x['end'][:4]) if x['end'][5:7]!='01' else int(x['end'][:4])-1
                k=(y)
                if k not in out or (x['filed'],)>(out[k][1],): out[k]=(x['val'],x['filed'],tag)
    return {k:v[0] for k,v in out.items()}
G='us-gaap'; I='ifrs-full'
NI=[(G,'NetIncomeLoss'),(G,'NetIncomeLossAvailableToCommonStockholdersBasic'),(I,'ProfitLossAttributableToOwnersOfParent')]
REV=[(G,'Revenues'),(G,'SalesRevenueNet'),(G,'RevenueFromContractWithCustomerExcludingAssessedTax'),(G,'SalesRevenueGoodsNet'),(I,'Revenue')]
PT=[(G,'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'),(G,'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'),(I,'ProfitLossBeforeTax')]
EQ=[(G,'StockholdersEquity'),(I,'EquityAttributableToOwnersOfParent')]
def merge(F,tags,inst=False):
    m={}
    for t in tags:
        a=ann(F,[t],inst)
        for k,v in a.items():
            if k not in m: m[k]=v
    return m
rows={}
names=['NUE','STLD','CMC','CLF','X','MTUS','RDUS','MT']
Y=range(2007,2026)
for n in names:
    F=facts('companyfacts.json' if n=='NUE' else 'peers/%s_facts.json'%n)
    ni=merge(F,NI); rev=merge(F,REV); pt=merge(F,PT); eq=merge(F,EQ,inst=True)
    A={};B={}
    for y in Y:
        if y in ni and y in eq and (y-1) in eq and (eq[y]+eq[y-1])>0: A[y]=ni[y]/((eq[y]+eq[y-1])/2)
        if y in pt and y in rev and rev[y]: B[y]=pt[y]/rev[y]
    rows[n]=(A,B)
def fmt(d,y): return f'{d[y]*100:.1f}' if y in d else 'n/f'
print('METRIC A: net income to parent / average parent equity, %')
print('| FY | '+' | '.join(names)+' |'); print('|'+'---|'*(len(names)+1))
for y in Y: print(f'| {y} | '+' | '.join(fmt(rows[n][0],y) for n in names)+' |')
print('METRIC B: pre-tax income / revenue, %')
print('| FY | '+' | '.join(names)+' |'); print('|'+'---|'*(len(names)+1))
for y in Y: print(f'| {y} | '+' | '.join(fmt(rows[n][1],y) for n in names)+' |')
import statistics as S
for lab,idx in (('A',0),('B',1)):
    print('SUMMARY',lab)
    for n in names:
        d=rows[n][idx]; ys=sorted(d)
        if not ys: print(n,'none'); continue
        v=[d[y] for y in ys]
        com=[y for y in range(2008,2026) if all(y in rows[m][idx] for m in ('NUE','STLD','CMC'))]
        vc=[d[y] for y in com if y in d]
        print(f'{n}: years {ys[0]}-{ys[-1]} (n={len(ys)}) mean {S.mean(v)*100:.1f} median {S.median(v)*100:.1f} min {min(v)*100:.1f} ({ys[v.index(min(v))]}) max {max(v)*100:.1f} ({ys[v.index(max(v))]}) negatives {sum(1 for x in v if x<0)} | common NUE/STLD/CMC window {com[0] if com else None}-{com[-1] if com else None} mean {S.mean(vc)*100 if vc else float("nan"):.1f} median {S.median(vc)*100 if vc else float("nan"):.1f}')
