"""Quantify the adjclose-vs-historical-shares market-cap bug.

The screen computed mkt_cap = split_adjusted_price * historical_share_count,
understating market cap (and thus overstating owner-earnings yield) by the
cumulative split factor occurring AFTER the anchor date. Because companies
that split are disproportionately companies whose stock rose, this injects
look-ahead bias directly into the top-N-by-yield candidate selection.

This script recomputes the true yield and re-tests the 4% hurdle.
"""
import json, os, csv, datetime, bisect

SCRATCH = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SCRATCH, "bt_cache")
FAILCACHE = os.path.join(CACHE, "failures")


def px_path(t):
    for base in (CACHE, FAILCACHE):
        for pref in ("px_", "pxlong_"):
            p = os.path.join(base, f"{pref}{t}.json")
            if os.path.exists(p):
                return p
    return None


def split_factor_after(t, anchor):
    """Product of split ratios with effective date strictly after anchor."""
    p = px_path(t)
    if not p:
        return None
    try:
        d = json.load(open(p))
        r = d["chart"]["result"][0]
    except Exception:
        return None
    f = 1.0
    for _, v in r.get("events", {}).get("splits", {}).items():
        try:
            sd = datetime.date.fromtimestamp(v["date"])
        except Exception:
            continue
        if sd > anchor:
            num, den = float(v.get("numerator", 1)), float(v.get("denominator", 1))
            if den:
                f *= num / den
    return f


BT14 = {
    "2016": ["NVDA","BKNG","ORLY","CSX","AAPL","CME","MA","NEE","AFL","FAST",
             "MPC","KEY","PSX","APH","PCAR","NDAQ","DOV","PNC","CMI"],
    "2020": ["BKNG","ORLY","GOOG","FOXA","LRCX","CME","CMCSA","AFL","PNC",
             "CSX","MA","AAPL"],
}

for label, names in BT14.items():
    anchor = datetime.date(int(label), 6, 30)
    rows = {r["ticker"]: r for r in csv.DictReader(
        open(os.path.join(SCRATCH, f"screen_{label}_results.csv")))}
    print(f"\n=== BT-14 {label} survivors: reported vs corrected yield "
          f"(hurdle 4.00%) ===")
    still, fell = [], []
    for t in names:
        r = rows.get(t)
        if not r or not r.get("yield"):
            print(f"  {t:6s} (no screen row)")
            continue
        y = float(r["yield"])
        sf = split_factor_after(t, anchor)
        if sf is None:
            print(f"  {t:6s} reported {y*100:6.2f}%  (no price file)")
            continue
        y_true = y / sf
        verdict = "PASS" if y_true >= 0.04 else "**FAIL**"
        (still if y_true >= 0.04 else fell).append(t)
        print(f"  {t:6s} reported {y*100:>8.2f}%   split_factor {sf:>5.1f}x   "
              f"corrected {y_true*100:>6.2f}%   -> {verdict}")
    print(f"  SUMMARY {label}: {len(still)} still pass, {len(fell)} FAIL once "
          f"corrected -> {fell}")
