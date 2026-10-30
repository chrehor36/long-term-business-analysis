import json, os, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")

SURV_2020 = ["BKNG","ORLY","GOOG","FOXA","LRCX","CME","CMCSA","AFL","PNC","CSX","MA","AAPL"]
SURV_2016 = ["NVDA","BKNG","ORLY","CSX","AAPL","CME","MA","NEE","AFL","FAST","MPC","KEY","PSX","APH","PCAR","NDAQ","DOV","PNC","CMI"]

def load_series(t):
    d = json.load(open(os.path.join(CACHE, f"px_{t}.json")))
    r = d["chart"]["result"][0]
    ts = r["timestamp"]
    adj = r["indicators"]["adjclose"][0]["adjclose"]
    out = []
    for i, tstamp in enumerate(ts):
        if adj[i] is None:
            continue
        dt = datetime.date.fromtimestamp(tstamp)
        out.append((dt, adj[i]))
    out.sort()
    return out

def price_on_or_after(series, target):
    for dt, px in series:
        if dt >= target:
            return dt, px
    return None, None

def price_latest(series):
    return series[-1]

def compute(tickers, anchor_str, label):
    anchor = datetime.date.fromisoformat(anchor_str)
    today = datetime.date.today()
    years = (today - anchor).days / 365.25
    results = []
    for t in tickers:
        series = load_series(t)
        entry_dt, entry_px = price_on_or_after(series, anchor)
        exit_dt, exit_px = price_latest(series)
        total_return = exit_px / entry_px
        cagr = total_return ** (1/years) - 1
        results.append({
            "ticker": t, "entry_date": str(entry_dt), "entry_px": round(entry_px,2),
            "exit_date": str(exit_dt), "exit_px": round(exit_px,2),
            "total_return_x": round(total_return,3), "cagr_pct": round(cagr*100,2)
        })
    spy_series = load_series("SPY")
    spy_entry_dt, spy_entry_px = price_on_or_after(spy_series, anchor)
    spy_exit_dt, spy_exit_px = price_latest(spy_series)
    spy_total = spy_exit_px / spy_entry_px
    spy_cagr = spy_total ** (1/years) - 1
    print(f"\n=== {label} (anchor {anchor}, {years:.2f} yrs to {today}) ===")
    print(f"SPY: entry {spy_entry_dt} ${spy_entry_px:.2f} -> exit {spy_exit_dt} ${spy_exit_px:.2f} = {spy_total:.3f}x, CAGR {spy_cagr*100:.2f}%")
    for r in sorted(results, key=lambda x: -x["cagr_pct"]):
        print(f"  {r['ticker']:6s} entry {r['entry_date']} ${r['entry_px']:>9.2f} -> exit ${r['exit_px']:>9.2f}  {r['total_return_x']:>6.2f}x  CAGR {r['cagr_pct']:>7.2f}%")
    json.dump({"anchor": anchor_str, "years": years, "spy": {"entry_date": str(spy_entry_dt), "entry_px": spy_entry_px, "exit_date": str(spy_exit_dt), "exit_px": spy_exit_px, "total_return_x": spy_total, "cagr_pct": spy_cagr*100}, "survivors": results},
              open(os.path.join(SCRATCH, f"bt14_returns_{label}.json"), "w"), indent=1)
    return results, (spy_total, spy_cagr, years)

r2020, spy2020 = compute(SURV_2020, "2020-06-30", "2020")
r2016, spy2016 = compute(SURV_2016, "2016-06-30", "2016")
