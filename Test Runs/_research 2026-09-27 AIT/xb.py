import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
j = json.load(open('companyfacts.json'))['facts']['us-gaap']
def ann(tag):
    out = {}
    if tag not in j: return out
    for u, arr in j[tag]['units'].items():
        for x in arr:
            if x.get('form') in ('10-K', '10-K/A') and x.get('fp') == 'FY' and 'frame' in x or (x.get('form') == '10-K' and x.get('start') and x.get('end')):
                if x.get('start'):
                    from datetime import date
                    s = date.fromisoformat(x['start']); e = date.fromisoformat(x['end'])
                    if not 350 <= (e - s).days <= 380: continue
                fy = int(x['end'][:4])
                out[fy] = x['val']  # last filed wins
    return out
tags = ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'SalesRevenueGoodsNet', 'CostOfGoodsAndServicesSold', 'CostOfRevenue', 'CostOfGoodsSold', 'GrossProfit', 'OperatingIncomeLoss', 'SellingGeneralAndAdministrativeExpense', 'ShareBasedCompensation', 'AllocatedShareBasedCompensationExpense', 'IncomeTaxesPaidNet', 'IncomeTaxesPaid', 'NetCashProvidedByUsedInOperatingActivities', 'PaymentsToAcquirePropertyPlantAndEquipment', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', 'InterestExpense', 'InterestExpenseNonoperating', 'Goodwill', 'StockholdersEquity', 'Assets', 'InventoryNet', 'AccountsReceivableNetCurrent', 'AccountsPayableCurrent', 'LongTermDebt', 'LongTermDebtNoncurrent', 'CashAndCashEquivalentsAtCarryingValue', 'IntangibleAssetsNetExcludingGoodwill', 'GoodwillImpairmentLoss', 'LIFOInventoryAmount', 'InventoryLIFOReserve']
res = {}
for t in tags:
    a = ann(t)
    if a: res[t] = a; print(t, {k: round(v / 1e6, 1) for k, v in sorted(a.items())})
json.dump(res, open('xb.json', 'w'))
