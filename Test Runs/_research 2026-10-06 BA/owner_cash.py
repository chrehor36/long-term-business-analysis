"""Boeing owner cash after every real cost, USD millions. Arithmetic only.
Inputs are the filed consolidated statements of cash flows (accessions in the run file):
  FY2025 10-K 0001628280-26-004357 (2025, 2024, 2023); FY2022 10-K 0000012927-23-000007 (2022, 2021, 2020);
  FY2019 10-K 0000012927-20-000014 (2019, 2018, 2017); 2016 from the XBRL facts (series.py).
Owner cash = OCF - share-based plans expense - treasury shares issued for the 401(k) match - capex.
The 401(k) match is paid in Boeing stock from 2020 and added back as a non-cash item in OCF; it is compensation
("all forms of compensation", L2021-003), so it is deducted. Before 2020 the match was paid in cash inside OCF."""
rows = {  # FY: (OCF, SBC, 401k shares, capex, D&A)
    2016: (10496, 190, 0, 2613, 1889),
    2017: (13346, 202, 0, 1739, 2047),
    2018: (15322, 202, 0, 1722, 2114),
    2019: (-2446, 212, 0, 1834, 2271),
    2020: (-18410, 250, 195, 1303, 2246),
    2021: (-3416, 833, 1233, 980, 2144),
    2022: (3512, 725, 1215, 1222, 1979),
    2023: (5960, 690, 1515, 1527, 1861),
    2024: (-12080, 407, 1601, 2230, 1836),
    2025: (1065, 426, 1530, 2942, 1953),
}
print(f"{'FY':>4} {'OCF':>8} {'SBC':>6} {'401k':>6} {'capex':>6} {'D&A':>6} {'OC capex':>9} {'OC D&A':>8}")
oc = {}
for y, (ocf, sbc, k, cx, da) in rows.items():
    a = ocf - sbc - k - cx
    b = ocf - sbc - k - da
    oc[y] = (a, b)
    print(f"{y:>4} {ocf:>8} {sbc:>6} {k:>6} {cx:>6} {da:>6} {a:>9} {b:>8}")
for span in [(2021, 2025), (2016, 2025)]:
    ys = range(span[0], span[1] + 1)
    print(f"mean {span}: capex basis {sum(oc[y][0] for y in ys)/len(ys):,.0f}; D&A basis {sum(oc[y][1] for y in ys)/len(ys):,.0f}")
# first half 2026 (10-Q 0001628280-26-050038 / EX-99.1 0001628280-26-049929): OCF 1,185, capex 2,008
print("H1 2026 OCF - capex:", 1185 - 2008, "(before stock pay and the 401(k) shares; see run file)")
# share count and market value
cover = 790.370020          # M, cover of the 10-Q, as of 2026-07-21
pref_conv = 5.75 * 5.8280   # M common at the minimum conversion rate (price above the threshold)
price = 192.72
print(f"preferred as converted {pref_conv:.3f}M; diluted {cover + pref_conv:.3f}M")
print(f"market cap common {cover*price/1000:,.2f}B; as converted {(cover+pref_conv)*price/1000:,.2f}B")
print(f"threshold price for the minimum rate: {1000/5.8280:.2f}")
