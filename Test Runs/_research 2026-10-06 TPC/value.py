"""COMPUTATION, NOT A CLEARANCE. Q7 convention arithmetic for TPC (USD millions). Inputs from tpc_span.py."""
r = 0.0566; sh = 52.569; price = 86.43
def pv(c, g, n=10):
    v = 0; cf = c
    for t in range(1, n+1):
        cf = c*(1+g)**t; v += cf/(1+r)**t
    return v + (c*(1+g)**n)/r/(1+r)**n   # then zero nominal growth (convention)
cases = {"five-year mean 2021-2025 (capex basis)":186.2, "five-year D&A variant":205.2,
         "whole cycle 2010-2025 (capex basis)":39.4, "whole cycle D&A variant":48.1}
g_shown = (5543.0/4175.7)**(1/12)-1   # revenue CAGR 2013-2025, the only steady growth series shown
print(f"growth shown (revenue 2013-2025 CAGR): {100*g_shown:.2f}%")
for k,c in cases.items():
    lo, hi = pv(c,0), pv(c,g_shown)
    print(f"{k:42s} C={c:6.1f}  no-growth {lo:7.0f} (${lo/sh:6.2f})  shown-growth {hi:7.0f} (${hi/sh:6.2f})")
lo_all = pv(39.4,0)/sh; hi_all = pv(205.2,g_shown)/sh
print(f"widest span: ${lo_all:.2f} to ${hi_all:.2f}  ratio {hi_all/lo_all:.1f} : 1")
tax = 0.30   # FY2025 effective rate, filed
for k,c in [("whole cycle",39.4),("five-year",186.2)]:
    pre = c/(1-tax)
    for g in (0, g_shown):
        cap = pre/(0.10-g)
        print(f"FAIR {k:11s} g={100*g:.2f}%: pre-tax owner cash {pre:6.1f}; cap at which yield+g = 10% pre-tax: {cap:7.0f} -> ${cap/sh:6.2f}; cheap (half) ${cap/sh/2:6.2f}")
print(f"price ${price}; market cap {price*sh:.0f}; owner-cash yield at price: five-year {186.2/(price*sh)*100:.2f}%  whole-cycle {39.4/(price*sh)*100:.2f}% (after tax)")
