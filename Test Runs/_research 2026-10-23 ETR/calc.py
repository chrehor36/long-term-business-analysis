"""ETR run 2026-10-23: Q7 arithmetic (COMPUTATION, NOT A CLEARANCE). Every input is a filed figure, USD millions,
from the cash-flow statements of the FY2022 10-K (0000065984-23-000014; 2021, 2022) and the FY2025 10-K
(0000065984-26-000174; 2023-2025), the stock-pay note (Note 12) of each, and the 10-Q for 2026-06-30
(0000065984-26-000283). No rule is computed here; the run file states which case is which."""
Y = [2021, 2022, 2023, 2024, 2025]
OCF   = [2300.713, 2585.490, 4294.328, 4488.510, 5150.651]
INV   = [-6179.276, -5709.897, -4628.977, -5849.010, -7109.454]   # net cash used in investing (all lines)
STORM = [0.0, 3163.572, 1457.676, 0.0, 0.0]                      # securitization proceeds via state-authority trusts (financing)
SBC   = [45.3+17.3, 45.4+18.4, 40.2+18.0, 42.9+20.1, 43.1+22.1]   # stock pay expensed + capitalized (Note 12)
CAPEX = [6087.296, 5065.126, 4440.652, 4838.339, 7684.922]
AFUDCE= [70.473, 72.832, 98.493, 133.046, 180.726]
NFUEL = [166.512, 223.613, 270.973, 309.437, 252.912]
PLANT = [168.304, 106.193, 35.094, 821.934, 3.517]
DA    = [2242.944, 2190.371, 2244.479, 2443.562, 2537.138]        # depreciation, amortization, decommissioning, nuclear fuel amortization
LTD_I = [8308.427, 6019.835, 4273.297, 7898.968, 5750.445]
LTD_R = [4827.827, 5995.903, 5135.753, 5054.094, 3501.800]
CP    = [-426.312, -373.556, 310.550, -210.880, -269.517]
ADV   = [0.0, 0.0, 259.505-108.903, 547.500-204.991, 1643.765-662.896]  # customer advances for construction, net (financing)
INT   = [843.228, 901.884, 987.252, 1114.631, 1238.284]           # interest paid, net of capitalized
REV   = [11742.896, 13764.237, 12147.412, 11879.653, 12946.686]
avg = lambda a: sum(a)/len(a)
pre   = [OCF[i]+INV[i]+STORM[i]-SBC[i] for i in range(5)]
netb  = [LTD_I[i]-LTD_R[i]+CP[i] for i in range(5)]
ltonly= [LTD_I[i]-LTD_R[i] for i in range(5)]
spend = [CAPEX[i]-AFUDCE[i]+NFUEL[i]+PLANT[i] for i in range(5)]
# allowed debt share: rate-base-weighted (1 - equity ratio), Entergy Arkansas also less ADIT at zero cost (2.2/11.4)
rb = {"EAI":(11.4,0.3803,2.2/11.4),"ELL":(16.7,0.5091,0),"EMI":(4.6,0.4983,0),"ENO":(1.2,0.55,0),"ETI":(4.4,0.512,0),"SERI":(1.79,0.508,0)}
dshare = sum(v[0]*(1-v[1]-v[2]) for v in rb.values())/sum(v[0] for v in rb.values())
cap = dshare*sum(spend)
credit = min(sum(netb), cap)
print("year        OCF    invest   storm   SBC    pre-credit  netborrow  spend   D&A")
for i in range(5):
    print(Y[i], f"{OCF[i]:8.1f} {INV[i]:9.1f} {STORM[i]:7.1f} {SBC[i]:5.1f} {pre[i]:10.1f} {netb[i]:9.1f} {spend[i]:8.1f} {DA[i]:7.1f}")
print(f"sum pre-credit {sum(pre):.1f}  avg {avg(pre):.1f}")
print(f"capital spending sum {sum(spend):.1f}; allowed debt share {dshare*100:.1f}%; cap {cap:.1f}")
print(f"net borrowing (LT+CP) sum {sum(netb):.1f}; LT only {sum(ltonly):.1f}; credit {credit:.1f} (cap binding: {sum(netb)>cap})")
eo = avg(pre) + credit/5
print(f"EQUITY-ONLY owner cash, all spending, debt credited: {eo:.1f}/yr")
print(f"  beside: LT-only credit {avg(pre)+min(sum(ltonly),cap)/5:.1f}; with customer advances {eo+avg(ADV):.1f}")
by = [pre[i]+netb[i] for i in range(5)]
print("  by year:", [round(x,1) for x in by])
maint = [OCF[i]-DA[i]-SBC[i] for i in range(5)]
print("MAINTENANCE-AT-DEPRECIATION owner cash by year:", [round(x,1) for x in maint], f"avg {avg(maint):.1f}")
tax = 0.21
ae = avg(pre) + avg(INT)*(1-tax)
print(f"ALL-EQUITY owner cash (pre-credit + after-tax interest at 21%): {ae:.1f}/yr; maint all-equity {avg(maint)+avg(INT)*(1-tax):.1f}")
# market
price, sh = 108.19, 466.631498 + 11.145984
mcap = price*sh
debt = 31547.652 + 1510.174 + 1569.496
cash = 3854.045
nd = debt - cash
nd_settle = nd - 913.0
print(f"shares {sh:.3f}M  mcap {mcap:,.0f}  net debt 2026-06-30 {nd:,.0f}  (after the 2026-09-02 settlement cash {nd_settle:,.0f})")
r, n = 0.0529, 10
def val(c0, g, rate, spend_g=0.0):
    pv = 0.0; c = c0
    for t in range(1, n+1):
        c = c0*(1+g)**t
        pv += (c - spend_g)/(1+rate)**t
    return pv + (c0*(1+g)**n)/rate/(1+rate)**n
