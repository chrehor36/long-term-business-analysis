# Q7 COMPUTATION, NOT A CLEARANCE. Billions of yen. Ten years at growth g, then zero nominal growth, discount r.
def val(c0,g,r):
    pv=0; c=c0
    for t in range(1,11):
        c=c*(1+g); pv+=c/(1+r)**t
    return pv + (c/r)/(1+r)**10
SH=1734.777285; PRICE=4250; MCAP=SH*PRICE/1000
r=0.04085
borrow_jun=133.699-130.642  # borrowings+leases at Jun 30 less leases at Mar 31 (Jun lease split not disclosed)
cash_jun=597.934; sec_jun=165.094
nd_jun=borrow_jun-cash_jun-sec_jun
nd_mar=(1.760+0.103+0.589)-450.366-157.580
print("mcap",round(MCAP,1),"net debt Jun",round(nd_jun,1),"Mar",round(nd_mar,1),"EV at price (Jun)",round(MCAP+nd_jun,1))
cases={"no-growth, 5-yr avg all-equity 50.2":(50.2,0.0),
       "beside: 5-yr avg at Service Solutions sales growth 5.4%":(50.2,0.054),
       "beside: latest-3-yr avg 95.1, no growth":(95.1,0.0),
       "beside: latest year 148.5, no growth":(148.5,0.0),
       "beside: latest year 148.5 at 5.4%":(148.5,0.054)}
for k,(c,g) in cases.items():
    v=val(c,g,r); v10=val(c,g,0.10)
    print(f"{k:58s} EV {v:8.1f} per share {(v-nd_jun)/SH*1000:7.0f}   at 10%: EV {v10:7.1f} per share {(v10-nd_jun)/SH*1000:6.0f}")
# equity-only (owner cash after interest, no net cash added)
for c in (59.2,):
    print("equity-only no-growth at 10%: per share", round(val(c,0,0.10)/SH*1000), " at sovereign:", round(val(c,0,r)/SH*1000))
# implied: owner cash needed at 10% no growth to justify EV at price
ev=MCAP+nd_jun
print("owner cash needed for 10% at price (no growth)",round(ev*0.10,1)," latest-year yield on EV",round(148.5/ev*100,2),"%  5yr avg yield",round(50.2/ev*100,2),"%")
# growth needed (perpetual) for latest year to give 10%: (c*(1+g))/(ev) + g = 0.10
g=(0.10*ev-148.5)/(ev+148.5); print("perpetual growth needed on latest year:",round(g*100,2),"%")
