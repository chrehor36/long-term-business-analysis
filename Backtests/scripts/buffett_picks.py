import json, os, datetime, bisect

CACHE = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad\bt_cache"

def load(ticker):
    d = json.load(open(os.path.join(CACHE, f"pxlong_{ticker}.json")))
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

def nearest(series, target):
    dates = sorted(series.keys())
    idx = bisect.bisect_left(dates, target)
    cands = []
    if idx < len(dates): cands.append(dates[idx])
    if idx > 0: cands.append(dates[idx-1])
    best = min(cands, key=lambda d: abs((d-target).days))
    return series[best], best

def cagr(start_val, end_val, years):
    return (end_val/start_val)**(1/years) - 1

TODAY = datetime.date(2026, 7, 22)

picks = [
    # ticker, entry_date, exit_date_or_None, label, note
    ("KO",  datetime.date(1989,1,1), None, "Coca-Cola", "position built 1988-89 [1989 Letter table]; still held"),
    ("AXP", datetime.date(1998,1,1), None, "American Express", "'last changed our position...in 1998' [2003 Letter]; still held"),
    ("WFC", datetime.date(1990,1,1), datetime.date(2022,3,1), "Wells Fargo", "1990 initial buy (public record); exited ~2022 (public record)"),
    ("MCO", datetime.date(2000,1,1), None, "Moody's", "'Moody's in 2000' [2003 Letter]; still held (trimmed)"),
    ("IBM", datetime.date(2011,3,1), datetime.date(2018,1,1), "IBM", "'late to the IBM party' [2011 Letter]; fully exited ~2018 (public record)"),
    ("AAPL",datetime.date(2016,6,1), None, "Apple", "'we began buying Apple stock' 2016 [2020 Letter]; still largely held (trimmed 2024)"),
    ("BAC", datetime.date(2011,8,1), None, "Bank of America", "2011 preferred/warrant deal, converted to common 2017 (public record); still largely held (trimmed 2024)"),
]

bench = {t: load(t) for t in ["BRK-A","SPY"]}

rows = []
for ticker, entry, exit_, label, note in picks:
    series = load(ticker)
    entry_px, entry_actual = nearest(series, entry)
    exit_date = exit_ or TODAY
    exit_px, exit_actual = nearest(series, exit_date)
    years = (exit_actual - entry_actual).days / 365.25
    pick_cagr = cagr(entry_px, exit_px, years)
    pick_mult = exit_px/entry_px

    brk_entry, _ = nearest(bench["BRK-A"], entry)
    brk_exit, _ = nearest(bench["BRK-A"], exit_date)
    brk_cagr_match = cagr(brk_entry, brk_exit, years)

    spy_entry_d = max(entry, datetime.date(1993,2,1))
    spy_entry, _ = nearest(bench["SPY"], spy_entry_d)
    spy_exit, _ = nearest(bench["SPY"], exit_date)
    spy_years = (exit_actual - spy_entry_d).days/365.25
    spy_cagr_match = cagr(spy_entry, spy_exit, spy_years)

    rows.append({
        "ticker": ticker, "label": label, "entry": entry_actual.isoformat(),
        "exit": exit_actual.isoformat(), "years": round(years,1),
        "cagr": pick_cagr, "mult": pick_mult,
        "brk_cagr_match": brk_cagr_match, "spy_cagr_match": spy_cagr_match,
        "note": note
    })

print(f"{'Ticker':6} {'Entry':11} {'Exit':11} {'Yrs':>5} {'CAGR':>8} {'Mult':>9} {'BRK.A CAGR (same window)':>26} {'SPY CAGR (same window)':>24}")
for r in rows:
    print(f"{r['ticker']:6} {r['entry']:11} {r['exit']:11} {r['years']:5.1f} {r['cagr']*100:7.2f}% {r['mult']:8.1f}x {r['brk_cagr_match']*100:25.2f}% {r['spy_cagr_match']*100:23.2f}%")

import statistics
mean_cagr = statistics.mean(r['cagr'] for r in rows)
median_cagr = statistics.median(r['cagr'] for r in rows)
print()
print(f"Equal-weighted mean CAGR across {len(rows)} picks: {mean_cagr*100:.2f}%")
print(f"Median CAGR: {median_cagr*100:.2f}%")

json.dump(rows, open(r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad\buffett_picks_results.json","w"), indent=2)
