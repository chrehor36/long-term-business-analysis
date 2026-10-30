import csv, os, json, datetime, bisect

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
REBAL = datetime.date(1993, 12, 31)
WINDOW_YEARS = {"1989", "1990", "1991", "1992", "1993"}

rows = list(csv.DictReader(open(os.path.join(SCRATCH, "sfd_master.csv"))))
by_ticker = {}
for r in rows:
    if r["fiscal_year"] and r["fiscal_year"] != "UNKNOWN":
        by_ticker.setdefault(r["ticker"], []).append(r)

def to_float(s):
    if not s:
        return None
    try:
        return float(s.replace(",", ""))
    except ValueError:
        return None

def unit_mult(unit):
    u = (unit or "").lower()
    if "million" in u:
        return 1_000_000
    if "thousand" in u:
        return 1_000
    return 1  # "as reported" -- assume already in dollars

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

def split_multiplier_since(fn, target):
    """Yahoo's price series is split-adjusted forward to today -- a price
    quoted for a 1990s date has already been divided by every split that
    happened AFTER that date. To recover the real, as-traded historical
    price (needed to multiply by the REAL historical share count from the
    filing, not a modern-equivalent count), multiply back by the product
    of every split ratio that occurred after the target date."""
    try:
        d = json.load(open(fn))
        events = d["chart"]["result"][0].get("events", {})
        splits = events.get("splits", {})
    except Exception:
        return 1.0
    mult = 1.0
    for s in splits.values():
        split_date = datetime.datetime.utcfromtimestamp(s["date"]).date()
        if split_date > target:
            mult *= s["numerator"] / s["denominator"]
    return mult

def price_near(ticker, target, max_gap=20):
    for prefix in ("pxfull_", "px_", "pxlong_"):
        fn = os.path.join(CACHE, f"{prefix}{ticker}.json")
        if os.path.exists(fn):
            try:
                s = load_series(fn)
                dates = sorted(s.keys())
                idx = bisect.bisect_left(dates, target)
                cands = []
                if idx < len(dates): cands.append(dates[idx])
                if idx > 0: cands.append(dates[idx-1])
                if cands:
                    best = min(cands, key=lambda d: abs((d-target).days))
                    if abs((best-target).days) <= max_gap:
                        mult = split_multiplier_since(fn, target)
                        return s[best] * mult
            except Exception:
                pass
    return None

def load_yields():
    rows = {}
    with open(os.path.join(CACHE, "dgs30.csv")) as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 2 or not row[0] or not row[1] or row[1] == ".":
                continue
            try:
                rows[datetime.date.fromisoformat(row[0])] = float(row[1])
            except ValueError:
                continue
    return sorted(rows.keys()), rows

def yield_as_of(dates_sorted, rows, asof, max_gap=10):
    idx = bisect.bisect_right(dates_sorted, asof) - 1
    while idx >= 0 and (asof - dates_sorted[idx]).days > max_gap:
        idx -= 1
    return rows[dates_sorted[idx]] if idx >= 0 else None

y_dates, y_rows = load_yields()
hurdle = max(yield_as_of(y_dates, y_rows, REBAL) / 100.0, 0.04)
print(f"Sovereign 30-yr yield as of {REBAL}: {hurdle*100:.2f}%  (floored at 4%)")

results = []
gaps = []
for t, recs in sorted(by_ticker.items()):
    # NI by year, in real dollars
    ni_by_year = {}
    for r in recs:
        y = r["fiscal_year"][:4]
        ni = to_float(r["net_income"])
        if ni is None:
            continue
        ni_by_year[y] = ni * unit_mult(r["unit"])

    covered = sorted(set(ni_by_year) & WINDOW_YEARS)
    if len(covered) < 3:
        gaps.append((t, f"INSUFFICIENT_NI_HISTORY ({len(covered)} yrs in 1989-1993 window)"))
        continue
    worst_ni = min(ni_by_year[y] for y in covered)

    # shares: direct disclosure preferred (most recent year), else derive NI/EPS
    shares = None
    shares_derived = False
    for r in sorted(recs, key=lambda r: r["fiscal_year"], reverse=True):
        so = to_float(r["shares_outstanding"])
        if so:
            # share counts follow the same table-wide unit caption as dollar
            # figures in these old filings (e.g. "in thousands, except per
            # share amounts" applies to the shares line too) -- same
            # multiplier as net_income, not a magnitude-based guess
            shares = so * unit_mult(r["unit"])
            break
    if shares is None:
        for r in recs:
            ni = to_float(r["net_income"])
            eps = to_float(r["eps"])
            if ni and eps and eps != 0:
                shares = (ni * unit_mult(r["unit"])) / eps
                shares_derived = True
                break
    if shares is None or shares <= 0:
        gaps.append((t, "NO_SHARES_DATA"))
        continue

    px = price_near(t, REBAL)
    if px is None:
        gaps.append((t, "NO_PRICE"))
        continue

    # Sanity check: cross-validate the (possibly split-adjustment-corrupted)
    # price against the P/E ratio implied by the most recent disclosed EPS.
    # A price recovered correctly should imply a plausible P/E (roughly
    # 3-60x covers virtually any real 1990s-era stock, including deep
    # value and high-growth names); a price still silently corrupted by an
    # unrecorded stock split (seen for MO, PFE -- Yahoo's cached event data
    # is simply missing their real historical splits) produces an
    # obviously-impossible P/E instead of a wrong-but-plausible one.
    latest_eps = None
    for r in sorted(recs, key=lambda r: r["fiscal_year"], reverse=True):
        e = to_float(r["eps"])
        if e and e > 0:
            latest_eps = e
            break
    if latest_eps:
        implied_pe = px / latest_eps
        if not (3.0 <= implied_pe <= 60.0):
            gaps.append((t, f"PRICE_SANITY_FAIL (implied P/E {implied_pe:.1f}x -- likely an unrecorded stock split Yahoo's cached events are missing)"))
            continue

    mkt_cap = px * shares
    if mkt_cap <= 0:
        gaps.append((t, "BAD_MARKET_CAP"))
        continue
    yld = worst_ni / mkt_cap
    passed = yld >= hurdle

    results.append({
        "ticker": t, "worst_ni": worst_ni, "years_covered": len(covered),
        "shares": shares, "shares_derived": shares_derived, "price": px,
        "mkt_cap": mkt_cap, "yield": yld, "passed": passed,
    })

print(f"\nScreened: {len(results)} / {len(by_ticker)}")
print(f"Coverage gaps: {len(gaps)}")
passes = [r for r in results if r["passed"]]
print(f"PASSES: {len(passes)}")

with open(os.path.join(SCRATCH, "screen_1990s_results.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker","worst_ni","years_covered","shares","shares_derived","price","mkt_cap","yield","passed"])
    for r in results:
        w.writerow([r["ticker"], r["worst_ni"], r["years_covered"], r["shares"], r["shares_derived"],
                    r["price"], r["mkt_cap"], r["yield"], r["passed"]])

with open(os.path.join(SCRATCH, "screen_1990s_gaps.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker","reason"])
    for t, reason in gaps:
        w.writerow([t, reason])

print("\nPassers by yield:")
for r in sorted(passes, key=lambda r: -r["yield"]):
    print(f"  {r['ticker']:6s} yield={r['yield']*100:6.2f}%  mkt_cap=${r['mkt_cap']/1e9:.2f}B  {'(shares derived)' if r['shares_derived'] else ''}")
