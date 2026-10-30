import json, os, csv, bisect, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
OUT = SCRATCH

wide = json.load(open(os.path.join(SCRATCH, "wide_universe.json")))
UNIVERSE = wide["tickers"]

REBAL_YEARS = list(range(2013, 2026))  # 2013..2025, June 30 each

NI_TAGS = ["NetIncomeLoss", "ProfitLoss"]
SHARES_TAGS = ["EntityCommonStockSharesOutstanding"]

def load_price_series(ticker):
    fn = os.path.join(CACHE, f"px_{ticker}.json")
    d = json.load(open(fn))
    res = d["chart"]["result"][0]
    ts = res["timestamp"]
    adj = res.get("indicators", {}).get("adjclose", [{}])[0].get("adjclose")
    close = res["indicators"]["quote"][0]["close"]
    series = {}
    for i, t in enumerate(ts):
        dt = datetime.datetime.utcfromtimestamp(t).date()
        val = None
        if adj and i < len(adj) and adj[i] is not None:
            val = adj[i]
        elif close[i] is not None:
            val = close[i]
        if val is not None:
            series[dt] = val
    return series

def nearest_price(series_sorted_dates, series, target_date, max_gap_days=10):
    idx = bisect.bisect_left(series_sorted_dates, target_date)
    candidates = []
    if idx < len(series_sorted_dates):
        candidates.append(series_sorted_dates[idx])
    if idx > 0:
        candidates.append(series_sorted_dates[idx-1])
    best = None
    best_gap = None
    for c in candidates:
        gap = abs((c - target_date).days)
        if best_gap is None or gap < best_gap:
            best_gap = gap
            best = c
    if best is None or best_gap > max_gap_days:
        return None
    return series[best]

def load_ni_facts(cik_data):
    gaap = cik_data.get("facts", {}).get("us-gaap", {})
    by_end = {}
    for tag in NI_TAGS:
        if tag not in gaap:
            continue
        for x in gaap[tag]["units"].get("USD", []):
            if x.get("form") not in ("10-K", "10-K/A"):
                continue
            start = x.get("start")
            end = x.get("end")
            filed = x.get("filed")
            if not (start and end and filed):
                continue
            sd = datetime.date.fromisoformat(start)
            ed = datetime.date.fromisoformat(end)
            if (ed - sd).days < 300 or (ed - sd).days > 380:
                continue
            fd = datetime.date.fromisoformat(filed)
            prev = by_end.get(ed)
            if prev is None or fd > prev[1]:
                by_end[ed] = (x["val"], fd, tag)
    return by_end

def load_shares(cik_data):
    dei = cik_data.get("facts", {}).get("dei", {})
    pts = []
    for tag in SHARES_TAGS:
        if tag not in dei:
            continue
        for x in dei[tag]["units"].get("shares", []):
            end = x.get("end")
            filed = x.get("filed")
            if not (end and filed):
                continue
            pts.append((datetime.date.fromisoformat(end), datetime.date.fromisoformat(filed), x["val"]))
    pts.sort()
    return pts

def shares_as_of(pts, asof):
    best = None
    for end, filed, val in pts:
        if filed <= asof:
            if best is None or filed > best[0]:
                best = (filed, val)
    return best[1] if best else None

def load_yields():
    rows = {}
    with open(os.path.join(CACHE, "dgs30.csv")) as f:
        r = csv.reader(f)
        header = next(r)
        for row in r:
            if len(row) < 2 or not row[0] or not row[1] or row[1] == ".":
                continue
            try:
                rows[datetime.date.fromisoformat(row[0])] = float(row[1])
            except ValueError:
                continue
    dates_sorted = sorted(rows.keys())
    return dates_sorted, rows

def yield_as_of(dates_sorted, rows, asof, max_gap=10):
    idx = bisect.bisect_right(dates_sorted, asof) - 1
    while idx >= 0 and (asof - dates_sorted[idx]).days > max_gap:
        idx -= 1
    if idx < 0:
        return None
    return rows[dates_sorted[idx]]

