"""Class A equivalent share count for Visa, from the filed cover and the filed conversion rates.
Cover: 10-Q for the quarter to 2026-06-30, filed 2026-07-29, accession 0001403161-26-000104, counts as of 2026-07-21.
Rates: Note 11 of the same 10-Q (rates in force at 2026-06-30, unchanged until the 2026-09-18 deposit).
Preferred: Note 11 gives only rounded as-converted millions (series A 7, B 1, C 2) at 2026-06-30.
Post-cover rate change: 8-K filed 2026-09-23, accession 0001403161-26-000121 (rates from 2026-09-18)."""

cover = {  # shares outstanding at 2026-07-21, from the cover
    "A": 1_704_112_694, "B-1": 2_180_148, "B-2": 486_669, "B-3": 60_589_871, "C": 17_059_152}
rate_jun = {"A": 1.0, "B-1": 1.5445, "B-2": 1.5014, "B-3": 1.4953, "C": 4.0}
rate_sep = {"A": 1.0, "B-1": 1.5400, "B-2": 1.4924, "B-3": 1.4773, "C": 4.0}
pref_asconv = 7e6 + 1e6 + 2e6  # series A, B, C preferred, as-converted, rounded to millions in the filing

def total(rates):
    rows = {k: cover[k] * rates[k] for k in cover}
    return rows, sum(rows.values()) + pref_asconv

for label, r in (("rates in force at the cover date", rate_jun), ("rates from 2026-09-18 (8-K)", rate_sep)):
    rows, t = total(r)
    print(label)
    for k, v in rows.items():
        print("   %-4s %15s x %.4f = %15.0f" % (k, f"{cover[k]:,}", r[k], v))
    print("   preferred series A, B, C as-converted (rounded in filing): %.0f" % pref_asconv)
    print("   TOTAL class A equivalent: %.3fM" % (t / 1e6))

price = 369.71  # close 2026-10-05, aggregator (tools/run.py, Yahoo), flagged
t = total(rate_sep)[1]
print("market cap at $%.2f on the post-2026-09-18 count: $%.1fB" % (price, price * t / 1e9))
t0 = total(rate_jun)[1]
print("market cap at $%.2f on the cover-date count: $%.1fB" % (price, price * t0 / 1e9))
