# OGE run 2026-10-26: Q7 arithmetic. Every input is a filed figure (USD millions) named in the run file.
# Consolidated statements: FY2025 10-K (0001193125-26-055414) for 2023-2025; FY2023 10-K
# (0000950170-24-017400) for 2021-2022 as restated (cost of removal in investing).
yrs = [2021, 2022, 2023, 2024, 2025]
ocf = [-229.9, 952.4, 1232.3, 812.8, 1137.1]
# midstream items removed (the business that produced them is sold; its sale proceeds are not counted):
enable_dist = [73.4, 0, 0, 0, 0]          # distributions from Enable, in OCF 2021
et_dist = [0, 34.0, 0, 0, 0]              # distributions from Energy Transfer, in OCF 2022
et_sale_tax = [0, 276.0 - 41.5, 0, 0, 0]  # 2022 cash tax less 2023 cash tax: the run's estimate of tax on the ET sale
sbc = [9.8, 9.7, 13.1, 11.7, 14.0]
capex = [778.5, 1050.9, 1178.2, 1090.9, 1054.4]
cor = [89.0, 112.7, 93.9, 70.3, 72.2]     # cost of removal and other (investing)
da = [416.0, 460.9, 506.6, 539.5, 559.8]
int_paid = [156.4, 164.0, 202.4, 251.1, 268.7]
tax_rate = 0.225                          # 21% federal + 1.5% state, FY2025 rate reconciliation
ltd_2020, ltd_2025 = 3494.0, 5369.0       # long-term debt incl. current maturities, 12/31/2020 and 12/31/2025 (no finance leases found)
cap_share = (0.88 * 0.465 + 0.07 * 0.50) / 0.95   # allowed debt share: OK 46.5% (53.5% equity), AR 50%; revenue-weighted
shares = 206.581287                       # cover of Q2 2026 10-Q, at 6/30/2026
fsa_shares, fsa_price = 4.613372, 41.71   # forward sale agreements, unsettled at 6/30/2026
price = 48.41
rf = 0.0533
floor = 0.10
net_debt = 5598.2 + 115.9 + 129.1 - 0.9  # 6/30/2026: LTD + current LTD + short-term debt - cash

def avg(x): return sum(x) / len(x)
ocf_adj = [o - e - d + t for o, e, d, t in zip(ocf, enable_dist, et_dist, et_sale_tax)]
spend = [c + r for c, r in zip(capex, cor)]
M = [o - s - d for o, s, d in zip(ocf_adj, sbc, da)]            # owner cash after maintenance (guess = D&A)
A = [o - s - p for o, s, p in zip(ocf_adj, sbc, spend)]          # owner cash after all spending
Mlit = [o - s - d for o, s, d in zip(ocf, sbc, da)]
Alit = [o - s - p for o, s, p in zip(ocf, sbc, spend)]
G = [p - d for p, d in zip(spend, da)]                           # growth spending
credit_raw = (ltd_2025 - ltd_2020) / 5
print("year  ocf_adj   M(maint)  A(all)   growth_spend")
for i, y in enumerate(yrs):
    print(f"{y}  {ocf_adj[i]:8.1f} {M[i]:8.1f} {A[i]:8.1f} {G[i]:8.1f}")
print(f"avg M {avg(M):.1f}  avg A {avg(A):.1f}  avg G {avg(G):.1f}  literal avg M {avg(Mlit):.1f}  literal avg A {avg(Alit):.1f}")
print(f"halves of M: first two yrs {avg(M[:2]):.1f}, last two yrs {avg(M[3:]):.1f}")
cap = cap_share * avg(G)
credit = min(credit_raw, cap)
print(f"LTD increase/yr {credit_raw:.1f}; cap {cap_share*100:.1f}% x G = {cap:.1f}; credit = {credit:.1f}")
print(f"all-spending with credit: {avg(A)+credit:.1f}")

def value_growth(m0, g0, c0, g, r, years=10):
    """maintenance cash m0, growth spend g0 and debt credit c0 all grow at g for 10 years; after
    year 10 growth stops, growth spend and credit stop, maintenance cash held flat (zero nominal)."""
    v = 0.0
    for t in range(1, years + 1):
        f = (1 + g) ** t
        v += (m0 * f - g0 * f + c0 * f) / (1 + r) ** t
    term = m0 * (1 + g) ** years / r
    return v + term / (1 + r) ** years

def ps(v): return v / shares
m0 = avg(M)
for r in (rf, floor):
    v0 = m0 / r
    print(f"no-growth maintenance case at {r*100:.2f}%: {v0:,.0f}M = ${ps(v0):.2f}/sh"
          f"  (with FSA settled: ${(v0+fsa_shares*fsa_price)/(shares+fsa_shares):.2f})")
# all-equity beside: owner cash before interest less net debt
mu = m0 + avg(int_paid) * (1 - tax_rate)
for r in (rf, floor):
    print(f"all-equity no-growth at {r*100:.2f}%: ({mu:.1f}/r - net debt {net_debt:.1f}) = ${ps(mu/r-net_debt):.2f}/sh")
cap_mkt = price * shares
print(f"market cap {cap_mkt:,.0f}M; owner cash yield at price (no growth) {m0/cap_mkt*100:.2f}%")
# sensitivities beside (not the range): generous base and growth
gr_da = (559.8 / 416.0) ** 0.25 - 1
gr_ni = (499.8 / 360.0) ** 0.25 - 1
base_ex21 = avg(M[1:]); g_ex21 = avg(G[1:])
cap2 = min(credit_raw, cap_share * g_ex21)
for label, mb, gb, cb in (("window base", m0, avg(G), credit), ("base without 2021", base_ex21, g_ex21, cap2)):
    for g in (gr_da, gr_ni):
        for r in (rf, floor):
            v = value_growth(mb, gb, cb, g, r)
            print(f"SENSITIVITY {label} M={mb:.1f} G={gb:.1f} C={cb:.1f} g={g*100:.1f}% r={r*100:.2f}%: {v:,.0f}M = ${ps(v):.2f}/sh")
# what owner cash a 10% floor needs at the price, no growth
print(f"owner cash needed for 10% at price, no growth: {cap_mkt*0.10:,.0f}M vs window {m0:.1f}")
fair = m0 / floor / shares
print(f"FAIR (equity-only, central; range is the no-growth case alone): ${fair:.2f}")
