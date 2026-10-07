"""GFS owner earnings, US$M, from the filed cash-flow statements (inputs in row.py, transcribed by hand).
OE = OCF - SBC - (change in contract liabilities) - (c).   CONVENTION (framework VI) plus disclosed run-specific choices:
  * SBC: the [E3-70] market-value measure = grant-date fair value of RSU+PSU grants (Note: share-based payments) for 2022-2025;
    the cash-flow charge where no grant table was read (2019-2021) and as the floor, displayed.
  * Contract liabilities (customer prepayments, capacity access fees) flow through operating cash ("Trade and other payables");
    the year's change is removed, as in the TSM run, because it is a customer advance, not earnings.
  * (c): two ends, both disclosed judgments [E2-23, E3-44, E5-20]:
      capex end  = capex (PP&E + intangibles) - government grant proceeds  (acquisitions displayed separately, in neither end, as the UMC run did)
      D&A end    = the cash-flow depreciation and amortisation add-back (the corpus default)
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "row_out.json")))["inputs"]
D = {int(k): v for k, v in R.items()}
grant_value = {2022: 3.416545*57.09 + 0.571277*70.85, 2023: 2.426183*62.94 + 0.875646*69.73,
               2024: 3.5*52.37 + 0.8*53.50, 2025: 6.8*36.25 + 1.6*36.88}
acq = {2019: 0.0, 2020: 0.0, 2021: 0.0, 2022: 0.0, 2023: 0.0, 2024: 69.0, 2025: 682.0}
cl_prev = {2020: 144.6}
rows = {}
for y in range(2019, 2026):
    d = D[y]
    sbc_charge = d["sbc"]; sbc = max(sbc_charge, grant_value.get(y, 0.0))
    dcl = None if y == 2019 else d["cl"] - (D[y-1]["cl"] if y-1 in D else cl_prev[y])
    base = d["ocf"] - sbc - (dcl or 0.0)
    cx = d["capex"] - d["grants"]
    rows[y] = dict(ocf=d["ocf"], sbc_charge=sbc_charge, sbc_used=round(sbc, 1), dcl=dcl and round(dcl, 1), net_capex=round(cx, 1), acq=acq[y],
                   da=d["da"], oe_capex=round(base - cx, 1), oe_da=round(base - d["da"], 1), oe_capex_charge_sbc=round(d["ocf"] - sbc_charge - (dcl or 0) - cx, 1), oe_capex_less_acq=round(base - cx - acq[y], 1))
# TTM to 2026-06-30 = FY2025 + H1 2026 - H1 2025 (interim statements, 6-K 0001709048-26-000219 and 0001709048-25-000057)
ttm = dict(ocf=1731+947-762, sbc_charge=200+128-94, capex=722+723-325, grants=148+6-5, acq=682+440-19, da=1314+618-687,
           dcl=(954-21)-1568)
ttm_sbc = ttm["sbc_charge"]  # no interim grant table; charge used, displayed only
ttm_base = ttm["ocf"] - ttm_sbc - ttm["dcl"]
rows["TTM 2026-06"] = dict(ocf=ttm["ocf"], sbc_used=ttm_sbc, dcl=ttm["dcl"], net_capex=ttm["capex"]-ttm["grants"], acq=ttm["acq"], da=ttm["da"],
                           oe_capex=ttm_base-(ttm["capex"]-ttm["grants"]), oe_da=ttm_base-ttm["da"], oe_capex_less_acq=ttm_base-(ttm["capex"]-ttm["grants"])-ttm["acq"])
for k, v in rows.items(): print(k, v)
def mean(ys, key): return round(sum(rows[y][key] for y in ys) / len(ys), 1)
W = {"5-yr 2021-2025": range(2021, 2026), "3-yr 2023-2025": range(2023, 2026), "4-yr 2022-2025": range(2022, 2026),
     "6-yr 2020-2025 (display; pre-2021 D&A on 5-8 year lives)": range(2020, 2026)}
win = {}
for n, ys in W.items():
    win[n] = dict(oe_capex=mean(ys, "oe_capex"), oe_da=mean(ys, "oe_da"), capex=mean(ys, "net_capex"), acq=mean(ys, "acq"), oe_capex_less_acq=mean(ys, "oe_capex_less_acq"), da=mean(ys, "da"),
                  sbc=mean(ys, "sbc_used"), dcl=round(sum((rows[y]["dcl"] or 0) for y in ys)/len(list(ys)), 1))
    print(n, win[n])
# no-strip sensitivity (prepayments left in), 5-yr
ns = round(sum(rows[y]["oe_capex"] + (rows[y]["dcl"] or 0) for y in range(2021, 2026)) / 5, 1)
ns_da = round(sum(rows[y]["oe_da"] + (rows[y]["dcl"] or 0) for y in range(2021, 2026)) / 5, 1)
print("5-yr without the prepayment strip: capex end", ns, "D&A end", ns_da)
json.dump(dict(rows={str(k): v for k, v in rows.items()}, windows=win, no_strip_5yr=dict(capex=ns, da=ns_da)),
          open(os.path.join(HERE, "oe_out.json"), "w"), indent=1)
