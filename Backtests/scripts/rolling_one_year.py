"""Corrected rolling one-year mechanical test, 2013-2025.

Replaces the original 49.3% "coin flip" figure, which was computed by
bt_engine.py -- an engine carrying the same market-cap look-ahead bug as the
main screen (adjclose price times a point-in-time share count). That bug
inflated the measured yield of companies that later split, i.e. of companies
whose stock rose, so the original selection was biased toward winners.

Two further improvements over the original run:
  * universe is the full 503-name 2013 reconstruction, not the 36 hand-picked
    large caps the original used;
  * every market cap is validated against dei:EntityPublicFloat, and the same
    rule-based data-quality exclusions used in BT-15 are applied.

Each Book One pass is held exactly one year from the anchor and compared with
SPY over the identical window -- the original test's design, so the headline
number stays comparable.
"""
import json, os, csv, datetime, bisect, statistics

SCRATCH = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SCRATCH, "bt_cache")
FAILCACHE = os.path.join(CACHE, "failures")
YEARS = [str(y) for y in range(2013, 2026)]
MAX_PLAUSIBLE_YIELD = 0.50
FLOAT_REQUIRED_ABOVE = 0.20


def load_adj(t):
    for base in (CACHE, FAILCACHE):
        for pref in ("pxfix_", "px_", "pxlong_"):
            p = os.path.join(base, f"{pref}{t}.json")
            if not os.path.exists(p):
                continue
            try:
                r = json.load(open(p))["chart"]["result"][0]
                ts = r["timestamp"]
                adj = r["indicators"].get("adjclose", [{}])[0].get("adjclose")
                if not adj:
                    adj = r["indicators"]["quote"][0]["close"]
                s = {datetime.date.fromtimestamp(x): adj[i]
                     for i, x in enumerate(ts)
                     if i < len(adj) and adj[i] is not None}
                if s:
                    return s
            except Exception:
                continue
    return None


def px_near(s, target, max_gap=25):
    ds = sorted(s)
    i = bisect.bisect_left(ds, target)
    if i >= len(ds) or (ds[i] - target).days > max_gap:
        return None
    return s[ds[i]]


def keep(r):
    flag = r.get("cap_flag", "") or ""
    y = float(r["yield"])
    if flag.startswith("CAP_BELOW_FLOAT"):
        try:
            ratio = float(flag.split("(")[1].rstrip("x)"))
        except (IndexError, ValueError):
            return False
        if ratio < (0.25 if "_APPROX" in flag else 0.5):
            return False
    if y > MAX_PLAUSIBLE_YIELD:
        return False
    if y > FLOAT_REQUIRED_ABOVE and flag == "NO_FLOAT_NEAR_ANCHOR":
        return False
    return True


spy = load_adj("SPY")
rows, per_year = [], []

for yr in YEARS:
    f = os.path.join(SCRATCH, f"v3b_screen_{yr}.csv")
    if not os.path.exists(f):
        print(f"  (skipping {yr}: no corrected screen)")
        continue
    entry = datetime.date(int(yr), 6, 30)
    exit_ = datetime.date(int(yr) + 1, 6, 30)
    if exit_ > datetime.date.today():
        print(f"  (skipping {yr}: one-year window not complete)")
        continue

    s_in, s_out = px_near(spy, entry), px_near(spy, exit_)
    if not (s_in and s_out):
        continue
    spy_ret = s_out / s_in - 1

    wins, rets = 0, []
    for r in csv.DictReader(open(f)):
        if r["passed"] != "True" or not keep(r):
            continue
        t = r["ticker"]
        s = load_adj(t)
        if not s:
            continue
        p_in, p_out = px_near(s, entry), px_near(s, exit_)
        if not (p_in and p_out):
            continue
        ret = p_out / p_in - 1
        rets.append(ret)
        if ret > spy_ret:
            wins += 1
        rows.append([yr, t, round(float(r["yield"]) * 100, 2),
                     round(ret * 100, 2), round(spy_ret * 100, 2),
                     ret > spy_ret])
    if rets:
        per_year.append({
            "year": yr, "n": len(rets), "wins": wins,
            "win_rate": round(100 * wins / len(rets), 1),
            "median_ret": round(100 * statistics.median(rets), 2),
            "mean_ret": round(100 * statistics.mean(rets), 2),
            "spy_ret": round(100 * spy_ret, 2),
        })

print(f"\n{'anchor':7s} {'n':>4s} {'win%':>6s} {'medRet':>8s} {'meanRet':>8s} "
      f"{'SPY':>8s} {'med-SPY':>8s}")
for p in per_year:
    print(f"{p['year']:7s} {p['n']:>4d} {p['win_rate']:>5.1f}% "
          f"{p['median_ret']:>7.2f}% {p['mean_ret']:>7.2f}% {p['spy_ret']:>7.2f}% "
          f"{p['median_ret']-p['spy_ret']:>+7.2f}")

tot_n = sum(p["n"] for p in per_year)
tot_w = sum(p["wins"] for p in per_year)
print(f"\nTOTAL one-year holdings: {tot_n}")
print(f"Overall win rate vs SPY: {100*tot_w/tot_n:.1f}%  ({tot_w}/{tot_n})")
print(f"Median of per-anchor (median pass - SPY): "
      f"{statistics.median(p['median_ret']-p['spy_ret'] for p in per_year):+.2f} pts")
print(f"Anchors where the median pass beat SPY: "
      f"{sum(1 for p in per_year if p['median_ret']>p['spy_ret'])}/{len(per_year)}")

json.dump(per_year, open(os.path.join(SCRATCH, "rolling_one_year.json"), "w"),
          indent=1)
with open(os.path.join(SCRATCH, "rolling_one_year_per_name.csv"), "w",
          newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["anchor", "ticker", "yield_pct", "fwd_1y_ret_pct",
                "spy_1y_ret_pct", "beat_spy"])
    w.writerows(rows)
