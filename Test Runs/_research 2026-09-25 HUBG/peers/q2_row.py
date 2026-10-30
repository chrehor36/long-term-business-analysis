"""Q2 competitor row, re-derived by the resume session of 2026-09-25 (night).
Uses the metric functions of hubg_row.py (written by an uncommitted session) after reading them, with one
change: the revenue tag list gains RevenueFromContractWithCustomerIncludingAssessedTax, so JBHT's 2018+
revenue resolves. TRANSCRIPTION AND ARITHMETIC ONLY, NO CONCLUSION. Prints 5-year means for the reliable
window FY2018-FY2022 and the FY2013-FY2022 ten-year window."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hubg_row as H
H.SALES = H.SALES + ["RevenueFromContractWithCustomerIncludingAssessedTax"]
yrs = list(range(2008, 2026))
def summ(tk, rows, a, b):
    om = [m['om'] for y, m in rows if m and a <= y <= b and m['om'] is not None]
    rt = [m['ret'] for y, m in rows if m and a <= y <= b and m['ret'] is not None]
    f = lambda L: (f"{sum(L)/len(L):.1%} (n={len(L)}, min {min(L):.1%}, max {max(L):.1%})" if L else "n/f")
    print(f"  {tk} FY{a}-{b}: op margin mean {f(om)} | op inc/avg NTOA mean {f(rt)}")
if __name__ == "__main__":
    out = {}
    r = H.metrics("HUBG", yrs, cutoff="2023-02-28"); H.show("HUBG", r, "(filed on or before 2023-02-28: NOT WITHDRAWN)"); out["HUBG"] = r
    H.show("HUBG", H.metrics("HUBG", yrs, after="2023-02-28"), "(filed after 2023-02-28: FY2023-24 WITHDRAWN)")
    for tk in ["JBHT", "SNDR", "KNX", "LSTR", "CHRW", "RXO", "ARCB", "FWRD", "WERN", "GXO"]:
        r = H.metrics(tk, yrs); H.show(tk, r); out[tk] = r
    print("=" * 80); print("MEANS")
    for tk, r in out.items():
        summ(tk, r, 2018, 2022); summ(tk, r, 2013, 2022)
