# ALKT owner earnings from FILED cash-flow statements, newest vintage of each year ($k).
# OCF: 10-K FY2021 (2019-20), FY2023 (2021), FY2024 (2022), FY2025 (2023-25); TTM = FY2025 - H1-2025 + H1-2026 (10-Q Q2-2026).
Y = {
 # year: (OCF, SBC_cf, SBC_apic, DA_filed, DA_ppe, ppe_capex, cap_software, rev)
 2019: (-39085, 1250, 1250, 2226, 2226, 3689, 0, 73541),
 2020: (-38145, 1954, 1954, 2775, 2575, 2147, 0, 112142),
 2021: (-28959, 14535, 14535, 3443, 2343, 1120, 2577, 152159),
 2022: (-38045, 44592, 45395, 8075, 2975, 1057, 3388, 204270),
 2023: (-17502, 51231, 52686, 10631, 3831, 1058, 5234, 264831),
 2024: (18597, 59437, 60767, 10508, 3708, 1195, 6660, 333849),
 2025: (42906, 76188, 76679, 26912, 4612, 1542, 7147, 443639),
}
# DA_ppe = DA_filed - amortization of acquired intangibles (notes: 2019 0; 2020 0.2M; 2021 1.1M; 2022 5.1M; 2023 6.8M; 2024 6.8M; 2025 22.3M)
TTM = (42906-(-4507)+17220, 76188-35608+34802, 76679-36253+35086, 26912-11186+16415, 4600-2100+3200, 1542-882+772, 7147-3208+4065, 443639-209894+255982)
def oe(v, sbc="apic", c="capex"):
    ocf, scf, sap, da, dap, ppe, sw, rev = v
    s = sap if sbc=="apic" else scf
    cc = {"capex": ppe+sw, "da_ppe": dap, "da_filed": da}[c]
    return ocf - s - cc
print("year | OCF | SBC(apic) | OCF-SBC | c:D&A ex-acq | c:capex | OE D&A-ex-acq end | OE capex end | OE D&A-as-filed (screen) | SBC/OCF")
for y,v in list(Y.items())+[("TTM",TTM)]:
    ocf=v[0]; s=v[2]
    print(y, ocf, s, ocf-s, v[4], v[5]+v[6], oe(v,c="da_ppe"), oe(v), oe(v,sbc="cf",c="da_filed"), ("%.0f%%"%(100*v[1]/ocf) if ocf>0 else "n/m (OCF<0)"))
yrs=sorted(Y)
rows=[]
for n in range(3,8):
    for i in range(0,len(yrs)-n+1):
        w=yrs[i:i+n]
        a=sum(oe(Y[y],c="da_ppe") for y in w)/n; b=sum(oe(Y[y]) for y in w)/n
        a2=sum(oe(Y[y],sbc="cf",c="da_ppe") for y in w)/n; b2=sum(oe(Y[y],sbc="cf") for y in w)/n
        rows.append((f"{n}y FY{w[0]}-{str(w[-1])[2:]}", a, b, a2, b2))
print("\nwindow | D&A-ex-acq end (apic SBC) | capex end (apic SBC) | D&A-ex-acq (cf SBC) | capex (cf SBC)")
for r in rows: print(r[0], round(r[1]), round(r[2]), round(r[3]), round(r[4]))
allv=[x for r in rows for x in r[1:]]
print("annual-window range (all four constructions):", round(min(allv)), round(max(allv)))
print("TTM: D&A-ex-acq", oe(TTM,c="da_ppe"), "capex", oe(TTM), "| cf SBC:", oe(TTM,sbc="cf",c="da_ppe"), oe(TTM,sbc="cf"))
# screen reproduction (earliest vintage 2022 and max-rule SBC, D&A as filed / capex):
S = dict(Y); S[2022]=(-37788,45395,45395,8075,2975,1057,3645,204270); S[2025]=(42906,80098,80098,26912,4612,1542,7147,443639)
def m(w,c): return sum(S[y][0]-S[y][1]-({"da":S[y][3],"capex":S[y][5]+S[y][6]}[c]) for y in w)/len(w)
print("\nSCREEN REPRO: 5y D&A", round(m(range(2021,2026),"da")), "5y capex", round(m(range(2021,2026),"capex")), "3y D&A", round(m(range(2023,2026),"da")), "3y capex", round(m(range(2023,2026),"capex")))
# grant-date SBC [E3-70]: gross grants x grant-date FV ($k); net of forfeitures at their grant-date FV
G = {2021:(2915667*28.48+2811098*8.53, 44500*28.89), 2022:(5771008*14.06, 641136*24.27), 2023:(3676190*16.12, 639816*17.33), 2024:(2550824*26.69, 792674*17.20), 2025:(3790874*28.13, 650727*24.00)}
print("\nGRANT-DATE MEASURE [E3-70] ($k): year gross net charge(apic) OE capex end on net-grant measure")
for y,(g,f) in G.items():
    v=Y[y]; net=(g-f)/1000
    print(y, round(g/1000), round(net), v[2], round(v[0]-net-(v[5]+v[6])))
print("5y sums: gross", round(sum(g for g,f in G.values())/1000), "net", round(sum(g-f for g,f in G.values())/1000), "charge", sum(Y[y][2] for y in G))
# working capital flag
print("\nWC FLAG FY2025: AP&accrued +19708 / OCF 42906 = %.1f%%; OCF ex-line %d; OCF-SBC ex-line %d" % (100*19708/42906, 42906-19708, 42906-19708-76679))
print("TTM AP&accrued = 19708-4199+(-5793) =", 19708-4199-5793)
cum = {k: sum(Y[y][i] for y in range(2021,2026)) for k,i in (("OCF",0),("SBCcf",1),("SBCapic",2),("capex_ppe",5),("capsw",6))}
print("\nFY2021-25 cumulative:", cum, "revenue", sum(Y[y][7] for y in range(2021,2026)))
