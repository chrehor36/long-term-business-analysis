"""Owner earnings for GWW, every trailing window, both (c) ends, consolidated and attributable.
OCF newest filed vintage; capex = property additions + capitalized-software additions (combined in the XBRL tag from FY2007);
D&A end = property depreciation + capitalized-software amortization (FY1991-FY2008, from the face; acquired goodwill/intangible
amortization excluded) and the face 'Depreciation and amortization' line FY2009-FY2025 (which also carries acquired-intangible
amortization, $7-20M a year FY2009-FY2015, more after the 2015 Cromwell purchase; conservative, not split).
SBC: face line FY2004-FY2025; FY2002-FY2005 total after-tax fair-value expense (SFAS 123 table) where larger; FY1995-FY2001 the
after-tax pro forma decrement; FY1991-FY1994 none disclosed (understated). NCI: net earnings attributable to the noncontrolling
interest (MonotaRO) FY2009-TTM, deducted for the attributable construction."""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# $M. year: (ocf, capex_total, dep_end, sbc, nci, source)
D = {
1991:(150.577, 32.778, 33.045, 0, 0,'10-K FY1993'),
1992:(196.368, 49.920, 35.217, 0, 0,'10-K FY1993'),
1993:(162.498, 98.405, 40.576, 0, 0,'10-K FY1993/FY1994'),
1994:(191.382,120.357, 49.795, 0, 0,'10-K FY1994'),
1995:(126.237,111.935, 57.760, 0.655, 0,'10-K FY1997 (OCF restated), FY1995'),
1996:(272.410, 62.051+0.900, 61.585+2.474, 1.830, 0,'10-K FY1998'),
1997:(432.910,108.252+0.122, 63.257+1.556, 2.726, 0,'10-K FY1999 (OCF restated)'),
1998:(331.481,132.857+36.983, 58.256+4.645, 4.247, 0,'10-K FY2000 (OCF, capex restated); software FY1998 10-K'),
1999:( 37.240,111.900+26.473, 72.446+9.840, 6.587, 0,'10-K FY2000 (restated)'),
2000:(278.395, 65.507+29.406, 81.898+16.249, 9.772, 0,'EX-13 FY2002 (OCF), 10-K FY2000'),
2001:(509.181,100.451+6.717, 77.737+19.483, 12.261, 0,'EX-13 FY2002 (OCF), 10-K FY2001'),
2002:(303.470,133.978+10.047, 75.226+18.262, 18.790, 0,'10-K FY2004'),
2003:(394.108, 74.064+6.422, 74.583+15.670, 17.740, 0,'10-K FY2004'),
2004:(406.487,128.276+32.482, 85.566+12.690, max(20.940,8.226), 0,'10-K FY2004/FY2006'),
2005:(432.543,112.297+44.950, 98.087+10.695, max(16.733,9.015), 0,'10-K FY2005/FY2006'),
2006:(436.753,127.814+8.950, 100.975+17.593, 33.741, 0,'10-K FY2006/FY2007'),
2007:(468.875,188.867+8.556, 106.839+25.160, 35.551, 0,'10-K FY2007'),
}
f = json.load(open('facts.json'))['facts']['us-gaap']
import datetime
def newest(tag):
    out={}
    for v in f.get(tag,{}).get('units',{}).get('USD',[]):
        if v.get('form')!='10-K' or 'start' not in v: continue
        d=(datetime.date.fromisoformat(v['end'])-datetime.date.fromisoformat(v['start'])).days
        if not 350<d<380: continue
        y=int(v['end'][:4])
        if y not in out or v['filed']>out[y][1]: out[y]=(abs(v['val'])/1e6,v['filed'])
    return {y:x[0] for y,x in out.items()}
