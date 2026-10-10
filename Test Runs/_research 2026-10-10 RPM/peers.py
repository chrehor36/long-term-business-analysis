"""Competitor series from each filer's own XBRL company facts (10-K, annual, first-filed value). Transcription only."""
import json, sys
from datetime import date
def annual(d, tags):
    out = {}
    for tag in tags:
        if tag not in d: continue
        for unit, vals in d[tag]['units'].items():
            for v in vals:
                if v.get('form') not in ('10-K', '10-K/A') or 'start' not in v: continue
                s = date.fromisoformat(v['start']); e = date.fromisoformat(v['end'])
                if 350 < (e - s).days < 380:
                    out.setdefault(int(v['end'][:4]) if v['end'][5:7] != '01' else int(v['end'][:4]) - 1, (v['val'], v['accn']))
    return out
def inst(d, tags):
    out = {}
    for tag in tags:
        if tag not in d: continue
        for unit, vals in d[tag]['units'].items():
            for v in vals:
                if v.get('form') not in ('10-K',) or 'start' in v: continue
                if v.get('fp') != 'FY': continue
                out.setdefault(int(v['end'][:4]), v['val'])
    return out
REV = ['Revenues', 'RevenueFromContractWithCustomerIncludingAssessedTax', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'SalesRevenueGoodsNet']
OI = ['OperatingIncomeLoss']
PT = ['IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest', 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments']
INT = ['InterestExpense', 'InterestExpenseNonoperating', 'InterestExpenseDebt']
EQ = ['StockholdersEquity']
GW = ['Goodwill']
IA = ['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet']
for tk in sys.argv[1:]:
    f = json.load(open(f'facts_{tk}.json'))
    d = f['facts']['us-gaap']
    rev = annual(d, REV); oi = annual(d, OI); pt = annual(d, PT); it = annual(d, INT)
    eq = inst(d, EQ); gw = inst(d, GW)
    print(f'== {tk} {f["entityName"]}')
    print('  year   revenue   op.inc  op%   pretax+int  (pt+int)%   equity  goodwill  accn(rev)')
    for y in range(2008, 2027):
        if y not in rev: continue
        r = rev[y][0] / 1e6
        o = oi.get(y, (None,))[0]; p = pt.get(y, (None,))[0]; i = it.get(y, (0,))[0]
        o = o / 1e6 if o is not None else None
        pi = (p + i) / 1e6 if p is not None else None
        os_ = '-' if o is None else str(round(o)); op = '-' if o is None else f'{100*o/r:.1f}'
        ps = '-' if pi is None else str(round(pi)); pp = '-' if pi is None else f'{100*pi/r:.1f}'
        print(f'  {y}  {r:9.0f}  {os_:>7} {op:>5}  {ps:>9}  {pp:>5}   {eq.get(y,0)/1e6:7.0f} {gw.get(y,0)/1e6:7.0f}  {rev[y][1]}')
