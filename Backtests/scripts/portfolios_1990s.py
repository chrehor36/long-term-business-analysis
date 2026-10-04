import csv, os, json, datetime, bisect, itertools, statistics

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
REBAL = datetime.date(1993, 12, 31)
TODAY = datetime.date(2026, 7, 24)
YEARS = (TODAY - REBAL).days / 365.25

SURVIVORS = ['WEC','MMM','WFC','GL','EMR','HBAN','NTRS','HRB','PCAR','MCD','GWW','STT']

def load_series(fn):
    d = json.load(open(fn))
    res = d["chart"]["result"][0]
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

def nearest(series, target, max_gap=20):
    dates = sorted(series.keys())
    idx = bisect.bisect_left(dates, target)
    cands = []
    if idx < len(dates): cands.append(dates[idx])
    if idx > 0: cands.append(dates[idx-1])
    if not cands: return None
    best = min(cands, key=lambda d: abs((d-target).days))
    if abs((best-target).days) > max_gap: return None
    return series[best]

def latest_price(ticker):
    for prefix in ("pxfull_", "pxlong_", "px_"):
        fn = os.path.join(CACHE, f"{prefix}{ticker}.json")
        if os.path.exists(fn):
            s = load_series(fn)
            d = max(s.keys())
            return d, s[d]
    return None

# entry prices from the 1990s screen (already split-corrected and sanity-checked)
screen = {r["ticker"]: r for r in csv.DictReader(open(os.path.join(SCRATCH, "screen_1990s_results.csv")))}

results = {}
for t in SURVIVORS:
    entry_px = float(screen[t]["price"])
    exit_date, exit_px = latest_price(t)
    total_return = exit_px / entry_px - 1.0
    cagr = (1 + total_return) ** (1/YEARS) - 1
    results[t] = {"entry_px": entry_px, "exit_px": exit_px, "exit_date": exit_date,
                  "total_return": total_return, "cagr": cagr}
    print(f"{t:6s} entry=${entry_px:8.2f}  exit=${exit_px:8.2f} ({exit_date})  "
          f"total={total_return*100:8.1f}%  CAGR={cagr*100:6.2f}%")

# SPY benchmark
spy_series = load_series(os.path.join(CACHE, "pxlong_SPY.json"))
spy_entry = nearest(spy_series, REBAL)
spy_exit_date = max(spy_series.keys())
spy_exit = spy_series[spy_exit_date]
spy_total = spy_exit / spy_entry - 1.0
spy_cagr = (1 + spy_total) ** (1/YEARS) - 1
print(f"\nSPY entry=${spy_entry:.2f} ({REBAL}) -> exit=${spy_exit:.2f} ({spy_exit_date})")
print(f"SPY total={spy_total*100:.1f}%  CAGR={spy_cagr*100:.2f}%")
print(f"({YEARS:.2f} years)")

with open(os.path.join(SCRATCH, "returns_1990s.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker","entry_px","exit_px","exit_date","total_return","cagr"])
    for t, r in results.items():
        w.writerow([t, r["entry_px"], r["exit_px"], r["exit_date"], r["total_return"], r["cagr"]])

# ---- Exhaustive enumeration: every possible 10-name portfolio from the 12 survivors ----
def port_cagr(tickers):
    mult = statistics.mean(1 + results[t]["total_return"] for t in tickers)
    return mult ** (1/YEARS) - 1

combos = list(itertools.combinations(SURVIVORS, 10))
cagrs = [port_cagr(c) for c in combos]
beat = sum(1 for c in cagrs if c > spy_cagr)

print(f"\n=== EVERY possible 10-name portfolio from the 12 full-gate 1990s survivors ===")
print(f"C(12,10) = {len(combos)} portfolios")
print(f"Beat SPY: {beat} / {len(combos)} ({beat/len(combos)*100:.1f}%)")
print(f"Mean CAGR:   {statistics.mean(cagrs)*100:.2f}%")
print(f"Median CAGR: {statistics.median(cagrs)*100:.2f}%")
print(f"Min / Max:   {min(cagrs)*100:.2f}% / {max(cagrs)*100:.2f}%")

ranked = sorted(zip(combos, cagrs), key=lambda x: x[1])
print(f"\nWorst portfolio: CAGR={ranked[0][1]*100:.2f}%  excludes={set(SURVIVORS)-set(ranked[0][0])}")
print(f"Best portfolio:  CAGR={ranked[-1][1]*100:.2f}%  excludes={set(SURVIVORS)-set(ranked[-1][0])}")

# all 12 together (reference)
all12 = port_cagr(SURVIVORS)
print(f"\nAll 12 survivors, equal-weight (reference, n=12 not 10): {all12*100:.2f}% CAGR")

with open(os.path.join(SCRATCH, "portfolios_1990s_all.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tickers", "cagr"])
    for c, cg in zip(combos, cagrs):
        w.writerow([" ".join(sorted(c)), cg])
