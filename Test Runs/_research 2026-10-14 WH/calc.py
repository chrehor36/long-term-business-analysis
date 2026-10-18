# WH owner cash and the Q7 range. USD millions. Every input is a line of a filed cash-flow statement or note:
# FY2019 10-K 0001722684-20-000007 (2017-2019), FY2021 10-K 0001722684-22-000005 (2019-2021),
# FY2023 10-K 0001722684-24-000006 (2021-2023), FY2025 10-K 0001722684-26-000007 (2023-2025), Q2 2026 10-Q 0001722684-26-000074.
import sys; sys.stdout.reconfigure(encoding="utf-8")
Y = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
OCF   = {2019:100, 2020:67, 2021:426, 2022:399, 2023:376, 2024:290, 2025:367}
LQTAX = {2019:195}                      # payment of tax liability assumed in La Quinta acquisition (purchase price, in OCF)
SBC   = {2019:20, 2020:21, 2021:28, 2022:33, 2023:39, 2024:45, 2025:43}
CAPEX = {2019:50, 2020:33, 2021:37, 2022:39, 2023:37, 2024:49, 2025:46}
FLEASE= {2019:5, 2020:5, 2021:5, 2022:5, 2023:5, 2024:39, 2025:0}   # finance-lease principal (2024 incl. $34M HQ purchase)
LOANS = {2019:2, 2020:-2, 2021:-3, 2022:0, 2023:29, 2024:16, 2025:57}   # loan advances less repayments
DANNET= {2019:17, 2020:16, 2021:30, 2022:48, 2023:72, 2024:109, 2025:105}  # development advance payments less proceeds (inside OCF)
ACQ   = {2019:195, 2022:44}             # cash paid for businesses: La Quinta tax (2019), Vienna House (2022)
SALE  = {2022:263}                      # proceeds from asset sales (two owned hotels), shown beside, not in the central base
INTPD = {2019:100, 2020:101, 2021:96, 2022:82, 2023:103, 2024:126, 2025:142}  # cash paid for interest
COBRAND = {2025:76}                     # deferred co-branded card revenue 22 -> 98: one partner advance (aberrational, spec. (d))
ADD = {2019:63500, 2020:35600, 2021:53100, 2022:70400, 2023:60800, 2024:63400, 2025:71600}
DEL = {2019:42400, 2020:70700, 2021:38900, 2022:38000, 2023:33000, 2024:31400, 2025:38400}
TAX = 0.25        # the filer's own outlook effective tax rate for 2026 (Q4 2025 release, outlook note (c))
SH = 74.211       # cover shares, 10-Q Q2 2026
NETDEBT = (23 + 2652) - 69    # 10-Q June 30, 2026: current + long-term debt less cash (restricted Revo cash excluded)
PRICE = 73.42; R = 0.0556; FLOOR = 0.10

def oc_equity(y, cobrand_adj=True):
    v = OCF[y] + LQTAX.get(y,0) - SBC[y] - CAPEX[y] - FLEASE[y] - LOANS[y] - ACQ.get(y,0)
    if cobrand_adj: v -= COBRAND.get(y,0)
    return v
def growth_share(y): return max(0.0, (ADD[y]-DEL[y])/ADD[y])
def oc_maint(y, cobrand_adj=True):   # spec. (e): add back the growth share of developer support (advances + loans)
    return oc_equity(y, cobrand_adj) + growth_share(y)*(DANNET[y] + max(LOANS[y],0))
def before_int(v, y): return v + INTPD[y]*(1-TAX)

print("year  OC-equity  OC-equity(asfiled)  maint-equity  OC-allequity  maint-allequity  growthshare  dev.support")
for y in Y:
    print(y, f"{oc_equity(y):9.1f} {oc_equity(y,False):12.1f} {oc_maint(y):13.1f} {before_int(oc_equity(y),y):12.1f} {before_int(oc_maint(y),y):14.1f} {growth_share(y):10.2f} {DANNET[y]+max(LOANS[y],0):8.0f}")
W = [2021, 2022, 2023, 2024, 2025]
def avg(f): return sum(f(y) for y in W)/len(W)
cases = {
 'all-equity, all spending (cobrand adj)':   lambda y: before_int(oc_equity(y), y),
 'all-equity, all spending (as filed)':      lambda y: before_int(oc_equity(y, False), y),
 'all-equity, maintenance only (cobrand adj)': lambda y: before_int(oc_maint(y), y),
 'all-equity, maintenance only (as filed)':  lambda y: before_int(oc_maint(y, False), y),
 'equity, all spending (cobrand adj)':       lambda y: oc_equity(y),
 'equity, maintenance only (cobrand adj)':   lambda y: oc_maint(y),
}
print()
for k, f in cases.items():
    first = (f(2021)+f(2022))/2; second = (f(2024)+f(2025))/2
    g_half = (second/first)**(1/3)-1
    g_end = (f(2025)/f(2021))**(1/4)-1
    print(f"{k:45s} 5yr avg {avg(f):7.1f}  halves {first:6.1f}->{second:6.1f} g={g_half*100:6.2f}%  end-to-end g={g_end*100:6.2f}%")
cyc = lambda y: before_int(oc_equity(y), y)
print("cycle 2019-2025 all-equity all-spending avg:", round(sum(cyc(y) for y in Y)/7,1),
      " (2019 without the La Quinta tax as acquisition:", round((sum(cyc(y) for y in Y)+195)/7,1), ")")

def pv(c0, g, r, years=10):
    v = 0; c = c0
    for t in range(1, years+1):
        c = c*(1+g); v += c/(1+r)**t
    return v + (c/r)/(1+r)**years
def per_share(ev, debt=NETDEBT): return (ev - debt)/SH

