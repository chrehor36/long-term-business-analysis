import json, sys
from datetime import date
sys.stdout.reconfigure(encoding='utf-8')
# One construction for every filer, from its own SEC companyfacts, newest filed vintage:
# operating margin = OperatingIncomeLoss / revenue; operating capital = equity (incl. NCI where tagged)
# + debt - cash; tangible operating capital = operating capital - goodwill - intangibles (net).
def load(p):
    f = json.load(open(p))['facts']
    return f.get('us-gaap') or f.get('ifrs-full')
def series(g, tag, dur):
    out = {}
    if tag not in g: return out
    for u, v in g[tag]['units'].items():
        if u not in ('USD', 'EUR'): continue
        for x in v:
            if x.get('form') not in ('10-K', '10-K/A', '20-F', '20-F/A', '8-K'): continue
            if dur:
                if 'start' not in x: continue
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if not 340 <= d <= 380: continue
            elif 'start' in x: continue
            e = x['end']
            if e not in out or x['filed'] > out[e][1]: out[e] = (x['val'], x['filed'], u)
    return {k: v[0] for k, v in out.items()}
def first(g, tags, dur=True):
    res = {}
    for t in tags:
        for k, v in series(g, t, dur).items(): res.setdefault(k, v)
    return res
def summ(g, tags, dur=False):
    res = {}
    for t in tags:
        for k, v in series(g, t, dur).items(): res[k] = res.get(k, 0) + v
    return res
REV = ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet', 'SalesRevenueGoodsNet', 'Revenue', 'RevenueFromContractsWithCustomers']
OI = ['OperatingIncomeLoss', 'ProfitLossFromOperatingActivities']
EQ = ['StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest', 'StockholdersEquity', 'Equity']
CASH = ['CashAndCashEquivalentsAtCarryingValue', 'CashAndCashEquivalents']
DEBT_LT = ['Borrowings', 'LongTermDebtNoncurrent', 'LongTermDebtAndCapitalLeaseObligations', 'LongTermDebtAndFinanceLeaseObligationsNoncurrent', 'NoncurrentPortionOfNoncurrentBorrowings', 'LongtermBorrowings', 'NoncurrentBorrowings']
DEBT_C = ['LongTermDebtCurrent', 'LongTermDebtAndCapitalLeaseObligationsCurrent', 'ShortTermBorrowings', 'DebtCurrent', 'CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings', 'CurrentPortionOfNoncurrentBorrowings', 'ShorttermBorrowings']
GW = ['Goodwill']
INT = ['IntangibleAssetsNetExcludingGoodwill', 'FiniteLivedIntangibleAssetsNet', 'IntangibleAssetsOtherThanGoodwill']
for t in sys.argv[1:]:
    p = 'cache/facts.json' if t == 'TCMD' else f'cache/peers/{t}_facts.json'
    g = load(p)
    rev = first(g, REV); oi = first(g, OI); eq = first(g, EQ, False); cash = first(g, CASH, False)
    dl = first(g, DEBT_LT, False); dc = first(g, DEBT_C, False); gw = first(g, GW, False); it = first(g, INT, False)
    print('=====', t)
    for e in sorted(oi):
        if e < '2012': continue
        r = rev.get(e); o = oi[e]
        cap = tang = None
        if e in eq:
            cap = eq[e] + dl.get(e, 0) + dc.get(e, 0) - cash.get(e, 0)
            tang = cap - gw.get(e, 0) - it.get(e, 0)
        print(e, 'rev %.1f' % (r / 1e6) if r else 'rev -', 'OI %.1f' % (o / 1e6), 'OM %.1f%%' % (100 * o / r) if r else 'OM -',
              'eq %.0f debt %.0f cash %.0f gw+int %.0f' % (eq.get(e, 0) / 1e6, (dl.get(e, 0) + dc.get(e, 0)) / 1e6, cash.get(e, 0) / 1e6, (gw.get(e, 0) + it.get(e, 0)) / 1e6),
              'OI/opcap %.1f%%' % (100 * o / cap) if cap else '-', 'OI/tangible %.1f%%' % (100 * o / tang) if tang and tang > 0 else '-')
