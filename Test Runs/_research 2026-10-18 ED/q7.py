# Q7 arithmetic for the ED run, 2026-10-18. Inputs typed from the filed statements (accessions in the run file).
yrs = [2021, 2022, 2023, 2024, 2025]
ocf_cons = [2733, 3935, 2156, 3614, 4800]          # Con Edison consolidated OCF
ocf_ceb  = [175, 506, 0, 0, 0]                     # Clean Energy Businesses OCF (segment cash-flow table)
sbc      = [35, 64, 53, 35, 55]                    # AllocatedShareBasedCompensationExpense
capex    = [3983, 4226, 4789, 5273, 5295]          # utility capex + cost of removal + transmission investments (ex-CEB)
capex_tr = [30, 65, 49, 29, 50]                    # transmission part
da       = [2032-231, 2056-178, 2031, 2155, 2321]  # D&A less CEB D&A
debt_cr  = [1610+75, 700+100, 2000+50, 2375+125, 900+250]  # Utilities' net LT debt raised (CECONY filed; O&R approx), sums to 8,185
int_exp  = [905-68, 852+35, 1023-16, 1187, 1233]   # net interest expense less CEB
rev      = [13676-1022, 15670-1319, 14663-129, 15256, 16918]
tax_rt = 0.25
sov = 0.0543; floor = 0.10
shares = 369.828633   # cover, 10-Q filed 2026-08-06
price = 112.26
netdebt = 26843 + 250 + 721 + 0 + 3 - 1470   # 2026-06-30 10-Q: LTD + current + notes payable + term loan + finance leases - cash
ocf = [a-b for a,b in zip(ocf_cons, ocf_ceb)]
util_capex = [c-t for c,t in zip(capex, capex_tr)]
cap52 = 0.52*sum(util_capex)
print("OCF ex-CEB", ocf, sum(ocf))
print("capex", capex, sum(capex), "utilities", sum(util_capex), "52% cap", round(cap52))
print("debt credit", debt_cr, sum(debt_cr), "(below cap)" if sum(debt_cr) <= cap52 else "CAPPED")
eq_all = [o-s-c+d for o,s,c,d in zip(ocf,sbc,capex,debt_cr)]
eq_maint = [o-s-d_ for o,s,d_ in zip(ocf,sbc,da)]
growth_sp = [c-d_ for c,d_ in zip(capex,da)]
ati = [i*(1-tax_rt) for i in int_exp]
ae_all = [o-s-c+a for o,s,c,a in zip(ocf,sbc,capex,ati)]
ae_maint = [o-s-d_+a for o,s,d_,a in zip(ocf,sbc,da,ati)]
avg = lambda x: sum(x)/len(x)
for name, s in [("equity-only all-spending w/ debt credit", eq_all), ("equity-only maintenance-only", eq_maint),
                ("growth spending (capex-D&A)", growth_sp), ("after-tax interest", ati),
                ("all-equity all-spending", ae_all), ("all-equity maintenance-only", ae_maint)]:
    print(f"{name:45s}", [round(v) for v in s], "avg", round(avg(s)))
def pv(base, g, r, n=10):
    v = sum(base*(1+g)**t/(1+r)**t for t in range(1, n+1))
    v += base*(1+g)**n/r/(1+r)**n
    return v
sales_g = (rev[-1]/rev[0])**(1/4)-1
print("sales growth ex-CEB", round(sales_g*100,2), "% ; capped at sovereign", sov*100)
g = min(sales_g, sov)
E_all, E_m = avg(eq_all), avg(eq_maint)
A_all, A_m = avg(ae_all), avg(ae_maint)
# equity-only (central for a regulated utility)
top = pv(E_m, 0, sov)/shares; bot_g = pv(E_all, g, sov)/shares; bot_0 = pv(E_all, 0, sov)/shares
print(f"EQUITY-ONLY range: maintenance-only no-growth (top) {top:.2f}; all-spending growth {bot_g:.2f}; all-spending no-growth {bot_0:.2f}")
ftop = pv(E_m, 0, floor)/shares; fbot = pv(E_all, g, floor)/shares
print(f"EQUITY-ONLY fair: top@10% {ftop:.2f} bottom@10% {fbot:.2f} fair {((ftop+fbot)/2):.2f}")
# all-equity beside
atop = (pv(A_m, 0, sov)-netdebt)/shares; abot = (pv(A_all, g, sov)-netdebt)/shares; abot0=(pv(A_all,0,sov)-netdebt)/shares
print(f"ALL-EQUITY range: maint no-growth {atop:.2f}; all-spending growth {abot:.2f}; all-spending no-growth {abot0:.2f}; net debt {netdebt}")
aftop = (pv(A_m,0,floor)-netdebt)/shares; afbot=(pv(A_all,g,floor)-netdebt)/shares
print(f"ALL-EQUITY fair: top {aftop:.2f} bottom {afbot:.2f} fair {(aftop+afbot)/2:.2f}")
mcap = price*shares
print(f"market cap {mcap:.0f}; top-case yield {E_m/mcap*100:.2f}% no growth; all-spending yield {E_all/mcap*100:.2f}%")
# floor test: return at the price on the top case (perpetuity, no growth) and growth case
import math
def irr(base, g, price_):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if pv(base,g,mid) > price_: lo=mid
        else: hi=mid
    return mid
print(f"IRR at price: top case {irr(E_m,0,mcap)*100:.2f}%; growth case {irr(E_all,g,mcap)*100:.2f}%; top case at sales growth uncapped {irr(E_m,sales_g,mcap)*100:.2f}%")
# literal window (consolidated, CEB included) beside
lit = [o-s-c for o,s,c in zip(ocf_cons, sbc, [3964+323, 4465+337, 4509+387+0, 4728+474+0, 4996+481])]
print("literal consolidated all-spending owner cash (no debt credit; capex = segment total + cost of removal):", lit, round(avg(lit)))
# --- added on resume 2026-10-18: sensitivities (not framework cases; shown to test the floor close) ---
# (1) debt credit on GROSS long-term issuance by the Utilities (CECONY filed 2,250/700/2,000/2,850/900; O&R as above), capped at 52% of utility capex
gross = [2250+75, 700+100, 2000+50, 2850+125, 900+250]
gcred = min(sum(gross), cap52)
eq_all_g = [o-s-c+d for o,s,c,d in zip(ocf,sbc,capex,gross)]
print("gross issuance", sum(gross), "credit used", round(gcred), "equity-only all-spending (gross credit) avg", round(avg(eq_all_g)))
print(f"  IRR at price, gross-credit all-spending at capped growth: {irr(avg(eq_all_g),g,mcap)*100:.2f}%")
# (2) the strongest contrary case of the foundations: GAAP net income for common 2025 (2,023) grown at the company's 6-7% target (6.5%) ten years, then flat
print(f"  IRR at price, 2025 GAAP net income 2,023 grown 6.5% ten years then flat: {irr(2023,0.065,mcap)*100:.2f}%")
print(f"  IRR at price, same at 7.53% (sales growth, uncapped): {irr(2023,sales_g,mcap)*100:.2f}%")
# (3) the value at 10% of every case, to show none reaches the price
for nm,b,gg in [("maint-only no growth",E_m,0),("maint-only at capped growth",E_m,g),("all-spending capped growth",E_all,g),("GAAP NI 6.5%",2023,0.065)]:
    print(f"  {nm:30s} value at 10% {pv(b,gg,floor)/shares:7.2f} a share; at sovereign {pv(b,gg,sov)/shares:7.2f}")
