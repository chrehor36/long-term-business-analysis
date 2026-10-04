import json, os, itertools, statistics

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"

def run(label):
    d = json.load(open(os.path.join(SCRATCH, f"bt14_returns_{label}.json")))
    years = d["years"]
    spy_total = d["spy"]["total_return_x"]
    spy_cagr = d["spy"]["cagr_pct"]
    names = [r["ticker"] for r in d["survivors"]]
    mult = {r["ticker"]: r["total_return_x"] for r in d["survivors"]}
    n = len(names)
    combos = list(itertools.combinations(names, 10))
    port_cagrs = []
    beat = 0
    for c in combos:
        avg_mult = sum(mult[t] for t in c) / 10
        cagr = (avg_mult ** (1/years) - 1) * 100
        port_cagrs.append(cagr)
        if cagr > spy_cagr:
            beat += 1
    port_cagrs.sort()
    med = statistics.median(port_cagrs)
    mean = statistics.mean(port_cagrs)
    worst = port_cagrs[0]
    best = port_cagrs[-1]
    print(f"\n=== {label}: C({n},10) = {len(combos)} portfolios, {years:.2f} yrs ===")
    print(f"SPY CAGR: {spy_cagr:.2f}%  ({spy_total:.3f}x)")
    print(f"Portfolio CAGR -- min {worst:.2f}% | median {med:.2f}% | mean {mean:.2f}% | max {best:.2f}%")
    print(f"Beat rate vs SPY: {beat}/{len(combos)} = {100*beat/len(combos):.1f}%")
    return {"label": label, "n_survivors": n, "n_portfolios": len(combos), "years": years,
            "spy_cagr": spy_cagr, "spy_total_x": spy_total,
            "port_cagr_min": worst, "port_cagr_median": med, "port_cagr_mean": mean, "port_cagr_max": best,
            "beat_count": beat, "beat_rate_pct": 100*beat/len(combos)}

s2020 = run("2020")
s2016 = run("2016")
json.dump({"2020": s2020, "2016": s2016}, open(os.path.join(SCRATCH, "bt14_enum_summary.json"), "w"), indent=1)
