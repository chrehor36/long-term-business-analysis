# COMPUTATION, NOT A CLEARANCE. EMAT 2026-10-13. Figures in $ thousands from the filings named in the run file.
r_sov = 0.056   # US Treasury 30-year par, 2026-10-09
r_floor = 0.10  # Q7 floor CONVENTION
price = 1.47
shares = 627_200_646   # 424B3 0001213900-26-108471, as of 2026-10-02
# owner cash by filed period
p2024_ocf = -3138.108; months_2024 = 10.75   # EM LLC 2024-02-08 to 2024-12-31, ex99.2 of 0001213900-26-036749
p2025_ocf = -8612.478                         # EM LLC FY2025, same exhibit; no capex filed
h1_ocf, h1_capex, h1_sbc, h1_inv_exp, h1_int_paid = -14818, -7736, -1947, -2837, -168  # 10-Q 0001213900-26-090427
oc2024 = p2024_ocf * 12 / months_2024
oc2025 = p2025_ocf
oc_h1 = h1_ocf + h1_capex + h1_sbc + h1_inv_exp      # after stock pay and investor-paid expenses
oc_h1_ann = oc_h1 * 2
oc_h1_ann_preint = (oc_h1 - h1_int_paid) * 2         # before interest (all-equity basis)
mean3 = (oc2024 + oc2025 + oc_h1_ann) / 3
# net debt at 2026-06-30 plus the 10-Q's own subsequent event (July 2026 debenture, $5.225M left after conversions, ~$5.6M cash)
borrow = 2625 + 1659 + 1246 + 2296 + 2309 + 16 + 17395
cash = 5254
nd = borrow - cash + 5225 - 5600
nd_with_step6d = nd + 47553 + 461    # non-trade payables incl. the Step 6-D obligation, shown beside
def per_share(v): return v * 1000 / shares
print(f"owner cash 2024 annualized {oc2024:,.0f}; 2025 {oc2025:,.0f}; H1 2026 {oc_h1:,.0f} (annualized {oc_h1_ann:,.0f}; before interest {oc_h1_ann_preint:,.0f}); three-period mean {mean3:,.0f}")
print(f"net debt {nd:,.0f}; with non-trade payables {nd_with_step6d:,.0f}")
for label, oc_eq, oc_ae in [("central: combined company H1 2026 annualized", oc_h1_ann, oc_h1_ann_preint), ("beside: three-period mean", mean3, mean3)]:
    v_ae = oc_ae / r_sov - nd; v_eq = oc_eq / r_sov
    f_ae = oc_ae / r_floor - nd; f_eq = oc_eq / r_floor
    print(f"{label}: value all-equity {per_share(v_ae):.2f}/sh, equity-only {per_share(v_eq):.2f}/sh; fair all-equity {per_share(f_ae):.2f}/sh, equity-only {per_share(f_eq):.2f}/sh; with Step 6-D in net debt fair all-equity {per_share(oc_ae/r_floor - nd_with_step6d):.2f}/sh")
print(f"market cap {price*shares/1e6:,.0f}M at {price}")
