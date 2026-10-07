"""STLA owner earnings, industrial perimeter, EUR million. Arithmetic only; every input is a filed figure
recorded in the run file with its source. (c) is a disclosed judgment: two ends shown.
capex end : industrial OCF - SBC - industrial capex (incl. capitalised development and payables change) - lease principal
D&A end   : industrial OCF - SBC - D&A   (D&A includes right-of-use depreciation, so lease principal is not also deducted)
"""
import json

# Stellantis perimeter (PSA accounting acquirer; FCA from 2021-01-17)
S = {
    # year: (consolidated OCF, FS OCF removed, industrial capex, D&A, SBC incl ESPP cost, lease principal)
    2021: (18646, 276, 10081, 5871, 201, 566),
    2022: (19959, 211, 8938, 6797, 170, 568),
    2023: (22485, -753, 9031, 7549, 189 + 36, 693),   # FY2024 20-F old basis
    2024: (1535, -5209, 10761, 7226, 45 + 58, 874),   # FY2025 20-F new basis (industrial identical on old basis)
    2025: (-4650, -9700, 9090, 6981, 73 + 32, 867),
}
FCA_STUB_2021_IFCF = -1813   # "Add: Industrial free cash flows of FCA, January 1 - 16, 2021" (20-F FY2022)

# Pro forma predecessors, both filed cash-flow statements added, no eliminations (none filed)
PF = {
    # FCA: IFCF reconciliation 20-F FY2020 (continuing OCF less non-industrial; capex for industrial activities);
    # PSA: 20-F FY2021 comparatives, continuing = total less discontinued (Faurecia); capex incl. payables change
    2019: dict(ocf=(10770 - 74) + (8667 - 1837), capex=8383 + (3544 + 123), da=5445 + 2191, sbc=92 + 37, lease=299 + 185),
    2020: dict(ocf=(9183 - 29) + (6241 - 1136), capex=8598 + (2733 + 217), da=5143 + 2376, sbc=98 + 34, lease=389 + 177),
}

rows = {}
for y, (ocf, fs, capex, da, sbc, lease) in S.items():
    ind = ocf - fs
    rows[y] = dict(ind_ocf=ind, capex=capex, da=da, sbc=sbc, lease=lease,
                   oe_capex=ind - sbc - capex - lease, oe_da=ind - sbc - da)
rows[2021]["oe_capex_pf"] = rows[2021]["oe_capex"] + FCA_STUB_2021_IFCF
rows[2021]["oe_da_pf"] = rows[2021]["oe_da"] + FCA_STUB_2021_IFCF
for y, d in PF.items():
    rows[y] = dict(ind_ocf=d["ocf"], capex=d["capex"], da=d["da"], sbc=d["sbc"], lease=d["lease"],
                   oe_capex=d["ocf"] - d["sbc"] - d["capex"] - d["lease"], oe_da=d["ocf"] - d["sbc"] - d["da"], pro_forma=True)

def mean(years, key, pf2021=False):
    vals = []
    for y in years:
        k = key + "_pf" if (pf2021 and y == 2021) else key
        vals.append(rows[y][k])
    return sum(vals) / len(vals)

out = {"rows": rows, "windows": {}}
W = {"5yr 2021-25 (as filed)": (list(range(2021, 2026)), False),
     "5yr 2021-25 (FCA Jan 1-16 added)": (list(range(2021, 2026)), True),
     "3yr 2023-25": ([2023, 2024, 2025], False),
     "2yr 2024-25": ([2024, 2025], False),
     "7yr 2019-25 pro forma (FCA+PSA 2019-20)": (list(range(2019, 2026)), True)}
for name, (ys, pf) in W.items():
    out["windows"][name] = dict(capex_end=round(mean(ys, "oe_capex", pf)), da_end=round(mean(ys, "oe_da", pf)))
for y in sorted(rows):
    r = rows[y]
    print(y, {k: v for k, v in r.items()})
for k, v in out["windows"].items():
    print(k, v)
tot_capex = sum(rows[y]["capex"] for y in range(2021, 2026)); tot_da = sum(rows[y]["da"] for y in range(2021, 2026))
print("capex/D&A 2021-25", round(tot_capex / tot_da, 3), "2019-25", round(sum(rows[y]["capex"] for y in rows) / sum(rows[y]["da"] for y in rows), 3))
json.dump(out, open("oe_out.json", "w"), indent=1)
