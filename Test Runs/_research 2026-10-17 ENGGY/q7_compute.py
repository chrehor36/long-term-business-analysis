# ENGGY Q7 arithmetic. Inputs: Enagas consolidated cash flow statements (EUR M), annual reports
# FY2022 (Spanish, 2021 column), FY2023 (Spanish), FY2025 (English; 2024 and 2025 columns).
yrs  = [2021, 2022, 2023, 2024, 2025]
cfo  = [579.934, 726.031, 568.839, 454.992, 212.542]   # net cash from operating activities (after interest, tax, WC)
wc   = [39.474, 235.342, 205.726, -73.710, -259.876]   # change in operating working capital (inside CFO)
divr = [160.268, 121.268, 192.213, 160.055, 163.369]   # "other proceeds from investment activities" (Note 1.6: dividends from equity investees)
capx = [69.854, 90.786, 156.967, 97.892, 118.122]      # fixed assets and real estate investments
acq  = [10.641+33.516, 23.012+36.440, 187.791+23.414, 26.281+15.875, 65.366+12.770]  # group cos/associates + other financial assets
intp = [82.473, 70.923, 101.750, 62.869, 63.120]       # interest paid
intr = [13.291, 12.138, 31.762, 50.343, 35.052]        # interest received
T = 0.25   # Spanish statutory corporate rate (CONVENTION of this run for the interest add-back)

oc_eq   = [c+d-k-a for c,d,k,a in zip(cfo,divr,capx,acq)]           # equity-only, after purchases, WC counted
oc_eq_pre = [c+d-k for c,d,k in zip(cfo,divr,capx)]                  # before purchases
addback = [(p-r)*(1-T) for p,r in zip(intp,intr)]
oc_ae   = [o+b for o,b in zip(oc_eq,addback)]
oc_ae_pre = [o+b for o,b in zip(oc_eq_pre,addback)]
growth_series = [c-w+d-k for c,w,d,k in zip(cfo,wc,divr,capx)]       # pre-WC, pre-purchase (total growth)
avg = lambda x: sum(x)/len(x)
for n,s in [("owner cash equity-only after purchases",oc_eq),("equity-only before purchases",oc_eq_pre),
            ("interest add-back after tax",addback),("all-equity after purchases",oc_ae),("all-equity before purchases",oc_ae_pre),
            ("growth series (pre-WC, pre-purchase)",growth_series)]:
    print(f"{n:42s}", " ".join(f"{v:8.1f}" for v in s), f"| avg {avg(s):8.1f}")
g = (growth_series[-1]/growth_series[0])**(1/4)-1
g_lit = (oc_ae[-1]/oc_ae[0])**(1/4)-1
print(f"growth end-to-end on growth series: {g*100:.2f}%  (literal all-equity series end-to-end {g_lit*100:.2f}%)")

def value(base, base_pre, gr, r, years=10):
    pv=0; cf=base; cfp=base_pre
    for t in range(1,years+1):
        cf*= (1+gr); cfp*=(1+gr)
        pv+= cf/(1+r)**t
    term = cfp/r/(1+r)**years      # zero nominal growth after year ten, purchases stop
    return pv+term

rf = 0.0367; floor=0.10
shares = 261.990074-1.980298        # M shares outstanding (issued less treasury, 31 Dec 2025)
nd = 2475.098; nd_h1 = 2305.0; terega = 573.0
price = 16.81; fx = 1.1253
for basis,b,bp in [("ALL-EQUITY",avg(oc_ae),avg(oc_ae_pre)),("EQUITY-ONLY",avg(oc_eq),avg(oc_eq_pre))]:
    debt = nd if basis=="ALL-EQUITY" else 0.0
    top = value(b,bp,0.0,rf); bot = value(b,bp,g,rf)
    ft = value(b,bp,0.0,floor); fb = value(b,bp,g,floor)
    ps = lambda ev: (ev-debt)/shares
    print(f"\n{basis}: base {b:.1f}, base before purchases {bp:.1f}")
    print(f"  range EV: bottom {bot:,.0f}  top {top:,.0f}  width {top/bot:.2f}x (EV) ; per share {ps(bot):.2f} to {ps(top):.2f} EUR (width {ps(top)/ps(bot):.2f}x)")
    fair = (ps(ft)+ps(fb))/2
    print(f"  at 10%: no-growth {ps(ft):.2f}, decline {ps(fb):.2f} -> FAIR {fair:.2f} EUR/share = {fair/2*fx:.2f} USD/ADS")
    print(f"  range per ADS USD: {ps(bot)/2*fx:.2f} to {ps(top)/2*fx:.2f}")
    if basis=="ALL-EQUITY":
        for lab,d2 in [("H1-2026 net debt (press release)",nd_h1),("plus Terega signed",nd+terega)]:
            print(f"  beside, {lab}: fair {((value(b,bp,0,floor)-d2)/shares+(value(b,bp,g,floor)-d2)/shares)/2:.2f}; range {(bot-d2)/shares:.2f} to {(top-d2)/shares:.2f}")
    # floor test: expected return at price for each case (IRR solving)
    ev_price = price*shares + debt
    for lab,gr in [("no-growth",0.0),("decline",g)]:
        lo,hi=0.0,1.0
        for _ in range(100):
            mid=(lo+hi)/2
            if value(b,bp,gr,mid)>ev_price: lo=mid
            else: hi=mid
        print(f"  expected return at price EUR {price} ({lab}): {mid*100:.2f}%")
mc = price*shares
print(f"\nmarket cap EUR {mc:,.0f}M; EV (all-equity) {mc+nd:,.0f}M")

# --- beside figures ---
b, bp = avg(oc_ae), avg(oc_ae_pre)
print("\nBESIDE (all-equity, Dec-2025 net debt):")
gl = g_lit
for lab, gr in [("literal window decline", gl)]:
    v_rf = value(b, bp, gr, rf); v10 = value(b, bp, gr, floor)
    print(f"  {lab} {gr*100:.1f}%: value at sovereign {(v_rf-nd)/shares:.2f}/share; at 10% {(v10-nd)/shares:.2f}/share")
dna  = [262.837, 264.122, 273.343, 287.108, 283.841]
dvar = b - (avg(dna) - avg(capx))
dvar_pre = bp - (avg(dna) - avg(capx))
print(f"  depreciation variant base {dvar:.1f} (D&A avg {avg(dna):.1f} vs capex avg {avg(capx):.1f}); no-growth at sovereign {(value(dvar,dvar_pre,0,rf)-nd)/shares:.2f}, at 10% {(value(dvar,dvar_pre,0,floor)-nd)/shares:.2f}/share")
# expected return, no-growth, with H1-2026 net debt
ev_h1 = price*shares + nd_h1
lo,hi=0.0,1.0
for _ in range(100):
    mid=(lo+hi)/2
    if value(b,bp,0.0,mid)>ev_h1: lo=mid
    else: hi=mid
print(f"  expected return no-growth with H1-2026 net debt {nd_h1}: {mid*100:.2f}%")
print(f"  serial-acquirer test: net purchases over window {sum(acq):.1f} vs half of owner cash before purchases {0.5*sum(oc_ae_pre):.1f}")
