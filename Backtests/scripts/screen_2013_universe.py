import json, os, csv, bisect, datetime

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
FAILURES_CACHE = os.path.join(CACHE, "failures")

import sys
REBAL = datetime.date(2013, 6, 30) if len(sys.argv) < 2 else datetime.date.fromisoformat(sys.argv[1])
NI_TAGS = ["NetIncomeLoss", "ProfitLoss"]
SHARES_TAGS = ["EntityCommonStockSharesOutstanding"]

recon = json.load(open(os.path.join(SCRATCH, "sp500_2013_reconstruction.json")))
universe = recon["reconstructed_tickers"]

fates = json.load(open(os.path.join(SCRATCH, "sp500_2013_fates_final.json")))
still_in = set(recon["still_in_index_today"])

def facts_path(t):
    for base in (CACHE, FAILURES_CACHE):
        p = os.path.join(base, f"facts_{t}.json")
        if os.path.exists(p):
            return p
    return None

def load_ni_facts(cik_data):
    gaap = cik_data.get("facts", {}).get("us-gaap", {})
    by_end = {}
    for tag in NI_TAGS:
        if tag not in gaap:
            continue
        for x in gaap[tag]["units"].get("USD", []):
            if x.get("form") not in ("10-K", "10-K/A"):
                continue
            start, end, filed = x.get("start"), x.get("end"), x.get("filed")
            if not (start and end and filed):
                continue
            sd, ed = datetime.date.fromisoformat(start), datetime.date.fromisoformat(end)
            if (ed - sd).days < 300 or (ed - sd).days > 380:
                continue
            fd = datetime.date.fromisoformat(filed)
            prev = by_end.get(ed)
            # keep the EARLIEST filed value per fiscal end, not the latest --
            # a later "filed" date is usually just that year's figure being
            # re-disclosed as a comparative in a subsequent 10-K. Keeping the
            # latest was defeating the whole point of the filed<=REBAL
            # point-in-time filter: it discarded the originally-timely filing
            # in favor of a re-statement date years later, which then failed
            # the filter even though the company reported on time (this was
            # silently starving GOOG/DIS/BLK/MDT/etc of otherwise-available
            # history).
            if prev is None or fd < prev[1]:
                by_end[ed] = (x["val"], fd, tag)
    return by_end

FALLBACK_SHARES_TAGS = ["CommonStockSharesOutstanding", "CommonStockSharesIssued",
                        "WeightedAverageNumberOfDilutedSharesOutstanding",
                        "WeightedAverageNumberOfSharesOutstandingBasic",
                        "WeightedAverageNumberOfShareOutstandingBasicAndDiluted"]

def _collect_shares(tagset, tags):
    pts = []
    for tag in tags:
        if tag not in tagset:
            continue
        for x in tagset[tag]["units"].get("shares", []):
            end, filed, val = x.get("end"), x.get("filed"), x.get("val")
            # val==0 shows up in some filers' stale/placeholder XBRL points
            # (e.g. SPG's 2010 10-K) -- treating it as real would make a
            # company's market cap compute to zero, not a coverage gap
            if not (end and filed) or not val:
                continue
            pts.append((datetime.date.fromisoformat(end), datetime.date.fromisoformat(filed), val))
    return pts

def load_shares(cik_data, asof):
    # A tag counts as usable only if it has a point actually available as of
    # our target date -- a non-empty series that's all stale (e.g. SPG's
    # primary dei tag only has 4 points, all from 2009-2010) must NOT block
    # fallback tags from being tried, which the old "if pts: return" logic did.
    dei = cik_data.get("facts", {}).get("dei", {})
    pts = _collect_shares(dei, SHARES_TAGS)
    if pts and any(filed <= asof for _, filed, _ in pts):
        pts.sort()
        return pts, False
    # fallback: no usable point-in-time EntityCommonStockSharesOutstanding
    # point -- use the most-precise available us-gaap share-count series
    # instead (balance-sheet point-in-time tags first, then weighted-average
    # as a last resort approximation -- flagged as such, not silently
    # treated as equally precise)
    gaap = cik_data.get("facts", {}).get("us-gaap", {})
    for tag in FALLBACK_SHARES_TAGS:
        pts2 = _collect_shares(gaap, [tag])
        if pts2 and any(filed <= asof for _, filed, _ in pts2):
            pts2.sort()
            return pts2, True
    return [], False

def shares_as_of(pts, asof):
    best = None
    for end, filed, val in pts:
        if filed <= asof:
            if best is None or filed > best[0]:
                best = (filed, val)
    return best[1] if best else None

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

