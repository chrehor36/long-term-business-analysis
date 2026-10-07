# Q2 arithmetic for the BN run, 2026-09-13 resume. Every input is a filed figure; sources in comments.
def pct(a, b): return 100.0 * a / b

print("== A. WEIGHTS: where the money is ==")
# (1) Segment common equity, 2026-06-30, BN 6-K Q2 2026 segment table ($M)
eq = {"Asset Management (BAM + direct fund stakes)": 14968, "Wealth Solutions": 13139, "Infrastructure (BIP)": 2097,
      "Energy (BEP)": 4729, "Private Equity (BBUC)": 1016, "Real Estate (BPG)": 26706}
tot = sum(eq.values())
print("positive segments total", tot, "corporate", -20172, "net", tot - 20172)
for k, v in eq.items(): print(f"  {k:48s} {v:7d}  {pct(v, tot):5.1f}%")
# Asset Management split at 2025-12-31: segment 15,511; direct investments 10,876 (40-F; Q1 table)
print("  AM split YE2025: direct fund stakes", 10876, pct(10876, 15511), "% of AM; BAM stake book", 15511 - 10876)
# (2) FY2025 cash measures reaching the Corporation (40-F Glossary reconciliation and segment tables, $M)
de = {"BAM distributions": 1891, "AM direct investment distributions": 876, "WS DE (retained in BWS)": 1671,
      "BIP distributions": 356, "BEP distributions": 485, "BBU distributions": 24}
de["BPG distributions (1,602 - 356 - 485 - 24)"] = 1602 - 356 - 485 - 24
carry = 560
dtot = sum(de.values())
print("pre-corporate total before realizations", dtot, "; with carry", dtot + carry)
for k, v in de.items(): print(f"  {k:48s} {v:6d}  {pct(v, dtot):5.1f}%")
print("  fee engine (BAM dist + carry) share of total incl carry", pct(1891 + carry, dtot + carry))
print("  fee engine + WS share of total incl carry", pct(1891 + carry + 1671, dtot + carry))
print("  BIP+BEP+BBU share incl carry", pct(356 + 485 + 24, dtot + carry))
# (3) market value of quoted stakes 2026-09-11 (Yahoo, aggregator, flagged) x units (6-K Q2 quoted-value table / Q1)
mv = {"BAM 1,193.0M x 47.26": 1193.0 * 47.26, "BIP 207.1M x 36.88": 207.1 * 36.88, "BEP 309.4M x 30.39": 309.4 * 30.39,
      "BBUC 142.5M x 26.41": 142.5 * 26.41}
for k, v in mv.items(): print(f"  MV {k:30s} {v/1000:6.1f}bn")
gross = sum(mv.values()) / 1000 + 13.139 + 26.706 + 10.876
print("  gross (quoted at market; BWS, BPG, direct stakes at book, no double-count adjustment)", round(gross, 1))
for k, v in mv.items(): print(f"    share {k:28s} {pct(v/1000, gross):5.1f}%")
print("    share BWS book", pct(13.139, gross), " BPG book", pct(26.706, gross), " direct stakes", pct(10.876, gross))
print("    BIP+BEP+BBUC share", pct((mv['BIP 207.1M x 36.88'] + mv['BEP 309.4M x 30.39'] + mv['BBUC 142.5M x 26.41'])/1000, gross))
print("    BIP+BEP+BBUC share of book positive segments", pct(2097 + 4729 + 1016, tot))

print("\n== B. INSURANCE ROW: cost of funds on average invested assets ==")
# BN 40-F FY2025 WS table: cost of funds $3,889M; avg invested insurance assets $112,700M; 2024 $2,726M / $78,080M
print("BWS effective 2025", round(pct(3889, 112700), 2), " 2024", round(pct(2726, 78080), 2))
print("BWS NII 2025", round(pct(5642, 112700), 2), " real-asset gains", round(pct(776, 112700), 2))
print("BWS gross spread 2025", round(pct(5642 + 776 - 3889, 112700), 2), " ex real-asset gains", round(pct(5642 - 3889, 112700), 2))
# implied weight if effective = w*3.82 + (1-w)*0.55
w = (3.45 - 0.55) / (3.82 - 0.55); print("implied life&annuity weight if the two component rates blend to 3.45:", round(w, 3))
# Q2 2026: cost of funds 1,562 (quarter), avg invested insurance assets 165,855; Q2 2025 996 / 109,204
print("BWS Q2 2026 annualised", round(pct(1562 * 4, 165855), 2), " Q2 2025 annualised", round(pct(996 * 4, 109204), 2))
print("BWS Q2 2026 NII+gains-cof annualised", round(pct((2091 + 207 - 1562) * 4, 165855), 2), " ex gains", round(pct((2091 - 1562) * 4, 165855), 2))
# KKR Global Atlantic: net cost of insurance / average insurance investments (not a filed rate)
kkr_avg = (170144744 + 192009748) / 2
print("KKR/GA 2025 net cost of insurance / avg investments", round(pct(5229343, kkr_avg), 2),
      " NII / avg", round(pct(7224118, kkr_avg), 2), " spread", round(pct(7224118 - 5229343, kkr_avg), 2))

print("\n== C. [E3-46] return on common equity, IFRS, net income to shareholders less preferred dividends ==")
ni = {2022: 2056, 2023: 1130, 2024: 641, 2025: 1307}
pref = {2022: 150, 2023: 166, 2024: 168, 2025: 167}
ce = {2021: 42210, 2022: 39608, 2023: 41674, 2024: 41874, 2025: 43796}
for y in [2022, 2023, 2024, 2025]:
    print(y, round(pct(ni[y] - pref[y], (ce[y] + ce[y - 1]) / 2), 2), "%   DE/avg CE (BN's measure, not used):",
          {2024: round(pct(6274, (ce[2024] + ce[2023]) / 2), 1), 2025: round(pct(6008, (ce[2025] + ce[2024]) / 2), 1)}.get(y, "n/a"))
print("\n== D. real estate: BPG super core share ==")
print("super core NOI share FY2025", round(pct(1407, 3144), 1), "; super core equity / BPG equity YE2025", round(pct(19362, 25141), 1),
      "; super core equity / positive segments (book, 2026-06-30)", round(pct(19650, tot), 1))
print("super core NOI 2024->2025", round(pct(1407 - 1490, 1490), 1), "% ; BPG NOI", round(pct(3144 - 3397, 3397), 1), "%")
