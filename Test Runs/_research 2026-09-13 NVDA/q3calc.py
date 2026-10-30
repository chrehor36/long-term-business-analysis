"""Q3 arithmetic for the NVDA run (resumed session). Inputs are hand-read from the filed statements named beside each
array; FY2016-FY2023 balance-sheet lines are companyfacts (screening) cross-checked against the FY2026 10-K and the
Q2 FY2027 10-Q for the two newest dates. $M unless stated. Arithmetic only: nothing here concludes."""
FY = ["FY2016", "FY2017", "FY2018", "FY2019", "FY2020", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]
# balance sheet at fiscal year end (companyfacts StockholdersEquity etc.; FY2025/FY2026 re-read on the FY2026 10-K face)
equity = [4469, 5762, 7471, 9342, 12204, 16893, 26612, 22101, 42978, 79327, 157293]
cash = [596, 1766, 4002, 782, 10896, 847, 1990, 3389, 7280, 8589, 10605]
mktsec = [4441, 5032, 3106, 6640, 1, 10714, 19218, 9907, 18704, 34621, 39065]   # FY2026: debt securities only (51,951 less 12,886 public equity)
stakes = [0, 0, 0, 0, 0, 0, 0, 288, 1321, 3387, 22251 + 12886 + 4840]           # non-marketable + public equity (current and locked-up in other assets)
debt = [1413, 2779, 2000, 1988, 1991, 6963, 10946, 10953, 9709, 8463, 8468]      # convertible + senior notes, face as tagged
goodwill_int = [784, 722, 670, 663, 667, 6930, 6688, 6048, 5542, 5995, 24138]
netinc = [614, 1666, 3047, 4141, 2796, 4332, 9752, 4368, 29760, 72880, 120067]
opinc = [747, 1934, 3210, 3804, 2846, 4532, 10041, 4224, 32972, 81453, 130387]
pretax = [None, None, None, None, None, None, None, None, 33818, 84026, 141450]
taxexp = [None, None, None, None, None, None, None, None, 4058, 11146, 21383]
# Q2 FY2027 10-Q balance sheet (2026-07-26)
Q = dict(equity=228984, cash=22443, mktsec=34143, stakes=42783 + 51157 + 4957, debt=1000 + 32366, gwi=21125 + 2998)
ttm_ni = 120067 - 45197 + 118010          # FY2026 - H1 FY2026 + H1 FY2027 (10-K; 10-Q)
ttm_oi = 130387 - (21638 + 28440) + (53536 + 63734)
ttm_pretax = 141450 - 53117 + 141410
ttm_tax = 21383 - 7920 + 23400
ttm_other = ttm_pretax - ttm_oi

def opcap(i):
    return equity[i] - cash[i] - mktsec[i] - stakes[i] + debt[i]

print("| FY | equity | NI / avg equity | operating capital (equity - cash - debt securities - stakes + debt) | after-tax OI / avg operating capital | same, ex goodwill and intangibles [E2-43] |")
print("|---|---|---|---|---|---|")
for i in range(1, len(FY)):
    avg_e = (equity[i] + equity[i - 1]) / 2
    oc, oc0 = opcap(i), opcap(i - 1)
    t = (taxexp[i] / pretax[i]) if pretax[i] else 0.15   # CONVENTION where the rate was not extracted: 15%
    at = opinc[i] * (1 - t)
    tang = (oc - goodwill_int[i] + oc0 - goodwill_int[i - 1]) / 2
    print(f"| {FY[i]} | {equity[i]:,} | {netinc[i]/avg_e*100:.1f}% | {oc:,} | {at/((oc+oc0)/2)*100:.0f}% | {at/tang*100:.0f}% |")
ocq = Q["equity"] - Q["cash"] - Q["mktsec"] - Q["stakes"] + Q["debt"]
t = ttm_tax / ttm_pretax
print(f"| TTM to 2026-07-26 | {Q['equity']:,} | {ttm_ni/((Q['equity']+equity[-1])/2)*100:.1f}% (on the Jan/Jul average) | {ocq:,} | "
      f"{ttm_oi*(1-t)/((ocq+opcap(10))/2)*100:.0f}% | {ttm_oi*(1-t)/((ocq-Q['gwi']+opcap(10)-goodwill_int[10])/2)*100:.0f}% |")
