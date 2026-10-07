"""Every computed number in the XOM run of 2026-10-06. Inputs are typed from the filed statements named beside each
row (USD millions); nothing here is a judgment.

Owner cash = OCF - stock pay (restricted stock compensation cost charged against income, Note "Incentive Program")
             - additions to PP&E - additional investments and advances (cash into equity companies)
             + other investing activities including collection of advances (cash back from them).
Variant A drops the last line (collections not credited)."""

# year: (OCF, SBC, PP&E additions, additional investments and advances, other investing incl. collection of advances, source)
CF = {
    2014: (45116, 831, 32952, 1631, 3346, '10-K FY2016 0000034088-17-000017'),
    2015: (30344, 855, 26490, 607, 842, '10-K FY2016 0000034088-17-000017'),
    2016: (22082, 880, 16163, 1417, 902, '10-K FY2016 0000034088-17-000017'),
    2017: (30066, 856, 15402, 5507, 2076, '10-K FY2019 0000034088-20-000016'),
    2018: (36014, 774, 19574, 1981, 986, '10-K FY2019 0000034088-20-000016'),
    2019: (29716, 741, 24361, 3905, 1490, '10-K FY2019 0000034088-20-000016'),
    2020: (14668, 672, 17282, 4857, 2681, '10-K FY2022 0000034088-23-000020'),
    2021: (48129, 612, 12076, 2817, 1482, '10-K FY2022 0000034088-23-000020'),
    2022: (76797, 648, 18407, 3090, 1508, '10-K FY2022 0000034088-23-000020'),
    2023: (55369, 600, 21919, 2995, 1562, '10-K FY2025 0000034088-26-000045'),
    2024: (55022, 800, 24306, 3299, 1926, '10-K FY2025 0000034088-26-000045'),
    2025: (51970, 1000, 28358, 4133, 3406, '10-K FY2025 0000034088-26-000045'),
}
H1_2026 = (32260, None, 12997, 711, 734, '10-Q Q2 2026 0000034088-26-000093')

print('year   OCF     SBC    PP&E   inv&adv  coll   owner cash   variant A (no collections)')
oc = {}
for y, (ocf, sbc, ppe, inv, coll, src) in CF.items():
    o = ocf - sbc - ppe - inv + coll
    a = ocf - sbc - ppe - inv
    oc[y] = (o, a)
    print(f'{y}  {ocf:6,} {sbc:6,} {ppe:6,} {inv:6,} {coll:6,}   {o:8,}   {a:8,}   {src}')
ocf, _, ppe, inv, coll, src = H1_2026
print(f'H1 2026 {ocf:,} SBC not in 10-Q {ppe:,} {inv:,} {coll:,}  owner cash before stock pay {ocf-ppe-inv+coll:,}  {src}')


def mean(ys, i=0):
    return sum(oc[y][i] for y in ys) / len(ys)


print('\nmeans of owner cash (variant A in brackets):')
for lo, hi in ((2021, 2025), (2016, 2025), (2014, 2025), (2017, 2025)):
    ys = range(lo, hi + 1)
    print(f'  {lo}-{hi}: {mean(ys):,.0f}  [{mean(ys, 1):,.0f}]')

PRICE, SHARES = 164.00, 4111.91196   # $ (aggregator, 2026-10-05); M shares (10-Q cover, 2026-06-30)
cap = PRICE * SHARES
print(f'\nmarket cap: {PRICE} x {SHARES:,.3f}M = ${cap:,.0f}M')
for lo, hi in ((2021, 2025), (2016, 2025)):
    m = mean(range(lo, hi + 1))
    print(f'  owner-cash yield on the {lo}-{hi} mean: {m / cap * 100:.2f}%')

# ROCE, corporate total, as each filer reports it (percent)
XOM_ROCE = {2014: 32984 / 203110 * 100, 2015: 7.9, 2016: 3.9, 2017: 9.0, 2018: 9.2, 2019: 6.5, 2020: -9.3,
            2021: 10.9, 2022: 24.9, 2023: 15.0, 2024: 12.7, 2025: 9.3}
CVX_ROCE = {2017: 5.0, 2018: 8.2, 2019: 2.0, 2020: -2.8, 2021: 9.4, 2022: 20.3, 2023: 11.9, 2024: 10.1, 2025: 6.6}
ys = range(2017, 2026)
print(f'\nXOM 2014 ROCE computed from the filed line (32,984 / 203,110): {XOM_ROCE[2014]:.1f}%')
print(f'ROCE mean 2017-2025: XOM {sum(XOM_ROCE[y] for y in ys)/9:.1f}%  CVX {sum(CVX_ROCE[y] for y in ys)/9:.1f}%')
print(f'ROCE mean 2014-2025 XOM: {sum(XOM_ROCE.values())/12:.1f}%')
print('years XOM ahead of CVX:', [y for y in ys if XOM_ROCE[y] > CVX_ROCE[y]])

# Average production (lifting) cost per oil-equivalent barrel, consolidated subsidiaries, $ (each filer's 10-K)
XOM_LIFT = {2020: 11.57, 2021: 12.15, 2022: 13.09, 2023: 12.05, 2024: 11.70, 2025: 11.29}
CVX_LIFT = {2020: 10.07, 2021: 9.90, 2022: 10.16, 2023: 10.23, 2024: 9.23, 2025: 9.71}
for y in XOM_LIFT:
    print(f'lifting cost {y}: XOM {XOM_LIFT[y]:.2f}  CVX {CVX_LIFT[y]:.2f}  XOM higher by {XOM_LIFT[y]/CVX_LIFT[y]*100-100:.0f}%')
print(f'mean 2020-2025: XOM {sum(XOM_LIFT.values())/6:.2f}  CVX {sum(CVX_LIFT.values())/6:.2f}')

# The 2020 trough: cash in against cash out (10-K FY2022)
ocf20, capex20, inv20, div20, buy20 = 14668, 17282, 4857, 14865, 405
print(f'\n2020: OCF {ocf20:,} less PP&E {capex20:,} less inv&adv {inv20:,} less dividends {div20:,} = '
      f'{ocf20-capex20-inv20-div20:,}')
print(f'total debt 2019 -> 2020: notes {20578:,}+LTD {26342:,} = {20578+26342:,} -> {20458:,}+{47182:,} = {20458+47182:,}')
