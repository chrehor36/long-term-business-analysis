import sys,os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json
from facts import series
def inst(cik,tags):
    d=json.load(open(f'cache/facts_{cik}.json')); out={}
    for t in tags:
        f=d['facts'].get('us-gaap',{}).get(t)
        if not f: continue
        for u,vals in f['units'].items():
            for v in vals:
                if v.get('form')!='10-K' or 'start' in v: continue
                # fiscal year-end: take value whose 'end' equals the fy end of the filing's own period (fp FY)
                if v.get('fp')!='FY': continue
                yr=v['end'][:4] if v['end'][5:7] not in ('01',) else str(int(v['end'][:4])-1)
                if v['end'][:7]!=v.get('frame','')[:0]+v['end'][:7]: pass
                key=yr
                # only the balance at the filing's own fiscal year end: fy field equals year
                if str(v.get('fy'))!=yr and not (v['end'][5:7]=='01'): continue
                if key not in out or v['filed']<out[key][1]: out[key]=(v['val'],v['filed'],t)
        if out: pass
    return out
C={'GIC':'0000945114','GWW':'0000277135','FAST':'0000815556','MSM':'0001003078'}
REV=['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueGoodsNet']
for n,c in C.items():
    rev=series(c,REV); gp=series(c,['GrossProfit']); op=series(c,['OperatingIncomeLoss'])
    eq=inst(c,['StockholdersEquity']); eqm=inst(c,['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'])
    cash=inst(c,['CashAndCashEquivalentsAtCarryingValue']); gw=inst(c,['Goodwill']); ia=inst(c,['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'])
    dl=inst(c,['LongTermDebtNoncurrent','LongTermDebt']); dc=inst(c,['LongTermDebtCurrent','DebtCurrent','ShortTermBorrowings'])
    print('==',n)
    print('yr   sales   GP%   op%    opinc  tangCap  preTaxROTC')
    for y in [str(x) for x in range(2016,2026)]:
        if y not in rev: continue
        s=rev[y][0]/1e6; g=gp.get(y,(None,))[0]; o=op.get(y,(None,))[0]
        E=(eqm.get(y) or eq.get(y) or (None,))[0]
        tc=None
        if E is not None:
            tc=(E+(dl.get(y,(0,))[0])+(dc.get(y,(0,))[0])-(cash.get(y,(0,))[0])-(gw.get(y,(0,))[0])-(ia.get(y,(0,))[0]))/1e6
        print(y, round(s), (round(100*g/1e6/s,1) if g else '-'), (round(100*o/1e6/s,1) if o else '-'), (round(o/1e6) if o else '-'), (round(tc) if tc else '-'), (round(100*o/1e6/tc) if (o and tc) else '-'))
