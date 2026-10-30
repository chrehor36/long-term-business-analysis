"""JKHY owner earnings, every trailing window, both (c) ends. $M. Arithmetic only.
OCF as filed (newest vintage). SBC subtracted in full: FY2006+ the cash-flow line (XBRL from FY2009); FY2000-2005 the
SFAS 123 pro forma deduction as filed (net of tax; the filer gives no pre-tax figure). Capex end = capital expenditures +
computer software developed + purchased software/intangibles. D&A end = depreciation + computer-software amortization
(acquired customer relationships and other intangibles excluded); FY2000-2006 software amortization is not separately
filed, so the D&A end there uses the whole filed 'Amortization' line (an upper bound on (c); pre-2002 it includes goodwill).
Acquisitions = payment for acquisitions net of cash acquired (+ purchase of customer contracts 2003)."""
import json,sys
sys.stdout.reconfigure(encoding='utf-8')
X={k:{int(y):v/1e6 for y,v in d.items()} for k,d in json.load(open('xb.json')).items()}
# FY2000-2008 from the filed statements ($K -> $M): 10-K FY2002 (2000-2002), FY2005 (2003-2005), FY2008 (2006-2008)
old={2000:dict(ocf=48860,sbc=7847,capex=32619,dev=875,sw=0,acq=93280,dep=8870,amort=6603),
     2001:dict(ocf=72822,sbc=19181,capex=57781,dev=1447,sw=0,acq=0,dep=12539,amort=9349),
     2002:dict(ocf=89941,sbc=9394,capex=49509,dev=1895,sw=0,acq=11111,dep=20885,amort=6585),
     2003:dict(ocf=98861,sbc=6572,capex=45958,dev=5162,sw=0,acq=6537+304,dep=24025,amort=6169),
     2004:dict(ocf=112809,sbc=7187,capex=49141,dev=4409,sw=0,acq=48288,dep=26790,amort=6750),
     2005:dict(ocf=108275,sbc=1614,capex=58046,dev=7846,sw=0,acq=119501,dep=29795,amort=9116),
     2006:dict(ocf=169438,sbc=454,capex=45396,dev=16079,sw=0,acq=20745,dep=33442,amort=10332),
     2007:dict(ocf=174247,sbc=1003,capex=34202,dev=20743,sw=0,acq=39307,dep=36427,amort=7908),
     2008:dict(ocf=181001,sbc=1444,capex=31105,dev=23736,sw=0,acq=49324,dep=40195,amort=13505)}
swam={2009:16920,2010:17782,2011:31189,2012:32807,2013:33145,2014:37720,2015:43798,2016:54810,2017:60880,2018:72859,2019:82605,
      2020:92460,2021:99305,2022:105036,2023:123210,2024:137958,2025:148734,2026:154212}
R={}
for y,d in old.items(): R[y]={k:v/1e3 for k,v in d.items()}
for y in range(2009,2027):
    g=lambda k: X[k].get(y,0.0) or 0.0
    R[y]=dict(ocf=g('ocf'),sbc=g('sbc'),capex=g('capex'),dev=g('dev'),sw=g('sw1')+(g('sw2') if y>=2020 else 0)+g('intang'),acq=g('acq'),dep=g('dep'),amort=swam[y]/1e3)
dtax2026=126.032
rows={}
print('| FY | OCF | SBC | capex | software developed | purchased software | (c) capex end | depreciation | software amort. | (c) D&A end | acquisitions | OE capex end | OE D&A end | OE capex end with acquisitions |')
print('|'+'---|'*14)
for y in sorted(R):
    d=R[y]; cc=d['capex']+d['dev']+d['sw']; cd=d['dep']+d['amort']
    oc=d['ocf']-d['sbc']-cc; od=d['ocf']-d['sbc']-cd; oa=oc-d['acq']
    rows[y]=(oc,od,oa,cc,cd)
    print(f"| {y} | {d['ocf']:,.1f} | {d['sbc']:,.1f} | {d['capex']:,.1f} | {d['dev']:,.1f} | {d['sw']:,.1f} | {cc:,.1f} | {d['dep']:,.1f} | {d['amort']:,.1f} | {cd:,.1f} | {d['acq']:,.1f} | **{oc:,.1f}** | **{od:,.1f}** | {oa:,.1f} |")
json.dump({y:dict(zip(['oe_capex','oe_da','oe_acq','c_capex','c_da'],v)) for y,v in rows.items()},open('oe_rows.json','w'),indent=0)
CAP=147.79*70112608/1e6
print('\ncap',round(CAP,1))
def win(n,adj=False):
    ys=list(range(2027-n,2027))
    a=[rows[y][0]-(dtax2026 if adj and y==2026 else 0) for y in ys]; b=[rows[y][1]-(dtax2026 if adj and y==2026 else 0) for y in ys]; c=[rows[y][2]-(dtax2026 if adj and y==2026 else 0) for y in ys]
    return sum(a)/n,sum(b)/n,sum(c)/n
print('\n| trailing window | OE capex end | OE D&A end | yield range on cap | with acquisitions | yield |  FY2026 deferred-tax catch-up removed: capex end / D&A end / yield |')
print('|---|---|---|---|---|---|---|')
allv=[];allv_adj=[]
for n in range(1,28):
    a,b,c=win(n); a2,b2,c2=win(n,True)
    lo,hi=min(a,b),max(a,b)
    if n>=3: allv+= [a,b]; allv_adj+=[a2,b2]
    print(f"| {n}y ({2027-n}-2026) | {a:,.1f} | {b:,.1f} | {lo/CAP:.2%}-{hi/CAP:.2%} | {c:,.1f} | {c/CAP:.2%} | {a2:,.1f} / {b2:,.1f} / {min(a2,b2)/CAP:.2%}-{max(a2,b2)/CAP:.2%} |")
print(f"\nALL trailing windows 3-27y, both ends: {min(allv):,.1f} to {max(allv):,.1f} = {min(allv)/CAP:.2%} to {max(allv)/CAP:.2%}")
print(f"same, FY2026 catch-up removed: {min(allv_adj):,.1f} to {max(allv_adj):,.1f} = {min(allv_adj)/CAP:.2%} to {max(allv_adj)/CAP:.2%}")
# rolling 5y windows
print('\nrolling 5-year means (capex end / D&A end / with acquisitions):')
for e in range(2004,2027):
    ys=range(e-4,e+1); print(e-4,'-',e, round(sum(rows[y][0] for y in ys)/5,1), round(sum(rows[y][1] for y in ys)/5,1), round(sum(rows[y][2] for y in ys)/5,1))
print('\n(c) capex end / D&A end by year:', ', '.join(f"{y}:{rows[y][3]/rows[y][4]:.2f}" for y in sorted(rows)))
