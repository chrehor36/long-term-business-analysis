import sys; sys.path.insert(0, 'scripts')
from xbrl import load, annual, first
def yr(k): return k[:4]
def series(cik, ns='us-gaap'):
    f = load(cik)
    if ns == 'us-gaap':
        rev = first(f, ['RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax','Revenues','SalesRevenueNet','SalesRevenueGoodsNet'])
        pti = first(f, ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'])
        intx = first(f, ['InterestExpense','InterestExpenseNonoperating','InterestExpenseNet','InterestIncomeExpenseNonoperatingNet'])
        eq = first(f, ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'], instant=True)
        cash = first(f, ['CashAndCashEquivalentsAtCarryingValue'], instant=True)
        sti = first(f, ['ShortTermInvestments'], instant=True)
        debt = first(f, ['LongTermDebt','LongTermDebtNoncurrent'], instant=True)
        ocf = first(f, ['NetCashProvidedByUsedInOperatingActivities'])
        capex = first(f, ['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'])
        acq = first(f, ['PaymentsToAcquireBusinessesNetOfCashAcquired'])
        sbc = first(f, ['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'])
    else:
        rev = first(f, ['Revenue','RevenueFromContractsWithCustomers'], ns='ifrs-full')
        pti = first(f, ['ProfitLossBeforeTax'], ns='ifrs-full')
        intx = first(f, ['FinanceCosts','InterestExpense'], ns='ifrs-full')
        eq = first(f, ['Equity'], ns='ifrs-full', instant=True)
        cash = first(f, ['CashAndCashEquivalents'], ns='ifrs-full', instant=True)
        sti = {}
        debt = first(f, ['Borrowings','NoncurrentPortionOfNoncurrentBorrowings'], ns='ifrs-full', instant=True)
        ocf = first(f, ['CashFlowsFromUsedInOperatingActivities'], ns='ifrs-full')
        capex = first(f, ['PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities'], ns='ifrs-full')
        acq = {}; sbc = {}
    by = {}
    for k, v in rev.items():
        y = yr(k)
        if y < '2014': continue
        r = dict(rev=v)
        def g(d):
            for kk, vv in d.items():
                if yr(kk) == y: return vv
            return None
        r.update(pti=g(pti), int=g(intx), eq=g(eq), cash=g(cash), sti=g(sti) or 0, debt=g(debt), ocf=g(ocf), capex=g(capex), acq=g(acq) or 0, sbc=g(sbc) or 0)
        by[y] = r
    return by
names = {'0000022444':'CMC','0000073309':'NUE','0001022671':'STLD','0001073404':'GGB'}
for cik, nm in names.items():
    s = series(cik, 'ifrs-full' if nm=='GGB' else 'us-gaap')
    print(f"== {nm}  (USD or BRL millions; ebit=pretax+interest; ROC=ebit/(equity+debt-cash-sti) prior-year-end capital)")
    prev = None
    for y in sorted(s):
        r = s[y]
        ebit = (r['pti'] or 0) + abs(r['int'] or 0)
        cap = None
        if prev and prev.get('eq') is not None:
            cap = prev['eq'] + (prev['debt'] or 0) - (prev['cash'] or 0) - (prev['sti'] or 0)
        m = ebit / r['rev'] if r['rev'] else None
        fcf = (r['ocf'] or 0) - (r['capex'] or 0) - (r['sbc'] or 0)
        print(y, f"rev {r['rev']/1e6:9.0f} ebit {ebit/1e6:8.0f} margin {m*100:5.1f}%", f"ROC {ebit/cap*100:5.1f}%" if cap else "ROC   n/a", f"ocf-capex-sbc {fcf/1e6:8.0f}", f"acq {r['acq']/1e6:6.0f}")
        prev = r
