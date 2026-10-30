# Annual operating margin and pre-tax return on capital employed from XBRL company facts (transcription; checked against filings in the run file).
# Capital employed = total equity + debt (current and noncurrent borrowings) - cash and short-term investments, at year end.
import json, sys, os
UNIT = None
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
def series(f, taxo, tags, kind='dur'):
    g = f['facts'].get(taxo, {})
    out = {}
    for t in tags:
        if t not in g: continue
        for u, arr in g[t]['units'].items():
            if UNIT and u != UNIT: continue
            for x in arr:
                if x.get('form') not in ('10-K', '20-F', '10-K/A', '20-F/A'): continue
                if kind == 'dur':
                    if 'start' not in x: continue
                    from datetime import date
                    s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                    if not (350 <= (e - s).days <= 380): continue
                    y = e.year if e.month > 6 else e.year - 1
                else:
                    if 'start' in x: continue
                    e = x['end']; y = int(e[:4]) if int(e[5:7]) > 6 else int(e[:4]) - 1
                out.setdefault(y, x['val'])
    return out
cfg = {
 'COKE': ('us-gaap', ['RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','Revenues'], ['OperatingIncomeLoss'], ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'], ['LongTermDebtNoncurrent','LongTermDebtCurrent'], ['CashAndCashEquivalentsAtCarryingValue']),
 'KDP': ('us-gaap', ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'], ['OperatingIncomeLoss'], ['StockholdersEquity'], ['LongTermDebtNoncurrent','LongTermDebtCurrent','ShortTermBorrowings','CommercialPaper'], ['CashAndCashEquivalentsAtCarryingValue']),
 'PEP': ('us-gaap', ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'], ['OperatingIncomeLoss'], ['StockholdersEquity'], ['LongTermDebtNoncurrent','ShortTermBorrowings','DebtCurrent'], ['CashAndCashEquivalentsAtCarryingValue']),
 'KO':  ('us-gaap', ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet'], ['OperatingIncomeLoss'], ['StockholdersEquity'], ['LongTermDebtAndCapitalLeaseObligations','LongTermDebtAndCapitalLeaseObligationsCurrent','ShortTermBorrowings'], ['CashAndCashEquivalentsAtCarryingValue']),
 'CCEP':('ifrs-full', ['Revenue'], ['ProfitLossFromOperatingActivities'], ['Equity'], ['Borrowings'], ['CashAndCashEquivalents']),
 'KOF': ('ifrs-full', ['Revenue'], ['ProfitLossFromOperatingActivities'], ['Equity'], ['LongtermBorrowings','CurrentPortionOfLongtermBorrowings','ShorttermBorrowings'], ['CashAndCashEquivalents']),
}
for t in sys.argv[1:]:
    UNIT = 'MXN' if t == 'KOF' else ('EUR' if t == 'CCEP' else 'USD')
    taxo, rt, ot, et, dt, ct = cfg[t]
    f = json.load(open(os.path.join(C, t + '_companyfacts.json')))
    rev = {}; 
    for tag in rt:
        for k, v in series(f, taxo, [tag]).items(): rev.setdefault(k, v)
    oi = series(f, taxo, ot); eq = series(f, taxo, et, 'inst'); cash = series(f, taxo, ct, 'inst')
    debt = {}
    for tag in dt:
        for k, v in series(f, taxo, [tag], 'inst').items(): debt[k] = debt.get(k, 0) + v
    print(t, 'year  revenue  op.income  margin  capital  pretax-ROCE')
    for y in sorted(set(rev) & set(oi)):
        if y < 2008: continue
        cap = eq.get(y, 0) + debt.get(y, 0) - cash.get(y, 0) if y in eq else None
        print(f"  {y} {rev[y]/1e6:10.0f} {oi[y]/1e6:9.0f} {100*oi[y]/rev[y]:6.1f}%", f"{cap/1e6:9.0f} {100*oi[y]/cap:6.1f}%" if cap else '  n/a', f"eq {eq.get(y,0)/1e6:.0f} debt {debt.get(y,0)/1e6:.0f} cash {cash.get(y,0)/1e6:.0f}")
