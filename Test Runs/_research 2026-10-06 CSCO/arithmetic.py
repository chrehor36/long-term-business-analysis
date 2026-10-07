"""Arithmetic for the CSCO run of 2026-10-06, from history_xbrl.csv (transcription of first-filed XBRL;
FY2024-FY2026 checked against the FY2026 10-K statements). Usage: python -I arithmetic.py"""
import csv, os
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, "history_xbrl.csv"))))


def f(r, k):
    return float(r[k]) if r[k] else None


print("year  revenue  GM%   OM%   R&D%  SBC%rev  acq")
acq = 0
for r in rows:
    rev = f(r, "revenue")
    gm = f(r, "gross_profit") / rev * 100
    om = f(r, "op_income") / rev * 100
    rnd = f(r, "rnd") / rev * 100 if r["rnd"] else float("nan")
    sbc = f(r, "sbc") / rev * 100
    a = f(r, "acq") or 0
    acq += a
    print(f"{r['fiscal_end'][:4]}  {rev:7.0f}  {gm:4.1f}  {om:4.1f}  {rnd:4.1f}  {sbc:4.1f}  {a:6.0f}")
first, last = rows[0], rows[-1]
n = int(last["fiscal_end"][:4]) - int(first["fiscal_end"][:4])
print("revenue CAGR FY%s-FY%s: %.2f%%" % (first["fiscal_end"][:4], last["fiscal_end"][:4],
      ((f(last, "revenue") / f(first, "revenue")) ** (1 / n) - 1) * 100))
r16 = [r for r in rows if r["fiscal_end"].startswith("2016")][0]
print("revenue CAGR FY2016-FY2026: %.2f%%" % (((f(last, "revenue") / f(r16, "revenue")) ** 0.1 - 1) * 100))
print("acquisitions net of cash, sum of tagged years (FY2019-FY2021 untagged): %.0f" % acq)
print("diluted shares FY2008 %.0f -> FY2026 %.0f (%.1f%%)" % (f(first, "diluted_shares"), f(last, "diluted_shares"),
      (f(last, "diluted_shares") / f(first, "diluted_shares") - 1) * 100))
oc = []
for r in rows[-5:]:
    o = f(r, "ocf") - f(r, "sbc") - f(r, "capex")
    oc.append(o)
    print(r["fiscal_end"][:4], "OCF", r["ocf"], "SBC", r["sbc"], "capex", r["capex"], "owner cash", round(o))
mean = sum(oc) / 5
shares = 3942.586873
price = 112.82
print("five-year mean owner cash %.0f; per share %.2f; yield at $%.2f: %.2f%%" % (
    mean, mean / shares, price, mean / shares / price * 100))
print("aggregate owner-cash growth FY2022-FY2026: %.1f%% a year" % (((oc[-1] / oc[0]) ** 0.25 - 1) * 100))
sov = 0.0566
print("COMPUTATION ONLY: no-growth value at sovereign %.2f%%: $%.1fB, $%.2f/share" % (
    sov * 100, mean / sov / 1000, mean / sov / shares))
print("COMPUTATION ONLY: no-growth value at 10%%: $%.1fB, $%.2f/share" % (mean / 0.10 / 1000, mean / 0.10 / shares))
print("market cap $%.1fB" % (price * shares / 1000))
