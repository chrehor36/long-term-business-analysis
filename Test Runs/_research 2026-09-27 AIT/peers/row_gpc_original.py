"""Competitor row: same metric, same window, from SEC companyfacts (each figure is a tag from a filed 10-K).
Metrics per fiscal year:
  EBIT = pretax income + interest expense (same construction for every company; GPC files no operating-income line)
  margin = EBIT / revenue
  NTOA = assets - cash - goodwill - intangibles - operating ROU - (current liabilities - current debt - current lease liability)
  return = EBIT / NTOA (year-end), the ORLY run's construction, recomputed here for every name
  ROE = net income / average equity
Values are the first-filed figure for each period end (as filed), duration 340-380 days for flows.
"""
import json, sys, datetime
from collections import defaultdict

def load(t):
    return json.load(open(f'{t}_facts.json'))['facts']

def series(f, tags, flow=True):
    out = {}
    for tag in tags:
        for ns in ('us-gaap',):
            if tag not in f.get(ns, {}): continue
            u = f[ns][tag]['units'].get('USD')
            if not u: continue
            cand = defaultdict(list)
            for x in u:
                if not x['form'].startswith('10-K'): continue
                if flow:
                    if 'start' not in x: continue
                    d = (datetime.date.fromisoformat(x['end']) - datetime.date.fromisoformat(x['start'])).days
                    if not 340 <= d <= 380: continue
                if x.get('segment'): continue
                cand[x['end']].append(x)
            for e, xs in cand.items():
                xs.sort(key=lambda x: x['filed'])
                if e not in out: out[e] = xs[0]['val']
    return out

def fy(d):
    # map period end to fiscal year label (end year; ends in Jan/Feb count to prior year)
    r = {}
    for e, v in d.items():
        y = int(e[:4]); m = int(e[5:7])
        if m <= 2: y -= 1
        r.setdefault(y, v)
    return r

T = dict(
    rev=['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'SalesRevenueGoodsNet'],
    pti=['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic'],
    intx=['InterestExpense', 'InterestExpenseNonoperating', 'InterestExpenseDebt', 'InterestIncomeExpenseNonoperatingNet', 'InterestIncomeExpenseNet'],
    ni=['NetIncomeLoss', 'ProfitLoss'],
    A=['Assets'], C=['CashAndCashEquivalentsAtCarryingValue'], G=['Goodwill'],
    I=['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet'],
    R=['OperatingLeaseRightOfUseAsset'], L=['LiabilitiesCurrent'],
    CL=['OperatingLeaseLiabilityCurrent'],
    CD=['LongTermDebtCurrent', 'DebtCurrent'], SD=['ShortTermBorrowings', 'CommercialPaper'],
    E=['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
)

def run(t, y0=2011, y1=2025):
    f = load(t)
    s = {k: fy(series(f, v, flow=k in ('rev', 'pti', 'intx', 'ni'))) for k, v in T.items()}
    rows = []
    for y in range(y0, y1 + 1):
        g = lambda k: s[k].get(y)
        rev, pti, ix = g('rev'), g('pti'), g('intx')
        if rev is None or pti is None:
            rows.append((y, None)); continue
        ix = abs(ix or 0)
        ebit = pti + ix
        z = lambda k: g(k) or 0
        n = z('A') - z('C') - z('G') - z('I') - z('R') - (z('L') - z('CD') - z('SD') - z('CL'))
        e0, e1 = s['E'].get(y - 1), s['E'].get(y)
        roe = (g('ni') / ((e0 + e1) / 2)) if (e0 and e1 and g('ni') is not None and (e0 + e1) > 0) else None
        rows.append((y, dict(rev=rev, ebit=ebit, m=ebit / rev, ntoa=n, ret=(ebit / n if n > 0 else None), roe=roe)))
    return rows

if __name__ == '__main__':
    for t in sys.argv[1:]:
        print('==', t)
        for y, r in run(t):
            if r is None: print(y, 'incomplete'); continue
            pc=lambda v: '   n/a' if v is None else '%6.1f%%'%(v*100)
            print(y, 'rev %9.0f ebit %7.0f margin %5.1f%% NTOA %8.0f ret %s ROE %s'%(r['rev']/1e6,r['ebit']/1e6,r['m']*100,r['ntoa']/1e6,pc(r['ret']),pc(r['roe'])))
