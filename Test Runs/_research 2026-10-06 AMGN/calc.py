"""Arithmetic for the AMGN run of 2026-10-06. Inputs are filed figures (USD M) with their sources; no judgment here."""
# Cash-flow statement lines: 10-K FY2025 0000318154-26-000010 (2023-2025); 10-K FY2022 0000318154-23-000017 (2022);
# 10-K FY2021 0000318154-22-000010 (2021), via SEC companyfacts (facts_output.txt), 2023-2025 checked to the filed statement.
ocf = {2021: 9261, 2022: 9721, 2023: 8471, 2024: 11490, 2025: 9958}
sbc = {2021: 341, 2022: 401, 2023: 431, 2024: 530, 2025: 494}
capex = {2021: 880, 2022: 936, 2023: 1112, 2024: 1096, 2025: 1858}
dna = {2021: 3398, 2022: 3417, 2023: 4071, 2024: 5592, 2025: 5167}
acq = {2021: 2529, 2022: 3839, 2023: 26989, 2024: 0, 2025: 53}
print('FY   OCF   SBC  capex  OC(capex)  D&A  OC(D&A)  acquisitions  OC after acquisitions')
oc_c, oc_d, oc_a = [], [], []
for y in ocf:
    a = ocf[y] - sbc[y] - capex[y]; b = ocf[y] - sbc[y] - dna[y]; c = a - acq[y]
    oc_c.append(a); oc_d.append(b); oc_a.append(c)
    print(y, ocf[y], sbc[y], capex[y], a, dna[y], b, acq[y], c)
m = lambda xs: sum(xs) / len(xs)
print('five-year mean: capex basis %.0f; D&A basis %.0f; after acquisitions %.0f' % (m(oc_c), m(oc_d), m(oc_a)))
print('shown change of aggregate owner cash, capex basis, 2021->2025: %.2f%% a year' % ((oc_c[-1] / oc_c[0]) ** 0.25 * 100 - 100))
price, shares = 402.98, 540.632005
cap = price * shares
print('market cap $%.0fM; owner-cash yield on five-year mean, capex basis %.2f%%, after acquisitions %.2f%%' % (cap, m(oc_c) / cap * 100, m(oc_a) / cap * 100))
# Product sales 2025 (10-K FY2025 MD&A) and the US patent table (Item 1, Patents)
ps = {'Prolia': 4414, 'XGEVA': 2084, 'Repatha': 3016, 'Otezla': 2265, 'ENBREL': 2226, 'EVENITY': 2100, 'TEPEZZA': 1903,
      'Nplate': 1524, 'KYPROLIS': 1412, 'KRYSTEXXA': 1340}
tot = 35148
s = sum(ps.values())
print('principal products whose first-listed US patent (antibody, compound, protein; Nplate formulation) has expired or expires by 2029: $%dM = %.1f%% of 2025 product sales' % (s, s / tot * 100))
# Q2 2026 (EX-99.1 of 8-K 0000318154-26-000124): denosumab pair after loss of exclusivity
q2_26 = 759 + 352; q2_25 = 1122 + 532
print('Prolia+XGEVA Q2 2026 vs Q2 2025: %d vs %d, %.1f%%' % (q2_26, q2_25, (q2_26 / q2_25 - 1) * 100))
print('ENBREL 2023->2025: 3697 -> 2226, %.1f%%' % ((2226 / 3697 - 1) * 100))
