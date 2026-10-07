# -*- coding: utf-8 -*-
import io, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(BASE, "Test Runs", "2026-09-21 Run - MGM MGM Resorts International.md")
t = io.open(P, encoding="utf-8").read()
FIX = [
 (u'The screen\u2019s warning that *"the numerator\nand the denominator may be different companies"* is correct and is worse than it looks,',
  u'The screen\u2019s warning \u2014 that the numerator\nand the denominator may be different companies \u2014 is correct and is worse than it looks,'),
 (u'reason is [E2-47]\u2019s own carve-out** - unusual debt-equity ratios and mis-stated asset values.',
  u'reason is [E2-47]\u2019s own carve-out**, which excepts *"companies with unusual debt-equity ratios\nor those with important assets carried at unrealistic balance sheet values."*'),
]
n = 0
for a, b in FIX:
    if a in t:
        t = t.replace(a, b, 1); n += 1
    else:
        print("NOT FOUND", repr(a[:60]))
io.open(P, "w", encoding="utf-8").write(t)
print("applied", n, "of", len(FIX))
