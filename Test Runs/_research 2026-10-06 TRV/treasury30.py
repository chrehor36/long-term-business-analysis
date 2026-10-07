"""Annual average of the US Treasury 30-year par yield, from the Treasury's own daily par yield curve CSV
(the issuing authority), for the years given. Caches each year's CSV in cache/.
Usage: python -I treasury30.py 2016 2025
"""
import os
import sys
import time
import urllib.request

URL = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{yr}/all"
       "?type=daily_treasury_yield_curve&field_tdr_date_value={yr}&page&_format=csv")
UA = "Mozilla/5.0 (research run; contact chrehor36@gmail.com)"


def year(yr):
    p = f"cache/treasury_{yr}.csv"
    if not os.path.exists(p) or os.path.getsize(p) == 0:
        req = urllib.request.Request(URL.format(yr=yr), headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            open(p, "wb").write(r.read())
        time.sleep(0.5)
    rows = [r for r in open(p, encoding="utf-8").read().strip().split("\n") if r.strip()]
    hdr = [h.strip('"') for h in rows[0].split(",")]
    i = hdr.index("30 Yr")
    vals = []
    for r in rows[1:]:
        c = r.split(",")
        if len(c) > i and c[i].strip('" '):
            vals.append(float(c[i].strip('"')))
    return sum(vals) / len(vals), len(vals)


if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2])
    out = []
    for y in range(a, b + 1):
        avg, n = year(y)
        out.append(avg)
        print(f"{y} 30Y average {avg:.3f}% over {n} days")
    print(f"mean of annual averages {a}-{b}: {sum(out)/len(out):.3f}%")
