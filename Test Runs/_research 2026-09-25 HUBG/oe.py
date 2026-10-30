"""HUBG owner earnings, the corpus's way [E2-23]: OCF - SBC - (c). ARITHMETIC ONLY, NO CONCLUSION.
Inputs typed from the filed Consolidated Statements of Cash Flows (in thousands), extracted to cf_FY*_flat.txt
from the 10-Ks FY2010, FY2013, FY2016, FY2019, FY2022 (each value grepped in the filed text before use).
FY2023-FY2024 are from the FY2024 10-K and are WITHDRAWN under Item 4.02 (8-K 2026-05-12); shown apart.
(c) band: smaller and larger of D&A and (capex less proceeds from equipment sales)."""
# year: (OCF, SBC, capex, proceeds from equipment sales, D&A)
D = {
2008: (61507, 4360, 10732, 1342, 7369),
2009: (45228, 4394, 4246, 84, 8199),
2010: (37654, 3576, 25616, 988, 8572),
2011: (74866, 4788, 55010, 410, 16340),
2012: (92917, 6539, 56882, 1071, 21575),
2013: (117417, 7667, 110917, 1837, 21302),
2014: (98541, 8258, 119171, 612, 29380),
2015: (171697, 7833, 83042, 2309, 37042),
2016: (102473, 8479, 107409, 2061, 44712),
2017: (125220, 9873, 74541, 5327, 62173),
2018: (210839, 13480, 199791, 10975, 83910),
2019: (254509, 16286, 94847, 10025, 116887),
2020: (174954, 17053, 115306, 3289, 123679),
2021: (252835, 20056, 132952, 45177, 130629),
2022: (458163, 20426, 219140, 42929, 153726),
}
W = {  # WITHDRAWN
2023: (422158, 21348, 140068, 27717, 184449),
2024: (194419, 19157, 50847, 12158, 192562),
}
CAP = 1836.4  # $M, Step 0: 61,153,510 x $30.03
def row(y, v):
    ocf, sbc, cx, pr, da = v
    net = cx - pr
    hi_c, lo_c = max(net, da), min(net, da)
    return (ocf - sbc - hi_c) / 1000, (ocf - sbc - lo_c) / 1000, net / 1000, da / 1000
print("| FY | OCF | SBC | capex net of sales | D&A | OE low | OE high |")
print("|---|---|---|---|---|---|---|")
R = {}
for y, v in list(D.items()) + list(W.items()):
    lo, hi, net, da = row(y, v); R[y] = (lo, hi)
    tag = " (WITHDRAWN)" if y in W else ""
    print(f"| {y}{tag} | {v[0]/1000:,.1f} | {v[1]/1000:,.1f} | {net:,.1f} | {da:,.1f} | {lo:,.1f} | {hi:,.1f} |")
print()
for a, b in [(2020, 2022), (2018, 2022), (2017, 2021), (2013, 2022), (2008, 2022), (2016, 2020), (2013, 2017)]:
    ys = range(a, b + 1)
    lo = sum(R[y][0] for y in ys) / len(ys); hi = sum(R[y][1] for y in ys) / len(ys)
    print(f"window FY{a}-{b} ({len(ys)}y): ${lo:,.1f}M to ${hi:,.1f}M  = {lo/CAP:.2%} to {hi/CAP:.2%} of ${CAP:,.1f}M")
ys = range(2020, 2025)
lo = sum(R[y][0] for y in ys) / 5; hi = sum(R[y][1] for y in ys) / 5
print(f"window FY2020-2024 incl. WITHDRAWN years (5y): ${lo:,.1f}M to ${hi:,.1f}M = {lo/CAP:.2%} to {hi/CAP:.2%}")
