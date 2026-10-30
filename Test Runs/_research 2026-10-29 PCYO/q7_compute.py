# Q7 COMPUTATION, NOT A CLEARANCE: PCYO, figures in USD thousands from the filed cash-flow statements
yrs = ["FY2021","FY2022","FY2023","FY2024","FY2025"]
ocf = [3456, 17454, -2339, 2312, 13164]          # net cash from operating activities, as filed
sbc = [497, 603, 539, 436, 323]                   # share-based compensation, as filed
da  = [1772, 2125, 2156, 2100, 2297]              # depreciation and depletion, as filed
capex = [2896, 6668, 9497, 4829, 9652]            # all investing spending, securities purchases/maturities excluded, land sale netted (FY2025)
tbill = [0, 0, 256, 0, 0]                         # FY2023 T-bill discount removed from OCF and returned in investing: real interest, added back
intpaid = [0, 55, 142, 417, 413]                  # cash paid for interest, as filed (FY2021: none disclosed; debt zero)
TAX = 0.25                                        # CONVENTION of this run: statutory federal 21% plus Colorado 4.4%, rounded, for the after-tax interest add-back
all_sp = [o-s-c+t for o,s,c,t in zip(ocf,sbc,capex,tbill)]
maint  = [o-s-d+t for o,s,d,t in zip(ocf,sbc,da,tbill)]
for y,a,m in zip(yrs,all_sp,maint): print(f"{y}: owner cash after all spending {a:8,d}  after maintenance guess (=D&A) {m:8,d}")
avg = lambda x: sum(x)/len(x)
ia = avg([i*(1-TAX) for i in intpaid])
A_eq, M_eq = avg(all_sp), avg(maint)           # equity-only (after interest)
A_ae, M_ae = A_eq+ia, M_eq+ia                    # all-equity (before interest)
print(f"5y avg all-spending: equity-only {A_eq:,.0f}  all-equity {A_ae:,.0f}")
print(f"5y avg maintenance-only: equity-only {M_eq:,.0f}  all-equity {M_ae:,.0f}")
growth_spend = avg([c-d for c,d in zip(capex,da)])
print(f"growth spending (all spending less the maintenance guess), 5y avg: {growth_spend:,.0f}")
# growth: series changes sign -> first and second halves of the window (specific (b))
h1, h2 = avg(maint[:2]), avg(maint[3:])
g = (h2/h1)**(1/3)-1
print(f"maintenance-only halves: FY21-22 avg {h1:,.0f}, FY24-25 avg {h2:,.0f}; compound over 3 yrs {g*100:.1f}%/yr")
ha1, ha2 = avg(all_sp[:2]), avg(all_sp[3:])
print(f"all-spending halves: FY21-22 avg {ha1:,.0f}, FY24-25 avg {ha2:,.0f}")
rev = {2021:17125, 2025:26087}
print(f"sales growth FY2021-FY2025: {((26087/17125)**(1/4)-1)*100:.1f}%/yr")
def value(c, g, r):
    v = sum(c*(1+g)**t/(1+r)**t for t in range(1,11))
    return v + c*(1+g)**10/r/(1+r)**10
SH = 24097.370  # thousand shares, 10-Q cover 2026-05-31 (as of 2026-07-06 cover date)
ND = 14123 - 8440  # net debt at 2026-05-31: debt 1,454 + 12,669 less cash 8,440; restricted cash 6,193 excluded (collateral for letters of credit)
P = 10.65
r = 0.0537
print(f"net debt {ND:,}  market cap {SH*P:,.0f}  EV {SH*P+ND:,.0f}")
for label, base_ae, base_eq in [("maintenance-only (central, e)", M_ae, M_eq), ("all-spending (beside)", A_ae, A_eq)]:
    top_ae = value(base_ae, 0.0, r); bot_ae = value(base_ae, g, r) if base_ae>0 else top_ae
    top_eq = value(base_eq, 0.0, r); bot_eq = value(base_eq, g, r) if base_eq>0 else top_eq
    print(f"\n{label}: all-equity per share: top (no growth) {(top_ae-ND)/SH:6.2f}  bottom (decline {g*100:.1f}%) {(bot_ae-ND)/SH:6.2f}")
    print(f"   equity-only per share: top {top_eq/SH:6.2f} bottom {bot_eq/SH:6.2f}")
    # fair price: each end valued at 10%
    f_top = value(base_ae,0.0,0.10); f_bot = value(base_ae,g,0.10) if base_ae>0 else f_top
    fe_top = value(base_eq,0.0,0.10); fe_bot = value(base_eq,g,0.10) if base_eq>0 else fe_top
    print(f"   FAIR PRICE all-equity {((f_top+f_bot)/2-ND)/SH:6.2f}   equity-only {((fe_top+fe_bot)/2)/SH:6.2f}")
# what the price implies: owner cash needed at 10% no growth, all-equity
print(f"\nowner cash needed for the price to earn 10% at no growth (all-equity): {(SH*P+ND)*0.10:,.0f} a year")
# sensitivity: the most generous case a reader could build: maintenance-only at the sales growth 11.1% for ten years
gs = (26087/17125)**(1/4)-1
print(f"beside, not a case of the convention: maintenance-only at sales growth {gs*100:.1f}% for 10 yrs, sovereign: {(value(M_ae,gs,r)-ND)/SH:6.2f}/sh; at 10%: {(value(M_ae,gs,0.10)-ND)/SH:6.2f}/sh")
# expected return at price, no-growth maintenance-only, all-equity
print(f"earnings yield at price, maintenance-only all-equity: {M_ae/(SH*P+ND)*100:.2f}%")

# Specific (e) as written: in the growth case the growth spending is charged, grows at the carried rate, stops after year ten.
def value_e(c, gsp, g, r):
    v = sum((c*(1+g)**t - gsp*(1+g)**(t-1))/(1+r)**t for t in range(1,11))
    return v + c*(1+g)**10/r/(1+r)**10
GS = growth_spend
for lab, rr in [("sovereign", r), ("ten percent", 0.10)]:
    b = value_e(M_ae, GS, g, rr); be = value_e(M_eq, GS, g, rr)
    print(f"(e) growth case (decline {g*100:.1f}%, growth spending {GS:,.0f} in year one, {GS*(1+g)**9:,.0f} in year ten), at {lab}: all-equity {(b-ND)/SH:6.2f}/sh, equity-only {be/SH:6.2f}/sh")
top10 = value(M_ae,0,0.10); bot10 = value_e(M_ae,GS,g,0.10)
tope10 = value(M_eq,0,0.10); bote10 = value_e(M_eq,GS,g,0.10)
print(f"FAIR PRICE under (e) as written: all-equity {((top10+bot10)/2-ND)/SH:6.2f}/sh; equity-only {((tope10+bote10)/2)/SH:6.2f}/sh")
