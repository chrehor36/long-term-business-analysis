"""Pull annual 10-K facts (first-filed vintage) for a company: revenue, operating income, assets, equity, goodwill, intangibles, debt, OCF, capex."""
import sys, json
sys.path.insert(0, '../../tools')
import sources as s
TAGS = {
 'rev': ['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax','SalesRevenueNet','SalesRevenueGoodsNet'],
 'opinc': ['OperatingIncomeLoss'],
 'ni': ['NetIncomeLoss'],
 'assets': ['Assets'],
 'equity': ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
 'gw': ['Goodwill'],
 'intang': ['IntangibleAssetsNetExcludingGoodwill','FiniteLivedIntangibleAssetsNet'],
 'ltdebt': ['LongTermDebtNoncurrent','LongTermDebt'],
 'ocf': ['NetCashProvidedByUsedInOperatingActivities'],
 'capex': ['PaymentsToAcquirePropertyPlantAndEquipment'],
 'acq': ['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 'sbc': ['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
 'da': ['DepreciationDepletionAndAmortization','DepreciationAndAmortization'],
 'tax': ['IncomeTaxExpenseBenefit'],
 'pretax': ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
 'interest': ['InterestExpense','InterestExpenseNonoperating','InterestPaidNet'],
 'buyback': ['PaymentsForRepurchaseOfCommonStock'],
 'div': ['PaymentsOfDividends','PaymentsOfDividendsCommonStock'],
}
def run(t, out):
    cik, name = s.cik_for(t)
    f = s.sec_facts(cik)
    g = f['facts'].get('us-gaap', {})
    res = {}
    for k, tags in TAGS.items():
        for tag in tags:
            if tag not in g: continue
            for unit, arr in g[tag]['units'].items():
                if unit != 'USD': continue
                for e in arr:
                    if e.get('form') not in ('10-K','10-K/A'): continue
                    fy_end = e['end']
                    if 'start' in e:
                        from datetime import date
                        d0 = date.fromisoformat(e['start']); d1 = date.fromisoformat(e['end'])
                        if not (340 <= (d1-d0).days <= 380): continue
                    key = (k, fy_end[:4] if fy_end[5:7] > '06' else str(int(fy_end[:4])-1))
                    # earliest filed wins
                    if key not in res or e['filed'] < res[key][1]:
                        if key in res and res[key][2] != tag: continue
                        res[key] = (e['val'], e['filed'], tag)
    years = sorted({y for (_, y) in res})
    lines = [f'{t} {name} CIK {cik}', 'year ' + ' '.join(f'{k:>8}' for k in TAGS)]
    for y in years:
        row = [f"{res[(k,y)][0]/1e6:8.0f}" if (k,y) in res else '       -' for k in TAGS]
        lines.append(y + ' ' + ' '.join(row))
    txt = '\n'.join(lines)
    open(out, 'w').write(txt + '\n')
    print(txt)
if __name__ == '__main__':
    for t in sys.argv[1:]:
        run(t, f'comp_{t}.txt')
