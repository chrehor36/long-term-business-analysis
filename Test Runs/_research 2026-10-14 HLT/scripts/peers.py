import json
from datetime import date
def series(path, tag):
    g = json.load(open(path))['facts']['us-gaap']
    if tag not in g: return {}
    u = g[tag]['units']; unit = list(u)[0]; out = {}
    for f in u[unit]:
        if f.get('form') != '10-K' or f.get('fp') != 'FY': continue
        if 'start' in f and (date.fromisoformat(f['end'])-date.fromisoformat(f['start'])).days < 350: continue
        y = int(f['end'][:4])
        if y not in out or f['filed'] > out[y][1]: out[y] = (f['val']/1e6, f['filed'])
    return {y: v[0] for y, v in out.items()}
Y = range(2017, 2026)
# Hilton intangibles from its balance sheets (brands + contracts + other): FY2018/2019/2021/2022/2024/2025 10-Ks
HLT_INT = {2017:4890+953+433, 2018:4869+872+415, 2019:4877+780+421, 2020:4904+653+266, 2021:4883+758+194, 2022:4840+887+161, 2023:4846+1064+173, 2024:4990+1235+194, 2025:5023+1471+206}
rows = {}
for t, path in (("HLT","cache/facts.json"),("MAR","cache/facts_MAR.json"),("CHH","cache/facts_CHH.json"),("H","cache/facts_H.json")):
    A = series(path,'Assets'); G = series(path,'Goodwill'); I = series(path,'IntangibleAssetsNetExcludingGoodwill')
    if t == "HLT": I = HLT_INT
    OI = series(path,'OperatingIncomeLoss')
    if t == "H":
        PT = series(path,'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest')
        IE = {**series(path,'InterestExpense'), **series(path,'InterestExpenseNonoperating')}
        OI = {y: PT[y]+IE.get(y,0) for y in PT}
    R = series(path,'Revenues'); R2 = series(path,'RevenueFromContractWithCustomerExcludingAssessedTax')
    rows[t] = (A,G,I,OI)
    line = []
    vals = []
    for y in Y:
        try:
            nta = A[y]-G[y]-I[y]; r = OI[y]/nta; vals.append(r); line.append(f"{y}:{r:5.0%}")
        except KeyError: line.append(f"{y}:  n/a")
    print(t.ljust(4), ' '.join(line), f"| mean {sum(vals)/len(vals):.0%} over {len(vals)} yrs")
