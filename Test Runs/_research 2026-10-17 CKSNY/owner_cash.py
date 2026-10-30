# Owner cash by year, GBP m, from the Group Statements of Cash Flows of the annual reports
# (AR2021 for 2020-2021, AR2023 for 2022, AR2024 for 2023, AR2025 for 2024-2025 as restated).
# OC = cash generated from operations - interest paid + interest received - tax paid
#      - PPE and intangible purchases + PPE/investment disposal proceeds - lease principal
#      - share-based payment charge (equity-settled, not added back explicitly in the reconciliation)
#      + JV dividends received - NCI share of profit after tax (CONVENTION of this run)
Y = {
 2020: dict(cgo=193.7, ip=18.9, ir=5.2, tax=27.5, capex=40.5, proc=1.1, lease=12.5, sbc=2.4, jv=2.3, nci=4.5, acq=1.4, tp=101.4, rev=1458.3, dep=50.6, esop=0.0),
 2021: dict(cgo=82.9, ip=11.9, ir=4.3, tax=30.1, capex=45.5, proc=1.2, lease=12.6, sbc=3.1, jv=1.0, nci=5.8, acq=43.7, tp=142.4, rev=1642.9, dep=49.8, esop=1.1),
 2022: dict(cgo=268.3, ip=15.6, ir=6.3, tax=47.9, capex=89.2, proc=3.1, lease=14.6, sbc=5.1, jv=1.3, nci=7.4, acq=3.5, tp=227.2, rev=2047.4, dep=55.5, esop=6.9),
 2023: dict(cgo=272.0, ip=16.8, ir=14.1, tax=52.8, capex=92.6, proc=5.4, lease=24.2, sbc=7.3, jv=1.0, nci=12.1, acq=0.0, tp=200.4, rev=1929.8, dep=57.8, esop=1.1),
 2024: dict(cgo=216.7, ip=23.9, ir=9.0, tax=46.1, capex=100.8, proc=4.7, lease=15.2, sbc=6.2, jv=0.7, nci=13.1, acq=0.0, tp=188.0, rev=1820.1, dep=62.2, esop=17.1),
 2025: dict(cgo=173.4, ip=23.7, ir=5.7, tax=38.8, capex=90.4, proc=10.6, lease=16.7, sbc=3.0, jv=0.9, nci=12.6, acq=38.9, tp=151.1, rev=1809.5, dep=65.8, esop=0.0),
}
T=0.25  # UK statutory rate, used only to put back the tax shield on interest for the all-equity basis
for y,d in Y.items():
    oc = d['cgo']-d['ip']+d['ir']-d['tax']-d['capex']+d['proc']-d['lease']-d['sbc']+d['jv']-d['nci']
    netint = d['ip']-d['ir']
    oc_ae = oc + netint*(1-T)
    oc_dep = oc + d['capex']-d['proc'] - d['dep']   # depreciation variant: depreciation in place of net capex
    d.update(oc=oc, oc_ae=oc_ae, oc_dep=oc_dep, oc_after_acq=oc-d['acq'], oc_ae_after_acq=oc_ae-d['acq'])
    print(y, f"rev {d['rev']:7.1f} TP {d['tp']:6.1f} OC(eq) {oc:6.1f} OC(all-eq) {oc_ae:6.1f} OCdepvar {oc_dep:6.1f} acq {d['acq']:5.1f} OC-acq(all-eq) {oc_ae-d['acq']:6.1f} capex-net {d['capex']-d['proc']:5.1f} dep {d['dep']}")
w=[2021,2022,2023,2024,2025]
avg=lambda k: sum(Y[y][k] for y in w)/5
for k in ('oc','oc_ae','oc_dep','oc_after_acq','oc_ae_after_acq','tp','rev'):
    print(k, round(avg(k),1))

# ---- 2016-2019 from the scanned filed accounts at Companies House (AR2017 for 2016-2017, AR2019 for 2018-2019).
# Pre-IFRS16 years (2016-2018): lease cost already inside cash generated from operations, lease=0.
# 2019: lease principal not separately shown in the cash flow statement (inside repayment of borrowings); estimated 12.0
# from the 2020-2021 level (a guess, disclosed). SBC 2016-2019 not read; estimated 3.0 a year (disclosed guess).
Y.update({
 2016: dict(cgo=130.2, ip=14.5, ir=2.4, tax=34.2, capex=31.3, proc=1.6, lease=0.0, sbc=3.0, jv=2.0, nci=6.3, acq=7.7, tp=133.3, rev=1401.4, dep=0.0),
 2017: dict(cgo=175.8, ip=15.6, ir=3.5, tax=38.2, capex=39.0, proc=1.8, lease=0.0, sbc=3.0, jv=1.7, nci=6.4, acq=0.0, tp=165.5, rev=1683.9, dep=0.0),
 2018: dict(cgo=195.2, ip=16.3, ir=4.8, tax=41.8, capex=41.2, proc=2.6, lease=0.0, sbc=3.0, jv=1.2, nci=6.8, acq=1.0, tp=197.2, rev=1798.0, dep=0.0),
 2019: dict(cgo=240.7, ip=17.3, ir=5.2, tax=44.5, capex=65.4, proc=5.5, lease=12.0, sbc=3.0, jv=0.1, nci=6.2, acq=25.9, tp=181.4, rev=1710.4, dep=0.0),
})
print("\n--- full series")
for y in sorted(Y):
    d=Y[y]
    oc = d['cgo']-d['ip']+d['ir']-d['tax']-d['capex']+d['proc']-d['lease']-d['sbc']+d['jv']-d['nci']
    netint=d['ip']-d['ir']; d['oc']=oc; d['oc_ae']=oc+netint*(1-T); d['oc_ae_acq']=d['oc_ae']-d['acq']
    print(y, f"TP {d['tp']:6.1f} OC(eq) {oc:6.1f} OC(all-eq) {d['oc_ae']:6.1f} after acq {d['oc_ae_acq']:6.1f} RoS {d['tp']/d['rev']*100:4.1f}%")
def avg(ys,k): return sum(Y[y][k] for y in ys)/len(ys)
for name,ys in (("window 2021-25",range(2021,2026)),("cycle 2018-25",range(2018,2026)),("ten yrs 2016-25",range(2016,2026))):
    print(name, "OC_ae", round(avg(ys,'oc_ae'),1), "OC_ae after acq", round(avg(ys,'oc_ae_acq'),1), "OC eq", round(avg(ys,'oc'),1))
# growth between halves (b): window
h1=avg([2021,2022],'oc_ae_acq'); h2=avg([2024,2025],'oc_ae_acq'); print("halves 21-22 vs 24-25 (after acq):",round(h1,1),round(h2,1))
c1=avg(range(2016,2021),'oc_ae_acq'); c2=avg(range(2021,2026),'oc_ae_acq'); print("successive five-yr blocks 2016-20 vs 2021-25 (after acq):",round(c1,1),round(c2,1), "rate/yr", round(((c2/c1)**(1/5)-1)*100,2) if c1>0 and c2>0 else None)
s1=avg(range(2016,2021),'rev'); s2=avg(range(2021,2026),'rev'); print("sales blocks", round(s1,1), round(s2,1), "rate/yr", round(((s2/s1)**(1/5)-1)*100,2))
