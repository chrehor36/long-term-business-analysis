# Parts table for Q1/Q2 (business of parts, five-year operating profit). USD millions.
# Sources: FY2025 10-K Note 5 (segment Adjusted EBITDA), MD&A (leasing depreciation), Note 4 (MER intangibles:
# customer relationships 65.9 over 9.3 yrs, trademarks 8.0 over 5 yrs), companyfacts OperatingIncomeLoss;
# 10-Q 2026-06-30 Note (segments) and income statement.
# CONVENTION of the run: segment operating profit = segment Adjusted EBITDA less the D&A the filing ties to the
# part; corporate costs, stock pay and other items allocated pro rata to segment operating profit.
op_income = {2021: -0.4, 2022: 41.8, 2023: 49.9, 2024: 52.8, 2025: 135.4}
mer_amort = 65.9/9.3 + 8.0/5
pw = {}; lg = {}
for y in (2021, 2022, 2023):
    lg[y] = op_income[y]; pw[y] = 0.0
seg = {2024: dict(pw_ebitda=26.8, lg_ebitda=97.6, lease_dep=6.035, amort=mer_amort*111/365, da=47.218),
       2025: dict(pw_ebitda=189.1, lg_ebitda=88.9, lease_dep=34.353, amort=mer_amort+0.1, da=84.285)}
for y, s in seg.items():
    pda = s['lease_dep'] + s['amort']; lda = s['da'] - pda
    p = s['pw_ebitda'] - pda; l = s['lg_ebitda'] - lda
    corp = op_income[y] - p - l
    pw[y] = p + corp * p/(p+l); lg[y] = l + corp * l/(p+l)
    print(y, f"power seg OP {p:.1f} logistics seg OP {l:.1f} corporate etc {corp:.1f} -> power {pw[y]:.1f} logistics {lg[y]:.1f}")
P = sum(pw.values()); L = sum(lg.values())
print(f"FY2021-2025: power {P:.1f}  logistics {L:.1f}  total {P+L:.1f}  logistics share {L/(P+L)*100:.1f}%")
# Trailing five years to 2026-06-30 (drops 1H2021, adds 1H2026); 1H2021 not read, shown at zero and at -5/+5.
h = dict(pw_ebitda=168.3, lg_ebitda=48.0, lease_dep=38.986, amort=mer_amort/2, da=64.3, oi=107.072)
pda = h['lease_dep'] + h['amort']; lda = h['da'] - pda
p = h['pw_ebitda'] - pda; l = h['lg_ebitda'] - lda; corp = h['oi'] - p - l
p26 = p + corp*p/(p+l); l26 = l + corp*l/(p+l)
print(f"1H2026: power {p26:.1f} logistics {l26:.1f}")
for h21 in (-5, 0, 5):
    Pt = P + p26; Lt = L - h21 + l26  # removing 1H2021 (logistics) = subtract its op income
    print(f"trailing (1H2021 op income {h21:+}): power {Pt:.1f} logistics {Lt:.1f} power share {Pt/(Pt+Lt)*100:.1f}%")
# Reported segment Adjusted EBITDA check (company Adjusted EBITDA 2021-2023 from the 10-Ks: about 30, 83, 96)
lgE = 30 + 83 + 96 + 97.6 + 88.9; pwE = 26.8 + 189.1
print(f"Adjusted EBITDA FY2021-2025: logistics {lgE:.1f} power {pwE:.1f} logistics share {lgE/(lgE+pwE)*100:.1f}%")
