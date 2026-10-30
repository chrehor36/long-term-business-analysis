# Owner cash and Q7 range for CWT, from the filed cash-flow statements ($ thousands -> $M).
# Sources: 10-K 2025 (0001628280-26-012444) for 2023-2025; 10-K 2023 (0001035201-24-000004) for 2021-2022.
import sys
sys.stdout.reconfigure(encoding='utf-8')
Y = [2021, 2022, 2023, 2024, 2025]
OCF   = [231.718, 243.772, 217.817, 290.867, 302.561]
SBC   = [6.805, 5.161, 2.993, 3.746, 4.981]
DA    = [111.581, 117.364, 123.124, 134.139, 146.523]
DEFTX = [25.200, 26.880, 35.627, 40.445, 38.205]      # changes in normalized deferred income taxes
CAPEX = [293.194, 327.757, 383.747, 470.800, 516.991]  # utility plant expenditures (company + developer funded)
ACQ   = [6.451 - 1.000, 7.766, 0.175 + 2.816, 1.609, 0.0]  # business + asset acquisitions, less 2021 return of investment
DEVIN = [28.171, 25.822, 21.156, 30.389, 37.509]       # advances and contributions in aid of construction
DEVOUT= [10.634, 9.468, 9.355, 9.399, 9.462]           # refunds of advances
LIFE  = [2.335, 6.688 - 6.688, 2.681, 3.935 - 1.426, 3.364 - 0.215]  # life insurance bought less proceeds
INT   = [41.621, 43.768, 49.145, 55.656, 61.136]       # interest paid, net of capitalized
REV   = [790.9, 846.4, 794.6, 1036.8, 1000.1]
NI    = [100.979, 95.263, 51.376, 190.085, 127.848]    # net income incl. NCI, as filed

def avg(x): return sum(x)/len(x)
moc_cash = [OCF[i]-SBC[i]-DA[i]-LIFE[i] for i in range(5)]           # maintenance-only, cash tax
moc_book = [moc_cash[i]-DEFTX[i] for i in range(5)]                  # maintenance-only, deferred tax charged
gs = [CAPEX[i]+ACQ[i]-(DEVIN[i]-DEVOUT[i])-DA[i] for i in range(5)]  # growth spending above maintenance guess
alls_cash = [moc_cash[i]-gs[i] for i in range(5)]
alls_book = [moc_book[i]-gs[i] for i in range(5)]
print('year | OCF | SBC | D&A | defTx | capex | acq | dev net | MOC cash-tax | MOC book-tax | growth spend | all-spend cash-tax | all-spend book-tax | MOC book / sales')
for i,y in enumerate(Y):
    print(f'{y} | {OCF[i]:.1f} | {SBC[i]:.1f} | {DA[i]:.1f} | {DEFTX[i]:.1f} | {CAPEX[i]:.1f} | {ACQ[i]:.1f} | {DEVIN[i]-DEVOUT[i]:.1f} | {moc_cash[i]:.1f} | {moc_book[i]:.1f} | {gs[i]:.1f} | {alls_cash[i]:.1f} | {alls_book[i]:.1f} | {moc_book[i]/REV[i]*100:.1f}%')
print(f'avg | | | | | | | | {avg(moc_cash):.1f} | {avg(moc_book):.1f} | {avg(gs):.1f} | {avg(alls_cash):.1f} | {avg(alls_book):.1f}')

r = 0.0530   # US Treasury 30y par, 2026-10-27
SH = 61.839101
PRICE = 47.82
MCAP = PRICE*SH
# debt credit (utility rule): increase in long-term debt incl. current maturities and finance leases, 2020-12-31 to 2025-12-31
ltd2020 = 781.1 + 5.1 + 5.204
ltd2025 = 1472.0 + 2.3 + 1.913
dc_raw = (ltd2025 - ltd2020)/5
cap_share = 0.466   # Cal Water authorized debt share (10-K 2025 Item 1)

def growth(a, b, n=4): return (b/a)**(1/n)-1
g_shown_book = growth(moc_book[0], moc_book[-1])
g_shown_cash = growth(moc_cash[0], moc_cash[-1])
g_sales = growth(REV[0], REV[-1])

def value(base, g, gs0, dc0, rate, years=10):
    """year t cash = base*(1+g)^t - (gs0-dc0)*(1+g)^t for t<=10; then base*(1+g)^10 flat forever."""
    v = 0.0
    for t in range(1, years+1):
        v += (base*(1+g)**t - (gs0-dc0)*(1+g)**t)/(1+rate)**t
    v += (base*(1+g)**years / rate)/(1+rate)**years
    return v

def cap_check(base, g):
    # share of sales in year 10 if owner cash grows at g and sales at sales growth
    oc10 = base*(1+g)**10
    s10 = REV[-1]*(1+g_sales)**10
    return oc10/s10

