"""Owner earnings for CHD, fiscal 2005-2025, from the filed cash-flow statements (cf_parsed.json, each year from the
10-K presenting it as the current year). Arithmetic only; (c) is a disclosed judgment shown at both ends.
OE = operating cash flow as filed - recurring SBC - (c).
Recurring SBC = 'Non-cash compensation expense' less acquisition-related restricted stock (Hero 2022-25, Touchland 2025),
which is moved to the acquisitions column. 2005: no SBC line (APB 25); the pro forma after-tax fair-value charge ($4.8M) is used, flagged.
Capex end: 'Additions to property, plant and equipment' (gross). Depreciation end: 'Depreciation expense' (2007-08 from the 2009 10-K
prior-year columns; 2005-06 = the combined D&A line less the note's intangible amortization).
Acquisitions line = acquisitions + contingent acquisition payments + payments of business acquisition liabilities
+ acquisition-related restricted stock + earnout fair-value charge, less proceeds from businesses sold."""
import json
cf=json.load(open('cf_parsed.json'))
dep={'2005':44.158-8.6,'2006':51.727-13.5,'2007':35.827,'2008':45.600}
acqstock={'2022':6.2,'2023':29.2,'2024':20.3,'2025':5.8+11.5}
interest={'2005':41.966,'2006':52.268,'2007':55.522,'2008':43.3,'2009':29.9,'2010':29.3,'2011':9.2,'2012':9.7,'2013':26.4,'2014':25.7,'2015':29.0,'2016':25.6,'2017':33.3,'2018':74.9,'2019':70.6,'2020':58.8,'2021':51.8,'2022':86.0,'2023':111.9,'2024':94.4,'2025':94.6}
rows={}
for y in [str(v) for v in range(2005,2026)]:
    r=cf[y]
    ocf=r['ocf']; sbc_all=r.get('sbc',4.814 if y=='2005' else 0)
    a_st=acqstock.get(y,0.0); sbc=sbc_all-a_st
    cap=-r['capex']; d=dep.get(y,r.get('dep'))
    acq=-(r.get('acq',0)+r.get('contingent',0)+r.get('payacq',0)) + a_st + (r.get('fvacq',0) if r.get('fvacq',0)>0 else 0)
    disp=r.get('sale_vit',0)+r.get('sale_passport',0)+r.get('held_for_sale',0)
    acq_net=acq-disp
    oe_c=ocf-sbc-cap; oe_d=ocf-sbc-d
    it=interest[y]
    cov=(ocf+it-cap)/it
    rows[y]=dict(ocf=ocf,sbc=sbc,sbc_all=sbc_all,capex=cap,dep=d,oe_capex=oe_c,oe_dep=oe_d,acq=acq_net,oe_acq=oe_c-acq_net,ratio=cap/d,interest=it,cov=cov,cov_acq=(ocf+it-cap-acq_net)/it)
json.dump(rows,open('oe_rows.json','w'),indent=1)
print('| year | OCF | SBC (recurring) | capex | depreciation | OE, capex end | OE, depreciation end | acquisitions net of disposals | OE capex end incl. acquisitions | capex/dep | cash interest | [E2-54] coverage | same incl. acquisitions |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for y,m in rows.items():
    print(f"| {y} | {m['ocf']:,.1f} | {m['sbc']:.1f} | {m['capex']:.1f} | {m['dep']:.1f} | {m['oe_capex']:,.1f} | {m['oe_dep']:,.1f} | {m['acq']:,.1f} | {m['oe_acq']:,.1f} | {m['ratio']:.2f} | {m['interest']:.1f} | {m['cov']:.1f} | {m['cov_acq']:.1f} |")
CAP=96.38*237203907/1e6
print('\ncap',round(CAP,1))
print('| window | capex end | depreciation end | yield, capex end | yield, depreciation end | capex end incl. acquisitions |')
print('|---|---|---|---|---|---|')
allv=[]
for n in range(3,22):
    ys=[str(v) for v in range(2026-n,2026)]
    c=sum(rows[y]['oe_capex'] for y in ys)/n; d=sum(rows[y]['oe_dep'] for y in ys)/n; a=sum(rows[y]['oe_acq'] for y in ys)/n
    allv+= [c,d]
    print(f"| {n}y {ys[0]}-{ys[-1][2:]} | ${c:,.1f}M | ${d:,.1f}M | {c/CAP:.2%} | {d/CAP:.2%} | ${a:,.1f}M |")
print('range',round(min(allv),1),round(max(allv),1), f"{min(allv)/CAP:.2%} {max(allv)/CAP:.2%}")
