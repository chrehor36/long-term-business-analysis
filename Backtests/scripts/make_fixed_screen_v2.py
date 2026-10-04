"""Patch v2: screen_universe_fixed.py -> screen_universe_v2.py

Adds two things on top of the split-factor fix:

1. Prefer the newly re-fetched `pxfix_*.json` files, which carry split events.
   The old `pxlong_*.json` files have none, so the split factor silently
   defaulted to 1.0 for 334 of ~500 tickers, leaving the look-ahead bug intact
   for most of the universe.

2. Validate every computed market cap against `dei:EntityPublicFloat` -- the
   10-K cover-page aggregate market value of non-affiliate common equity, a
   REAL filed figure whose measurement date is normally the fiscal-Q2 close
   (June 30 for calendar filers = our anchor). Available for 553/558 filers.

   Float is deliberately used as a VALIDATOR, not as the market cap itself:
   it excludes affiliate/insider holdings, so it understates true cap for
   controlled companies (Walton family ~45% of WMT), and using it as the yield
   denominator would bias the screen toward founder-controlled firms. But it
   is more than good enough to catch the 5x-50x errors we are hunting: a
   computed cap BELOW the float is close to impossible and means the cap is
   understated (the split bug); a cap many times the float is suspicious.
   Flags: OK / CAP_BELOW_FLOAT / CAP_FAR_ABOVE_FLOAT / NO_FLOAT_NEAR_ANCHOR.
"""
import os

SCRATCH = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(SCRATCH, "screen_universe_fixed.py")).read()

# --- 1. prefer pxfix_ (has split events) over px_/pxlong_ everywhere ---
n = src.count('("px_", "pxlong_")')
assert n >= 2, f"expected >=2 prefix tuples, found {n}"
src = src.replace('("px_", "pxlong_")', '("pxfix_", "px_", "pxlong_")')

# --- 2. helper: public float nearest the anchor ---
helper = '''
def public_float_near(cik_data, anchor, max_gap_days=20):
    """dei:EntityPublicFloat measured within max_gap_days of anchor.

    Returns (value, end_date) or (None, None). Prefers the closest
    measurement date; ignores zero/None values (some filers report 0)."""
    dei = cik_data.get("facts", {}).get("dei", {})
    pts = dei.get("EntityPublicFloat", {}).get("units", {}).get("USD", [])
    best = None
    for x in pts:
        v, e = x.get("val"), x.get("end")
        if not v or not e:
            continue
        try:
            ed = datetime.date.fromisoformat(e)
        except ValueError:
            continue
        gap = abs((ed - anchor).days)
        if gap <= max_gap_days and (best is None or gap < best[2]):
            best = (v, ed, gap)
    return (best[0], best[1]) if best else (None, None)


def split_factor_after(ticker, anchor):'''
assert "\ndef split_factor_after(ticker, anchor):" in src
src = src.replace("\ndef split_factor_after(ticker, anchor):", helper, 1)

# --- 3. compute the flag alongside mkt_cap ---
old = '''    if shares and entry_px:
        mkt_cap = entry_px * shares
        yld = worst5 / mkt_cap
        passed = yld >= hurdle'''
new = '''    pub_float, float_end = public_float_near(cik_data, REBAL)
    cap_flag = "NO_FLOAT_NEAR_ANCHOR"
    if shares and entry_px:
        mkt_cap = entry_px * shares
        yld = worst5 / mkt_cap
        passed = yld >= hurdle
        if pub_float:
            ratio = mkt_cap / pub_float
            if ratio < 0.8:
                cap_flag = f"CAP_BELOW_FLOAT ({ratio:.2f}x)"
            elif ratio > 4.0:
                cap_flag = f"CAP_FAR_ABOVE_FLOAT ({ratio:.2f}x)"
            else:
                cap_flag = "OK"'''
assert old in src
src = src.replace(old, new)

# --- 4. carry the flag into the result rows and the CSV ---
old_row = '''        "shares_approx": shares_approx if (shares and entry_px) else False,
    })'''
new_row = '''        "shares_approx": shares_approx if (shares and entry_px) else False,
        "pub_float": pub_float, "cap_flag": cap_flag,
    })'''
assert old_row in src
src = src.replace(old_row, new_row)

old_hdr = '''    w.writerow(["ticker", "worst5_ni", "yield", "mkt_cap", "passed", "still_in_index_today", "fate", "shares_approx"])'''
new_hdr = '''    w.writerow(["ticker", "worst5_ni", "yield", "mkt_cap", "passed", "still_in_index_today", "fate", "shares_approx", "pub_float", "cap_flag"])'''
assert old_hdr in src
src = src.replace(old_hdr, new_hdr)

old_w = '''        w.writerow([r["ticker"], r["worst5_ni"], r["yld"], r["mkt_cap"], r["passed"],'''
assert old_w in src
# append the two new fields to whatever that writerow ends with
i = src.index(old_w)
j = src.index("])", i)
src = src[:j] + ', r["pub_float"], r["cap_flag"]' + src[j:]

# --- 5. distinct outputs + a validation summary ---
src = src.replace('"fixed_screen_results.csv"', '"v2_screen_results.csv"')
src = src.replace('"fixed_coverage_gaps.csv"', '"v2_coverage_gaps.csv"')

src += '''

# --- validation summary -------------------------------------------------
from collections import Counter
flags = Counter(r["cap_flag"].split(" (")[0] for r in results)
print("\\nMARKET-CAP VALIDATION vs dei:EntityPublicFloat")
for k, v in flags.most_common():
    print(f"  {k:24s} {v}")
bad = [r for r in results if r["cap_flag"].startswith("CAP_BELOW_FLOAT")]
bad.sort(key=lambda r: float(r["cap_flag"].split("(")[1].rstrip("x)")))
print(f"\\nWorst CAP_BELOW_FLOAT (cap understated -> yield overstated), top 15:")
for r in bad[:15]:
    print(f"  {r['ticker']:6s} {r['cap_flag']:26s} "
          f"cap=${r['mkt_cap']/1e9:>8.2f}B float=${r['pub_float']/1e9:>8.2f}B "
          f"yield={r['yld']*100 if r['yld'] else 0:>7.2f}% passed={r['passed']}")
n_bad_pass = sum(1 for r in results
                 if r["passed"] and r["cap_flag"].startswith("CAP_BELOW_FLOAT"))
print(f"\\nPASSES resting on an understated cap: {n_bad_pass}")
'''

out = os.path.join(SCRATCH, "screen_universe_v2.py")
open(out, "w").write(src)
print("wrote", out, "-- all patches applied")
