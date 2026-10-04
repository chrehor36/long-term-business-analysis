"""Forward returns for the CORRECTED Book One + Gate 4 survivors, 8 anchors.

This is the honest base rate the qualitative gates (1/2/3/5) would have to
improve on. It is deliberately computed BEFORE spending research effort on the
qualitative gates, so the expensive step can be judged against a known
starting point rather than assumed to be worth it.

Returns use adjclose (split AND dividend adjusted) -- correct for total return
and unaffected by the market-cap bug, which concerned the price-times-shares
product at the anchor, not the ratio of two prices in the same series.

Names whose series ends before today (acquired, merged, delisted) are carried
to their last available price and counted; the count is reported, since an
acquisition usually closes at a premium and a bankruptcy near zero, and hiding
either would bias the result.
"""
import json, os, datetime, bisect, statistics, csv

SCRATCH = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SCRATCH, "bt_cache")
FAILCACHE = os.path.join(CACHE, "failures")
YEARS = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
TODAY = datetime.date.today()


def load_adj(t):
    for base in (CACHE, FAILCACHE):
        for pref in ("pxfix_", "px_", "pxlong_"):
            p = os.path.join(base, f"{pref}{t}.json")
            if not os.path.exists(p):
                continue
            try:
                d = json.load(open(p))
                r = d["chart"]["result"][0]
                ts = r["timestamp"]
                adj = r["indicators"].get("adjclose", [{}])[0].get("adjclose")
                if not adj:
                    adj = r["indicators"]["quote"][0]["close"]
                s = {}
                for i, x in enumerate(ts):
                    if i < len(adj) and adj[i] is not None:
                        s[datetime.date.fromtimestamp(x)] = adj[i]
                if s:
                    return s
            except Exception:
                continue
    return None


def px_on_or_after(s, target, max_gap=25):
    ds = sorted(s)
    i = bisect.bisect_left(ds, target)
    if i >= len(ds) or (ds[i] - target).days > max_gap:
        return None, None
    return ds[i], s[ds[i]]


spy = load_adj("SPY")
rows_out = []
summary = []

for yr in YEARS:
    anchor = datetime.date(int(yr), 6, 30)
    years = (TODAY - anchor).days / 365.25
    surv = json.load(open(os.path.join(SCRATCH, f"gate4_survivors_{yr}.json")))

    _, spy_in = px_on_or_after(spy, anchor)
    spy_out = spy[max(spy)]
    spy_mult = spy_out / spy_in
    spy_cagr = (spy_mult ** (1 / years) - 1) * 100

    mults, truncated, missing = [], [], []
    for t in surv:
        s = load_adj(t)
        if not s:
            missing.append(t)
            continue
        d_in, p_in = px_on_or_after(s, anchor)
        if p_in is None:
            missing.append(t)
            continue
        d_out = max(s)
        p_out = s[d_out]
        m = p_out / p_in
        if (TODAY - d_out).days > 180:
            truncated.append((t, str(d_out), round(m, 2)))
        mults.append((t, m, (m ** (1 / years) - 1) * 100))
        rows_out.append([yr, t, str(d_in), round(p_in, 2), str(d_out),
                         round(p_out, 2), round(m, 3),
                         round((m ** (1 / years) - 1) * 100, 2)])

    ms = [m for _, m, _ in mults]
    cs = sorted(c for _, _, c in mults)
    ew_cagr = (statistics.mean(ms) ** (1 / years) - 1) * 100
    med_cagr = statistics.median(cs)
    beat = sum(1 for c in cs if c > spy_cagr)

    summary.append({
        "yr": yr, "years": round(years, 2), "n": len(ms),
        "spy_cagr": round(spy_cagr, 2),
        "ew_cagr": round(ew_cagr, 2), "median_name_cagr": round(med_cagr, 2),
        "names_beating_spy": beat, "pct_names_beating": round(100 * beat / len(ms), 1),
        "ew_vs_spy": round(ew_cagr - spy_cagr, 2),
        "truncated": truncated, "missing": missing,
    })

print(f"{'anchor':8s} {'yrs':>5s} {'n':>3s} {'SPY':>7s} {'EQ-WT':>7s} "
      f"{'vs SPY':>7s} {'medName':>8s} {'names>SPY':>10s}")
for s in summary:
    print(f"{s['yr']:8s} {s['years']:>5.2f} {s['n']:>3d} {s['spy_cagr']:>6.2f}% "
          f"{s['ew_cagr']:>6.2f}% {s['ew_vs_spy']:>+6.2f}  {s['median_name_cagr']:>7.2f}% "
          f"{s['names_beating_spy']:>4d}/{s['n']:<3d} ({s['pct_names_beating']:.0f}%)")

wins = sum(1 for s in summary if s["ew_vs_spy"] > 0)
print(f"\nEqual-weight basket beat SPY at {wins} of {len(summary)} anchor dates")
print(f"Mean margin vs SPY across dates: "
      f"{statistics.mean(s['ew_vs_spy'] for s in summary):+.2f} pts/yr")
print(f"Median margin vs SPY across dates: "
      f"{statistics.median(s['ew_vs_spy'] for s in summary):+.2f} pts/yr")

allt = [t for s in summary for t in s["truncated"]]
print(f"\nSeries ending >180d before today (acquired/delisted): {len(allt)}")
for t in allt[:12]:
    print("   ", t)
miss = {t for s in summary for t in s["missing"]}
print(f"No usable price data: {len(miss)} {sorted(miss)}")

json.dump(summary, open(os.path.join(SCRATCH, "bt15_base_rate.json"), "w"), indent=1)
with open(os.path.join(SCRATCH, "bt15_base_rate_per_name.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["anchor_year", "ticker", "entry_date", "entry_px",
                "exit_date", "exit_px", "total_return_x", "cagr_pct"])
    w.writerows(rows_out)
