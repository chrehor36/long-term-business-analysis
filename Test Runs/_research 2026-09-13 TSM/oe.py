"""TSMC owner earnings, NT$ millions. Arithmetic only; every judgment is in the run file.
Inputs typed from the audited cash-flow statements of the 20-Fs FY2017 (0001193125-18-121866), FY2020
(0001193125-21-118512), FY2023 (0001193125-24-099840), FY2025 (0001628280-26-025362); OCF, capex, D&A for
FY2015-FY2024 also agree with companyfacts (series_out.json). H1 figures from the Q2 2026 consolidated report
(6-K 0001046179-26-000541), NT$ thousands converted.

CONVENTION (framework VI): OE = OCF - SBC(equity-settled add-back) - (c).
Run-specific adjustment, disclosed: minus the change in customer 'temporary receipts' (capacity-reservation
prepayments, refundable or offset against receivables; Note 22), because that cash is a customer advance, not
earnings.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
Y = list(range(2015, 2026))
ocf = dict(zip(Y, [529879.4, 539834.6, 585318.2, 573954.3, 615138.7, 822666.2, 1112160.7, 1610599.2, 1241967.3, 1826177.1, 2274975.6]))
capex = dict(zip(Y, [257516.8, 328045.3, 330588.2, 315581.9, 460422.2, 507238.7, 839195.7, 1082672.1, 949816.8, 956006.5, 1272410.5]))
intang = dict(zip(Y, [4283.9, 4243.1, 4480.6, 7100.3, 9329.9, 9542.4, 9040.7, 6954.3, 5518.4, 8875.7, 10146.9]))
dep = dict(zip(Y, [219303.4, 220085.0, 255796.0, 288124.9, 281411.8, 324538.4, 414187.7, 428498.2, 522932.7, 653610.5, 679684.0]))
amort = dict(zip(Y, [3202.2, 3743.4, 4346.7, 4421.4, 5472.4, 7186.2, 8207.2, 8756.1, 9258.2, 9186.1, 8412.4]))
sbc = dict(zip(Y, [0.0, 0.0, 0.0, 0.0, 2.8, 6.6, 7.8, 302.4, 483.0, 1242.7, 1246.1]))
grants = dict(zip(Y, [0.0, 738.6 + 798.5, 2629.8 + 1.8, 0.0, 2565.3 + 850.6, 1044.3 + 25.4, 821.3 + 6.6, 7046.1 + 5.3, 47544.7 + 1.2, 75164.0 + 0.3, 76258.8]))
int_rec = dict(zip(Y, [3641.9, 6353.2, 9526.3, 14660.4, 16875.0, 9775.1, 5990.9, 18083.7, 55887.2, 76434.1, 98954.7]))
int_paid = dict(zip(Y, [3156.2, 3302.4, 3482.7, 3233.4, 3597.1, 1781.1, 3833.6, 12218.6, 17359.0, 18751.2, 19128.8]))
temp_bal = {2014: 0.0, 2015: 0.0, 2016: 0.0, 2017: 0.0, 2018: 0.0, 2019: 0.0, 2020: 0.0, 2021: 185994.2, 2022: 276122.8, 2023: 278294.6, 2024: 291101.8, 2025: 189858.2}
rev = dict(zip(Y, [843497.4, 947938.3, 977447.2, 1031473.6, 1069985.4, 1339254.8, 1587415.0, 2263891.3, 2161735.8, 2894307.7, 3809054.3]))
TAX = 0.17  # 2025 income tax expense / pretax = 346,529.8 / 2,041,654.7; used only for the after-tax interest line

# TTM to 2026-06-30 = FY2025 + H1 2026 - H1 2025 (NT$ millions)
ttm = dict(ocf=2274975.6 + 1482341.2 - 1122637.8, capex=1272410.5 + 846764.7 - 628052.5,
           intang=10146.9 + 3876.4 - 4616.4, da=688096.4 + (359541.5 + 4447.1) - (359012.2 + 4184.8),
           sbc=1246.1 + 237.0 - 799.6, grants=76258.8 + 590.4 - 67128.2, dtemp=234225.1 - 221915.3,
           int_net=(98954.7 + 52546.1 - 50443.7) - (19128.8 + 9889.4 - 9738.7))

# The maintenance judgment's second end: capex/D&A in the flattest revenue years on file (2017-2019:
# revenue +3.1%, +5.5%, +3.7%). A disclosed guess [E2-23], not a computed truth.
flat = [2017, 2018, 2019]
flat_ratio = sum(capex[y] + intang[y] - grants[y] for y in flat) / sum(dep[y] + amort[y] for y in flat)

rows = {}
for y in Y[1:]:
    da = dep[y] + amort[y]
    net_capex = capex[y] + intang[y] - grants[y]
    dtemp = temp_bal[y] - temp_bal[y - 1]
    base = ocf[y] - sbc[y] - dtemp
    rows[y] = dict(ocf=ocf[y], sbc=sbc[y], dtemp=dtemp, base=base, da=da, net_capex=net_capex,
                   oe_capex=base - net_capex, oe_judged=base - flat_ratio * da, oe_da_INVALID=base - da,
                   int_net_after_tax=(int_rec[y] - int_paid[y]) * (1 - TAX), capex_da=net_capex / da,
                   capex_rev=net_capex / rev[y])
base_t = ttm["ocf"] - ttm["sbc"] - ttm["dtemp"]
net_capex_t = ttm["capex"] + ttm["intang"] - ttm["grants"]
rows["TTM 2026-06"] = dict(ocf=ttm["ocf"], sbc=ttm["sbc"], dtemp=ttm["dtemp"], base=base_t, da=ttm["da"],
                           net_capex=net_capex_t, oe_capex=base_t - net_capex_t, oe_judged=base_t - flat_ratio * ttm["da"],
                           oe_da_INVALID=base_t - ttm["da"], int_net_after_tax=ttm["int_net"] * (1 - TAX),
                           capex_da=net_capex_t / ttm["da"], capex_rev=None)


def mean(keys, field):
    return sum(rows[k][field] for k in keys) / len(keys)

windows = {"10-yr 2016-2025": list(range(2016, 2026)), "5-yr 2021-2025": list(range(2021, 2026)),
           "3-yr 2023-2025": [2023, 2024, 2025], "5-yr prior 2016-2020": list(range(2016, 2021))}
print(f"flat-year capex/D&A ratio (2017-2019) = {flat_ratio:.3f}")
print("year        OCF      SBC   dTemp      base      D&A   netCapex  OE(capex)  OE(judged)  OE(D&A,INVALID)  netInt*  capex/DA")
for k, r in rows.items():
    print(f"{str(k):11s} {r['ocf']:>9,.0f} {r['sbc']:>6,.0f} {r['dtemp']:>8,.0f} {r['base']:>9,.0f} {r['da']:>8,.0f} {r['net_capex']:>9,.0f} {r['oe_capex']:>10,.0f} {r['oe_judged']:>10,.0f} {r['oe_da_INVALID']:>12,.0f} {r['int_net_after_tax']:>9,.0f} {r['capex_da']:>6.2f}")
res = {"flat_ratio": flat_ratio, "rows": {str(k): v for k, v in rows.items()}, "windows": {}}
for w, ks in windows.items():
    res["windows"][w] = {f: mean(ks, f) for f in ("oe_capex", "oe_judged", "oe_da_INVALID", "int_net_after_tax", "base", "net_capex", "da")}
    m = res["windows"][w]
    print(f"{w:22s} OE capex-end {m['oe_capex']:>10,.0f}  judged-end {m['oe_judged']:>10,.0f}  D&A-end(INVALID) {m['oe_da_INVALID']:>10,.0f}  +net interest a.t. {m['int_net_after_tax']:>8,.0f}")
json.dump(res, open(os.path.join(HERE, "oe_out.json"), "w"), indent=1)
