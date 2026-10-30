p = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\_daily\OVERNIGHT LOG.md"
s = open(p, encoding='utf-8').read()
assert '| SPOT |' not in s
line = ("- 2026-09-13 16:30 EDT | SPOT | Q1 IN / Q2 OUT (on the business as constituted, on [E3-03] criterion 2 with [E4-04] and [E3-43]/[E3-46]; "
        "Q3-Q6 recorded, not governing; companyfacts holds ten EUR IFRS years incl. FY2025 - unpriceable only by the USD-unit filter and US-GAAP names; "
        "EUR 30-yr 3.83% from the ECB, cap converted at the ECB reference rate 1.1592; no ADR; 20-F cover count is outstanding (ERIC trap does not fire); "
        "beneficiary certificates carry no economic right and are excluded; UMG says all services carry all content, price rises parallel across "
        "Spotify, Apple, YouTube, Amazon, Deezer; labels took 50-64% of Premium revenue increments; owner earnings EUR 95M-2,186M across windows, "
        "UNKNOWABLE on the range; buybacks at ~US$664 above every computed value; proposed thirteenth shape THE TENANT) | US$525.75 (2026-09-11 close) | PASS | 87bd1d7\n")
if not s.endswith('\n'):
    s += '\n'
open(p, 'w', encoding='utf-8').write(s + line)
print('appended')
