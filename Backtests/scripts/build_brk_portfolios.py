import json, os, re, datetime, bisect, statistics, csv

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")

TICKER_MAP = [
    (r"COCA COLA", "KO"), (r"AMERICAN EXPRESS", "AXP"), (r"WELLS FARGO", "WFC"),
    (r"^APPLE\b", "AAPL"), (r"KRAFT HEINZ", "KHC"), (r"KRAFT FOODS", "KFT"),
    (r"MOODY", "MCO"), (r"PROCT[EO]R & GAMBLE", "PG"), (r"GILLETTE", "G"),
    (r"WASHINGTON POST", "GHC"), (r"BURLINGTON NORTHERN", "BNI"),
    (r"US BANCORP", "USB"), (r"^CITIGROUP", "C"), (r"CONOCO", "COP"),
    (r"PHILLIPS 66|^PHILLIPS$", "PSX"), (r"EXXON MOBIL", "XOM"),
    (r"OCCIDENTAL", "OXY"), (r"GOLDMAN SACHS", "GS"), (r"JPMORGAN", "JPM"),
    (r"CHEVRON", "CVX"),
    (r"BANK AMER", "BAC"), (r"BANK OF NEW YORK MELLON", "BK"),
    (r"M & T BANK|M&T BANK", "MTB"), (r"CHUBB", "CB"), (r"AMERIPRISE", "AMP"),
    (r"CHARTER COMMUNICATIONS", "CHTR"), (r"ACTIVISION", "ATVI"),
    (r"ALPHABET", "GOOGL"), (r"DAVITA", "DVA"), (r"DELTA AIR", "DAL"),
    (r"^DIRECTV", "DTV"), (r"DUN & BRADSTREET", "DNB"), (r"^HCA\b", "HCA"),
    (r"^HP INC", "HPQ"), (r"INTERNATIONAL BUSINESS MACH|INTER-?\s*NATIONAL BUSINESS", "IBM"),
    (r"JOHNSON & JOHNSON", "JNJ"), (r"SUN TRUST", "STI"), (r"VERIZON", "VZ"),
    (r"WAL[- ]?MART", "WMT"), (r"^GATX", "GATX"), (r"BLOCK H ?& ?R", "HRB"),
    (r"JONES APPAREL", "JNY"), (r"SHAW COMMUNI", "SJR"),
    (r"WESCO FINL", None),  # Berkshire's own majority-owned subsidiary -- excluded, not a 3rd-party pick
    (r"PS GROUP HOLDINGS", None),  # too small/obscure to reliably resolve
    (r"AMERICAN STANDARD", None),  # 2007-08 breakup (Trane/Ideal Standard/WABCO) -- too complex for this pass
    (r"ANHEUSER", None),  # acquired by InBev 2008 -- delisted, not resolved this pass
]

def resolve(issuer):
    name = re.sub(r"\.{2,}", "", issuer)
    name = re.sub(r"\b\d+(,\s*\d+)*\s*$", "", name)  # trailing footnote refs only
    name = re.sub(r"[.,]", "", name)
    name = re.sub(r"\s+", " ", name).strip().upper()
    for pattern, ticker in TICKER_MAP:
        if re.search(pattern, name):
            return ticker
    return None

def load_monthly(ticker):
    fn = os.path.join(CACHE, f"pxlong_{ticker}.json")
    if not os.path.exists(fn):
        return None
    try:
        d = json.load(open(fn))
        res = d["chart"]["result"]
        if not res:
            return None
        res = res[0]
    except Exception:
        return None
    if "timestamp" not in res or "indicators" not in res:
        return None
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

def nearest(series, target, max_gap=45):
    if not series:
        return None
    dates = sorted(series.keys())
    idx = bisect.bisect_left(dates, target)
    cands = []
    if idx < len(dates): cands.append(dates[idx])
    if idx > 0: cands.append(dates[idx-1])
    if not cands:
        return None
    best = min(cands, key=lambda d: abs((d-target).days))
    if abs((best-target).days) > max_gap:
        return None
    return series[best]

d = json.load(open(os.path.join(SCRATCH, "brk_13f_all_years.json")))
years = sorted(d.keys())

# resolve top-10 by value each year, normalize units
year_tops = {}
unresolved_log = []
for y in years:
    mult = 1 if int(y) >= 2022 else 1000
    top10 = d[y]["holdings"][:10]
    resolved = []
    for h in top10:
        t = resolve(h["issuer"])
        val = h["value"] * mult
        if t is None:
            unresolved_log.append((y, h["issuer"], val))
            continue
        resolved.append({"ticker": t, "issuer": h["issuer"], "value": val})
    year_tops[y] = resolved

