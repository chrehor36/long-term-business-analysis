"""TRV, Q7 check: the same construction as value.py on the five MATURE accident years 2019 to 2023 only
(A3: immature accident years 2024 and 2025 are not averaged in as if developed). Inputs from comp_out.txt.
Usage: python -I value_mature.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import value as V  # noqa: E402

c2 = (463 + 1408 + 1375 + 537 + 733) / 5                      # component 2, AY basis, 2019-2023, pre-tax
t = (516 + 540 + 796 + 512 + 380) / (3138 + 3237 + 4458 + 3354 + 3371)  # effective tax 2019-2023
non = (-433 - 444 - 443 - 490 - 579) / 5                       # items other than underwriting, pre-tax
c2at, nonat = c2 * (1 - t), non * (1 - t)
print(f"mature 2019-2023: C2 pre-tax {c2:.0f}, effective tax {t*100:.1f}%, after tax {c2at:.0f}, non-UW after tax {nonat:.0f}")
c1 = V.INV + V.CASH - V.FLOAT_C1
lo, mid, hi = c1 + nonat / V.R, c1 + c2at / V.R, c1 + V.pv(c2at, V.R, V.R)
print(f"per share: low ${lo/V.SH:.0f}  middle ${mid/V.SH:.0f}  top ${hi/V.SH:.0f}  width {hi/lo:.2f} to 1  price ${V.PRICE}")
inv = c1 * V.NII_YIELD_PRE * V.NII_AT_SHARE
own = c2at + inv
fat = 0.10 * (1 - t)
print(f"owner earnings after tax {own:.0f}; yield at the price {own/(V.PRICE*V.SH)*100:.2f}% after tax; "
      f"cheap ${own/fat/V.SH:.0f}; fair ${(V.pv(c2at, V.R, fat) + inv/fat)/V.SH:.0f}")
