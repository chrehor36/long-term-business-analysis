"""Competitor row and UMC return/capital arithmetic. UMC: companyfacts FY2015-24 + FY2025 20-F (series_out.json), cash-flow
lines from filed statements (cfread_out.json). TSMC/GFS gross margin from the TSM run's row_out.json; Tower from companyfacts
(peers/peers_out.json); SMIC and Hua Hong typed from their own releases (peers/*.txt). Arithmetic only."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
s = json.load(open(os.path.join(H, "series_out.json")))
cf = json.load(open(os.path.join(H, "cfread_out.json")))
tsm = json.load(open(os.path.join(H, "..", "_research 2026-09-13 TSM", "row_out.json")))
tw = json.load(open(os.path.join(H, "peers", "peers_out.json")))["TSEM"]
def c(k, y):
    d = cf[k][y]; return list(d.values())[-1] if len(d) == 1 else d[max(d)]
yrs = [str(y) for y in range(2015, 2026)]
out = {"UMC": {}}
print("yr  UMC_GM OM  capex/rev capex/dep ROE  | TSMC_GM GFS_GM TSEM_GM")
for y in yrs:
    rev = s["rev"][y]; gm = 100*s["gp"][y]/rev; om = 100*s["oi"][y]/rev
    capex = -c("capex", y); dep = c("dep", y)
    py = str(int(y)-1); roe = None
    if py in s["equity_parent"] and y in s["equity_parent"]:
        roe = 100*s["ni_parent"][y]/((s["equity_parent"][y]+s["equity_parent"][py])/2)
    out["UMC"][y] = dict(gm=gm, om=om, capex_rev=100*capex/rev, capex_dep=capex/dep, roe=roe)
    t = tsm["TSMC"].get(y, {}).get("gm"); g = tsm["GFS"].get(y, {}).get("gm"); w = tw.get(y, {}).get("gm")
    f = lambda v: "  -  " if v is None else f"{v:5.1f}"
    print(y, f(gm), f(om), f(100*capex/rev), f"{capex/dep:4.2f}", f(roe), "|", f(t), f(g), f(w))
SMIC = {"gm": {"2022": 38.0, "2023": 19.3, "2024": 18.0, "2025": 21.0}, "cap_end": {"2022": 714.0, "2023": 805.5, "2024": 948.0, "2025": 1059.0},
        "capex_usd_bn": {"2024": 7.33, "2025": 8.1}, "rev_usd_bn": {"2022": 7.2733, "2023": 6.3216, "2024": 8.0299, "2025": 9.3268}}
HH = {"gm": {"2021": 27.7, "2022": 34.1, "2023": 21.3, "2024": 10.2, "2025": 11.8}, "cap_end": {"2022": 324.0, "2023": 391.0, "2024": 391.0, "2025": 486.0},
      "rev_usd_bn": {"2023": 2.2861, "2024": 2.004, "2025": 2.4021}}
umc_cap_8in_month = {"2022": 10031/12, "2023": 4674*2.25/12, "2024": 5022*2.25/12, "2025": 5163*2.25/12}
cn = {y: SMIC["cap_end"][y]+HH["cap_end"][y] for y in SMIC["cap_end"]}
print("China two (end-yr monthly 8in eq, k):", cn, "change 2022->2025 %.1f%%" % (100*(cn["2025"]/cn["2022"]-1)))
print("UMC (annual est. capacity as monthly 8in eq, k):", {k: round(v) for k, v in umc_cap_8in_month.items()}, "change %.1f%%" % (100*(umc_cap_8in_month["2025"]/umc_cap_8in_month["2022"]-1)))
print("SMIC capex/rev 2024 %.0f%% 2025 %.0f%%" % (100*7.33/8.0299, 100*8.1/9.3268))
# ASP index
asp = {"2015": 1.1, "2016": -1.8, "2017": -4.9, "2018": -3.4, "2019": -2.9, "2020": -0.5, "2021": 14.6, "2022": 21.3, "2023": 6.3, "2024": -5.0, "2025": -5.4}
idx = 100.0; ix = {"2014": 100.0}
for y in yrs:
    idx *= 1 + asp[y]/100; ix[y] = idx
print("UMC ASP index (2014=100):", {k: round(v, 1) for k, v in ix.items()})
print("2015-2019 cumulative: %.1f%%; 2023->2025: %.1f%%" % (100*(ix["2020"]/ix["2014"]-1), 100*(ix["2025"]/ix["2023"]-1)))
cum_capex = sum(-c("capex", y) for y in yrs[1:]); cum_dep = sum(c("dep", y) for y in yrs[1:])
print("UMC 2016-25 capex %.0f dep %.0f ratio %.2f" % (cum_capex, cum_dep, cum_capex/cum_dep))
out.update(SMIC=SMIC, HH=HH, umc_cap=umc_cap_8in_month, asp_index=ix)
json.dump(out, open(os.path.join(H, "row_out.json"), "w"), indent=1)
