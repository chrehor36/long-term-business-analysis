"""Owner cash after every real cost, SHW, USD millions, from the filed cash-flow statements
(2023-2025: 10-K FY2025 0000089800-26-000008; 2020-2022: 10-K FY2022 0000089800-23-000007;
2016-2019: companyfacts first-filed vintage, accessions in run_py_output.txt).
owner cash = OCF - stock pay - all capital expenditures - amortization of non-traded (tax-credit) investments.
The last term is the cost of the tax credits whose benefit sits inside OCF while the contributions sit outside it;
filed from 2020 only (FY2022 10-K line 'Amortization of non-traded investments'); earlier years carry no deduction."""

rows = {
    # FY: (OCF, SBC, capex, depreciation (not amortization of acquired intangibles), NTI amortization or None, acquisitions net)
    2016: (1308.6, 72.1, 239.0, 172.1, None, None),
    2017: (1884.0, 90.3, 222.8, 285.0, None, None),
    2018: (1943.7, 82.6, 251.0, 278.2, None, None),
    2019: (2321.3, 101.7, 328.9, 262.1, None, None),
    2020: (3408.6, 95.9, 303.8, 268.0, 84.8, None),
    2021: (2244.6, 97.7, 372.0, 263.1, 53.6, None),
    2022: (1919.9, 99.7, 644.5, 264.0, 38.5, None),
    2023: (3521.9, 115.9, 888.4, 292.3, 65.4, 264.7),
    2024: (3153.2, 138.1, 1070.0, 297.4, 75.0, 78.9),
    2025: (3451.6, 123.5, 797.6, 340.3, 104.0, 1211.3),
}

print(f"{'FY':>4} {'OCF':>8} {'SBC':>6} {'capex':>7} {'NTI':>6} {'owner cash':>11} {'dep var':>8}")
oc = {}
for y, (ocf, sbc, cx, da, nti, acq) in rows.items():
    n = nti or 0.0
    oc[y] = ocf - sbc - cx - n
    dav = ocf - sbc - da - n
    print(f"{y:>4} {ocf:>8.1f} {sbc:>6.1f} {cx:>7.1f} {n:>6.1f} {oc[y]:>11.1f} {dav:>8.1f}")

w = [2021, 2022, 2023, 2024, 2025]
m5 = sum(oc[y] for y in w) / 5
print(f"five-year mean 2021-2025 owner cash: {m5:.1f}")
w10 = list(range(2016, 2026))
print(f"ten-year mean 2016-2025 owner cash: {sum(oc[y] for y in w10)/10:.1f}")
# growth on aggregate owner cash, smoothed: three-year means at each end
a = sum(oc[y] for y in (2016, 2017, 2018)) / 3
b = sum(oc[y] for y in (2023, 2024, 2025)) / 3
print(f"3yr mean 2016-18 {a:.1f}  3yr mean 2023-25 {b:.1f}  CAGR over 7 yrs {((b/a)**(1/7)-1)*100:.2f}%")
print(f"point 2021->2025 CAGR {((oc[2025]/oc[2021])**0.25-1)*100:.2f}%")
print(f"point 2016->2025 CAGR {((oc[2025]/oc[2016])**(1/9)-1)*100:.2f}%")
print(f"point 2018->2025 CAGR (first full post-Valspar year) {((oc[2025]/oc[2018])**(1/7)-1)*100:.2f}%")
c = sum(oc[y] for y in (2018, 2019, 2020)) / 3
print(f"3yr mean 2018-20 {c:.1f} -> 2023-25 {b:.1f}: CAGR over 5 yrs {((b/c)**(1/5)-1)*100:.2f}%")
p5 = sum(oc[y] for y in range(2016, 2021)) / 5
print(f"five-year mean 2016-2020 {p5:.1f} -> 2021-2025 {m5:.1f}: CAGR over 5 yrs {((m5/p5)**(1/5)-1)*100:.2f}%")
dv = {y: rows[y][0]-rows[y][1]-rows[y][3]-(rows[y][4] or 0) for y in rows}
print(f"depreciation variant five-year mean 2021-2025: {sum(dv[y] for y in w)/5:.1f}")
print(f"depreciation variant point 2018->2025 CAGR {((dv[2025]/dv[2018])**(1/7)-1)*100:.2f}%")
