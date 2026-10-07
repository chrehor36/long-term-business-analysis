# Arithmetic for the LCII run of 2026-10-05. Sources: XBRL companyfacts (first-filed 10-K values),
# 10-K FY2008 (accession 0001144204-09-013467) for 2007-2008, FY2009 selected data for 2005-2009 sales.
sales={2005:669.1,2006:729.2,2007:668.6,2008:510.5,2009:397.8,2010:572.8,2011:681.2,2012:901.1,2013:1015.6,2014:1190.8,2015:1403.1,
 2016:1678.9,2017:2147.8,2018:2475.8,2019:2371.5,2020:2796.2,2021:4472.7,2022:5207.1,2023:3784.8,2024:3741.2,2025:4122.0}
op={2005:57.7,2006:55.3,2007:66.0,2008:19.9,2009:-35.6,2010:45.4,2011:48.5,2012:58.1,2013:78.3,2014:95.5,2015:116.3,2016:200.8,2017:214.3,
 2018:198.8,2019:200.2,2020:222.9,2021:398.4,2022:553.0,2023:123.4,2024:218.2,2025:279.9}
imp={2008:5.5,2009:45.0}
ocf={2007:84.9,2008:4.7,2009:63.3,2010:42.1,2011:36.8,2012:72.7,2013:82.7,2014:107.0,2015:95.0,2016:203.4,2017:155.1,2018:156.6,2019:269.5,2020:231.4,2021:-111.6,2022:602.5,2023:527.2,2024:370.3,2025:331.0}
sbc={2007:3.6,2008:3.6,2009:3.5,2010:4.2,2011:4.6,2012:6.3,2013:10.8,2014:10.8,2015:14.0,2016:15.4,2017:20.0,2018:14.1,2019:16.1,2020:18.5,2021:27.2,2022:23.7,2023:18.2,2024:18.7,2025:22.7}
capex={2007:8.8,2008:4.2,2009:3.1,2010:10.1,2011:24.3,2012:32.0,2013:32.6,2014:42.5,2015:29.0,2016:44.7,2017:87.2,2018:119.8,2019:58.2,2020:57.3,2021:98.5,2022:130.6,2023:62.2,2024:42.3,2025:52.6}
da={2007:17.6,2008:17.1,2009:18.5,2010:17.1,2011:20.5,2012:25.7,2013:27.5,2014:32.6,2015:41.6,2016:46.2,2017:54.7,2018:67.5,2019:75.4,2020:98.0,2021:112.3,2022:129.2,2023:131.8,2024:125.7,2025:121.2}
acq={2007:17.3,2008:31.8,2009:1.7,2010:21.9,2011:50.3,2012:1.5,2013:4.8,2014:106.8,2015:41.1,2016:48.7,2017:60.6,2018:184.8,2019:447.8,2020:182.1,2021:194.1,2022:108.5,2023:25.9,2024:20.0,2025:112.7}
div={2015:48.2,2016:34.4,2017:51.1,2018:59.3,2019:63.8,2020:70.4,2021:87.2,2022:102.7,2023:106.3,2024:109.5,2025:114.0}
bb={2018:28.7,2022:24.1,2025:128.6}
ttship={2007:261.7,2008:185.1,2009:138.8,2010:199.2,2011:212.9,2012:242.9,2013:268.0,2014:298.9,2015:314.4,2016:362.7,2017:429.5,2018:415.1,2019:349.5,2020:380.1,2021:531.2,2022:421.7,2023:259.1,2024:291.6,2025:298.2}
content={2006:1555,2007:1700,2008:1902,2009:2101,2010:2171,2011:2398,2012:2713,2013:2716,2014:2825,2015:2987,2016:3022,2017:3263,2018:3450,2019:3618,2020:3390,2021:4198,2022:6090,2023:5058,2024:5097,2025:5670}
patk_sales={2009:212.5,2010:278.2,2011:307.8,2012:437.4,2013:594.9,2014:735.7,2015:920.3,2016:1221.9,2017:1635.7,2018:2263.1,2019:2337.1,2020:2486.6,2021:4078.1,2022:4881.9,2023:3468.0,2024:3715.7,2025:3950.8}
patk_op={2009:1.3,2010:6.4,2011:13.5,2012:27.0,2013:40.9,2014:51.5,2015:69.9,2016:90.8,2017:121.9,2018:178.4,2019:154.4,2020:173.4,2021:351.7,2022:496.2,2023:260.2,2024:258.0,2025:276.0}
patk_gp={2009:22.9,2010:29.6,2011:44.3,2012:65.7,2013:91.0,2014:118.5,2015:152.3,2016:202.5,2017:278.9,2018:415.9,2019:422.9,2020:459.0,2021:801.2,2022:1059.9,2023:782.2,2024:835.9,2025:912.9}
lcii_gp={2009:78.7,2010:126.2,2011:139.7,2012:168.7,2013:213.1,2014:254.9,2015:306.0,2016:428.9,2017:493.1,2018:520.3,2019:539.2,2020:706.1,2021:1043.0,2022:1273.3,2023:776.2,2024:879.7,2025:980.3}
print("year sales opm% opm_ex_imp% OC_capex OC_DA acq OC-acq TTship content LCIIgm% PATKopm% PATKgm%")
oc={};ocd={}
for y in range(2005,2026):
    s=sales[y]; o=op[y]; oi=o+imp.get(y,0)
    line=f"{y} {s:7.1f} {100*o/s:5.1f} {100*oi/s:5.1f}"
    if y in ocf:
        oc[y]=ocf[y]-sbc[y]-capex[y]; ocd[y]=ocf[y]-sbc[y]-da[y]
        line+=f" {oc[y]:7.1f} {ocd[y]:7.1f} {acq[y]:6.1f} {oc[y]-acq[y]:7.1f} {ttship[y]:6.1f} {content[y]:5d}"
    if y in lcii_gp: line+=f" {100*lcii_gp[y]/s:5.1f} {100*patk_op[y]/patk_sales[y]:5.1f} {100*patk_gp[y]/patk_sales[y]:5.1f}"
    print(line)