base_top = avg(cases['all-equity, maintenance only (cobrand adj)'])
base_bot = avg(cases['all-equity, all spending (cobrand adj)'])
f = cases['all-equity, all spending (cobrand adj)']; g_bot = (((f(2024)+f(2025))/2)/((f(2021)+f(2022))/2))**(1/3)-1
print()
print(f"net debt {NETDEBT}, EV at price {PRICE*SH+NETDEBT:,.0f}, market cap {PRICE*SH:,.0f}")
for name, c0, g in [("TOP: maintenance-only, no growth", base_top, 0.0), ("BOTTOM: all spending, shown decline", base_bot, g_bot),
                    ("beside: all spending, no growth", base_bot, 0.0)]:
    ev = pv(c0, g, R); ev10 = pv(c0, g, FLOOR)
    print(f"{name:40s} c0={c0:6.1f} g={g*100:6.2f}%  EV@5.56%={ev:7.0f} per share {per_share(ev):7.2f}   EV@10%={ev10:6.0f} per share {per_share(ev10):7.2f}")
# literal window as filed (spec. (a) 'the literal window shown beside')
lt = avg(cases['all-equity, maintenance only (as filed)']); lb = avg(cases['all-equity, all spending (as filed)'])
fl = cases['all-equity, all spending (as filed)']; glb = (((fl(2024)+fl(2025))/2)/((fl(2021)+fl(2022))/2))**(1/3)-1
print(f"LITERAL as filed: top {lt:.1f} -> {per_share(pv(lt,0,R)):.2f}/sh ; bottom {lb:.1f} at {glb*100:.2f}% -> {per_share(pv(lb,glb,R)):.2f}/sh")
# equity-only figures (owner cash after interest against market value)
et = avg(cases['equity, maintenance only (cobrand adj)']); eb = avg(cases['equity, all spending (cobrand adj)'])
fe = cases['equity, all spending (cobrand adj)']; geb = (((fe(2024)+fe(2025))/2)/((fe(2021)+fe(2022))/2))**(1/3)-1
print(f"EQUITY-ONLY: top {et:.1f} -> {pv(et,0,R)/SH:.2f}/sh @5.56%, {pv(et,0,FLOOR)/SH:.2f}/sh @10% ; bottom {eb:.1f} at {geb*100:.2f}% -> {pv(eb,geb,R)/SH:.2f}/sh @5.56%, {pv(eb,geb,FLOOR)/SH:.2f}/sh @10%")
fair_ae = (per_share(pv(base_top,0,FLOOR)) + per_share(pv(base_bot,g_bot,FLOOR)))/2
fair_eq = (pv(et,0,FLOOR)/SH + pv(eb,geb,FLOOR)/SH)/2
print(f"FAIR (all-equity, central) {fair_ae:.2f}   FAIR (equity-only) {fair_eq:.2f}")
# floor test: the expected return of the best case at the price (no-growth perpetuity yield = c0/EV)
for nm, c0 in [("best case maint-only cobrand adj", base_top), ("best case maint-only as filed", lt)]:
    print(f"{nm}: yield at price {c0/(PRICE*SH+NETDEBT)*100:.2f}% (no growth: expected return = yield)")
# a generous case beside: maintenance-only as filed growing at the fee-revenue growth 2022-2025
g_rev = (1429/1354)**(1/3)-1
print(f"generous beside: maint-only as filed {lt:.1f} growing {g_rev*100:.2f}% for ten years -> {per_share(pv(lt,g_rev,R)):.2f}/sh; return at price ~ {lt/(PRICE*SH+NETDEBT)*100+g_rev*100:.2f}%")

# ---- CENTRAL (spec. (a)): 2021 is a pandemic-recovery year on the filer's own description (FY2021 10-K: "Our 2021
# adjusted EBITDA recovered to 95% of 2019 levels"), so the base is the last full cycle 2019-2025 (pre-pandemic year,
# the 2020 trough, the recovery). One cycle only: growth between successive cycles cannot be measured, so by (b) the range
# is the no-growth case alone; with no growth credited, no acquisition spending is charged (spec. (c), purchases stop with growth).
def oc_eq_noacq(y): return oc_equity(y) + ACQ.get(y,0)
def oc_mt_noacq(y): return oc_maint(y) + ACQ.get(y,0)
ae_all = sum(before_int(oc_eq_noacq(y), y) for y in Y)/7
ae_mt  = sum(before_int(oc_mt_noacq(y), y) for y in Y)/7
eq_all = sum(oc_eq_noacq(y) for y in Y)/7
eq_mt  = sum(oc_mt_noacq(y) for y in Y)/7
print()
print("CENTRAL cycle base 2019-2025, no growth, before acquisitions:")
print(f"  all-equity: all spending {ae_all:.1f} -> {per_share(ae_all/R):.2f}/sh ; maintenance only {ae_mt:.1f} -> {per_share(ae_mt/R):.2f}/sh ; width {per_share(ae_mt/R)/per_share(ae_all/R):.2f}:1")
print(f"  best yield at price {ae_mt/(PRICE*SH+NETDEBT)*100:.2f}%")
fa = (per_share(ae_all/FLOOR) + per_share(ae_mt/FLOOR))/2
fe2 = (eq_all/FLOOR/SH + eq_mt/FLOOR/SH)/2
print(f"  FAIR all-equity {fa:.2f} (ends {per_share(ae_all/FLOOR):.2f}, {per_share(ae_mt/FLOOR):.2f}) ; FAIR equity-only {fe2:.2f} (ends {eq_all/FLOOR/SH:.2f}, {eq_mt/FLOOR/SH:.2f})")
print(f"  equity-only range at 5.56%: {eq_all/R/SH:.2f} to {eq_mt/R/SH:.2f}")
