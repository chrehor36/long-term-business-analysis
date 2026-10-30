# Q7 COMPUTATION, NOT A CLEARANCE (the file closed at Q2). USD millions. Inputs from cf_output.txt (XBRL, first-filed,
# checked against the 10-K cash-flow statements for FY2023-FY2025) and the 10-Q of 2026-06-30.
yrs = [2021, 2022, 2023, 2024, 2025]
OCF   = [182.7, 217.3, 233.1, 281.4, 329.8]
SBC   = [11.6, 8.2, 9.1, 12.2, 14.2]
CAPEX = [123.3, 131.0, 154.9, 203.2, 245.1]
FLPP  = [6.5, 7.8, 9.0, 12.1, 20.9]      # finance-lease principal, equipment bought on lease: capital spending
ACQ   = [170.6, 78.2, 851.8, 468.6, 224.2]
INTP  = [19.0, 21.0, 43.6, 61.2, 59.0]
TAXP  = [1.4, 2.8, 10.1, 6.8, -0.2]
PRETAX= [58.0, 75.0, 37.0, 21.0, 13.1]
INTX  = [21.2, 23.7, 47.6, 62.4, 62.5]
REV   = [889.2, 1085.1, 1264.5, 1557.3, 1836.8]
ORG   = [6.1, 12.4, 7.0, 3.8, 4.2]         # filer's solid-waste organic change: price+volume+surcharges+commodity (acquisitions out), %
T = 0.21                                  # federal statutory rate (CONVENTION of this run: state tax left out, said so)
r, floor = 0.0537, 0.10
shares = 63.640046
net_debt = 1350.7 - 25.5                  # 10-Q 2026-06-30: debt incl. finance leases (net of issuance costs) less cash
ue = []; eq = []
for i in range(5):
    pre = OCF[i] + INTP[i] + TAXP[i]      # operating cash before interest and tax paid
    ue.append(pre - T*(PRETAX[i] + INTX[i]) - SBC[i] - CAPEX[i] - FLPP[i])   # all-equity, before purchases
    eq.append(OCF[i] + TAXP[i] - T*PRETAX[i] - SBC[i] - CAPEX[i] - FLPP[i])  # equity-only, before purchases
    print(yrs[i], f"all-equity {ue[i]:7.1f}  equity-only {eq[i]:7.1f}  after purchases {ue[i]-ACQ[i]:8.1f}  share of sales {100*ue[i]/REV[i]:4.1f}%")
m = lambda x: sum(x)/len(x)
C, Ce = m(ue), m(eq)
print(f"5-yr mean all-equity {C:.1f}; equity-only {Ce:.1f}; purchases total {sum(ACQ):.1f} vs owner cash before purchases {sum(ue):.1f} -> serial acquirer: {sum(ACQ) > 0.5*sum(ue)}")
print(f"default pair (purchases deducted) mean {m([ue[i]-ACQ[i] for i in range(5)]):.1f}")
g_org = m(ORG)/100
g_shown = (ue[-1]/ue[0])**0.25 - 1
print(f"organic growth mean {100*g_org:.2f}%; shown growth of owner cash incl. bought growth {100*g_shown:.1f}%; sales CAGR {100*((REV[-1]/REV[0])**0.25-1):.1f}%")
def val(c, g, rate):
    v = sum(c*(1+g)**t/(1+rate)**t for t in range(1, 11))
    return v + c*(1+g)**10/rate/(1+rate)**10
for basis, c, nd in (("all-equity", C, net_debt), ("equity-only", Ce, 0.0)):
    lo, hi = val(c, 0, r), val(c, g_org, r)
    print(f"{basis}: range whole {lo:7.0f} to {hi:7.0f}; per share {(lo-nd)/shares:7.2f} to {(hi-nd)/shares:7.2f}; width {hi/lo:.2f}x")
    f0, f1 = val(c, 0, floor), val(c, g_org, floor)
    print(f"   fair price (each end at 10%, averaged) {((f0+f1)/2-nd)/shares:7.2f} per share")
    # expected return at the price: rate that sets the growth case equal to price
    P = 89.39*shares + nd
    lo_r, hi_r = 0.0001, 0.5
    for _ in range(100):
        mid = (lo_r+hi_r)/2
        (lo_r, hi_r) = (mid, hi_r) if val(c, g_org, mid) > P else (lo_r, mid)
    print(f"   expected return at $89.39 on the growth case {100*mid:.2f}%; no-growth case {100*c/P:.2f}%")
# literal window beside: latest year as base
print(f"latest-year base all-equity {ue[-1]:.1f}: growth-case value per share {(val(ue[-1], g_org, r)-net_debt)/shares:.2f}")
