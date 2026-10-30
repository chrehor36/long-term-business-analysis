# CTAS Q7 arithmetic. Inputs transcribed from the filed 10-Ks (accessions in notes.md). USD millions.
R = 0.0530          # 30-yr Treasury par yield 2026-10-27 (tools/sources.py)
FLOOR = 0.10
PRICE = 214.80      # close 2026-10-27, aggregator (tools/run.py)
SHARES = 397.075093 # cover, 10-Q filed 2026-10-07, as of 2026-09-30
# net debt: 10-Q 2026-08-31 face debt 2,436.55 less cash 243.599, plus buybacks after 8/31 through 10/7 stated in that 10-Q (494.0)
NET_DEBT = 2436.55 - 243.599 + 494.0
years = [2022, 2023, 2024, 2025, 2026]
OCF   = [1537.625, 1597.814, 2068.500, 2165.905, 2276.280]   # FY24 as re-presented in FY26 10-K
SBC   = [109.308, 103.621, 116.986, 128.329, 128.076]
CAPEX = [240.672, 331.109, 409.469, 408.884 - 23.972, 395.105]  # FY25 net of PP&E sale proceeds
ACQ   = [164.228 - 15.347, 46.357, 186.837, 232.899, 164.548]   # FY22 net of operating assets sold
DEP   = [249.376, 257.041, 280.866, 303.377, 318.637]
INTX  = [88.844, 111.232, 100.740, 101.108, 106.285]
INTI  = [0.242, 1.716, 5.742, 5.584, 5.107]
TAXR  = [263.011/1498.768, 345.138/1693.148, 402.043/1973.635, 451.921/2264.202, 505.366/2505.334]
WC    = [-188.3, -154.2, 95.5, -62.7, -248.6]  # AR, inventory, rental items, AP, accrued comp, accrued & other, taxes
REV   = [7854.459, 8815.769, 9596.615, 10340.181, 11264.761]
n = 5
oc_pre = [OCF[i]-SBC[i]-CAPEX[i] for i in range(n)]
oc     = [oc_pre[i]-ACQ[i] for i in range(n)]
aint   = [(INTX[i]-INTI[i])*(1-TAXR[i]) for i in range(n)]
oc_ae  = [oc[i]+aint[i] for i in range(n)]
oc_ae_pre = [oc_pre[i]+aint[i] for i in range(n)]
gspend = [CAPEX[i]-DEP[i] for i in range(n)]
avg = lambda x: sum(x)/len(x)
def cagr(a, b, yrs): return (b/a)**(1/yrs)-1
print("year  OCF-SBC-capex  -acq  +aftertax int (all-equity)  share of sales")
for i in range(n):
    print(years[i], f"{oc_pre[i]:8.1f} {oc[i]:8.1f} {oc_ae[i]:8.1f}  {oc_ae[i]/REV[i]:.3f}")
B_eq, B_ae, B_ae_pre = avg(oc), avg(oc_ae), avg(oc_ae_pre)
g = cagr(oc_ae[0], oc_ae[-1], 4); g_eq = cagr(oc[0], oc[-1], 4); gs = cagr(REV[0], REV[-1], 4)
print(f"5-yr avg: equity-only {B_eq:.1f}; all-equity {B_ae:.1f}; all-equity before purchases {B_ae_pre:.1f}")
print(f"growth shown FY22->FY26: all-equity {g:.4f}; equity-only {g_eq:.4f}; sales {gs:.4f}")
print(f"net purchases {sum(ACQ):.1f} vs half owner cash before purchases {sum(oc_pre)/2:.1f}")
print(f"avg growth spending (capex-dep) {avg(gspend):.1f}; avg WC build {-avg(WC):.1f}; avg acq {avg(ACQ):.1f}")
# cap (f): year-10 owner cash vs sales path at own sales growth from FY26
hist_share = max(oc_ae[i]/REV[i] for i in range(n))
fy21_share = (1360.740-112.035-143.470-10.038+98.210*(1-176.781/1287.749))/7116.340
print(f"highest share of sales in window {hist_share:.3f}; FY2021 {fy21_share:.3f}")
oc10 = B_ae*(1+g)**10; s10 = REV[-1]*(1+gs)**10
print(f"cap test: year-10 owner cash {oc10:.0f} vs sales {s10:.0f} share {oc10/s10:.3f}")
def value(base, gr, r, base_pre=None, addback=0.0):
    """years 1-10 at base grown; after year 10 zero growth on base_pre (purchases stop) plus addback (growth spending stops)."""
    base_pre = base if base_pre is None else base_pre
    pv = sum(base*(1+gr)**t/(1+r)**t for t in range(1, 11))
    term = (base_pre*(1+gr)**10 + addback*(1+gr)**10)/r/(1+r)**10
    return pv + term
