import json, os, csv, datetime, bisect, random, statistics, sys

SCRATCH = r"C:\Users\chreh\AppData\Local\Temp\claude\c--Users-chreh-OneDrive-Documents-BRK\e482e324-36bc-46f9-aaa9-08c4a48da963\scratchpad"
CACHE = os.path.join(SCRATCH, "bt_cache")
TODAY = datetime.date(2026, 7, 22)
FLOOR = datetime.date(1985, 1, 1)  # the practical data ceiling, per user decision

RUN_SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1

def load_series(ticker):
    fn = os.path.join(CACHE, f"pxlong_{ticker}.json")
    if not os.path.exists(fn):
        return None
    d = json.load(open(fn))
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
    return series

def first_date(series):
    return min(series.keys()) if series else None

def nearest(series, target, max_gap=45):
    dates = sorted(series.keys())
    idx = bisect.bisect_left(dates, target)
    cands = []
    if idx < len(dates): cands.append(dates[idx])
    if idx > 0: cands.append(dates[idx-1])
    if not cands: return None
    best = min(cands, key=lambda d: abs((d-target).days))
    if abs((best-target).days) > max_gap: return None
    return series[best]

# ---- Build the universe pool: every ticker this session has identified as
# framework-relevant (ever passed the mechanical screen, a Buffett actual
# pick, or a resolved Berkshire 13F top-10 holding), deduped ----
pool = set()
for row in csv.DictReader(open(os.path.join(SCRATCH, "screen_portfolios_per_ticker.csv"))):
    pool.add(row["ticker"])
for row in csv.DictReader(open(os.path.join(SCRATCH, "brk_13f_top10_resolved.csv"))):
    if row["ticker"] != "UNRESOLVED":
        pool.add(row["ticker"])
for p in json.load(open(os.path.join(SCRATCH, "buffett_picks_results.json"))):
    pool.add(p["ticker"])
pool.discard("SPY")
pool.discard("BRK-A")
pool.discard("BRK-B")

DATA_1985_CUTOFF = datetime.date(1985, 3, 1)  # small tolerance around the Jan-1985 Yahoo ceiling

series_cache = {}
first_avail = {}
excluded = []
for t in sorted(pool):
    s = load_series(t)
    if s is None:
        excluded.append((t, "no data"))
        continue
    fd = first_date(s)
    exit_px = nearest(s, TODAY, max_gap=45)
    if exit_px is None:
        excluded.append((t, "no recent price"))
        continue
    if fd > DATA_1985_CUTOFF:
        excluded.append((t, f"data starts {fd} -- too late for a 1985 start"))
        continue
    series_cache[t] = s
    first_avail[t] = fd

print(f"Universe pool: {len(pool)} tickers total; {len(series_cache)} have genuine 1985 data "
      f"(excluded {len(excluded)} -- most for starting after 1985, logged not hidden)")

spy_series = load_series("GSPC")  # ^GSPC index -- also caps at 1985-01-01 via
# Yahoo's monthly-bar limit, but (unlike the SPY ETF, inception 1993) that cap
# lines up EXACTLY with our portfolio floor, giving a true apples-to-apples
# 1985-to-today comparison instead of a mismatched 41.6yr-vs-33.5yr one.

def cagr_window(tickers, weight="equal"):
    """Portfolio starts at the LATEST first-availability date among its
    members (so every member has real data for the whole window), floored
    at 1985-01-01, held equal-weight to today, no rebalancing."""
    start = max([max(first_avail[t], FLOOR) for t in tickers])
    entry_prices = {}
    for t in tickers:
        p = nearest(series_cache[t], start)
        if p is None:
            return None
        entry_prices[t] = p
    exit_prices = {t: nearest(series_cache[t], TODAY, max_gap=45) for t in tickers}
    if any(v is None for v in exit_prices.values()):
        return None
    years = (TODAY - start).days / 365.25
    if years < 3:
        return None
    rets = [exit_prices[t]/entry_prices[t] for t in tickers]
    port_mult = statistics.mean(rets)  # equal-weight buy-and-hold multiple
    port_cagr = port_mult**(1/years) - 1
    spy_start = max(start, min(spy_series.keys()))
    spy_p0 = nearest(spy_series, spy_start)
    spy_p1 = nearest(spy_series, TODAY, max_gap=45)
    spy_years = (TODAY - spy_start).days / 365.25
    spy_cagr = (spy_p1/spy_p0)**(1/spy_years) - 1 if (spy_p0 and spy_p1) else None
    spy_note = "SPY inception-limited (started after portfolio)" if spy_start > start else None
    return {"start": start.isoformat(), "years": round(years,1), "cagr": port_cagr,
            "mult": port_mult, "spy_cagr": spy_cagr, "spy_note": spy_note, "tickers": tickers}

# ---- Construct 20 different portfolios, max 11 names each ----
rng = random.Random(RUN_SEED)
all_tickers = sorted(series_cache.keys())
portfolios = {}

# Named/themed constructions (deterministic, not random)
persistence = {}
for row in csv.DictReader(open(os.path.join(SCRATCH, "screen_portfolios_per_ticker.csv"))):
    persistence[row["ticker"]] = int(row["times_passed_of_13"])

high_persist = [t for t in all_tickers if persistence.get(t, 0) >= 8]
low_persist = [t for t in all_tickers if 0 < persistence.get(t, 0) <= 2]
buffett_actual = [p["ticker"] for p in json.load(open(os.path.join(SCRATCH, "buffett_picks_results.json")))]
buffett_actual = [t for t in buffett_actual if t in series_cache]

