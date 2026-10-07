"""Toyota owner earnings, industrial (Non-Financial Services) perimeter. ¥ millions.
Arithmetic only (operator rule 8). Every input is transcribed from the filed two-way cash-flow
statements (IFRS FY2020-FY2026; US GAAP FY2017-FY2019) and notes; sources in the run file."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

# year: (basis, OCF, add_fixed, add_leased, add_intang, proc_fixed, proc_leased, DA, SBC, FS_NI_attrib, eq_share, eq_divs)
Y = {
 2017: ("USGAAP", 2564310, 1206738, 152550, 0, 40189, 72659, 939795, 0, 152157, 362060, 180326),
 2018: ("USGAAP", 2917887, 1276788, 155114, 0, 70755, 63402, 1010972, 0, 521473, 470083, 196403),
 2019: ("USGAAP", 2707336, 1435964, 137314, 0, 63955, 60657, 1033528, 0, 227799, 360066, 204322),
 2020: ("IFRS", 2623364, 1222821, 163592, 299253, 46765, 49892, 855863, 4000, 218060, 310247, 208416),
 2021: ("IFRS", 2634200, 1203662, 142217, 271274, 38575, 46461, 928533, 4000, 369824, 351029, 205101),
 2022: ("IFRS", 3126101, 1186900, 151456, 335436, 36219, 45183, 1060079, 4000, 480716, 560346, 252557),
 2023: ("IFRS", 3682203, 1439724, 147792, 333295, 54572, 44195, 1240749, 4000, 292334, 643063, 349632),
 2024: ("IFRS", 6970082, 1815239, 153324, 317606, 152830, 47557, 1303053, 971, 411114, 763137, 460008),
 2025: ("IFRS", 4736610, 1878342, 24855, 341131, 68266, 6035, 1413066, 2833, 484129, 591219, 502793),
 2026: ("IFRS", 5479380, 2119162, 33176, 365834, 28647, 7997, 1472087, 2578, 618430, 552742, 304211),
}
# FY2020 on the US GAAP basis, for the basis-gap display only
FY2020_US = dict(OCF=2506822, fixed=1377238, leased=155601, proc_f=47488, proc_l=49913, DA=861673)

rows = {}
for y, (b, ocf, af, al, ai, pf, pl, da, sbc, fsni, eqs, eqd) in Y.items():
    capex_net = af + al + ai - pf - pl
    A = ocf - sbc - capex_net                 # (A) industrial, (c) = total net capex
    B = ocf - sbc - da                        # (B) industrial, (c) = D&A  -- INVALID end, display only
    undist = eqs - eqd                        # undistributed equity-method earnings [E3-04]
    D = A + fsni                              # (D) + FS net income attributable (look-through)
    E = D + undist                            # (E) + undistributed equity-method share
    rows[y] = dict(basis=b, ocf=ocf, capex_net=capex_net, da=da, capex_over_da=round(capex_net / da, 2),
                   sbc=sbc, A=A, B=B, fs_ni=fsni, undist=undist, D=D, E=E)

def mean(keys, col):
    return sum(rows[k][col] for k in keys) / len(keys)

windows = {"5yr FY2022-FY2026": range(2022, 2027), "7yr FY2020-FY2026 (IFRS only)": range(2020, 2027),
           "10yr FY2017-FY2026 (two bases)": range(2017, 2027), "3yr FY2024-FY2026": range(2024, 2027),
           "5yr ex-FY2024 (FY2021-23,25-26)": [2021, 2022, 2023, 2025, 2026]}
out = {"rows": rows, "windows": {}}
print(f"{'FY':6}{'basis':8}{'OCF':>11}{'netcapex':>11}{'D&A':>11}{'cx/DA':>7}{'(A)':>11}{'(B)inv':>11}{'FS NI':>10}{'undist':>10}{'(D)':>11}{'(E)':>11}")
for y, r in rows.items():
    print(f"{y:<6}{r['basis']:8}{r['ocf']:>11,}{r['capex_net']:>11,}{r['da']:>11,}{r['capex_over_da']:>7}{r['A']:>11,}{r['B']:>11,}{r['fs_ni']:>10,}{r['undist']:>10,}{r['D']:>11,}{r['E']:>11,}")
for name, ks in windows.items():
    ks = list(ks)
    w = {c: round(mean(ks, c)) for c in ("ocf", "capex_net", "da", "A", "B", "D", "E")}
    out["windows"][name] = w
    print(name, {k: f"{v:,}" for k, v in w.items()})
us = FY2020_US
capus = us["fixed"] + us["leased"] - us["proc_f"] - us["proc_l"]
print("FY2020 basis gap: US GAAP OCF-capex", f"{us['OCF'] - capus:,}", " IFRS", f"{rows[2020]['ocf'] - rows[2020]['capex_net'] - 0:,}")
print("capex/DA mean 10yr", round(sum(r['capex_over_da'] for r in rows.values()) / 10, 2))
json.dump(out, open(os.path.join(HERE, "oe_out.json"), "w"), indent=1)
