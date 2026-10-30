"""The segment table, transcribed by hand from each FY 10-K's MD&A sentences (cache/seg2.txt, produced from the
10-K texts; accessions in tenk_accessions.txt). Prints margins, five-year shares, cycle comparisons and compound
organic growth to segments_table.txt (committed). Organic ("internal") growth is the filer's own reported
percentage for the whole company; for 2009-2013 the filer reported it by group only and the company figure is the
sales-weighted mean of the two group figures (marked w)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
# year: (EIG sales, EIG OI, EMG sales, EMG OI, company organic %, mark)
D = {
    2005: (808.5, 164.2, 626.0, 99.2, None, ""),
    2006: (1016.5, 203.4, 802.8, 139.9, 9, "w"),
    2007: (1199.8, 260.3, 937.1, 167.2, 7, ""),
    2008: (1402.7, 306.8, 1128.5, 175.2, 4, ""),
    2009: (1146.6, 232.9, 951.8, 166.6, -20.5, "w"),
    2010: (1324.1, 316.2, 1146.8, 210.4, 13.6, "w"),
    2011: (1647.2, 420.2, 1342.7, 262.7, 11.5, "w"),
    2012: (1872.6, 497.1, 1461.7, 292.2, 1.2, "w"),
    2013: (2034.6, 552.1, 1559.5, 309.4, 1.6, "w"),
    2014: (2421.6, 613.0, 1600.3, 335.0, 3, ""),
    2015: (2417.2, 639.4, 1557.1, 318.1, -1.4, "w"),
    2016: (2360.3, 577.7, 1479.8, 277.9, -6.6, "w"),
    2017: (2690.6, 677.5, 1609.6, 310.9, 6, ""),
    2018: (3029.0, 782.1, 1816.9, 363.8, 7, ""),
    2019: (3322.9, 865.3, 1835.7, 387.9, 2, ""),
    2020: (2989.9, 770.6, 1550.1, 325.0, -13, ""),
    2021: (3763.8, 958.2, 1782.8, 437.4, 15, ""),
    2022: (4229.4, 1089.7, 1921.2, 503.6, 11, ""),
    2023: (4624.3, 1311.0, 1972.7, 496.6, 4, ""),
    2024: (4659.9, 1428.4, 2281.3, 456.5, -2, ""),
    2025: (4919.1, 1447.1, 2482.0, 578.9, 2, ""),
}
L = ["year   EIG sales  EIG OI  EIG mgn   EMG sales  EMG OI  EMG mgn   EIG share of seg. OI   organic %"]
for y, (es, eo, ms, mo, org, mk) in D.items():
    L.append(f"{y}   {es:9,.1f} {eo:7,.1f}  {eo/es*100:5.1f}%   {ms:9,.1f} {mo:7,.1f}  {mo/ms*100:5.1f}%   {eo/(eo+mo)*100:5.1f}%"
             f"                {'' if org is None else f'{org:+.1f}{mk}'}")
for a, b in [(2021, 2025), (2016, 2020), (2011, 2015)]:
    e = sum(D[y][1] for y in range(a, b + 1)); m = sum(D[y][3] for y in range(a, b + 1))
    L.append(f"five years {a}-{b}: EIG OI {e:,.1f}  EMG OI {m:,.1f}  EIG share {e/(e+m)*100:.1f}%")
# cycles: peak-to-trough
for pk, tr in [(2008, 2009), (2019, 2020), (2015, 2016)]:
    L.append(f"cycle {pk}->{tr}: EIG sales {D[tr][0]/D[pk][0]*100-100:+.1f}%  EIG OI {D[tr][1]/D[pk][1]*100-100:+.1f}%  "
             f"EIG margin {D[pk][1]/D[pk][0]*100:.1f}->{D[tr][1]/D[tr][0]*100:.1f}  EMG OI {D[tr][3]/D[pk][3]*100-100:+.1f}%  "
             f"EMG margin {D[pk][3]/D[pk][2]*100:.1f}->{D[tr][3]/D[tr][2]*100:.1f}")
# compound organic vs total sales growth
def comp(a, b):
    g = 1.0
    for y in range(a + 1, b + 1):
        g *= 1 + D[y][4] / 100
    tot = (D[b][0] + D[b][2]) / (D[a][0] + D[a][2])
    n = b - a
    return g ** (1 / n) - 1, tot ** (1 / n) - 1
for a, b in [(2005, 2025), (2008, 2019), (2010, 2025), (2015, 2025), (2019, 2025)]:
    o, t = comp(a, b)
    L.append(f"compound {a}-{b}: organic {o*100:+.2f}%/yr   total segment sales {t*100:+.2f}%/yr")
open(os.path.join(HERE, "segments_table.txt"), "w", encoding="utf-8").write("\n".join(L) + "\n")