print(f"TTM net income {ttm_ni:,}; operating income {ttm_oi:,}; other income {ttm_other:,}; pretax {ttm_pretax:,}; tax rate {t*100:.1f}%")
print(f"TTM NI ex other income after tax at the TTM rate: {(ttm_ni - ttm_other*(1-t)):,.0f}; / avg equity ex stakes "
      f"{(ttm_ni - ttm_other*(1-t))/((Q['equity']-Q['stakes']+equity[-1]-stakes[-1])/2)*100:.1f}%")
print(f"stakes share of equity 2026-07-26: {Q['stakes']/Q['equity']*100:.1f}% ; 2026-01-25: {stakes[-1]/equity[-1]*100:.1f}%")

# share count, split-adjusted to today's basis (4-for-1 July 2021, 10-for-1 June 2024; both verified at Step 0)
cover = [("2016-03-11", 541.6 * 40), ("2017-02-24", 588.6 * 40), ("2018-02-26", 604.6 * 40), ("2019-02-15", 606.0 * 40),
         ("2020-02-14", 612.0 * 40), ("2021-02-19", 620.0 * 40), ("2022-03-11", 2510 * 10), ("2023-02-17", 2470 * 10),
         ("2024-02-16", 2500 * 10), ("2025-02-21", 24400), ("2026-02-20", 24300), ("2026-07-26 (equity statement)", 24147)]
print("\nshares (M, split-adjusted):", "; ".join(f"{d} {v:,.0f}" for d, v in cover))
print(f"2016-03 -> 2026-07: {(24147/cover[0][1]-1)*100:+.1f}% ; 2017-02 -> 2026-07: {(24147/cover[1][1]-1)*100:+.1f}% ; 2022-03 peak -> 2026-07: {(24147/25100-1)*100:+.1f}%")
rep = {"FY2017": 739, "FY2018": 909, "FY2019": 1579, "FY2020": 0, "FY2021": 0, "FY2022": 0, "FY2023": 10039, "FY2024": 9533,
       "FY2025": 33706, "FY2026": 40086, "H1 FY2027": 39044}                       # cash-flow statements
rsutax = {"FY2017": 176, "FY2018": 612, "FY2019": 1032, "FY2020": 551, "FY2021": 942, "FY2022": 1904, "FY2023": 1475,
          "FY2024": 2783, "FY2025": 6930, "FY2026": 7948, "H1 FY2027": 4531}
print(f"repurchases FY2017-H1 FY2027 {sum(rep.values()):,}; RSU tax withholding {sum(rsutax.values()):,}; total {sum(rep.values())+sum(rsutax.values()):,}")
since23 = sum(v for k, v in rep.items() if k >= "FY2023" or k.startswith("H1")) + sum(v for k, v in rsutax.items() if k >= "FY2023" or k.startswith("H1"))
print(f"FY2023-H1 FY2027 repurchases + withholding {since23:,}; net shares retired {25100-24147:,}M; ${since23/(25100-24147):,.0f} per net share retired")
# average repurchase price, split-adjusted (10-K equity notes; 10-Q)
for k, sh, amt, adj in [("FY2019", 9, 1580, 40), ("FY2023", 63, 10040, 10), ("FY2024", 21, 9700, 10), ("FY2025", 310, 34000, 1),
                        ("FY2026", 282, 40400, 1), ("H1 FY2027", 203, 39800, 1), ("Q2 FY2027", 94, 19700, 1)]:
    print(f"  {k}: {sh}M shares for ${amt:,}M -> ${amt/sh/adj:,.2f} a share on today's basis")
# cash tax / pretax (cash-flow supplemental; income statement)
ct = {"FY2024": (6549, 33818), "FY2025": (15118, 84026), "FY2026": (20288, 141450)}
for k, (c, p) in ct.items():
    print(f"  cash tax {k}: {c/p*100:.1f}% of pretax")
print(f"  FY2026 ex equity gains of 8,918: {20288/(141450-8918)*100:.1f}%")
# grant-date fair value of awards vs the SBC charge (10-K Note 4 tables)
g = {"FY2022": (3492, 2004), "FY2023": (4505, 2709), "FY2024": (5316, 3549), "FY2025": (7834, 4737), "FY2026": (9389, 6386)}
for k, (gv, ch) in g.items():
    print(f"  {k}: grant-date value {gv:,} vs charge {ch:,} = {gv/ch:.2f}x")
