# COMPUTATION, NOT A CLEARANCE. FET owner cash and the Q7 construction, arithmetic only (USD millions).
# Inputs: FET XBRL as first filed (companyfacts), cross-checked for 2025 against 10-K 0001401257-26-000015.
Y=list(range(2010,2026))
OCF={2010:66.0,2011:39.3,2012:137.9,2013:211.4,2014:270.0,2015:155.9,2016:64.7,2017:-40.0,2018:2.4,2019:104.1,2020:3.9,2021:-15.8,2022:-17.1,2023:8.2,2024:92.2,2025:70.4}
SBC={2010:5.1,2011:5.2,2012:8.2,2013:19.0,2014:18.8,2015:21.7,2016:20.5,2017:20.3,2018:19.9,2019:15.8,2020:9.8,2021:7.6,2022:4.2,2023:4.6,2024:7.1,2025:9.0}
CAPEX={2010:19.6,2011:41.2,2012:49.7,2013:60.3,2014:53.8,2015:32.3,2016:16.8,2017:26.7,2018:24.0,2019:15.1,2020:2.2,2021:2.4,2022:7.5,2023:7.9,2024:8.1,2025:6.0}
FLP={2010:0.6,2011:0.3,2012:0.5,2013:0.9,2014:1.2,2015:0.7,2016:0.1,2017:1.2,2018:1.1,2019:1.2,2020:1.2,2021:1.5,2022:1.2,2023:1.2,2024:1.7,2025:2.0}
ACQ={2010:0.0,2011:509.9,2012:139.9,2013:181.7,2014:38.3,2015:60.8,2016:4.1,2017:162.2,2018:60.6,2019:0.0,2020:-105.2,2021:3.4+1.3,2022:0.5,2023:0.0,2024:150.4,2025:0.0}  # net of businesses sold (2020 ABZ/Quadrant sale; 2021 settlement paid)
INT={2010:14.2,2011:17.7,2012:15.2,2013:18.0,2014:27.6,2015:27.9,2016:26.3,2017:26.0,2018:30.3,2019:31.9,2020:23.8,2021:27.1,2022:25.3,2023:17.1,2024:26.8,2025:16.9}  # interest paid
REV={2010:747.3,2011:1128.1,2012:1414.9,2013:1524.8,2014:1739.7,2015:1073.7,2016:587.6,2017:818.6,2018:1064.2,2019:956.5,2020:512.5,2021:541.1,2022:699.9,2023:738.9,2024:816.4,2025:791.5}
eq={y:OCF[y]-SBC[y]-CAPEX[y]-FLP[y] for y in Y}           # owner cash after every real cost, before purchases, after interest (equity basis)
ae={y:eq[y]+INT[y] for y in Y}                             # before interest (all-equity basis); no tax shield credited (CONVENTION of this run)
print("year   rev   OCF   SBC capex  FLP  ownercash(eq) +int=allequity  net purchases  eq after purch  allequity/rev%")
for y in Y: print(f"{y} {REV[y]:6.1f} {OCF[y]:6.1f} {SBC[y]:5.1f} {CAPEX[y]:5.1f} {FLP[y]:4.1f} {eq[y]:8.1f} {ae[y]:10.1f} {ACQ[y]:10.1f} {eq[y]-ACQ[y]:10.1f} {ae[y]/REV[y]*100:7.1f}")
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
W=range(2021,2026); C=range(2016,2021); P=range(2011,2016)
for name,ys in [('window 2021-25',W),('cycle 2016-20',C),('prior 2011-15',P)]:
    print(f"{name}: eq {avg(eq,ys):6.1f}  all-eq {avg(ae,ys):6.1f}  net purch/yr {avg(ACQ,ys):6.1f}  eq after purch {avg(eq,ys)-avg(ACQ,ys):6.1f}  all-eq after purch {avg(ae,ys)-avg(ACQ,ys):6.1f}  rev {avg(REV,ys):6.1f}  owner cash before purch sum {sum(eq[y] for y in ys):6.1f} purch sum {sum(ACQ[y] for y in ys):6.1f}")
r=0.0543; floor=0.10
ND=143.708-33.716   # net debt 2026-06-30 (10-Q 0001401257-26-000053): current + long-term debt less cash
SH=11.246295        # cover 10-Q
PRICE=77.11
print(f"net debt {ND:.1f}  shares {SH}  cap {PRICE*SH:.1f}  EV {PRICE*SH+ND:.1f}")
def pv(c0,g,rate,yrs=10):
    v=0; c=c0
    for t in range(1,yrs+1):
        c*= (1+g); v+= c/(1+rate)**t
    v+= c/rate/(1+rate)**yrs     # zero nominal growth after year ten
    return v