add_g = avg(gspend) + (-avg(WC))      # growth capex and WC build stop after year ten in the growth case
cases = {}
for r, lab in ((R, "sovereign"), (FLOOR, "at 10%")):
    nog = value(B_ae, 0.0, r, B_ae_pre)
    gro = value(B_ae, g, r, B_ae_pre, add_g)
    nog_eq = value(B_eq, 0.0, r, avg(oc_pre))
    gro_eq = value(B_eq, g_eq, r, avg(oc_pre), add_g)
    cases[lab] = (nog, gro, nog_eq, gro_eq)
    print(f"[{lab}] all-equity EV: no-growth {nog:,.0f}  growth {gro:,.0f}; per share less net debt {(nog-NET_DEBT)/SHARES:.2f} .. {(gro-NET_DEBT)/SHARES:.2f}")
    print(f"[{lab}] equity-only: per share {nog_eq/SHARES:.2f} .. {gro_eq/SHARES:.2f}")
lo, hi = [(x-NET_DEBT)/SHARES for x in cases["sovereign"][:2]]
print(f"VALUE RANGE (central, all-equity) {lo:.2f} to {hi:.2f}; width {hi/lo:.2f}x; price {PRICE}")
fair = (avg(cases["at 10%"][:2]) - NET_DEBT)/SHARES
fair_eq = avg(cases["at 10%"][2:])/SHARES
print(f"FAIR PRICE all-equity {fair:.2f}; equity-only {fair_eq:.2f}")
# literal window without purchases-stop/growth-spending-stop refinements
lit_hi = (sum(B_ae*(1+g)**t/(1+R)**t for t in range(1,11)) + B_ae*(1+g)**10/R/(1+R)**10 - NET_DEBT)/SHARES
print(f"literal growth case (all spending, purchases forever) {lit_hi:.2f}; literal no-growth {(B_ae/R-NET_DEBT)/SHARES:.2f}")
# expected return at the price: IRR of the growth case (all-equity)
EV = PRICE*SHARES + NET_DEBT
def irr(base, gr, base_pre, addb):
    lo_, hi_ = 0.0, 0.5
    for _ in range(100):
        m = (lo_+hi_)/2
        if value(base, gr, m, base_pre, addb) > EV: lo_ = m
        else: hi_ = m
    return m
print(f"EV at price {EV:,.0f}; implied return growth case {irr(B_ae, g, B_ae_pre, add_g):.4f}; no-growth {irr(B_ae, 0, B_ae_pre, 0):.4f}")
# maintenance-only variant (depreciation as the maintenance guess; WC build as growth spending)
oc_m = [OCF[i]-SBC[i]-DEP[i]-WC[i]-ACQ[i]+aint[i] for i in range(n)]
oc_m_pre = [x+ACQ[i] for i, x in enumerate(oc_m)]
Bm = avg(oc_m); gm = cagr(oc_m[0], oc_m[-1], 4)
print("maintenance-only all-equity by year", [round(x,1) for x in oc_m], f"avg {Bm:.1f} growth {gm:.4f}")
# growth case on maintenance basis: growth spending charged, grows with growth, stops at yr 10
def value_m(r, gr):
    gsp = add_g
    pv = sum((Bm*(1+gr)**t - gsp*(1+gr)**t)/(1+r)**t for t in range(1,11))
    term = avg(oc_m_pre)*(1+gr)**10/r/(1+r)**10
    return pv + term