price_cache = {}
def get_series(t):
    if t not in price_cache:
        price_cache[t] = load_monthly(t)
    return price_cache[t]

# --- Portfolio construction: annual reconstitution, Dec 31 of each year ---
def run_portfolio(weight_mode, topn):
    """weight_mode: 'equal' or 'value'. Returns list of {year, ret} annual returns
    and coverage gaps."""
    annual_rets = []
    gaps = []
    for i in range(len(years) - 1):
        y0, y1 = years[i], years[i+1]
        d0 = datetime.date(int(y0), 12, 31)
        d1 = datetime.date(int(y1), 12, 31)
        holdings = year_tops[y0][:topn]
        if not holdings:
            continue
        total_val = sum(h["value"] for h in holdings) if weight_mode == "value" else None
        weighted_rets = []
        weights_used = []
        for h in holdings:
            series = get_series(h["ticker"])
            p0 = nearest(series, d0)
            p1 = nearest(series, d1)
            if p0 is None or p1 is None:
                gaps.append((y0, y1, h["ticker"], "NO_PRICE"))
                continue
            r = p1/p0 - 1.0
            w = (h["value"]/total_val) if weight_mode == "value" else (1.0/len(holdings))
            weighted_rets.append(r)
            weights_used.append(w)
        if not weighted_rets:
            gaps.append((y0, y1, "ALL", "NO_HOLDINGS_PRICED"))
            continue
        wsum = sum(weights_used)
        port_ret = sum(r*w for r, w in zip(weighted_rets, weights_used)) / wsum
        annual_rets.append({"year": y1, "ret": port_ret, "n": len(weighted_rets)})
    return annual_rets, gaps

def cagr_from_annual(annual_rets):
    mult = 1.0
    for a in annual_rets:
        mult *= (1 + a["ret"])
    n = len(annual_rets)
    return mult**(1/n) - 1, mult

spy_series = get_series("SPY") or {}
brk_series = get_series("BRK-A") or {}

def bench_annual_rets(series):
    rets = []
    for i in range(len(years)-1):
        d0 = datetime.date(int(years[i]), 12, 31)
        d1 = datetime.date(int(years[i+1]), 12, 31)
        p0, p1 = nearest(series, d0), nearest(series, d1)
        if p0 and p1:
            rets.append(p1/p0 - 1.0)
    mult = 1.0
    for r in rets: mult *= (1+r)
    return mult**(1/len(rets)) - 1, mult, len(rets)

spy_cagr, spy_mult, spy_n = bench_annual_rets(spy_series)
brk_cagr, brk_mult, brk_n = bench_annual_rets(brk_series)

print(f"Benchmark SPY 1999-2025 (n={spy_n} yrs): CAGR {spy_cagr*100:.2f}%, total mult {spy_mult:.1f}x")
print(f"Benchmark BRK.A 1999-2025 (n={brk_n} yrs): CAGR {brk_cagr*100:.2f}%, total mult {brk_mult:.1f}x")
print()

results = {}
for weight_mode in ["equal", "value"]:
    for topn in [5, 10]:
        rets, gaps = run_portfolio(weight_mode, topn)
        cagr, mult = cagr_from_annual(rets)
        key = f"top{topn}_{weight_mode}"
        results[key] = {"cagr": cagr, "mult": mult, "n_years": len(rets), "n_gaps": len(gaps)}
        print(f"{key:20} CAGR {cagr*100:6.2f}%  total mult {mult:8.1f}x  years={len(rets)}  coverage_gaps={len(gaps)}")

print()
print("Unresolved top-10 issuer name-years (logged, not silently dropped):", len(unresolved_log))
for u in unresolved_log[:20]:
    print(" ", u)

json.dump({"results": results, "unresolved": unresolved_log, "spy_cagr": spy_cagr, "brk_cagr": brk_cagr},
          open(os.path.join(SCRATCH, "brk_portfolio_results.json"), "w"), indent=2, default=str)

# Save the full resolved top-10 holdings per year for the record
with open(os.path.join(SCRATCH, "brk_13f_top10_resolved.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["year","rank","issuer","ticker","value_usd"])
    for y in years:
        for i, h in enumerate(d[y]["holdings"][:10]):
            mult = 1 if int(y) >= 2022 else 1000
            t = resolve(h["issuer"])
            w.writerow([y, i+1, h["issuer"], t or "UNRESOLVED", h["value"]*mult])
