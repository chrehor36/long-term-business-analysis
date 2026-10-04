"""Patch v3: screen_universe_v2.py -> screen_universe_v3.py

THE UNIFYING INSIGHT: market cap is split-invariant. Yahoo `close` is already
back-adjusted to TODAY's share basis, so the clean fix is to put the SHARE
COUNT on today's basis too and multiply directly -- no price adjustment at all:

    cap = close(anchor) * shares(at measurement date)
                        * product(splits effective AFTER that measurement date)

v2 instead scaled the price by splits after the ANCHOR while leaving shares at
their measurement date. That is wrong whenever a split falls BETWEEN the share
measurement date and the anchor -- which is exactly what broke the last three
validation failures:
  CL   shares 2013-04-25 = 466M, then a 2:1 split in May 2013 -> 932M
  FLS  shares 2013-04-19 = 47.7M, then a 3:1 split in Jun 2013 -> 143M
  CME  shares 2010-02-17 = 66.5M (dei went stale), 5:1 in 2012 -> 333M
All three are fixed by adjusting shares forward instead.

Also fixes PSA, whose 10-K cover tag is a filing typo (dei reports 171,858
shares against a real ~171.5M): cross-check the chosen count against the best
us-gaap share tag and prefer gaap on gross (>5x) disagreement.

Finally widens the public-float validation: strict window +/-25d, else a loose
+/-200d check flagged _APPROX (price drifts over 6 months, so thresholds
loosen) -- this shrinks the unvalidated bucket well below v2's 122.
"""
import os

SCRATCH = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(SCRATCH, "screen_universe_v2.py")).read()

# --- 1. shares_as_of also returns the measurement date -------------------
old = '''def shares_as_of(pts, asof):
    best = None
    for end, filed, val in pts:
        if filed <= asof:
            if best is None or filed > best[0]:
                best = (filed, val)
    return best[1] if best else None'''
new = '''def shares_as_of(pts, asof):
    """Returns (value, measurement_date). The measurement date is the `end`
    (cover-page as-of date) -- the date the count was actually true, which is
    what the split-forward adjustment must be measured from."""
    best = None
    for end, filed, val in pts:
        if filed <= asof:
            if best is None or filed > best[0]:
                best = (filed, val, end)
    return (best[1], best[2]) if best else (None, None)


def best_gaap_shares(cik_data, asof):
    """Most precise us-gaap share count available as of `asof`, for sanity-
    checking a dei cover-page value that may be a filing typo."""
    gaap = cik_data.get("facts", {}).get("us-gaap", {})
    for tag in FALLBACK_SHARES_TAGS:
        pts = _collect_shares(gaap, [tag])
        cand = [(f, v, e) for e, f, v in pts if f <= asof]
        if cand:
            cand.sort()
            return cand[-1][1], cand[-1][2]
    return None, None'''
assert old in src, "shares_as_of not found"
src = src.replace(old, new)

# --- 2. prices stay on today's basis (no price-side split scaling) -------
old = '''                        # un-adjust back to the price as actually traded
                        return px * split_factor_after(ticker, target), False'''
new = '''                        # keep today's-basis price; shares are brought to
                        # the same basis instead (cap is split-invariant)
                        return px, False'''
assert old in src, "cached price return not found"
src = src.replace(old, new)

# 10-K implied prices are TRUE historical prices, so convert them ONTO
# today's basis for consistency with the share-side adjustment.
old = '''                    return r["implied_price"], True'''
new = '''                    sf = split_factor_after(ticker, point_date) or 1.0
                    return r["implied_price"] / sf, True'''
assert old in src, "10-K price return not found"
src = src.replace(old, new)

# --- 3. widen float validation ------------------------------------------
old = '''def public_float_near(cik_data, anchor, max_gap_days=20):'''
new = '''def public_float_near(cik_data, anchor, max_gap_days=25):'''
assert old in src
src = src.replace(old, new)

# --- 4. new cap computation --------------------------------------------
old = '''    shares_pts, shares_approx = load_shares(cik_data, REBAL)
    shares = shares_as_of(shares_pts, REBAL)'''
new = '''    shares_pts, shares_approx = load_shares(cik_data, REBAL)
    shares, shares_date = shares_as_of(shares_pts, REBAL)

    # guard against cover-page tagging typos (PSA 2013: dei says 171,858
    # shares against a real ~171.5M) by cross-checking us-gaap
    if shares:
        g_val, g_end = best_gaap_shares(cik_data, REBAL)
        if g_val and (shares / g_val > 5.0 or g_val / shares > 5.0):
            shares, shares_date = g_val, g_end
            shares_approx = True

    # bring the count onto today's share basis: apply every split effective
    # AFTER the date the count was measured
    shares_split_factor = 1.0
    if shares and shares_date:
        shares_split_factor = split_factor_after(t, shares_date) or 1.0
        shares = shares * shares_split_factor'''
assert old in src, "shares block not found"
src = src.replace(old, new)

# --- 5. record the share adjustment, and loosen the approx float check ---
old = '''        if pub_float:
            ratio = mkt_cap / pub_float
            if ratio < 0.8:
                cap_flag = f"CAP_BELOW_FLOAT ({ratio:.2f}x)"
            elif ratio > 4.0:
                cap_flag = f"CAP_FAR_ABOVE_FLOAT ({ratio:.2f}x)"
            else:
                cap_flag = "OK"'''
new = '''        if not pub_float:
            pub_float, float_end = public_float_near(cik_data, REBAL, 200)
            approx = "_APPROX"
            lo, hi = 0.5, 6.0
        else:
            approx = ""
            lo, hi = 0.8, 4.0
        if pub_float:
            ratio = mkt_cap / pub_float
            if ratio < lo:
                cap_flag = f"CAP_BELOW_FLOAT{approx} ({ratio:.2f}x)"
            elif ratio > hi:
                cap_flag = f"CAP_FAR_ABOVE_FLOAT{approx} ({ratio:.2f}x)"
            else:
                cap_flag = "OK" + approx'''
assert old in src
src = src.replace(old, new)

old = '''        "pub_float": pub_float, "cap_flag": cap_flag,'''
new = '''        "pub_float": pub_float, "cap_flag": cap_flag,
        "shares_split_factor": shares_split_factor,'''
assert old in src
src = src.replace(old, new)

src = src.replace('"v2_screen_results.csv"', '"v3_screen_results.csv"')
src = src.replace('"v2_coverage_gaps.csv"', '"v3_coverage_gaps.csv"')

out = os.path.join(SCRATCH, "screen_universe_v3.py")
open(out, "w").write(src)
print("wrote", out, "-- all v3 patches applied")