print("--- VALUES (equity-only, $M and per share) ---")
for name, c0, g, sg in [("bottom: all spending, no growth", eo, 0, 0), ("top: maintenance at depreciation, no growth", avg(maint), 0, 0)]:
    v = val(c0, g, r, sg); v10 = val(c0, g, 0.10, sg)
    print(f"{name}: at {r*100:.2f}% {v:,.0f} = ${v/sh:.2f}; at 10% {v10:,.0f} = ${v10/sh:.2f}")
sg_rev = (REV[4]/REV[0])**(1/4)-1
print(f"sales growth 2021-2025 {sg_rev*100:.2f}%/yr")
gspend = avg(maint) - eo
v = val(avg(maint), sg_rev, r, gspend)
print(f"maintenance case grown at sales growth, growth spending {gspend:.1f}/yr charged: {v:,.0f} = ${v/sh:.2f}")
# generosity check: 2023-25 maintenance base, 8% growth, no growth spending charged, at 10%
b = avg(maint[2:]); vg = val(b, 0.08, 0.10)
print(f"generosity check: base {b:.1f} at 8% growth, nothing charged, at 10%: {vg:,.0f} = ${vg/sh:.2f} vs price {price}")
# implied return of the generosity case at the price: solve rate where value = mcap
lo, hi = 0.0, 0.5
for _ in range(100):
    mid = (lo+hi)/2
    if val(b, 0.08, mid) > mcap: lo = mid
    else: hi = mid
print(f"  return at the price for that case {mid*100:.2f}%")
lo, hi = 0.001, 0.5
for _ in range(100):
    mid = (lo+hi)/2
    if val(avg(maint), 0, mid) > mcap: lo = mid
    else: hi = mid
print(f"return at the price, top case (maintenance, no growth): {mid*100:.2f}%  (yield {avg(maint)/mcap*100:.2f}%)")
print(f"yield at the price, bottom case: {eo/mcap*100:.2f}%")
# fair price: each end at 10%, averaged
fb = val(eo,0,0.10)/sh; ft = val(avg(maint),0,0.10)/sh
print(f"FAIR (equity-only, central): ends ${fb:.2f} and ${ft:.2f}; average ${(fb+ft)/2:.2f}")
ab = (val(ae,0,0.10)-nd)/sh; at = (val(avg(maint)+avg(INT)*(1-tax),0,0.10)-nd)/sh
print(f"FAIR (all-equity, beside): ends ${ab:.2f} and ${at:.2f}; average ${(ab+at)/2:.2f}")
# literal window shown beside: central series compound growth meaningless (sign change); halves
print("halves (central series by year):", round(avg(by[:2]),1), round(avg(by[3:]),1))
print("--- (e) CENTRAL RANGE: maintenance-only no-growth (top) and the growth case with its spending charged (bottom) ---")
g = sg_rev
gc = val(avg(maint), g, r, gspend); gc10 = val(avg(maint), g, 0.10, gspend)
mt = val(avg(maint), 0, r); mt10 = val(avg(maint), 0, 0.10)
print(f"equity-only: growth case at {r*100:.2f}% ${gc/sh:.2f}, at 10% ${gc10/sh:.2f}; maintenance no-growth at {r*100:.2f}% ${mt/sh:.2f}, at 10% ${mt10/sh:.2f}")
print(f"FAIR equity-only central: (${gc10/sh:.2f} + ${mt10/sh:.2f})/2 = ${(gc10+mt10)/2/sh:.2f}")
mae = avg(maint)+avg(INT)*(1-tax); gsp_ae = mae - ae
gca = val(mae, g, 0.10, gsp_ae); mta = val(mae, 0, 0.10)
gca5 = val(mae, g, r, gsp_ae); mta5 = val(mae, 0, r)
print(f"all-equity: growth spending {gsp_ae:.1f}/yr; range at {r*100:.2f}% ${(gca5-nd)/sh:.2f} to ${(mta5-nd)/sh:.2f}; at 10% ends ${(gca-nd)/sh:.2f}, ${(mta-nd)/sh:.2f}; FAIR ${((gca+mta)/2-nd)/sh:.2f}")
# does any case earn the floor at the price? return at price of each case
def irr(c0, gg, sgp):
    lo, hi = 0.0005, 0.5
    for _ in range(200):
        mid = (lo+hi)/2
        if val(c0, gg, mid, sgp) > mcap: lo = mid
        else: hi = mid
    return mid
print(f"return at the price: growth case {irr(avg(maint), g, gspend)*100:.2f}%; maintenance no-growth {irr(avg(maint),0,0)*100:.2f}%")
