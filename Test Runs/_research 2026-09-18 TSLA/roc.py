# Return on capital employed, from the filed balance sheets and income statements ($M).
# capital employed = total equity incl. NCI and redeemable NCI + debt and finance leases - cash - short-term investments
import sys; sys.stdout.reconfigure(encoding="utf-8")
bs = {  # year: (stockholders equity, NCI, redeemable NCI, debt current, debt noncurrent, cash, ST inv, DTA)
 2021: (30189, 826, 568, 1589, 5245, 17576, 131, 0),        # FY2022 10-K comparative
 2022: (44704, 785, 409, 1502, 1597, 16253, 5932, 328),     # FY2023 10-K
 2023: (62634, 733, 242, 2373, 2857, 16398, 12696, 6733),   # FY2023 10-K
 2024: (72913, 704, 63, 2456, 5757, 16139, 20424, 6524),    # FY2025 10-K comparative
 2025: (82137, 670, 58, 1640, 6736, 16513, 27546, 6925),    # FY2025 10-K
}
opi = {2021: 6523, 2022: 13656, 2023: 8891, 2024: 7076, 2025: 4355}
cred = {2021: 1465, 2022: 1776, 2023: 1790, 2024: 2763, 2025: 1993}
ce = {y: e+n+r+d1+d2-c-s for y,(e,n,r,d1,d2,c,s,dta) in bs.items()}
ce_x = {y: ce[y]-bs[y][7] for y in bs}  # excluding the deferred tax asset created by the 2023 valuation-allowance release
print("year | capital employed | ex-DTA | op income | pre-tax ROCE (avg) | ex credits | ex-DTA ROCE")
for y in range(2022, 2026):
    a = (ce[y]+ce[y-1])/2; ax = (ce_x[y]+ce_x[y-1])/2
    print(y, ce[y], ce_x[y], opi[y], f"{100*opi[y]/a:.1f}%", f"{100*(opi[y]-cred[y])/a:.1f}%", f"{100*opi[y]/ax:.1f}%")
print(2021, ce[2021], "year-end only:", f"{100*opi[2021]/ce[2021]:.1f}%")