brk13f_top = []
seen = set()
for row in sorted(csv.DictReader(open(os.path.join(SCRATCH, "brk_13f_top10_resolved.csv"))), key=lambda r: -int(r["year"])):
    t = row["ticker"]
    if t != "UNRESOLVED" and t in series_cache and t not in seen:
        seen.add(t); brk13f_top.append(t)

portfolios["01_chronic_passers"] = high_persist[:11]
portfolios["02_occasional_passers"] = low_persist[:11]
portfolios["03_buffett_actual_picks"] = buffett_actual[:11]
portfolios["04_brk_13f_recent_top"] = brk13f_top[:11]

# Sector-flavored buckets (rough, name-based groupings from the pool)
tech = [t for t in all_tickers if t in ("AAPL","MSI","ANET","LRCX","MCHP","WDC","INTC","CSCO","ADP","GOOGL")]
staples_health = [t for t in all_tickers if t in ("PG","KO","CL","HSY","SJM","GIS","CHD","CLX","JNJ","BMY","BAX","DHR")]
industrial = [t for t in all_tickers if t in ("MMM","HON","CAT","DE","CMI","DOV","UNP","CSX","GATX","GE")]
financials_ex_bank = [t for t in all_tickers if t in ("AXP","MCO","GS","AMP","CB","BK")]
energy = [t for t in all_tickers if t in ("XOM","CVX","COP","PSX","OXY","HAL","MPC")]
consumer_disc = [t for t in all_tickers if t in ("LOW","AZO","BBY","DG","DRI","ROST","NKE","LVS","BKNG")]
utilities = [t for t in all_tickers if t in ("SO","AEP","PEG","CNP","ETR","DUK","ED")]

portfolios["05_tech"] = tech[:11]
portfolios["06_staples_health"] = staples_health[:11]
portfolios["07_industrial"] = industrial[:11]
portfolios["08_financials"] = financials_ex_bank[:11]
portfolios["09_energy"] = energy[:11]
portfolios["10_consumer_disc"] = consumer_disc[:11]
portfolios["11_utilities"] = utilities[:11]

# One-of-each-sector "true diversified 11"
diversified = []
for bucket in [tech, staples_health, industrial, financials_ex_bank, energy, consumer_disc, utilities, buffett_actual]:
    for t in bucket:
        if t not in diversified:
            diversified.append(t)
            break
    if len(diversified) >= 11:
        break
portfolios["12_one_per_sector_diversified"] = diversified[:11]

# Longest-history-available (the true "stood the test of time since 1985" set)
by_history = sorted(all_tickers, key=lambda t: first_avail[t])
portfolios["13_longest_history"] = by_history[:11]

# Fill the remainder with random samples until we have TARGET_TOTAL distinct
# portfolios (distinct = different set of tickers, not just a different label)
TARGET_TOTAL = 100
seen_sets = set(frozenset(v) for v in portfolios.values())
i = len(portfolios) + 1
attempts = 0
while len(portfolios) < TARGET_TOTAL and attempts < TARGET_TOTAL * 50:
    attempts += 1
    n = rng.choice([5, 6, 7, 8, 9, 10, 11])
    sample = rng.sample(all_tickers, min(n, len(all_tickers)))
    key = frozenset(sample)
    if key in seen_sets:
        continue
    seen_sets.add(key)
    portfolios[f"{i:03d}_random_{i}"] = sample
    i += 1

# ---- Run all 20 ----
results = {}
print(f"\n=== RUN (seed={RUN_SEED}) ===")
for name, tickers in portfolios.items():
    tickers = [t for t in tickers if t in series_cache]
    if len(tickers) < 3:
        print(f"{name}: SKIPPED (only {len(tickers)} resolvable names)")
        continue
    r = cagr_window(tickers)
    if r is None:
        print(f"{name}: SKIPPED (no valid window)")
        continue
    results[name] = r
    if r["spy_cagr"] is None:
        beat = "N/A"
    else:
        beat = "BEAT SPY" if r["cagr"] > r["spy_cagr"] else "trailed"
    spy_str = f"{r['spy_cagr']*100:6.2f}%" if r["spy_cagr"] is not None else "  N/A "
    print(f"{name:26} n={len(tickers):2}  start={r['start']}  yrs={r['years']:5.1f}  "
          f"port={r['cagr']*100:7.2f}%  spy={spy_str}  [{beat}]")

comparable = [r for r in results.values() if r["spy_cagr"] is not None]
beats = sum(1 for r in comparable if r["cagr"] > r["spy_cagr"])
print(f"\n{len(results)} portfolios computed ({len(comparable)} with a valid SPY comparison)")
print(f"{beats}/{len(comparable)} portfolios beat SPY over their own matched window")
print(f"Mean portfolio CAGR: {statistics.mean(r['cagr'] for r in results.values())*100:.2f}%")
print(f"Median portfolio CAGR: {statistics.median(r['cagr'] for r in results.values())*100:.2f}%")
print(f"Mean matched-SPY CAGR: {statistics.mean(r['spy_cagr'] for r in comparable)*100:.2f}%")
print(f"Best: {max(results.items(), key=lambda kv: kv[1]['cagr'])}")
print(f"Worst: {min(results.items(), key=lambda kv: kv[1]['cagr'])}")

json.dump({"seed": RUN_SEED, "results": results}, open(os.path.join(SCRATCH, f"portfolios20_run{RUN_SEED}.json"), "w"), indent=2, default=str)
