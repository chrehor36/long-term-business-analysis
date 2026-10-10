"""RPM capital arithmetic from its own XBRL facts (10-K, May year-ends, first-filed values). Transcription and sums only."""
import json
from datetime import date
d = json.load(open('cache/facts.json'))['facts']['us-gaap']
def inst(tags):
    out = {}
    for t in tags:
        if t not in d: continue
        for u, vals in d[t]['units'].items():
            for v in vals:
                if v.get('form') == '10-K' and 'start' not in v and v['end'][5:7] == '05':
                    out.setdefault(int(v['end'][:4]), v['val'] / 1e6)
    return out
def ann(tags):
    out = {}
    for t in tags:
        if t not in d: continue
        for u, vals in d[t]['units'].items():
            for v in vals:
                if v.get('form') == '10-K' and 'start' in v and v['end'][5:7] == '05':
                    s = date.fromisoformat(v['start']); e = date.fromisoformat(v['end'])
                    if 350 < (e - s).days < 380: out.setdefault(int(v['end'][:4]), v['val'] / 1e6)
    return out
eq = inst(['StockholdersEquity']); gw = inst(['Goodwill']); ia = inst(['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet'])
cash = inst(['CashAndCashEquivalentsAtCarryingValue'])
ltd = inst(['LongTermDebtNoncurrent', 'LongTermDebtAndCapitalLeaseObligations']); std = inst(['LongTermDebtCurrent', 'DebtCurrent']); stb = inst(['ShortTermBorrowings', 'NotesPayable'])
nci = inst(['MinorityInterest'])
ar = inst(['AccountsReceivableNetCurrent']); inv = inst(['InventoryNet']); ap = inst(['AccountsPayableCurrent'])
pt = ann(['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'])
ie = ann(['InterestExpense']); rev = ann(['RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'Revenues'])
dep = ann(['Depreciation']); capex = ann(['PaymentsToAcquireProductiveAssets'])
print('FY   rev    pt+int  totcap tangcap ret_tot ret_tang  AR   inv   AP   (AR+inv-AP)/rev  capex  dep  capex/dep')
for y in range(2010, 2027):
    if y not in pt: continue
    debt = ltd.get(y, 0) + std.get(y, 0) + stb.get(y, 0)
    tc = eq.get(y, 0) + nci.get(y, 0) + debt - cash.get(y, 0); tg = tc - gw.get(y, 0) - ia.get(y, 0)
    e = pt[y] + ie.get(y, 0); r = rev.get(y, 0)
    wc = ar.get(y, 0) + inv.get(y, 0) - ap.get(y, 0)
    print(y, f'{r:6.0f} {e:6.0f} {tc:6.0f} {tg:6.0f} {100*e/tc:6.1f} {100*e/tg:7.1f}  {ar.get(y,0):5.0f} {inv.get(y,0):5.0f} {ap.get(y,0):5.0f}  {100*wc/r if r else 0:6.1f}  {capex.get(y,0):6.1f} {dep.get(y,0):6.1f} {capex.get(y,0)/dep[y] if dep.get(y) else 0:5.2f}')