vm0 = avg(oc_m)/R  # no-growth maintenance-only, purchases charged (literal)
vm0_pre = sum(Bm/(1+R)**t for t in range(1,11)) + avg(oc_m_pre)/R/(1+R)**10
vmg = value_m(R, g)
print(f"maintenance variant per share: no-growth {(vm0_pre-NET_DEBT)/SHARES:.2f}; growth {(vmg-NET_DEBT)/SHARES:.2f}")
fm = (avg([sum(Bm/(1.1)**t for t in range(1,11)) + avg(oc_m_pre)/0.1/1.1**10, value_m(0.1, g)]) - NET_DEBT)/SHARES
print(f"maintenance variant fair price {fm:.2f}")
# signed, unclosed UniFirst deal beside (as if closed; UNF FY2021-FY2025 filed record; no synergies)
UNF_SH = 14.586347 + 3.501265
unf_oc = [212.3-133.6-7.0-8.4, 122.6-144.3-9.1-44.2, 215.8-172.0-9.1-306.2, 295.3-160.4-9.8-0.2, 296.9-154.3-12.2-11.9]
unf_pre = [212.3-133.6-7.0, 122.6-144.3-9.1, 215.8-172.0-9.1, 295.3-160.4-9.8, 296.9-154.3-12.2]
cash_paid = 155.0*UNF_SH; new_sh = 0.7720*UNF_SH
nd2 = NET_DEBT + cash_paid - 192.1
B2, B2pre = B_ae+avg(unf_oc), B_ae_pre+avg(unf_pre)
print(f"UNF avg owner cash {avg(unf_oc):.1f} (before purchases {avg(unf_pre):.1f}); cash paid {cash_paid:.0f}; shares issued {new_sh:.3f}M")
v0 = value(B2, 0, R, B2pre); v1 = value(B2, g, R, B2pre, add_g)
print(f"with deal: range {(v0-nd2)/(SHARES+new_sh):.2f} to {(v1-nd2)/(SHARES+new_sh):.2f}")
f2 = (avg([value(B2,0,FLOOR,B2pre), value(B2,g,FLOOR,B2pre,add_g)]) - nd2)/(SHARES+new_sh)
print(f"with deal: fair price {f2:.2f}")
# organic pair beside (purchases left out; organic growth as the filer reports it, FY2023-FY2026: 12.2, 8.0, 8.0, 8.3)
go = (1.122*1.080*1.080*1.083)**0.25 - 1
o0 = value(B_ae_pre, 0, R, B_ae_pre); o1 = value(B_ae_pre, go, R, B_ae_pre, add_g)
print(f"organic pair: growth {go:.4f}; range {(o0-NET_DEBT)/SHARES:.2f} to {(o1-NET_DEBT)/SHARES:.2f}")
fo = (avg([value(B_ae_pre,0,FLOOR,B_ae_pre), value(B_ae_pre,go,FLOOR,B_ae_pre,add_g)]) - NET_DEBT)/SHARES
print(f"organic pair fair price {fo:.2f}; implied return at price, organic growth case {irr(B_ae_pre, go, B_ae_pre, add_g):.4f}")
# tangible returns (operating income over equity + debt - cash - goodwill; and including goodwill)
for fy, oi, eq, debt, cash, gw in ((2018, 949.834, 3016.5, 2535.3, 138.7, 2846.9), (2021, 1385.492, 3687.8, 2542.3, 493.6, 2913.1), (2026, 2606.512, 5139.9, 2428.1, 289.0, 3544.2)):
    ce = eq + debt - cash
    print(fy, f"pre-tax return on capital ex goodwill {oi/(ce-gw):.3f}; incl goodwill {oi/ce:.3f}")
print(f"incremental FY21->FY26 ex goodwill {(2606.512-1385.492)/((5139.9+2428.1-289.0-3544.2)-(3687.8+2542.3-493.6-2913.1)):.3f}; incl goodwill {(2606.512-1385.492)/((5139.9+2428.1-289.0)-(3687.8+2542.3-493.6)):.3f}")
