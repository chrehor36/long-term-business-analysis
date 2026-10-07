# Owner earnings for TSLA from the filed cash-flow faces ($M): FY2021-23 from the FY2023 10-K, FY2023-25 from the
# FY2025 10-K, H1 2025/2026 from the Q2 2026 10-Q. SBC made complete with the capitalised part (equity note, each 10-K).
# (c) two ends: total cash capex (face, incl. solar systems lines FY2021-23) and PP&E depreciation (PP&E note).
import sys; sys.stdout.reconfigure(encoding="utf-8")
Y    = ["FY2021","FY2022","FY2023","FY2024","FY2025"]
ocf  = [11497, 14724, 13256, 14923, 14747]
sbc  = [2121, 1560, 1812, 1999, 2825]
sbcc = [182, 245, 199, 198, 238]            # SBC capitalised to the balance sheet
capx = [6482+32, 7158+5, 8899, 11342, 8527] # PP&E excl. finance leases net of sales (+ solar systems FY21-22; FY2023 as re-presented 8,899)
dep  = [1910, 2420, 3330, 4120, 5030]       # depreciation of PP&E (PP&E note)
flp  = [439, 502, 464, 381, 104]            # principal payments on finance leases (financing)
wc   = [667, -3712, -2248, 81, 642]         # sum of 'changes in operating assets and liabilities' lines on the face
cred = [1465, 1776, 1790, 2763, 1993]       # regulatory credits (cash, no cost)
ni   = [5644, 12587, 14974, 7153, 3855]
rows=[]
for i,y in enumerate(Y):
    s=sbc[i]+sbcc[i]
    rows.append((y, ocf[i], s, capx[i], dep[i], ocf[i]-s-capx[i], ocf[i]-s-dep[i], ocf[i]-s-capx[i]-flp[i], wc[i], cred[i], ni[i]))
print("year | OCF | SBC complete | capex | PP&E dep | OE capex end | OE dep end | capex end less finance-lease principal | WC lines | credits | net income")
for r in rows: print(" | ".join([r[0]]+[f"{x:,}" for x in r[1:]]))
# TTM to 2026-06-30
t_ocf=14747+8634-4696; t_sbc=2825+2181-1208; t_cap=8527+8282-3886; t_dep=5030+2710-2300
print(f"TTM Jun-26 | {t_ocf:,} | {t_sbc:,} (+ capitalised part not disclosed quarterly) | {t_cap:,} | {t_dep:,} | {t_ocf-t_sbc-t_cap:,} | {t_ocf-t_sbc-t_dep:,}")
m=lambda ix,lo,hi: sum(r[ix] for r in rows[lo:hi])/(hi-lo)
for n,lo,hi in [("5y FY2021-25",0,5),("3y FY2023-25",2,5)]:
    print(f"{n}: capex end {m(5,lo,hi):,.0f} | dep end {m(6,lo,hi):,.0f} | capex end less FL principal {m(7,lo,hi):,.0f} | OCF {m(1,lo,hi):,.0f} | SBC {m(2,lo,hi):,.0f} | capex {m(3,lo,hi):,.0f} | dep {m(4,lo,hi):,.0f} | credits {m(9,lo,hi):,.0f} | WC {m(8,lo,hi):,.0f} | NI {m(10,lo,hi):,.0f}")
print("capex/dep by year:", [round(c/d,2) for c,d in zip(capx,dep)], "5y", round(sum(capx)/sum(dep),2))
print("SBC/OCF 5y:", round(100*sum(r[2] for r in rows)/sum(ocf),1), "%")
