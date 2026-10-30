# Owner earnings from filed cash-flow faces ($M): OCF - SBC - (c); (c) at capex end and D&A end.
# FY2021-23 from FY2023 10-K face (FY2021 also FY2021 10-K); FY2023-25 from FY2025 10-K face; H1 from Q2 2026 / Q2 2025 10-Q faces.
ocf = {2021:-2622,2022:-5052,2023:-4866,2024:-1716,2025:-779}
sbc = {2021:570,2022:987,2023:821,2024:692,2025:741}
capex={2021:1794,2022:1369,2023:1026,2024:1141,2025:1710}
da  = {2021:197,2022:652,2023:937,2024:1031,2025:784}
defrev={2021:None,2022:None,2023:149,2024:1619,2025:503}   # "Deferred revenues" line, FY2025 10-K face (recast)
h1_25 = dict(ocf=-124,sbc=377,capex=800,da=396,defrev=403)
h1_26 = dict(ocf=-1190,sbc=433,capex=734,da=431,defrev=-362)
ttm = {k: {2025:v} for k,v in []}
T = dict(ocf=ocf[2025]-h1_25["ocf"]+h1_26["ocf"], sbc=sbc[2025]-h1_25["sbc"]+h1_26["sbc"], capex=capex[2025]-h1_25["capex"]+h1_26["capex"], da=da[2025]-h1_25["da"]+h1_26["da"], defrev=defrev[2025]-h1_25["defrev"]+h1_26["defrev"])
rows=[]
for y in range(2021,2026):
    ce=ocf[y]-sbc[y]-capex[y]; de=ocf[y]-sbc[y]-da[y]
    dr=defrev[y]
    rows.append((y,ce,de,dr))
    print(y, f"OCF {ocf[y]} SBC {sbc[y]} capex {capex[y]} D&A {da[y]} | OE capex end {ce} | OE D&A end {de} | deferred rev {dr} | capex/D&A {capex[y]/da[y]:.2f}" + (f" | capex end ex-deferred {ce-dr}" if dr is not None else ""))
print("TTM Jun-26", T, "OE capex end", T["ocf"]-T["sbc"]-T["capex"], "D&A end", T["ocf"]-T["sbc"]-T["da"], "ex-deferred capex end", T["ocf"]-T["sbc"]-T["capex"]-T["defrev"])
def mean(ys,i): return sum(r[i] for r in rows if r[0] in ys)/len(ys)
for nm,ys in [("5y FY2021-25",range(2021,2026)),("3y FY2023-25",range(2023,2026))]:
    print(nm, f"capex end {mean(ys,1):,.0f}  D&A end {mean(ys,2):,.0f}")
exd = [r[1]-r[3] for r in rows if r[3] is not None]
print("3y capex end ex-deferred revenue", sum(exd)/3, " 3y D&A end ex-deferred", sum(r[2]-r[3] for r in rows if r[3] is not None)/3)
print("5y capex end with FY2024-25 deferred revenue removed", (sum(r[1] for r in rows) - 1619 - 503)/5)
print("sum capex FY21-25", sum(capex.values()), "sum D&A", sum(da.values()), "ratio", sum(capex.values())/sum(da.values()))
print("contract liability 94% check", 1619/1716)
