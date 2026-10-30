# Q7 arithmetic for HGV. USD millions. Every input is transcribed from the filed statements named in the run file.
yrs = [2021, 2022, 2023, 2024, 2025]
ocf  = dict(zip(yrs, [168, 747, 312, 309, 300]))
nr_in  = dict(zip(yrs, [264, 769, 868, 1849, 3738]))   # proceeds from non-recourse debt
nr_out = dict(zip(yrs, [359, 990, 694, 1590, 3334]))   # repayment of non-recourse debt
sbc  = dict(zip(yrs, [48, 46, 40, 47, 64]))
capex= dict(zip(yrs, [18+21, 58+39, 31+44, 42+84, 70+76]))  # property and equipment + software
corp_int = dict(zip(yrs, [105, 142, 178, 329, 311]))   # interest expense (corporate debt)
cons_int = dict(zip(yrs, [30, 47, 50, 99, 117]))       # consumer financing interest expense (2021 from FY2022 10-K)
acq  = dict(zip(yrs, [1592, 0, 74, 1444, 0]))          # acquisitions, net of cash acquired
rev  = dict(zip(yrs, [2335, 3835, 3978, 4981, 5047]))
T = 0.25   # CONVENTION of this run: tax shield on interest at 21% federal plus state
r_gov, floor = 0.0556, 0.10
price, shares = 35.18, 77.724
mcap = price*shares
corp_debt, cash = 4876, 272          # 2026-06-30, 10-Q
nr_debt = 2896
net_debt = corp_debt - cash

def eq_oc(y):  # equity-level owner cash: finance arm self-funded (net non-recourse borrowing counted as its working capital)
    return ocf[y] + nr_in[y] - nr_out[y] - sbc[y] - capex[y]
def un_oc(y):  # all-equity: add back after-tax corporate interest
    return eq_oc(y) + corp_int[y]*(1-T)
def p2_oc(y):  # alternative: non-recourse debt counted as debt; add back after-tax interest on both
    return ocf[y] - sbc[y] - capex[y] + (corp_int[y]+cons_int[y])*(1-T)

print("year  OCF  NRnet  SBC capex | eq_OC  unlev_OC | NR-as-debt OC | acq | OC/rev(unlev)")
for y in yrs:
    print(y, ocf[y], nr_in[y]-nr_out[y], sbc[y], capex[y], "|", eq_oc(y), round(un_oc(y),2), "|", round(p2_oc(y),2), "|", acq[y], f"{un_oc(y)/rev[y]:.1%}")

def avg(f, ys): return sum(f(y) for y in ys)/len(ys)
base_ys = [2022, 2023, 2024, 2025]
B_un = avg(un_oc, base_ys); B_eq = avg(eq_oc, base_ys); B_p2 = avg(p2_oc, base_ys)
L_un = avg(un_oc, yrs); L_eq = avg(eq_oc, yrs)
A4 = sum(acq[y] for y in base_ys)/4; A5 = sum(acq.values())/5
print(f"\nbase 2022-25: unlev {B_un:.2f} equity {B_eq:.2f} NR-as-debt {B_p2:.2f}; literal 2021-25: unlev {L_un:.2f} equity {L_eq:.2f}")
print(f"acquisitions per year: base {A4:.1f}, literal {A5:.1f}")
print(f"serial-acquirer test: purchases {sum(acq.values())} vs half of unlev OC before purchases {sum(un_oc(y) for y in yrs)/2:.1f} and half of equity OC {sum(eq_oc(y) for y in yrs)/2:.1f}")

# organic growth as the filer reports it: pro forma / actual revenue, 2022 -> 2025
g_org = ((3978/3835)*(5028/5013)*(5047/5028))**(1/3)-1
# total growth shown, unlevered owner cash 2022 -> 2025 (acquisitions included)
g_tot = (un_oc(2025)/un_oc(2022))**(1/3)-1
g_rev_tot = (rev[2025]/rev[2022])**(1/3)-1
print(f"organic growth (pro forma revenue 2022-25) {g_org:.2%}; total unlev OC growth 2022-25 {g_tot:.2%}; total revenue growth {g_rev_tot:.2%}")

def pv(c0, g, r, n=10):
    v=0; c=c0
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**n
def irr(c0, g, target):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if pv(c0,g,mid) > target: lo=mid
        else: hi=mid
    return mid