def price_near(ticker, target):
    """Try each price source in order; use the FIRST one that actually has
    a point close enough to the target date, not just the first non-empty
    series (a real Yahoo file that only covers years outside our window
    would otherwise silently block the 10-K fallback from ever being
    tried)."""
    for base in (CACHE, FAILURES_CACHE):
        for prefix in ("px_", "pxlong_"):
            p = os.path.join(base, f"{prefix}{ticker}.json")
            if os.path.exists(p):
                series = _load_one_series(p)
                if series:
                    px = nearest(series, target, max_gap=20)
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
                # 130d not 100d: a 10-K's AMV date is defined relative to the
                # filer's OWN fiscal 2nd quarter, not calendar June 30 -- a
                # company with an off-calendar fiscal year (e.g. PDCO, FYE
                # April) can legitimately report an AMV date ~4mo from our
                # target without that being a data-quality problem.
                if abs((point_date - target).days) <= 130:
                    return r["implied_price"], True
    return None, False

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
print(f"Hurdle as of {REBAL}: {hurdle*100:.2f}%")

results = []
coverage_gaps = []
for t in universe:
    fp = facts_path(t)
    if fp is None:
        coverage_gaps.append((t, "NO_XBRL_DATA"))
        continue
    try:
        cik_data = json.load(open(fp))
    except Exception:
        coverage_gaps.append((t, "BAD_JSON"))
        continue

    ni_by_end = load_ni_facts(cik_data)
    known = [(end, val) for end, (val, filed, tag) in ni_by_end.items()
             if filed <= REBAL and end <= REBAL]
    known.sort(key=lambda x: x[0])
    last5 = known[-5:]
    if len(last5) < 5:
        coverage_gaps.append((t, f"INSUFFICIENT_NI_HISTORY ({len(last5)} yrs)"))
        continue
    worst5 = min(v for _, v in last5)

    shares_pts, shares_approx = load_shares(cik_data, REBAL)
    shares = shares_as_of(shares_pts, REBAL)
    entry_px, from_10k = price_near(t, REBAL)

    mkt_cap = None
    yld = None
    passed = None
    if shares and entry_px:
        mkt_cap = entry_px * shares
        yld = worst5 / mkt_cap
        passed = yld >= hurdle
    elif worst5 < 0:
        # negative worst-5yr -- range-anchoring auto-fail, no price needed
        passed = False
        yld = None
    else:
        coverage_gaps.append((t, "NO_PRICE_OR_SHARES_BUT_POSITIVE_NI"))
        continue

    results.append({
        "ticker": t, "worst5_ni": worst5, "yld": yld, "mkt_cap": mkt_cap,
        "passed": passed, "still_in_index_today": t in still_in,
        "fate": fates.get(t, "STILL_IN_INDEX" if t in still_in else "UNKNOWN"),
        "shares_approx": shares_approx if (shares and entry_px) else False,
    })

print(f"\nScreened: {len(results)} / {len(universe)}")
print(f"Coverage gaps: {len(coverage_gaps)}")
passes = [r for r in results if r["passed"]]
print(f"PASSES: {len(passes)}")

with open(os.path.join(SCRATCH, "sp500_2013_screen_results.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker", "worst5_ni", "yield", "mkt_cap", "passed", "still_in_index_today", "fate", "shares_approx"])
    for r in results:
        w.writerow([r["ticker"], r["worst5_ni"], r["yld"], r["mkt_cap"], r["passed"],
                    r["still_in_index_today"], r["fate"], r["shares_approx"]])

with open(os.path.join(SCRATCH, "sp500_2013_coverage_gaps.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticker", "reason"])
    for t, reason in coverage_gaps:
        w.writerow([t, reason])

# --- the actual discrimination test ---
BAD_FATES = {"FAILED", "SEVERELY_IMPAIRED"}
tp = sum(1 for r in results if not r["passed"] and r["fate"] in BAD_FATES)  # correctly avoided
fp_ = sum(1 for r in results if r["passed"] and r["fate"] in BAD_FATES)     # dangerous false positive
fn = sum(1 for r in results if not r["passed"] and r["fate"] not in BAD_FATES)  # missed a fine name
tn = sum(1 for r in results if r["passed"] and r["fate"] not in BAD_FATES)  # passed a fine name

print("\n=== DISCRIMINATION TEST ===")
print(f"Correctly avoided (FAIL screen, bad fate):   {tp}")
print(f"DANGEROUS false positive (PASS screen, bad fate): {fp_}")
print(f"Missed but harmless (FAIL screen, fine fate): {fn}")
print(f"Passed and fine (PASS screen, fine fate):     {tn}")

bad_total = tp + fp_
print(f"\nOf {bad_total} bad-fate names with usable data, the screen avoided {tp} ({100*tp/bad_total if bad_total else 0:.1f}%)")

if fp_ > 0:
    print("\nDANGEROUS FALSE POSITIVES (screen said pass, but it later failed/was impaired):")
    for r in results:
        if r["passed"] and r["fate"] in BAD_FATES:
            print(f"  {r['ticker']}: yield={r['yld']*100 if r['yld'] else None:.2f}% fate={r['fate']}")
