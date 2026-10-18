import sys
sys.path.insert(0, '.')
from facts import annual
co = {'NOV':['cache/facts_0001021860.json'], 'SLB':['cache/facts_0000087347.json'], 'HAL':['cache/facts_0000045012.json'],
      'BKR':['cache/facts_0000808362.json','cache/facts_0001701605.json']}
T = {'rev':['Revenues','SalesRevenueNet','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueServicesNet'],
     'pti':['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments','IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic'],
     'int':['InterestExpense','InterestExpenseNonoperating','InterestExpenseDebt'],
     'eq':['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
     'gw':['Goodwill'], 'ia':['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],
     'cash':['CashAndCashEquivalentsAtCarryingValue','CashCashEquivalentsAndShortTermInvestments'],
     'sti':['ShortTermInvestments'],
     'ltd':['LongTermDebtNoncurrent','LongTermDebt'], 'std':['DebtCurrent','LongTermDebtCurrent','ShortTermBorrowings','ShortTermDebtAndCurrentPortionOfLongTermDebt'],
     'gwimp':['GoodwillImpairmentLoss'], 'ocf':['NetCashProvidedByUsedInOperatingActivities'], 'capex':['PaymentsToAcquirePropertyPlantAndEquipment'],
     'da':['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet']}
def series(paths, tags):
    res = {}
    for p in paths:
        o = annual(p, tags)
        for t in tags:  # priority order
            for (tt, end), v in o.items():
                if tt != t: continue
                y = int(end[:4])
                if y not in res: res[y] = v[0]/1e6
    return res
data = {}
for c, paths in co.items():
    data[c] = {k: series(paths, tags) for k, tags in T.items()}
yrs = range(2008, 2026)
import json
json.dump({c:{k:{str(y):v for y,v in s.items()} for k,s in d.items()} for c,d in data.items()}, open('field_series.json','w'), indent=0)
for c in co:
    d = data[c]
    print(f'== {c}: year rev pti int ebit ebit% eq gw ia cash debt tangcap  ebit/tangcap  ebit_excl_gwimp/tangcap')
    tot = {'ebit':0,'rev':0,'tc':0,'ebitx':0}
    for y in yrs:
        g = lambda k: d[k].get(y)
        rev, pti, it = g('rev'), g('pti'), g('int') or 0
        if rev is None or pti is None: print(' ', y, 'missing', rev, pti); continue
        ebit = pti + it
        eq, gw, ia, cash = g('eq') or 0, g('gw') or 0, g('ia') or 0, (g('cash') or 0)
        debt = (g('ltd') or 0) + (g('std') or 0)
        tc = eq + debt - cash - gw - ia
        gwi = g('gwimp') or 0
        tot['ebit'] += ebit; tot['rev'] += rev; tot['tc'] += tc; tot['ebitx'] += ebit + gwi
        print(f'  {y} {rev:8.0f} {pti:7.0f} {it:5.0f} {ebit:7.0f} {100*ebit/rev:6.1f}% eq{eq:7.0f} gw{gw:6.0f} ia{ia:6.0f} c{cash:6.0f} d{debt:6.0f} tc{tc:7.0f} {100*ebit/tc if tc>0 else float("nan"):6.1f}% {100*(ebit+gwi)/tc if tc>0 else float("nan"):6.1f}%')
