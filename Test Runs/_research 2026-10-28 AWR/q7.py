"""Q7 arithmetic for the AWR run of 2026-10-28. Figures from the filed statements (see run file). USD millions.
Arithmetic only: every rule applied is the framework's (Q7 range convention, specifics (a)-(f), The regulated utility,
Part VII fair price)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")

yrs = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
ocf = dict(zip(yrs, [116.864, 122.170, 115.584, 117.799, 67.683, 198.732, 229.730]))
sbc = dict(zip(yrs, [2.517, 2.463, 2.566, 2.571, 3.298, 3.744, 3.559]))
capex = dict(zip(yrs, [151.940, 130.423, 144.515, 166.240, 188.540, 231.960, 236.822]))
da = dict(zip(yrs, [35.713, 37.204, 39.974, 41.697, 43.254, 44.226, 48.873]))
dev = dict(zip(yrs, [10.171 - 5.005, 9.338 - 3.729, 12.432 - 4.666, 6.901 - 5.321, 11.889 - 4.540, 11.195 - 4.919, 13.981 - 5.833]))
oth = dict(zip(yrs, [-1.424 + 0.169, -1.275 + 0.088, -1.142 + 0.565, -0.921 + 0.059, -0.224, -0.820, -0.719]))
reg = dict(zip(yrs, [None, 10.150, -5.842, -18.915, -81.373, 18.487, 46.124]))  # regulatory assets/liabilities line in OCF
interest_paid = dict(zip([2021, 2022, 2023, 2024, 2025], [22.540, 26.005, 39.367, 50.347, 46.050]))
pretax = dict(zip([2021, 2022, 2023, 2024, 2025], [124.770, 102.060, 166.520, 149.441, 169.798]))
taxexp = dict(zip([2021, 2022, 2023, 2024, 2025], [30.423, 23.664, 41.599, 30.173, 39.356]))
rev = dict(zip([2021, 2025], [498.853, 658.073]))

W = [2021, 2022, 2023, 2024, 2025]
ocm = {y: ocf[y] - sbc[y] - da[y] + dev[y] + oth[y] for y in yrs}      # owner cash after maintenance only
oca = {y: ocf[y] - sbc[y] - capex[y] + dev[y] + oth[y] for y in yrs}   # owner cash after all spending
avg = lambda d, ks: sum(d[k] for k in ks) / len(ks)
OCm, OCa = avg(ocm, W), avg(oca, W)
CAP, DA = avg(capex, W), avg(da, W)
GS = CAP - DA
print("owner cash after maintenance by year", {y: round(ocm[y], 1) for y in yrs})
print("owner cash after all spending by year", {y: round(oca[y], 1) for y in yrs})
print(f"5y means: OC maint {OCm:.2f}  OC all {OCa:.2f}  capex {CAP:.2f}  D&A {DA:.2f}  growth spending {GS:.2f}")

# utility debt credit
ltd_2020, ltd_2025 = 444.271, 794.310
inc = (ltd_2025 - ltd_2020) / 5
cap_share = 0.43
credit = min(inc, cap_share * GS)
print(f"LTD increase/yr {inc:.2f}; cap 43% x GS = {cap_share*GS:.2f}; credit {credit:.2f}")
GSnet = GS - credit

# growth shown and the cap
end_cagr = (ocm[2025] / ocm[2021]) ** 0.25 - 1
sales_g = (rev[2025] / rev[2021]) ** 0.25 - 1
r = 0.0530
max_share = max(ocm[y] / v for y, v in [(2025, 658.073), (2024, 595.459), (2023, 595.699), (2022, 491.528), (2021, 498.853)])
print(f"shown growth (end years) {end_cagr*100:.1f}%; 10y at it -> {OCm*(1+end_cagr)**10:.0f} vs highest share of sales {max_share*100:.1f}%; sales growth {sales_g*100:.2f}%")
g = min(sales_g, r)
print(f"growth carried g = {g*100:.2f}% (sales growth, never above the discount rate {r*100:.2f}%)")

def value(base, gsnet, g, rate, years=10):
    """PV of (base - gsnet) growing at g for 10 years, then base*(1+g)^10 flat forever; gsnet stops at year 10."""
    pv = sum((base - gsnet) * (1 + g) ** t / (1 + rate) ** t for t in range(1, years + 1))
    term = base * (1 + g) ** years / rate / (1 + rate) ** years
    return pv + term

shares = 39.635626
price = 85.48
mcap = shares * price
print(f"shares {shares}M  price {price}  mcap {mcap:.1f}")

def report(label, base, gsnet, g, netdebt=0.0):
    ng_r = base / r - netdebt
    gr_r = value(base, gsnet, g, r) - netdebt
    ng_10 = base / 0.10 - netdebt
    gr_10 = value(base, gsnet, g, 0.10) - netdebt
    lo, hi = sorted([ng_r, gr_r])
    fair = (ng_10 + gr_10) / 2
    print(f"{label}: no-growth {ng_r/shares:7.2f}  growth {gr_r/shares:7.2f}  range {lo/shares:.2f}-{hi/shares:.2f}"
          f"  width {hi/lo if lo>0 else float('nan'):.2f}x | at 10%: no-growth {ng_10/shares:.2f} growth {gr_10/shares:.2f}"
          f"  FAIR {fair/shares:.2f}")
    return lo / shares, hi / shares, fair / shares

print("\n== CENTRAL: equity-only, regulated utility, maintenance case (e), debt credit on growth spending")
report("central", OCm, GSnet, g)
print(f"   growth spending gross yr1 {GS*(1+g):.1f} yr10 {GS*(1+g)**10:.1f}; credit yr1 {credit*(1+g):.1f} yr10 {credit*(1+g)**10:.1f}; net yr1 {GSnet*(1+g):.1f} yr10 {GSnet*(1+g)**10:.1f}")

print("\n== BESIDE (e): all spending charged, credit applied, no growth")
print(f"   owner cash all spending + credit = {OCa + credit:.2f}; value at 5.30% {(OCa+credit)/r/shares:.2f}/sh; at 10% {(OCa+credit)/0.10/shares:.2f}/sh")
print(f"   all spending, no credit: {OCa:.2f} (negative; no value)")

# implied growth at the price? the return the price implies on the central no-growth case
print(f"\n   earnings yield of central maintenance owner cash at the price: {OCm/mcap*100:.2f}%")

# all-equity beside
tax = sum(taxexp.values()) / sum(pretax.values())
intat = avg(interest_paid, W) * (1 - tax)
netdebt = 717.735 + 73.227 + 119.0 - 21.657
print(f"\n== BESIDE: all-equity basis (tax {tax*100:.1f}%, interest after tax {intat:.2f}, net debt 2026-06-30 {netdebt:.1f}; operating leases left out)")
report("all-equity", OCm + intat, GS, g, netdebt)

# variants on the base (specific (a) and (d))
print("\n== VARIANTS on the base")
cyc = avg(ocm, [2022, 2023, 2024])
norm = {y: ocm[y] - reg[y] for y in W}
norm[2025] -= 14.7  # PFAS proceeds, filer-described one-off
print("   normalized (reg asset/liability line removed, 2025 PFAS removed)", {y: round(v, 1) for y, v in norm.items()})
for lab, b in [("cycle base 2022-2024 (one rate case)", cyc), ("literal window incl. 2019-2020 (7y)", avg(ocm, yrs)), ("normalized 5y", avg(norm, W))]:
    report(lab + f" base {b:.1f}", b, GSnet, g)
print(f"\n   growth of normalized series end years: {((norm[2025]/norm[2021])**0.25-1)*100:.1f}%")
