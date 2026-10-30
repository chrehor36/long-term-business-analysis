import json, sys, os, time
from datetime import date
sys.path.insert(0, '../../tools')
sys.stdout.reconfigure(encoding='utf-8')
import sources as S
from fetch import get
# Competitor row: owner-operated US sit-down chains that file with the SEC, plus CMG (the fast-casual precedent).
# Metric, each filer's own last N fiscal years (latest 10-K): operating income / revenue, summed; and operating income over
# tangible operating capital = total assets - cash - short-term investments - goodwill - intangibles - operating ROU assets
# - (current liabilities - current debt - current operating lease liabilities). Same formula for every filer (the DRI run's NTOA).
PEERS = ['TXRH', 'DRI', 'EAT', 'BLMN', 'CAKE', 'BJRI', 'CBRL', 'DENN', 'RRGB', 'CMG', 'FWRG', 'KRUS']
os.makedirs('cache/peers', exist_ok=True)
def series(g, tags, inst=False):
    out = {}
    for t in tags:
        if t not in g: continue
        for k, u in g[t]['units'].items():
            if k != 'USD': continue
            for f in u:
                if f.get('form') not in ('10-K', '10-K/A'): continue
                e = f['end']
                if not inst:
                    s = f.get('start')
                    if not s: continue
                    dd = (date.fromisoformat(e) - date.fromisoformat(s)).days
                    if dd < 340 or dd > 380: continue
                if e not in out or f['filed'] > out[e][1]:
                    out[e] = (f['val'], f['filed'])
        # first tag that has data for a date wins; later tags only fill gaps
    return {k: v[0] for k, v in out.items()}
def pick(g, tags, inst=False):
    res = {}
    for t in tags:
        s = series(g, [t], inst)
        for k, v in s.items():
            res.setdefault(k, v)
    return res
def near(d, e):
    # instant value at a fiscal-year end e (allow +-10 days)
    for k, v in d.items():
        if abs((date.fromisoformat(k) - date.fromisoformat(e)).days) <= 10: return v
    return None
rows = {}
for t in PEERS:
    try:
        cik, name = S.cik_for(t)
    except Exception as ex:
        print(t, 'no cik', ex); continue
    if not cik: print(t, 'no cik'); continue
    p = f'cache/peers/{t}_facts.json'
    if not os.path.exists(p):
        open(p, 'wb').write(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json')); time.sleep(0.3)
    g = json.load(open(p))['facts'].get('us-gaap', {})
    rev = pick(g, ['Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax', 'SalesRevenueNet'])
    oi = pick(g, ['OperatingIncomeLoss'])
    A = pick(g, ['Assets'], 1); C = pick(g, ['CashAndCashEquivalentsAtCarryingValue'], 1)
    STI = pick(g, ['ShortTermInvestments', 'MarketableSecuritiesCurrent'], 1)
    GW = pick(g, ['Goodwill'], 1); IN = pick(g, ['IntangibleAssetsNetExcludingGoodwill', 'IndefiniteLivedTrademarks', 'FiniteLivedIntangibleAssetsNet'], 1)
    ROU = pick(g, ['OperatingLeaseRightOfUseAsset'], 1); CL = pick(g, ['LiabilitiesCurrent'], 1)
    CD = pick(g, ['LongTermDebtCurrent', 'DebtCurrent'], 1); LLC = pick(g, ['OperatingLeaseLiabilityCurrent'], 1)
    ends = sorted(e for e in oi if e in rev)
    print(f'\n{t} {name}: fiscal years with revenue and operating income: {len(ends)}')
    line = []
    for e in ends:
        a, c = near(A, e), near(C, e)
        ntoa = None
        if a is not None and c is not None and near(CL, e) is not None:
            ntoa = a - c - (near(STI, e) or 0) - (near(GW, e) or 0) - (near(IN, e) or 0) - (near(ROU, e) or 0) - (near(CL, e) - (near(CD, e) or 0) - (near(LLC, e) or 0))
        line.append((e, rev[e], oi[e], ntoa))
        print(f"  {e} rev {rev[e]/1e6:9.1f} OI {oi[e]/1e6:8.1f} margin {oi[e]/rev[e]:6.1%}" + (f" NTOA {ntoa/1e6:8.1f} OI/NTOA {oi[e]/ntoa:6.1%}" if ntoa and ntoa > 0 else ''))
    rows[t] = line
def summ(line, n):
    L = line[-n:]
    if len(L) < n: return None
    m = sum(x[2] for x in L) / sum(x[1] for x in L)
    nt = [x for x in L if x[3] and x[3] > 0 and date.fromisoformat(x[0]) >= date(2019, 6, 1)]
    r = sum(x[2] for x in nt) / sum(x[3] for x in nt) if nt else None
    return m, r, L[0][0], L[-1][0]
print('\nSUMMARY (each filer\'s own last 5 and 10 fiscal years; OI/NTOA over the years inside the window from mid-2019, when ROU assets are on the balance sheet)')
for t, line in rows.items():
    s5, s10 = summ(line, 5), summ(line, 10)
    print(t, '5y', s5 and f"{s5[2]}..{s5[3]} margin {s5[0]:.1%} OI/NTOA {s5[1]:.1%}" if s5 and s5[1] else s5, '| 10y', s10 and f"margin {s10[0]:.1%}")
