"""Owner cash after every real cost, WMT, from the filed cash-flow statements and notes ($ millions).
Sources (all Walmart 10-Ks): FY2024-FY2026 from 0000104169-26-000055 (cash-flow statement; SBC note: 3,603 / 2,769 / 2,093;
finance-lease financing cash flows 891 / 908 / 1,055 in the lease note); FY2022-FY2023 from 0000104169-23-000020
(OCF 28,841 / 24,181, capex 16,857 / 13,106, SBC 1,578 / 1,163, finance-lease 563 / 538, NCI dividends 444 / 424);
FY2020-FY2021 from 0000104169-21-000033 (OCF 36,074 / 25,255, capex 10,264 / 10,705, SBC 1,169 / 854,
finance-lease 546 / 485, NCI dividends 434 / 555).
Owner cash (capex basis) = OCF - SBC - all capex - finance-lease principal - dividends to noncontrolling partners.
Owner cash (D&A basis)   = OCF - SBC - D&A        - finance-lease principal - dividends to noncontrolling partners.
SBC is subtracted because the filed OCF adds it back as non-cash; it is a real cost (paid in shares).
"""
rows = {  # FY: (OCF, capex, SBC, D&A, finlease, nci_div)
    2020: (25255, 10705, 854, 10987, 485, 555),
    2021: (36074, 10264, 1169, 11152, 546, 434),
    2022: (24181, 13106, 1163, 10658, 538, 424),
    2023: (28841, 16857, 1578, 10945, 563, 444),
    2024: (35726, 20606, 2093, 11853, 1055, 763),
    2025: (36443, 23783, 2769, 12973, 908, 576),
    2026: (41565, 26642, 3603, 14203, 891, 439),
}
oc_c, oc_d = {}, {}
print("FY    OCF    capex  SBC    D&A    finL  NCIdiv  OC_capex  OC_D&A")
for fy, (ocf, cx, sbc, da, fl, nci) in rows.items():
    oc_c[fy] = ocf - sbc - cx - fl - nci
    oc_d[fy] = ocf - sbc - da - fl - nci
    print(f"{fy}  {ocf:6d} {cx:6d} {sbc:5d} {da:6d} {fl:5d} {nci:5d}  {oc_c[fy]:8d} {oc_d[fy]:7d}")
five = [2022, 2023, 2024, 2025, 2026]
avg_c = sum(oc_c[y] for y in five) / 5
avg_d = sum(oc_d[y] for y in five) / 5
print(f"five-year mean FY2022-FY2026: capex basis {avg_c:,.0f}; D&A basis {avg_d:,.0f}")
# growth shown, aggregate, endpoints of the five-year window (four intervals)
g_c = (oc_c[2026] / oc_c[2022]) ** 0.25 - 1
g_d = (oc_d[2026] / oc_d[2022]) ** 0.25 - 1
print(f"growth FY2022->FY2026 (4 yrs): capex basis {g_c:.1%}; D&A basis {g_d:.1%}")
# the operating income line as a steadier read of the earning power (filed income statements)
opinc = {2020: 20568, 2021: 22548, 2022: 25942, 2023: 20428, 2024: 27012, 2025: 29348, 2026: 29825}
print("operating income FY2020..FY2026:", opinc)
print(f"op income growth FY2021->FY2026 (5 yrs): {(opinc[2026]/opinc[2021])**0.2-1:.1%}")
