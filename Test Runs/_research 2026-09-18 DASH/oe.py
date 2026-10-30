# Owner earnings from the filed cash-flow faces ($M). FY2021-22: FY2022 10-K; FY2023-25: FY2025 10-K; H1: Q2 2026 10-Q.
Y=["FY2021","FY2022","FY2023","FY2024","FY2025","TTM 2026-06"]
ocf=[692,367,1673,2132,2431]; sbc=[486,889,1088,1099,1051]
ppe=[129,176,123,104,257]; sw=[108,170,201,226,348]; capsbc=[93,132,161,165,193]
da=[156,369,509,561,747]; amort=[13,99,127,125,212]
wc=[435,148,530,252,-400]   # sum of working-capital lines excl. operating-lease payments
acq=[0,-71,0,0,4151+20]     # cash paid for acquisitions (FY2022 net cash acquired 71), plus deferred paid in financing
intinc=[None,None,152,199,211]
# TTM = FY2025 - H1 2025 + H1 2026
def ttm(a,h25,h26): return a-h25+h26
ocf.append(ttm(2431,1139,1538)); sbc.append(ttm(1051,517,580)); ppe.append(ttm(257,140,118)); sw.append(ttm(348,150,258))
capsbc.append(ttm(193,91,132)); da.append(ttm(747,311,564)); amort.append(ttm(212,63,228))
wc.append(ttm(-400,(128-90-47-142+25+10-43),(68-12+16-68-99+84-23))); acq.append(ttm(4171,1173,30+20))
c_cap=[p+s+c for p,s,c in zip(ppe,sw,capsbc)]; c_da=[d-a for d,a in zip(da,amort)]
oe_cap=[o-s-c for o,s,c in zip(ocf,sbc,c_cap)]; oe_da=[o-s-c for o,s,c in zip(ocf,sbc,c_da)]
print("year        OCF   SBC  c_cap c_da  OE_cap OE_da  WC   acq")
for i,y in enumerate(Y): print(f"{y:12}{ocf[i]:5}{sbc[i]:6}{c_cap[i]:6}{c_da[i]:5}{oe_cap[i]:7}{oe_da[i]:6}{wc[i]:6}{acq[i]:6}")
m=lambda L:sum(L)/len(L)
for nm,sl in [("5y FY2021-25",slice(0,5)),("3y FY2023-25",slice(2,5))]:
    a,b=m(oe_cap[sl]),m(oe_da[sl]); w=m(wc[sl]); q=m(acq[sl])
    print(nm,"capex end %.1f  D&A end %.1f | ex-WC %.1f / %.1f | with cash acquisitions %.1f / %.1f"%(a,b,a-w,b-w,a-q,b-q))
print("TTM capex end", oe_cap[5], "D&A end", oe_da[5], "ex-WC", oe_cap[5]-wc[5], oe_da[5]-wc[5])
cap=83600
for lab,v in [("5y cap",m(oe_cap[:5])),("3y cap",m(oe_cap[2:5])),("TTM cap",oe_cap[5]),("5y da",m(oe_da[:5])),("3y da",m(oe_da[2:5])),("TTM da",oe_da[5])]:
    print(lab, round(v,1), "yield %.2f%%"%(100*v/cap))
# grant-value SBC [E3-70]: FY2025 RSU grants 9,143K x $195.33 ; H1 2026 9,611K x $187.56
g25=9143*195.33/1000; g26=9611*187.56/1000; f25=2211*114.55/1000
print("FY2025 grant value %.0f, net of forfeits %.0f vs charge incl capitalised %d"%(g25,g25-f25,1051+193))
print("H1 2026 grant value %.0f vs H1 charge incl cap %d"%(g26,580+132))
print("SBC/OCF FY2025 %.1f%%, 5y %.1f%%"%(100*(1051+193)/2431, 100*sum(s+c for s,c in zip(sbc[:5],capsbc[:5]))/sum(ocf[:5])))
print("10%% floor needs %.0f"%(0.10*cap))
