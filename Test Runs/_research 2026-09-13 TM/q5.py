"""Q5 arithmetic only (operator rule 8): yields, implied growth, value ranges. ¥bn."""
P = 3031.0            # ¥ per share, TSE close 2026-09-11 (aggregator, flagged)
N = 11813.621960      # million shares, walked to 2026-08-31
CAP = P * N / 1000    # ¥bn
SOV = 0.03995         # 30Y JGB, MOF, 2026-09-10
FLOOR = 0.10          # [E4-28]
oe = {"(A) 10-yr": 2015.334, "(A) 7-yr": 2279.523, "(A) 5-yr": 2765.645, "(A) 5-yr ex-FY2024": 2008.595,
      "(D) 10-yr": 2392.938, "(D) 5-yr": 3222.989, "(E) 10-yr": 2602.960, "(E) 5-yr": 3471.250,
      "(E) 3-yr": 4198.704, "(A) 3-yr": 3480.784, "(B) 5-yr INVALID": 3498.192}
print(f"cap ¥{CAP:,.1f}bn")
def g_needed(r, oe):  # perpetuity: CAP = OE(1+g)/(r-g)  ->  g = (r*CAP - OE)/(CAP + OE)
    return (r * CAP - oe) / (CAP + oe)
for k, v in oe.items():
    y = v / CAP
    print(f"{k:20s} OE {v:8,.0f}  yield {y*100:5.2f}%  pts over JGB {(y-SOV)*100:+5.2f}  "
          f"g implied @JGB {g_needed(SOV, v)*100:+5.2f}%  g needed for floor {g_needed(FLOOR, v)*100:+5.2f}%  "
          f"value@floor g0 ¥{v/FLOOR:,.0f}bn = ¥{v/FLOOR/N*1000:,.0f}/sh  value@JGB g0 ¥{v/SOV:,.0f}bn = ¥{v/SOV/N*1000:,.0f}/sh  per-share OE ¥{v/N*1000:,.1f}")
