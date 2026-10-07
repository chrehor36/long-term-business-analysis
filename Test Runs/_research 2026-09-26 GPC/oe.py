"""GPC owner earnings the corpus's way [E2-23]: operating cash as filed - SBC - (c), every window, both (c) ends.
Each year read from the 10-K presenting it as its current year (first filed); 2007 and 2008 from the 2009 10-K's
prior-year columns (the 2007 and 2008 10-Ks carry the statements in an exhibit). 2020-2022 operating cash is the
filer's "from continuing operations" line (Business Products sold 2020-06-30); 2006-2019 include the businesses since sold.
Columns ($M): ocf, sbc, capex, disposal proceeds, D&A, acquired-intangible amortisation, acquisitions line, cash interest.
"""
Y = {
2006: (433.500, 11.948, 126.044, 4.452, 73.423, 0.463, 29.007, 32.521),
2007: (641.471, 14.300, 115.648, 67.656, 87.702, 1.118, 44.855, 31.540),
2008: (530.309, 12.977, 105.026, 11.721, 88.698, 2.861, 133.604, 31.297),
2009: (845.298, 8.578, 69.445, 12.042, 90.411, 3.644, 134.203, 27.626),
2010: (678.663, 7.016, 85.379, 3.676, 89.332, 4.737, 90.645, 28.061),
2011: (624.927, 7.547, 103.469, 8.908, 88.936, 6.774, 136.936, 27.640),
2012: (906.438, 10.747, 101.987, 8.504, 98.383, 12.991, 558.384, 20.416),
2013: (1056.731, 12.648, 124.063, 10.657, 133.957, 28.987, 712.173, 27.221),
2014: (790.145, 16.239, 107.681, 8.866, 148.313, 36.867, 287.900, 25.155),
2015: (1159.373, 17.717, 109.544, 8.618, 141.675, 34.878, 162.701, 23.687),
2016: (946.078, 19.719, 160.643, 28.811, 147.487, 40.9, 462.167, 19.043),
2017: (815.043, 16.892, 156.760, 21.275, 167.691, 51.993, 1494.795, 38.401),
2018: (1145.164, 20.716, 232.422, 14.665, 241.635, 88.972, 278.367, 102.131),
2019: (892.010, 32.050, 297.869, 24.772, 270.288, 97.459, 724.718, 95.281),
2020: (2014.522, 22.621, 153.502, 18.064, 272.842, 94.962, 69.173, 91.344),
2021: (1258.285, 25.597, 266.136, 26.549, 290.971, 103.273, 284.315, 65.732),
2022: (1466.971, 38.058, 339.632, 145.007, 347.819, 157.437, 1690.208, 73.368),
2023: (1435.610, 57.226, 512.675, 25.099, 350.529, 147.178, 306.881, 90.405),
2024: (1251.251, 40.693, 567.339, 122.432, 407.978, 142.994, 1080.238, 124.977),
2025: (890.762, 48.847, 469.838, 52.293, 538.023 - 42.021, 152.431, 318.291, 191.334),
}
# receivables sold under the A/R Sales Agreement, outstanding at year end ($M), from the 10-K notes; the increase is financing inside operating cash
ARS = {2019: 0, 2020: 800, 2021: 800, 2022: 1000, 2023: 1000, 2024: 1000, 2025: 1000}
CAP = 17867.5
SOV = 0.0549

def yr(y):
    ocf, sbc, cx, dp, da, am, acq, ip = Y[y]
    net = cx - dp
    dep = da - am
    ars = ARS.get(y, 0) - ARS.get(y - 1, 0)
    return dict(ocf=ocf, sbc=sbc, net=net, dep=dep, capend=ocf - sbc - net, daend=ocf - sbc - dep,
                acq=acq, ars=ars, ip=ip, gross=ocf - sbc - cx, daraw=ocf - sbc - Y[y][4] - (42.021 if y == 2025 else 0))

if __name__ == '__main__':
    print('year | OCF | SBC | net capex | depreciation (D&A - acq. amortisation) | OE capex end | OE D&A end | acquisitions | A/R-sale increase | net capex/dep')
    for y in sorted(Y):
        r = yr(y)
        print(f"{y} | {r['ocf']:,.1f} | {r['sbc']:,.1f} | {r['net']:,.1f} | {r['dep']:,.1f} | {r['capend']:,.1f} | {r['daend']:,.1f} | {r['acq']:,.1f} | {r['ars']:,.0f} | {r['net']/r['dep']:.2f}")
    print()
    print('window | capex end | D&A end | yield capex | yield D&A | incl. acquisitions (capex end) | A/R-sale stripped capex end | A/R-sale stripped D&A end | net capex/dep')
    lo, hi = 1e9, -1e9; lo2, hi2 = 1e9, -1e9
    for n in range(3, 21):
        ys = list(range(2026 - n, 2026))
        R = [yr(y) for y in ys]
        m = lambda k: sum(r[k] for r in R) / n
        ce, de = m('capend'), m('daend')
        acq = ce - m('acq')
        s_ce, s_de = ce - m('ars'), de - m('ars')
        lo, hi = min(lo, ce, de), max(hi, ce, de)
        lo2, hi2 = min(lo2, s_ce, s_de), max(hi2, s_ce, s_de)
        print(f"{n}y {ys[0]}-{str(ys[-1])[2:]} | ${ce:,.1f}M | ${de:,.1f}M | {ce/CAP*100:.2f}% | {de/CAP*100:.2f}% | ${acq:,.1f}M | ${s_ce:,.1f}M | ${s_de:,.1f}M | {m('net')/m('dep'):.2f}")
    print(f'\nRANGE every window both ends: ${lo:,.1f}M to ${hi:,.1f}M ({lo/CAP*100:.2f}% to {hi/CAP*100:.2f}%)')
    print(f'RANGE, A/R-sale increments stripped: ${lo2:,.1f}M to ${hi2:,.1f}M ({lo2/CAP*100:.2f}% to {hi2/CAP*100:.2f}%)')
    # screen reproduction
    exp = {2021: 25.6, 2022: 38.0, 2023: 57.0, 2024: 44.0, 2025: 47.0}  # AllocatedShareBasedCompensationExpense tag
    b = sum(Y[y][0] - exp[y] - Y[y][2] for y in (2023, 2024, 2025)) / 3
    t = sum(Y[y][0] - exp[y] - (Y[y][4] + (42.021 if y == 2025 else 0)) for y in range(2021, 2026)) / 5
    print(f'screen reproduction: 3y gross-capex end with the expense tag ${b:,.1f}M; 5y D&A end, amortisation and accelerated depreciation left in ${t:,.1f}M')
    # coverage [E2-54]: (OCF + cash interest - net capex) / cash interest
    for y in (2006, 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024, 2025):
        r = yr(y); print(y, 'coverage %.1fx' % ((r['ocf'] + r['ip'] - r['net']) / r['ip']), 'with acquisitions %.1fx' % ((r['ocf'] + r['ip'] - r['net'] - r['acq']) / r['ip']))
