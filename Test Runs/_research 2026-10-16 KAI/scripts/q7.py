# Q7 arithmetic for KAI, 2026-10-16. Inputs: filed 10-K cash-flow, income and debt lines (accessions in run file).
yrs = ["FY2021","FY2022","FY2023","FY2024","FY2025"]
ocf  = [162.420,102.625,165.545,155.265,171.328]
sbc  = [8.527,8.576,9.765,10.639,11.242]
capex= [12.771,28.199,31.850,21.005,17.048]
fl   = [1.044,1.002,1.100,1.169,1.216]      # finance-lease principal
mdiv = [0.560,0.630,0.000,1.346,1.698]      # dividends to minority partners
acq  = [143.981,3.474,0.905,300.335,189.983]
dep  = [None,None,14.849,20.547,22.924]     # depreciation only (10-K FY2025 recon, 2023-2025)
intpaid=[4.441,6.053,8.071,19.699,14.925]
intinc=[0.267,0.904,1.758,1.915,1.929]
pretax=[112.052,165.636,159.016,153.070,143.585]
tax  = [27.171,43.906,42.210,40.516,39.904]
rev  = [786.579,904.739,957.672,1053.384,1052.248]
org  = [None,0.15,0.06,-0.02,-0.04]         # consolidated organic revenue change, as the filer reports it
r = 0.0543; floor = 0.10
shares = 11.809117
netdebt = 510.632 - 134.533   # 2026-07-04: long-term obligations incl. current and finance leases, less cash
price = 264.15
oc_eq, oc_ae, oc_acq = [], [], []
for i,y in enumerate(yrs):
    t = tax[i]/pretax[i]
    eq = ocf[i]-sbc[i]-capex[i]-fl[i]-mdiv[i]
    ae = eq + (intpaid[i]-intinc[i])*(1-t)
    oc_eq.append(eq); oc_ae.append(ae); oc_acq.append(ae-acq[i])
    print(f"{y}: tax {t:.3f} owner cash equity-only {eq:7.1f}  all-equity {ae:7.1f}  after acquisitions {ae-acq[i]:7.1f}  OC/sales {ae/rev[i]:.3f}")
m = lambda v: sum(v)/len(v)
print("5-yr means: equity-only %.1f all-equity %.1f after-acq %.1f" % (m(oc_eq), m(oc_ae), m(oc_acq)))
print("net purchases %.1f vs owner cash before purchases %.1f (serial acquirer if > half)" % (sum(acq), sum(oc_ae)))
g = 1.0
for x in org[1:]: g *= 1+x
g = g**(1/4)-1
print("organic revenue CAGR FY2021->FY2025: %.4f" % g)
salesg = (rev[-1]/rev[0])**(1/4)-1
print("reported revenue CAGR FY2021->FY2025: %.4f" % salesg)
def value(oc, g, rate, years=10):
    pv = 0; c = oc
    for k in range(1, years+1):
        c *= (1+g); pv += c/(1+rate)**k
    pv += (c/rate)/(1+rate)**years   # zero nominal growth after year ten
    return pv
def pershare(ev, nd): return (ev-nd)/shares
for label, base, nd in [("all-equity", m(oc_ae), netdebt), ("equity-only", m(oc_eq), 0.0)]:
    lo = value(base, 0.0, r); hi = value(base, g, r)
    flo = value(base, 0.0, floor); fhi = value(base, g, floor)
    print(f"{label}: base {base:.1f}  range EV {lo:.0f}..{hi:.0f}  per share ${pershare(lo,nd):.0f} .. ${pershare(hi,nd):.0f}  width {hi/lo if lo>0 else float('nan'):.2f}")
    print(f"   at 10%: ${pershare(flo,nd):.0f} .. ${pershare(fhi,nd):.0f}  fair (average) ${ (pershare(flo,nd)+pershare(fhi,nd))/2:.0f}")
# depreciation variant (2023-2025 only, where depreciation is filed separately)
dv = [ocf[i]-sbc[i]-dep[i]-fl[i]-mdiv[i]+(intpaid[i]-intinc[i])*(1-tax[i]/pretax[i]) for i in (2,3,4)]
print("depreciation variant, all-equity, 3-yr mean %.1f vs capex basis same years %.1f" % (m(dv), m(oc_ae[2:])))
# implied return at the price: IRR of the growth case, all-equity
ev_price = price*shares + netdebt
def irr(base, g):
    lo_, hi_ = 0.0001, 0.5
    for _ in range(200):
        mid = (lo_+hi_)/2
        if value(base, g, mid) > ev_price: lo_ = mid
        else: hi_ = mid
    return mid
print("EV at price %.0f; expected return no-growth %.4f, growth case %.4f" % (ev_price, irr(m(oc_ae),0.0), irr(m(oc_ae), g)))
print("growth needed for 10%% at the price (ten years then flat): ", end="")
lo_, hi_ = 0.0, 0.6
for _ in range(200):
    mid=(lo_+hi_)/2
    if value(m(oc_ae), mid, floor) < ev_price: lo_=mid
    else: hi_=mid
print("%.4f" % mid)
# default pair beside: acquisitions deducted, total growth (first vs second half; series changes sign)
print("default pair: after-acquisition means first half (FY21-22) %.1f second half (FY24-25) %.1f, five-year mean %.1f" % (m(oc_acq[:2]), m(oc_acq[3:]), m(oc_acq)))
# Profil beside: credited at its price (neutral), i.e. add back its cost
print("Profil credited at its price paid (170.1) adds $%.1f a share" % (170.1/shares))
