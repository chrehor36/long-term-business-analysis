"""PM owner cash after every real cost, USD millions, from the filed statements.
Sources (cash-flow statements and statements of stockholders' deficit):
  FY2018-2020: 10-K FY2020, accession 0001413329-21-000007
  FY2021-2023: 10-K FY2023, accession 0001413329-24-000013
  FY2024-2025: 10-K FY2025, accession 0001628280-26-005939
SBC = "Issuance of stock awards" in the equity statement (the stock pay credited to equity; the
cash-flow statement carries no separate SBC line, it sits in "Other"). NCI = dividends/payments
to noncontrolling interests in the equity statement (cash paid to the minority owners of
consolidated subsidiaries, a real cost to PM's owners).
"""
rows = {
#  yr:  (OCF,   SBC, capex,  D&A,  NCI,  netrev, acq_and_rights, buyback, dividends)
 2018: (9478,  128, 1436,  989,  435, 29625,     0,    0, 6885),
 2019: (10090, 160,  852,  964,  378, 29805,  1346,    0, 7161),  # 1346 = cash removed on RBH deconsolidation
 2020: (9812,  160,  602,  981,  602, 28694,     0,    0, 7364),
 2021: (11967, 197,  748,  998,  560, 31405,  2111,  775, 7580),
 2022: (10803, 155, 1077, 1077,  472, 31762, 13976+1002+1495, 209, 7812),
 2023: (9204,  193, 1321, 1398,  497, 35174,  1775+883,    0, 7964),
 2024: (12217, 195, 1444, 1787,  494, 37878,   -43,    0, 8197),
 2025: (12233, 208, 1569, 1996,  430, 40648,     0,    0, 8624),
}
print("FY    OCF    SBC  capex   D&A   NCI | OC capex  OC D&A | acq/rights  dividends")
oc = {}
for y, (ocf, sbc, cap, da, nci, rev, acq, bb, div) in rows.items():
    a = ocf - sbc - cap - nci
    b = ocf - sbc - da - nci
    oc[y] = (a, b)
    print(f"{y} {ocf:6} {sbc:5} {cap:6} {da:5} {nci:5} | {a:7} {b:7} | {acq:9} {div:9}")
five = [2021, 2022, 2023, 2024, 2025]
ma = sum(oc[y][0] for y in five) / 5
mb = sum(oc[y][1] for y in five) / 5
print(f"5-yr mean 2021-2025: capex basis {ma:.0f}; D&A basis {mb:.0f}")
eight_a = sum(oc[y][0] for y in rows) / len(rows)
print(f"8-yr mean 2018-2025 capex basis {eight_a:.0f}")
# growth shown on aggregate owner cash (capex basis), first to last of the five-year window
g5 = (oc[2025][0] / oc[2021][0]) ** (1 / 4) - 1
g7 = (oc[2025][0] / oc[2018][0]) ** (1 / 7) - 1
print(f"growth 2021->2025 (4 yrs) capex basis: {g5*100:.2f}%/yr; 2018->2025 (7 yrs): {g7*100:.2f}%/yr")
gr = (rows[2025][5] / rows[2018][5]) ** (1 / 7) - 1
print(f"net revenue growth 2018->2025: {gr*100:.2f}%/yr")
tot_oc = sum(oc[y][0] for y in rows); tot_div = sum(rows[y][8] for y in rows)
tot_acq = sum(rows[y][6] for y in rows); tot_bb = sum(rows[y][7] for y in rows)
print(f"2018-2025 sums: owner cash {tot_oc}; dividends {tot_div}; acquisitions/rights {tot_acq}; buybacks {tot_bb}")
print(f"gap (dividends+acq+buybacks - owner cash) = {tot_div+tot_acq+tot_bb-tot_oc}")
