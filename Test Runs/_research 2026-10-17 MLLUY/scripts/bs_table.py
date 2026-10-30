"""Ten balance sheets, 2016-2025, from the consolidated balance sheets of each year's annual report
(HKEX 1618), RMB bn. Typed from the filed statements (cache/stmts_<year>.txt). Arithmetic only.
2016-2017: construction work in progress sat in inventories (pre-contract-asset standard); 2018:
bills and accounts receivable/payable filed as one line each."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
#        rev     rec(AR+notes+recfin)  contract_assets  lt_rec  other_rec  invent  ap(+notes)  borrowings(st+lt+bonds+ncl1y)  cash   perp   minority  eq_attrib  retained
D = {
2016: (219.6, 69.5 + 16.0, 0.0, 11.3, 31.4, 122.2, 112.0 + 17.6, 49.7 + 25.0 + 6.7 + 14.4, 44.9, 9.9, 12.6, 70.6, 16.2),
2017: (244.0, 73.5 + 20.8, 0.0, 23.5, 41.3, 118.3, 117.5 + 22.3, 39.4 + 23.5 + 7.1 + 18.4, 43.6, 17.9, 14.8, 82.5, 20.0),
2018: (289.5, 87.4, 66.7, 21.6, 56.4, 57.6, 141.0, 47.8 + 23.8 + 8.5 + 14.7, 44.5, 15.9, 18.7, 83.9, 23.5),
2019: (338.6, 66.0 + 7.9, 72.8, 24.3, 57.3, 60.6, 115.9 + 31.5, 40.5 + 27.2 + 1.7 + 15.7, 43.7, 25.9, 19.0, 97.9, 27.1),
2020: (400.1, 69.4 + 6.6, 83.2, 25.6, 64.2, 60.6, 133.7 + 30.5, 29.3 + 25.6 + 0.8 + 12.2, 53.1, 20.5, 42.5, 97.9, 32.5),
2021: (500.6, 83.9 + 3.4, 91.2, 30.4, 67.8, 61.8, 155.3 + 37.6, 21.4 + 25.3 + 0.2 + 13.2, 41.8, 23.7, 43.9, 107.5, 38.0),
2022: (592.7, 93.4 + 5.1, 106.8, 35.8, 48.1, 79.9, 187.2 + 37.2, 20.2 + 28.8 + 1.3 + 12.0, 45.5, 28.5, 40.8, 121.1, 45.1),
2023: (633.9, 130.0 + 5.6, 121.8, 50.8, 40.4, 80.1, 240.4 + 31.7, 28.2 + 34.2 + 3.3 + 8.0, 44.4, 47.4, 22.5, 145.5, 49.9),
2024: (552.0, 213.5 + 4.8 + 8.6, 156.3, 54.4, 42.2, 75.6, 335.1 + 30.1, 33.9 + 40.3 + 4.0 + 15.2, 52.6, 50.6, 29.3, 153.0, 52.7),
2025: (455.4, 243.4 + 5.4 + 9.1, 189.5, 51.7, 59.4, 15.7, 396.6 + 25.6, 22.1 + 41.4 + 2.0 + 14.5, 77.8, 54.1, 27.8, 155.8, 51.3),
}
print("year  rev | rec+CA+LTrec  %rev | AP+notes %rev | borrow  cash | perp  minor | ordinary book (eq_attrib-perp)")
for y, (rev, rec, ca, ltr, orc, inv, ap, bor, cash, perp, mi, eq, ret) in D.items():
    r = rec + ca + ltr
    print(f"{y} {rev:6.1f} | {r:6.1f} {100*r/rev:5.0f}% | {ap:6.1f} {100*ap/rev:4.0f}% | {bor:5.1f} {cash:5.1f} | {perp:4.1f} {mi:5.1f} | {eq-perp:6.1f}")
