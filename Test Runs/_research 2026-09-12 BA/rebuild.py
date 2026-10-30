import json
s = json.load(open("Test Runs/_research 2026-09-12 BA/series.json"))
# Treasury shares issued for 401(k) contribution -- READ FROM THE FILED CASH-FLOW STATEMENTS.
# XBRL carries this only for FY2010-12 and FY2020; FY2021 onward exist only in the filing.
# sources: FY2025 10-K (2025/2024/2023), FY2023 10-K (2023/2022/2021), FY2022 10-K (2022/2021/2020),
# FY2020 10-K (2020). Line absent before FY2020 (the 401(k) match was paid in cash then, so it is
# already an operating outflow inside OCF and must NOT be subtracted again).
K401 = {2020:195, 2021:1233, 2022:1215, 2023:1515, 2024:1601, 2025:1530}

rows = {}
for e in sorted(s["OCF"]):
    y = int(e[:4])
    ocf = s["OCF"][e]; sbc = s["SBC"].get(e); da = s["DA"].get(e); cx = s["CAPEX"].get(e)
    if None in (sbc, da, cx):
        continue
    k = K401.get(y, 0.0)
    comp = sbc + k                      # ALL equity-settled employee compensation [E5-06, E3-70]
    rows[y] = dict(ocf=ocf, sbc=sbc, k401=k, comp=comp, da=da, cx=cx,
                   oe_da=ocf-comp-da, oe_cx=ocf-comp-cx,
                   scr_da=ocf-sbc-da, scr_cx=ocf-sbc-cx)

print("OWNER EARNINGS, REBUILT WITH ALL EQUITY-SETTLED COMPENSATION SUBTRACTED ($M)")
print(f"{'FY':<5}{'OCF':>9}{'SBC':>7}{'401kSTK':>9}{'=comp':>8}{'D&A':>7}{'capex':>8}"
      f"{'OE(D&A)':>10}{'OE(capex)':>11}   {'screen OE(D&A)':>14}{'screen OE(cx)':>14}")
for y in sorted(rows):
    r = rows[y]
    print(f"{y:<5}{r['ocf']:>9,.0f}{r['sbc']:>7,.0f}{r['k401']:>9,.0f}{r['comp']:>8,.0f}"
          f"{r['da']:>7,.0f}{r['cx']:>8,.0f}{r['oe_da']:>10,.0f}{r['oe_cx']:>11,.0f}"
          f"   {r['scr_da']:>14,.0f}{r['scr_cx']:>14,.0f}")

WINS = [
 ("FY2008-2025 (18y, all filed)",        range(2008, 2026)),
 ("FY2016-2025 (10y)",                   range(2016, 2026)),
 ("FY2021-2025 (5y, the screen window)", range(2021, 2026)),
 ("FY2023-2025 (3y, the screen window)", range(2023, 2026)),
 ("--- pre-break: a different company ---", []),
 ("FY2011-2018 (8y, pre-grounding)",     range(2011, 2019)),
 ("FY2014-2018 (5y, pre-grounding)",     range(2014, 2019)),
 ("--- post-break: the business that exists now ---", []),
 ("FY2019-2025 (7y, whole post-grounding era)", range(2019, 2026)),
 ("FY2021-2025 (5y, post-COVID-trough)", range(2021, 2026)),
 ("FY2022-2025 (4y)",                    range(2022, 2026)),
 ("FY2024-2025 (2y, post-door-plug)",    range(2024, 2026)),
 ("FY2025 (1y, single year)",            range(2025, 2026)),
]
print("\nWINDOWS -- mean owner earnings, $M")
band = []
for label, yrs in WINS:
    yrs = [y for y in yrs if y in rows]
    if not yrs:
        print(f"  {label}")
        continue
    a = sum(rows[y]['oe_da'] for y in yrs)/len(yrs)
    b = sum(rows[y]['oe_cx'] for y in yrs)/len(yrs)
    print(f"  {label:<46} n={len(yrs):<3} D&A end {a:>10,.0f}   capex end {b:>10,.0f}")
    if len(yrs) > 1:
        band += [a, b]
print(f"\n  FULL BAND, every multi-year window x both (c) ends: {min(band):,.0f} to {max(band):,.0f}"
      f"   width {max(band)-min(band):,.0f}")
post = [w for w in WINS if w[0].startswith(("FY2019-2025","FY2021-2025","FY2022-2025","FY2024-2025"))]
pb = []
for label, yrs in post:
    yrs = [y for y in yrs if y in rows]
    pb += [sum(rows[y]['oe_da'] for y in yrs)/len(yrs), sum(rows[y]['oe_cx'] for y in yrs)/len(yrs)]
print(f"  POST-BREAK ONLY (FY2019-25 and inside it): {min(pb):,.0f} to {max(pb):,.0f}")

# TTM from the filings: FY2025 - H1 2025 + H1 2026
H1_25 = dict(ocf=-1389, sbc=254, k401=793, da=926,   cx=1101)
H1_26 = dict(ocf= 1185, sbc=264, k401=855, da=1169,  cx=2008)
f25 = rows[2025]
ttm = {k: f25[k] - H1_25[k] + H1_26[k] for k in ("ocf","sbc","k401","da","cx")}
comp = ttm["sbc"] + ttm["k401"]
print("\nTTM to 2026-06-30 (FY2025 10-K less H1-2025 10-Q plus H1-2026 10-Q):")
print(f"  OCF {ttm['ocf']:,.0f}  SBC {ttm['sbc']:,.0f}  401k stock {ttm['k401']:,.0f}"
      f"  D&A {ttm['da']:,.0f}  capex {ttm['cx']:,.0f}")
print(f"  TTM OE, D&A end   {ttm['ocf']-comp-ttm['da']:>10,.0f}")
print(f"  TTM OE, capex end {ttm['ocf']-comp-ttm['cx']:>10,.0f}")

# working-capital dependence
WC = {2020:(-1060,-5363), 2021:(2505,-3783), 2022:(108,838), 2023:(3365,1672),
      2024:(4069,-793), 2025:(-723,724)}
print("\nIS THE OPERATING CASH BEING FUNDED BY CUSTOMERS AND SUPPLIERS? ($M)")
print(f"{'FY':<6}{'OCF':>9}{'advances':>10}{'payables':>10}{'both':>9}{'OCF ex-both':>13}")
for y in sorted(WC):
    adv, ap = WC[y]
    o = rows[y]['ocf']
    print(f"{y:<6}{o:>9,.0f}{adv:>10,.0f}{ap:>10,.0f}{adv+ap:>9,.0f}{o-adv-ap:>13,.0f}")
print(f"{'H1-26':<6}{1185:>9,.0f}{4660:>10,.0f}{1381:>10,.0f}{6041:>9,.0f}{1185-6041:>13,.0f}")
