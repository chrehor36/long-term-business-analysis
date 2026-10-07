# owner earnings from the filed cash-flow faces, $M. Sources: FY2019 10-K (2017-19), FY2021 10-K (2019-21 OCF/SBC/D&A),
# FY2023 10-K (2021-23; capex shown net of 'Proceeds relating to property and equipment' to match the FY2025 face), FY2025 10-K (2023-25), Q2 2026 10-Q (H1).
Y = {
 2017: dict(ocf=24216, sbc=3723, da=3025, capex=6733, fl=0, acq=122),
 2018: dict(ocf=29274, sbc=4152, da=4315, capex=13915, fl=0, acq=137),
 2019: dict(ocf=36314, sbc=4836, da=5741, capex=15102, fl=552, acq=508),
 2020: dict(ocf=38747, sbc=6536, da=6862, capex=15115, fl=604, acq=388),
 2021: dict(ocf=57683, sbc=9164, da=7967, capex=18690-123, fl=677, acq=851),
 2022: dict(ocf=50475, sbc=11992, da=8686, capex=31431-245, fl=850, acq=1312),
 2023: dict(ocf=71113, sbc=14027, da=11178, capex=27045, fl=1058, acq=629),
 2024: dict(ocf=91328, sbc=16690, da=15498, capex=37256, fl=1969, acq=270),
 2025: dict(ocf=115800, sbc=20427, da=18616, capex=69691, fl=2524, acq=4231),
}
H1_25 = dict(ocf=49587, sbc=8981, da=8242, capex=29479, fl=1225, acq=62)
H1_26 = dict(ocf=64088, sbc=13690, da=12355, capex=49113, fl=1805, acq=474)
TTM = {k: Y[2025][k] - H1_25[k] + H1_26[k] for k in H1_26}
def oe(d):
    da_end = d["ocf"] - d["sbc"] - d["da"]
    cx_end = d["ocf"] - d["sbc"] - d["capex"] - d["fl"]
    return da_end, cx_end, cx_end - d["acq"]
print("FY | OCF | SBC | D&A | capex | FL principal | acq | OE D&A end | OE capex end | capex end + acq | capex+FL / D&A | SBC/OCF")
for y, d in list(Y.items()) + [("TTM 2026-06", TTM)]:
    a, b, c = oe(d)
    print(y, d["ocf"], d["sbc"], d["da"], d["capex"], d["fl"], d["acq"], a, b, c, round((d["capex"]+d["fl"])/d["da"], 2), f"{d['sbc']/d['ocf']*100:.1f}%")
def win(ys):
    n = len(ys); r = [oe(Y[y]) for y in ys]
    return tuple(round(sum(x[i] for x in r)/n) for i in range(3))
cap = 665.75 * 2547506225 / 1e6
for name, ys in [("5y FY2021-25", range(2021, 2026)), ("3y FY2023-25", range(2023, 2026)), ("9y FY2017-25", range(2017, 2026)), ("pre-build FY2017-21", range(2017, 2022))]:
    w = win(list(ys)); print(name, w, [f"{x/cap*100:.2f}%" for x in w])
t = oe(TTM); print("TTM", t, [f"{x/cap*100:.2f}%" for x in t])
print("cap $M", round(cap))
# working capital lines FY2025 (face): AR, prepaid, other assets, AP, accrued, other liabilities
wc25 = [-1815, -89, -481, -14, 1077, 437]; print("FY2025 WC lines sum", sum(wc25))
wc_h126 = [-2273, -3230, -2535, -354, 5662, -4528]; print("H1 2026 WC lines sum", sum(wc_h126))
# floor arithmetic
print("OE needed for 10% pre-tax on cap ($bn):", round(cap*0.10/1000,1))
