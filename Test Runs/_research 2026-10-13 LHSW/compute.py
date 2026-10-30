# COMPUTATION, NOT A CLEARANCE. Figures from the filed statements (USD as reported; functional currency RMB).
# OCF and capital spending: FY2024-26 from 20-F FY2026 (0001213900-26-089090); FY2023 from 424B4 2025-04-04
# (0001213900-25-028729) [F-1 2024-05-10 (0001213900-24-041530) gave -1,478,638]; FY2022 from F-1 2024-05-10.
years = ["FY2022","FY2023","FY2024","FY2025","FY2026"]
ocf   = [239201, -1469694, -2075626, -1474574, -8966396]
sbc   = [0, 0, 0, 0, 1300181]
capex = [57618, 5257, 66745+5381, 4917+35011, 83006+8947]   # PP&E plus intangibles purchased
intpaid = [None, None, 57941, 100563, 128253]               # interest paid (supplemental), FY2024-26
rp_in_ocf = [370131, None, -(875797) + 239734 - 10350, -415590 + 800893 + 10695, -930035 - 177888 + 2548]  # related-party and shareholder advances run through OCF (sign as in OCF)
oc = [o - s - c for o, s, c in zip(ocf, sbc, capex)]
for y, v in zip(years, oc): print(f"{y} owner cash (OCF - stock pay - capital spending): {v:>12,.0f}")
avg5 = sum(oc)/5; print(f"five-year average: {avg5:,.0f}")
avg3 = sum(oc[2:])/3; print(f"literal three-year window FY2024-26 average: {avg3:,.0f}")
mid = sum(oc[1:4])/3; print(f"FY2023-25 average (both end years set aside): {mid:,.0f}")
# all-equity (before interest) for the three years with interest paid filed
oc_pre = [oc[i] + (intpaid[i] or 0) for i in range(5)]
print("owner cash before interest:", [f"{v:,.0f}" for v in oc_pre], f"avg {sum(oc_pre)/5:,.0f}")
# ex related-party flows
oc_ex = [oc[i] - (rp_in_ocf[i] or 0) for i in range(5)]
print("owner cash excluding related-party/shareholder advances in OCF:", [f"{v:,.0f}" for v in oc_ex], f"avg {sum(oc_ex)/5:,.0f}")
# Net debt at 2026-03-31 (20-F balance sheet)
borrow = 6319223 + 28994 + 10169 + 681357 + 34517
cash = 1885367
nd = borrow - cash
print(f"borrowings {borrow:,.0f}; cash {cash:,.0f}; net debt {nd:,.0f}")
nd_20f_events = nd - 334000 - 396000
nd_with_sept = nd_20f_events - 9221087
print(f"net debt after Apr and Jul placements (stated in the 20-F): {nd_20f_events:,.0f}; after Sept offering net (424B4 estimate): {nd_with_sept:,.0f}")
shares = 10906166 + 2587500
print(f"shares (Class A + Class B, 424B4 2026-09-03): {shares:,}")
sov = 0.0207; floor = 0.10
for label, base in [("five-year avg", avg5), ("FY2023-25 avg", mid), ("literal 3-yr", avg3)]:
    ev_sov = base / sov; ev_floor = base / floor
    print(f"{label}: no-growth value at sovereign 2.07% {ev_sov:,.0f}; at 10% {ev_floor:,.0f}")
    for ndl, ndv in [("20-F events", nd_20f_events), ("with Sept", nd_with_sept)]:
        print(f"   per share at sovereign ({ndl}) {(ev_sov - ndv)/shares:,.2f}; fair (10%) {(ev_floor - ndv)/shares:,.2f}")
# equity-only (after interest) fair price
for label, base in [("five-year avg", avg5)]:
    print(f"equity-only fair price at 10%: {base/floor/shares:,.2f} USD/share; RMB {base/floor/shares*6.7298:,.2f}")
price = 0.47
print(f"market cap at $0.47: {price*shares:,.0f}")
# the June 2026 Class B sale
for mkt in (1.00, 1.83):
    print(f"value transfer at {mkt}: {(mkt-0.165)*2400000:,.0f}")
# revenue path
rev = [949341, 13070586, 36598667, 36539846, 43269569]
ar  = [674159, 7591115, 13272976, 19144103, 14978869]
for y, r, a in zip(years, rev, ar): print(f"{y} revenue {r:,.0f}; receivables {a:,.0f}; receivables/revenue {a/r:.2f}")
