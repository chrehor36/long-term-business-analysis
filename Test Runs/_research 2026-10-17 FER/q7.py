# Q7 arithmetic for FER run 2026-10-17. EUR millions. Sources in notes.md / run file.
yrs=[2021,2022,2023,2024,2025]
ocf  =[810,1002,1263,1293,1926]   # consolidated cash flows from operating activities (before interest; incl dividends from equity-accounted)
capex=[124,95,86,226,187]         # PP&E / intangible
infra=[239,809,319,186,466]       # investments in infrastructure projects
grant=[0,25,9,0,0]
lease=[131,72,87,104,121]
mindv=[270,161,377,444,367]       # dividends paid to non-controlling interests of investees
intpd=[295,329,432,464,455]; intrc=[3,47,236,172,144]
rev  =[6910,7551,8515,9148,9627]
acq  =[923,347,257,1286,1636]; divs=[1621,429,43,2582,1158]
MAINT_INFRA=50   # CONVENTION of the run: project maintenance capex guess
sov=0.0367; floor=0.10
shares=721.132155  # millions, 6/30/2026
netdebt=6283       # consolidated net debt 6/30/2026 (H1 2026 report)
px_usd=49.41; fx=1.1244; px=px_usd/fx
mcap=px*shares
def avg(x): return sum(x)/len(x)
allsp=[o-c-i+g-l for o,c,i,g,l in zip(ocf,capex,infra,grant,lease)]
maint=[o-c-l-MAINT_INFRA for o,c,l in zip(ocf,capex,lease)]
allsp_m=[a-m for a,m in zip(allsp,mindv)]
maint_m=[a-m for a,m in zip(maint,mindv)]
netint=[p-r for p,r in zip(intpd,intrc)]
eq_maint=[a-n for a,n in zip(maint_m,netint)]
eq_all=[a-n for a,n in zip(allsp_m,netint)]
print('price EUR',round(px,2),'mcap',round(mcap),'EV',round(mcap+netdebt))
for n,s in [('all-spending 100%',allsp),('maint 100%',maint),('all-spending attrib',allsp_m),('maint attrib',maint_m),('equity-only maint',eq_maint),('equity-only all',eq_all)]:
    print(f'{n:22s}',s,'avg',round(avg(s),1))
def halves(s):
    a=(s[0]+s[1])/2; b=(s[3]+s[4])/2
    return (b/a)**(1/3)-1 if a>0 and b>0 else None
g_rev=(rev[-1]/rev[0])**(1/4)-1
print('revenue CAGR 21-25',round(g_rev*100,2))
for n,s in [('maint attrib',maint_m),('equity-only maint',eq_maint),('all attrib',allsp_m)]:
    h=halves(s); print(n,'halves growth',None if h is None else round(h*100,2))
    if h: 
        y10=avg(s)*(1+h)**10; print('  carried 10y',round(y10),'share of sales at 2035 at rev growth', round(y10/(rev[-1]*(1+g_rev)**10)*100,1),'max share shown',round(max(x/r for x,r in zip(s,rev))*100,1))
def value(base,g,r):
    v=sum(base*(1+g)**t/(1+r)**t for t in range(1,11))
    v+= base*(1+g)**10/r/(1+r)**10
    return v
def irr(base,g,target):
    lo,hi=0.001,0.5
    for _ in range(100):
        m=(lo+hi)/2
        if value(base,g,m)>target: lo=m
        else: hi=m
    return m
print('net purchases over window',sum(acq)-sum(divs))
for label,base,debt,g in [('CENTRAL all-equity maint attrib',avg(maint_m),netdebt,g_rev),('beside all-spending attrib',avg(allsp_m),netdebt,g_rev),('beside equity-only maint',avg(eq_maint),0,g_rev),('beside 100% maint (NCI not deducted)',avg(maint),netdebt,g_rev)]:
    lo=(value(base,0,sov)-debt)/shares; hi=(value(base,g,sov)-debt)/shares
    f0=(value(base,0,floor)-debt)/shares; f1=(value(base,g,floor)-debt)/shares
    tgt=mcap+debt
    print(f'{label}: base {base:.0f} g {g*100:.2f}% range EUR {lo:.2f}-{hi:.2f} (USD {lo*fx:.2f}-{hi*fx:.2f}); fair EUR {(f0+f1)/2:.2f} USD {(f0+f1)/2*fx:.2f}; ends at 10%: {f0:.2f},{f1:.2f}; IRR at price no-growth {irr(base,0,tgt)*100:.2f}% growth {irr(base,g,tgt)*100:.2f}%')
# literal window: compound 2021->2025 of maint attrib
s=maint_m; print('literal CAGR maint attrib 21-25',round(((s[-1]/s[0])**(1/4)-1)*100,1))
# what growth would earn the floor on central base?
b=avg(maint_m); lo,hi=0,1
for _ in range(100):
    m=(lo+hi)/2
    if value(b,m,floor)<mcap+netdebt: lo=m
    else: hi=m
print('growth needed for 10% on central base',round(m*100,1))
# beside: default pair (c) with net divestments credited (net purchases negative -> adds to owner cash)
adj=-(sum(acq)-sum(divs))/5
b=avg(maint_m)+adj
lo=(value(b,0,sov)-netdebt)/shares; hi=(value(b,g_rev,sov)-netdebt)/shares
f0=(value(b,0,floor)-netdebt)/shares; f1=(value(b,g_rev,floor)-netdebt)/shares
print(f'beside net sales credited: base {b:.0f} range EUR {lo:.2f}-{hi:.2f} fair {(f0+f1)/2:.2f} IRR growth {irr(b,g_rev,mcap+netdebt)*100:.2f}%')