def main():
    y_dates, y_rows = load_yields()
    spy_series = load_price_series("SPY")
    spy_dates = sorted(spy_series.keys())

    results = []
    coverage_log = []

    for ticker in UNIVERSE:
        fn = os.path.join(CACHE, f"facts_{ticker}.json")
        pxfn = os.path.join(CACHE, f"px_{ticker}.json")
        if not (os.path.exists(fn) and os.path.exists(pxfn)):
            coverage_log.append((ticker, "ALL", "NO_DATA_FILE", None))
            continue
        try:
            cik_data = json.load(open(fn))
        except Exception:
            coverage_log.append((ticker, "ALL", "BAD_FACTS_JSON", None))
            continue
        ni_by_end = load_ni_facts(cik_data)
        shares_pts = load_shares(cik_data)
        try:
            price_series = load_price_series(ticker)
        except Exception:
            coverage_log.append((ticker, "ALL", "BAD_PRICE_JSON", None))
            continue
        price_dates = sorted(price_series.keys())

        for yr in REBAL_YEARS:
            asof = datetime.date(yr, 6, 30)
            known = [(end, val) for end, (val, filed, tag) in ni_by_end.items()
                     if filed <= asof and end <= asof]
            known.sort(key=lambda x: x[0])
            last5 = known[-5:]
            if len(last5) < 5:
                coverage_log.append((ticker, yr, "INSUFFICIENT_NI_HISTORY", len(last5)))
                continue
            worst5 = min(v for _, v in last5)

            shares = shares_as_of(shares_pts, asof)
            if shares is None:
                coverage_log.append((ticker, yr, "NO_SHARES_DATA", None))
                continue

            entry_px = nearest_price(price_dates, price_series, asof)
            if entry_px is None:
                coverage_log.append((ticker, yr, "NO_PRICE_AT_REBAL", None))
                continue

            mkt_cap = entry_px * shares
            yld = worst5 / mkt_cap
            hurdle = yield_as_of(y_dates, y_rows, asof)
            if hurdle is None:
                coverage_log.append((ticker, yr, "NO_YIELD_DATA", None))
                continue
            hurdle = max(hurdle / 100.0, 0.04)

            passed = yld >= hurdle

            fwd_date = datetime.date(yr + 1, 6, 30)
            fwd_px = nearest_price(price_dates, price_series, fwd_date)
            spy_entry = nearest_price(spy_dates, spy_series, asof)
            spy_fwd = nearest_price(spy_dates, spy_series, fwd_date)

            fwd_ret = None
            spy_ret = None
            if fwd_px is not None:
                fwd_ret = fwd_px / entry_px - 1.0
            if spy_entry is not None and spy_fwd is not None:
                spy_ret = spy_fwd / spy_entry - 1.0

            results.append({
                "ticker": ticker, "asof": asof.isoformat(), "worst5_ni": worst5,
                "mkt_cap": mkt_cap, "yield": yld, "hurdle": hurdle, "pass": passed,
                "entry_px": entry_px, "fwd_px": fwd_px, "fwd_ret": fwd_ret, "spy_ret": spy_ret,
            })

    with open(os.path.join(OUT, "bt_results_wide.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker","asof","worst5_ni","mkt_cap","yield","hurdle","pass","entry_px","fwd_px","fwd_ret","spy_ret"])
        for r in results:
            w.writerow([r["ticker"], r["asof"], r["worst5_ni"], r["mkt_cap"], f"{r['yield']:.4f}",
                        f"{r['hurdle']:.4f}", r["pass"], r["entry_px"], r["fwd_px"],
                        f"{r['fwd_ret']:.4f}" if r["fwd_ret"] is not None else "",
                        f"{r['spy_ret']:.4f}" if r["spy_ret"] is not None else ""])

    with open(os.path.join(OUT, "bt_coverage_log_wide.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ticker","year","reason","detail"])
        for row in coverage_log:
            w.writerow(row)

    print(f"Universe size: {len(UNIVERSE)}")
    print(f"Total screen-year observations: {len(results)}")
    print(f"Coverage failures logged: {len(coverage_log)}")
    passes = [r for r in results if r["pass"]]
    print(f"PASSES: {len(passes)}")

if __name__ == "__main__":
    main()
