import json, os, csv, bisect, datetime, sys

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
FAILURES_CACHE = os.path.join(CACHE, "failures")

REBAL = datetime.date(2018, 6, 30)
TODAY = datetime.date(2026, 7, 22)

# ticker -> (exit_ticker_or_None, ratio, fixed_cash_or_None)
# fixed_cash overrides everything (all-cash deal / bankruptcy)
SPECIAL = {
    "BIG":  (None, None, 0.00),      # Chapter 7, common equity cancelled, $0 recovery
    "JWN":  (None, None, 24.25),     # taken private, May 2025, all cash
    "TGNA": (None, None, 22.00),     # acquired by Nexstar, closed Mar 2026, all cash
    "PDCO": (None, None, 31.35),     # taken private by Patient Square Capital, Apr 2025, all cash
    "PBCT": ("MTB", 0.118, None),    # merged into M&T Bank, Apr 2022, stock-for-stock
    "STI":  ("TFC", 1.295, None),    # merged into BB&T/Truist, Dec 2019, stock-for-stock
    "RTN":  ("RTX", 2.3348, None),   # merged into United Technologies (renamed RTX), Apr 2020
    "SLM":  ("SLM", 1.0, None),      # Navient spinoff (2014) predates entry date; just track SLM itself
    "SAI":  ("SAIC", 1.0, None),     # ticker rename (old ticker SAI -> SAIC), same entity
    "GT":   ("GT", 1.0, None),       # fate mislabeled ACQUIRED; still independently trading
    "ACE":  ("CB", 1.0, None),       # ACE Ltd renamed Chubb Ltd, Jan 2016, same entity/shares
}

NI_TAGS = ["NetIncomeLoss", "ProfitLoss"]
SHARES_TAGS = ["EntityCommonStockSharesOutstanding"]
FALLBACK_SHARES_TAGS = ["CommonStockSharesOutstanding", "CommonStockSharesIssued",
                        "WeightedAverageNumberOfDilutedSharesOutstanding",
                        "WeightedAverageNumberOfSharesOutstandingBasic",
                        "WeightedAverageNumberOfShareOutstandingBasicAndDiluted"]

def _load_one_series(p):
    try:
        d = json.load(open(p))
        res = d["chart"]["result"]
        if not res or "timestamp" not in res[0]:
            return None
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
        return series if series else None
    except Exception:
        return None

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
    """Most recent available price in cached series (our proxy for 'today')."""
    best = None
    for base in (CACHE, FAILURES_CACHE):
        for prefix in ("pxlong_", "px_"):
            p = os.path.join(base, f"{prefix}{ticker}.json")
            if os.path.exists(p):
                series = _load_one_series(p)
                if series:
                    d = max(series.keys())
                    if best is None or d > best[0]:
                        best = (d, series[d])
    return best  # (date, price) or None

def entry_price(ticker):
    for base in (CACHE, FAILURES_CACHE):
        for prefix in ("px_", "pxlong_"):
            p = os.path.join(base, f"{prefix}{ticker}.json")
            if os.path.exists(p):
                series = _load_one_series(p)
                if series:
                    px = nearest(series, REBAL, max_gap=20)
                    if px is not None:
                        return px, False
    tenk_fn = os.path.join(SCRATCH, "10k_implied_prices.json")
    if os.path.exists(tenk_fn):
        tenk = json.load(open(tenk_fn))
        if ticker in tenk:
            r = tenk[ticker]
            d = r.get("amv_date")
            if d:
                point_date = datetime.date.fromisoformat(d)
                if abs((point_date - REBAL).days) <= 130:
                    return r["implied_price"], True
    return None, False

rows = list(csv.DictReader(open(os.path.join(SCRATCH, "sp500_2013_screen_results.csv"))))
passed = [r["ticker"] for r in rows if r["passed"] == "True"]
print(f"Passed screen as of {REBAL}: {len(passed)} names")

