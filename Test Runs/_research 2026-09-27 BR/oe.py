"""BR owner earnings from the filed cash-flow statements (cfs.json, newest filed vintage per fiscal year). Arithmetic only.
OE capex end = OCF - SBC - (capital expenditures + software purchases/purchases of intangibles)
OE D&A end   = OCF - SBC - 'Depreciation and amortization' line (acquired-intangible amortization excluded where the vintage
               splits it out, from fiscal 2010; 'Amortization of other assets' excluded because the cash for those deferred
               client costs is already inside OCF via 'Other non-current assets')
With acquisitions = capex end - acquisitions net of cash - purchases of intellectual property.
Display only: OCF with deferred client-cost spending replaced by its amortization (OCF - onca_change - otham)."""
import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
R={int(k):v for k,v in json.load(open('cfs.json')).items()}
CAP=163.77*114021798/1e6
def val(fy,key):
    for v in range(min(fy+2,2026),fy-1,-1):
        g=R.get(v,{})
        if key in g and len(g[key])==3:
            return g[key][v-fy], v
    return None,None
rows={}
print(f'cap ${CAP:,.1f}M')
print('| FY | OCF | SBC | capex | software | D&A line | acq. amort (sep.) | acquisitions+IP | client-cost spend (onca) | amort. other assets | **OE capex end** | **OE D&A end** | OE with acquisitions | display: OCF w/ client costs at amortization, capex end | vintage |')
print('|'+'---|'*15)
for fy in range(2007,2027):
    o,vo=val(fy,'ocf'); s,_=val(fy,'sbc'); c,_=val(fy,'capex'); sw,_=val(fy,'soft'); d,vd=val(fy,'da'); aa,_=val(fy,'acqam')
    a,_=val(fy,'acq'); ip,_=val(fy,'ipp'); on,_=val(fy,'onca'); oa,_=val(fy,'otham')
    a=a or 0.0; ip=ip or 0.0; sw=sw or 0.0
    ce=o-s+c+sw; de=o-s-d; wa=ce+a+ip
    disp=(o-(on or 0)-(oa or 0))-s+c+sw if on is not None and oa is not None else None
    rows[fy]=dict(ce=ce,de=de,wa=wa,disp=disp,o=o,s=s,cx=-(c+sw),d=d)
    f=lambda x: f'{x:,.1f}' if x is not None else 'n/f'
    print(f'| {fy} | {f(o)} | {f(s)} | {f(-c)} | {f(-sw)} | {f(d)} | {f(aa)} | {f(-(a+ip))} | {f(-on if on is not None else None)} | {f(oa)} | **{f(ce)}** | **{f(de)}** | {f(wa)} | {f(disp)} | {vo} |')
print()
def mean(ys,k): 
    v=[rows[y][k] for y in ys]; return sum(v)/len(v)
print('TRAILING WINDOWS ending 2026 (continuing perimeter from 2008):')
lo=hi=None
for n in (3,5,7,10,15,19):
    ys=range(2027-n,2027)
    ce=mean(ys,'ce'); de=mean(ys,'de'); wa=mean(ys,'wa'); dp=mean(ys,'disp')
    a,b=min(ce,de),max(ce,de)
    lo=a if lo is None else min(lo,a); hi=b if hi is None else max(hi,b)
    print(f'{n}y {min(ys)}-2026: capex end {ce:,.1f} ({ce/CAP:.2%}) | D&A end {de:,.1f} ({de/CAP:.2%}) | with acquisitions {wa:,.1f} ({wa/CAP:.2%}) | display client-costs-at-amort {dp:,.1f} ({dp/CAP:.2%})')
print(f'COMBINED RANGE every trailing window 3-19y both ends: {lo:,.1f} to {hi:,.1f} = {lo/CAP:.2%} to {hi/CAP:.2%}')
print('ROLLING 5y windows:')
for e in range(2012,2027):
    ys=range(e-4,e+1); print(f' {e-4}-{e}: capex {mean(ys,"ce"):,.1f} D&A {mean(ys,"de"):,.1f} with acq {mean(ys,"wa"):,.1f}')
print('ROLLING 3y windows:')
for e in range(2010,2027):
    ys=range(e-2,e+1); print(f' {e-2}-{e}: capex {mean(ys,"ce"):,.1f} D&A {mean(ys,"de"):,.1f}')
