# HTCMY: Q7 range and fair price, COMPUTATION, NOT A CLEARANCE (the file closed at Q2).
# Every input is a filed figure (see owner_cash.py and the run file's Step 0); millions of yen.
r = 0.04085                 # MOF jgbcme.csv, 30Y, 2026/10/9 (latest row in the file fetched 2026-10-13)
price = 5606.0              # Tokyo close 2026-10-13, Yahoo Finance chart API (aggregator, flagged)
issued = 215_115_038        # 62nd ASR and Q1 FY2026 Kessan Tanshin
treasury_jun = 2_354_657    # Q1 FY2026 Kessan Tanshin, June 30, 2026
bought_after = 5_999_100    # press releases 2026-09-04, 2026-10-02, 2026-10-09 (Aug 19 to Oct 8, 2026)
buyback_cash = 33_999.9217  # same releases, cumulative amount
shares = issued - treasury_jun - bought_after
borrow = 323_331 + 175_218  # bonds and borrowings, June 30, 2026 (Kessan Tanshin)
cash = 130_831
net_debt_filed = borrow - cash
net_debt = net_debt_filed + buyback_cash   # CONVENTION of this run: the share count already reflects the buyback
mcap = shares * price / 1e6
ev = mcap + net_debt
T = 0.306

# Bottom: all spending, literal window FY2021-25, acquisitions deducted (default pair), no growth
# (series changes sign, halves meaningless: specific (b), range is the no-growth case alone on this leg).
bottom_ae = (13118 + (-105024) + 21725 + 72038 + 100404) / 5      # from owner_cash.py, OC all-equity after acq
oc_eq_after_acq = {2021: -7856 - (-18920), 2022: -40918 - 68311, 2023: -1489 - (-15289), 2024: 76917 - 13719, 2025: 92305 - (-861)}
bottom_eq = sum(oc_eq_after_acq.values()) / 5

# Top: maintenance-only case, specific (e), depreciation as the proxy for required capex [M1998-127]:
# net income to the parent, equity-method share replaced by dividends received (Q4 convention), no working-capital
# growth at constant volume. The growth bought over the window was worth less than its cost (see run), so this
# no-growth maintenance case is the TOP and the all-spending case the BOTTOM.
ni = {2021: 75826, 2022: 70175, 2023: 93294, 2024: 81428, 2025: 73193}
eqm = {2021: 6224, 2022: -5537, 2023: 3442, 2024: 3239, 2025: 3576}
divr = {2021: 1479, 2022: 1148, 2023: 1328, 2024: 1672, 2025: 2577}
netint = {2021: (4729-1769), 2022: (8858-2799), 2023: (15012-3593), 2024: (18300-5562), 2025: (16036-5606)}
top_eq_y = {y: ni[y] - eqm[y] + divr[y] for y in ni}
top_ae_y = {y: top_eq_y[y] + netint[y]*(1-T) for y in ni}
top_eq = sum(top_eq_y.values()) / 5
top_ae = sum(top_ae_y.values()) / 5

def ps(v): return v / shares * 1e6
print(f"shares {shares:,}  mcap {mcap:,.0f}  net debt filed {net_debt_filed:,.0f}  +buyback {net_debt:,.0f}  EV {ev:,.0f}")
print("top all-equity by year", {y: round(v) for y, v in top_ae_y.items()})
print(f"bottom all-equity OC {bottom_ae:,.0f}; top {top_ae:,.0f}; width (EV basis) {top_ae/bottom_ae:.2f}x")
# value at the long government rate, no growth
for name, oc in (("bottom", bottom_ae), ("top", top_ae)):
    v = oc / r
    print(f"{name}: business value {v:,.0f}; less net debt {v-net_debt:,.0f}; per share {ps(v-net_debt):,.0f}; yield at price {oc/ev:.2%}")
# floor test at the price
print(f"floor test: top-case return at the price {top_ae/ev:.2%} vs about 10%")
# fair price: each end valued at ten percent, averaged (Part VII)
fb = ps(bottom_ae/0.10 - net_debt); ft = ps(top_ae/0.10 - net_debt)
print(f"fair all-equity: bottom end {fb:,.0f}, top end {ft:,.0f}, fair {((fb+ft)/2):,.0f}")
eb = ps(bottom_eq/0.10); et = ps(top_eq/0.10)
print(f"equity-only: bottom OC {bottom_eq:,.0f} -> {eb:,.0f}; top OC {top_eq:,.0f} -> {et:,.0f}; fair {((eb+et)/2):,.0f}")
# beside: ten-year all-equity after acquisitions (owner_cash.py) and organic pair
for name, oc in (("ten-year after acq", 9702), ("organic pair, literal window before acq", 29844)):
    print(f"beside, {name}: OC {oc:,} -> per share at gov rate {ps(oc/r-net_debt):,.0f}; at 10% {ps(oc/0.10-net_debt):,.0f}")
# net debt without the buyback added, for the record
print(f"fair all-equity with filed net debt only: {(ps(bottom_ae/0.10-net_debt_filed)+ps(top_ae/0.10-net_debt_filed))/2:,.0f}")
