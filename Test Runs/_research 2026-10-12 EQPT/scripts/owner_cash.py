# Owner cash for EQPT from the filed cash-flow statements ($M).
# 2022-2024: 424B4 (0001628280-26-003334) F-36; 2023-2025: 10-K FY2025 (0001628280-26-019656) p.86;
# H1 2025 / H1 2026: 10-Q Q2 2026 (0001693736-26-000020) p.12.
import sys; sys.stdout.reconfigure(encoding="utf-8")
Y = {
 # ocf, rent_buy, rent_sell, ppe_buy, ppe_sell, software, acq, sbc, cash_int, dep_amort, fin_lease_pay?, pref_div, rev, gp_own_sales
 2022: dict(ocf=228.5, rb=1248.0, rs=491.2, pb=155.9, ps=148.9, sw=20.2, acq=39.5, sbc=2.9, ci=112.1, da=211.7, pd=0.0, rev=1732.8, oi=170.1),
 2023: dict(ocf=278.8, rb=1097.8, rs=646.6, pb=185.4, ps=57.6, sw=24.7, acq=0.0, sbc=3.4, ci=199.9, da=295.0, pd=5.0, rev=2556.2, oi=250.1),
 2024: dict(ocf=281.3, rb=1585.5, rs=1322.6, pb=194.5, ps=101.6, sw=38.4, acq=6.3, sbc=4.2, ci=230.3, da=332.2, pd=9.0, rev=3763.3, oi=217.8),
 2025: dict(ocf=264.0, rb=1780.0, rs=1160.0, pb=248.0, ps=2.0, sw=39.0, acq=48.0, sbc=4.0, ci=272.0, da=365.0, pd=37.0, rev=4379.0, oi=297.0),
}
T = 0.21  # statutory federal rate, a CONVENTION of this run for the interest add-back
print("year | OCF | all capex net | acq | SBC | owner cash equity-only (all spending) | + after-tax cash interest = all-equity | D&A | maintenance-only equity-only (OCF - D&A - SBC) | maintenance-only all-equity")
res = {}
for y, d in Y.items():
    capex = d["rb"] - d["rs"] + d["pb"] - d["ps"] + d["sw"]
    eq_all = d["ocf"] - capex - d["acq"]          # SBC already deducted in net income; OCF adds it back -> deduct
    eq_all -= d["sbc"]
    ae_all = eq_all + d["ci"] * (1 - T)
    eq_m = d["ocf"] - d["da"] - d["sbc"]
    ae_m = eq_m + d["ci"] * (1 - T)
    res[y] = (eq_all, ae_all, eq_m, ae_m)
    print(f"{y} | {d['ocf']:.1f} | {capex:.1f} | {d['acq']:.1f} | {d['sbc']:.1f} | {eq_all:.1f} | {ae_all:.1f} | {d['da']:.1f} | {eq_m:.1f} | {ae_m:.1f}")
n = len(res)
avg = [sum(v[i] for v in res.values())/n for i in range(4)]
print("4-yr avg (2022-2025):", " | ".join(f"{a:.1f}" for a in avg))
# H1 2026 vs H1 2025
h = dict(ocf=-142, rb=1017, rs=483, pb=163, ps=1, sw=17, acq=9, sbc=45, ci=131, da=216)
c = h["rb"]-h["rs"]+h["pb"]-h["ps"]+h["sw"]
print("H1 2026 equity-only all spending:", h["ocf"]-c-h["acq"]-h["sbc"], " maint-only:", h["ocf"]-h["da"]-h["sbc"])