def run(label, mocs, g_shown):
    base = avg(mocs); gs0 = avg(gs)
    dc0 = min(dc_raw, cap_share*gs0)
    hi_share = max(mocs[i]/REV[i] for i in range(5))
    share10 = cap_check(base, g_shown)
    g = g_shown
    cut = ''
    if share10 > hi_share:
        g = min(g_sales, r); cut = f'cut to sales growth {g_sales*100:.2f}% (shown {g_shown*100:.2f}% would need {share10*100:.1f}% of sales in yr10 vs highest {hi_share*100:.1f}%)'
    ng = base/r
    gr = value(base, g, gs0, dc0, r)
    ng10 = base/0.10
    gr10 = value(base, g, gs0, dc0, 0.10)
    print(f'\n== {label}: base {base:.1f}, shown growth {g_shown*100:.2f}%, carried {g*100:.2f}% {cut}')
    print(f'   growth spending yr1 {gs0*(1+g):.1f}, yr10 {gs0*(1+g)**10:.1f}; debt credit raw {dc_raw:.1f}/yr, cap {cap_share*gs0:.1f} -> credit {dc0:.1f} (yr1 {dc0*(1+g):.1f}, yr10 {dc0*(1+g)**10:.1f})')
    print(f'   at {r*100:.2f}%: no-growth {ng:.0f}M = ${ng/SH:.2f}/sh ; growth {gr:.0f}M = ${gr/SH:.2f}/sh ; width {max(ng,gr)/max(min(ng,gr),1e-9):.2f}x')
    print(f'   at 10%: no-growth ${ng10/SH:.2f} ; growth ${gr10/SH:.2f} ; FAIR (avg) ${(ng10+gr10)/2/SH:.2f}')
    # floor test: expected return at price for each case (IRR on market cap)
    def irr_ng(): return base/MCAP
    def irr_g():
        lo,hi=-0.5,1.0
        for _ in range(200):
            mid=(lo+hi)/2
            if value(base,g,gs0,dc0,mid)>MCAP: lo=mid
            else: hi=mid
        return mid
    print(f'   expected return at ${PRICE}: no-growth {irr_ng()*100:.2f}% ; growth {irr_g()*100:.2f}%')
    return ng, gr

ng_b, gr_b = run('CENTRAL equity-only, maintenance-only, deferred tax charged, growth spending net of capped debt credit', moc_book, g_shown_book)
ng_c, gr_c = run('BESIDE equity-only, cash tax (deferred tax not charged)', moc_cash, g_shown_cash)

# all-spending case beside (literal): owner cash after all spending, no debt credit
print(f'\n== BESIDE all spending deducted (book tax): avg {avg(alls_book):.1f}M/yr; cash tax: {avg(alls_cash):.1f}M/yr -> negative; no positive value at any rate')

# all-equity basis beside: add back after-tax interest, value, less net debt at 2026-06-30
tax = 0.21 + 0.0884*(1-0.21)
at_int = avg(INT)*(1-tax)
netdebt = 1471.948 + 0.590 + 205.0 - 43.445
for lbl, mocs in [('book tax', moc_book), ('cash tax', moc_cash)]:
    base = avg(mocs)+at_int
    g = g_sales
    ng = base/r - netdebt
    gr = value(base, g, avg(gs), 0.0, r) - netdebt
    ng10 = base/0.10 - netdebt; gr10 = value(base, g, avg(gs), 0.0, 0.10) - netdebt
    print(f'\n== BESIDE all-equity ({lbl}): unlevered base {base:.1f} (after-tax interest {at_int:.1f} at {tax*100:.2f}%), net debt {netdebt:.1f}')
    print(f'   at 5.30%: no-growth ${ng/SH:.2f}/sh ; growth (no debt credit, sales growth {g*100:.2f}%) ${gr/SH:.2f}/sh ; at 10% fair ${(ng10+gr10)/2/SH:.2f}')

# the signed, unclosed deals beside: financing added, nothing credited (no filed target record)
deals = 218.0 + (45.0-10.8)
print(f'\n== BESIDE signed unclosed deals (Nexus $218.0M, BVRT remaining ${45.0-10.8:.1f}M unpaid): per share effect if nothing credited: -${deals/SH:.2f}')

# literal window check and returns
print('\nNI/avg-equity and EPS checks in peers.txt; earned return on capital:')
EQ = [1171.9,1322.4,1430.3,1638.3,1692.0]; EQ0=910.3
LTD = [1061.0,1055.8,1053.5,1177.0,1474.3]; LTD0=786.2
for i,y in enumerate(Y):
    ebit_at = NI[i] + INT[i]*(1-tax)
    capital = (EQ[i]+LTD[i] + (EQ[i-1] if i else EQ0) + (LTD[i-1] if i else LTD0))/2
    print(f'{y}: NI+after-tax interest {ebit_at:.1f} on avg equity+LT debt {capital:.0f} = {ebit_at/capital*100:.1f}%')
