"""Patch v3b: screen_universe_v3.py -> screen_universe_v3b.py

Drops v3's us-gaap share cross-check. Intent was to catch cover-page tagging
typos (PSA 2013 dei = 171,858 vs a real ~171.5M), but the ">5x disagreement ->
prefer gaap" rule cannot tell a typo apart from a filer that tags share counts
in THOUSANDS under the `shares` unit. It therefore swapped correct dei values
for thousands-scale gaap values and broke COL, DLTR, EFX, FHN, RTX, SPG, SYK
(caps collapsing to ~$0.0B) while fixing only PSA -- a bad trade.

Kept from v3: the share-side split-forward adjustment, which is the correct
unified fix and did resolve CME/CL/FLS. Kept the widened float validation,
which cut the unvalidated bucket from 122 to 38.

Residual cover-page typos (PSA) are left to the float validator to flag, and
are excluded as data-quality gaps rather than silently repaired -- consistent
with how AIV/TSN/PSA/TRIP were handled before.

_APPROX float comparisons (+/-200d window) are advisory only: over six months
price drift alone can breach the band, and at least one flag is already known
to be a false alarm (EXC 2013 computes $25.95B, which is right, against a
float measured far from the anchor).
"""
import os

SCRATCH = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(SCRATCH, "screen_universe_v3.py")).read()

old = '''    # guard against cover-page tagging typos (PSA 2013: dei says 171,858
    # shares against a real ~171.5M) by cross-checking us-gaap
    if shares:
        g_val, g_end = best_gaap_shares(cik_data, REBAL)
        if g_val and (shares / g_val > 5.0 or g_val / shares > 5.0):
            shares, shares_date = g_val, g_end
            shares_approx = True

'''
assert old in src, "v3 gaap guard block not found"
src = src.replace(old, '')

src = src.replace('"v3_screen_results.csv"', '"v3b_screen_results.csv"')
src = src.replace('"v3_coverage_gaps.csv"', '"v3b_coverage_gaps.csv"')

# report strict vs advisory separately in the summary
old_sum = '''n_bad_pass = sum(1 for r in results
                 if r["passed"] and r["cap_flag"].startswith("CAP_BELOW_FLOAT"))
print(f"\\nPASSES resting on an understated cap: {n_bad_pass}")'''
new_sum = '''strict_bad = [r for r in results if r["passed"]
              and r["cap_flag"].startswith("CAP_BELOW_FLOAT")
              and "_APPROX" not in r["cap_flag"]]
approx_bad = [r for r in results if r["passed"]
              and r["cap_flag"].startswith("CAP_BELOW_FLOAT")
              and "_APPROX" in r["cap_flag"]]
print(f"\\nPASSES on an understated cap -- STRICT (must exclude): "
      f"{len(strict_bad)} {[r['ticker'] for r in strict_bad]}")
print(f"PASSES flagged only by the loose +/-200d check (advisory): "
      f"{len(approx_bad)} {[r['ticker'] for r in approx_bad]}")'''
assert old_sum in src
src = src.replace(old_sum, new_sum)

out = os.path.join(SCRATCH, "screen_universe_v3b.py")
open(out, "w").write(src)
print("wrote", out)
