# COMPUTATION, NOT A CLEARANCE. KION GROUP AG, EUR million; per share on 131.124771m shares outstanding (30 Jun 2026).
SH=131.124771; PRICE=33.85; ND=1244.1; ND_LEASEBOND=1244.1-494.7; ND_ALL_FIN=1244.1+4540.1+774.7
RF=0.0378
def pv(c0,g,r,yrs=10):
    v=0;c=c0
    for t in range(1,yrs+1):
        c*=1+g; v+=c/(1+r)**t
    return v + c/r/(1+r)**yrs   # zero nominal growth after year ten
def irr(price,c0,g):
    lo,hi=0.0005,1.0
    for _ in range(200):
        m=(lo+hi)/2
        if pv(c0,g,m)>price: lo=m
        else: hi=m
    return m
cases={
 'bottom: 8y cycle base 242.9, decline -12.9%/yr (halves 2018-21 vs 2022-25)':(242.9,-0.129),
 'literal window 2021-25, all spending, no growth (series changes sign)':(221.5,0.0),
 'top: window, maintenance-only (capex replaced by depreciation, +158.9), no growth':(380.4,0.0),
}
EV=PRICE*SH+ND
print('market cap %.1f  EV(all-equity) %.1f' % (PRICE*SH, EV))
vals={}
for k,(c,g) in cases.items():
    v=pv(c,g,RF); v10=pv(c,g,0.10)
    vals[k]=(v,v10)
    print('%-85s value@3.78%% %8.1f -> EUR/sh %6.2f | @10%% %7.1f -> EUR/sh %6.2f | return at price %5.2f%%' % (k,v,(v-ND)/SH,v10,(v10-ND)/SH,100*irr(EV,c,g)))
ends=[list(cases)[0],list(cases)[2]]
lo=(vals[ends[0]][0]-ND)/SH; hi=(vals[ends[1]][0]-ND)/SH
print('RANGE EUR/sh %.2f to %.2f (width %.1fx on whole-business value %.0f to %.0f)' % (lo,hi,vals[ends[1]][0]/vals[ends[0]][0],vals[ends[0]][0],vals[ends[1]][0]))
fair=((vals[ends[0]][1]+vals[ends[1]][1])/2-ND)/SH
print('FAIR PRICE all-equity EUR/sh %.2f ; ADR (1/4 share) EUR %.2f' % (fair,fair/4))
for lab,nd in [('net debt less bond funds used for leases 749.4',ND_LEASEBOND),('lease+rental liabilities in net debt 6558.9',ND_ALL_FIN)]:
    print('  beside, %s: fair %.2f ; range %.2f to %.2f' % (lab,((vals[ends[0]][1]+vals[ends[1]][1])/2-nd)/SH,(vals[ends[0]][0]-nd)/SH,(vals[ends[1]][0]-nd)/SH))
# signed, unclosed robotics stake (low-triple-digit millions): take 100 and 300 as the stated band edges
for x in (100,300):
    print('  beside, robotics stake %d added to net debt, credited nothing: fair %.2f' % (x,((vals[ends[0]][1]+vals[ends[1]][1])/2-ND-x)/SH))
# equity-only: owner cash after interest, 5y 175.9 ; 8y 197.7; maintenance +158.9
eq_b=pv(197.7,-0.129,0.10); eq_t=pv(175.9+158.9,0.0,0.10)
print('FAIR PRICE equity-only EUR/sh %.2f (ends %.1f, %.1f at 10%%) ; equity-only yield at price lit. window %.2f%%' % ((eq_b+eq_t)/2/SH,eq_b,eq_t,100*175.9/(PRICE*SH)))
print('beside: ex-NWC window (avg NWC change -95.6 added back) + maintenance, no growth: return at price %.2f%%' % (100*irr(EV,221.5+95.6+158.9,0.0)))
print('beside: top case carried at the 8y revenue CAGR 5.06%% (double-credits growth spending): return %.2f%%' % (100*irr(EV,380.4,0.0506)))
