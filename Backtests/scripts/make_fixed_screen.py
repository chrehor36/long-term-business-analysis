"""Patch screen_2013_universe.py -> screen_universe_fixed.py.

THE BUG: mkt_cap = price * shares_as_of(anchor), where price came from Yahoo
`adjclose`. Both Yahoo `adjclose` and `quote.close` are back-adjusted to
TODAY's share basis, while `shares` is the true point-in-time count. Market cap
was therefore understated -- and owner-earnings yield overstated -- by the
cumulative split factor occurring AFTER the anchor date. Companies that split
are overwhelmingly companies whose stock rose, so this fed look-ahead bias
directly into top-N-by-yield candidate selection.

THE FIX: true historical price = quote.close * product(split ratios with
effective date > anchor). Use `close` (split-adjusted only), NOT `adjclose`
(also dividend-adjusted). Verified: AAPL 2013-07-01 close $14.61 * 28 (7:1
2014 x 4:1 2020) = $409.08 vs real $409.22.

10-K-implied prices are TRUE historical prices already (from cover-page
aggregate market value) and must NOT be scaled by the split factor.
"""
import os, re

SCRATCH = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(SCRATCH, "screen_2013_universe.py")).read()

# --- 1. raw close instead of adjclose, for point-in-time market cap ---
old_series = '''        adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose")
        close = res["indicators"]["quote"][0]["close"]
        series = {}
        for i, t in enumerate(ts):
            dt = datetime.datetime.utcfromtimestamp(t).date()
            v = adj[i] if adj and i < len(adj) and adj[i] is not None else close[i]'''
new_series = '''        # FIXED 2026-07-25: use raw `close`, NOT `adjclose`. Both are
        # back-adjusted to today's share basis, but adjclose ALSO removes
        # dividends, so it is not a price at all. `close` * post-anchor split
        # factor recovers the true historical price (see split_factor_after).
        close = res["indicators"]["quote"][0]["close"]
        series = {}
        for i, t in enumerate(ts):
            dt = datetime.datetime.utcfromtimestamp(t).date()
            v = close[i]'''
assert old_series in src, "series loader block not found"
src = src.replace(old_series, new_series)

# --- 2. add split-factor helper right before price_near ---
helper = '''
def split_factor_after(ticker, anchor):
    """Product of split ratios effective AFTER anchor. Yahoo prices are
    back-adjusted to today's basis; multiplying by this recovers the true
    price as traded at `anchor`, which is what pairs with a point-in-time
    share count. Returns 1.0 when no post-anchor splits (or no data)."""
    for base in (CACHE, FAILURES_CACHE):
        for prefix in ("px_", "pxlong_"):
            p = os.path.join(base, f"{prefix}{ticker}.json")
            if not os.path.exists(p):
                continue
            try:
                d = json.load(open(p))
                res = d["chart"]["result"][0]
            except Exception:
                continue
            f = 1.0
            for _, v in res.get("events", {}).get("splits", {}).items():
                try:
                    sd = datetime.datetime.utcfromtimestamp(v["date"]).date()
                except Exception:
                    continue
                if sd > anchor:
                    num = float(v.get("numerator", 1))
                    den = float(v.get("denominator", 1))
                    if den:
                        f *= num / den
            return f
    return 1.0


def price_near(ticker, target):'''
assert "\ndef price_near(ticker, target):" in src, "price_near def not found"
src = src.replace("\ndef price_near(ticker, target):", helper, 1)

# --- 3. scale the cached-series price by the split factor (but NOT the
#        10-K implied price, which is already a true historical price) ---
old_ret = '''                    px = nearest(series, target, max_gap=20)
                    if px is not None:
                        return px, False'''
new_ret = '''                    px = nearest(series, target, max_gap=20)
                    if px is not None:
                        # un-adjust back to the price as actually traded
                        return px * split_factor_after(ticker, target), False'''
assert old_ret in src, "price_near return block not found"
src = src.replace(old_ret, new_ret)

# --- 4. distinct output filenames so nothing overwrites the buggy originals ---
src = src.replace('"sp500_2013_screen_results.csv"', '"fixed_screen_results.csv"')
src = src.replace('"sp500_2013_coverage_gaps.csv"', '"fixed_coverage_gaps.csv"')

out = os.path.join(SCRATCH, "screen_universe_fixed.py")
open(out, "w").write(src)
print("wrote", out)
print("patches applied: 4/4")
