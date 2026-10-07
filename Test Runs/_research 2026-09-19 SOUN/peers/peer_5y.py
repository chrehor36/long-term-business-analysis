import sys, importlib.util, os
sys.stdout.reconfigure(encoding="utf-8")
spec = importlib.util.spec_from_file_location("pr", os.path.join(os.path.dirname(os.path.abspath(__file__)), "peer_row.py"))
src = open(spec.origin).read().split("for t in sys.argv[1:]:")[0]
ns = {"__file__": spec.origin}; exec(src, ns)
for t in ["SOUN","CRNC","LPSN","FIVN","NICE"]:
    f = ns["load"](t); d = {k: ns["first"](f, v) for k, v in ns["M"].items()}
    ys = [2021,2022,2023,2024,2025]
    rev = sum(d["rev"][y] for y in ys)
    oc = sum(d["ocf"][y] - d["sbc"][y] - (d["capex"].get(y) or 0) - (d["capsw"].get(y) or 0) for y in ys)
    sbc = sum(d["sbc"][y] for y in ys); ocf = sum(d["ocf"][y] for y in ys)
    cagr = (d["rev"][2025]/d["rev"][2021])**0.25 - 1
    gp = d["gp"].get(2025) or (d["rev"][2025] - d["cor"][2025])
    print(f"{t}: rev FY2021 {d['rev'][2021]/1e6:.1f} FY2025 {d['rev'][2025]/1e6:.1f} CAGR {cagr:.1%}; GM FY2025 {gp/d['rev'][2025]:.1%}; opm FY2025 {d['opinc'][2025]/d['rev'][2025]:.1%}; "
          f"5y owner cash (OCF-SBC-capex-capsw) {oc/1e6:.1f} on rev {rev/1e6:.1f} = {oc/rev:.1%}; SBC/OCF 5y {sbc/ocf:.1%} (OCF {ocf/1e6:.1f}); SBC/rev 5y {sbc/rev:.1%}")
