# Owner earnings for SNOW from the filed cash-flow faces (cf_faces.txt): FY2019-21 from the FY2021 10-K,
# FY2021-23 from the FY2023 10-K, FY2024-26 from the FY2026 10-K, H1 FY2026/FY2027 from the Q2 FY2027 10-Q. $M.
import sys
sys.stdout.reconfigure(encoding="utf-8")
Y = ["FY2019","FY2020","FY2021","FY2022","FY2023","FY2024","FY2025","FY2026"]
ocf   = [-144.0,-176.6,-45.4,110.2,545.6,848.1,959.8,1221.9]
sbc   = [22.4,78.4,301.4,605.1,861.5,1168.0,1479.3,1599.5]   # face, net of capitalised
sbccap= [0.6,1.1,2.1,23.6,28.5,48.2,38.5,0.0]                 # supplemental: SBC in capitalised software
ppe   = [2.1,18.6,35.0,16.2,25.1,35.1,46.3,101.6]
capsw = [2.0,4.3,5.3,12.8,24.0,34.1,29.4,0.0]
da    = [1.4,3.5,9.8,21.5,63.5,119.9,182.5,220.4]
dref  = [79.6,223.0,312.9,526.2,514.3,528.0,382.8,755.2]      # deferred revenue line in OCF
acq_c = [0.0,6.3,6.0,0.0,362.6,275.7,30.3,178.9]
acq_s = [0.0,4.7,0.0,0.0,438.9,174.3,87.7,13.1]
nss   = [0.0,0.0,0.0,0.0,184.6,380.8,489.1,672.9]              # taxes paid on net share settlement (financing)
buy   = [29.6,0.0,0.0,0.0,0.0,591.7,1932.3,873.5]              # repurchases (FY2019 = issuer tender offer)
# TTM to 2026-07-31 = FY2026 + H1 FY2027 - H1 FY2026
ttm = dict(ocf=1221.9+334.6-303.3, sbc=1599.5+826.1-783.7, ppe=101.6+18.0-61.7, capsw=0.0, da=220.4+136.2-103.6,
           dref=755.2-807.2+323.9, acq_c=178.9+254.4-164.2)
rows = []
for i, y in enumerate(Y):
    s = sbc[i] + sbccap[i]
    cx = ocf[i] - s - ppe[i] - capsw[i]
    dd = ocf[i] - s - da[i]
    rows.append((y, ocf[i], s, ppe[i]+capsw[i], da[i], dref[i], cx, dd, cx - dref[i], dd - dref[i], ocf[i]-ppe[i]-capsw[i], acq_c[i]+acq_s[i], nss[i]+buy[i]))
print("year | OCF | SBC total | capex+capSW | D&A | deferred rev | OE capex end | OE D&A end | capex end ex-DR | D&A end ex-DR | FCF before SBC | acquisitions cash+stock | buybacks+net-settle taxes")
for r in rows: print(" | ".join([r[0]] + [f"{x:,.1f}" for x in r[1:]]))
t = ttm; s = t["sbc"]
print(f"TTM Jul-26 | {t['ocf']:,.1f} | {s:,.1f} | {t['ppe']:,.1f} | {t['da']:,.1f} | {t['dref']:,.1f} | {t['ocf']-s-t['ppe']:,.1f} | {t['ocf']-s-t['da']:,.1f} | {t['ocf']-s-t['ppe']-t['dref']:,.1f} | {t['ocf']-s-t['da']-t['dref']:,.1f} | {t['ocf']-t['ppe']:,.1f}")
def mean(ix, lo, hi): return sum(r[ix] for r in rows[lo:hi]) / (hi - lo)
for name, lo, hi in [("3y FY2024-26", 5, 8), ("5y FY2022-26", 3, 8), ("7y FY2020-26 (every year with a full filed statement set)", 1, 8)]:
    print(f"{name}: capex end {mean(6,lo,hi):,.1f} | D&A end {mean(7,lo,hi):,.1f} | capex ex-DR {mean(8,lo,hi):,.1f} | D&A ex-DR {mean(9,lo,hi):,.1f} | FCF before SBC {mean(10,lo,hi):,.1f} | acq {mean(11,lo,hi):,.1f} | DR {mean(5,lo,hi):,.1f} | SBC {mean(2,lo,hi):,.1f} | OCF {mean(1,lo,hi):,.1f}")
cum = lambda ix, lo, hi: sum(r[ix] for r in rows[lo:hi])
print(f"cumulative FY2019-26: OCF {cum(1,0,8):,.1f}; SBC {cum(2,0,8):,.1f}; SBC/OCF {100*cum(2,0,8)/cum(1,0,8):.0f}%; buybacks+net-settle FY2023-26 {cum(12,4,8):,.1f}")
