"""Q7 COMPUTATION for PCG (not a clearance). Inputs are filed figures, $ millions; sources in the run file."""
Y   = [2021, 2022, 2023, 2024, 2025]
OCF = [2262, 3721, 4747, 8035, 8716]      # Net cash provided by operating activities
CAP = [7689, 9584, 9714, 10369, 11787]    # Capital expenditures
DA  = [3403, 3856, 3738, 4189, 4634]      # Depreciation, amortization, and decommissioning
SBC = [56, 115, 91, 98, 134]              # Share-based compensation expense (XBRL AllocatedShareBasedCompensationExpense)
SUBPREF = [14, 13, 14, 14, 14]            # Utility preferred dividends (noncontrolling interest); 2022 13 per XBRL
RBP = [0, 51, 168, 175, 223]              # Recovery bond principal repaid (SB 901 + AB 1054): the dedicated charge left out
INT = [1404, 1607, 2286, 2421, 2665]      # Cash interest paid, net of capitalized
REV = [20642, 21680, 24428, 24419, 24935]
r, floor = 0.0533, 0.10
shares = 2_202_429_703 + 32_200_000*2.4331   # cover less Utility-held shares, plus MCP at max conversion rate
shares_m = shares/1e6
price = 12.63
avg = lambda xs: sum(xs)/len(xs)
oc = [o-d-s-p-b for o,d,s,p,b in zip(OCF,DA,SBC,SUBPREF,RBP)]
print("owner cash, equity-only, maintenance only, by year:", dict(zip(Y,oc)))
base = avg(oc); print(f"five-year average {base:,.0f}")
half1, half2 = avg(oc[:2]), avg(oc[3:]); print(f"halves: first {half1:,.0f} second {half2:,.0f}  (sign change -> growth meaningless by (b))")
share_of_sales = [o/s for o,s in zip(oc,REV)]; print("owner cash / sales:", [f"{x*100:.1f}%" for x in share_of_sales])
g_sales = (REV[-1]/REV[0])**(1/4)-1; print(f"sales growth 2021-2025 CAGR {g_sales*100:.2f}%")
# no-growth case (the range, alone, by specific (b))
v0 = base/r; v0_10 = base/floor
print(f"NO-GROWTH value at {r*100:.2f}%: {v0:,.0f}  = ${v0/shares_m:.2f}/sh ; at 10%: {v0_10:,.0f} = ${v0_10/shares_m:.2f}/sh (fair price, equity-only)")
print(f"earnings yield on price: owner cash {base:,.0f} / market value {price*shares_m:,.0f} = {base/(price*shares_m)*100:.2f}%")
# growth spending and the utility debt credit
gs = avg(CAP)-avg(DA); ltd_2020 = 37288+28; ltd_2025 = 57387+821+2-10145
credit = (ltd_2025-ltd_2020)/5; cap = 0.475*gs
print(f"growth spending (capex - D&A) avg {gs:,.0f}; LTD ex recovery bonds 2020 {ltd_2020:,} -> 2025 {ltd_2025:,}: credit {credit:,.0f}/yr; cap 47.5% x gs = {cap:,.0f}; credited {min(credit,cap):,.0f}")
credit = min(credit, cap)
# BESIDE (not a range end): growth case at the sales-growth cut, growth spending grown and stopped at year ten
def growth_case(g, rate):
    pv = 0
    for t in range(1, 11):
        cf = base*(1+g)**t - (gs - credit)*(1+g)**(t-1)
        pv += cf/(1+rate)**t
    term = base*(1+g)**10/rate/(1+rate)**10
    return pv+term
for rate in (r, floor):
    v = growth_case(g_sales, rate); print(f"BESIDE growth case g={g_sales*100:.2f}% at {rate*100:.2f}%: {v:,.0f} = ${v/shares_m:.2f}/sh")
print(f"growth spending net of credit, year 1 {gs-credit:,.0f}, year 10 {(gs-credit)*(1+g_sales)**9:,.0f}; gross year1 {gs:,.0f} year10 {gs*(1+g_sales)**9:,.0f}")
# all-spending case beside
allsp = avg(OCF)-avg(CAP)-avg(SBC)-avg(SUBPREF)-avg(RBP)+credit
print(f"BESIDE all-spending owner cash (debt credit added) {allsp:,.0f}/yr")
# all-equity basis beside
oc_ae = base + avg(INT) + avg(RBP)
netdebt = 2205+1474+61347+0-902 + 252
for rate in (r, floor):
    v = oc_ae/rate - netdebt
    print(f"ALL-EQUITY no-growth at {rate*100:.2f}%: owner cash before interest {oc_ae:,.0f}; EV {oc_ae/rate:,.0f} - net debt {netdebt:,} = {v:,.0f} = ${v/shares_m:.2f}/sh")
print(f"shares {shares:,.0f}; market value at ${price}: {price*shares_m:,.0f}M")
# TTM to Sep 30 2026, beside
ttm_ocf = 8716-6756+5840; ttm_da = 4634-3302+3434; ttm_rb = 223-139+134
print(f"TTM Q3-2026 (beside): OCF {ttm_ocf:,} D&A {ttm_da:,} -> maintenance owner cash approx {ttm_ocf-ttm_da-130-14-ttm_rb:,}")
