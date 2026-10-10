# COMPUTATION for KLAC: owner cash, range, fair price. USD millions. Inputs transcribed from XBRL companyfacts
# of the 10-Ks (accessions in the run file), cross-checked against the FY2026 10-K statement lines.
yrs=[2022,2023,2024,2025,2026]
ocf=[3313,3670,3309,4082,4143]
sbc=[127,171,213,265,310]
capex=[307,342,277,335,376]
acq=[479,27,4,0,0]
intexp=[160,297,311,302,284]
pti=[3489,3789,3190,4644,5606]
tax=[167,402,428,583,775]
dep_amort=[363,415,402,394,394]
r=0.0564; floor=0.10; shares=1306.546783
debt=5887; cash=1650; mkt=3253; div_after=0.23*shares
netdebt=debt-cash-mkt+div_after
def pv(c0,g,rate,n=10):
    v=0;c=c0
    for t in range(1,n+1):
        c*=1+g; v+=c/(1+rate)**t
    return v + c/rate/(1+rate)**n   # zero nominal growth after year 10
def series(add_int):
    out=[]
    for i in range(5):
        t=tax[i]/pti[i]
        oc=ocf[i]-sbc[i]-capex[i]-acq[i]
        if add_int: oc+=intexp[i]*(1-t)
        out.append(oc)
    return out
for label,add in (('ALL-EQUITY (before interest)',True),('EQUITY-ONLY (after interest)',False)):
    s=series(add); base=sum(s)/5; g=(s[-1]/s[0])**(1/4)-1
    lo=pv(base,0,r); hi=pv(base,g,r)
    if add: lo_ps=(lo-netdebt)/shares; hi_ps=(hi-netdebt)/shares
    else: lo_ps=lo/shares; hi_ps=hi/shares
    mid=(lo+hi)/2
    # growth giving midpoint at sovereign
    a,b=0,g
    for _ in range(200):
        m=(a+b)/2
        if pv(base,m,r)<mid: a=m
        else: b=m
    gm=(a+b)/2; fair=pv(base,gm,floor)
    fair_ps=(fair-netdebt)/shares if add else fair/shares
    print(label); print('  series',[round(x) for x in s],'base',round(base,1),'growth %.2f%%'%(g*100))
    print('  whole range $%.0fM-$%.0fM; per share $%.2f-$%.2f (ratio %.2f)'%(lo,hi,lo_ps,hi_ps,hi/lo))
    print('  midpoint growth %.2f%%; fair (midpoint stream at 10%%) $%.0fM -> $%.2f/share'%(gm*100,fair,fair_ps))
    # yield at price
print('net debt incl. post-year-end dividend', round(netdebt,1))
# depreciation variant (D&A replaces capex), and organic (acq left out) shown for reference
s=[ocf[i]-sbc[i]-dep_amort[i] for i in range(5)]; print('D&A variant series',s, 'avg',sum(s)/5)
s=[ocf[i]-sbc[i]-capex[i] for i in range(5)]; print('acq left out series',s,'avg',sum(s)/5,'growth %.2f%%'%(((s[-1]/s[0])**.25-1)*100))
price=195.36; mcap=price*shares
print('mcap',round(mcap),'EV',round(mcap+netdebt))