results = []
missing = []
for t in passed:
    ep, ep_from_10k = entry_price(t)
    if ep is None:
        missing.append((t, "NO_ENTRY_PRICE"))
        continue

    if t in SPECIAL:
        exit_t, ratio, fixed_cash = SPECIAL[t]
    else:
        exit_t, ratio, fixed_cash = t, 1.0, None

    if fixed_cash is not None:
        exit_val = fixed_cash
        exit_date = "deal-close"
    else:
        lp = latest_price(exit_t)
        if lp is None:
            missing.append((t, f"NO_EXIT_PRICE ({exit_t})"))
            continue
        exit_date, px = lp
        exit_val = px * ratio

    total_return = exit_val / ep - 1.0
    years = (TODAY - REBAL).days / 365.25
    cagr = (1 + total_return) ** (1/years) - 1
    results.append({
        "ticker": t, "exit_ticker": exit_t, "entry_px": ep, "entry_from_10k": ep_from_10k,
        "exit_val": exit_val, "exit_date": str(exit_date), "total_return": total_return, "cagr": cagr,
    })

print(f"\nComputed returns for {len(results)} / {len(passed)}")
print(f"Missing: {len(missing)}")
for m in missing:
    print("  ", m)

with open(os.path.join(SCRATCH, "portfolio_returns.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker","exit_ticker","entry_px","entry_from_10k","exit_val","exit_date","total_return","cagr"])
    for r in results:
        w.writerow([r["ticker"], r["exit_ticker"], r["entry_px"], r["entry_from_10k"],
                    r["exit_val"], r["exit_date"], r["total_return"], r["cagr"]])

# Portfolio-level stats: equal-weight, buy-and-hold, no rebalancing
rets = [r["total_return"] for r in results]
avg_total_return = sum(rets) / len(rets)
years = (TODAY - REBAL).days / 365.25
port_cagr = (1 + avg_total_return) ** (1/years) - 1

print(f"\n=== EQUAL-WEIGHT PORTFOLIO ({len(results)} names, {REBAL} -> {TODAY}, {years:.2f} yrs) ===")
print(f"Average total return: {avg_total_return*100:.1f}%")
print(f"Portfolio CAGR (price return only, no dividends): {port_cagr*100:.2f}%")

winners = sum(1 for r in rets if r > 0)
losers = sum(1 for r in rets if r <= 0)
print(f"Winners: {winners} / {len(rets)}  Losers: {losers} / {len(rets)}")

worst5 = sorted(results, key=lambda r: r["total_return"])[:5]
best5 = sorted(results, key=lambda r: -r["total_return"])[:5]
print("\nWorst 5:")
for r in worst5:
    print(f"  {r['ticker']:6s} {r['total_return']*100:8.1f}%  entry=${r['entry_px']:.2f} exit=${r['exit_val']:.2f} ({r['exit_ticker']})")
print("Best 5:")
for r in best5:
    print(f"  {r['ticker']:6s} {r['total_return']*100:8.1f}%  entry=${r['entry_px']:.2f} exit=${r['exit_val']:.2f} ({r['exit_ticker']})")

# SPY benchmark over the identical window
spy_entry, _ = entry_price("SPY")
spy_exit = latest_price("SPY")
if spy_entry and spy_exit:
    spy_total = spy_exit[1] / spy_entry - 1.0
    spy_cagr = (1 + spy_total) ** (1/years) - 1
    print(f"\n=== SPY BENCHMARK, same window ===")
    print(f"SPY entry ${spy_entry:.2f} ({REBAL}) -> exit ${spy_exit[1]:.2f} ({spy_exit[0]})")
    print(f"SPY total return: {spy_total*100:.1f}%  SPY CAGR: {spy_cagr*100:.2f}%")
    print(f"\nPortfolio CAGR minus SPY CAGR: {(port_cagr-spy_cagr)*100:+.2f} pts/yr (price return only, no dividends either side)")
else:
    print("\nSPY price data missing for entry or exit")
