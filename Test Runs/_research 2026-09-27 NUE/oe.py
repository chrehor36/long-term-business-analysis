"""NUE owner earnings from the FILED cash-flow statements (cfs_raw.json via cfs.py; newest filed vintage per fiscal year).
COMPUTATION - NOT A CLEARANCE. Arithmetic only; the (c) guess is displayed at both ends, never chosen here.
  OE capex end = OCF - SBC - capital expenditures
  OE D&A end   = OCF - SBC - (depreciation + amortization lines)
  with acquisitions = capex end - acquisitions (net of cash acquired) - investment in and advances to affiliates
  attributable = the same, less distributions to noncontrolling interests (the 49% partners in Nucor-Yamato, CSI, NJSM
                 and others take their share in cash; OCF is consolidated). A disclosed judgment, displayed beside the
                 consolidated figure.
SBC: the face line from FY2004 (FY2006 vintage restates FY2004-05); FY2000-03 have no SBC on the face (APB 25) and the
fair-value total from the SFAS 123 pro forma note is used (after tax, so slightly understated; FY2000-01 from the FY2002
report, FY2002-03 from the FY2004 report)."""
import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
R={int(k):v for k,v in json.load(open('cfs_raw.json')).items()}
SKIP={2022,2023}   # vintages whose statement did not parse cleanly; their years are covered by the adjacent vintages
PRO_SBC={2000:4.3,2001:4.5,2002:6.1,2003:7.7}
CAP=247.25*226875676/1e6
def scale(v):
    o=v.get('ocf')
    if not o: return 1
    m=abs(o[0])
    return 1e6 if m>1e7 else (1e3 if m>2e4 else 1)
def val(fy,key):
    for vin in range(min(fy+2,2025),fy-1,-1):
        if vin in SKIP: continue
        g=R.get(vin,{})
        if key in g and len(g[key])==3:
            s=scale(g); return g[key][vin-fy]/s, vin
    return None,None
rows={}
hdr='| FY | OCF | SBC | capex | D&A | acq.+affiliates | NCI distrib. | **OE capex end** | **OE D&A end** | capex end with acq. | capex end attributable | vintage |'
print(f'cap ${CAP:,.1f}M'); print(hdr); print('|'+'---|'*12)
for fy in range(2000,2026):
    o,vo=val(fy,'ocf'); c,_=val(fy,'capex'); d,_=val(fy,'dep'); am,_=val(fy,'amort'); s,_=val(fy,'sbc')
    a,_=val(fy,'acq'); af,_=val(fy,'aff'); n,_=val(fy,'nci')
    if s is None: s=PRO_SBC.get(fy)
    am=am or 0.0; a=a or 0.0; af=af or 0.0; n=n or 0.0
    da=d+am; ce=o-s+c; de=o-s-da; wa=ce+a+af; at=ce+n
    rows[fy]=dict(ce=ce,de=de,wa=wa,at=at,dat=de+n,o=o,s=s,c=-c,da=da)
    print(f'| {fy} | {o:,.1f} | {s:,.1f} | {-c:,.1f} | {da:,.1f} | {-(a+af):,.1f} | {-n:,.1f} | **{ce:,.1f}** | **{de:,.1f}** | {wa:,.1f} | {at:,.1f} | {vo} |')
def mean(ys,k): v=[rows[y][k] for y in ys]; return sum(v)/len(v)
print('\nTRAILING WINDOWS ending FY2025:')
lo=hi=None; alo=ahi=None
for n in range(1,27):
    ys=range(2026-n,2026)
    ce,de,wa,at,dat=(mean(ys,k) for k in ('ce','de','wa','at','dat'))
    if n>=3:
        lo=min(x for x in (ce,de) if True) if lo is None else min(lo,ce,de); hi=max(ce,de) if hi is None else max(hi,ce,de)
        alo=min(at,dat) if alo is None else min(alo,at,dat); ahi=max(at,dat) if ahi is None else max(ahi,at,dat)
    print(f'{n:2d}y {min(ys)}-2025: capex end {ce:,.1f} ({ce/CAP:.2%}) | D&A end {de:,.1f} ({de/CAP:.2%}) | capex end with acq. {wa:,.1f} ({wa/CAP:.2%}) | attributable capex end {at:,.1f} ({at/CAP:.2%}) D&A end {dat:,.1f} ({dat/CAP:.2%})')
print(f'\nCOMBINED RANGE, every trailing window 3-26y, both ends, consolidated: {lo:,.1f} to {hi:,.1f} = {lo/CAP:.2%} to {hi/CAP:.2%}')
print(f'COMBINED RANGE, same, attributable (less NCI distributions): {alo:,.1f} to {ahi:,.1f} = {alo/CAP:.2%} to {ahi/CAP:.2%}')
print('\nROLLING 5y windows (capex end / D&A end / capex end with acq. / attributable capex end):')
for e in range(2004,2026):
    ys=range(e-4,e+1); print(f' {e-4}-{e}: {mean(ys,"ce"):,.1f} / {mean(ys,"de"):,.1f} / {mean(ys,"wa"):,.1f} / {mean(ys,"at"):,.1f}')
neg_ce=[y for y in rows if rows[y]['ce']<0]; neg_wa=[y for y in rows if rows[y]['wa']<0]
print('\nyears negative at capex end:',neg_ce); print('years negative with acquisitions:',neg_wa)
tc=sum(rows[y]['c'] for y in rows); td=sum(rows[y]['da'] for y in rows); print(f'capex/D&A FY2000-2025 cumulative: {tc:,.1f} / {td:,.1f} = {tc/td:.2f}')
# TTM to 2026-07-04 from the 10-Q (six months 2026 and 2025) and the FY2025 statement
o=3234+2286-1096; c=3422+1232-1813; s=133+91-78; da=1480+(641+126)-(606+128); n=249+282-214
print(f'\nTTM to 2026-07-04: OCF {o} SBC {s} capex {c} D&A {da} NCI {n} -> capex end {o-s-c} ({(o-s-c)/CAP:.2%}), D&A end {o-s-da} ({(o-s-da)/CAP:.2%}), attributable capex end {o-s-c-n} ({(o-s-c-n)/CAP:.2%})')
