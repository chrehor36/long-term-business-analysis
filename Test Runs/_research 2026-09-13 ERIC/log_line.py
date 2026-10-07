p = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\_daily\OVERNIGHT LOG.md"
s = open(p, encoding='utf-8').read()
assert '| ERIC |' not in s
line = ("- 2026-09-13 14:02 EDT | ERIC | Q1 IN / Q2 OUT (on the business as constituted, on [E3-03] criterion 2 and [E4-04]; Q3-Q6 recorded, "
        "not governing; resumed after the 07:46 session limit with Step 0 on disk; companyfacts HAD ingested the FY2025 20-F - the skip was "
        "run.py carrying only US-GAAP tag names; SEK 10-yr sovereign from the Riksbank by hand, 10-year tenor limit stated; A and B shares "
        "summed after reading the charter, the 20-F cover count found to be the issued count; radio margin 6-18 points above Nokia in every "
        "5G year but operators dual-source and re-tender; Q3 UNKNOWABLE on the DOJ Iraq, ATA and CFIUS matters still open; no new survival "
        "shape) | SEK 98.66 (2026-09-11 close) | PASS | 2c1d4ad\n")
if not s.endswith('\n'): s += '\n'
open(p, 'w', encoding='utf-8').write(s + line)
print('appended')
