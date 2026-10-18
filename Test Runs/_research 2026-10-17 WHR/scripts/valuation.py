"""COMPUTATION, NOT A CLEARANCE. Q7 range and fair price for WHR, per the v5 Q7 construction. USD millions."""
yrs = list(range(2016, 2026))
ocf  = [1203,1264,1229,1230,1500,2176,1390,915,835,470]
sbc  = [39,48,51,50,67,82,58,33,28,28]          # AllocatedShareBasedCompensationExpense (filed expense)
capex= [660,684,590,532,410,525,570,549,451,389]
da   = [655,654,645,587,568,494,475,361,333,338]
intp = [198,181,183,194,193,169,161,370,352,350] # cash paid for interest
acq  = [12,35,25,0,0,46,3000,14,0,0]            # cash paid for businesses
sold = [0,0,160,1174,166,302-393,77-75,10,95-245,198-327]  # proceeds less cash held by divested businesses; 2016-17 not read (0)
TAX = 0.25; R = 0.0543; FLOOR = 0.10
NETDEBT = 16+212+6840-1239       # 2026-06-30 borrowings less cash; operating leases left out
SH = 65.199378 + 0.575*14.4920   # millions, as-converted
PRICE = 27.89
oc = [o-s-c for o,s,c in zip(ocf,sbc,capex)]
net_purch = [a-b for a,b in zip(acq,sold)]
oc_after = [x-p for x,p in zip(oc,net_purch)]
ati = [i*(1-TAX) for i in intp]
avg = lambda v: sum(v)/len(v)
def pv(c0, g, r, n=10):
    v, c = 0.0, c0
    for t in range(1, n+1):
        c *= (1+g); v += c/(1+r)**t
    return v + c/r/(1+r)**n
def per_share(ev): return (ev-NETDEBT)/SH
print("year owner_cash net_purchases after_purch after-tax_interest")
for y,a,b,c,d in zip(yrs,oc,net_purch,oc_after,ati): print(y,a,b,c,round(d,1))
print("sum owner cash", sum(oc), "sum net purchases", sum(net_purch), " half of owner cash", sum(oc)/2)
d_eq = avg(oc_after); d_ae = d_eq + avg(ati)
o_eq = avg(oc); o_ae = o_eq + avg(ati)
h1 = avg(oc_after[:5]); h2 = avg(oc_after[5:])
o1 = avg(oc[:5]); o2 = avg(oc[5:]); g_org = (o2/o1)**(1/5)-1
print(f"default pair (purchases deducted): avg equity-only {d_eq:.1f}, all-equity {d_ae:.1f}; halves {h1:.1f} -> {h2:.1f} (sign change: no-growth case alone)")
print(f"organic pair (purchases left out): avg equity-only {o_eq:.1f}, all-equity {o_ae:.1f}; halves {o1:.1f} -> {o2:.1f}, g = {g_org*100:.2f}%/yr")
print(f"net debt {NETDEBT}, shares {SH:.3f}M, EV at price {PRICE*SH+NETDEBT:.0f}")
cases = {
 "central default no-growth, all-equity": (d_ae, 0.0, True),
 "central default no-growth, equity-only": (d_eq, 0.0, False),
 "organic top no-growth, all-equity": (o_ae, 0.0, True),
 "organic bottom shown growth, all-equity": (o_ae, g_org, True),
 "organic top no-growth, equity-only": (o_eq, 0.0, False),
 "organic bottom shown growth, equity-only": (o_eq, g_org, False),
}
for k,(c,g,ae) in cases.items():
    v = pv(c,g,R); f = pv(c,g,FLOOR)
    ps = per_share(v) if ae else v/SH
    fp = per_share(f) if ae else f/SH
    print(f"{k:45s} value/share at 5.43% {ps:8.2f}   at 10% {fp:8.2f}")
# expected yield at price on each case (no-growth): cash / price paid
ev = PRICE*SH+NETDEBT
print(f"no-growth yields at the price: default all-equity {d_ae/ev*100:.1f}%, organic all-equity {o_ae/ev*100:.1f}%, default equity-only {d_eq/(PRICE*SH)*100:.1f}%, organic equity-only {o_eq/(PRICE*SH)*100:.1f}%")
# literal five-year window 2021-2025
l_eq = avg(oc_after[5:]); l_ae = l_eq + avg(ati[5:]); lo_eq = avg(oc[5:]); lo_ae = lo_eq + avg(ati[5:])
print(f"literal window 2021-25: default equity-only {l_eq:.1f}, all-equity {l_ae:.1f} -> per share at 5.43% {per_share(l_ae/R):.2f}; organic equity-only {lo_eq:.1f} all-equity {lo_ae:.1f} -> {per_share(lo_ae/R):.2f}")
# D&A variant beside
print(f"D&A variant: avg capex {avg(capex):.1f} vs avg D&A {avg(da):.1f}")
# 2026 company outlook beside (projection, recorded not used)
oc26 = 700-400-28; print("2026 outlook-implied equity-only owner cash ~", oc26)
