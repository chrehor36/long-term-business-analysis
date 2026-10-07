"""Competitor row arithmetic. TSMC from series_out.json (companyfacts FY2015-24, FY2025 typed from the 20-F);
UMC and GFS from peers/peerseries_out.json, UMC FY2025 typed from UMC 20-F 0001193125-26-193757.
Intel Foundry operating margin from the INTC run (10-K Note 3). Arithmetic only."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
s = json.load(open(os.path.join(HERE, "series_out.json")))
p = json.load(open(os.path.join(HERE, "peers", "peerseries_out.json")))
s["gp"]["2025"] = 2281294.0
s["oi"]["2025"] = 1936091.7
s["ni_parent"]["2025"] = 1717882.6
s["equity_parent"]["2025"] = 5419596.0
p["UMC"]["rev"]["2025"] = 237553.2; p["UMC"]["gp"]["2025"] = 68906.5; p["UMC"]["oi"]["2025"] = 43948.7
p["UMC"]["capex"]["2025"] = 47744.9; p["UMC"]["ocf"]["2025"] = 99864.2
yrs = [str(y) for y in range(2015, 2026)]
out = {"TSMC": {}, "UMC": {}, "GFS": {}}
print("year | TSMC GM OM capex/rev capex/dep ROE | UMC GM OM capex/rev | GFS GM OM capex/rev")
for y in yrs:
    t = s
    r = t["rev"][y]
    gm = 100 * t["gp"][y] / r; om = 100 * t["oi"][y] / r; cr = 100 * t["capex"][y] / r
    cd = t["capex"][y] / t["dep"][y]
    py = str(int(y) - 1)
    roe = None
    if py in t["equity_parent"] and y in t["equity_parent"]:
        roe = 100 * t["ni_parent"][y] / ((t["equity_parent"][y] + t["equity_parent"][py]) / 2)
    out["TSMC"][y] = dict(gm=gm, om=om, capex_rev=cr, capex_dep=cd, roe=roe, rev=r)
    u = p["UMC"]; ug = uo = uc = None
    if y in u["rev"]:
        ug = 100 * u["gp"][y] / u["rev"][y]; uo = 100 * u["oi"][y] / u["rev"][y]; uc = 100 * u["capex"][y] / u["rev"][y]
        out["UMC"][y] = dict(gm=ug, om=uo, capex_rev=uc, rev=u["rev"][y])
    g = p["GFS"]; gg = go = gc = None
    if y in g["rev"]:
        gg = 100 * g["gp"][y] / g["rev"][y]; go = 100 * g["oi"][y] / g["rev"][y]; gc = 100 * g["capex"][y] / g["rev"][y]
        out["GFS"][y] = dict(gm=gg, om=go, capex_rev=gc, rev=g["rev"][y])
    f = lambda v: "  n/a" if v is None else f"{v:5.1f}"
    print(y, "|", f(gm), f(om), f(cr), f"{cd:4.2f}", f(roe), "|", f(ug), f(uo), f(uc), "|", f(gg), f(go), f(gc))
# revenue multiples
print("TSMC rev 2015->2025 x", round(s["rev"]["2025"] / s["rev"]["2015"], 2), " 2019->2025 x", round(s["rev"]["2025"] / s["rev"]["2019"], 2))
print("UMC  rev 2015->2025 x", round(p["UMC"]["rev"]["2025"] / p["UMC"]["rev"]["2015"], 2), " 2019->2025 x", round(p["UMC"]["rev"]["2025"] / p["UMC"]["rev"]["2019"], 2))
print("GFS  rev 2019->2025 x", round(p["GFS"]["rev"]["2025"] / p["GFS"]["rev"]["2019"], 2))
# ten-year cumulative capex
print("TSMC cum capex 2016-25 NT$bn", round(sum(s["capex"][y] for y in yrs[1:]) / 1e3), "UMC", round(sum(p["UMC"]["capex"][y] for y in yrs[1:]) / 1e3))
print("TSMC cum dep 2016-25 NT$bn", round(sum(s["dep"][y] for y in yrs[1:]) / 1e3))
# revenue per wafer, USD, from decks: rev US$bn / shipments kpcs
pairs = {"3Q22": (20.23, 3974), "3Q23": (17.28, 2902), "4Q22": (19.93, 3702), "4Q23": (19.62, 2957),
         "2Q25": (30.07, 3718), "2Q26": (40.20, 4336), "3Q24": (23.50, 3338), "3Q25": (33.10, 4085)}
for k, (rv, sh) in pairs.items():
    print(k, "US$ per 12in-equiv wafer", round(rv * 1e9 / (sh * 1e3)))
json.dump(out, open(os.path.join(HERE, "row_out.json"), "w"), indent=1)
