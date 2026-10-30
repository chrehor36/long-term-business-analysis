# Owner earnings beneath the close, MLI. Arithmetic only (COMPUTATION - NOT A CLEARANCE).
# Each year from the latest filed 10-K cash-flow statement showing it (cf_parsed.json, parsed by cfparse.py),
# 2006 from the FY2008 10-K. NCI share of earnings from the filed income statements (2006-2008) and the
# companyfacts tag NetIncomeLossAttributableToNoncontrollingInterest (2009-2025), checked to FY2025 statement.
import json
d=json.load(open('cf_parsed.json'))
CAP=13385.9
NCI={2006:2610,2007:582,2008:1796,2009:662,2010:1364,2011:765,2012:1278,2013:689,2014:974,2015:543,2016:27,2017:1413,2018:2361,2019:5260,2020:4156,2021:6604,2022:4504,2023:6752,2024:12663,2025:8399}
def g(fy,label,col):
    v=d[str(fy)].get(label)
    return 0.0 if v is None else v[col]
rows={}
for y in range(2006,2026):
    if y<=2023: fy,col=(y+2,2)
    elif y==2024: fy,col=(2025,1)
    else: fy,col=(2025,0)
    if y==2006: fy,col=(2008,2)
    if y==2007: fy,col=(2009,2)
    if y==2008: fy,col=(2010,2)
    r=dict(src='FY%d'%fy,
      ocf=g(fy,'Net cash provided by operating activities',col),
      dep=g(fy,'Depreciation',col),
      am=g(fy,'Amortization of intangibles',col),
      sbc=g(fy,'Stock-based compensation expense',col),
      capex=-g(fy,'Capital expenditures',col),
      wc=g(fy,'Receivables',col)+g(fy,'Inventories',col)+g(fy,'Current liabilities',col),
      ins=g(fy,'Insurance proceeds',col) if y>=2008 else 0.0,
      nci=NCI[y])
    for k in list(r):
        if k!='src': r[k]=r[k]/1000.0
    base=r['ocf']-r['sbc']-r['nci']
    r['oe_da']=base-r['dep']
    r['oe_cx']=base-r['capex']
    r['oe_cx_ins']=r['oe_cx']-r['ins']
    r['oe_cx_wc']=r['oe_cx']-r['wc']
    rows[y]=r
# TTM to 2026-06-27: FY2025 + H1 2026 - H1 2025 (10-Qs 0000089439-26-000032 and the Q2 2025 10-Q)
h26=dict(ocf=292.001,sbc=15.846,capex=38.796,nci=3.003,ins=0.0,wc=-292.241-89.164+167.903)
h25=dict(ocf=304.161,sbc=13.940,capex=30.691,nci=4.414,ins=12.345,wc=-134.535-41.190+72.259)
t={k:rows[2025][k]+h26[k]-h25[k] for k in h26}
t['oe_cx']=t['ocf']-t['sbc']-t['nci']-t['capex']
print('year src   OCF    SBC   NCI   dep  amort  capex  WC3   ins   OE_DA  OE_CX  OE_CX_exins OE_CX_exWC')
for y,r in rows.items():
    print('%d %s %7.1f %5.1f %5.1f %5.1f %5.1f %6.1f %7.1f %5.1f %7.1f %7.1f %7.1f %7.1f'%(y,r['src'],r['ocf'],r['sbc'],r['nci'],r['dep'],r['am'],r['capex'],r['wc'],r['ins'],r['oe_da'],r['oe_cx'],r['oe_cx_ins'],r['oe_cx_wc']))
print('TTM 2026-06-27: OCF %.1f SBC %.1f NCI %.1f capex %.1f WC %.1f OE_CX %.1f yield %.2f%%'%(t['ocf'],t['sbc'],t['nci'],t['capex'],t['wc'],t['oe_cx'],100*t['oe_cx']/CAP))
def mean(ys,k): return sum(rows[y][k] for y in ys)/len(ys)
print()
print('window        OE_CX    OE_DA   y_CX   y_DA   exIns_CX  exWC_CX  vs_sov_CX vs_sov_DA')
allv=[]
for n in range(3,21):
    ys=range(2026-n,2026)
    a,b,c,e=mean(ys,'oe_cx'),mean(ys,'oe_da'),mean(ys,'oe_cx_ins'),mean(ys,'oe_cx_wc')
    allv+= [a,b]
    print('%2dy %d-25  %7.1f  %7.1f  %5.2f%%  %5.2f%%  %7.1f  %7.1f  %+.2f %+.2f'%(n,2026-n,a,b,100*a/CAP,100*b/CAP,c,e,100*a/CAP-5.49,100*b/CAP-5.49))
print('range all windows both ends: %.1f to %.1f (%.2f%% to %.2f%%)'%(min(allv),max(allv),100*min(allv)/CAP,100*max(allv)/CAP))
for lab,ys in [('pre-step 2006-2020',range(2006,2021)),('pre-step 2011-2020',range(2011,2021)),('step 2021-2025',range(2021,2026)),('pre-step 2016-2020',range(2016,2021))]:
    print(lab,'CX %.1f DA %.1f exIns %.1f exWC %.1f  y_CX %.2f%% y_DA %.2f%%'%(mean(ys,'oe_cx'),mean(ys,'oe_da'),mean(ys,'oe_cx_ins'),mean(ys,'oe_cx_wc'),100*mean(ys,'oe_cx')/CAP,100*mean(ys,'oe_da')/CAP))
tot=sum(rows[y]['oe_cx'] for y in rows); step=sum(rows[y]['oe_cx'] for y in range(2021,2026))
print('share of 20y capex-end total in 2021-2025: %.1f%%'%(100*step/tot))
sb=sum(rows[y]['sbc'] for y in rows); oc=sum(rows[y]['ocf'] for y in rows); print('SBC / OCF 20y %.1f%%'%(100*sb/oc))
cx=sum(rows[y]['capex'] for y in rows); dp=sum(rows[y]['dep'] for y in rows); print('capex/dep 20y %.2f'%(cx/dp))
for ys in [range(2021,2026),range(2016,2021),range(2006,2011),range(2011,2016)]:
    print(list(ys)[0],'capex/dep %.2f'%(sum(rows[y]['capex'] for y in ys)/sum(rows[y]['dep'] for y in ys)))
# per share at floor and sovereign
SH=221.181388
for v in [min(allv),max(allv)]:
    print('per share: OE %.1f -> floor10 $%.1f  sov $%.1f'%(v,v/0.10/SH,v/0.0549/SH))
print('growth needed to reach 10%% floor: %.1f to %.1f points'%(10-100*max(allv)/CAP,10-100*min(allv)/CAP))