ev = mcap + net_debt
print(f"\nprice {price}  shares {shares}  mcap {mcap:.0f}  net debt {net_debt}  EV {ev:.0f}")
cases = {
 "organic pair, no growth (central bottom)": (B_un, 0.0),
 "organic pair, organic growth (central top)": (B_un, g_org),
 "default pair, acq deducted, total growth": (B_un-A4, g_tot),
 "default pair, acq deducted, no growth": (B_un-A4, 0.0),
 "literal window 2021-25, organic, no growth": (L_un, 0.0),
 "literal window 2021-25, organic growth": (L_un, g_org),
}
# cap check for the total-growth case: owner cash in year 10 against the highest share of sales earned
maxshare = max(un_oc(y)/rev[y] for y in base_ys)
c10 = (B_un-A4)*(1+g_tot)**10; s10 = rev[2025]*(1+g_rev_tot)**10
print(f"cap check (default pair): year-10 OC {c10:.0f} vs sales {s10:.0f} -> {c10/s10:.1%}; highest share earned {maxshare:.1%}")
print("\ncase | base | g | value@5.56% | per share (less net debt) | expected return at price | value@10% per share")
res={}
for k,(c,g) in cases.items():
    v = pv(c,g,r_gov); v10 = pv(c,g,floor)
    res[k]=((v-net_debt)/shares, (v10-net_debt)/shares)
    print(f"{k} | {c:.1f} | {g:.2%} | {v:.0f} | {(v-net_debt)/shares:.2f} | {irr(c,g,ev):.2%} | {(v10-net_debt)/shares:.2f}")

# equity-only (owner cash after all interest, against market value)
print("\nequity-only: base", round(B_eq,2), "yield at price", f"{B_eq/mcap:.2%}")
for k,g in [("eq no growth",0.0),("eq organic",g_org)]:
    print(k, f"value@5.56% per share {pv(B_eq,g,r_gov)/shares:.2f}", f"exp return {irr(B_eq,g,mcap):.2%}", f"value@10% per share {pv(B_eq,g,floor)/shares:.2f}")
fair_eq = (pv(B_eq,0,floor)+pv(B_eq,g_org,floor))/2/shares
fair_un = ((pv(B_un,0,floor)+pv(B_un,g_org,floor))/2 - net_debt)/shares
print(f"\nFAIR PRICE (central, organic pair, all-equity): {fair_un:.2f}; equity-only: {fair_eq:.2f}")
# NR counted as debt, beside
nd2 = net_debt + nr_debt
fair_p2 = ((pv(B_p2,0,floor)+pv(B_p2,g_org,floor))/2 - nd2)/shares
print(f"beside: non-recourse debt counted in net debt ({nd2}): base {B_p2:.1f}, range {(pv(B_p2,0,r_gov)-nd2)/shares:.2f} to {(pv(B_p2,g_org,r_gov)-nd2)/shares:.2f}, exp return no-growth {irr(B_p2,0,mcap+nd2):.2%}, fair {fair_p2:.2f}")
# default pair fair beside
fair_def = ((pv(B_un-A4,0,floor)+pv(B_un-A4,g_tot,floor))/2 - net_debt)/shares
print(f"beside: default pair fair {fair_def:.2f}")

# (e) maintenance guess: VOI inventory spending above the cost of inventory relieved by the year's sales
inv_spend = {2022:182, 2023:298, 2024:445, 2025:369}
inv_relieved = {2022:274-33+22, 2023:194-1+10, 2024:239-30+48, 2025:152-0+105}  # cost of VOI sales, deferrals/recognitions undone
growth_inv = {y: inv_spend[y]-inv_relieved[y] for y in base_ys}
G = sum(growth_inv.values())/4
print("\n(e) growth inventory by year", growth_inv, "avg", G)
M_un = B_un + G; M_eq = B_eq + G
top = pv(M_un,0,r_gov); bot = pv(B_un,g_org,r_gov)
print(f"(e) maintenance-only no-growth: base {M_un:.2f} value {(top-net_debt)/shares:.2f}/sh exp return {irr(M_un,0,ev):.2%}")
print(f"(e) growth case, all spending charged, organic growth: value {(bot-net_debt)/shares:.2f}/sh exp return {irr(B_un,g_org,ev):.2%}")
fair_e = ((pv(M_un,0,floor)+pv(B_un,g_org,floor))/2 - net_debt)/shares
fair_e_eq = (pv(M_eq,0,floor)+pv(B_eq,g_org,floor))/2/shares
print(f"FAIR (e central, all-equity): {fair_e:.2f}; equity-only: {fair_e_eq:.2f}")
print(f"equity-only exp returns at price: maint no-growth {irr(M_eq,0,mcap):.2%}, growth case {irr(B_eq,g_org,mcap):.2%}")
# owner cash needed for 10% on EV, no growth
print(f"owner cash needed for 10% at EV, no growth: {0.10*ev:.0f}")
# with 21% shield sensitivity