def avg(d,ys): return sum(d[y] for y in ys)/len(ys)
W=range(2021,2026)
print("5yr avg OC capex",round(avg(oc,W),1),"D&A",round(avg(ocd,W),1),"acq",round(avg(acq,W),1))
for a,b in [(2009,2025),(2010,2025),(2016,2025)]:
    ys=range(a,b+1)
    print(f"span {a}-{b}: OC/sales {100*sum(oc[y] for y in ys)/sum(sales[y] for y in ys):.2f}%  OC-acq/sales {100*sum(oc[y]-acq[y] for y in ys)/sum(sales[y] for y in ys):.2f}%  opm {100*sum(op[y]+imp.get(y,0) for y in ys)/sum(sales[y] for y in ys):.2f}%  PATK opm {100*sum(patk_op[y] for y in ys)/sum(patk_sales[y] for y in ys):.2f}%")
print("mean TT shipments 2007-2025",round(avg(ttship,range(2007,2026)),1))
print("content CAGR 2007-2025", round(100*((content[2025]/content[2007])**(1/18)-1),2), " 2007-2019", round(100*((content[2019]/content[2007])**(1/12)-1),2))
print("sales CAGR 2007-2025", round(100*((sales[2025]/sales[2007])**(1/18)-1),2))
print("sum acq 2007-2025", round(sum(acq.values()),1), " 2016-2025", round(sum(acq[y] for y in range(2016,2026)),1))
print("sum OC 2016-2025", round(sum(oc[y] for y in range(2016,2026)),1), " div+bb 2016-2025", round(sum(div.get(y,0)+bb.get(y,0) for y in range(2016,2026)),1))
# valuation
r=0.0563; sh=24.311; price=82.60
def val(base,g,yrs=10):
    pv=0; c=base
    for t in range(1,yrs+1):
        c=c*(1+g); pv+=c/(1+r)**t
    term=c/r/(1+r)**yrs   # zero nominal growth after year ten
    return pv+term
cases={}
cases['no-growth capex']=val(avg(oc,W),0)
cases['no-growth D&A']=val(avg(ocd,W),0)
ws=sum(oc[y] for y in range(2009,2026))/sum(sales[y] for y in range(2009,2026))
ltm=4028.4
cases['whole-cycle no-growth (OC/sales 2009-2025 x LTM sales)']=val(ws*ltm,0)
ws2=sum(oc[y]-acq[y] for y in range(2009,2026))/sum(sales[y] for y in range(2009,2026))
cases['whole-cycle net of acquisitions, no-growth']=val(ws2*ltm,0)
cases['shown growth capped at the rate (5.63%), base net of acquisitions']=val(avg(oc,W)-avg(acq,W),r)
cases['shown growth capped at the rate, whole-cycle net-of-acq base']=val(ws2*ltm,r)
for k,v in cases.items(): print(f"{k:70s} {v:8.0f}M  ${v/sh:7.2f}/sh")
print("whole-cycle OC/sales",round(100*ws,2),"% ->",round(ws*ltm,1),"; net of acq",round(100*ws2,2),"% ->",round(ws2*ltm,1))
t=0.262
for nm,base in [('5yr capex',avg(oc,W)),('5yr D&A',avg(ocd,W)),('whole-cycle',ws*ltm),('whole-cycle net acq',ws2*ltm)]:
    pre=base/(1-t)
    print(f"{nm}: after-tax {base:.1f} pretax {pre:.1f}; pretax yield at price {100*pre/(price*sh):.2f}%; fair price (10% pretax, no growth) ${pre/0.10/sh:.2f}; cheap (15% pretax) ${pre/0.15/sh:.2f}")
# tangible capital returns
eq={2016:550.3,2019:800.7,2022:1381.0,2023:1355.0,2024:1386.9,2025:1360.8}
gw={2016:89.2,2019:351.1,2022:567.1,2023:589.5,2024:585.8,2025:622.2}
it={2016:112.9,2019:341.4,2022:503.3,2023:448.8,2024:392.0,2025:402.6}
debt={2016:50,2019:631,2022:1119,2023:847,2024:757,2025:945}
cash={2016:86.2,2019:35.4,2022:47.5,2023:66.2,2024:165.8,2025:222.6}
for y in eq:
    tc=eq[y]-gw[y]-it[y]+debt[y]-cash[y]; tot=eq[y]+debt[y]-cash[y]
    print(y,"tangible capital",round(tc),"pretax op/tc",round(100*(op[y]+imp.get(y,0))/tc,1),"% ; on total capital incl goodwill",round(100*op[y]/tot,1),"%")
