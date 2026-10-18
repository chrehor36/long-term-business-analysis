# Competitor rows from SEC companyfacts (XBRL transcription; the 10-K is the filed source). Same number sooner.
import sys, json; sys.path.insert(0, 'tools'); import sources
from datetime import date
def inst(facts, tags):
    out = {}
    for t in tags:
        node = facts['facts'].get('us-gaap', {}).get(t)
        if not node: continue
        for u, pts in node['units'].items():
            for x in pts:
                if x.get('form') == '10-K' and 'start' not in x:
                    out.setdefault(x['end'], x['val'] / 1e6)
    return out
for tk in ['ROK', 'ETN', 'GEHC']:
    cik, name = sources.cik_for(tk)
    f = sources.sec_facts(cik)
    rev, _, _ = sources.annual(f, ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet'], vintage='newest')
    oi, _, _ = sources.annual(f, ['OperatingIncomeLoss'], vintage='newest')
    pti, _, _ = sources.annual(f, ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'], vintage='newest')
    cfo, _, _ = sources.annual(f, ['NetCashProvidedByUsedInOperatingActivities', 'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'], vintage='newest')
    capex, _, _ = sources.annual(f, ['PaymentsToAcquirePropertyPlantAndEquipment'], vintage='newest')
    eq = inst(f, ['StockholdersEquity']); gw = inst(f, ['Goodwill']); ia = inst(f, ['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet'])
    print(f'== {tk} {name} CIK {cik}')
    for e in sorted(rev):
        if e < '2015-06-01': continue
        r = rev[e]
        if not r: continue
        o = oi.get(e); p = pti.get(e); c = cfo.get(e); k = capex.get(e)
        tang = None
        if e in eq and e in gw: tang = eq[e] - gw[e] - ia.get(e, 0)
        print(e, f'rev {r:,.0f}', f'opinc {o:,.0f} ({o/r*100:.1f}%)' if o and r else 'opinc n/a', f'pretax {p:,.0f} ({p/r*100:.1f}%)' if p and r else '',
              f'FCF {c-k:,.0f} ({(c-k)/r*100:.1f}%)' if c and k and r else '', f'tangible equity {tang:,.0f}' if tang is not None else '')
