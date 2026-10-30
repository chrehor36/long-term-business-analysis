# every input from the filed cash-flow faces, $K (FY2017-19 FY2019 10-K; FY2020 FY2020/21 10-Ks; FY2021-22 FY2022 10-K,
# FY2022 D&A as restated on the FY2024 face; FY2023-24 FY2024 10-K; FY2025-26 FY2026 10-K)
Y   = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
OCF = [-4495,-1351,-5637,-2024,-2701, 1508,10011, 1756,-7400,-3310]
SBC = [  999,  996,  905,  910, 1101, 3006, 2748, 2518, 5162, 6761]
DA  = [  271,  417,  431,  384,  310,  356,  450,  657, 2312, 2799]
CAP = [  477,  572,  173,  163,  227,  416, 1362,  749, 4992, 2066]
ACQ = [    0,    0,    0,    0,    0,    0,    0,    0,11075, 1801]
WC  = [ -313,-3234,-1735, -561,  316,-10295,-7841,-14378,-12203,-1760]   # sum of 'changes in operating assets and liabilities' lines
INV = [  430,-2073, -112, 1164, -972,-6674,-9469,-13732,-2441,   11]
REV = [18898,29555,21056,22291,16600,50829,64961,66218,58968,50001]
rows = []
print("FY    OCF    SBC   D&A  capex   acq |  OE(D&A)  OE(capex)  OE(capex+acq) | WC chg  (inv) | OE before WC (D&A end) | SBC/OCF")
for i, y in enumerate(Y):
    a = OCF[i]-SBC[i]-DA[i]; b = OCF[i]-SBC[i]-CAP[i]; c = b-ACQ[i]; d = a-WC[i]
    rows.append((a,b,c,d))
    print(f"{y} {OCF[i]:6} {SBC[i]:6} {DA[i]:5} {CAP[i]:6} {ACQ[i]:5} | {a:8} {b:9} {c:13} | {WC[i]:7} {INV[i]:7} | {d:8} | {'n/a' if OCF[i]<=0 else f'{100*SBC[i]/OCF[i]:.0f}%'}")
def win(lo, hi, lab):
    idx = [i for i, y in enumerate(Y) if lo <= y <= hi]; n = len(idx)
    m = [sum(rows[i][k] for i in idx)/n for k in range(4)]
    r = sum(REV[i] for i in idx)/n
    print(f"{lab:28} mean OE: D&A end {m[0]:8.0f}  capex end {m[1]:8.0f}  capex+acq {m[2]:8.0f}  | before WC (D&A end) {m[3]:7.0f} | mean revenue {r:7.0f}")
win(2022, 2026, "5y FY2022-26 (default)")
win(2024, 2026, "3y FY2024-26")
win(2017, 2026, "10y FY2017-26")
win(2022, 2024, "the wave FY2022-24")
win(2017, 2021, "before the wave FY2017-21")
pos = [(Y[i], rows[i][1]) for i in range(len(Y)) if rows[i][1] > 0]
print("years with positive OE (capex end):", pos)
