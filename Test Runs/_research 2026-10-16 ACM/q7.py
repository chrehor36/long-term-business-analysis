# COMPUTATION, NOT A CLEARANCE: AECOM range and fair price (USD millions)
yrs = ["FY21","FY22","FY23","FY24","FY25"]
ocf  = [704.7, 713.6, 696.0, 827.5, 821.6]
sbc  = [44.7, 38.5, 45.9, 61.5, 61.4]
capx = [136.3, 137.0, 105.6, 119.6, 136.7]
flp  = [13.7, 19.8, 23.7, 28.9, 32.4]
nci  = [10.3, 12.4, 2.2, 16.2, 53.4]
ipaid= [255.7, 104.6, 154.0, 177.4, 166.9]
iinc = [6.7, 8.2, 40.3, 58.6, 62.9]
acq  = [0.0, 0.0, 0.0, 18.7, 212.5]
divp = [265.9, 42.3, 0.0, 0.0, 0.0]   # payments on businesses sold (discontinued exits), shown beside
da   = [176.4, 170.9, 175.7, 178.8, 175.9]
T = 0.21
eq = [o-s-c-f-n for o,s,c,f,n in zip(ocf,sbc,capx,flp,nci)]
ae = [e+(p-i)*(1-T) for e,p,i in zip(eq,ipaid,iinc)]
eqD = [o-s-d-f-n for o,s,d,f,n in zip(ocf,sbc,da,flp,nci)]
aeD = [e+(p-i)*(1-T) for e,p,i in zip(eqD,ipaid,iinc)]
avg = lambda x: sum(x)/len(x)
for nm, s in [("equity-only OE (capex)",eq),("all-equity OE (capex)",ae),("equity-only OE (D&A)",eqD),("all-equity OE (D&A)",aeD)]:
    print(f"{nm:26s}", " ".join(f"{v:7.1f}" for v in s), f" avg {avg(s):7.1f}")
g_ae = (ae[-1]/ae[0])**0.25-1; g_eq = (eq[-1]/eq[0])**0.25-1
h_ae = (avg(ae[3:])/avg(ae[:2]))**(1/3)-1
print(f"growth end-to-end: all-equity {g_ae*100:.2f}%  equity-only {g_eq*100:.2f}%  all-equity halves (FY21-22 vs FY24-25, 3 yrs apart) {h_ae*100:.2f}%")
A = avg(acq); Dv = avg(divp)
print(f"avg acquisitions {A:.1f}; avg payments on businesses sold {Dv:.1f}")
def pv(c0, g, r, n=10):
    v=0; c=c0
    for t in range(1,n+1):
        c*= (1+g); v+= c/(1+r)**t
    return v + c/r/(1+r)**n
r = 0.0543; sh = 128.696
debt = 2745.2; cash = 1012.932; nd = debt-cash   # Note 7 total debt principal (credit agreement, 2033 notes, other debt incl. finance leases), Q3 10-Q
price=58.94; mcap=price*sh
print(f"net debt {nd:.1f} (debt {debt:.1f} cash {cash:.1f}); mcap {mcap:.1f}; EV {mcap+nd:.1f}")
def case(base, g, label, basis):
    v = pv(base, g, r); f = pv(base, g, 0.10)
    if basis=="ae": ps, fp = (v-nd)/sh, (f-nd)/sh
    else: ps, fp = v/sh, f/sh
    print(f"  {label:44s} base {base:6.1f} g {g*100:5.2f}%  value/sh ${ps:7.2f}  at10% ${fp:7.2f}")
    return ps, fp
print("CENTRAL, all-equity, acquisitions deducted, total growth credited:")
b = avg(ae)-A
top = case(b, 0.0, "top: no growth", "ae"); bot = case(b, g_ae, "bottom: shown decline", "ae")
print(f"  range ${bot[0]:.2f} to ${top[0]:.2f}; fair (avg of ends at 10%) ${(top[1]+bot[1])/2:.2f}")
print(f"  yield on EV at price, base {b:.1f}: {100*b/(mcap+nd):.2f}%")
print("BESIDE: payments on businesses sold also deducted:")
b2 = avg(ae)-A-Dv; case(b2,0.0,"no growth","ae"); case(b2,g_ae,"decline","ae")
print("BESIDE: halves growth instead of end years:")
case(b, h_ae, "halves growth", "ae")
print("BESIDE: organic pair (acquisitions left out), all-equity:")
case(avg(ae),0.0,"no growth","ae"); case(avg(ae), g_ae, "shown decline","ae")
print("BESIDE: depreciation variant all-equity:")
case(avg(aeD)-A,0.0,"no growth (D&A)","ae"); case(avg(aeD)-A,(aeD[-1]/aeD[0])**0.25-1,"decline (D&A)","ae")
print("EQUITY-ONLY (beside, never decides):")
be = avg(eq)-A
t2=case(be,0.0,"no growth","eq"); b3=case(be,g_eq,"shown growth","eq")
print(f"  range ${t2[0]:.2f} to ${b3[0]:.2f}; fair ${(t2[1]+b3[1])/2:.2f}; yield on mcap {100*be/mcap:.2f}%")
# TTM to Q3 FY26
ttm_ocf = 821.602-625.472+169.234; ttm_sbc=61.439-46.063+26.486; ttm_cx=136.675-74.639+99.879; ttm_nci=53.380-33.313+30.655
ttm_eq = ttm_ocf-ttm_sbc-ttm_cx-32.4-ttm_nci; ttm_ae = ttm_eq+(166.9-62.9)*(1-T)
print(f"TTM to 2026-07-03: OCF {ttm_ocf:.1f} SBC {ttm_sbc:.1f} capex {ttm_cx:.1f} NCI {ttm_nci:.1f} -> equity-only OE {ttm_eq:.1f}, all-equity ~{ttm_ae:.1f}")
print("what the floor needs: all-equity owner cash at 10% no growth on EV:", round(0.10*(mcap+nd),1))
