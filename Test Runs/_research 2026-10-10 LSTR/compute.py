"""LSTR run 2026-10-10: owner cash and the Q7 COMPUTATION (NOT A CLEARANCE). USD millions.
Inputs transcribed from the 10-K cash-flow statements (XBRL first-filed vintage, cross-checked in text where noted).
OC  = OCF - SBC - capex - finance-lease principal (trailers acquired by finance lease are capital spending).
OCae = OC + (operating income - pretax income) * (1 - tax rate): owner cash before net interest (all-equity basis)."""
D = {  # year: OCF, SBC, capex, FLprincipal, OI, pretax, taxrate
2014:(101.9,6.8,10.5,37.4,224.4,221.2,.37),
2015:(216.0,6.9,4.8,36.5,241.7,238.8,.38),
2016:(190.2,2.7,22.6,47.5,223.3,219.5,.37),
2017:(139.0,7.7,15.6,46.8,244.0,240.8,.37),
2018:(297.9,18.3,9.7,43.3,331.7,328.4,.24),
2019:(307.8,4.2,19.4,44.6,298.9,295.8,.24),
2020:(210.7,4.6,30.6,43.7,252.9,249.0,.24),
2021:(276.7,27.5,23.3,37.6,505.7,501.7,.24),
2022:(622.7,12.4,26.0,39.1,571.1,567.5,.24),
2023:(393.6,4.3,25.7,36.4,344.1,348.1,.24),
2024:(286.6,3.4,31.0,31.0,248.9,254.3,.23),
2025:(224.9,6.0,9.9,33.2,151.6,150.6,.236)}
OC={y:v[0]-v[1]-v[2]-v[3] for y,v in D.items()}
AE={y:OC[y]+(v[4]-v[5])*(1-v[6]) for y,v in D.items()}
print("year   OC(equity-only)  OC(all-equity)")
for y in D: print(y, f"{OC[y]:8.1f} {AE[y]:8.1f}")
avg=lambda S,a,b: sum(S[y] for y in range(a,b+1))/(b-a+1)
r=0.056; fl=0.10; sh=33.936925
# net cash at 2026-06-27 (10-Q 0001193125-26-322966): cash 294.350 + STI 53.352 + LTI 95.748 - overdraft 71.849 - debt (finance leases) 24.686 - 42.088
netcash=294.350+53.352+95.748-71.849-24.686-42.088
def val(C,g,rate,n=10):
    s=sum(C*(1+g)**t/(1+rate)**t for t in range(1,n+1))
    return s + C*(1+g)**n/rate/(1+rate)**n
def growth(a,b,yrs): return (b/a)**(1/yrs)-1
out=[]
for label,S,addcash in [("ALL-EQUITY (central)",AE,True),("EQUITY-ONLY (beside)",OC,False)]:
    lit=avg(S,2021,2025); glit=growth(S[2021],S[2025],4)
    base=avg(S,2020,2024); prev=avg(S,2016,2019); g=growth(prev,base,4.5)
    nc = netcash if addcash else 0.0
    lo=val(base,0,r); hi=val(base,g,r)
    fair=(val(base,0,fl)+val(base,g,fl))/2
    print(f"\n{label}: literal window 2021-25 avg {lit:.1f}, growth 2021->2025 {glit*100:.1f}%/yr")
    print(f"  cycle base (trough 2020 to trough 2025: 2020-24 avg) {base:.1f}; prior cycle 2016-19 avg {prev:.1f}; growth between cycle averages {g*100:.1f}%/yr")
    print(f"  net cash added {nc:.1f}")
    print(f"  range whole business {lo:,.0f} to {hi:,.0f}; width {hi/lo:.2f}x")
    print(f"  per share ${(lo+nc)/sh:.2f} to ${(hi+nc)/sh:.2f}; midpoint ${((lo+hi)/2+nc)/sh:.2f}")
    print(f"  fair price (midpoint of the two cases valued at the 10% floor) ${(fair+nc)/sh:.2f}")
    # literal window shown beside: negative growth -> bottom, no growth top
    lo2=val(lit,glit,r); hi2=val(lit,0,r)
    print(f"  literal window beside: ${(lo2+nc)/sh:.2f} (growth {glit*100:.1f}%) to ${(hi2+nc)/sh:.2f} (no growth)")
    # operating-income check on growth between cycles
oi={y:D[y][4] for y in D}
print("\nOI cycle check: 2016-19 avg %.1f, 2020-24 avg %.1f, growth %.1f%%/yr" % (avg(oi,2016,2019),avg(oi,2020,2024),growth(avg(oi,2016,2019),avg(oi,2020,2024),4.5)*100))
print("price 169.11 x shares 33.936925 = market cap %.1f; EV = %.1f" % (169.11*sh, 169.11*sh-netcash))
print("owner-cash yield on EV at cycle base: %.2f%%" % (avg(AE,2020,2024)/(169.11*sh-netcash)*100))