cases={}
# central: cycle base 2016-20 (spec a: 2021 aberrational on the filer's description), organic pair (serial-acquirer test met)
g_shown=(avg(ae,W)/avg(ae,C))**(1/5)-1
g_sales=(avg(REV,W)/avg(REV,C))**(1/5)-1
print(f"shown growth all-eq cycle->window {g_shown*100:.2f}%/yr ; sales growth same periods {g_sales*100:.2f}%/yr")
c10=avg(ae,C)*(1+g_shown)**10; print(f"cap test: all-eq owner cash yr10 at shown growth {c10:.1f} = {c10/avg(REV,W)*100:.1f}% of window sales; highest share earned (filings read) {max(ae[y]/REV[y] for y in Y)*100:.1f}%")
for lab,base,g in [('central bottom: cycle base, growth cut to sales growth',avg(ae,C),g_sales),('central top: cycle base, no growth',avg(ae,C),0.0),('literal window beside, no growth (halves change sign)',avg(ae,W),0.0)]:
    v=pv(base,g,r); v10=pv(base,g,floor)
    print(f"{lab}: all-eq value {v:6.1f} less ND -> {(v-ND)/SH:6.2f}/sh ; at 10%: {(v10-ND)/SH:6.2f}/sh")
for lab,base,g in [('equity-only cycle base, cut',avg(eq,C),g_sales),('equity-only cycle base, no growth',avg(eq,C),0.0),('equity-only window, no growth',avg(eq,W),0.0)]:
    v=pv(base,g,r); v10=pv(base,g,floor)
    print(f"{lab}: value {v:6.1f} -> {v/SH:6.2f}/sh ; at 10%: {v10/SH:6.2f}/sh")
# default pair beside (purchases deducted, total growth): window
print(f"default pair window all-eq after purchases {avg(ae,W)-avg(ACQ,W):.1f}; equity after purchases {avg(eq,W)-avg(ACQ,W):.1f}")
# what the price implies
print(f"all-eq owner cash yield at price: cycle {avg(ae,C)/(PRICE*SH+ND)*100:.2f}%  window {avg(ae,W)/(PRICE*SH+ND)*100:.2f}%  best year 2024 {ae[2024]/(PRICE*SH+ND)*100:.2f}%")
print(f"equity owner cash yield at price: window {avg(eq,W)/(PRICE*SH)*100:.2f}%")
print("--- growth case (shown growth cycle 2016-20 -> window 2021-25, not cut by the cap) ---")
for lab,base,g in [('central top: cycle base at shown growth',avg(ae,C),g_shown)]:
    v=pv(base,g,r); v10=pv(base,g,floor)
    print(f"{lab}: all-eq value {v:6.1f} less ND -> {(v-ND)/SH:6.2f}/sh ; at 10%: {(v10-ND)/SH:6.2f}/sh")
lo=(pv(avg(ae,C),0,r)-ND)/SH; hi=(pv(avg(ae,C),g_shown,r)-ND)/SH
f_lo=(pv(avg(ae,C),0,floor)-ND)/SH; f_hi=(pv(avg(ae,C),g_shown,floor)-ND)/SH
print(f"CENTRAL RANGE all-equity: {lo:.2f} to {hi:.2f} /sh (width {hi/lo:.2f}:1) vs price {PRICE}; FAIR (avg of ends at 10%): {(f_lo+f_hi)/2:.2f}")
elo=pv(avg(eq,C),0,floor)/SH; print(f"equity-only: cycle base negative ({avg(eq,C):.1f}); growth not measurable on a sign change; window no-growth at 10% {pv(avg(eq,W),0,floor)/SH:.2f}; equity-only fair on cycle base {elo:.2f} (negative)")
# return at price on the top case: solve rate where all-eq value - ND = price*SH
import math
def irr(base,g):
    lo_,hi_=0.0001,0.5
    for _ in range(100):
        m=(lo_+hi_)/2
        if pv(base,g,m)-ND>PRICE*SH: lo_=m
        else: hi_=m
    return m
print(f"expected return at price: top case {irr(avg(ae,C),g_shown)*100:.2f}%  bottom case {irr(avg(ae,C),0)*100:.2f}%  window literal {irr(avg(ae,W),0)*100:.2f}%")
