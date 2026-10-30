"""CHFFF run: Q7 COMPUTATION, NOT A CLEARANCE (the file closed OUT at Q2). HK$'000 unless stated.
Filed figures only; every input below was checked against the filing named beside it (second analyst, 2026-10-29).
Run: python -I calc_q7.py"""
price = 4.735                      # HK$, 00257 close 2026-10-28, aggregator (Yahoo), flagged
shares = 6142975292                # Monthly Return, September 2026 (HKEXnews 2026100202491)
sov = 0.0205                       # MOF China Government Bond curve, 30 years, 2026-10-28
floor = 0.10                       # Q7 floor CONVENTION, about ten percent
mcap = price * shares / 1000

# owner cash by year, all-equity basis: net cash from operating activities (after tax paid; interest paid is in
# financing; the concession construction spending runs through operating cash as the change in contract assets)
# less PP&E additions, intangible (operating-right) additions and acquisitions net of cash acquired; from
# data_10y.csv via calc_returns.py. Equity basis: less interest paid, lease interest and perpetual distributions.
ae = {2021: -12007359, 2022: -1851781, 2023: -1350632, 2024: 4415847, 2025: 10277204}
eq = {2021: -15050781, 2022: -5332964, 2023: -4936983, 2024: 1221710, 2025: 7678751}
avg_ae, avg_eq = sum(ae.values()) / 5, sum(eq.values()) / 5

# claims at 30 June 2026 (Interim Report 2026, condensed statement of financial position) plus the interim dividend
# the same report declares, paid on or around 20 October 2026
borrow = 31012942 + 59501316                   # interest-bearing borrowings, current + non-current
cash = 9705127 + 178356 + 34763                # cash and equivalents + pledged deposits + deposits over 3 months
interim_div = 0.16 * shares / 1000             # HK16.0 cents a share
net_debt = borrow - cash + interim_div
perps = 7824893                                # perpetual capital instruments (CONVENTION of this run: a claim ahead of the shares)
nci = 13316645                                 # non-controlling interests at book (CONVENTION of this run)
claims = net_debt + perps + nci
ev = mcap + claims
nci_share = 597786 / (3925162 + 597786)        # NCI share of 2025 profit after the perpetual holders (AR2025 P&L)

def ps(x):  # HK$ a share
    return x * 1000 / shares

cases = {
    "A. literal window 2021-25, all spending (central by the text)": (avg_ae, avg_eq),
    "B. 2025 alone less the HK$1,564,593k subsidy receivables sold to a trust (AR2025 note 45), beside": (ae[2025] - 1564593, eq[2025] - 1564593),
    "C. 2024-25 operating years average, beside": ((ae[2024] + ae[2025]) / 2, (eq[2024] + eq[2025]) / 2),
}
# D. maintenance guess (specific (e)), beside: earnings before interest after the company's tax, 2025, treating the
# recovery of the concession assets as the maintenance charge (each concession is handed back for nothing, AR2025 note 48(b)):
# profit before tax 5,650,911 + finance costs 2,393,735, less income tax 946,316 and less the tax shield on the
# finance costs at the 25% PRC statutory rate (CONVENTION of this run: the tax the business would pay unlevered)
ebit = 5650911 + 2393735
maint_ae = ebit - 946316 - 0.25 * 2393735
maint_eq = 4704595 - 206485                     # profit for the year less perpetual distributions paid
cases["D. maintenance guess, 2025 earnings before interest after tax, beside"] = (maint_ae, maint_eq)

print(f"market cap HK$m {mcap/1e3:,.0f}; borrowings {borrow/1e3:,.0f}; cash {cash/1e3:,.0f}; interim dividend {interim_div/1e3:,.0f}")
print(f"net debt HK$m {net_debt/1e3:,.0f}; perps {perps/1e3:,.0f}; NCI at book {nci/1e3:,.0f}; claims {claims/1e3:,.0f}; EV at price {ev/1e3:,.0f}")
print(f"owner cash needed for 10% on EV at the price: HK$m {ev*floor/1e3:,.0f}; on market cap alone (equity-only): {mcap*floor/1e3:,.0f}")
print("halves: 2021-22 avg", round((ae[2021]+ae[2022])/2/1e3), " 2024-25 avg", round((ae[2024]+ae[2025])/2/1e3),
      "-> the series and the halves change sign: growth meaningless, no-growth case alone (specific (b))")
for k, (a, e) in cases.items():
    print("---", k)
    print(f"  owner cash HK$m all-equity {a/1e3:,.0f}; equity basis {e/1e3:,.0f}")
    print(f"  return at the price: all-equity {a/ev*100:.1f}% (NCI and perps not counted as claims: {a/(mcap+net_debt)*100:.1f}%);"
          f" equity-only, attributable share {e*(1-nci_share)/mcap*100:.1f}%")
    print(f"  value at the sovereign, no growth, all-equity a share: HK${ps(a/sov - claims):,.2f}")
    print(f"  valued at the floor (10%): all-equity a share HK${ps(a/floor - claims):,.2f}; equity-only a share HK${ps(e*(1-nci_share)/floor):,.2f}")
print(f"FAIR PRICE (case A, no-growth case alone, so both ends are the same case): all-equity HK${ps(avg_ae/floor - claims):,.2f}"
      f" (central); equity-only HK${ps(avg_eq*(1-nci_share)/floor):,.2f} (beside)")
print(f"VALUE RANGE (case A at the sovereign, no-growth alone): HK${ps(avg_ae/sov - claims):,.2f} a share, all-equity")
