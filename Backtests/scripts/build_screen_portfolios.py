import csv, json, os, datetime, bisect, statistics
from collections import defaultdict

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
TODAY = datetime.date(2026, 7, 22)

rows = list(csv.DictReader(open(os.path.join(SCRATCH, "bt_results_combined.csv"))))

def f(x):
    return float(x) if x not in (None, "") else None

# first pass date + yield-at-first-pass, per ticker
first_pass = {}
pass_count = defaultdict(int)
for r in rows:
    if r["pass"] == "True":
        pass_count[r["ticker"]] += 1
        d = datetime.date.fromisoformat(r["asof"])
        if r["ticker"] not in first_pass or d < first_pass[r["ticker"]]["date"]:
            first_pass[r["ticker"]] = {"date": d, "yield": f(r["yield"]), "entry_px": f(r["entry_px"])}

def load_price_series(ticker):
    fn = os.path.join(CACHE, f"px_{ticker}.json")
    if not os.path.exists(fn):
        return None
    d = json.load(open(fn))
    res = d["chart"]["result"]
    if not res: return None
    res = res[0]
    ts = res["timestamp"]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
    close = res["indicators"]["quote"][0]["close"]
    series = {}
    for i, t in enumerate(ts):
        dt = datetime.datetime.utcfromtimestamp(t).date()
        v = adj[i] if adj and i < len(adj) and adj[i] is not None else close[i]
        if v is not None:
            series[dt] = v
    return series

def nearest(series, target, max_gap=10):
    dates = sorted(series.keys())
    idx = bisect.bisect_left(dates, target)
    cands = []
    if idx < len(dates): cands.append(dates[idx])
    if idx > 0: cands.append(dates[idx-1])
    if not cands: return None
    best = min(cands, key=lambda d: abs((d-target).days))
    if abs((best-target).days) > max_gap: return None
    return series[best]

# per-ticker buy-at-first-pass, hold-to-today CAGR
ticker_cagr = {}
for t, info in first_pass.items():
    series = load_price_series(t)
    if not series:
        continue
    entry_px = nearest(series, info["date"])
    exit_px = nearest(series, TODAY, max_gap=15)
    if entry_px is None or exit_px is None:
        continue
    years = (TODAY - info["date"]).days / 365.25
    if years < 0.5:
        continue
    cagr = (exit_px/entry_px)**(1/years) - 1
    ticker_cagr[t] = {"cagr": cagr, "years": years, "first_pass_date": info["date"].isoformat(),
                       "yield_at_pass": info["yield"], "times_passed": pass_count[t]}

spy_series = load_price_series("SPY")

def spy_cagr_for(entry_date):
    p0 = nearest(spy_series, entry_date)
    p1 = nearest(spy_series, TODAY, max_gap=15)
    years = (TODAY - entry_date).days / 365.25
    return (p1/p0)**(1/years) - 1

print(f"Buy-and-hold-to-today: {len(ticker_cagr)} tickers with computable CAGR (of {len(first_pass)} that ever passed)")
print()

# ---- Portfolio A: "Perpetual passers" (passed >= 8 of 13 years) ----
def portfolio_stats(name, tickers):
    if not tickers:
        print(f"{name}: no names")
        return
    cagrs = [ticker_cagr[t]["cagr"] for t in tickers if t in ticker_cagr]
    spys = [spy_cagr_for(first_pass[t]["date"]) for t in tickers if t in ticker_cagr]
    if not cagrs:
        print(f"{name}: 0 resolved names")
        return
    port_cagr = statistics.mean(cagrs)
    spy_match = statistics.mean(spys)
    print(f"{name}: n={len(cagrs)}  mean CAGR={port_cagr*100:6.2f}%  matched-SPY={spy_match*100:6.2f}%  names={sorted([t for t in tickers if t in ticker_cagr])}")
    return {"n": len(cagrs), "cagr": port_cagr, "spy_match": spy_match}

results = {}

high = [t for t, n in pass_count.items() if n >= 8]
med = [t for t, n in pass_count.items() if 3 <= n <= 7]
low = [t for t, n in pass_count.items() if n <= 2]
results["A_high_persistence"] = portfolio_stats("A. HIGH persistence (passed >=8/13 yrs)", high)
results["A_med_persistence"] = portfolio_stats("A. MED persistence (passed 3-7/13 yrs)", med)
results["A_low_persistence"] = portfolio_stats("A. LOW persistence (passed 1-2/13 yrs)", low)
print()

# ---- Portfolio B: top-10 cheapest at first pass (highest yield-at-first-pass) ----
by_yield = sorted(ticker_cagr.keys(), key=lambda t: -first_pass[t]["yield"])
results["B_top10_cheapest"] = portfolio_stats("B. Top 10 cheapest at first pass (highest yield)", by_yield[:10])
results["B_top20_cheapest"] = portfolio_stats("B. Top 20 cheapest at first pass (highest yield)", by_yield[:20])
print()

# ---- Portfolio C: earliest-discovered (first pass date earliest) small basket ----
by_date = sorted(ticker_cagr.keys(), key=lambda t: first_pass[t]["date"])
results["C_earliest10"] = portfolio_stats("C. Earliest 10 to ever pass (2013-14 vintage)", by_date[:10])
print()

# ---- Portfolio D: quality overlay -- only names where latest verified NI > worst-5yr NI
# (i.e. earnings recovering/growing off the trough, not still AT the trough) ----
# recompute from raw combined csv: need last5 NI trend -- reload with more fields
# (approximate using the 'yield' vs a recomputed "current yield" proxy is unavailable;
# use simplest available proxy: only keep tickers whose OVERALL historical pass rate
# is in the "MED" tier (3-7), i.e. exclude perma-cheap (HIGH) and one-off blips (LOW))
results["D_med_only_quality_proxy"] = portfolio_stats("D. Quality proxy: MED-persistence only (excludes perma-cheap & one-off blips)", med)
print()

# ---- All passers, equal weight (the full universe, for comparison) ----
all_t = list(ticker_cagr.keys())
results["ALL_passers"] = portfolio_stats("ALL tickers that ever passed, equal weight", all_t)

json.dump({k: v for k, v in results.items() if v}, open(os.path.join(SCRATCH, "screen_portfolios_results.json"), "w"), indent=2, default=str)
with open(os.path.join(SCRATCH, "screen_portfolios_per_ticker.csv"), "w", newline="") as fo:
    w = csv.writer(fo)
    w.writerow(["ticker","first_pass_date","times_passed_of_13","cagr","years_held","spy_matched_cagr"])
    for t, info in sorted(ticker_cagr.items(), key=lambda kv: -kv[1]["cagr"]):
        w.writerow([t, info["first_pass_date"], info["times_passed"], f"{info['cagr']*100:.2f}", f"{info['years']:.1f}", f"{spy_cagr_for(first_pass[t]['date'])*100:.2f}"])
