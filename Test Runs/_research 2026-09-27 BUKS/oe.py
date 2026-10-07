import json
P={int(k):v for k,v in json.load(open('cfs_parsed.json')).items()}
# newest filed vintage where a later 10-K re-presented the year (read in cfs_2014/2015/2016/2023 comparatives)
NEWEST={2013:dict(ocf=3010.0),2014:dict(ocf=5001.0),2015:dict(ocf=5369.0,capex=-5065.0),2022:dict(ocf=11178.0)}
NCI_DIST_FIX={2013:-320.0}
# NCI share of consolidated income, companyfacts NetIncomeLossAttributableToNoncontrollingInterest (xb_out.txt), $K
NCI={2012:2000,2013:1000,2014:400,2015:800,2016:800,2017:800,2018:900,2019:1800,2020:-1000,2021:1000,2022:1900}
import sys
sys.path.insert(0,'.')
# refine NCI to the tag's exact values
F=json.load(open('companyfacts.json'))['facts']['us-gaap']['NetIncomeLossAttributableToNoncontrollingInterest']['units']['USD']
from datetime import date
best={}
for x in F:
    if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
    if not 340<=(date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<=380: continue
    e=int(x['end'][:4])
    if e not in best or x['filed']>best[e][1]: best[e]=(x['val']/1000,x['filed'])
NCI={y:v[0] for y,v in best.items()}
ACQ={2021:41205.0,2022:16400.0}  # casino land and building (non-cash, secured notes); remaining BHCMC units
CAP=257922.161  # $K at $4.04 x 63,842,119
rows={}
print('| FY | OCF | stock comp (all captions) | capex (incl. STCs) | D&A line | NCI share of income | OE capex end | OE D&A end | acquisitions | OE capex end with acquisitions |')
print('|---|---|---|---|---|---|---|---|---|---|')
for y in range(2011,2027):
    d=dict(P[y]); d.update(NEWEST.get(y,{}))
    sbc=sum((d.get(k) or 0) for k in ('stock_401k','stock_opt','stock_serv','stock_dir','rsu'))
    capex=-(d['capex'] or 0); da=(d['da'] or 0)+(d.get('stc_amort') or 0)
    nci=NCI.get(y,0.0) if y<=2022 else 0.0
    ocf=d['ocf']
    ce=ocf-sbc-capex-nci; de=ocf-sbc-da-nci; acq=ACQ.get(y,0.0)
    rows[y]=(ce,de,ce-acq,ocf,sbc,capex,da,nci)
    print(f'| {y} | {ocf/1e3:.1f} | {sbc/1e3:.2f} | {capex/1e3:.1f} | {da/1e3:.1f} | {nci/1e3:.2f} | **{ce/1e3:.1f}** | **{de/1e3:.1f}** | {acq/1e3:.1f} | {(ce-acq)/1e3:.1f} |')
print()
def win(a,b):
    ys=range(a,b+1); n=len(ys)
    c=sum(rows[y][0] for y in ys)/n; d=sum(rows[y][1] for y in ys)/n; q=sum(rows[y][2] for y in ys)/n
    return c,d,q
print('Trailing windows ending FY2026 (mean $M; yield on $257.9M cap):')
for n in (1,2,3,5,7,10,15,16):
    c,d,q=win(2027-n,2026)
    lo,hi=min(c,d),max(c,d)
    print(f'{n:>2}y {2027-n}-2026: ${lo/1e3:.1f}M-${hi/1e3:.1f}M  {lo/CAP:.2%}-{hi/CAP:.2%} | with acquisitions (capex end) ${q/1e3:.1f}M {q/CAP:.2%}')
print('Rolling 5-year windows (capex end / D&A end / with acq):')
for e in range(2015,2027):
    c,d,q=win(e-4,e); print(f'  {e-4}-{e}: {c/1e3:.1f} / {d/1e3:.1f} / {q/1e3:.1f}')
print('Rolling 3-year windows:')
for e in range(2013,2027):
    c,d,q=win(e-2,e); print(f'  {e-2}-{e}: {c/1e3:.1f} / {d/1e3:.1f} / {q/1e3:.1f}')
allv=[]
for n in (3,5,7,10,15,16):
    c,d,q=win(2027-n,2026); allv+= [c,d]
print('Combined trailing 3-16y both ends: $%.1fM to $%.1fM, %.2f%% to %.2f%%'%(min(allv)/1e3,max(allv)/1e3,100*min(allv)/CAP,100*max(allv)/CAP))
# TTM through 2026-07-31: FY2026 + Q1FY27 - Q1FY26 (10-Q)
ocf=25779-14699+4639; capex=6538-1438+1890; sbc=(213+196)-(63+34)+(50+66); da=6865-1703+1771
print('TTM to 2026-07-31: OCF %.1f capex %.1f sbc %.2f D&A %.1f -> OE %.1f to %.1f'%(ocf/1e3,capex/1e3,sbc/1e3,da/1e3,(ocf-sbc-max(capex,da))/1e3,(ocf-sbc-min(capex,da))/1e3))
print('capex/D&A sum 2012-2026: %.2f; 2022-2026: %.2f'%(sum(rows[y][5] for y in range(2012,2027))/sum(rows[y][6] for y in range(2012,2027)), sum(rows[y][5] for y in range(2022,2027))/sum(rows[y][6] for y in range(2022,2027))))