ocf=newest('NetCashProvidedByUsedInOperatingActivities'); cx=newest('PaymentsToAcquirePropertyPlantAndEquipment')
da=newest('DepreciationAndAmortization'); sbc=newest('ShareBasedCompensation'); nci=newest('NetIncomeLossAttributableToNoncontrollingInterest')
acq=newest('PaymentsToAcquireBusinessesNetOfCashAcquired')
for y in range(2008,2026):
    D[y]=(ocf[y],cx[y],da[y],sbc[y],nci.get(y,0),'companyfacts newest 10-K value')
TTM=(2015-1023+1183, 684-300+281, 254-125+128, 64-35+39, 102-47+56)
CAP=1243.07*47100942/1e6
print(f'cap ${CAP:,.1f}M')
print('FY    OCF    capex   D&A    SBC    NCI  | OE capex  OE D&A | attrib capex attrib D&A')
rows={}
for y in sorted(D):
    o,c,d,s,n,src=D[y]
    a=o-s-c; b=o-s-d
    rows[y]=(a,b,a-n,b-n)
    print(f'{y} {o:7.1f} {c:7.1f} {d:6.1f} {s:6.1f} {n:6.1f} | {a:7.1f} {b:7.1f} | {a-n:7.1f} {b-n:7.1f}   {src}')
o,c,d,s,n=TTM
print(f'TTM {o:7.1f} {c:7.1f} {d:6.1f} {s:6.1f} {n:6.1f} | {o-s-c:7.1f} {o-s-d:7.1f} | {o-s-c-n:7.1f} {o-s-d-n:7.1f}   10-K FY2025 + 10-Q H1 2026 - H1 2025')
print('\nTrailing windows ending FY2025 (mean $M, % of cap):')
lo=hi=None; alo=ahi=None
for w in [1,3,5,10,15,20,25,30,35]:
    ys=[y for y in range(2025-w+1,2026) if y in rows]
    if len(ys)<w: continue
    m=[sum(rows[y][k] for y in ys)/w for k in range(4)]
    print(f' {w:2d}y FY{ys[0]}-{ys[-1]}: capex {m[0]:7.1f} ({m[0]/CAP*100:.2f}%)  D&A {m[1]:7.1f} ({m[1]/CAP*100:.2f}%)  | attributable capex {m[2]:7.1f} ({m[2]/CAP*100:.2f}%)  D&A {m[3]:7.1f} ({m[3]/CAP*100:.2f}%)')
allm=[]; allattr=[]
for w in range(1,36):
    ys=[y for y in range(2025-w+1,2026) if y in rows]
    if len(ys)<w: break
    m=[sum(rows[y][k] for y in ys)/w for k in range(4)]
    allm+=m[:2]; allattr+=m[2:]
print(f'\nEvery trailing window 1-{w-1 if len(ys)<w else w} yrs: consolidated ${min(allm):.1f}-{max(allm):.1f}M ({min(allm)/CAP*100:.2f}-{max(allm)/CAP*100:.2f}%); attributable ${min(allattr):.1f}-{max(allattr):.1f}M ({min(allattr)/CAP*100:.2f}-{max(allattr)/CAP*100:.2f}%)')
print('\nRolling five-year windows (capex end, D&A end, consolidated):')
for e in range(1995,2026):
    ys=list(range(e-4,e+1))
    if all(y in rows for y in ys):
        a=sum(rows[y][0] for y in ys)/5; b=sum(rows[y][1] for y in ys)/5
        print(f'  FY{ys[0]}-{e}: {a:7.1f} {b:7.1f}')
print('\nNegative years:',[ (y,round(rows[y][0]),round(rows[y][1])) for y in rows if rows[y][0]<0 or rows[y][1]<0])
print('\nCapex / D&A cumulative FY1991-2025: %.2f; FY2021-2025: %.2f' % (sum(D[y][1] for y in D)/sum(D[y][2] for y in D), sum(D[y][1] for y in range(2021,2026))/sum(D[y][2] for y in range(2021,2026))))
print('Acquisitions (tag) ', {y:round(v,1) for y,v in acq.items()})
json.dump({str(k):v for k,v in rows.items()},open('oe_rows.json','w'))
