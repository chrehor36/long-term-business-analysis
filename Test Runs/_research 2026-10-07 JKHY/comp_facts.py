"""Transcribe annual figures from SEC XBRL company facts (cache/facts_*.json). Transcription only; read the filings."""
import json, sys
from datetime import date
TAGS = {
 'rev': ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','RevenueFromContractWithCustomerIncludingAssessedTax'],
 'opinc': ['OperatingIncomeLoss'],
 'ni': ['NetIncomeLoss'],
 'ocf': ['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
 'ppe': ['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
 'sw': ['PaymentsToDevelopSoftware','PaymentsForSoftware'],
 'sbc': ['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'gw': ['Goodwill'],
 'eq': ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
 'debt': ['LongTermDebt','LongTermDebtNoncurrent'],
 'impair': ['GoodwillImpairmentLoss'],
}
def series(f, tags, flow=True):
    g = f['facts'].get('us-gaap', {})
    out = {}
    for t in tags:
        if t not in g: continue
        for u in g[t]['units'].values():
            for x in u:
                if not x['form'].startswith('10-K'): continue
                e = date.fromisoformat(x['end'])
                if flow:
                    if 'start' not in x: continue
                    if (e - date.fromisoformat(x['start'])).days < 340: continue
                key = e.year if e.month > 3 else e.year - 1
                out.setdefault(key, x['val'])
    return out
cik = sys.argv[1]
f = json.load(open(f'cache/facts_{cik}.json'))
print(f['entityName'])
res = {k: series(f, v, flow=(k not in ('gw','eq','debt'))) for k, v in TAGS.items()}
yrs = sorted(set().union(*[set(v) for v in res.values()]))
yrs = [y for y in yrs if y >= 2012]
print('FY   ' + ''.join(f'{k:>9}' for k in TAGS) + '   opm')
for y in yrs:
    row = [res[k].get(y) for k in TAGS]
    opm = (res['opinc'].get(y) or 0) / res['rev'][y] * 100 if res['rev'].get(y) else float('nan')
    print(f'{y} ' + ''.join(f'{(v/1e6 if v is not None else float("nan")):9.0f}' for v in row) + f'  {opm:5.1f}')
