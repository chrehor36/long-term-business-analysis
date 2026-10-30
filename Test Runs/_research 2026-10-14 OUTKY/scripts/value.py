# OUTKY: owner cash by year, cycle bases, Q7 range and fair price. COMPUTATION, NOT A CLEARANCE.
# Every input is a filed figure (Outokumpu financial statements releases / annual reports, EUR million)
# except those marked GUESS, which are disclosed in the run file.
yrs   = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
ocf   = [389, 328, 214, 371, 322, 597, 778, 325, 147, 79]     # net cash from operating activities (after interest and tax paid)
capex = [156, 186, 245, 189, 166, 156, 160, 170, 211, 144]     # purchases of PP&E + intangibles (cash)
lease = [10,  10,  10,  34,  33,  32,  33,  39,  38,  42]      # repayments of lease liabilities; 2016-18 GUESS (finance leases, pre-IFRS 16)
sbc   = [5,   13,  5,   2,   1,   7,   8,   1,   2,   1]       # share-based payment expense; 2016, 2018, 2019, 2021 GUESS
intpd = [105, 92,  70,  56,  69,  63,  39,  47,  48,  52]      # interest paid; 2016-18 interest EXPENSE used (paid not extracted)
da    = [226, 216, 204, 230, 243, 259, 245, 242, 220, 215]     # depreciation and amortization (2021 incl. Long Products)
sales = [5690,6356,6872,6403,5639,7243,9494,6961,5942,5468]
TAX = 0.20  # Finnish statutory rate, used to put interest after tax for the all-equity basis
eq  = [o-c-l-s for o,c,l,s in zip(ocf,capex,lease,sbc)]
ae  = [e + i*(1-TAX) for e,i in zip(eq,intpd)]
dep = [o-d-l-s for o,d,l,s in zip(ocf,da,lease,sbc)]  # depreciation variant (D&A in place of capex)
print("year  owner_cash_equity  all_equity  dep_variant  share_of_sales")
for y,e,a,d,s in zip(yrs,eq,ae,dep,sales): print(y, e, round(a), d, f"{e/s:.1%}")
avg=lambda v: sum(v)/len(v)
A_eq, B_eq = avg(eq[:5]), avg(eq[5:]); A_ae, B_ae = avg(ae[:5]), avg(ae[5:])
A_dep, B_dep = avg(dep[:5]), avg(dep[5:])
print(f"cycle A 2016-20 eq {A_eq:.0f} ae {A_ae:.0f} dep {A_dep:.0f}; cycle B 2021-25 eq {B_eq:.0f} ae {B_ae:.0f} dep {B_dep:.0f}")
g = lambda a,b: (b/a)**(1/5)-1
g_ae, g_eq = g(A_ae,B_ae), g(A_eq,B_eq)
sA, sB = avg(sales[:5]), avg(sales[5:]); g_s = g(sA,sB)
print(f"growth between cycles: all-equity {g_ae:.2%} equity {g_eq:.2%} sales {g_s:.2%} (A sales incl. Long Products)")
hi_share = max(e/s for e,s in zip(eq,sales)); print(f"highest owner-cash share of sales {hi_share:.1%}")
def pv(c,gr,r):
    v=sum(c*(1+gr)**t/(1+r)**t for t in range(1,11))
    return v + c*(1+gr)**10/r/(1+r)**10
R=0.0376; NETDEBT=224; SH=471.377716; PRICE=5.015
for label,c,gr in [("all-equity",B_ae,g_ae),("equity",B_eq,g_eq)]:
    # cap (f): carried ten years, does owner cash exceed the highest share of sales? then use sales growth
    c10 = c*(1+gr)**10; s10 = sB*(1+g_s)**10
    cut = c10/s10 > hi_share
    gr2 = min(g_s,R) if cut else gr
    print(f"{label}: base {c:.0f}, shown growth {gr:.2%}, year-10 share {c10/s10:.1%} -> cut={cut}, carried {gr2:.2%}")
    lo = pv(c,0,R); hi = pv(c,gr2,R)
    if label=="all-equity":
        print(f"  range EV {lo:.0f}-{hi:.0f}; per share {(lo-NETDEBT)/SH:.2f}-{(hi-NETDEBT)/SH:.2f}; width {hi/lo:.2f}x")
        f = (pv(c,0,0.10)+pv(c,gr2,0.10))/2; print(f"  fair (ends at 10%, averaged) per share {(f-NETDEBT)/SH:.2f}; ends {(pv(c,0,0.10)-NETDEBT)/SH:.2f} / {(pv(c,gr2,0.10)-NETDEBT)/SH:.2f}")
        ev = PRICE*SH+NETDEBT; print(f"  EV at price {ev:.0f}; no-growth yield {c/ev:.1%}")
        # floor test: return earned by each end case at the price (IRR solving pv(c,g,irr)=ev)
        for gg in (0,gr2):
            lo_r,hi_r=0.0001,0.5
            for _ in range(100):
                mid=(lo_r+hi_r)/2
                if pv(c,gg,mid)>ev: lo_r=mid
                else: hi_r=mid
            print(f"  expected return at price, growth {gg:.2%}: {mid:.1%}")
    else:
        print(f"  range per share {lo/SH:.2f}-{hi/SH:.2f}")
        f=(pv(c,0,0.10)+pv(c,gr2,0.10))/2; print(f"  fair equity-only per share {f/SH:.2f}")
# literal window shown beside: sign change in window -> halves; meaningless -> no-growth only
print("literal window 2021-25 eq", eq[5:], "ae", [round(x) for x in ae[5:]])
lw = B_ae; print(f"literal no-growth all-equity per share {(pv(lw,0,R)-NETDEBT)/SH:.2f}")
# depreciation variant beside
print(f"dep variant cycle B all-equity base {B_dep+avg(intpd[5:])*(1-TAX):.0f}")
