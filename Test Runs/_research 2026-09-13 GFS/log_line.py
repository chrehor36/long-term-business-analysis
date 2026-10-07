p = r"C:\Users\chreh\OneDrive\Documents\BRK\Screens\_daily\OVERNIGHT LOG.md"
import sys
h = sys.argv[1]
s = open(p, encoding='utf-8').read()
assert '| GFS |' not in s
line = ("- 2026-09-13 EDT | GFS | Q1 IN / Q2 OUT (on the business, on [E3-03] criterion 2 as [E3-43] demonstrates it and [E2-44](1); "
        "Q3-Q6 recorded, not governing; IFRS in USD, companyfacts has seven USD years incl. FY2025 - unpriceable only by run.py's US-GAAP tag names; "
        "USD 30-yr 5.35% from the US Treasury; 548,751,082 issued and outstanding at 2026-06-30 plus 9,907,399 agreed for the Department of Commerce "
        "at $37.85 = 558,658,481 (ERIC trap does not fire, repurchases cancelled); Mubadala 81.0% -> 72.82%; filed ASP flat in 2023 on shortfall payments, "
        "-3% and -10.4% after, the second 'where customers are dual sourced'; ROE 5-yr 5.6%; prepayments in operating cash, TSM's strip followed; "
        "owner earnings $234-519M, gruesome; buybacks of $500M from Mubadala above value; PSU yardsticks replaced; material weaknesses 2023-25; "
        "THE PASS-THROUGH likely, THE PATRON proposed) | US$46.95 (2026-09-11 close) | PASS | " + h + "\n")
if not s.endswith('\n'):
    s += '\n'
open(p, 'w', encoding='utf-8').write(s + line)
print('appended')
