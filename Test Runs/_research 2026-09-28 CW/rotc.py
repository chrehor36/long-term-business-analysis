import json
from datetime import date
f = json.load(open('cache/facts_cw.json'))['facts']['us-gaap']
def inst(tags):
    out = {}
    for t in tags:
        if t not in f: continue
        for u, arr in f[t]['units'].items():
            for x in arr:
                if x.get('form') == '10-K' and 'start' not in x and x['end'][5:] == '12-31':
                    out[x['end'][:4]] = x['val'] / 1e6   # later filings overwrite: newest vintage
    return out
def dur(tags):
    out = {}
    for t in tags:
        if t not in f: continue
        for u, arr in f[t]['units'].items():
            for x in arr:
                if x.get('form') == '10-K' and 'start' in x and 350 <= (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days <= 380:
                    out[x['end'][:4]] = x['val'] / 1e6
    return out
eq = inst(['StockholdersEquity']); gw = inst(['Goodwill']); ia = inst(['IntangibleAssetsNetExcludingGoodwill'])
debt = inst(['DebtInstrumentCarryingAmount']); ltd = inst(['LongTermDebt'])
cash = inst(['CashAndCashEquivalentsAtCarryingValue']); cash.update({k: v for k, v in inst(['CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents']).items() if k >= '2022'})
dr = inst(['ContractWithCustomerLiabilityCurrent', 'DeferredRevenueCurrent'])
pp = inst(['DefinedBenefitPlanAssetsForPlanBenefitsNoncurrent', 'AssetsForPlanBenefitsDefinedBenefitPlan'])
oi = dur(['OperatingIncomeLoss']); rev = dur(['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax'])
print('yr  equity  debt   cash  gw+ia   NTC   OI  OI/NTC  OI/all(net cash)  defrev  pensasset  OI/(NTC+defrev)  OM')
for y in [str(v) for v in range(2012, 2026)]:
    d = debt.get(y, ltd.get(y))
    if d is None: print(y, 'no debt'); continue
    try:
        ntc = eq[y] + d - cash[y] - gw[y] - ia[y]
        allc = eq[y] + d - cash[y]
        s = f"{y} {eq[y]:7.1f} {d:6.1f} {cash[y]:6.1f} {gw[y]+ia[y]:7.1f} {ntc:6.1f} {oi[y]:6.1f} {100*oi[y]/ntc:6.1f}% {100*oi[y]/allc:6.1f}%"
        s += f"  {dr.get(y, float('nan')):6.1f} {pp.get(y, float('nan')):6.1f}"
        if y in dr: s += f"  {100*oi[y]/(ntc+dr[y]):6.1f}%"
        if y in rev: s += f"  {100*oi[y]/rev[y]:5.1f}%"
        print(s)
    except KeyError as e:
        print(y, 'missing', e)
