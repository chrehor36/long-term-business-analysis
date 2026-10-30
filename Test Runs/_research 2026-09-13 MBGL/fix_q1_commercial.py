RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - MBGL Mobility Global.md"
s = open(RUN, encoding="utf-8").read()
old = """  separation (10-Q supplemental: *"Consolidation of Canada Carfax Loan $230"*). **No commercial
  supply or customer agreement between the two companies is described in the 8-K as a separation
  agreement.**"""
new = """  separation (10-Q supplemental: *"Consolidation of Canada Carfax Loan $230"*).
- **Commercial data agreements** (Information Statement, "Commercial Arrangements"; the 8-K does not
  list them; the 10-Q names *"other commercial arrangements"*): *"(i) we will provide S&P Global with a
  non-exclusive right to use certain Mobility data products for internal business purposes and derived
  data creation across certain S&P Global business divisions and (ii) S&P Global ... will provide us
  with a non-exclusive right to use certain S&P Global data products"*, on *"multiyear terms"* and
  *"arms-length terms"*; the company's own words: *"These agreements are not material to us."*
  *(Corrected before commit: a first draft of this line said no commercial agreement was described; the
  8-K is silent, the Information Statement is not.)*"""
assert old in s
s = s.replace(old, new)
old2 = """SPGI awards held by MBGL staff were converted into MBGL awards (10-Q Note 9) — a dilution source, measured at Q4."""
if old2 in s:
    s = s.replace(old2, """SPGI awards held by MBGL staff were converted into MBGL awards under the 2026 Long Term Incentive Plan (10-Q, Subsequent Events) — a dilution source, measured at Q4.""")
open(RUN, "w", encoding="utf-8").write(s)
print("ok")
