"""SUGP arithmetic, by hand from the filed statements (HK$). Arithmetic only, no verdict."""
r = 0.04519   # HKSAR Government 20-year benchmark 20GB4503001 closing yield 2026-10-16 (hkgb.gov.hk)
tax = 0.165
yrs = ["FY21","FY22","FY23","FY24","FY25"]
ocf   = [18583165, 4453913, -13540058, 14098052, -15456974]
capex = [2890250, 2153000, 775120, 3018966, 1640534]
intang= [0, 145000, 0, 227000, 0]
svcfee= [0, 0, 0, 1369388, 5534772]   # shares issued to consultants, amortised (added back in OCF)
sbc   = [0, 0, 0, 0, 2940224]         # restricted shares to directors (added back in OCF)
intpaid=[195748, 43600, 38340, 19632, 148878]
intinc= [0, 0, 182047, 799631, 755232] # finance income per segment note (FY21-22 not separately disclosed: taken as 0)
ni_attr=[5799176, 7762677, 9697369, 10653488, -18484477]
dep   = [2775397, 2253593, 1943260, 1902005, 1707989]
amort = [56000, 82583, 85001, 103379, 74400]
gain_disp=[3932639, 0, 0, 0, 0]
oc = [ocf[i]-capex[i]-intang[i]-svcfee[i]-sbc[i] for i in range(5)]
oc_ae = [oc[i] + intpaid[i]*(1-tax) - intinc[i]*(1-tax) for i in range(5)]
pre_wc = [ni_attr[i]+dep[i]+amort[i]-capex[i]-intang[i]-gain_disp[i] for i in range(5)]
pre_wc_ae = [pre_wc[i] + intpaid[i]*(1-tax) - intinc[i]*(1-tax) for i in range(5)]
avg = lambda x: sum(x)/len(x)
for n,s in [("owner cash (equity)",oc),("owner cash (all-equity)",oc_ae),("before working capital (equity)",pre_wc),("before working capital (all-equity)",pre_wc_ae)]:
    print(f"{n:38s}", " ".join(f"{v/1e6:8.2f}" for v in s), f"| avg {avg(s)/1e6:7.3f}m")
print("first half avg FY21-22 owner cash:", avg(oc[:2])/1e6, " second half FY24-25:", avg(oc[3:])/1e6)
# Q7: series changes sign -> no-growth case alone (spec b). Ten years then zero nominal growth = perpetuity at r.
cash, notes, restricted = 28651212, 1484395, 10111578   # 2026-03-31 interim 6-K 0001753926-26-001875
netcash = cash - notes
print("net cash 2026-03-31 (restricted excluded):", netcash/1e6, " with restricted:", (netcash+restricted)/1e6)
def val(c, rate): return c/rate
for n,c in [("central all-equity",avg(oc_ae)),("beside: before WC all-equity",avg(pre_wc_ae))]:
    v = val(c,r); v10 = val(c,0.10)
    print(f"{n}: business at sovereign {v/1e6:8.2f}m; +net cash {(v+netcash)/1e6:8.2f}m | at 10% {v10/1e6:8.2f}m; +net cash {(v10+netcash)/1e6:8.2f}m")
# share count after 2026-10-07 consolidation
clsA = 1501789; clsB = 901680//5//6
shares = clsA + clsB
price = 1.76; fx = 7.78
print("shares post 2026-10-07:", clsA, "+ B", clsB, "=", shares, " mkt cap US$m", shares*price/1e6)
# cash raised after 2026-03-31, as stated or inferred from the 6-Ks
offer_net_usd = 3.6e6          # prospectus estimate of net proceeds, 424B3 2026-05-12
ex087 = (7124092-3563092)*0.87 # inferred: shares issued 2026-06-12..08-04 at US$0.87 (pre-consolidation basis)
ex070 = (9010733-1424819)*0.70 # inferred: shares issued 2026-08-06..10-02 at US$0.70
km = 5616000
print("inferred warrant cash US$m:", ex087/1e6, ex070/1e6)
nc_b = netcash + (offer_net_usd+ex087+ex070)*fx - km
print("beside net cash incl. stated/inferred raises less KM, HK$m:", nc_b/1e6)
for n,c in [("central",avg(oc_ae)),("before WC",avg(pre_wc_ae))]:
    for rate in (r,0.10):
        eq = val(c,rate)+nc_b
        print(f"  {n} @ {rate:.4f}: equity HK${eq/1e6:8.2f}m = US${eq/fx/shares:6.2f}/share")
for rate in (r,0.10):
    eq = val(avg(oc_ae),rate)+netcash
    print(f"  central on filed balance sheet only @ {rate:.4f}: HK${eq/1e6:.2f}m")
# returns
eq_end = [40322466, 40085143, 56424541, 97721696, 86150722]
print("SUGP attributable NI sum", sum(ni_attr)/1e6, "avg equity", avg(eq_end)/1e6, "-> ", sum(ni_attr)/sum(eq_end))
eci_p = [8716, 6344, 5624, 8948, 2638]; eci_e=[64497,70719,75579,84694,87434]
print("ECI profit sum", sum(eci_p), "avg eq", avg(eci_e), "->", sum(eci_p)/sum(eci_e))
rev=[117565797,136447442,163690966,182164539,192386583]; gp=[35969957,39227115,48042953,47596440,30743562]
print("SUGP GM", [round(g/v*100,1) for g,v in zip(gp,rev)])
eci_rev=[138207,130433,174012,200265,195049]; eci_gp=[30947,31933,40595,49811,49968]
print("ECI GM", [round(g/v*100,1) for g,v in zip(eci_gp,eci_rev)])
print("warrants remaining (est.) post 2026-10-07:", (42717046-(9010733-1424819))/6, "at US$", 0.70*6)
