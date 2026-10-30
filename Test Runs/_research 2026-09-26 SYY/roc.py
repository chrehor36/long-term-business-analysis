import json,sys
from datetime import date
def load(fn):
    return json.load(open(fn))['facts']['us-gaap']
def pick(f,tags,inst):
    out={}
    for t in tags:
        d=f.get(t)
        if not d: continue
        for x in d['units'].get('USD',[]):
            if x.get('form') not in ('10-K',): continue
            if not inst:
                if 'start' not in x: continue
                if not 350<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=380: continue
            k=x['end']
            if k not in out: out[k]=x['val']/1e6
    return out
def run(fn,label):
    f=load(fn)
    oi=pick(f,['OperatingIncomeLoss'],False)
    eq=pick(f,['StockholdersEquity'],True); cash=pick(f,['CashAndCashEquivalentsAtCarryingValue'],True)
    gw=pick(f,['Goodwill'],True); ig=pick(f,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],True)
    ltd=pick(f,['LongTermDebtNoncurrent','LongTermDebtAndCapitalLeaseObligations'],True)
    std=pick(f,['LongTermDebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent','DebtCurrent'],True)
    stb=pick(f,['ShortTermBorrowings','CommercialPaper'],True)
    print('===',label,'end | OI | debt | equity | cash | capital | OI/capital | GW+intang | OI/tangible capital')
    for e in sorted(oi):
        if e not in eq: continue
        d=ltd.get(e,0)+std.get(e,0)+stb.get(e,0); c=d+eq[e]-cash.get(e,0); g=gw.get(e,0)+ig.get(e,0)
        print(e, f"{oi[e]:7.0f} {d:7.0f} {eq[e]:7.0f} {cash.get(e,0):6.0f} {c:7.0f} {100*oi[e]/c:6.1f}% {g:7.0f} {100*oi[e]/(c-g) if c-g>0 else float('nan'):6.1f}%")
run('companyfacts.json','SYY')
run('peers/USFD_facts.json','USFD')
run('peers/PFGC_facts.json','PFGC')
