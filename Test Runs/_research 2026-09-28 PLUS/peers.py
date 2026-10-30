import json,sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
def load(p): return json.load(open(p))['facts']['us-gaap']
def series(g,tags,dur=True):
    out={}
    for tag in tags:
        if tag not in g: continue
        for u,v in g[tag]['units'].items():
            if u!='USD': continue
            for x in v:
                if x.get('form') not in ('10-K','10-K/A','8-K'): continue
                if dur:
                    if 'start' not in x: continue
                    d=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days
                    if not 340<=d<=380: continue
                elif 'start' in x: continue
                e=x['end']
                if e not in out or x['filed']>out[e][1]: out[e]=(x['val'],x['filed'],tag)
        # first tag wins for any end it covers; continue to fill gaps
    return {k:v[0] for k,v in sorted(out.items())}
def first(g,taglist,dur=True):
    res={}
    for t in taglist:
        s=series(g,[t],dur)
        for k,v in s.items(): res.setdefault(k,v)
    return dict(sorted(res.items()))
REV=['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet']
GP=['GrossProfit']; OI=['OperatingIncomeLoss']
EQ=['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest']
CASH=['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents']
DEBT_LT=['LongTermDebtNoncurrent','LongTermDebt','LongTermDebtAndCapitalLeaseObligations','LongTermLineOfCredit','LongTermDebtAndFinanceLeaseObligations']
DEBT_C=['LongTermDebtCurrent','ShortTermBorrowings','DebtCurrent','LongTermDebtAndCapitalLeaseObligationsCurrent','LinesOfCreditCurrent']
import os
for t in sys.argv[1:]:
    p='cache/facts.json' if t=='PLUS' else f'cache/peers/{t}_facts.json'
    g=load(p)
    rev=first(g,REV); gp=first(g,GP); oi=first(g,OI); eq=first(g,EQ,False); cash=first(g,CASH,False)
    dl=first(g,DEBT_LT,False); dc=first(g,DEBT_C,False)
    print('=====',t)
    for e in sorted(oi):
        if e<'2012': continue
        r=rev.get(e); o=oi[e]; gg=gp.get(e)
        opcap=None
        if e in eq:
            opcap=eq[e]+dl.get(e,0)+dc.get(e,0)-cash.get(e,0)
        print(e, 'rev %.1f'%(r/1e6) if r else '-', 'GM %.1f%%'%(100*gg/r) if gg and r else '-', 'OI %.1f'%(o/1e6), 'OM %.1f%%'%(100*o/r) if r else '-',
              'eq %.0f debt %.0f cash %.0f'%(eq.get(e,0)/1e6,(dl.get(e,0)+dc.get(e,0))/1e6,cash.get(e,0)/1e6), 'OI/opcap %.1f%%'%(100*o/opcap) if opcap else '-')
