import sys; sys.path.insert(0,'.')
from field import co, series
T = {'rev':['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax'],
     'pti':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'],
     'op':['OperatingIncomeLoss'],
     'int':['InterestExpense','InterestExpenseDebt'],
     'eq':['StockholdersEquity'],
     'ltd':['LongTermDebtNoncurrent','LongTermDebt'], 'std':['LongTermDebtCurrent','DebtCurrent','ShortTermBorrowings','ShortTermDebtAndCurrentPortionOfLongTermDebt']}
out = []
for c, paths in co.items():
    d = {k: series(paths, t) for k, t in T.items()}
    print(f'== {c}  year  revenue  EBIT(pti+int)  margin  opinc_asfiled  book cap(eq+debt)  EBIT/bookcap')
    S = {}
    for y in range(2008, 2026):
        rev = d['rev'].get(y); pti = d['pti'].get(y); it = abs(d['int'].get(y) or 0)
        if pti is None and d['op'].get(y) is not None: ebit = d['op'][y]; src='op'
        elif pti is not None: ebit = pti + it; src='pti'
        else: ebit=None
        bc = (d['eq'].get(y) or 0) + (d['ltd'].get(y) or 0) + (d['std'].get(y) or 0)
        if rev and ebit is not None:
            S[y] = (rev, ebit, bc)
            print(f'  {y} {rev:8.0f} {ebit:8.0f}{"*" if src=="op" else " "} {100*ebit/rev:6.1f}%  {d["op"].get(y,float("nan")):8.0f}  {bc:8.0f}  {100*ebit/bc:6.1f}%')
    for a,b in [(2008,2014),(2015,2025),(2008,2025),(2012,2025)]:
        ys=[y for y in S if a<=y<=b]
        if not ys: continue
        R=sum(S[y][0] for y in ys); E=sum(S[y][1] for y in ys); C=sum(S[y][2] for y in ys)
        print(f'   {a}-{b} ({len(ys)}y): cum EBIT {E:8.0f} / cum rev {R:8.0f} = {100*E/R:5.1f}%;  avg EBIT/avg book capital {100*E/C:5.1f}%')
