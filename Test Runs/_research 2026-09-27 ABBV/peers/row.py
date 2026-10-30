"""ABBV competitor row (the MRK run row.py, copied unchanged in its arithmetic). Arithmetic only, from SEC companyfacts (10-K / 20-F annual facts, newest filed vintage).
Metrics: net sales, operating profit as filed, operating margin, pre-tax return on average net tangible operating
assets (the CL/KVUE row construction: assets less cash, short-term investments, goodwill, intangibles and operating
ROU assets, less current liabilities other than debt and current lease liabilities), goodwill+intangibles share of
operating capital, pre-tax return on average operating capital INCLUDING goodwill and intangibles.
Keyed by fiscal-year END DATE. Usage: python row.py FACTS.json [from_year]"""
import json, sys, io
from datetime import date
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
FN = sys.argv[1]
FROM = sys.argv[2] if len(sys.argv) > 2 else '2014-06-01'
FACTS = json.load(open(FN, encoding='utf-8'))['facts']
FORMS = ('10-K', '10-K/A', '20-F', '20-F/A')

def ser(tag, instant=False):
    out = {}
    for tax in ('us-gaap', 'ifrs-full'):
        F = FACTS.get(tax, {})
        if tag not in F: continue
        for u, arr in F[tag]['units'].items():
            for x in arr:
                if x.get('form') not in FORMS: continue
                if not instant:
                    if 'start' not in x: continue
                    d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                    if not 340 <= d <= 380: continue
                elif 'start' in x: continue
                e = x['end']
                if e not in out or x['filed'] > out[e][1]: out[e] = (x['val'], x['filed'], u)
    return {k: v[0] for k, v in out.items()}, {v[2] for v in out.values()}

def first(tags, instant=False):
    d = {}; units = set()
    for t in tags:
        s, u = ser(t, instant)
        if s: units |= u
        for k, v in s.items(): d.setdefault(k, v)
    return d, units

M = 1e6
sales, su = first(['RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues', 'SalesRevenueNet', 'SalesRevenueGoodsNet', 'Revenue', 'RevenueFromContractsWithCustomers', 'RevenueFromSaleOfGoods'])
op, _ = first(['OperatingIncomeLoss', 'ProfitLossFromOperatingActivities'])
OPSRC = 'as filed'
if not [k for k in op if k >= '2020']:
    pt, _ = first(['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments', 'ProfitLossBeforeTax'])
    ie, _ = first(['InterestExpense', 'InterestExpenseNonoperating', 'InterestExpenseDebt'])
    op = {k: v + (ie.get(k) or 0) for k, v in pt.items()}
    OPSRC = 'PROXY: pre-tax income plus interest expense (no operating-income tag filed)'
assets, _ = first(['Assets'], True)
cash, _ = first(['CashAndCashEquivalentsAtCarryingValue', 'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents', 'CashAndCashEquivalents'], True)
sti, _ = first(['ShortTermInvestments', 'AvailableForSaleSecuritiesDebtSecuritiesCurrent', 'MarketableSecuritiesCurrent', 'CurrentInvestments', 'OtherCurrentFinancialAssets'], True)
gw, _ = first(['Goodwill'], True)
it, _ = first(['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet', 'IntangibleAssetsOtherThanGoodwill'], True)
rou, _ = first(['OperatingLeaseRightOfUseAsset'], True)
cl, _ = first(['LiabilitiesCurrent', 'CurrentLiabilities'], True)
debtc, _ = first(['DebtCurrent', 'CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings'], True)
stb, _ = first(['ShortTermBorrowings', 'CommercialPaper', 'LoansAndNotesPayable'], True)
ltdc, _ = first(['LongTermDebtCurrent', 'LongTermDebtAndCapitalLeaseObligationsCurrent'], True)
leasec, _ = first(['OperatingLeaseLiabilityCurrent'], True)
ends = [e for e in sorted(set(assets) & set(cl)) if e >= FROM]
print(FN, 'sales unit', su, '| operating profit:', OPSRC)
print('| FY end | sales | op profit | op margin | NTOA | ret avg NTOA | gw+intang | gw share | ret incl gw+intang |')
print('|---|---|---|---|---|---|---|---|---|')
prev = prevc = None; rows = []
for e in ends:
    d = debtc.get(e)
    if d is None: d = (stb.get(e) or 0) + (ltdc.get(e) or 0)
    ntoa = ((assets[e] - (cash.get(e) or 0) - (sti.get(e) or 0) - (gw.get(e) or 0) - (it.get(e) or 0) - (rou.get(e) or 0)) - (cl[e] - d - (leasec.get(e) or 0))) / M
    g = ((gw.get(e) or 0) + (it.get(e) or 0)) / M; cap = ntoa + g
    s = sales.get(e); o = op.get(e)
    avg = (ntoa + prev) / 2 if prev is not None else None
    avgc = (cap + prevc) / 2 if prevc is not None else None
    f = lambda v, sp='{:,.0f}': sp.format(v) if v is not None else 'n/f'
    print(f"| {e} | {f(s/M if s else None)} | {f(o/M if o is not None else None)} | {f(o/s if o is not None and s else None,'{:.1%}')} | {f(ntoa)} | {f(o/M/avg if o is not None and avg else None,'{:.1%}')} | {f(g)} | {f(g/cap if cap else None,'{:.0%}')} | {f(o/M/avgc if o is not None and avgc else None,'{:.1%}')} |")
    prev = ntoa; prevc = cap
# sales series incl. years without balance sheet
ks = sorted(k for k in sales if k >= FROM)
print('sales series:', ', '.join(f"{k}:{sales[k]/M:,.0f}" for k in ks))
print('op series:', ', '.join(f"{k}:{op[k]/M:,.0f}" for k in sorted(op) if k >= FROM))
