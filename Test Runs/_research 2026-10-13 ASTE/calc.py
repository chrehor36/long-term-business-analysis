"""ASTE arithmetic for the 2026-10-13 run. Inputs are the filed figures (USD millions) read from the 10-Ks
listed in the run file; XBRL first-filed values, cross-checked to the FY2025 filed statements for 2023-2025."""
yrs = list(range(2016, 2026))
ocf   = dict(zip(yrs,[134.8,41.9,-29.8,112.4,141.5,7.4,-73.9,27.8,23.0,61.4]))
sbc   = dict(zip(yrs,[2.9,3.1,2.2,2.6,5.1,6.0,6.8,4.1,5.0,7.1]))
capex = dict(zip(yrs,[27.4,20.0,27.4,23.4,15.4,20.1,40.7,34.1,20.5,40.7]))
ppesale=dict(zip(yrs,[0.6,0.5,0.4,0.5,17.7,1.9,5.7,20.3,2.3,0.8]))
da    = dict(zip(yrs,[24.8,25.8,27.9,26.2,26.9,30.2,27.9,25.6,26.8,36.3]))
acq   = dict(zip(yrs,[39.8,26.4,0.0,0.0,32.5,-0.1,17.8,0.0,0.0,248.7]))
intpd = dict(zip(yrs,[1.4,0.6,0.9,1.8,0.3,0.3,1.1,7.0,8.5,16.1]))
sales = dict(zip(yrs,[1147.4,1184.7,1171.6,1169.6,1024.4,1097.2,1274.5,1338.2,1305.1,1410.4]))
opinc = dict(zip(yrs,[87.2,55.5,-86.4,25.1,43.0,22.1,7.5,48.6,23.2,65.9]))
ni    = dict(zip(yrs,[55.2,37.8,-60.4,22.3,46.9,17.8,-0.1,33.5,4.3,38.8]))
eq    = dict(zip(yrs,[648,686,585,602,642,654,627,653,638,682]))
TAX = 0.269   # the filer's own 2025 effective rate (FY2025 10-K, MD&A, Income Tax Provision)
r, floor = 0.056, 0.10
shares = 23.025367
price = 39.48
debt, cash, inv = 16.2+11.8+365.4, 76.8, 1.8   # 10-Q 2026-06-30 balance sheet
netdebt = debt - cash - inv
out = []
p = out.append
p("year  OCF   SBC  capex  owner(eq)  +aftertax int = owner(all-eq)  D&A  owner D&A basis  acq  sales  opmargin  ROE")
oe, oa, od = {}, {}, {}
for y in yrs:
    oe[y] = ocf[y]-sbc[y]-capex[y]
    oa[y] = oe[y] + intpd[y]*(1-TAX)
    od[y] = ocf[y]-sbc[y]-da[y]
    p(f"{y} {ocf[y]:6.1f} {sbc[y]:5.1f} {capex[y]:5.1f} {oe[y]:8.1f} {oa[y]:12.1f} {da[y]:8.1f} {od[y]:8.1f} {acq[y]:6.1f} {sales[y]:7.1f} {opinc[y]/sales[y]*100:6.1f}% {ni[y]/eq[y]*100:6.1f}%")
def mean(d, ys): return sum(d[y] for y in ys)/len(ys)
w5, w10 = yrs[-5:], yrs
p("")
for nm, ys in (("five-year 2021-2025", w5), ("ten-year 2016-2025", w10)):
    p(f"{nm}: owner cash equity-only mean {mean(oe,ys):.1f}; all-equity mean {mean(oa,ys):.1f}; D&A basis {mean(od,ys):.1f}; "
      f"net PP&E sales added back {mean({y:oe[y]+ppesale[y] for y in yrs},ys):.1f}; acquisitions mean {mean(acq,ys):.1f}; "
      f"op margin {sum(opinc[y] for y in ys)/sum(sales[y] for y in ys)*100:.1f}%; mean ROE {mean({y:ni[y]/eq[y] for y in yrs},ys)*100:.1f}%")
# before working capital: NI + D&A + goodwill impairment (2024 20.2) + other impairment (2023 1.2) - capex
nwc = {y: ni[y]+da[y]-capex[y] for y in yrs}; nwc[2024]+=20.2; nwc[2023]+=1.2
p(f"beside: five-year owner earnings before working capital (NI + D&A + impairments - capex) mean {mean(nwc,w5):.1f}")
# halves test for growth (decline rule b): first two vs last two years of window
h1, h2 = mean(oe,[2021,2022]), mean(oe,[2024,2025])
p(f"halves: 2021-22 mean {h1:.1f}, 2024-25 mean {h2:.1f}: sign changes, growth meaningless -> no-growth case alone")
sg = (sales[2025]/sales[2021])**(1/4)-1
p(f"sales growth 2021->2025 compound {sg*100:.1f}%/yr; 2016->2025 {((sales[2025]/sales[2016])**(1/9)-1)*100:.1f}%/yr")
def val(base, rate): return base/rate   # no growth, perpetual (zero nominal growth after year ten, and none before)
p("")
p(f"net debt 2026-06-30: borrowings {debt:.1f} - cash {cash:.1f} - current investments {inv:.1f} = {netdebt:.1f}")
cases = {
 "organic pair (central; serial-acquirer rule), all-equity": (mean(oa,w5), True),
 "organic pair, equity-only": (mean(oe,w5), False),
 "default pair (acquisitions deducted), all-equity": (mean(oa,w5)-mean(acq,w5), True),
 "default pair, equity-only": (mean(oe,w5)-mean(acq,w5), False),
 "beside: ten-year base, all-equity": (mean(oa,w10), True),
 "beside: ten-year base, equity-only": (mean(oe,w10), False),
 "beside: five-year before working capital, equity-only": (mean(nwc,w5), False),
}
for k,(b,alleq) in cases.items():
    v_r = val(b,r); v_f = val(b,floor)
    if alleq: per_r=(v_r-netdebt)/shares; per_f=(v_f-netdebt)/shares
    else: per_r=v_r/shares; per_f=v_f/shares
    p(f"{k}: base {b:.1f}; value at 5.60% {per_r:.2f}/sh; at 10% (fair, single end) {per_f:.2f}/sh")
p(f"price {price} x shares {shares} = market cap {price*shares:.1f}; EV {price*shares+netdebt:.1f}")
p(f"owner cash yield at price: all-equity {mean(oa,w5)/(price*shares+netdebt)*100:.2f}% ; equity-only {mean(oe,w5)/(price*shares)*100:.2f}%")
# returns on capital 2025, generous: EBIT + transformation cost add-back, tangible capital employed
tce = 681.7 + (16.2+12.1+319.6) - 72.0 - 2.1 - 111.8 - 124.5
p(f"2025 tangible capital employed {tce:.1f}; EBIT 65.9 -> {65.9/tce*100:.1f}% pre-tax; with transformation 19.6 added back {85.5/tce*100:.1f}%")
open("calc_output.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
