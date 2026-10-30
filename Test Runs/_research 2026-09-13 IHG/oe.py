"""IHG owner earnings - ARITHMETIC ONLY on figures transcribed from the 20-Fs (latest vintage for each year).
Every input line carries its source. The judgments ((c) ends, what is stripped as System Fund) are named in the run file,
not decided here. US$ millions."""
import json

Y = list(range(2017, 2026))
D = {
    # Net cash from operating activities (after interest and tax; key money INSIDE). FY2019 20-F (2017-2019, IFRS 15/16 restated),
    # FY2022 20-F (2020-2022), FY2025 20-F (2023-2025); cross-checked to companyfacts ifrs-full CashFlowsFromUsedInOperatingActivities.
    "ncfo":      [616, 709, 653, 137, 636, 646, 893, 724, 898],
    # Contract acquisition costs (key money), net of repayments, deducted INSIDE cash flow from operations (Note 25/26 each year)
    "keymoney":  [57, 54, 61, 64, 42, 64, 101, 237, 179],
    # Principal element of lease payments (financing section; IFRS 16 restated back to 2017 in the FY2019 free cash flow table)
    "lease":     [25, 35, 59, 65, 32, 36, 28, 46, 30],
    # Share-based payments cost, operating (reportable segments) - Note 25; 2017-2018 only a combined figure exists
    "sbc_op":    [27, 38, 30, 21, 28, 30, 36, 44, 47],
    # Share-based payments cost charged to the System Fund - Note 25 "System Fund adjustments"; 2017-2018 not separately stated (0 here, total above)
    "sbc_sf":    [0, 0, 12, 11, 13, 16, 20, 23, 25],
    # Capital expenditure: gross maintenance, EXCLUDING key money (FY2019 FCF recon 2017-2019; FY2021 2020-2021; FY2023 2022-2023; FY2025 2024-2025)
    "maint":     [72, 60, 86, 43, 33, 44, 38, 31, 31],
    # Depreciation and amortisation excluding System Fund (Note 25 operating adjustments)
    "da":        [112, 115, 116, 110, 98, 68, 67, 65, 67],
    # Contract assets deduction in revenue (the amortisation of key money), Note 25
    "ca_ded":    [17, 19, 21, 25, 35, 32, 37, 43, 52],
    # System Fund (and reimbursable) result, as reported (FY2018 20-F 2017-2018; FY2021 2019-2021; FY2023 2022; FY2025 2023-2025)
    "sf_result": [-34, -146, -49, -102, -11, -105, 19, -83, -46],
    # System Fund non-cash adjustments INCLUDING its SBC (Note 25); 2017-2018 = System Fund D&A only (FY2019 recon: 41, 49), flagged
    "sf_noncash":[41, 49, 106, 159, 100, 110, 106, 117, 125],
    # Capital expenditure: gross System Fund capital investments (FY2018 20-F 2017-2018; FY2021 2019-2021; FY2023 2022-2023; FY2025 2024-2025)
    "sf_capex":  [142, 99, 98, 35, 19, 35, 46, 45, 43],
    # Increase in deferred revenue (working capital line inside cash flow from operations, Note 25) - loyalty points and co-brand upfronts
    "d_defrev":  [43, 141, 57, 1, 39, 108, 123, 214, 107],
    # Display only: recyclable investments and acquisitions (investing section)
    "recyclable":[85, 38, 19, 6, 5, 15, 50, 68, 16],
    "acquis":    [0, 38, 292, 0, 0, 0, 0, 0, 120],
}
for k, v in D.items():
    assert len(v) == len(Y), k

rows = {}
for i, y in enumerate(Y):
    g = {k: D[k][i] for k in D}
    sbc = g["sbc_op"] + g["sbc_sf"]
    sf_ops_ex_sbc = g["sf_result"] + g["sf_noncash"] - g["sbc_sf"]     # the fund's operating cash, excluding the cash that reimburses its share awards
    base = g["ncfo"] - g["lease"] - sbc                                 # key money already deducted inside ncfo
    r = {}
    # CONSOLIDATED (System Fund left in; its capex charged because IHG pays it out of consolidated cash)
    r["cons_km_maint"]  = base - g["maint"] - g["sf_capex"]                          # (c) = maintenance + all key money
    r["cons_km_growth"] = base + g["keymoney"] - g["maint"] - g["sf_capex"]          # (c) = maintenance only, key money treated as growth
    # FEE BUSINESS, SYSTEM FUND SEPARATED: remove the fund's operating cash and its deferred-revenue float; fund capex not charged
    sep = base - sf_ops_ex_sbc - g["d_defrev"]
    r["sep_km_maint"]   = sep - g["maint"]
    r["sep_km_growth"]  = sep + g["keymoney"] - g["maint"]
    r["sep_da_default"] = sep + g["keymoney"] - g["da"] - g["ca_ded"]               # [E3-44] default: D&A plus key-money amortisation
    r["sf_total_cash"]  = sf_ops_ex_sbc - g["sf_capex"] + g["d_defrev"]
    r["sbc_total"] = sbc
    rows[y] = r

windows = {
    "9y 2017-2025 (all)": list(range(2017, 2026)),
    "7y 2019-2025 (fund lines fully stated)": list(range(2019, 2026)),
    "5y 2021-2025 (DEFAULT [E2-42], includes 2021)": list(range(2021, 2026)),
    "4y 2022-2025 (ex 2020-21)": list(range(2022, 2026)),
    "3y 2023-2025": list(range(2023, 2026)),
    "7y ex-trough 2017-19 + 2022-25": [2017, 2018, 2019, 2022, 2023, 2024, 2025],
    "5y 2019-2023 (includes 2020 and 2021)": list(range(2019, 2024)),
    "6y 2020-2025 (includes 2020)": list(range(2020, 2026)),
}
keys = ["cons_km_maint", "cons_km_growth", "sep_km_maint", "sep_km_growth", "sep_da_default", "sf_total_cash"]
out = {"by_year": rows, "windows": {}}
CAP = 22613.0
print("year " + " ".join(f"{k:>15}" for k in keys))
for y in Y:
    print(y, " ".join(f"{rows[y][k]:>15.0f}" for k in keys))
for w, ys in windows.items():
    m = {k: sum(rows[y][k] for y in ys) / len(ys) for k in keys}
    m["yield_sep_lo_%"] = round(100 * m["sep_km_maint"] / CAP, 2)
    m["yield_sep_hi_%"] = round(100 * m["sep_km_growth"] / CAP, 2)
    m["yield_cons_hi_%"] = round(100 * m["cons_km_growth"] / CAP, 2)
    out["windows"][w] = {k: round(v, 1) for k, v in m.items()}
    print(f"{w:48}", " ".join(f"{m[k]:>8.0f}" for k in keys), m["yield_sep_lo_%"], m["yield_sep_hi_%"], m["yield_cons_hi_%"])
json.dump(out, open("oe_out.json", "w"), indent=1)
