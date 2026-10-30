"""Q2 competitor row: the field's returns over 2015-2025 from each company's own annual reports.
Figures typed from the filed summaries (RMB million). Sources:
 MCC: consolidated statements of the 2016-2025 annual reports (HKEX 1618), total profit and total equity.
 CREC (China Railway Group, HKEX 0390): 2025 AR pp.4-5 financial summary (2021-2025); 2019 AR pp.2-3 (2015-2019).
 CRCC (China Railway Construction, HKEX 1186): 2025 AR Section X five years' summary (2021-2025);
   2019 AR Section XIV (2015-2019). 2020 for CREC and CRCC not read (2022 ARs not opened): gap.
Metric: pre-tax profit / revenue, and pre-tax profit / year-end total equity (total equity includes
minority interests and perpetual instruments for all three, so the three are on one footing).
Arithmetic only."""

data = {
    "MCC": {  # year: (revenue, pretax, total_equity)
        2015: (217324, 7143, 71155), 2016: (219558, 7648, 83108), 2017: (244000, 8975, 97320),
        2018: (289535, 9524, 102669), 2019: (338638, 9782, 116906), 2020: (400115, 11917, 140355),
        2021: (500572, 14012, 151388), 2022: (592669, 15392, 161909), 2023: (633870, 13765, 167991),
        2024: (552025, 9255, 182336), 2025: (455380, 5009, 183559)},
    "CREC": {
        2015: (599942, 17017, 139238), 2016: (632856, 18772, 148996), 2017: (688773, 20828, 169558),
        2018: (740383, 24945, 221981), 2019: (850843, 33187, 245328),
        2021: (1073272, 39636, 358158), 2022: (1154349, 44692, 422869), 2023: (1263412, 47581, 459754),
        2024: (1160311, 40613, 509992), 2025: (1093494, 34451, 540450)},
    "CRCC": {
        2015: (600539, 17113, 128819), 2016: (629327, 18970, 148716), 2017: (680981, 21256, 178649),
        2018: (730123, 25105, 207335), 2019: (830452, 28027, 262022),
        2021: (1020010, 35151, 346356), 2022: (1096313, 37824, 385920), 2023: (1137993, 38828, 417120),
        2024: (1067171, 32475, 422597), 2025: (1029784, 26933, 426955)},
}

print("pre-tax margin % / pre-tax return on year-end total equity %")
years = sorted({y for d in data.values() for y in d})
print("year  " + "  ".join(f"{n:>15}" for n in data))
for y in years:
    cells = []
    for n, d in data.items():
        if y in d:
            r, p, e = d[y]
            cells.append(f"{100*p/r:5.2f} / {100*p/e:5.2f}")
        else:
            cells.append(f"{'n/r':>15}")
    print(f"{y}  " + "  ".join(f"{c:>15}" for c in cells))
for n, d in data.items():
    ys = sorted(d)
    m = sum(d[y][1] for y in ys) / sum(d[y][0] for y in ys)
    e = sum(d[y][1] / d[y][2] for y in ys) / len(ys)
    print(f"{n}: span {ys[0]}-{ys[-1]} ({len(ys)} yrs) aggregate pre-tax margin {100*m:.2f}%, mean pre-tax return on total equity {100*e:.2f}%")
